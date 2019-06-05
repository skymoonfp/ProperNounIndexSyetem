

$(function() {
    ChangeTab("#tab-menu-title", "#tab-menu-body");
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
    });
}