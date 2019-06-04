# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render


def index(request, **kwargs):
    return render(request, "index.html", locals())


def test(request, **kwargs):
    return render(request, "test.html", locals())


def login(request, **kwargs):
    ret = {"status": ""}

    if request.method == "POST":
        pass

    return render(request, "login.html", {"data": "AAA"})


def operation(request, **kwargs):
    return render(request, "operation.html", locals())


def site_map(request, **kwargs):
    print(str(kwargs))
    return HttpResponse("<h1>map</h1>")


def books(request, **kwargs):
    print(str(kwargs))
    return HttpResponse("<h1>book</h1>")


def insert_data(request, **kwargs):
    pass
