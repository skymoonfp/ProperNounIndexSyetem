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

from Main.models import *


class BooksInput(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        exclude = ("create_time",)
        labels = {
            "book_name": "书名",
            "author": "作者",
            "translator": "译者",
            "ISBN": "ISBN",
            "edition": "版次",
            "publication_date": "出版日期",
        }
        help_texts = None
        error_messages = {
            "book_name": {"required": "书名不能为空！"},
        }

    def __init__(self, *args, **kwargs):
        super(BooksInput, self).__init__(*args, **kwargs)
        self.fields["author"].required = False
        self.fields["translator"].required = False
        self.fields["ISBN"].required = False
        self.fields["edition"].required = False
        self.fields["publication_date"].required = False


class ProperNounInput(forms.ModelForm):
    class Meta:
        model = ProperNoun
        fields = "__all__"
        exclude = ("create_time",)
        labels = {
            "Noun": "专有名词",
            "book": "书名",
            "category": "专名范畴（人名、地名、其他）",
            "classes": "专名类别（如：河流、城市；神、政治家）",
            "properties": "专名属性（如：长达50km；活了70岁）",
            "relation": "专名关系（如：XX的城市；XX的国王）",
            "comment": "注释",
        }
        help_texts = None
        widgets = {"category": forms.CheckboxSelectMultiple()}
        error_messages = {
            "Noun": {"required": "专名不能为空！"},
        }

    def __init__(self, *args, **kwargs):
        super(ProperNounInput, self).__init__(*args, **kwargs)
        self.fields["category"].required = False
        self.fields["classes"].required = False
        self.fields["properties"].required = False
        self.fields["relation"].required = False
        self.fields["comment"].required = False


class BookNounIndexInput(forms.ModelForm):
    class Meta:
        model = BookNounIndex
        fields = "__all__"
        exclude = ("create_time",)
        labels = {
            "book": "书籍",
            "Noun": "专名",
            "page": "页码",
            "context": "上下文",
        }
        help_texts = None
        error_messages = {
            "page": {"required": "页码不能为空！"},
        }

    def __init__(self, *args, **kwargs):
        super(BookNounIndexInput, self).__init__(*args, **kwargs)
        self.fields["context"].required = False
