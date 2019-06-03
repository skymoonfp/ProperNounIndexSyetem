# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render


def index(request, **kwargs):
    return HttpResponse("<h1>这是主页</h1>")


def login(request, **kwargs):
    return render(request, "login.html", {"data": "AAA"})


def operation(request, **kwargs):
    # return render(request, "operation.html", {"data": "AAA"})
    return render(request, "operation.html", locals())


def site_map(request, **kwargs):
    print(str(kwargs))
    return HttpResponse("<h1>map</h1>")


def books(request, **kwargs):
    print(str(kwargs))
    return HttpResponse("<h1>book</h1>")


def insert_data(request, **kwargs):
    pass
