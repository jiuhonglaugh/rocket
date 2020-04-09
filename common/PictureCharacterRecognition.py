#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import requests
import base64

from common import fileUtil

BD_AIUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
AUTH_URL = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'


class PictureCharacterRecognition:
    '''
    client_id = 'sPWpvq1GvCEeGKWsGFnr4Wve'  # 此变量赋值成自己API Key的值
    client_secret = '8pXnRaoHV8aprWfzyLXMNEm5y41ySLnH'  # 此变量赋值成自己Secret Key的值
    '''

    def __init__(self, client_id='sPWpvq1GvCEeGKWsGFnr4Wve',
                 client_secret='8pXnRaoHV8aprWfzyLXMNEm5y41ySLnH'):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_access_token(self):
        # 此函数用于获取access_token，返回access_token的值
        # 此函数被parse_face_pic调用
        response = requests.get(AUTH_URL.format(self.client_id, self.client_secret))
        if response:
            json_result = json.loads(response.text)
            self.access_token = json_result['access_token']
            return True
        return False

    def requestBaiDuAi(self, img):
        if isinstance(img, bytes):
            if self.get_access_token():
                request_url = "{}?access_token={}".format(BD_AIUrl, self.access_token)
                headers = {'content-type': 'application/x-www-form-urlencoded'}
                response = requests.post(request_url, data={"image": img}, headers=headers)
                if response:
                    result = json.loads(response.text)['words_result']
                    return json.dumps({'code': 0, 'result': result}, ensure_ascii=False)
            return json.dumps({'code': 1, 'result': '获取 BAIDU-AI access_token 失败'})
        return json.dumps({'code': 1, 'result': '传入的 Img 不是 Bytes 类型'})

    '''
    通用文字识别
    '''

    def startRecognition(self, path):
        if not fileUtil.isFile(path):
            return json.dumps({'result': '文件不存在或这不是文件', 'code': 1}, ensure_ascii=False)
        f = open(path, 'rb')
        img = base64.b64encode(f.read())
        return self.requestBaiDuAi(img)


if __name__ == '__main__':
    pcr = PictureCharacterRecognition()
    path = 'C:/Users/MAIBENBEN/Desktop/Snipaste_2020-03-24_15-27-45.png'
    print(pcr.startRecognition(path))
