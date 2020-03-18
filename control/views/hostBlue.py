#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, jsonify, render_template, request

from common import timeUtil
from common.Logger import Logger
from model.HostModel import HostInfoModel

hostInfo_blue = Blueprint('hostInfo', __name__)
log = Logger(loggername='loginBlue')


@hostInfo_blue.route('/host/hostsInfo')
def hostsInfo():
    isLine = request.args.get('line', 0)
    result = HostInfoModel.query.with_entities(HostInfoModel.id, HostInfoModel.host_name,
                                               HostInfoModel.host_total_memory, HostInfoModel.host_ip,
                                               HostInfoModel.host_total_cpu, HostInfoModel.host_total_disk,
                                               HostInfoModel.update_time)
    for node in result:
        if str(node.update_time) > timeUtil.getTime(reduce=10):
            for key in node:
                print(node.get('key'))
            node.setStatus(status='online')
            # node.append({'status', 'online'})
            continue
        for key, value in node:
            print(key, value)
        node.setStatus(status='offline')
        # node.append({'status', 'offline'})

    if isLine is None or isLine == "0":
        return render_template('hostsinfo.html', result=result), 200
    elif isLine == "1":
        return render_template('hostsinfo.html', result=result), 200
    else:
        return render_template('hostsinfo.html', result=result), 200


@hostInfo_blue.route('/host/hostInfo')
def hostInfo():
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
