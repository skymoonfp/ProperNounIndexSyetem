from django.http.response import HttpResponse


# Create your views here.


def index(request, **kwargs):
    return HttpResponse("<h1>这是主页</h1>")


def login(request, **kwargs):
    return HttpResponse("<h1>log</h1>")


def site_map(request, **kwargs):
    print(str(kwargs))
    return HttpResponse("<h1>map</h1>")


def books(request, **kwargs):
    print(str(kwargs))
    return HttpResponse("<h1>book</h1>")
