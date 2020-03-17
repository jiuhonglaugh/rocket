#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, url_for, jsonify, session, g
from werkzeug.utils import redirect
from model.UserModel import User
from common.form import LoginForm
from common.Logger import Logger

login_blue = Blueprint('login', __name__)
log = Logger(loggername='loginBlue')


@login_blue.route('/')
def default():
    return render_template('login.html', form=LoginForm())


@login_blue.route('/index')
def index():
    username = session.get('user_name')
    if username is None:
        return render_template('login.html', form=LoginForm())
    return render_template('index.html', username=username)


@login_blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm(request.form)
        if form.validate_on_submit():
            result = {}
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(user_name=username).first()
            if user is None:
                log.info('{} 用户不存在'.format(username))
                result['code'] = 400
                result['data'] = '用户不存在'
            elif not user.verify_password(user_pwd=password):
                log.warn('用户 {} 登录失败'.format(username))
                result['code'] = 300
                result['data'] = '密码错误'
            else:
                log.info('用户 {} 登录成功'.format(username))
                # session.permanent = True
                session['user_name'] = user.user_name
                result['code'] = 200
                result['data'] = '登陆成功'
            return jsonify(result)
        return render_template('login.html', form=form)


@login_blue.route('/logout/')
def logout():
    log.info('{} 用户退出登录'.format(session['user_name']))
    session['user_name'] = None
    g.user = None
    return redirect(url_for('login.index'))
