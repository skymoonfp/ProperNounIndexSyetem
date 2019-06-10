$(function(){
    var per_item = $.cookie("page_num_onehour");
    if(per_item){
        $('#s1').val(per_item);
    } else {
        $.cookie("page_num_onehour", 12, {path: '/'});
    }
})

$(function(){
    var per_item = $.cookie("page_num_oneday");
    if(per_item){
        $('#s2').val(per_item);
    } else {
        $.cookie("page_num_oneday", 18, {path: '/'});
    }
})

$(function(){
    var per_item = $.cookie("page_num_thirtydays");
    if(per_item){
        $('#s3').val(per_item);
    } else {
        $.cookie("page_num_thirtydays", 12, {path: '/'});
    }
})


function ChangePageItem(id, name){
    var value = $(id).val();
    $.cookie(name, value, {path: '/'});
}


