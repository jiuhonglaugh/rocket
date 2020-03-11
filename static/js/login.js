$(function () {
    $('#login').click(function () {
    //获取用户名和密码:
    username = $('#username').val();
    password = $('#password').val();
    if(!username || username == ""){
        showMes("请输入用户名");
        fm.username.focus();
        return false;
    }
    if(!password || password == ""){
        showMes("请输入密码");
        fm.password.focus ();
        return false;
    }
                // alert(rember);
    $.ajax({
        url:"/login",
        type:"POST",    //提交方式
        data:{"username":username,"password":password},
        dataType:"text",
        contentType:"application/x-www-form-urlencoded; charset=utf-8",
        success:(function (data) {
            if (data != ""){
                showMes(data)
            }
            })
        })
    });
});
function showMes(data){
    $('.div1').show().html(data)
}