import newspaper
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
conn_string = "host='localhost' dbname='postgres' user='postgres' password='secret'"
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()

print("Connected!\n")
url = 'http://cnn.com'
print ('Building newspaper tree...\n')
paper = newspaper.build(url, memoize_articles=False)
total = paper.size()
numScraped = 10

#make a DF and arrays for temp storage
cols = ['titles', 'urls', 'authors', 'texts']
df = pd.DataFrame(data=None, columns=cols)
titles = []
urls = []
authors = []
texts = []

for x in range(0,numScraped):
	if paper.articles[x] != None:
		paper.articles[x].download()
		if paper.articles[x].is_downloaded:
			if(paper.articles[x].html != None):
				paper.articles[x].parse()
			if paper.articles[x].title != None:
				titles.append(paper.articles[x].title)
				#file.write(str(x)+',"' + paper.articles[x].title+ '"\n')
			if paper.articles[x].url != None:
				urls.append(paper.articles[x].url)
			if paper.articles[x].authors != None:
				authors.append(paper.articles[x].authors)
			if paper.articles[x].text != None:
				texts.append(paper.articles[x].text.replace('\n', ' '))
				print ('Article ' + str(x) + ' done\n')

df.titles = list(titles)
df.urls = list(urls)
df.authors = list(authors)
df.texts = list(texts)
engine = create_engine('postgresql://postgres:secret@localhost:5432/postgres')
df.to_sql('test_a', engine,if_exists='replace')
conn.close()
print(df)
