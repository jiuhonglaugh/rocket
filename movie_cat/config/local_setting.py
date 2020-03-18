# -*- coding: utf-8 -*-
#本地开发环境配置文件
from config.base_setting import *
#SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://wxgz:Gdzq_Infobeat_2019@172.10.4.100/mysql"
SECRET_KEY = "Gdzq_Infobeat_2019"

hosts='172.10.4.100,172.10.4.101,172.10.4.102'