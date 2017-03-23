from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from custom_logging import get_logger
import datetime
import random
import pytz	

from auto_scrape import scrape

# create a scheduler
s = Scheduler()


# This is what I want to happen
# I define a function that will the job I want to run. I supply that function to the add_job for scheduler

def job():
	
	logger = get_logger()

	logger.info('Starting scrape job')	
	try:	
		scrape()
	except Exception as e:
		logger.error("Exception caught inside job" + str(e))

	logger.info('Ending scrape job')
def main():
	
	logger = get_logger()

	# this actually creates the job and background scheduler for it
	randHour = random.randrange(2,6)
	randMin = random.randrange(0, 60, 5)
	'''logger.info('Scrape scheduled with random time: ' + str(randHour) + ':' + str(randMin)) 
	s.add_job(job, 'cron', hour=randHour, minute=randMin, timezone=pytz.timezone('US/Central'))'''
	s.add_job(job, 'date')	

	s.start()

	try:
    # This is here to simulate application activity (which keeps the main thread alive).
		while True:
			sleep(2)

	except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
		s.shutdown()

if __name__ == "__main__":
	main()

