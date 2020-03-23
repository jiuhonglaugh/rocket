#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
from aip import AipImageClassify

""" 你的 APPID AK SK """
# APP_ID = '你的 App ID'
APP_ID = '18988864'
# API_KEY = '你的 Api Key'
API_KEY = 'sPWpvq1GvCEeGKWsGFnr4Wve'
# SECRET_KEY = '你的 Secret Key'
SECRET_KEY = '8pXnRaoHV8aprWfzyLXMNEm5y41ySLnH'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    # filePath = 'C:/Users/MAIBENBEN/Desktop/Snipaste_2020-03-22_10-54-46.png'
    # image = get_file_content(filePath)
    # result = client.advancedGeneral(image)
    print(hashlib.md5('123dafd'.encode(encoding='utf-8')).hexdigest())
