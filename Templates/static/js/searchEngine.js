function SearchEngine(form_id, input_id) {
    var se_name = $("input[name='search_engine']:checked").val();
    //var se_name = $(id).parent().find("input[name='search_engine']:checked").val()

    if (se_name == "baidu") {
        var se_url = "https://www.baidu.com/s?";
        var url_id = document.getElementById(form_id);
        url_id.action = se_url
        var se_key = "wd";
        var key_id = document.getElementById(input_id);
        key_id.name = se_key;
    }

    else if (se_name == "google") {
        var se_url = "https://www.google.com.hk/search?";
        var url_id = document.getElementById(form_id);
        url_id.action = se_url
        var se_key = "q";
        var key_id = document.getElementById(input_id);
        key_id.name = se_key;
    }

    else if (se_name == "sogou") {
        var se_url = "https://www.sogou.com/tx?";
        var url_id = document.getElementById(form_id);
        url_id.action = se_url
        var se_key = "query";
        var key_id = document.getElementById(input_id);
        key_id.name = se_key;
    }
}