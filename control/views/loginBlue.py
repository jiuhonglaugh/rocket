#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, request, url_for, session, g
from werkzeug.utils import redirect
from control.manager.loginManager import verifyLogin, cklogin
from common.form import LoginForm
from common.Logger import Logger

login_blue = Blueprint('login', __name__)
log = Logger(loggername='loginBlue')


@login_blue.route('/')
def default():
    return render_template('login.html', form=LoginForm())


@login_blue.route('/index')
@cklogin()
def index():
    pass


@login_blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    form = LoginForm(request.form)
    loginResult = verifyLogin(form)
    if loginResult is not None:
        return loginResult
    return render_template('login.html', form=form)


@login_blue.route('/logout/')
def logout():
    log.info('{} 用户退出登录'.format(session['user_name']))
    session['user_name'] = None
    g.user = None
    return redirect(url_for('login.index'))
