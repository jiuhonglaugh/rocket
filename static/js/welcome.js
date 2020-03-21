var dt = {}
var arrs = ['cpu', 'mem', 'net', 'disk']
$(document).ready(function(){
    var arr = [];
    $.each($('input:checkbox:checked'),function(){
        arr.push($(this).val())
        });
    var time = $("#love5").val() * 1000
    start(arr,time)
});
$("#love5").mouseout(function(){
    var arr = [];
  	$.each($('input:checkbox:checked'),function(){
        arr.push($(this).val())
        });
    var time = $("#love5").val() * 1000
    start(arr,time)
});

$("#love1,#love2,#love3,#love4").click(function(){
    var arr = [];
    $.each($('input:checkbox:checked'),function(){
        arr.push($(this).val())
        });
        var time = $("#love5").val() * 1000
        start(arr,time)
    });

function start(arr,refreshTime){
    var str = arr.toString()
    for (var key in dt) {
　　     var value = dt[key];
         clearInterval(dt[value]);
    }
    for (var value of arrs) {
        var num = str.indexOf(value)
        if (num > -1 ){
            document.getElementById(value).style.display = "block";
            switch(value) {
                case 'cpu':
                    fnSearchCore()
                    dt[value] = setInterval(fnSearchCore,refreshTime);
                    break;
                case 'mem':
                    fnSearchMem()
                    dt[value]=setInterval(fnSearchMem,refreshTime);
                    break;
                case 'net':
                    fnSearchNet()
                    dt[value]=setInterval(fnSearchNet,refreshTime);
                    break;
                case 'disk':
                    fnSearchDisk()
                    dt[value]=setInterval(fnSearchDisk,refreshTime);
                    break;
                default:
                    alert('error')
                }
        }else{
             document.getElementById(value).style.display = "none";
        }
    }
    arr = []
}

function fnSearchMem(){
    var myChart = echarts.init(document.getElementById('mem'));
    var app = {
        xday:[],
        yvalue:[]
    };
    // 发送ajax请求，从后台获取json数据
    $(document).ready(function () {
       getData();
       console.log(app.xday);
       console.log(app.yvalue)
    });
    function getData() {
         $.ajax({
            url:'/host/mem',
            data:{},
            type:'GET',
            async:false,
            dataType:'json',
            success:function(data) {
                app.xday = data.xdays;
                app.yvalue = data.yvalues;
                myChart.setOption({
                    title: {
                        text: '内存使用率'
                    },
                    tooltip: {},
                    legend: {
                        data:['内存使用率']
                    },
                    xAxis: {
                        data: app.xday
                    },
                    yAxis: {},
                    series: [{
                        name: '内存使用率',
                        type: 'bar',
                        data: app.yvalue
                    }]
                })
            },
            error:function (msg) {
                console.log(msg);
                alert('系统发生错误');
            }
        })
    };
}
function fnSearchCore(){
    var myChart = echarts.init(document.getElementById('cpu'));
    var app = {
        xday:[],
        yvalue:[]
    };
    // 发送ajax请求，从后台获取json数据
    $(document).ready(function () {
       getData();
       console.log(app.xday);
       console.log(app.yvalue)
    });
    function getData() {
         $.ajax({
            url:'/host/core',
            data:{},
            type:'GET',
            async:false,
            dataType:'json',
            success:function(data) {
                title = data.title;
                time = data.time;
                data = data.data
                myChart.setOption({title: {
        text: 'CPU使用率'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: title
    },
    grid: {
        left: '4%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: time
    },
    yAxis: {
        type: 'value'
    },
    series: data
                })
            },
            error:function (msg) {
                console.log(msg);
                alert('系统发生错误');
            }
        })
    };
}
function fnSearchDisk(){
    var myChart = echarts.init(document.getElementById('disk'));
    var app = {
        xday:[],
        yvalue:[]
    };
    // 发送ajax请求，从后台获取json数据
    $(document).ready(function () {
       getData();
       console.log(app.xday);
       console.log(app.yvalue)
    });
    function getData() {
         $.ajax({
            url:'/host/disk',
            data:{},
            type:'GET',
            async:false,
            dataType:'json',
            success:function(data) {
                app.xday = data.xdays;
                app.yvalue = data.yvalues;
                myChart.setOption({
                    title: {
                        text: '磁盘使用率'
                    },
                    tooltip: {},
                    legend: {
                        data:['磁盘使用率']
                    },
                    xAxis: {
                        data: app.xday
                    },
                    yAxis: {},
                    series: [{
                        name: '磁盘使用率',
                        type: 'bar',
                        data: app.yvalue
                    }]
                })
            },
            error:function (msg) {
                console.log(msg);
                alert('系统发生错误');
            }
        })
    };
}
function fnSearchNet(){
    var myChart = echarts.init(document.getElementById('net'));
    var app = {
        xday:[],
        yvalue:[]
    };
    // 发送ajax请求，从后台获取json数据
    $(document).ready(function () {
       getData();
       console.log(app.xday);
       console.log(app.yvalue)
    });
    function getData() {
         $.ajax({
            url:'/host/net',
            data:{},
            type:'GET',
            async:false,
            dataType:'json',
            success:function(data) {
                title = data.title;
                time = data.time;
                data = data.data
                myChart.setOption({title: {
        text: '网络使用率'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: title
    },
    grid: {
        left: '4%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: time
    },
    yAxis: {
        type: 'value'
    },
    series: data
                })
            },
            error:function (msg) {
                console.log(msg);
                alert('系统发生错误');
            }
        })
    };
}