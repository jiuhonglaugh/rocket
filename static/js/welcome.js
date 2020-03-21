
var arrs = ['cpu', 'mem', 'net', 'disk']
var cpuId = null
var memId = null
var netId = null
var diskId = null
/**
    获取所有 checkbox 的值
*/
function getCheckBoxs(){
    var arr = [];
    $.each($('input:checkbox:checked'),function(){
        arr.push($(this).val())
        });
    return arr;
    }

/**
    获取定时刷新的值
*/
function getTime(){
    var r= /^\+?[0-9][0-9]*$/;
    time = $("#love5").val().trim()
    if (!r.test(time) || time < 1 ){
        time = 5
        }
    return time * 1000
    }
/**
    刷新或第一次进入页面时
    立即展示数据并设置定时器
*/
$(document).ready(function(){
    refresh(getCheckBoxs(),getTime())
    });
/**
    设置定时器刷新时间鼠标离开
    input 输入框时刷新定时器
*/
$("#love5").mouseout(function(){
    refresh(getCheckBoxs(),getTime())
    });
/**
    点击checkBox时隐藏或开启对应的模块
    同时刷新定时器
*/
$("#love1,#love2,#love3,#love4").click(function(){
    refresh(getCheckBoxs(),getTime())
    });

/**
    刷新展示数据和刷新定时器
*/
function refresh(arr,refreshTime){
    clearInterval(cpuId)
    clearInterval(memId)
    clearInterval(netId)
    clearInterval(diskId)
    var str = arr.toString()
    for (var value of arrs) {
        var num = str.indexOf(value)
        if (num > -1 ){
            document.getElementById(value).style.display = "block";
            switch(value) {
                case 'cpu':
                    fnSearchCore()
                    cpuId = setInterval(fnSearchCore,refreshTime)
                    break;
                case 'mem':
                    fnSearchMem()
                    memId = setInterval(fnSearchMem,refreshTime)
                    break;
                case 'net':
                    fnSearchNet()
                    netId = setInterval(fnSearchNet,refreshTime)
                    break;
                case 'disk':
                    fnSearchDisk()
                    diskId = setInterval(fnSearchDisk,refreshTime)
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
/**
    获取 mem 数据并展示
*/
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
/**
    获取 cpu 数据并展示
*/
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

/**
    获取 disk 数据并展示
*/
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
/**
    获取 net 数据并展示
*/
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