var ids='';
    loginForSSH = function () {
        data = $('#sshLoginForm').serialize();
        $.ajax({
            url: '/ssh/connect',
            dataType: "html",
            type: "POST",
            data: data,
            success: function (data) {
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
                    alert(jQuery.parseJSON(data).result,{title:false,skin: "layui-layer-molv",area: ["250px", "150px"],time: 10000,btn:["知道了"]})
                };
            }
        })
        return false;
};
function keyLogin(){
    if(window.event.keyCode == 13){
        if (document.all('login-ssh') !=null ){
            document.all('login-ssh').click();
        }
    }
}