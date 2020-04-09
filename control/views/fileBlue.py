#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request, render_template, session, Blueprint
from PIL import Image
import shutil
from common import fileUtil, extract
from common.ConfigUtil import ConfigUtil
from common.Logger import Logger
from common.PictureCharacterRecognition import PictureCharacterRecognition
from control.manager.fileManager import *
from control.form import FileForm

confDict = ConfigUtil('application.properties').getDict('fiel-system')
workPath = confDict.get('work.path')
allow = confDict.get('allow.jump.path', 'false').lower()
temp = confDict.get('picture.catalog')

file_blue = Blueprint('file', __name__)
log = Logger(loggername='fileBlue')
sep = os.path.sep  # 当前系统分隔符


@file_blue.route('/file/index/', methods=['GET', 'POST'])
def file():
    form = FileForm(request.form)
    session['secectList'] = json.dumps(list(set({})))
    return render_template('file.html', nowPath=b64encode_(workPath), sep=b64encode_(sep),
                           workPath=b64encode_(workPath), form=form)


# 返回文件目录
@file_blue.route('/file/GetFile', methods=['POST'])
def GetFile():
    form = FileForm(request.form)
    path = b64decode_(form.path.data)
    if not path.startswith(workPath) and 'true' != allow:
        return json.dumps({'resultCode': 1, 'result': "不允许访问上层目录或其他路径"})
    result = getFiles(path)
    return result


# 下载
@file_blue.route('/file/DownFile', methods=['GET', 'POST'])
def DownFile():
    form = FileForm(request.form)
    fileName = b64decode_(form.filename.data)
    result = DownLoadFile(fileName)
    return result


# 在线编辑
@file_blue.route('/file/codeEdit', methods=['GET', 'POST'])
def codeEdit():
    # 前端点击编辑时,传来一个get请求,filename为base64编码的包含路径的文件全名
    fileName = request.values.get('filename', None)
    if fileName:
        form = FileForm(request.form)
        return render_template('iframe/codeEdit.html', filename=fileName, form=form)
    # 返回的网页打开后,自动ajax请求该文件内容
    filename = b64decode_(request.form['path'])
    result = editing(filename)
    return result


# 保存编辑后的文件
@file_blue.route('/file/saveEditCode', methods=['POST'])
def saveEditCode():
    form = FileForm(request.form)
    editValues = b64decode_(form.editValues.data)
    fileName = b64decode_(form.filename.data)
    result = txtSaveAs(editValues, fileName)
    return result


# 删除
@file_blue.route('/file/Delete', methods=['POST'])
def Delete():
    form = FileForm(request.form)
    fileName = b64decode_(form.filename.data)
    result = deleteFileOrDir(fileName)
    if result[0]:
        return json.dumps({'resultCode': 0, 'result': 'success'})
    else:
        return json.dumps({'resultCode': 1, 'result': str(result[1])})


# 修改文件权限
@file_blue.route('/file/chmod', methods=['POST'])
def chmod():
    form = FileForm(request.form)
    fileName = b64decode_(form.filename.data)
    power = form.power.data
    try:
        os.chmod(fileName, int(power, 8))
    except Exception as e:
        return json.dumps({'resultCode': 1, 'result': str(e)})
    else:
        return json.dumps({'resultCode': 0, 'result': 'success'})


# 重命名
@file_blue.route('/file/RenameFile', methods=['POST'])
def RenameFile():
    form = FileForm(request.form)
    newFileName = b64decode_(form.newFileName.data)
    oldFileName = b64decode_(form.oldFileName.data)  # 原文件名,包含路径
    result = reNameFile(newFileName, oldFileName)
    return result


# 创建目录
@file_blue.route('/file/CreateDir', methods=['POST'])
def CreateDir():
    form = FileForm(request.form)
    dirName = b64decode_(form.dirName.data)
    path = b64decode_(form.path.data)
    result = createDir(path, dirName)
    return result


# 创建文件
@file_blue.route('/file/CreateFile', methods=['POST'])
def CreateFile():
    form = FileForm(request.form)
    fileName = b64decode_(form.filename.data)
    path = b64decode_(form.path.data)
    result = createFile(path, fileName)
    return result


# 批量操作
@file_blue.route('/file/batch', methods=['POST'])
def batch():
    form = FileForm(request.form)
    batchType = form.type.data
    selectedList = form.selectedList.data
    path = form.path.data
    # batchType = request.values.get('type')
    selectedListBase64 = json.loads(selectedList)
    # path = b64decode_(request.values.get('path'))
    selectedList = list(b64decode_(selected) for selected in selectedListBase64)
    result = batchOperation(batchType, selectedList, path)
    return result


