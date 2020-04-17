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

class HostForm(FlaskForm):
    host_ip = StringField('What is your name?', validators=[DataRequired()])
    host_port = IntegerField('host_port')
    host_user = StringField('What is your name?', validators=[DataRequired()])
    host_password = StringField('What is your name?', validators=[DataRequired()])
    host_script_path = StringField('What is your name?', validators=[DataRequired()])
    host_disk_path = StringField('What is your name?', validators=[DataRequired()])

class MysqlForm(FlaskForm):
    mysqlHost = StringField('What is your name?', validators=[DataRequired()])
    mysqlPort = IntegerField('mysqlPort')
    mysqlUser = StringField('What is your name?', validators=[DataRequired()])
    mysqlPwd = StringField('What is your name?', validators=[DataRequired()])
    mysqlDbName = StringField('What is your name?', validators=[DataRequired()])
    mysqlParam = StringField('What is your name?', validators=[DataRequired()])

class RedisForm(FlaskForm):
    redisHost = StringField('What is your name?', validators=[DataRequired()])
    redisPwd = StringField('What is your name?', validators=[DataRequired()])
    redisDbName = StringField('What is your name?', validators=[DataRequired()])

class NameForm(FlaskForm):
    username = StringField('What is your name?', validators=[DataRequired()])
    password = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FileForm(FlaskForm):
    path = StringField('path', validators=[DataRequired()])
    editValues = StringField('editValues', validators=[DataRequired()])
    filename = StringField('filename', validators=[DataRequired()])
    power = StringField('power', validators=[DataRequired()])
    newFileName = StringField('newFileName', validators=[DataRequired()])
    oldFileName = StringField('oldFileName', validators=[DataRequired()])
    dirName = StringField('dirName', validators=[DataRequired()])
    type = StringField('type', validators=[DataRequired()])
    selectedList = StringField('selectedList', validators=[DataRequired()])


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
