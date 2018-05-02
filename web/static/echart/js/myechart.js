$(function(){
    var myChart = echarts.init(document.getElementById('echart'));
    $.ajax({
        //提交数据的类型 POST GET
        type: 'POST',
        url: "/assets/echart/getdata/",
        data: {},
        dataType: "json",
        beforeSend: function () {
            myChart.showLoading();;
        }
        }).done(function (result) {
            var template = [];
            var datalist = [];
            for (i=0;i<result.length;i++){
                datalist.push(result[i]);
                template.push(result[i]['name'])
            }

        myChart.hideLoading();
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
                color: ['#dd6b66','#759aa0','#e69d87','#8dc1a9','#ea7e53','#eedd78','#73a373','#73b9bc','#7289ab', '#91ca8c','#f49f42'],
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