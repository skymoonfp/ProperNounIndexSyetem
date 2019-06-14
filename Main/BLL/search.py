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
    start_time = None
    end_time = None
    time_interval = None

    try:
        start_time = kwargs["start_time"]
    except Exception:
        pass

    try:
        end_time = kwargs["end_time"]
    except Exception:
        pass

    try:
        time_interval = kwargs["time_interval"]
    except Exception:
        pass

    if not end_time:
        end_time = datetime.datetime.now()
    if not start_time:
        start_time = end_time - datetime.timedelta(seconds=time_interval)

    return_data = table.objects.filter(create_time__range=(start_time, end_time)).order_by("-create_time")
    return return_data


def data_search_count(data_search_return):
    count = data_search_return.count()
    return count

# def proper_noun_data_search(**kwargs):
#
#     return_data = data_search(**kwargs)
#     return_data_r = []
#
#     for item in return_data:
#         item_dict = dict()
#         item_dict["ProperNounIndex"] = item
#         item_dict["noun_property_name"] = item.noun_property.noun_property_name
#         return_data_r.append(item_dict)
#
#     return return_data_r
