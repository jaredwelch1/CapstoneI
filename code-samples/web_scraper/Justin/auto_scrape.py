import newspaper
from newspaper import Config
import psycopg2
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import func
from random import randint
from time import sleep
import json
import sys

host = 'localhost'
dbname = 'justin'
user = 'justin'
password = '123'

conn_string = "host='"+host+"' dbname='"+dbname+"' user='"+user+"' password='"+password+"'"
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print("Connected!\n")

# create a sqlalchemy engine that connects to our db
engine = create_engine('postgresql://' + user + ':' + password + '@localhost:5432/' + dbname)
# get the metadata describing our database structure
meta = sqlalchemy.MetaData(bind=engine, reflect=True)
# build an object representing the specified table so we can interact with it
table = meta.tables['articles']

# get dictionary of sites to scrap from file
with open('site_list.json') as json_data:
	site_list = json.load(json_data)

for site in site_list:
	name = site['name']
	url = site['url']
	print ('Building newspaper tree for '+ url + '...\n')
	paper = newspaper.build(url,
							keep_article_html=True,
							fetch_images=False,
							memoize_articles=False,	# track the articles we have already scraped from session to session
							MIN_WORD_COUNT=200,		# this doesn't seem to be having any affect
							number_threads=2,
							request_timeout=12,
							thread_timeout=3)
	total = paper.size()
	print('Number of articles: ' + str(total))
	numScraped = 5

	htmls = []
	titles = []
	urls = []
	authors = []
	published_dates = []
	texts = []
	keywords = []	# keywords according to newspaper's nlp functionality
	summaries = []	# summary according to newspaper's nlp functionality

	for x in range(0,numScraped):
		sleep(randint(3,6))
		if paper.articles[x] != None:
			paper.articles[x].download()
			if paper.articles[x].is_downloaded:
				if paper.articles[x].html != None:
					paper.articles[x].parse()
					htmls.append(paper.articles[x].article_html.replace('\n', ' '))
					titles.append(paper.articles[x].title)
					urls.append(paper.articles[x].url)
					published_dates.append(paper.articles[x].publish_date)
					authors.append(paper.articles[x].authors)
					texts.append(paper.articles[x].text.replace('\n', ' '))
					print ('Article ' + str(x + 1) + ' done\n')
				paper.articles[x].nlp()
				keywords.append(paper.articles[x].keywords)
				summaries.append(paper.articles[x].summary)

	for i in range(0, len(titles)-1):
		# catch cases in which there is no primary author
		try:
			primary_author = authors[i][0]
		except IndexError:
			primary_author = None
		# if the secondary authors list is too long there was some sort of parsing problem, so throw them away
		if sum([len(c) for c in authors[i][1:]]) > 100:
			authors[i][1:] = []
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

conn.close()
