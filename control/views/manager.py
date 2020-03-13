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


@manager_blue.route('/echart/')
def echart():
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


@manager_blue.route('/discount/')
def discount():
    title = ['hadoop01', 'hadoop02', 'hadoop03', 'hadoop04', 'hadoop05']
    time = [getTime(format='%H:%M:%S', reduce=30), getTime(format='%H:%M:%S', reduce=25),
            getTime(format='%H:%M:%S', reduce=20), getTime(format='%H:%M:%S', reduce=15),
            getTime(format='%H:%M:%S', reduce=10), getTime(format='%H:%M:%S', reduce=10),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S'),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S')]
    jsondata = {}
    jsondata['title'] = title
    jsondata['time'] = time
    for node in title:
        jsondata[node + '_data'] = getData()
    return jsonify(jsondata), 200


def getRandom():
    return random.randint(10, 30)


def getData():
    return [random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99),
            random.randint(50, 99), random.randint(50, 99), random.randint(50, 99),
            random.randint(50, 99), random.randint(50, 99), random.randint(50, 99)]
