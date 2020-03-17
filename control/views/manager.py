#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

from flask import Blueprint, jsonify, render_template
from common.timeUtil import getTime
from common.Logger import Logger

manager_blue = Blueprint('manager', __name__)
log = Logger(loggername='manager')


# src="templates/welcome.html"
@manager_blue.route('/manager/')
def mnager():
    return render_template('welcome.html')


@manager_blue.route('/mem/')
def mem():
    x = []
    y = []
    x.append('hadoop01')
    y.append(getRandom())
    x.append('hadoop01')
    y.append(getRandom())
    x.append('hadoop03')
    y.append(getRandom())
    x.append('hadoop04')
    y.append(getRandom())
    x.append('hadoop05')
    y.append(getRandom())
    jsondata = {}
    jsondata['xdays'] = x
    jsondata['yvalues'] = y
    return jsonify(jsondata), 200


'''
折线图需要三种数据
第一 title 对应折线图上方显示的 标题数据
第二 time  对应折线图下方显示的 时间数据
第三 data  对应折现图中显示的   结果数据
time 和 data 中的数据数量一致否则显示会缺失
'''


@manager_blue.route('/core/')
def core():
    title = ['hadoop01', 'hadoop02', 'hadoop03', 'hadoop04', 'hadoop05']
    time = [getTime(format='%H:%M:%S', reduce=30), getTime(format='%H:%M:%S', reduce=25),
            getTime(format='%H:%M:%S', reduce=20), getTime(format='%H:%M:%S', reduce=15),
            getTime(format='%H:%M:%S', reduce=10), getTime(format='%H:%M:%S', reduce=10),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S'),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S')]
    jsondata = {'title': title, 'time': time}
    data = []
    for node in title:
        data.append({'name': node, 'type': 'line', 'stack': '总量', 'data': getData()})
    jsondata['data'] = data
    return jsonify(jsondata), 200


@manager_blue.route('/disk/')
def disk():
    x = []
    y = []
    x.append('hadoop01')
    y.append(getRandom(40,50))
    x.append('hadoop01')
    y.append(getRandom(40,50))
    x.append('hadoop03')
    y.append(getRandom(40,50))
    x.append('hadoop04')
    y.append(getRandom(40,50))
    x.append('hadoop05')
    y.append(getRandom(40,50))
    jsondata = {}
    jsondata['xdays'] = x
    jsondata['yvalues'] = y
    return jsonify(jsondata), 200


'''
折线图需要三种数据
第一 title 对应折线图上方显示的 标题数据
第二 time  对应折线图下方显示的 时间数据
第三 data  对应折现图中显示的   结果数据
time 和 data 中的数据数量一致否则显示会缺失
'''


@manager_blue.route('/net/')
def net():
    title = ['hadoop01', 'hadoop02', 'hadoop03', 'hadoop04', 'hadoop05']
    time = [getTime(format='%H:%M:%S', reduce=30), getTime(format='%H:%M:%S', reduce=25),
            getTime(format='%H:%M:%S', reduce=20), getTime(format='%H:%M:%S', reduce=15),
            getTime(format='%H:%M:%S', reduce=10), getTime(format='%H:%M:%S', reduce=10),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S'),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S')]
    jsondata = {'title': title, 'time': time}
    data = []
    for node in title:
        data.append({'name': node, 'type': 'line', 'stack': '总量', 'data': getData()})
    jsondata['data'] = data
    return jsonify(jsondata), 200


def getRandom(start=50, end=100):
    return random.randint(start, end)


def getData():
    return [random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99),
            random.randint(50, 99), random.randint(50, 99), random.randint(50, 99),
            random.randint(50, 99), random.randint(50, 99), random.randint(50, 99)]
