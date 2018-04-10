from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Sum
from django.http.response import HttpResponse
from . import models
import json
import datetime
from django.core.paginator import Paginator


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def show_assets(request):
    return render(request, 'show_assets.html')


@csrf_exempt
def show_assets_free(request):
    return render(request, 'show_assets_free.html')


@csrf_exempt
def show_assets_used(request):
    return render(request, 'show_assets_used.html')


# 获取所有资产
@csrf_exempt
def show_table(request):
    Temp_data = []
    J_data = models.Asset.objects.all()
    for data in J_data.values():
        data['buying_price'] = float(data['buying_price'])
        if data['buying_date'] != None:
            if type(data['buying_date']) == 'str':
                data['buying_date'] = datetime.date.strftime(data['buying_date'], '%Y-%m-%d')
            elif type(data['buying_date']) == 'datetime.date':
                data['buying_date'] = data['buying_date'].strftime('%Y-%m-%d')
            else:
                data['buying_date'] = 'None'
        Temp_data.append(data)
    return HttpResponse({json.dumps(Temp_data)})


# 获取库存中的资产
@csrf_exempt
def show_table_free(request):
    Temp_data = []
    J_data = models.Asset.objects.all()
    for data in J_data.values():
        data['buying_price'] = float(data['buying_price'])
        if data['buying_date'] != None:
            if type(data['buying_date']) == 'str':
                data['buying_date'] = datetime.date.strftime(data['buying_date'], '%Y-%m-%d')
            elif type(data['buying_date']) == 'datetime.date':
                data['buying_date'] = data['buying_date'].strftime('%Y-%m-%d')
            else:
                data['buying_date'] = 'None'
        if data['asset_status'] == 2:
            Temp_data.append(data)
    return HttpResponse({json.dumps(Temp_data)})


# 获取使用中的资产
@csrf_exempt
def show_table_used(request):
    Temp_data = []
    J_data = models.Asset.objects.all()
    for data in J_data.values():
        data['buying_price'] = float(data['buying_price'])
        if data['buying_date'] != None:
            if type(data['buying_date']) == 'str':
                data['buying_date'] = datetime.date.strftime(data['buying_date'], '%Y-%m-%d')
            elif type(data['buying_date']) == 'datetime.date':
                data['buying_date'] = data['buying_date'].strftime('%Y-%m-%d')
            else:
                data['buying_date'] = 'None'
        if data['asset_status'] == 1:
            Temp_data.append(data)
    return HttpResponse({json.dumps(Temp_data)})