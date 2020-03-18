#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser

from movie_cat.common.utils import fileUtil_copy


class configUtil:
    """
    初始化即读取配置文件
    """
    def __init__(self, confName):
        configPath = fileUtil_copy.repairPath(fileUtil_copy.getConfigPath())
        self.configPath = configPath + confName
        ###必须使用RawConfigParser()，否则会报错
        self.cf = configparser.RawConfigParser()
        # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
        self.cf.read(self.configPath)

    """
    获取所有顶级配置
    """
    def getAllSections(self):
        sections = self.cf.sections()
        return sections

    """
    1、获取配置文件全部配置项
    2、返回一个字典类型数据
    """
    def getDicts(self):
        dt = {}
        for sect in self.getAllSections():
            list = self.cf.items(sect)
            for tuple in list:
                dt[tuple[0]] = tuple[1]
        return dt

    """
    获取单个
    """

    def getDict(self, section):
        dt = {}
        list = self.cf.items(section)
        for tuple in list:
            dt[tuple[0]] = tuple[1]
        return dt

