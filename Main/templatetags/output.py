#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     output
 IDE：    PyCharm
创建时间： 2019/6/4 10:07
@author： skymoon
"""

from django import template

register = template.Library()


@register.simple_tag
def mymethod(v1):
    result = v1 * 1000
    return result
