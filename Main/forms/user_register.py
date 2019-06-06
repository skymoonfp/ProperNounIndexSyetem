#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     user_register
 IDE：    PyCharm
创建时间： 2019/6/6 14:07
@author： skymoon
"""

from django import forms


class RegisterForm(forms.Form):
    user = forms.CharField()
    pwd = forms.CharField(widget=forms.PasswordInput())
    pwd2 = forms.CharField(widget=forms.PasswordInput())
    birth = forms.DateField()
    email = forms.CharField()
    mobile = forms.CharField()
    idcode = forms.CharField()
