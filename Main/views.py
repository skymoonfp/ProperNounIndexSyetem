# Create your views here.


from django.http.response import HttpResponse
from django.shortcuts import render

from Main import forms
from Main.models import *
from Main.utility import *


# 主页
def index(request, **kwargs):
    return render(request, "index.html", locals())


# 登陆
def login(request, **kwargs):

    if request.method == "POST":
        user = request.POST.get("username_1", None)
        pwd = request.POST.get("password_1", None)
        print(user, pwd)

        erro = {}

        userinfo = UserInfo.objects.filter(username=user)
        print(userinfo)
        if len(userinfo) != 1:
            erro["erro_verify"] = r"该用户不存在！请注册！"
            return render(request, "login.html", erro)
        else:
            userinfo = UserInfo.objects.filter(username=user, password=pwd)
            if len(userinfo) == 0:
                erro["erro_verify"] = r"密码错误！"
                return render(request, "login.html", erro)
            else:
                erro["erro_verify"] = r"登陆成功！5秒后跳转！"
                return render(request, "operation.html", erro)

    return render(request, "login.html", locals())


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

        # obj = RegisterForm()
        # obj.user = user
        # obj.pwd = pwd
        # obj.pwd2 = pwd2
        # obj.birth = birth
        # obj.email = email
        # obj.mobile = mobile
        # obj.idcode = idcode
        # print(obj)

        if birth == "请输入出生日期":
            birth = None
        if email == "请输入电子邮箱":
            email = None
        if mobile == "请输入手机号":
            mobile = None
        if idcode == "请输入身份证号":
            idcode = None

        erro = {}

        if len(UserInfo.objects.filter(username=user)) >= 1:
            erro["erro_verify"] = r"该用户名已存在！"
            return render(request, "register.html", erro)
        else:
            UserInfo.objects.create(username=user, password=pwd, birthday=birth, e_mail=email, mobile=mobile,
                                    identify_code=idcode)
            erro["erro_verify"] = r"注册成功！请登录！"
            return render(request, "login.html", erro)
    else:
        return render(request, "register.html", locals())


def operation(request, **kwargs):
    return render(request, "operation.html", locals())


def site_map(request, **kwargs):
    print(str(kwargs))
    return HttpResponse("<h1>map</h1>")


# 查询
def search(request, **kwargs):
    return render(request, "search.html", locals())


# 书籍录入
def books_input(request, **kwargs):
    booksBack = forms.BooksInput()
    check = request.POST.getlist("book_input_check", "")
    return_dict = {"books_input": booksBack, "onehourdata": "", "onedaydata": "", "thirtydaysdata": ""}

    # 根据request.method决定是否传入数据库
    if request.method == "POST":
        data = {}
        booksInput = forms.BooksInput(request.POST)
        if booksInput.is_valid():
            data = booksInput.cleaned_data
            print(data)
            Books.objects.create(**data)
            return_dict["books_input_status"] = "提交成功！"

        # 根据复选框决定提交数据后的数据显示情况
        for key in data.keys():
            if key in check:
                pass
            else:
                data[key] = ""
        booksBack = forms.BooksInput(data)
        return_dict["books_input"] = booksBack

        # 查询最近1小时记录
        onehourdata = data_search(table=Books, time_interval=60 * 60, start_time="", end_time="")
        # 查询最近1天记录
        onedaydata = data_search(table=Books, time_interval=60 * 60 * 24, start_time="", end_time="")
        # 查询最近30天记录
        thirtydaysdata = data_search(table=Books, time_interval=60 * 60 * 24 * 30, start_time="", end_time="")

        return_dict["onehourdata"] = onehourdata
        return_dict["onedaydata"] = onedaydata
        return_dict["thirtydaysdata"] = thirtydaysdata

    return render(request, "books_input.html", return_dict)


# 专名录入
def propernoun_input(request, **kwargs):
    propernounBack = forms.ProperNounInput()
    check = request.POST.getlist("book_input_check", "")
    return_dict = {"propernoun_input": propernounBack}

    # 根据request.method决定是否传入数据库
    if request.method == "POST":
        data = {}
        propernounInput = forms.ProperNounInput(request.POST)
        if propernounInput.is_valid():
            data = propernounInput.cleaned_data
            print(data)
            ProperNounIndex.objects.create(**data)
            return_dict["nouns_input_status"] = "提交成功！"

        # 根据复选框决定提交数据后的数据显示情况
        for key in data.keys():
            if key in check:
                pass
            else:
                data[key] = ""
        propernounBack = forms.ProperNounInput(data)
        return_dict["propernoun_input"] = propernounBack

        # 查询最近1小时记录
        onehourdata = data_search(table=ProperNounIndex, time_interval=60 * 60, start_time="", end_time="")
        # 查询最近1天记录
        onedaydata = data_search(table=ProperNounIndex, time_interval=60 * 60 * 24, start_time="", end_time="")
        # 查询最近30天记录
        thirtydaysdata = data_search(table=ProperNounIndex, time_interval=60 * 60 * 24 * 30, start_time="", end_time="")

        return_dict["onehourdata"] = onehourdata
        return_dict["onedaydata"] = onedaydata
        return_dict["thirtydaysdata"] = thirtydaysdata

    return render(request, "propernoun_input.html", return_dict)



def test(request, **kwargs):
    return render(request, "test.html", locals())
