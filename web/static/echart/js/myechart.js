$(function(){
    var myChart = echarts.init(document.getElementById('echart'));
    $.ajax({
        //提交数据的类型 POST GET
        type: 'POST',
        url: "/assets/echart/getdata/",
        data: {},
        dataType: "json",
        beforeSend: function () {
            myChart.showLoading();
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
$(function () {
   var myChart = echarts.init(document.getElementById('echart2'));
   $.ajax({
        //提交数据的类型 POST GET
        type: 'POST',
        url: "/assets/echart/getdata2/",
        data: {},
        dataType: "json",
        beforeSend: function () {
            myChart.showLoading();
        }
   }).done(function (result) {
       var template = [];
       var used_list = [];
       var free_list = [];
       var trouble_list = [];
       for (i=0;i<result.length;i++){
           template.push(result[i]['name']);
           used_list.push(result[i]['used_num']);
           free_list.push(result[i]['free_num']);
           trouble_list.push(result[i]['trouble_num'])
            }
       myChart.hideLoading();
       var option = {
           title: {
                    text: '各种类别状态一览',
                    x: 'center'
                },
           tooltip: {
               trigger: 'axis',
               axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                   type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
               }
           },
           legend: {
               data: template
           },
           grid: {
               left: '3%',
               right: '4%',
               bottom: '3%',
               containLabel: true
           },
           yAxis: {
               type: 'value'
           },
           xAxis: {
               type: 'category',
               data: template
           },
           series: [
               {
                   name: '使用中',
                   color: '#4682B4',
                   type: 'bar',
                   stack: '总量',
                   label: {
                       normal: {
                           show: true,
                           position: 'insideTop'
                       }
                   },
                   data: used_list
               },
               {
                   name: '库房中',
                   color: '#7FFF00',
                   type: 'bar',
                   stack: '总量',
                   label: {
                       normal: {
                           show: true,
                           position: 'insideTop'
                       }
                   },
                   data: free_list
               }, {
                   name: '故障中',
                   color: '#FF0000',
                   type: 'bar',
                   stack: '总量',
                   label: {
                       normal: {
                           show: true,
                           position: 'insideTop'
                       }
                   },
                   data: trouble_list
               }
           ]
       };
       myChart.setOption(option);
       window.onresize = myChart.resize;
   });
});