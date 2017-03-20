import newspaper as newspaper
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import select, text

host = 'localhost'
dbname = 'capstone'
user = 'postgres'
password = 'testPass'

try:
	engine = create_engine('postgresql://' + user + ':' + password + '@' + host + '/' + dbname)

	conn = engine.connect()
except:
	print("error with database")


s = select([text('* FROM articles')]) 

result = conn.execute(s)

i = 0

for row in result:
	print(row['html'])
	print(i)
	i+=1