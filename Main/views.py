# Create your views here.

from django.http.response import *

from Main import forms
from Main.models import *
from Main.utility.html_helper import *
from Main.utility.search_helper import *
from Main.utility.session_helper import *
from Main.utility.transfer_helper import *


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
        # print(userinfo)
        if len(userinfo) != 1:
            erro["erro_verify"] = r"该用户不存在！请注册！"
            return render(request, "login.html", erro)
        else:
            userinfo = UserInfo.objects.filter(username=user, password=pwd)
            if len(userinfo) == 0:
                erro["erro_verify"] = r"密码错误！"
                return render(request, "login.html", erro)
            else:
                request.session["userinfo"] = {"is_login": True, "user": user, "pwd": pwd}
                print("session的值", request.session.get("userinfo"))
                # erro["erro_verify"] = mark_safe("<button><a herf='/Main/books_input/'>请进入操作页面！</a></button>")
                return render(request, "books_input.html", erro)

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
@login_session
def search(request, *args, **kwargs):
    userinfo = request.session.get("userinfo", None)
    return_dict = {"user": userinfo["user"]}

    return render(request, "search.html", return_dict)

# 书籍录入
@login_session
def books_input(request, *args, **kwargs):
    # userinfo = request.session.get("userinfo", None)
    # print("aaa", userinfo)
    # if userinfo["is_login"]:
    #     pass
    # else:
    #     print("错误")

    # print("bbb", request.session, request.session.session_key)
    # print("session的值", request.session.get("userinfo"))

    userinfo = request.session.get("userinfo", None)
    return_dict = {"user": userinfo["user"]}

    per_item_onehour = try_int(request.COOKIES.get("page_num_onehour", 10), 10)
    per_item_oneday = try_int(request.COOKIES.get("page_num_oneday", 10), 10)
    per_item_thirtydays = try_int(request.COOKIES.get("page_num_thirtydays", 10), 10)
    time_interval_books = request.COOKIES.get("time_interval_books", "onehour")

    # 创建返回form对象
    booksBack = forms.BooksInput()

    # 获取checkbox值
    check = request.POST.getlist("book_input_check", "")

    # 返回字典添加form对象
    # return_dict = dict()
    return_dict["books_input"] = booksBack

    # 根据request.method决定是否传入数据库
    if request.method == "POST":
        data = {}
        booksInput = forms.BooksInput(request.POST)
        if booksInput.is_valid():
            data = booksInput.cleaned_data
            # print("输入数据：", data)
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

    # print(page_url)

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
    onehour_page = PageInfo("/Main/books_input/", page_name_judge(page_url)[0], onehourdata_count, per_item_onehour)
    oneday_page = PageInfo("/Main/books_input/", page_name_judge(page_url)[1], onedaydata_count, per_item_oneday)
    thirtydays_page = PageInfo("/Main/books_input/", page_name_judge(page_url)[2], thirtydaysdata_count,
                               per_item_thirtydays)

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

    # print(return_dict)

    response = render(request, "books_input.html", return_dict)

    response.set_cookie("page_num_onehour", per_item_onehour)
    response.set_cookie("page_num_oneday", per_item_oneday)
    response.set_cookie("page_num_thirtydays", per_item_thirtydays)
    response.set_cookie("time_interval_books", time_interval_books)
    print(time_interval_books)

    return response


