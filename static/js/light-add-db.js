
//用来记录清空后的ID值
var inputId = ''
    <!-- 给所有的td标签添加双击可编辑属性 -->
$(document).ready(function() {
    $("#next").hide();
    var tds = $("td");
    tds.click(tdclick);
    tds.mouseout(close)
});
function tdclick() {
    var td = $(this);
    inputId = td.children('input').attr('id')
    $("#next").hide();
    td.attr('contenteditable','true');
}

function close(){
    var td = $(this);
    tmp = td.text().trim()
    if (tmp == ""){
        inputTag = "<input hidden='hidden' lay-verify='" + inputId + "' lay-filter='" + inputId+ "' name='" + inputId +"'>"
        td.append(inputTag)
        td.children('input').val(tmp)
    }else if(td.children().length == 0){
        inputTag = "<input hidden='hidden' lay-verify='" + inputId + "' lay-filter='" + inputId+ "' name='" + inputId +"'>"
        td.append(inputTag)
        td.children('input').val(tmp)
    }
    else{
        td.children('input').val(tmp)
    }
    td.attr('contenteditable','false');
}