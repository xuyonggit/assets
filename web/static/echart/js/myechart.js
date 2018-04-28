$(function(){
    $.ajax({
        //提交数据的类型 POST GET
        type: 'POST',
        url: "/assets/echart/getdata/",
        data: {},
        dataType: "json",
        beforeSend: function () {
            $("#echart").html("loadding");
        }
        }).done(function (result) {
            var template = [];
            var datalist = [];
            for (i=0;i<result.length;i++){
                datalist.push(result[i]);
                template.push(result[i]['name'])
            }
        var myChart = echarts.init(document.getElementById('echart'));

        // 指定图表的配置项和数据
        var option = {
            baseOption: {
                title: {
                    text: '库存状态一览',
                    x: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: template
                },
                toolbox: {
                    show: true,
                    feature : {
                        mark : {show: true},
                        dataView : {show: true, readOnly: false},
                        magicType : {
                            show: true,
                            type: ['pie', 'funnel']
                        },
                    restore : {show: true},
                    saveAsImage : {show: true}
                    }
                },
                calculable : true,
                series: [{
                    name: '资产状态',
                    type: 'pie',
                    data: datalist,
                    lableLine: {
                        normal: {
                            show: false
                        },
                        emphasis: {
                            show: true
                        }
                    }
                }]
            }
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.onresize = myChart.resize;
        })
});