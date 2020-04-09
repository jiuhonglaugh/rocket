#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import Thread
import requests

from common import timeUtil
from common.timeUtil import sleep


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def agentTask():
    # 启动定时器任务，每 十 秒执行一次
        try:
            headers = {'content-type': 'application/json',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
            result = requests.get(url='http://127.0.0.1:80/agent/base', headers=headers)
            print(result.text, timeUtil.getTime())
        except:
            print('系统还未初始化', timeUtil.getTime())
