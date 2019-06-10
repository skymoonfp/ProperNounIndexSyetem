#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     session_helper.py
 IDE：    PyCharm
创建时间： 2019/6/11 0:25
@author： skymoon
"""

from django.shortcuts import render


def login_session(main_func):
    def wrapper(request, *args, **kwargs):
        print(request.session)
        print(request.session.session_key)
        userinfo = request.session.get("userinfo", None)
        print("aaa", userinfo)
        if userinfo["is_login"]:
            return main_func(request, *args, **kwargs)
        else:
            return render(request, "login.html", locals())

    return wrapper