# 图片浏览
@file_blue.route('/file/picVisit', methods=['POST'])
def picVisit():
    fileName = request.values.get('filename', None)
    fileName = b64decode_(fileName)
    img = Image.open(fileName)
    # 因为图片展示页面的div大小为800*800，所以根据图片高、宽等比例缩小
    h_pic = img.size[0] / 800
    w_pic = img.size[1] / 800
    size = ((int(img.size[0] / h_pic), int(img.size[1] / h_pic)) if h_pic >= w_pic else (
        int(img.size[0] / w_pic), int(img.size[1] / w_pic)))
    img = img.resize(size, Image.ANTIALIAS)

    name = os.path.join(fileUtil.getHome() + temp, os.path.split(fileName)[1])
    img.save(name)
    with open(name, 'rb') as f:
        imgBase64 = base64.b64encode(f.read()).decode()
    os.remove(name)
    return imgBase64


# 上传文件
@file_blue.route('/file/UploadFile', methods=['POST'])
def UploadFile():
    try:
        nowPath = b64decode_(request.values.get('nowPath'))
        UploadFileContent = request.files['File']
        UploadFileName = UploadFileContent.filename
        UploadFileContent.save(os.path.join(nowPath, UploadFileName))
    except Exception as e:
        return json.dumps({'resultCode': 1, 'result': str(e)})
    else:
        return json.dumps({'resultCode': 0, 'result': 'success'})


# 解压文件
@file_blue.route('/file/Extract', methods=['POST'])
def Extract_():
    fileName = b64decode_(request.values.get('filename'))
    extractResult = extract.main(fileName)
    if extractResult[0]:
        return json.dumps({'resultCode': 0, 'result': 'success'})
    else:
        return json.dumps({'resultCode': 1, 'result': str(extractResult[1])})


# 将前端多选的文件记录到session
@file_blue.route('/file/secectList', methods=['POST'])
def secectList():
    types = request.values.get('type')
    value = request.values.get('value')
    if 'secectList' in session:
        sejson = json.loads(session['secectList'])
    if (types == 'in') and (value not in sejson):
        sejson += [value]
        session['secectList'] = json.dumps(list(set(sejson)))
    elif (types == 'out') and (value in sejson):
        sejson.remove(value)
        session['secectList'] = json.dumps(sejson)
    elif types == 'del':
        session['secectList'] = '[]'
    elif types == 'get':
        return json.dumps({'resultCode': 0, 'result': session['secectList']})
    return json.dumps({'resultCode': 0, 'result': 'success'})


@file_blue.route('/file/distinguish', methods=['POST'])
def distinguish():
    fileName = request.values.get('filename', None)
    fileName = b64decode_(fileName)
    pcr = PictureCharacterRecognition()
    result = pcr.startRecognition(fileName)
    return result


# --------------API---------------#
def delete_(fileName):
    try:
        if os.path.exists(fileName):
            if os.path.isfile(fileName):
                os.remove(fileName)
            else:
                shutil.rmtree(fileName)
        else:
            return [False, "文件或目录不存在"]
    except Exception as e:
        return [False, e]
    else:
        return [True]


def copy_(copyFile, path):
    try:
        if os.path.isdir(copyFile):
            # 将要复制过来的文件夹名
            newPath = os.path.join(path, os.path.split(copyFile)[1])
            if not os.path.exists(os.path.join(path, os.path.split(copyFile)[1])):
                os.mkdir(newPath)
            else:
                return [False, '要复制的文件夹已存在！']
            for i in os.listdir(copyFile):
                # 拼接将要复制的文件全路径
                i = os.path.join(copyFile, i)
                if os.path.isdir(i):
                    # 要是能像cut一样简单就好了
                    copy_(i, newPath)
                else:
                    shutil.copy(i, newPath)
        else:
            if not os.path.exists(os.path.join(path, os.path.split(copyFile)[1])):
                shutil.copy(copyFile, path)
            else:
                return [False, '要复制的文件已存在！']
    except Exception as e:
        return [False, e]
    else:
        return [True]


def cut_(cutFile, path):
    try:
        if os.path.exists(os.path.join(path, os.path.split(cutFile)[1])):
            return [False, '要剪切的文件已存在！']
        shutil.move(cutFile, path)
    except Exception as e:
        return [False, e]
    else:
        return [True]


def b64decode_(v):
    try:
        return base64.b64decode(v).decode()
    except:
        # 网页传来的base64内容,在被flask捕捉的时候,加号会被解码成空格,导致解码报错
        # 这个bug调了我半个小时,我还以为前端js生成的base64有问题,fuck
        return base64.b64decode(v.replace(' ', '+')).decode()


def b64encode_(v):
    return base64.b64encode(v.encode()).decode()
