# _*_ coding:utf-8 _*_
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
import xlwt
import io
import datetime

def excel_export(request):
    """
    导出excel表格
    :param request: 
    :return: 
    """
    list_obj = models.Asset.objects.all()
    if list_obj:
        filesname = u"2018-05固定资产盘点表"
        ws = xlwt.Workbook()
        w = ws.add_sheet(u'2018-05固定资产盘点')
        # 写入表头
        excel_head = [
            {'序号': 'id'},
            {'资产ID': 'assets_id'},
            {'资产名称': 'assets_name'},
            {'品牌': 'assets_brand'},
            {'型号': 'assets_version'},
            {'购买日期': 'buying_date'},
            {'购买价格': 'buying_price'},
            {'备注': 'notes'},
            {'状态': 'asset_status'}
        ]
        for n in range(len(excel_head)):
            w.write(0, n, list(excel_head[n].keys())[0])
        # 写入数据
        num = 1
        for data in list_obj.values():
            # 未知设备跳过
            if data['asset_status'] == 0:
                continue
            w.write(num, 0, num)
            for n in range(1, len(excel_head)):
                # 格式化状态
                if list(excel_head[n].values())[0] != 'asset_status':
                    # 格式化日期
                    if list(excel_head[n].values())[0] == 'buying_date':
                        # 去除默认日期
                        if data[list(excel_head[n].values())[0]].strftime('%Y-%m-%d') == '1997-01-01':
                            w.write(num, n, '-')
                        else:
                            w.write(num, n, data[list(excel_head[n].values())[0]].strftime('%Y-%m-%d'))
                    # 去除默认价格
                    elif list(excel_head[n].values())[0] == 'buying_price':
                        if data[list(excel_head[n].values())[0]] == 0:
                            w.write(num, n, '-')
                        else:
                            w.write(num, n, data[list(excel_head[n].values())[0]])
                    else:
                        w.write(num, n, data[list(excel_head[n].values())[0]])
                else:
                    # 闲置输出
                    if data[list(excel_head[n].values())[0]] == 2:
                        w.write(num, n, '闲置中')
                    # 使用中设备输出
                    elif data[list(excel_head[n].values())[0]] == 1:
                        assets_id = data['assets_id']
                        use_data = models.Asset_detial.objects.filter(assets_id=assets_id).order_by('-id')[:1]
                        for d in use_data.values():
                            txt = '{}-{}于{}借用'
                            w.write(num, n, txt.format(
                                    d['use_department'],
                                    d['use_people'],
                                    d['create_date'].strftime('%Y-%m-%d'))
                                    )
                    # 故障设备输出
                    elif data[list(excel_head[n].values())[0]] == 3:
                        assets_id = data['assets_id']
                        use_data = models.Asset_trouble.objects.filter(assets_id=assets_id).order_by('-id')[:1]
                        for d in use_data.values():
                            txt = '{}-{}于{}损坏：{}'
                            w.write(num, n, txt.format(
                                    d['trouble_department'],
                                    d['trouble_people'],
                                    d['trouble_date'].strftime('%Y-%m-%d'),
                                    d['trouble_info'])
                                    )
                    else:
                        pass
            num += 1
        sio = io.BytesIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}.xls'.format(filesname.encode().decode('ISO-8859-1'))
        response.write(sio.getvalue())
        return response