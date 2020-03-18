import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func  time :',ts)

def func2():
    #耗时2S
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：',ts)

def dojob():
    #创建调度器：BlockingScheduler
    #scheduler = BlockingScheduler()
    scheduler = BackgroundScheduler()
    #添加任务,时间间隔2S
    scheduler.add_job(func, 'interval', seconds=2)
    #添加任务,时间间隔5S
    scheduler.add_job(func2, 'interval', seconds=4)
    scheduler.start()
dojob()
