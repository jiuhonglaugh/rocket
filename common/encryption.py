#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64

'''
加密
'''

def b64encode_(v):
    return base64.b64encode(v.encode()).decode()

'''
解密
'''
def b64decode_(v):
    try:
        return base64.b64decode(v).decode()
    except:
        # 网页传来的base64内容,在被flask捕捉的时候,加号会被解码成空格,导致解码报错
        # 这个bug调了我半个小时,我还以为前端js生成的base64有问题,fuck
        return base64.b64decode(v.replace(' ', '+')).decode()