from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler

def tick1():
    print('Tick1! The time is: %s'% datetime.now())
def tick2():
    time.sleep(4)
    print('Tick2! The time is: %s' % datetime.now())
if __name__=='__main__':
    scheduler=BackgroundScheduler()
    scheduler.add_job(tick1,'interval',seconds = 3)
    scheduler.add_job(tick2, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break'if os.name== 'nt'else 'C'))
    try:
#  This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except(KeyboardInterrupt,SystemExit):
#  Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
