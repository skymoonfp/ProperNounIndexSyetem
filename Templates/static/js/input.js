$(document).ready(function(){
    $("input.username:text").val("请输入用户名");
    $("input.username").css({"background-color":"white", "color":"grey"});

    $("input.username").focus(function(){
        if ($("input.username:text").val() == "请输入用户名" || $("input.username:text").val().trim() == "") {
            $("input.username:text").val("");
            $("input.username").css({"background-color":"#FFFFCC", "color":"blue"});
        }
    });

    $("input.username").blur(function(){
        if ($("input.username:text").val() == "请输入用户名" || $("input.username:text").val().trim() == "") {
            $("input.username:text").val("请输入用户名");
            $("input.username").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.username").css("background-color","#D6D6FF");
        }
    });
});


//暗文pwd
$(document).ready(function(){
    $("input.password").css({"background-color":"white", "color":"grey"});

    $("input.password").focus(function(){
        $("input.password").css({"background-color":"#FFA07A", "color":"blue"});
    });

    $("input.password").blur(function(){
         if ($("input.password").val().trim() == "") {
            $("input.password").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.password").css("background-color","#D6D6FF");}
    });
});


//明文pwd
/*$(document).ready(function(){
    $("input.password:text").val("请输入密码");
    $("input.password").css({"background-color":"white", "color":"grey"});

    $("input.password").focus(function(){
        if ($("input.password:text").val() == "请输入密码" || $("input.password:text").val().trim() == "") {
            $("input.password:text").val("");
            $("input.password").css({"background-color":"#FFA07A", "color":"blue"});
        }
        $("input.password").css({"background-color":"#FFA07A", "color":"blue"});
    });

    $("input.password").blur(function(){
        if ($("input.password:text").val() == "请输入密码" || $("input.password:text").val().trim() == "") {
            $("input.password:text").val("请输入密码");
            $("input.password").css({"background-color":"white", "color":"grey"});
        } else {
            $("input.password").css("background-color","#D6D6FF");
        }
    });
});*/
