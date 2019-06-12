//登陆用户名
$(document).ready(function(){
    $("input.username_log:text").val("请输入用户名");
    $("input.username_log").css({"background-color":"white", "color":"grey"});

    $("input.username_log").focus(function(){
        if ($("input.username_log:text").val() == "请输入用户名" || $("input.username_log:text").val().trim() == "") {
            $("input.username_log:text").val("");
            $("input.username_log").css({"background-color":"#FFFFCC", "color":"blue"});
        } else {
            $("input.username_log").css({"background-color":"#FFFFCC", "color":"blue"});
        }
    });

    $("input.username_log").blur(function(){
        if ($("input.username_log:text").val() == "请输入用户名" || $("input.username_log:text").val().trim() == "") {
            $("input.username_log:text").val("请输入用户名");
            $("input.username_log").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.username_log").css("background-color","#D6D6FF");
        }
    });
});


//登陆暗文pwd
$(document).ready(function(){
    $("input.password_log").css({"background-color":"white", "color":"grey"});

    $("input.password_log").focus(function(){
        $("input.password_log").css({"background-color":"#FFA07A", "color":"blue"});
    });

    $("input.password_log").blur(function(){
         if ($("input.password_log").val().trim() == "") {
            $("input.password_log").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.password_log").css("background-color","#D6D6FF");}
    });
});


//登陆明文pwd
/*$(document).ready(function(){
    $("input.password_log:text").val("请输入密码");
    $("input.password_log").css({"background-color":"white", "color":"grey"});

    $("input.password_log").focus(function(){
        if ($("input.password_log:text").val() == "请输入密码" || $("input.password_log:text").val().trim() == "") {
            $("input.password_log:text").val("");
            $("input.password_log").css({"background-color":"#FFA07A", "color":"blue"});
        }
        $("input.password_log").css({"background-color":"#FFA07A", "color":"blue"});
    });

    $("input.password_log").blur(function(){
        if ($("input.password_log:text").val() == "请输入密码" || $("input.password_log:text").val().trim() == "") {
            $("input.password_log:text").val("请输入密码");
            $("input.password_log").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.password_log").css("background-color","#D6D6FF");
        }
    });
});*/


//注册用户名
$(document).ready(function(){
    $("input.username_reg:text").val("请输入用户名");
    $("input.username_reg").css({"background-color":"white", "color":"grey"});

    $("input.username_reg").focus(function(){
        if ($("input.username_reg:text").val() == "请输入用户名" || $("input.username_reg:text").val().trim() == "") {
            $("input.username_reg:text").val("");
            $("input.username_reg").css({"background-color":"#FFFFCC", "color":"blue"});
        } else {
            $("input.username_reg").css({"background-color":"#FFFFCC", "color":"blue"});
        }
    });

    $("input.username_reg").blur(function(){
        if ($("input.username_reg:text").val() == "请输入用户名" || $("input.username_reg:text").val().trim() == "") {
            $("input.username_reg:text").val("请输入用户名");
            $("input.username_reg").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.username_reg").css("background-color","#D6D6FF");
        }
    });
});


//注册暗文pwd
$(document).ready(function(){
    $("input.password_reg").css({"background-color":"white", "color":"grey"});

    $("input.password_reg").focus(function(){
        $("input.password_reg").css({"background-color":"#FFA07A", "color":"blue"});
    });

    $("input.password_reg").blur(function(){
         if ($("input.password_reg").val().trim() == "") {
            $("input.password_reg").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.password_reg").css("background-color","#D6D6FF");}
    });
});


//注册暗文pwd确认
$(document).ready(function(){
    $("input.password_reg2").css({"background-color":"white", "color":"grey"});

    $("input.password_reg2").focus(function(){
        $("input.password_reg2").css({"background-color":"#FFA07A", "color":"blue"});
    });

    $("input.password_reg2").blur(function(){
         if ($("input.password_reg2").val().trim() == "") {
            $("input.password_reg2").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.password_reg2").css("background-color","#D6D6FF");}
    });
});


//注册明文pwd
/*$(document).ready(function(){
    $("input.password_reg:text").val("请输入密码");
    $("input.password_reg").css({"background-color":"white", "color":"grey"});

    $("input.password_reg").focus(function(){
        if ($("input.password_reg:text").val() == "请输入密码" || $("input.password_reg:text").val().trim() == "") {
            $("input.password_reg:text").val("");
            $("input.password_reg").css({"background-color":"#FFA07A", "color":"blue"});
        }
        $("input.password_reg").css({"background-color":"#FFA07A", "color":"blue"});
    });

    $("input.password_reg").blur(function(){
        if ($("input.password_reg:text").val() == "请输入密码" || $("input.password_reg:text").val().trim() == "") {
            $("input.password_reg:text").val("请输入密码");
            $("input.password_reg").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.password_reg").css("background-color","#D6D6FF");
        }
    });
});*/


//注册明文pwd确认
/*$(document).ready(function(){
    $("input.password_reg2:text").val("请再次输入密码");
    $("input.password_reg2").css({"background-color":"white", "color":"grey"});

    $("input.password_reg2").focus(function(){
        if ($("input.password_reg2:text").val() == "请再次输入密码" || $("input.password_reg2:text").val().trim() == "") {
            $("input.password_reg2:text").val("");
            $("input.password_reg2").css({"background-color":"#FFA07A", "color":"blue"});
        }
        $("input.password_reg2").css({"background-color":"#FFA07A", "color":"blue"});
    });

    $("input.password_reg2").blur(function(){
        if ($("input.password_reg2:text").val() == "请再次输入密码" || $("input.password_reg2:text").val().trim() == "") {
            $("input.password_reg2:text").val("请再次输入密码");
            $("input.password_reg2").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.password_reg2").css("background-color","#D6D6FF");
        }
    });
});*/


//注册出生日期
$(document).ready(function(){
    $("input.birthday_reg:text").val("请输入出生日期");
    $("input.birthday_reg").css({"background-color":"white", "color":"grey"});

    $("input.birthday_reg").focus(function(){
        if ($("input.birthday_reg:text").val() == "请输入出生日期" || $("input.birthday_reg:text").val().trim() == "") {
            $("input.birthday_reg:text").val("");
            $("input.birthday_reg").css({"background-color":"#7FFF00", "color":"blue"});
        } else {
            $("input.birthday_reg").css({"background-color":"#7FFF00", "color":"blue"});
        }
    });

    $("input.birthday_reg").blur(function(){
        if ($("input.birthday_reg:text").val() == "请输入出生日期" || $("input.birthday_reg:text").val().trim() == "") {
            $("input.birthday_reg:text").val("请输入出生日期");
            $("input.birthday_reg").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.birthday_reg").css("background-color","#D6D6FF");
        }
    });
});


//注册电子邮箱
$(document).ready(function(){
    $("input.e_mail_reg:text").val("请输入电子邮箱");
    $("input.e_mail_reg").css({"background-color":"white", "color":"grey"});

    $("input.e_mail_reg").focus(function(){
        if ($("input.e_mail_reg:text").val() == "请输入电子邮箱" || $("input.e_mail_reg:text").val().trim() == "") {
            $("input.e_mail_reg:text").val("");
            $("input.e_mail_reg").css({"background-color":"#7FFF00", "color":"blue"});
        } else {
            $("input.e_mail_reg").css({"background-color":"#7FFF00", "color":"blue"});
        }
    });

    $("input.e_mail_reg").blur(function(){
        if ($("input.e_mail_reg:text").val() == "请输入电子邮箱" || $("input.e_mail_reg:text").val().trim() == "") {
            $("input.e_mail_reg:text").val("请输入电子邮箱");
            $("input.e_mail_reg").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.e_mail_reg").css("background-color","#D6D6FF");
        }
    });
});


//注册手机号
$(document).ready(function(){
    $("input.mobile_reg:text").val("请输入手机号");
    $("input.mobile_reg").css({"background-color":"white", "color":"grey"});

    $("input.mobile_reg").focus(function(){
        if ($("input.mobile_reg:text").val() == "请输入手机号" || $("input.mobile_reg:text").val().trim() == "") {
            $("input.mobile_reg:text").val("");
            $("input.mobile_reg").css({"background-color":"#00BFFF", "color":"blue"});
        } else {
            $("input.mobile_reg").css({"background-color":"#00BFFF", "color":"blue"});
        }
    });

    $("input.mobile_reg").blur(function(){
        if ($("input.mobile_reg:text").val() == "请输入手机号" || $("input.mobile_reg:text").val().trim() == "") {
            $("input.mobile_reg:text").val("请输入手机号");
            $("input.mobile_reg").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.mobile_reg").css("background-color","#D6D6FF");
        }
    });
});


//注册身份证号
$(document).ready(function(){
    $("input.identify_code_reg:text").val("请输入身份证号");
    $("input.identify_code_reg").css({"background-color":"white", "color":"grey"});

    $("input.identify_code_reg").focus(function(){
        if ($("input.identify_code_reg:text").val() == "请输入身份证号" || $("input.identify_code_reg:text").val().trim() == "") {
            $("input.identify_code_reg:text").val("");
            $("input.identify_code_reg").css({"background-color":"#00BFFF", "color":"blue"});
        } else {
            $("input.identify_code_reg").css({"background-color":"#00BFFF", "color":"blue"});
        }
    });

    $("input.identify_code_reg").blur(function(){
        if ($("input.identify_code_reg:text").val() == "请输入身份证号" || $("input.identify_code_reg:text").val().trim() == "") {
            $("input.identify_code_reg:text").val("请输入身份证号");
            $("input.identify_code_reg").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.identify_code_reg").css("background-color","#D6D6FF");
        }
    });
});