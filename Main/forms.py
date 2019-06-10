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


class BooksInput(forms.Form):
    book_name = forms.CharField(label="书名", max_length=100, error_messages={"required": "书名不能为空！", "invalid": "书名格式错误"})
    author = forms.CharField(label="作者", max_length=50, error_messages={"required": "作者不能为空！"})
    translator = forms.CharField(label="译者", max_length=50, required=False)
    ISBN = forms.CharField(label="ISBN", max_length=20, required=False)
    edition = forms.CharField(label="版本", max_length=10, required=False)
    publication_date = forms.CharField(label="发行日期", max_length=6, required=False)


class ProperNounInput(forms.ModelForm):
    class Meta:
        model = ProperNounIndex
        fields = "__all__"
        exclude = ("create_time",)
        labels = {
            "book_name": "书名",
            "ISBN": "ISBN",
            "Noun": "专有名词",
            "page": "页码",
            "noun_property": "专名属性（人名、地名、其他）",
            "classes": "专名类别（如：河流、城市；神、政治家）",
            "relation": "专名关系（如：XX的城市；XX的国王）",
            "comment": "注释（如：长达50km；活了70岁）",
            "context": "上下文",
        }
        help_texts = None
        widgets = {"noun_property": forms.RadioSelect()}
        error_messages = {
            "book_name": {"required": "书名不能为空！"},
            "ISBN": {"required": "ISBN不能为空！"},
            "Noun": {"required": "专名不能为空！"},
            "page": {"required": "页码不能为空！"},
        }

    def __init__(self, *args, **kwargs):
        super(ProperNounInput, self).__init__(*args, **kwargs)
        self.fields["classes"].required = False
        self.fields["relation"].required = False
        self.fields["comment"].required = False
        self.fields["context"].required = False

        # choices = {"noun_property": ((1, "Person"), (2, "Location"), (3, "Other"))}

    # noun_property = forms.TypedChoiceField(label="专名属性（人名、地名、其他）", choices=((1, "Person"), (2, "Location"), (3, "Other")), widget=forms.RadioSelect)

# choices={1: "Person", 2: "Location", 3: "Other"}
# choices=((1, "Person"), (2, "Location"), (3, "Other"))

