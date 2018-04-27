from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from . import models

#@login_required
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