var interval;

function Go_() {
    var content = document.title;
    var firstChar = content.charAt(0);
    var sub = content.substring(1, content.length);
    document.title = sub +firstChar;
}

function Go() {
    interval = setInterval("Go_()", 500);
}

Go();

function Stop() {
    clearInterval(interval);
}


/*//定义setTimeout执行方法
var time = null;

$('#full_2').click(function () {
    // 取消上次延时未执行的方法
    Stop();
    clearTimeout(time);
    //执行延时
    time = setTimeout(function(){
        //do function在此处写单击事件要执行的代码
        Go();
    },300);
});

$('#full_2').dblclick(functin () {
    // 取消上次延时未执行的方法
    Go();
    clearTimeout(time);
    //双击事件的执行代码
    Stop();
});*/

