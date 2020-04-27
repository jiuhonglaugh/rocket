#!/usr/bin/python3
# -*- encoding:utf-8 -*-
import yaml


def load(filePath):
    with open(filePath, "r", encoding='utf-8')as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def saveWrite(dicts, filePath):
    with open(filePath, "w", encoding='utf-8') as f:
        yaml.dump(dicts, f)
