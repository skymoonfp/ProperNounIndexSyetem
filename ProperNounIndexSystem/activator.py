#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.shortcuts import HttpResponse, redirect


def process(request, **kwargs):
    """
    接收所有匹配url的请求，根据请求url中的参数，通过反射动态指定view中的方法
    :param request:
    :param kwargs:
    :return:
    """

    app = kwargs.get('app', None)
    function = kwargs.get('function', None)
    print("路径分发：", kwargs)

    try:
        appObj = __import__("%s.views" % app)
        viewObj = getattr(appObj, 'views')
        funcObj = getattr(viewObj, function)

        # 执行view.py中的函数，并获取其返回值
        result = funcObj(request, **kwargs)

    except (ImportError, AttributeError) as e:
        # 导入失败时，自定义404错误
        print(e)
        return HttpResponse('404 Not Found：', e)
    except Exception as e:
        print(Exception, e)
        # 代码执行异常时，自动跳转到指定页面
        return redirect('/Main/index/')
        # return HttpResponse('代码执行异常：'.encode("gbk"), e)

    return result
