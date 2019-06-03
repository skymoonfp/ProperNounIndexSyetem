#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     urls
 IDE：    PyCharm
创建时间： 2019/6/3 17:08
@author： skymoon
"""

from django.conf.urls import url

from Main.views import *

urlpatterns = [

    url(r"^index/$", index),
    url(r"^login/(\d*)/$", login),
    url(r"^site_map/(?P<name>\d*)/$", site_map),
    url(r"^books/(?P<classes>\d*)/(?P<name>\w*)/$", books),

]
