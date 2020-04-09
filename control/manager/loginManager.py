#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import wraps
from flask import jsonify, session, render_template
from common.Logger import Logger
from control.form import LoginForm
from control.model.UserModel import User

log = Logger(loggername='loginManager')


def verifyLogin(form):
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
    return None


# 验证登录的修饰器
def cklogin(**kw):
    def ck(func):
        @wraps(func)
        def _ck(*args, **kwargs):
            username = session.get('user_name')
            if username is None:
                return render_template('login.html', form=LoginForm()), 401
            # else:
            #     return func(*args, **kwargs)

            return render_template('index.html', username=username)

        return _ck

    return ck
