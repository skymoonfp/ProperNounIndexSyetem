$(function() {
    UserPage("#user_page");
})


function UserPage(id) {
    $(id).bind("mouseenter", function() {
        $(this).siblings().removeClass("hide");
    })
    $(id).parent().bind("mouseleave", function() {
        $(id).siblings().addClass("hide");
    })
}


