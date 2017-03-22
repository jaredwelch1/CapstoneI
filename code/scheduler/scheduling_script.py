import sys
sys.path.insert(0, '../scraper/')
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
import logging
import datetime
import random

from auto_scrape import scrape

# create a scheduler
s = Scheduler()

# create logging config
logging.basicConfig(filename='scheduler.log',level=logging.INFO,
	 					format='%(asctime)s %(message)s line: %(lineno)d')

# This is what I want to happen
# I define a function that will the job I want to run. I supply that function to the add_job for scheduler

def job():
	logging.info('Starting scrape job')	
	scrape('../scraper/site_list.json')
	logging.info('Ending scrape job')

def main():
	# this actually creates the job and background scheduler for it
	randHour = random.randrange(2,6)
	randMin = random.randrange(0, 60, 5)
	logging.info('Scrape scheduled with random time: ' + str(randHour) + ':' + str(randMin)) 
	s.add_job(job, 'cron', hour=randHour, minute=randMin)
	
	s.start()

	try:
    # This is here to simulate application activity (which keeps the main thread alive).
		while True:
			sleep(2)

	except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
		scheduler.shutdown()

if __name__ == "__main__":
	main()

