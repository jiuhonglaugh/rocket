#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, jsonify, url_for
from werkzeug.utils import redirect
from common.Logger import Logger
from control.manager.hostManager import getDisk, getNet, getCore, getMem, getHostsInfo, getHostInfo
from control.manager.loginManager import cklogin

hostInfo_blue = Blueprint('host', __name__)
log = Logger(loggername='hostBlue')


@hostInfo_blue.route('/host/hostsInfo')
def hostsInfo():
    isLine = request.args.get('line', '0')
    dtList = getHostsInfo(isLine)
    return render_template('hostsinfo.html', result=dtList), 200


@hostInfo_blue.route('/host/hostInfo')
def hostInfo():
    hostId = request.args.get('hostId')
    result = getHostInfo(hostId)
    if result is not None:
        return render_template('hostinfo.html', result=result)
    log.warn('传入要查询的主机 ID 不存在 ：{}'.format(hostId))
    return redirect(url_for('login.index'))


@hostInfo_blue.route('/host/index')
def mnager():
    return render_template('welcome.html')


@hostInfo_blue.route('/host/mem/')
def mem():
    dict = getMem()
    return jsonify(dict), 200


'''
折线图需要三种数据
第一 title 对应折线图上方显示的 标题数据
第二 time  对应折线图下方显示的 时间数据
第三 data  对应折现图中显示的   结果数据
time 和 data 中的数据数量一致否则显示会缺失
'''


@hostInfo_blue.route('/host/core/')
def core():
    jsondata = getCore()
    return jsonify(jsondata), 200


@hostInfo_blue.route('/host/disk/')
def disk():
    jsondata = getDisk()
    return jsonify(jsondata), 200


@hostInfo_blue.route('/host/net/')
def net():
    jsondata = getNet()
    return jsonify(jsondata), 200
