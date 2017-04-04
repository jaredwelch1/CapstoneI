
import newspaper
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import func
import nltk
from random import randint
from time import sleep, time
import json
import sys, os
from custom_logging import get_logger 

def scrape(logging):
	
	start = time()

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
	for site in site_list:
		child_id = os.fork()

		if child_id == 0:			
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
				authors = []
				secondAuth = ''
			
				for x in range(0,numScraped):
					sleep(randint(3,6))
					if paper.articles[x] != None:
						paper.articles[x].download()
						if paper.articles[x].is_downloaded:
							if paper.articles[x].html != None:
								paper.articles[x].parse()
								# Ensure article is long enough to be valid
								if len(nltk.word_tokenize(paper.articles[x].text)) > 200:
									html = paper.articles[x].article_html.replace('\n', ' ')
									title = (paper.articles[x].title)
									url = paper.articles[x].url
									published_date = paper.articles[x].publish_date
									authors = paper.articles[x].authors
									text = paper.articles[x].text.replace('\n', ' ')
									paper.articles[x].nlp()
									keywords = paper.articles[x].keywords
									summary = paper.articles[x].summary
									try:
										primary_author = str(authors[0])
									except IndexError as ie:
										primary_author = None
										pass
									# if the secondary authors list is too long there was some sort of parsing problem, so throw them away to avoid insertion errors
									try:
										if sum([len(author) for author in authors[1:]]) > 100:
											secondAuth = ''
										else:
											secondAuth = str(authors[1:])
									except IndexError as ie:
										pass
									try:
										insert = table.insert().values( 
											site=name, 
											title=title, 
											author=primary_author,
											secondary_authors=secondAuth,
											published_on=published_date,
											accessed_on=func.current_timestamp(),
											url=url,
											body=text,
											html=html,
											newspaper_keywords=keywords,
											newspaper_summary= 	
											summary)					
										engine.execute(insert)
									except Exception as e:
										logging.error("::Exception:Database insertion error for page: " + url + "::")
										logging.error("::Exception: " + str(e) + "::")
										pass
			except Exception as e:
				logging.error("::Exception:Scrapping error for site: " + name + "::")
				logging.error("::Exception: " + str(e) + "::")
				pass
			os._exit(0)
		else:
			pid, status = os.waitpid(child_id, 0)
	end = time()
	logging.info("___________Scraper took " + str(end - time) + " seconds_____________")