# 专名录入
@login_session
def propernoun_input(request, **kwargs):
    userinfo = request.session.get("userinfo", None)
    return_dict = {"user": userinfo["user"]}

    per_item_onehour_propernoun = try_int(request.COOKIES.get("page_num_onehour_propernoun", 10), 10)
    per_item_oneday_propernoun = try_int(request.COOKIES.get("page_num_oneday_propernoun", 10), 10)
    per_item_thirtydays_propernoun = try_int(request.COOKIES.get("page_num_thirtydays_propernoun", 10), 10)
    time_interval_propernoun = request.COOKIES.get("time_interval_propernoun", "onehour")

    # 创建返回form对象
    propernounBack = forms.ProperNounInput()

    # 获取checkbox值
    check = request.POST.getlist("propernounBack_input_check", "")

    # 返回字典添加form对象
    return_dict["propernoun_input"] = propernounBack

    # 根据request.method决定是否传入数据库
    if request.method == "POST":
        data = {}
        propernounInput = forms.ProperNounInput(request.POST)
        if propernounInput.is_valid():
            data = propernounInput.cleaned_data
            # print("输入数据：", data)
            ProperNounIndex.objects.create(**data)
            return_dict["nouns_input_status"] = "提交成功！"

        # 根据复选框决定提交数据后的数据显示情况
        for key in data.keys():
            if key in check:
                pass
            else:
                data[key] = ""
        propernounBack = forms.BooksInput(data)
        return_dict["propernoun_input"] = propernounBack

    # 查询最近1小时记录
    onehourdata_propernoun = data_search(table=ProperNounIndex, time_interval=60 * 60)
    print(onehourdata_propernoun)
    onehourdata_count_propernoun = data_search_count(onehourdata_propernoun)
    # 查询最近1天记录
    onedaydata_propernoun = data_search(table=ProperNounIndex, time_interval=60 * 60 * 24)
    print(onedaydata_propernoun)
    onedaydata_count_propernoun = data_search_count(onedaydata_propernoun)
    # 查询最近30天记录
    thirtydaysdata_propernoun = data_search(table=ProperNounIndex, time_interval=60 * 60 * 24 * 30)
    thirtydaysdata_count_propernoun = data_search_count(thirtydaysdata_propernoun)

    # 返回字典中添加记录总条数
    return_dict["onehourdata_count_propernoun"] = onehourdata_count_propernoun
    return_dict["onedaydata_count_propernoun"] = onedaydata_count_propernoun
    return_dict["thirtydaysdata_count_propernoun"] = thirtydaysdata_count_propernoun

    # 获取page_url，如果为空，设置为"onehour_1"
    try:
        page_url = kwargs["id"]  # 输入页数时
    except Exception:
        page_url = "onehour_1"

    # 分页
    onehour_page_propernoun = PageInfo("/Main/propernoun_input/", page_name_judge(page_url)[0],
                                       onehourdata_count_propernoun, per_item_onehour_propernoun)
    oneday_page_propernoun = PageInfo("/Main/propernoun_input/", page_name_judge(page_url)[1],
                                      onedaydata_count_propernoun, per_item_oneday_propernoun)
    thirtydays_page_propernoun = PageInfo("/Main/propernoun_input/", page_name_judge(page_url)[2],
                                          thirtydaysdata_count_propernoun,
                                          per_item_thirtydays_propernoun)

    # 返回字典中添加页码标签
    return_dict["page_onehour_propernoun"] = onehour_page_propernoun.pagify()
    return_dict["page_oneday_propernoun"] = oneday_page_propernoun.pagify()
    return_dict["page_thirtydays_propernoun"] = thirtydays_page_propernoun.pagify()

    # 返回字典中添加每页记录
    return_dict["onehourdata_propernoun"] = onehourdata_propernoun[
                                            onehour_page_propernoun.start:onehour_page_propernoun.over]
    return_dict["onedaydata_propernoun"] = onedaydata_propernoun[
                                           oneday_page_propernoun.start:oneday_page_propernoun.over]
    return_dict["thirtydaysdata_propernoun"] = thirtydaysdata_propernoun[
                                               thirtydays_page_propernoun.start:thirtydays_page_propernoun.over]

    # 返回字典中添加当前页记录在总记录中的起止位置（无记录从0开始，有记录从1开始）
    if onehourdata_count_propernoun == 0:
        return_dict["onehourdata_page_count_propernoun"] = str(onehour_page_propernoun.start) + "-" + str(
            onehour_page_propernoun.over)
    else:
        return_dict["onehourdata_page_count_propernoun"] = str(onehour_page_propernoun.start + 1) + "-" + str(
            onehour_page_propernoun.over)
    if onedaydata_count_propernoun == 0:
        return_dict["onedaydata_page_count_propernoun"] = str(oneday_page_propernoun.start) + "-" + str(
            oneday_page_propernoun.over)
    else:
        return_dict["onedaydata_page_count_propernoun"] = str(oneday_page_propernoun.start + 1) + "-" + str(
            oneday_page_propernoun.over)
    if thirtydaysdata_count_propernoun == 0:
        return_dict["thirtydaysdata_page_count_propernoun"] = str(thirtydays_page_propernoun.start) + "-" + str(
            thirtydays_page_propernoun.over)
    else:
        return_dict["thirtydaysdata_page_count_propernoun"] = str(thirtydays_page_propernoun.start + 1) + "-" + str(
            thirtydays_page_propernoun.over)

    response = render(request, "propernoun_input.html", return_dict)

    response.set_cookie("page_num_onehour_propernoun", per_item_onehour_propernoun)
    response.set_cookie("page_num_oneday_propernoun", per_item_oneday_propernoun)
    response.set_cookie("page_num_thirtydays_propernoun", per_item_thirtydays_propernoun)
    response.set_cookie("time_interval_propernoun", time_interval_propernoun)

    return response


@login_session
def test(request, **kwargs):
    return render(request, "test.html", locals())
