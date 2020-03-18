#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import decimal

from flask import Blueprint, render_template, request
from common import timeUtil, ModelUtil
from common.Logger import Logger
from model.HostModel import HostInfoModel

hostInfo_blue = Blueprint('hostInfo', __name__)
log = Logger(loggername='loginBlue')


@hostInfo_blue.route('/host/hostsInfo')
def hostsInfo():
    isLine = request.args.get('line', '0')
    result = HostInfoModel.query.with_entities(HostInfoModel.id, HostInfoModel.host_name,
                                               HostInfoModel.host_total_memory, HostInfoModel.host_ip,
                                               HostInfoModel.host_total_cpu, HostInfoModel.host_total_disk,
                                               HostInfoModel.update_time)
    dtList = ModelUtil.toDictAll(result)
    for i in range(len(dtList) - 1, -1, -1):
        dtList[i]['host_os'] = 'CentOS Linux release 7.7.1908 (Core)'
        if str(dtList[i]['update_time']) > timeUtil.getTime(reduce=10):
            dtList[i]['status'] = 'online'
        else:
            dtList[i]['status'] = 'offline'
        if isLine == "1" and dtList[i]['status'] == 'offline':
            dtList.pop(i)
        elif isLine == "2" and dtList[i]['status'] == 'online':
            dtList.pop(i)
    return render_template('hostsinfo.html', result=dtList), 200


@hostInfo_blue.route('/host/hostInfo')
def hostInfo():
    hostId = request.args.get('hostId')
    if hostId is None:
        log.warn('传入要查询的主机 ID 不存在 ：{}'.format(hostId))

    res = HostInfoModel.query_by_hostsID(hostId)
    result = ModelUtil.toDict(res, res.__class__)

    result['host_os'] = 'CentOS Linux release 7.7.1908 (Core)'
    return render_template('hostinfo.html', result=result)
