#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     Base
 IDE：    PyCharm
创建时间： 2019/6/13 20:03
@author： skymoon
"""


class BaseResponse(object):

    def __init__(self):
        self.status = False
        self.data = None
        self.error = ""
