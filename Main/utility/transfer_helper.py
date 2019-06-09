#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     transfer_helper
 IDE：    PyCharm
创建时间： 2019/6/9 17:15
@author： skymoon
"""


def try_int(arg, default):
    try:
        arg = int(arg)
    except Exception:
        arg = default
    return arg
