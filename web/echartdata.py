from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from . import models


@login_required
@csrf_exempt
def getdata1(request):
    data_list = []
    nametemplates = [
        {'name': '库存中', 'status': 2},
        {'name': '使用中', 'status': 1},
        {'name': '故障', 'status': 3},
        {'name': '未知', 'status': 0}
    ]
    for dic in nametemplates:
        dic_tmp = {}
        num = models.Asset.objects.filter(asset_status=dic['status']).count()
        dic_tmp['name'], dic_tmp['value'] = dic['name'], num
        data_list.append(dic_tmp)
    return HttpResponse(json.dumps(data_list))


#@login_required
@csrf_exempt
def getdata2(request):
    if request.method == 'POST':
        data_all = models.Asset.objects.filter()
        list_all = [
            {'name': u'笔记本', 'used_num': 0, 'free_num': 0, 'trouble_num': 0},
            {'name': u'台式机', 'used_num': 0, 'free_num': 0, 'trouble_num': 0},
            {'name': u'显示器', 'used_num': 0, 'free_num': 0, 'trouble_num': 0},
            {'name': u'手机', 'used_num': 0, 'free_num': 0, 'trouble_num': 0},
        ]
        other_dic = {'name': u'其他', 'used_num': 0, 'free_num': 0, 'trouble_num': 0}
        for template in list_all:
            name = template['name']
            for d in data_all:
                if d.assets_name == name:
                    if d.asset_status == 1:
                        template['used_num'] += 1
                    elif d.asset_status == 2:
                        template['free_num'] += 1
                    elif d.asset_status == 3:
                        template['trouble_num'] += 1
                    else:
                        pass
        list_all.append(other_dic)
        return HttpResponse(json.dumps(list_all))