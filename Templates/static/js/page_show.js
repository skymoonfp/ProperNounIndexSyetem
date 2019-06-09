function PageShow(url) {
    var temp = $("#na").val();
    $.ajax({
        url: url,
        type: "POST",
        data: {dat:temp},
        success:function(arg){
            var obj = jQuery.parseJSON(arg);
            $().val(obj.data)

        },
        error:function(){

        }
    });
}