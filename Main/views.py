# Create your views here.


from django.http.response import HttpResponse
from django.shortcuts import render

from Main import forms
from Main.models import *
from Main.utility.html_helper import *
from Main.utility.search_helper import *


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
    # 创建返回form对象
    booksBack = forms.BooksInput()

    # 获取checkbox值
    check = request.POST.getlist("book_input_check", "")

    # 定义返回字典，初始化添加form对象
    return_dict = {"books_input": booksBack}

    # 根据request.method决定是否传入数据库
    if request.method == "POST":
        data = {}
        booksInput = forms.BooksInput(request.POST)
        if booksInput.is_valid():
            data = booksInput.cleaned_data
            print("输入数据：", data)
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
    onehourdata = data_search(table=Books, time_interval=60 * 60)
    onehourdata_count = data_search_count(onehourdata)
    # 查询最近1天记录
    onedaydata = data_search(table=Books, time_interval=60 * 60 * 24)
    onedaydata_count = data_search_count(onedaydata)
    # 查询最近30天记录
    thirtydaysdata = data_search(table=Books, time_interval=60 * 60 * 24 * 30)
    thirtydaysdata_count = data_search_count(thirtydaysdata)

    # 返回字典中添加记录总条数
    return_dict["onehourdata_count"] = onehourdata_count
    return_dict["onedaydata_count"] = onedaydata_count
    return_dict["thirtydaysdata_count"] = thirtydaysdata_count

    # 获取page_url，如果为空，设置为"onehour_1"
    try:
        page_url = kwargs["id"]  # 输入页数时
    except Exception:
        page_url = "onehour_1"

    print(page_url)

    # 分页
    # # 异步刷新
    # page_name = page_url.split("_")[0]
    # if page_name == "onehour":
    #     onehour_page = PageInfo("/Main/books_input/", page_url, onehourdata_count, 12)
    #     return_dict["page_onehour"] = onehour_page.pagify()
    #     return_dict["onehourdata"] = onehourdata[onehour_page.start:onehour_page.over]
    #     if onehourdata_count == 0:
    #         return_dict["onehourdata_page_count"] = str(onehour_page.start) + "-" + str(onehour_page.over)
    #     else:
    #         return_dict["onehourdata_page_count"] = str(onehour_page.start + 1) + "-" + str(onehour_page.over)
    # elif page_name == "oneday":
    #     oneday_page = PageInfo("/Main/books_input/", page_url, onedaydata_count, 18)
    #     return_dict["page_oneday"] = oneday_page.pagify()
    #     return_dict["onedaydata"] = onedaydata[oneday_page.start:oneday_page.over]
    #     if onedaydata_count == 0:
    #         return_dict["onedaydata_page_count"] = str(oneday_page.start) + "-" + str(oneday_page.over)
    #     else:
    #         return_dict["onedaydata_page_count"] = str(oneday_page.start + 1) + "-" + str(oneday_page.over)
    # else:
    #     thirtydays_page = PageInfo("/Main/books_input/", page_url, thirtydaysdata_count, 12)
    #     return_dict["page_thirtydays"] = thirtydays_page.pagify()
    #     return_dict["thirtydaysdata"] = thirtydaysdata[thirtydays_page.start:thirtydays_page.over]
    #     if thirtydaysdata_count == 0:
    #         return_dict["thirtydaysdata_page_count"] = str(thirtydays_page.start) + "-" + str(thirtydays_page.over)
    #     else:
    #         return_dict["thirtydaysdata_page_count"] = str(thirtydays_page.start + 1) + "-" + str(thirtydays_page.over)

    # 同步刷新
    onehour_page = PageInfo("/Main/books_input/", page_name_judge(page_url)[0], onehourdata_count, 12)
    oneday_page = PageInfo("/Main/books_input/", page_name_judge(page_url)[1], onedaydata_count, 18)
    thirtydays_page = PageInfo("/Main/books_input/", page_name_judge(page_url)[2], thirtydaysdata_count, 12)

    # 返回字典中添加页码标签
    return_dict["page_onehour"] = onehour_page.pagify()
    return_dict["page_oneday"] = oneday_page.pagify()
    return_dict["page_thirtydays"] = thirtydays_page.pagify()

    # 返回字典中添加每页记录
    return_dict["onehourdata"] = onehourdata[onehour_page.start:onehour_page.over]
    return_dict["onedaydata"] = onedaydata[oneday_page.start:oneday_page.over]
    return_dict["thirtydaysdata"] = thirtydaysdata[thirtydays_page.start:thirtydays_page.over]

    # 返回字典中添加当前页记录在总记录中的起止位置（无记录从0开始，有记录从1开始）
    if onehourdata_count == 0:
        return_dict["onehourdata_page_count"] = str(onehour_page.start) + "-" + str(onehour_page.over)
    else:
        return_dict["onehourdata_page_count"] = str(onehour_page.start + 1) + "-" + str(onehour_page.over)
    if onedaydata_count == 0:
        return_dict["onedaydata_page_count"] = str(oneday_page.start) + "-" + str(oneday_page.over)
    else:
        return_dict["onedaydata_page_count"] = str(oneday_page.start + 1) + "-" + str(oneday_page.over)
    if thirtydaysdata_count == 0:
        return_dict["thirtydaysdata_page_count"] = str(thirtydays_page.start) + "-" + str(thirtydays_page.over)
    else:
        return_dict["thirtydaysdata_page_count"] = str(thirtydays_page.start + 1) + "-" + str(thirtydays_page.over)

    # # 返回字典中添加每页记录
    # return_dict["onehourdata"] = onehourdata
    # return_dict["onedaydata"] = onedaydata
    # return_dict["thirtydaysdata"] = thirtydaysdata

    print(return_dict)

    return render(request, "books_input.html", return_dict)


def page_show():
    pass


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
        onehourdata = data_search(table=ProperNounIndex, time_interval=60 * 60)
        # 查询最近1天记录
        onedaydata = data_search(table=ProperNounIndex, time_interval=60 * 60 * 24)
        # 查询最近30天记录
        thirtydaysdata = data_search(table=ProperNounIndex, time_interval=60 * 60 * 24 * 30)

        return_dict["onehourdata"] = onehourdata
        return_dict["onedaydata"] = onedaydata
        return_dict["thirtydaysdata"] = thirtydaysdata

    return render(request, "propernoun_input.html", return_dict)


def test(request, **kwargs):
    return render(request, "test.html", locals())
