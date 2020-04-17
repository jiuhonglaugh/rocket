#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from flask import Blueprint, render_template, request, jsonify, url_for
from werkzeug.utils import redirect
from common.Logger import Logger
from control.form import MysqlForm, RedisForm
from control.manager.lightManager import testAndSaveMysql, testAndSaveRedis

light_blue = Blueprint('light', __name__)
log = Logger(loggername='lightBlue')


@light_blue.route('/light/add-mysql', methods=['GET', 'POST'])
def lightAddMysql():
    if request.method == 'GET':
        form = MysqlForm(request.form)
        return render_template('light-add-mysql.html', form=form)
    else:
        form = MysqlForm(request.form)
        result = testAndSaveMysql(form)
        return result

@light_blue.route('/light/add-redis', methods=['GET', 'POST'])
def lightAddRedis():
    if request.method == 'GET':
        form = RedisForm(request.form)
        return render_template('light-add-redis.html', form=form)
    else:
        form = RedisForm(request.form)
        result = testAndSaveRedis(form)
        return result