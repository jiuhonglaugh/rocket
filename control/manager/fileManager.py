#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64
import json
import os
import time
import traceback
import chardet
from flask import make_response, send_from_directory
from common.fileUtil import getFileSize, zip_, delFileOrDir, cut_, copy_


def getFiles(path):
    try:
        Files = sorted(os.listdir(path))
        dir_ = []
        file_ = []
        fileQuantity = len(Files)
        for i in Files:
            try:
                i = os.path.join(path, i)
                if not os.path.isdir(i):
                    if os.path.islink(i):
                        fileLinkPath = os.readlink(i)
                        file_.append({
                            'fileName': i,
                            'fileSize': getFileSize(i),
                            'fileOnlyName': os.path.split(i)[1] + '-->' + fileLinkPath,
                            'fileMODTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(i).st_mtime)),
                            'power': oct(os.stat(i).st_mode)[-3:],
                            'fileType': 'file'
                        })
                    else:
                        file_.append({
                            'fileName': i,
                            'fileSize': getFileSize(i),
                            'fileOnlyName': os.path.split(i)[1],
                            'fileMODTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(i).st_mtime)),
                            'power': oct(os.stat(i).st_mode)[-3:],
                            'fileType': 'file'
                        })
                else:
                    dir_.append({
                        'fileName': i,
                        'fileOnlyName': os.path.split(i)[1],
                        'fileSize': getFileSize(i),
                        'fileMODTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(i).st_mtime)),
                        'power': oct(os.stat(i).st_mode)[-3:],
                        'fileType': 'dir'
                    })
            except Exception as e:
                print(e)
                continue
        returnJson = {
            'path': base64.b64encode(path.encode()).decode(),
            'fileQuantity': fileQuantity,
            'files': dir_ + file_
        }
    except Exception as e:
        return json.dumps({'resultCode': 1, 'result': str(traceback.format_exc())})
    else:
        return json.dumps({'resultCode': 0, 'result': returnJson})


'''
文件下载，如果下载的是文件夹将会压缩后返回压缩文件
'''


def DownLoadFile(fileName):
    if os.path.isdir(fileName):
        result = zip_(fileList=[fileName], zipPath=os.path.split(fileName)[0])
        if result[0]:
            fileName = result[1]
        else:
            return json.dumps({'resultCode': 1, 'fileCode': str("error")})
    response = make_response(
        send_from_directory(os.path.split(fileName)[0], os.path.split(fileName)[1], as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(
        os.path.split(fileName)[1].encode().decode('latin-1'))
    return response


def createFile(path, fileName):
    try:
        if os.path.exists(os.path.join(path, fileName)):
            return json.dumps({'resultCode': 1, 'result': '文件已存在'})
        else:
            open(os.path.join(path, fileName), 'w', encoding='utf-8')
    except Exception as e:
        return json.dumps({'resultCode': 1, 'result': str(e)})
    else:
        return json.dumps({'resultCode': 0, 'result': 'success'})


def createDir(path, dirName):
    try:
        if os.path.exists(os.path.join(path, dirName)):
            return json.dumps({'resultCode': 1, 'result': '目录已存在'})
        else:
            os.mkdir(os.path.join(path, dirName))
    except Exception as e:
        return json.dumps({'resultCode': 1, 'result': str(e)})
    else:
        return json.dumps({'resultCode': 0, 'result': 'success'})


def reNameFile(newFileName, oldFileName):
    try:
        filePath = os.path.split(oldFileName)[0]  # 提取路径
        oldFileName = os.path.split(oldFileName)[1]  # 原文件名,不包含路径
        if os.path.exists(os.path.join(filePath, newFileName)):
            return json.dumps({'resultCode': 1, 'result': '新文件名和已有文件名重复!'})
        else:
            os.rename(os.path.join(filePath, oldFileName), os.path.join(filePath, newFileName))
    except Exception as e:
        return json.dumps({'resultCode': 1, 'result': str(e)})
    else:
        return json.dumps({'resultCode': 0, 'result': 'success'})


def editing(filename):
    if os.path.getsize(filename) > 2097152:
        return json.dumps({'resultCode': 1, 'fileCode': '不能在线编辑大于2MB的文件！'});
    with open(filename, 'rb') as f:
        # 文件编码,fuck you
        srcBody = f.read()
        char = chardet.detect(srcBody)
        fileCoding = char['encoding']
        if fileCoding == 'GB2312' or not fileCoding or fileCoding == 'TIS-620' or fileCoding == 'ISO-8859-9': fileCoding = 'GBK';
        if fileCoding == 'ascii' or fileCoding == 'ISO-8859-1': fileCoding = 'utf-8';
        if fileCoding == 'Big5': fileCoding = 'BIG5';
        if not fileCoding in ['GBK', 'utf-8', 'BIG5']: fileCoding = 'utf-8';
        if not fileCoding:
            fileCoding = 'utf-8'
        try:
            fileCode = srcBody.decode(fileCoding).encode('utf-8')
        except:
            # 这一步说明文件编码不被支持,可以按需修改返回数据
            return json.dumps({'resultCode': 0, 'fileCode': str(srcBody)})
        else:
            return json.dumps(
                {'resultCode': 0, 'fileCode': fileCode.decode(), 'encoding': fileCoding, 'fileName': filename})


def txtSaveAs(editValues, fileName):
    try:
        with open(fileName, 'w', encoding='utf-8') as f:
            f.write(editValues)
    except Exception as e:
        return json.dumps({'resultCode': 1, 'result': str(e)})
    else:
        return json.dumps({'resultCode': 0, 'result': 'success'})


def deleteFileOrDir(fileName):
    return delFileOrDir(fileName)

def batchOperation(batchType,selectedList,path):
    if batchType == 'cut':
        for cutFile in selectedList:
            result = cut_(cutFile, path)
            if not result[0]:
                return json.dumps({'resultCode': 1, 'result': str(result[1])})
        return json.dumps({'resultCode': 0, 'result': 'success'})
    elif batchType == 'copy':
        for copyFile in selectedList:
            result = copy_(copyFile, path)
            if not result[0]:
                return json.dumps({'resultCode': 1, 'result': str(result[1])})
        return json.dumps({'resultCode': 0, 'result': 'success'})
    elif batchType == 'delete':
        for i in selectedList:
            result = deleteFileOrDir(i)
            if not result[0]:
                return json.dumps({'resultCode': 1, 'result': str(result[1])})
        return json.dumps({'resultCode': 0, 'result': 'success'})
    elif batchType == 'zip':
        result = zip_(fileList=selectedList, zipPath=path)
        if not result[0]:
            return json.dumps({'resultCode': 1, 'result': str(result[1])})
        return json.dumps({'resultCode': 0, 'result': 'success'})
    return json.dumps({'resultCode': 1, 'result': '未知请求'})