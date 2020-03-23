#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Required, Length, Email, InputRequired


class SshForm(FlaskForm):
    host = StringField('host', validators=[DataRequired()])
    port = PasswordField('port', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    pwd = StringField('pwd', validators=[DataRequired()])
    submit = SubmitField('Log in SSH')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('passowrd', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Log in')


class NameForm(FlaskForm):
    username = StringField('What is your name?', validators=[DataRequired()])
    password = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FileForm(FlaskForm):
    path = StringField('path', validators=[DataRequired()])
    editValues = StringField('editValues', validators=[DataRequired()])
    filename = StringField('filename', validators=[DataRequired()])


class LinuxServerForm(FlaskForm):
    """服务器信息表单"""
    name = StringField('name', validators=[DataRequired()])
    ipaddr = StringField('ipaddr', validators=[DataRequired()])
    port = IntegerField('port')
    cpu_num = IntegerField('cpu_num')
    mem_total = StringField('mem_total')
    submit = SubmitField('submit')


class LinuxSysInfoForm(FlaskForm):
    """采集信息"""
    mem_use = StringField('mem_use', validators=[DataRequired()])
    # mem_total = db.Column(db.String(16))
    mem_ava = StringField('mem_ava', validators=[DataRequired()])
    cpu_load = StringField('cpu_load', validators=[DataRequired()])
    disk_use = StringField('disk_use', validators=[DataRequired()])
    # disk_total = IntegerField('disk_total')
    disk_free = IntegerField('disk_free')
