#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     output
 IDE：    PyCharm
创建时间： 2019/6/4 10:07
@author： skymoon
"""

import datetime

from django import template

register = template.Library()


@register.simple_tag
def datetime_format(time_data):
    time_return = datetime.datetime.strftime(time_data, "%Y-%m-%d %H:%M:%S")
    return time_return


@register.simple_tag
def datetime_format_hour(time_data):
    time_return = datetime.datetime.strftime(time_data, "%H:%M:%S")
    return time_return


@register.simple_tag
def datetime_format_month_day(time_data):
    time_return = datetime.datetime.strftime(time_data, "%b %d %H:%M:%S")
    return time_return
