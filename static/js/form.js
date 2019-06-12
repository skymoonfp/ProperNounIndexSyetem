//复选框onclick事件：点击全选，再次点击全不选
function check(checkboxall_id, checkbox_name){
    //添加外部判断：奇数点击时value为1，全不选，否则全选，如此可以在反选与全选间衍生出极端选择的方案
    var checkbox = document.getElementById(checkboxall_id);
    //value初始化为1，此处的三目执行后value一定不为1，而页面初始化时checkbox都为未选中状态，所以value为1时全不选
    checkbox.value==1?checkbox.value=2 : checkbox.value=1;
    var checkboxs = document.getElementsByName(checkbox_name);
    for(var i=0; i<checkboxs.length;i++){
        if(checkbox.value==1){
        checkboxs[i].checked=false;//全不选
        }else{
        checkboxs[i].checked=true;//全选
        }
}}



//ModelForm选择框格式内容
$(function(){
    ChangeModelForm("#id_noun_property");
})

function ChangeModelForm(id) {
    //$(id).find("label[for='id_noun_property_0']").addClass("hide");
    $(id).find("label[for='id_noun_property_0']").html("");
    $(id).find("label[for='id_noun_property_1']").html('人名<input name="noun_property" id="id_noun_property_1" required="" type="radio" value="1">');
    $(id).find("label[for='id_noun_property_2']").html('地名<input name="noun_property" id="id_noun_property_2" required="" type="radio" value="2">');
    $(id).find("label[for='id_noun_property_3']").html('其他<input name="noun_property" id="id_noun_property_3" required="" type="radio" value="3">');
}

