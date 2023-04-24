from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import main

scheduler = BlockingScheduler()

def my_cron_job():
    now = datetime.now()
    print("Cron job ran at {}".format(now))
    main.run()

scheduler.add_job(my_cron_job, 'interval', hours=1)

if __name__ == '__main__':
    scheduler.start()
