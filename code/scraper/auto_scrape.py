
import newspaper
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import func
import nltk
from random import randint
from time import sleep
import json
import sys
from custom_logging import get_logger 

def scrape():
	# log errors to a log file in this directory
	
	logging = get_logger()

	host = 'localhost'
	dbname = 'cap'
	user = 'postgres'
	password = 'secret'

	try:
		# create a sqlalchemy engine that connects to our db
		engine = create_engine('postgresql://' + user + ':' + password + '@' + host + '/' + dbname)
		# get the metadata describing our database structure
		meta = sqlalchemy.MetaData(bind=engine, reflect=True)
		# build an object representing the specified table so we can interact with it
		table = meta.tables['articles']
	except Exception as e:
		logging.error("::Exception:Failed to create sqlalchemy objects::")
		logging.error("::Exception: " + str(e) + "::")
		sys.exit(1)

	# get dictionary of sites to scrap from file
	try:
		with open('site_list.json') as json_data:
			site_list = json.load(json_data)
	except Exception as e:
		logging.error("::Exception:Failed to load site list json::")
		logging.error("::Exception: " + str(e) + "::")
		sys.exit(1)

	logging.info("_________SCRIPT START________" + str(func.current_timestamp()))
	for site in site_list:
		name = site['name']
		url = site['url']
		# if a site should throw an exception for any reason (maybe bad url), catch it, pass, and move to next site
		try:
			paper = newspaper.build(url,
									keep_article_html=True,
									fetch_images=False,
									memoize_articles=True,	# track the articles we have already scraped from session to session
									MIN_WORD_COUNT=200,		# this doesn't seem to be having any affect
									number_threads=2,
									request_timeout=12,
									thread_timeout=3)
			total = paper.size()
			numScraped = total

			htmls = []
			titles = []
			urls = []
			authors = []
			published_dates = []
			texts = []
			keywords = []	# keywords according to newspaper's nlp functionality
			summaries = []	# summary according to newspaper's nlp functionality
			logging.error('Test error to log before looks at scraped articles')
			for x in range(0,numScraped):
				sleep(randint(3,6))
				if paper.articles[x] != None:
					paper.articles[x].download()
					if paper.articles[x].is_downloaded:
						if paper.articles[x].html != None:
							paper.articles[x].parse()
							# Ensure article is long enough to be valid
							if len(nltk.word_tokenize(paper.articles[x].text)) > 200:
								htmls.append(paper.articles[x].article_html.replace('\n', ' '))
								titles.append(paper.articles[x].title)
								urls.append(paper.articles[x].url)
								published_dates.append(paper.articles[x].publish_date)
								authors.append(paper.articles[x].authors)
								texts.append(paper.articles[x].text.replace('\n', ' '))
								paper.articles[x].nlp()
								keywords.append(paper.articles[x].keywords)
								summaries.append(paper.articles[x].summary)
			for i in range(0, len(titles)-1):
				# catch cases in which there is no primary author
				# chose not to log the errors regarding authors because this will probably be common
				try:
					primary_author = authors[i][0]
				except IndexError as ie:
					primary_author = None
					pass
				# if the secondary authors list is too long there was some sort of parsing problem, so throw them away to avoid insertion errors
				try:
					if sum([len(author) for author in authors[i][1:]]) > 100:
						authors[i][1:] = []
				except IndexError as ie:
					authors[i] = []
					pass
				try:
					insert = table.insert().values(site=name,
											title=titles[i],
											author=primary_author,
											secondary_authors=authors[i][1:],
											published_on=published_dates[i],
											accessed_on=func.current_timestamp(),
											url=urls[i],
											body=texts[i],
											html=htmls[i],
											newspaper_keywords=keywords[i],
											newspaper_summary=summaries[i])
					engine.execute(insert)
				except Exception as e:
					logging.error("::Exception:Database insertion error for page: " + url + "::")
					logging.error("::Exception: " + str(e) + "::")
					pass
		except Exception as e:
			logging.error("::Exception:Scrapping error for site: " + name + "::")
			logging.error("::Exception: " + str(e) + "::")
	logging.info("_________SCRIPT FINISHED________" + str(func.current_timestamp()))
