var ids='';
    loginForSSH = function () {
        data = $('#sshLoginForm').serialize();
        layui.use(['layer'], function(){
        $ = layui.jquery;
        layer = layui.layer;
        var loading = layer.load({icon: 16, shade: 0.3, time:0})
        $.ajax({
            url: '/ssh/connect',
            dataType: "html",
            type: "POST",
            data: data,
            async: true,
            success: function (data) {
                layer.close(loading)
                resultCode = jQuery.parseJSON(data).resultCode;
                if (resultCode == '0') {
                    document.getElementById('loginbox').hidden=true;
                    ids=jQuery.parseJSON(data).ids;
                    var term = new Terminal();
                    term.open(document.getElementById('terms'));
                    term.on('data', function (data) {
                        $.ajax({
                            type:'POST',
                            dataType:'html',
                            url:'/ssh/sshInput',
                            data:{'ids':ids,'input':data},
                            success:function (data){
                            if(result.resultCode == 1){
                                clearInterval(getSSHResult);
                                term.destroy();
                                document.getElementById('loginbox').hidden=false;
                                };
                        }});
                    });
                   function getResult(){
                        data = {'ids':ids}
                        $.ajax({
                            type:'POST',
                            dataType:'html',
                            url:'/ssh/getSsh',
                            data:data,
                            success:function (data){
                                result = jQuery.parseJSON(data)
                                if(result.resultCode == 0){
                                    term.write(result.data);
                                 }
                                 else{
                                    clearInterval(getSSHResult);
                                    term.destroy();
                                    document.getElementById('loginbox').hidden=false;
                                 }
                            }

                        });
                   };
                    getSSHResult = setInterval(getResult,100);
                } else {
                    layer.open({
                            content: jQuery.parseJSON(data).result
                            ,title: '连接失败'
                            ,cancel: function(){
                                //右上角关闭回调
                                //return false 开启该代码可禁止点击该按钮关闭
                            }
                        });
//                    alert(jQuery.parseJSON(data).result,{title:false,skin: "layui-layer-molv",area: ["250px", "150px"],time: 10000,btn:["知道了"]})
                };
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                    layer.close(loading)
                    layer.open({
                        content: '服务器异常或者主机列表中已存在请检查主机列表或稍后再试'
                        ,cancel: function(){
                            //右上角关闭回调
                            //return false 开启该代码可禁止点击该按钮关闭
                        }
                    });
　　            }
        })
        });
        return false;
};
function keyLogin(){
    if(window.event.keyCode == 13){
        if (document.all('login-ssh') !=null ){
            document.all('login-ssh').click();
        }
    }
}