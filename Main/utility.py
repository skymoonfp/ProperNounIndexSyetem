#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     utility
 IDE：    PyCharm
创建时间： 2019/6/8 15:39
@author： skymoon
"""

import datetime


def data_search(**kwargs):
    table = kwargs["table"]
    start_time = kwargs["start_time"]
    end_time = kwargs["end_time"]
    time_interval = kwargs["time_interval"]
    if not end_time:
        end_time = datetime.datetime.now()
    if not start_time:
        start_time = end_time - datetime.timedelta(seconds=time_interval)

    return_data = table.objects.filter(create_time__range=(start_time, end_time))
    # print(return_data)
    return return_data
