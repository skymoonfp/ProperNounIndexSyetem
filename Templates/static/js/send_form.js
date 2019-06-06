/*注册*/
function CheckPost (form_id) {

    var form = document.getElementById(form_id);
    var element = document.getElementById("error_reg");

    /*必填项是否为空*/
    if (form.username_2.value == "请输入用户名" || form.username_2.value.trim() == "") {
        element.innerHTML="用户名不能为空！";
        form.username_2.focus();
        return false;
      } else

    if (form.password_2.value == "请输入密码" || form.password_2.value.trim() == "") {
        element.innerHTML="密码不能为空！";
        form.password_2.focus();
        return false;
      } else

    if (form.password_3.value == "请再次输入密码" || form.password_3.value.trim() == "") {
        element.innerHTML="确认密码不能为空！";
        form.password_3.focus();
        return false;
      } else

    /*两次密码是否一致*/
    if (form.password_2.value != form.password_3.value) {
        element.innerHTML="密码不一致！";
        form.password_2.focus();
        return false;
      } else

    /*用户名和密码是否雷同*/
    if (form.password_2.value == form.username_2.value) {
        element.innerHTML="用户名和密码不可相同！";
        form.username_2.focus();
        return false;
      } else

    /*出生日期是否符合格式*/
    if (form.birthday.value != "请输入出生日期" && form.birthday.value.trim() != "") {
        var reg= /(19|20)[0-9]{2}-[0-1][0-9]-[0-3][0-9]/;
        if (reg.test(form.birthday.value)==false) {
            element.innerHTML="生日格式不对！";
            form.birthday.focus();
            return false;
        }
      } else

    /*电子邮箱是否符合格式*/
    if (form.e_mail.value != "请输入电子邮箱" && form.e_mail.value.trim() != "") {
        var reg= /\w+@\w+.\w+/;
        if (reg.test(form.e_mail.value)==false) {
            element.innerHTML="电子邮箱格式不对！";
            form.e_mail.focus();
            return false;
        }
      } else

    /*手机号是否符合格式*/
    if (form.mobile.value != "请输入手机号" && form.mobile.value.trim() != "") {
        var reg= /[0-9]{11}/;
        if (reg.test(form.mobile.value)==false) {
            element.innerHTML="手机号格式不对！";
            form.mobile.focus();
            return false;
        }
      } else

    /*身份证号是否符合格式*/
    if (form.identify_code.value != "请输入身份证号" && form.identify_code.value.trim() != "") {
        var reg= /[0-9]{18}/;
        if (reg.test(form.identify_code.value)==false) {
            element.innerHTML="身份证号格式不对！";
            form.identify_code.focus();
            return false;
        }
      } else

     return true;
}


/*登录*/
function CheckPost2 (form_id) {

    var form = document.getElementById(form_id);
    var element = document.getElementById("error_log");

    /*必填项是否为空*/
    if (form.username_1.value == "请输入用户名" || form.username_1.value.trim() == "") {
        element.innerHTML="用户名不能为空！";
        form.username_1.focus();
        return false;
      } else

    if (form.password_1.value == "请输入密码" || form.password_1.value.trim() == "") {
        element.innerHTML="密码不能为空！";
        form.password_1.focus();
        return false;
      } else

     return true;
}