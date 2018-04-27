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
            var datalist = [];
            for (i=0;i<result.length;i++){
                datalist.push(result[i]);
            }
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart'));

        // 指定图表的配置项和数据
        var option = {
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
                data: ['库存中','使用中','故障','未知']
            },
            series: [{
                name: '资产状态',
                type: 'pie',
                data: datalist,
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        })
})