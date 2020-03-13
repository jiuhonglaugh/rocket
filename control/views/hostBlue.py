#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, jsonify, render_template, request

from common.Logger import Logger

hostInfo_blue = Blueprint('hostInfo', __name__)
log = Logger(loggername='loginBlue')


@hostInfo_blue.route('/host/hostsInfo')
def hostsInfo():
    result = []
    for num in range(10):
        data = {}
        data['id'] = num + 1
        if num % 2 == 0:
            data['online'] = 'yes'
        else:
            data['online'] = 'no'
        data['hostname'] = 'hadoop0' + str(num + 1)
        data['ip'] = '172.10.44.22' + str(num + 1)
        data['os'] = 'rehad 7.' + str(num + 1)
        data['core'] = num
        data['mem'] = num
        data['disk'] = num
        result.append(data)
    return render_template('hostsinfo.html', result=result)


@hostInfo_blue.route('/host/hostInfo')
def hostInfo():
    hostName = request.args.get('hostname')
    result = []
    for num in range(10):
        data = {}
        data['hostname'] = 'hadoop0' + str(num + 1)
        data['ip'] = '172.10.44.22' + str(num + 1)
        data['os'] = 'rehad 7.' + str(num + 1)
        data['core'] = num
        data['mem'] = num
        data['disk'] = num
        result.append(data)
    return render_template('hostinfo.html', result=result)
