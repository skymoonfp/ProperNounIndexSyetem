#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     forms.py
 IDE：    PyCharm
创建时间： 2019/6/7 15:20
@author： skymoon
"""

from django import forms


class BooksInput(forms.Form):
    book_name = forms.CharField(label="书名", max_length=100, error_messages={"required": "书名不能为空！", "invalid": "书名格式错误"})
    author = forms.CharField(label="作者", max_length=50, error_messages={"required": "作者不能为空！"})
    translator = forms.CharField(label="译者", max_length=50, required=False)
    ISBN = forms.CharField(label="ISBN", max_length=20, required=False)
    edition = forms.CharField(label="版本", max_length=10, required=False)
    publication_date = forms.CharField(label="发行日期", max_length=6, required=False)


class ProperNounInput(forms.Form):
    book_name = forms.CharField(label="书名", max_length=100, error_messages={"required": "书名不能为空！"})
    ISBN = forms.CharField(label="ISBN", max_length=20)
    Noun = forms.CharField(label="专有名词", max_length=30)
    page = forms.CharField(label="页码", max_length=20)
    noun_property = forms.MultipleChoiceField(label="专名属性（人名、地名、其他）",
                                              choices=[(1, "Person"), (2, "Location"), (3, "Other")],
                                              widget=forms.RadioSelect)
    classes = forms.CharField(label="专名类别（如：河流、城市；神、政治家）", max_length=30, required=False)
    relation = forms.CharField(label="专名关系（如：XX的城市；XX的国王）", max_length=60, required=False)
    comment = forms.CharField(label="注释（如：长达50km；活了70岁）", max_length=60, required=False)
    context = forms.Field(label="上下文", required=False)
