/**
 * Created by gintong on 2018-04-08.
 */
$(function(){
    $('#show_assets').bootstrapTable({
        url: "show_table",         //请求后台的URL（*）
        cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        //detailView:true,            //详情展示
        showRefresh: true,           //刷新按钮
        pageNumber: 1,                       //初始化加载第一页，默认第一页
        pageSize: 20,                       //每页的记录行数（*）
        pageList: [5, 10, 20, 50],            //可供选择的每页的行数（*）
        search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        pagination: true,
        clickToSelect: true,                //是否启用点击选中行
        uniqueId: "name",
        showToggle: true,                    //是否显示详细视图和列表视图的切换按钮
        cardView: false,                    //是否显示详细视图
        detailView: false,                  //是否显示父子表
        showColumns: true,                  //是否显示所有的列
        columns: [{checkbox: true},
            {field: 'assets_id', title: '资产ID', sortable: true},
            {field: 'assets_name', title: '资产名', sortable: true},
            {field: 'assets_brand', title: '品牌', sortable: true},
            {field: 'assets_version', title: '型号', sortable: true},
            {field: 'buying_price', title: '购买价格', sortable: true},
            {field: 'buying_date', title: '购买日期', sortable: true}
        ]
    });
    $(".panel-heading").click(function(e){
                /*切换折叠指示图标*/
                $(this).find("span").toggleClass("glyphicon-chevron-down");
                $(this).find("span").toggleClass("glyphicon-chevron-up");
    });
})
