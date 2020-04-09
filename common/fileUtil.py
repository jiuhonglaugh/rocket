#!/usr/bin/python3
# -*- encoding:utf-8 -*-
import os
import shutil
import zipfile
from os.path import dirname, abspath
'''
判断路径最后一位是不是 /
如果不是则添加/
'''


def repairPath(path):
    if str(path).endswith('/'):
        return path
    return path + '/'


'''
写文件,当文件不存在会自动创建
字符串写入
'''


def _writeFileLf(strOrList, path):
    if len(strOrList) > 1:
        with open(path, mode='a', encoding='utf-8') as f:
            for line in strOrList:
                f.write(line + "\n")
    else:
        with open(path, mode='a', encoding='utf-8') as f:
            f.write(strOrList + "\n")


def _writeFile(strOrList, path):
    with open(path, mode='a', encoding='utf-8') as f:
        if len(strOrList) > 1:
            with open(path, mode='a', encoding='utf-8') as f:
                for line in strOrList:
                    f.write(line)
        else:
            with open(path, mode='a', encoding='utf-8') as f:
                f.write(strOrList)


def writeFile(str, path, lf=True):
    if lf:
        _writeFileLf(str, path)
    else:
        _writeFile(str, path)


def readConfig(fileName):
    confPath = getConfigPath()
    with open(repairPath(confPath) + fileName) as r:
        return r.readlines()


def getHome():
    return dirname(dirname(abspath(__file__)))


def getConfigPath():
    return getHome() + '/conf'


def getFileSize(filePath):
    filesizes = ''
    filesizeK = os.stat(filePath).st_size / 1024
    if filesizeK > 1024:
        filesizeM = filesizeK / 1024
        if filesizeM > 1024:
            filesizeG = str(round(filesizeM / 1024, 2))
            filesizes = filesizeG + 'G'
        else:
            filesizes = str(round(filesizeM, 2)) + 'M'
    else:
        filesizes = str(round(filesizeK, 2)) + 'K'
    return filesizes


def zip_(fileList, zipPath):
    try:
        if len(fileList) > 1:
            zipName = os.path.split(zipPath)[1]
        else:
            zipName = os.path.split(fileList[0])[1]
        zipName = ('根目录' if zipName == '' else zipName)
        f = zipfile.ZipFile(os.path.join(zipPath, zipName) + '.zip', 'w', zipfile.ZIP_DEFLATED)
        for i in fileList:
            if os.path.isdir(i):
                for dirpath, dirnames, filenames in os.walk(i):
                    for filename in filenames:
                        f.write(os.path.join(dirpath, filename))
            else:
                f.write(i)
        f.close()
    except Exception as e:
        return [False, e]
    else:
        return [True, os.path.join(zipPath, zipName) + '.zip']


def delFileOrDir(fileName):
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


def isFile(filePath):
    return os.path.isfile(filePath)


if __name__ == '__main__':
    print(getConfigPath())
