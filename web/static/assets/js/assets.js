/**
 * Created by gintong on 2018-04-08.
 */
$(function(){
    $(document).ready(function() {
        $("#mws-login-form form").validate({
            rules: {
                username: {required: true},
                password: {required: true}
            },
            errorPlacement: function(error, element) {
            },
            invalidHandler: function(form, validator) {
                if($.fn.effect) {
                    $("#mws-login").effect("shake", {distance: 6, times: 2}, 35);
                }
            }
        });

    });
    $('#show_assets').bootstrapTable({
        method: 'post',
        url: "/assets/show_assets/",         //请求后台的URL（*）
        contentType : "application/x-www-form-urlencoded",
        cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        //detailView:true,            //详情展示
        //sidePagination: "server",
        showRefresh: true,           //刷新按钮
        pageNumber: 1,                       //初始化加载第一页，默认第一页
        pageSize: 30,                       //每页的记录行数（*）
        pageList: [5, 10, 20, 50],            //可供选择的每页的行数（*）
        search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        pagination: true,
        clickToSelect: true,                //是否启用点击选中行
        uniqueId: "assets_name",
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
            {field: 'buying_date', title: '购买日期', sortable: true},
            {field: 'asset_status', title:'状态', sortable:true,
            formatter: function(value,row,index) {
                var aa = "";
                if(value == "1"){
                    var aa = '<span style="color:black">使用中</span>';
                }else if(value == "2"){
                    var aa = '<span style="color:green">闲置中</span>';
                }else{
                    var aa = '<span style="color:red">未知</span>'
                }
                return aa;
            }
            }
        ]
    });
    $('#show_assets_free').bootstrapTable({
        method: 'post',
        url: "/assets/show_assets_free/",         //请求后台的URL（*）
        contentType : "application/x-www-form-urlencoded",
        cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        //detailView:true,            //详情展示
        //sidePagination: "server",
        showRefresh: true,           //刷新按钮
        pageNumber: 1,                       //初始化加载第一页，默认第一页
        pageSize: 30,                       //每页的记录行数（*）
        pageList: [5, 10, 20, 50],            //可供选择的每页的行数（*）
        search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        pagination: true,
        clickToSelect: true,                //是否启用点击选中行
        uniqueId: "assets_name",
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
            {field: 'buying_date', title: '购买日期', sortable: true},
        ]
    });
    $('#show_assets_used').bootstrapTable({
        method: 'post',
        url: "/assets/show_assets_used/",         //请求后台的URL（*）
        contentType : "application/x-www-form-urlencoded",
        cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        //detailView:true,            //详情展示
        //sidePagination: "server",
        showRefresh: true,           //刷新按钮
        pageNumber: 1,                       //初始化加载第一页，默认第一页
        pageSize: 30,                       //每页的记录行数（*）
        pageList: [5, 10, 20, 50],            //可供选择的每页的行数（*）
        search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        pagination: true,
        clickToSelect: true,                //是否启用点击选中行
        uniqueId: "assets_name",
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
            {field: 'buying_date', title: '购买日期', sortable: true},
        ]
    });
    $('#from_inrepo').on('submit', function (event) {
        // 阻止元素发生默认的行为，此处用来阻止对表单的提交
        event.preventDefault();
        var formData = $('#from_inrepo').serialize();
        console.log(formData);
        // jQuery Ajax 上传文件，关键在于设置：processData 和 contentType
        $.ajax({
            type: 'POST',
            url: '/assets/in_assets_repo/',
            cache: false,
            data: formData,
            // 告诉 jQuery 不要去处理发送的数据
            processData: false,
            dataType:'json',
            // 告诉 jQuery 不要去设置 Content-Type 请求头
            // 因为这里是由 <form> 表单构造的 FormData 对象，且已经声明了属性 enctype="multipart/form-data"，所以设置为 false
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        }).done(function (res) {
            var data = res.status;
            if (data==0){
                var txt="入库成功！";
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.success);
            }else if (data==1){
                var txt="入库失败！";
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.error);
            }else if (data==2){
                var txt="入库失败！<br>该设备已在仓库中！";
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.error);
            }else if (data==3){
                var txt="入库失败！<br>入库时间不能小于上次出库时间";
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.error);
            }
        })
    });
    $('#from_inrepo2').on('submit', function (event) {
        // 阻止元素发生默认的行为，此处用来阻止对表单的提交
        event.preventDefault();
        var formData = $('#from_inrepo2').serialize();
        console.log(formData);
        // jQuery Ajax 上传文件，关键在于设置：processData 和 contentType
        $.ajax({
            type: 'POST',
            url: '/assets/in_repo/',
            cache: false,
            data: formData,
            // 告诉 jQuery 不要去处理发送的数据
            processData: false,
            dataType:'json',
            // 告诉 jQuery 不要去设置 Content-Type 请求头
            // 因为这里是由 <form> 表单构造的 FormData 对象，且已经声明了属性 enctype="multipart/form-data"，所以设置为 false
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        }).done(function (res) {
            var data = res.status;
            if (data==0){
                var txt="入库成功！";
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.success);
            }else{
                var txt=res.errormessage;
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.error);
            }
        })
    });
    $('#from_outrepo').on('submit', function (event) {
        // 阻止元素发生默认的行为，此处用来阻止对表单的提交
        event.preventDefault();
        var formData = $('#from_outrepo').serialize();
        // jQuery Ajax 上传文件，关键在于设置：processData 和 contentType
        $.ajax({
            type: 'POST',
            url: '/assets/out_assets_repo/',
            cache: false,
            data: formData,
            // 告诉 jQuery 不要去处理发送的数据
            processData: false,
            dataType:'json',
            // 告诉 jQuery 不要去设置 Content-Type 请求头
            // 因为这里是由 <form> 表单构造的 FormData 对象，且已经声明了属性 enctype="multipart/form-data"，所以设置为 false
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        }).done(function (res) {
            var data = res.status;
            if (data==0){
                var txt="出库成功！";
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.success);
            }else{
                var txt=res.errormessage;
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.error);
            }
        })
    });
    $(".panel-heading").click(function(e){
                /*切换折叠指示图标*/
                $(this).find("span").toggleClass("glyphicon-chevron-down");
                $(this).find("span").toggleClass("glyphicon-chevron-up");
    });
    $("#get_info").bootstrapTable({
        method: 'get',
        url: window.location.href + '&type=onlygetdata',
        contentType : "application/x-www-form-urlencoded",
        cache: false,
        columns:[
            {field: 'id',title: '序号'},
            {field: 'department', title: '使用部门'},
            {field: 'people', title: '责任人'},
            {field: 'outdate',title: '借出时间'},
            {field: 'indate', title: '归还时间'}
        ]
    })
    $("#searchdata").on('submit', function (event) {
        event.preventDefault();
        var ff = $('#searchdata').serialize();
        //$("#get_assets").bootstrapTable('refresh');
        $.ajax({
            type: 'post',
            url: '/assets/count/',
            cache: false,
            data: ff,
            // 告诉 jQuery 不要去处理发送的数据
            processData: false,
            dataType:'json',
            // 告诉 jQuery 不要去设置 Content-Type 请求头
            // 因为这里是由 <form> 表单构造的 FormData 对象，且已经声明了属性 enctype="multipart/form-data"，所以设置为 false
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        }).done(function (res) {
            var status = res.status;
            if(status==1){
                document.getElementById("title").innerText="个人名下资产 - " + res.uname;
                var formdata2 = {'uname': res.uname};
                console.log(formdata2);
                $("#get_assets").bootstrapTable('destroy').bootstrapTable({
                    method: 'post',
                    url: '/assets/count/getdata/',
                    queryParams: formdata2,
                    contentType : "application/x-www-form-urlencoded",
                    cache: false,
                    columns:[
                        {field: 'id',title: '#序号'},
                        {field: 'assets_name',title: '资产名称'},
                        {field: 'assets_id',title: '资产编号'},
                        {field: 'outdate',title: '借用时间'}
                    ]
                })
            }
        })
    })
    //changepassword
    $(document).ready(function() {
        /*change password*/
        if ($.fn.dialog) {
            $("#change-password-dialog").dialog({
                autoOpen: false,
                title: "修改密码",
                modal: true,
                width: "350",
                closeText: "hide",
                buttons: {
                    "确定": function (event, ui) {
                        $('#change-password-form').submit();
                    },
                },
            });
        }

        $("#change-password").bind("click", function (event) {
            $("#change-password-dialog").dialog("open");
            event.preventDefault();
        });
    });
    //故障展示
    $('#show_assets_trouble').bootstrapTable({
        method: 'post',
        url: "/assets/show_assets_trouble/",         //请求后台的URL（*）
        contentType : "application/x-www-form-urlencoded",
        cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        //detailView:true,            //详情展示
        //sidePagination: "server",
        showRefresh: true,           //刷新按钮
        pageNumber: 1,                       //初始化加载第一页，默认第一页
        pageSize: 30,                       //每页的记录行数（*）
        pageList: [5, 10, 20, 50],            //可供选择的每页的行数（*）
        search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        pagination: true,
        clickToSelect: true,                //是否启用点击选中行
        uniqueId: "assets_name",
        showToggle: true,                    //是否显示详细视图和列表视图的切换按钮
        cardView: false,                    //是否显示详细视图
        detailView: false,                  //是否显示父子表
        showColumns: true,                  //是否显示所有的列
        columns: [{checkbox: true},
            {field: 'assets_id', title: '资产ID', sortable: true},
            {field: 'assets_name', title: '资产名', sortable: true},
            {field: 'trouble_people', title: '责任人',sortable: true},
            {field: 'buying_price', title: '购买价格', sortable: true},
            {field: 'trouble_date', title: '损坏日期', sortable: true},
            {field: 'trouble_info', title: '故障详情', sortable: true}
        ]
    });
    //故障登记
    $('#trouble_note').on('submit', function (event) {
        // 阻止元素发生默认的行为，此处用来阻止对表单的提交
        event.preventDefault();
        var formData = $('#trouble_note').serialize();
        console.log(formData);
        // jQuery Ajax 上传文件，关键在于设置：processData 和 contentType
        $.ajax({
            type: 'POST',
            url: '/assets/trouble/',
            cache: false,
            data: formData,
            // 告诉 jQuery 不要去处理发送的数据
            processData: false,
            dataType:'json',
            // 告诉 jQuery 不要去设置 Content-Type 请求头
            // 因为这里是由 <form> 表单构造的 FormData 对象，且已经声明了属性 enctype="multipart/form-data"，所以设置为 false
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        }).done(function (res) {
            var data = res.status;
            if (data==0){
                var txt="录入成功！";
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.success);
            }else{
                txt = res.errormessage;
                window.wxc.xcConfirm(txt,window.wxc.xcConfirm.typeEnum.error);
            }
        })
    });
});
