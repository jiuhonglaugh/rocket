$(document).ready(function(){
fnSearchMem()
fnSearchCore()
});
interval1=setInterval(fnSearchMem,2000);
interval1=setInterval(fnSearchCore,2000);

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
            url:'/echart',
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
                        data:['内存GB']
                    },
                    xAxis: {
                        data: app.xday
                    },
                    yAxis: {},
                    series: [{
                        name: '内存GB',
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
    var myChart = echarts.init(document.getElementById('core'));

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
            url:'/discount',
            data:{},
            type:'GET',
            async:false,
            dataType:'json',
            success:function(data) {
                title = data.title;
                time = data.time;
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
    series: [
        {
            name: title[0],
            type: 'line',
            stack: '总量',
            data: data.hadoop01_data
        },
        {
            name: title[1],
            type: 'line',
            stack: '总量',
            data: data.hadoop02_data
        },
        {
            name: title[2],
            type: 'line',
            stack: '总量',
            data: data.hadoop03_data
        },
        {
            name: title[3],
            type: 'line',
            stack: '总量',
            data: data.hadoop04_data
        },
        {
            name: title[4],
            type: 'line',
            stack: '总量',
            data: data.hadoop05_data
        }
    ]
                })
            },
            error:function (msg) {
                console.log(msg);
                alert('系统发生错误');
            }
        })
    };
}
