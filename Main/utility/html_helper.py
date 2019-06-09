#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     html_helper
 IDE：    PyCharm
创建时间： 2019/6/9 16:20
@author： skymoon
"""

import math
from django.utils.safestring import mark_safe


def page_name_judge(page_url):
    page_name = page_url.split("_")[0]
    if page_name == "onehour":
        page_url_onehour = page_url
        page_url_oneday = "oneday_1"
        page_url_thirtydays = "thirtydays_1"
    elif page_name == "oneday":
        page_url_onehour = "onehour_1"
        page_url_oneday = page_url
        page_url_thirtydays = "thirtydays_1"
    else:
        page_url_onehour = "onehour_1"
        page_url_oneday = "oneday_1"
        page_url_thirtydays = page_url
    return page_url_onehour, page_url_oneday, page_url_thirtydays


class PageInfo(object):

    def __init__(self, url, page_url, total_count, per_item=8):
        """

        :param url: 当前网址
        :param page_url: 分页网址
        :param total_count: 总记录条数
        :param per_item: 每页显示记录条数
        """
        self.url = url
        self.page_url = page_url
        self.total_count = total_count
        self.per_item = per_item
        self.page_name = page_url.split("_")[0]
        self.page = int(page_url.split("_")[1])
        self.all_pages = math.ceil(self.total_count / self.per_item)

    @property
    def start(self):
        """

        :return: 当前页显示记录在所有显示记录中的起始位置
        """
        return (self.page - 1) * self.per_item

    @property
    def over(self):
        """

        :return: 当前页显示记录在所有显示记录中的结束位置
        """
        # return self.page * self.per_item
        if self.page < self.all_pages:
            return self.page * self.per_item
        else:
            return self.total_count

    def page_show(self, show_pages):
        """

        :param show_pages: 分页栏显示页码数量
        :return:
        """
        # 全部页数小于或等于显示页数
        if self.all_pages <= show_pages:
            begin = 0
            end = self.all_pages
        # 全部页数大于显示页数
        else:
            # 当前页数小于或等于显示页数的中位数
            if self.page <= math.floor((show_pages + 1) / 2):
                begin = 0
                end = show_pages
            # （总页数-当前页数）小于显示页数的中位数
            elif (self.all_pages - self.page) < math.floor((show_pages + 1) / 2):
                begin = self.all_pages - show_pages
                end = self.all_pages
            else:
                begin = self.page - math.floor((show_pages + 1) / 2)
                end = self.page + math.floor((show_pages + 1) / 2) - 1

        return begin, end

    def pagify(self):
        page_html = []

        # 首页
        first_html = "<a href='" + self.url + self.page_name + "_" + "%d/'>首页</a>" % (1,)
        page_html.append(first_html)

        # 上一页
        if self.page <= 1:
            pre_html = "<a href='#'>上一页</a>"
        else:
            pre_html = "<a href='" + self.url + self.page_name + "_" + "%d/'>上一页</a>" % (self.page - 1,)
        page_html.append(pre_html)

        # 中间
        begin, end = self.page_show(show_pages=5)
        for i in range(begin, end):
            if self.page == i + 1:
                a_html = "<a class='selected' href='" + self.url + self.page_name + "_" + "%d/'>%d</a>" % (i + 1, i + 1)
            else:
                a_html = "<a href='" + self.url + self.page_name + "_" + "%d/'>%d</a>" % (i + 1, i + 1)
            page_html.append(a_html)

        # 下一页
        if self.page >= self.all_pages:
            post_html = "<a href='#'>下一页</a>"
        else:
            post_html = "<a href='" + self.url + self.page_name + "_" + "%d/'>下一页</a>" % (self.page + 1,)
        page_html.append(post_html)

        # 尾页
        last_html = "<a href='" + self.url + self.page_name + "_" + "%d/'>尾页</a>" % (self.all_pages,)
        page_html.append(last_html)

        # 分页html字符串
        page_mark = mark_safe("".join(page_html))
        return page_mark
