from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
import logging
import datetime

# create a scheduler
s = Scheduler()

# This is what I want to happen
def job():

	logging.basicConfig(filename='scheduled_task.log',level=logging.INFO,
 					format='%(asctime)s %(message)s line: %(lineno)d')

	try:
		logging.info( "scheduled event")
	except Exception as e:
		print("open file failed")

def main():
	newTime = datetime.datetime.now() + datetime.timedelta(seconds = 2)
	s.add_job(job, 'cron',  hour='0-23')
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


# Running a python script with python script & will fork that process immediately, so you can close the terminal. 