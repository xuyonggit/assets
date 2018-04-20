from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
import json
import datetime
from django.core.paginator import Paginator


@login_required
def Info(request):
    username = request.user.username
    if request.method == 'POST':
        uname = request.POST.get('uname', '')
        datadic = {'uname': uname, 'status': 1}
        return HttpResponse(json.dumps(datadic))
    else:
        return render(request, 'count.html', {'username': username})


@csrf_exempt
@login_required
def Getdata(request):
    if request.method == 'POST':
        uname = request.POST.get('uname', '')
        details = models.Asset_detial.objects.filter(use_people=uname).order_by('create_date')
        datalist = []
        data_dic = {}
        for res_data in details.values():
            if res_data['assets_id'] not in data_dic.keys():
                data_dic[res_data['assets_id']] = {}
                data_dic[res_data['assets_id']]['create_type'] = res_data['create_type']
                data_dic[res_data['assets_id']]['create_date'] = res_data['create_date'].strftime('%Y-%m-%d')
            else:
                data_dic[res_data['assets_id']]['create_type'] = res_data['create_type']
                data_dic[res_data['assets_id']]['create_date'] = res_data['create_date'].strftime('%Y-%m-%d')
        num = 1
        for d in data_dic.keys():
            if data_dic[d]['create_type'] == "入库":
                pass
            else:
                if models.Asset.objects.values('asset_status').filter(assets_id=d)[0]['asset_status'] == 1:
                    data_d = {}
                    data_d['id'] = num
                    data_d['uname'], data_d['assets_id'], data_d['outdate'] = uname,  '<a href="/assets/get_info?assets_id={}">{}</a>'.format(d, d), data_dic[d]['create_date']
                    data_d['assets_name'] = models.Asset.objects.values('assets_name').filter(assets_id=d)[0]['assets_name']
                    datalist.append(data_d)
                    num += 1
        return HttpResponse(json.dumps(datalist))
