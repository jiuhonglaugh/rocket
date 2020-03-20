#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def randomRandint(start=50, end=100):
    return random.randint(start, end)