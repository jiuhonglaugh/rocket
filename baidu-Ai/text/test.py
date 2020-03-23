import json

import requests
import base64


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


'''
通用文字识别
'''
if __name__ == '__main__':

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    f = open('C:/Users/MAIBENBEN/Desktop/Snipaste_2020-03-22_11-23-26.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = get_access_token()
    request_url = "{}?access_token={}".format(request_url, access_token)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        result = json.loads(response.text)['words_result']
        for word in result:
            print(word)
