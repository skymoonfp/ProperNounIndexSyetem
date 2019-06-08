#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     output
 IDE：    PyCharm
创建时间： 2019/6/4 10:07
@author： skymoon
"""

import time

from django import template

register = template.Library()


@register.simple_tag
def datetime_format(time_data):
    time_return = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(time_data, "%b %d, %Y, %I:%M %p"))
    return time_return
