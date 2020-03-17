$(document).ready(function(){
fnSearchMem()
fnSearchCore()
fnSearchNet()
fnSearchDisk()
});
//interval1=setInterval(fnSearchMem,2000);
//interval1=setInterval(fnSearchCore,2000);
//interval1=setInterval(fnSearchNet,2000);
//interval1=setInterval(fnSearchDisk,2000);

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
            url:'/mem',
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
            url:'/core',
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
            url:'/disk',
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
            url:'/net',
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