#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, jsonify, url_for
from werkzeug.utils import redirect
from common.Logger import Logger

light_blue = Blueprint('light', __name__)
log = Logger(loggername='lightBlue')

@light_blue.route('/light/index')
def lightIndex():
    return render_template('light-index.html')