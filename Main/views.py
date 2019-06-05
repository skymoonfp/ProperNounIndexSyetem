# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render


# 主页
def index(request, **kwargs):
    return render(request, "index.html", locals())


# 登陆
def login(request, **kwargs):
    ret = {"status": ""}

    if request.method == "POST":
        pass

    return render(request, "login.html", {"data": "AAA"})


# 注册
def register(request, **kwargs):
    if request.method == "POST":
        user = request.POST.get("username_2", None)
        pwd = request.POST.get("password_2", None)
        pwd2 = request.POST.get("password_3", None)
        birth = request.POST.get("birthday", None)
        email = request.POST.get("e_mail", None)
        mobile = request.POST.get("mobile", None)
        idcode = request.POST.get("identify_code", None)

        print(user, pwd, pwd2, birth, email, mobile, idcode)

        pwderro = {}
        pwderro["pwd_verify"] = r"<a style='color:red;font-size:16px;'>两次输入的密码不一致，请检查后重新输入！</a>"

        if pwd != pwd2:
            return render(request, "login.html", pwderro)
        else:
            return render(request, "index.html", locals())

    else:
        return render(request, "login.html", locals())



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


def test(request, **kwargs):
    return render(request, "test.html", locals())
