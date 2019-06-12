//按钮切换显示区域
//tab 结果显示区
$(function() {
    ChangeTab("#display_menu_title", "#display_menu_body");
})

$(function() {
    ChangeTab("#search_menu_title", "#search_menu_body");
})

$(function() {
    ChangeTab("#tool_menu_title", "#tool_menu_body");
})

$(function() {
    ChangeTab("#tab-menu-title", "#tab-menu-body");
})

$(function() {
    ChangeTab("#tab-menu-title2", "#tab-menu-body2");
})



function ChangeTab(title, body) {

    /*for (li in $(title).children()) {
        if (li.attr("class")="current") {
            $content = $(body).find('div[content="' + li.attr("content-to") + '"]');
            $content.removeClass("hide").siblings().addClass("hide");
        }
    }*/

    $(title).children().bind("click", function() {
        var $menu = $(this);
        $menu.addClass("current").siblings().removeClass("current");

        var $contentValue = $(this).attr("content-to");
        $content = $(body).find('div[content="' + $contentValue + '"]');
        $content.removeClass("hide").siblings().addClass("hide");

        $.cookie("time_interval", $contentValue, {path: '/'});
    });
}



//当前按钮信息存入cookie
//tab 结果显示区
/*function TimeIntervalMenu (ul_id){
    for (i = 0; i < 3; i++) {
        if ($(ul_id).children()[i].attr("class") == "current") {
            $.cookie("time_interval", $(ul_id).children()[i].attr("content-to"), {path: '/'});
        }
    }
}*/

function ChangeTime(button_id){
    $(button_id).trigger("click");
}

$(function(){
    //TimeIntervalMenu("#display_menu_title");
    var time_interval = $.cookie("time_interval");
    if (time_interval == "onehour"){
        ChangeTime("#onehour_button");
    } else
    if (time_interval == "oneday"){
        ChangeTime("#oneday_button");
    } else
    if (time_interval == "thirtydays"){
        ChangeTime("#thirtydays_button");
    }
})
