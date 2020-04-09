#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=sPWpvq1GvCEeGKWsGFnr4Wve&client_secret=8pXnRaoHV8aprWfzyLXMNEm5y41ySLnH'


def get_access_token():
    # 此函数用于获取access_token，返回access_token的值
    # 此函数被parse_face_pic调用
    client_id = 'sPWpvq1GvCEeGKWsGFnr4Wve'  # 此变量赋值成自己API Key的值
    client_secret = '8pXnRaoHV8aprWfzyLXMNEm5y41ySLnH'  # 此变量赋值成自己Secret Key的值
    auth_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
        client_id, client_secret)

    response_at = requests.get(auth_url)
    json_result = json.loads(response_at.text)
    access_token = json_result['access_token']
    return access_token
