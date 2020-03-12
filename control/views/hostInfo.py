#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, url_for, jsonify, session, g
from werkzeug.utils import redirect
from model.User import User
from common.form import LoginForm
from common.Logger import Logger

host_blue = Blueprint('host', __name__)
log = Logger(loggername='loginBlue')


@host_blue.route('/host/hostInfe')
def hostInfo():
    result = {}
    result['hostname'] = "node1"
    result['mem'] = "1"
    result['core'] = "10"
    result['disk'] = "100"
    return jsonify(result)
