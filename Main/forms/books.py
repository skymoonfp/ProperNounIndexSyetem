#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     books
 IDE：    PyCharm
创建时间： 2019/6/6 16:32
@author： skymoon
"""

from django import forms


class BooksInput(forms.Form):
    book_name = forms.CharField(label="书名", max_length=100)
    author = forms.CharField(label="作者", max_length=50)
    translator = forms.CharField(label="译者", max_length=50, required=False)
    ISBN = forms.CharField(label="ISBN", max_length=20, required=False)
    edition = forms.CharField(label="版本", max_length=10, required=False)
    publication_date = forms.CharField(label="发行日期", max_length=6, required=False)
