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
		scrape(logger)
	except Exception as e:
		logger.error("Exception caught inside job " + str(e))
		pass
	logger.info('Ending scrape job')
def main():
	
	logger = get_logger()

	
	logger.info('Scrape scheduled with time: ' + str(3) + ':' + str(30)) 
	s.add_job(job, 'cron', hour=3, minute=30, timezone=pytz.timezone('US/Central'))

	# I am keeping this here because I use it anytime we need to test run the scheduler
	# schedules a job for now
	# s.add_job(job, 'date')	

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

