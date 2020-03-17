#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import datetime


def getTime(format='%Y-%m-%d %H:%M:%S', reduce=0):
    return time.strftime(format, time.localtime(time.time() - reduce))


def sleep(mm):
    time.sleep(mm)


def sessionTimeOut(minutes):
    return datetime.timedelta(minutes=minutes)





if __name__ == '__main__':
    print(getTime(reduce=10) < getTime())
