#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, url_for, jsonify, session, g
from werkzeug.utils import redirect
from model.User import User
from common.form import LoginForm
from common.Logger import Logger

login_blue = Blueprint('login', __name__)
log = Logger(loggername='loginBlue')


@login_blue.route('/')
def default():
    # username = session.get('username')
    # if username is None:
    #     return render_template('login.html', form=LoginForm())
    return render_template('index.html')


@login_blue.route('/index')
def index():
    username = session.get('username')
    if username is None:
        return render_template('login.html',form=LoginForm())
    return render_template('index.html')


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
            user = User.query.filter_by(name=username).first()
            if user is None:
                log.warn('{} 用户不存在'.format(username))
                result['code'] = 400
                result['data'] = '用户不存在'
            elif user.verify_password(password=password):
                log.info('用户 {} 登录成功'.format(username))
                session.permanent = True
                session['username'] = user.name
                result['code'] = 200
                result['data'] = '登陆成功'
                return redirect(url_for('index'))
            else:
                log.warn('用户 {} 登录失败'.format(username))
                result['code'] = 300
                result['data'] = '密码错误'
            return jsonify(result)
        return render_template('login.html', form=form)


@login_blue.route('/logout/')
def logout():
    session['user_id'] = None
    g.user = None
    return redirect(url_for('login'))
