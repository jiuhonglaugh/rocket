    <!-- 给所有的td标签添加双击可编辑属性 -->
$(document).ready(function() {
    $("#next").hide();
    var tds = $("td");
    tds.click(tdclick);
    tds.mouseout(close)
});
function tdclick() {
    var td = $(this);
    $("#next").hide();
    td.attr('contenteditable','true');
}
//function close(){
//    var td = $(this);
//    alert(td.children('input').val())
//    tmp = td.text().trim()
////    td.children('input').val(tmp);
//    td.children('input').attr('value',tmp);
//    alert(td.children('input').val())
//    td.attr('contenteditable','false');
//}

function close(){
    var td = $(this);
    tmp = td.text().trim()
    td.children('input').val(tmp)
    td.attr('contenteditable','false');
}