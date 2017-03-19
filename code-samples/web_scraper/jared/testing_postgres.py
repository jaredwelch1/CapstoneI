import newspaper as newspaper
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

try:
	conn_string = "host='localhost' dbname='capstone' user='postgres' password='testPass'"
	conn = psycopg2.connect(conn_string)
except:
	print("error??")


'''
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
'''