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
    data = $('#loginform').serialize();
    $.ajax({
        url: "/login",
        type: "POST",    //提交方式
        data: data,
        dataType: "json",
        async: true,
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        success:(function (data) {
            if (data.code != 200 ){
                showMes(data.data)
            }else{
                window.location.href="/index";
            }
            })
        })
    });
});
function showMes(data){
    $('.div1').show().html(data)
}
function keyLogin(){
    if(window.event.keyCode == 13){
        if (document.all('login') !=null ){
            document.all('login').click();
        }
    }
}