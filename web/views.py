from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Sum
from django.http.response import HttpResponse
from . import models
from . import forms
import json
import datetime
from django.core.paginator import Paginator


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')


# 所有资产展示
@csrf_exempt
def show_assets(request):
    if request.method == 'POST':
        Temp_data = []
        J_data = models.Asset.objects.all()
        for data in J_data.values():
            data['buying_price'] = float(data['buying_price'])
            data['assets_id'] = '<a href="/assets/get_info?assets_id={}">{}</a>'.format(data['assets_id'],
                                                                                        data['assets_id'])
            if data['buying_date'] != None:
                if type(data['buying_date']) == str:
                    del data['buying_date']
                else:
                    if data['buying_date'].strftime('%Y-%m-%d') == '1997-01-01':
                        del data['buying_date']
                    else:
                        data['buying_date'] = data['buying_date'].strftime('%Y-%m-%d')
            Temp_data.append(data)
        return HttpResponse({json.dumps(Temp_data)})
    else:
        return render(request, 'show_assets.html')


# 闲置资产展示
@csrf_exempt
def show_assets_free(request):
    if request.method == 'POST':
        Temp_data = []
        J_data = models.Asset.objects.all()
        for data in J_data.values():
            data['buying_price'] = float(data['buying_price'])
            data['assets_id'] = '<a href="/assets/get_info?assets_id={}">{}</a>'.format(data['assets_id'], data['assets_id'])
            if data['buying_date'] != None:
                if type(data['buying_date']) == str:
                    del data['buying_date']
                else:
                    if data['buying_date'].strftime('%Y-%m-%d') == '1997-01-01':
                        del data['buying_date']
                    else:
                        data['buying_date'] = data['buying_date'].strftime('%Y-%m-%d')
            if data['asset_status'] == 2:
                Temp_data.append(data)
        return HttpResponse({json.dumps(Temp_data)})
    else:
        return render(request, 'show_assets_free.html')


# 使用中资产展示
@csrf_exempt
def show_assets_used(request):
    if request.method == 'POST':
        Temp_data = []
        J_data = models.Asset.objects.all()
        for data in J_data.values():
            data['buying_price'] = float(data['buying_price'])
            data['assets_id'] = '<a href="/assets/get_info?assets_id={}">{}</a>'.format(data['assets_id'],
                                                                                        data['assets_id'])
            if data['buying_date'] != None:
                if type(data['buying_date']) == str:
                    del data['buying_date']
                else:
                    if data['buying_date'].strftime('%Y-%m-%d') == '1997-01-01':
                        del data['buying_date']
                    else:
                        data['buying_date'] = data['buying_date'].strftime('%Y-%m-%d')
            if data['asset_status'] == 1:
                Temp_data.append(data)
        return HttpResponse({json.dumps(Temp_data)})
    else:
        return render(request, 'show_assets_used.html')


@csrf_exempt
def In_assets_repo(request):
    if request.method == 'POST':
        form = forms.In_repo(request.POST)
        if form.is_valid():
            use_people = request.POST['use_people']
            asset_id = request.POST['asset_id']
            create_date = request.POST['create_date']
            use_department = request.POST['use_department']
            create_type = '入库'
            # 更新状态
            status_data = models.Asset.objects.get(assets_id=asset_id)
            if status_data.asset_status == 2:
                return HttpResponse({json.dumps({'status': 2})})
            else:
                date_data = models.Asset_detial.objects.filter(assets_id=asset_id, create_type='入库').order_by(
                    '-create_date')[:1]
                if date_data:
                    if datetime.datetime.strptime(str(create_date), '%Y-%m-%d') < datetime.datetime.strptime(
                            str(date_data.values()[0]['create_date']), '%Y-%m-%d'):
                        return HttpResponse({json.dumps({'status': 3})})
                status_data.asset_status = 2
                status_data.save()

                # 写入出库数据
                models.Asset_detial.objects.create(
                    use_people=use_people,
                    assets_id=asset_id,
                    create_date=create_date,
                    use_department=use_department,
                    create_type=create_type
                )

                return HttpResponse({json.dumps({'status': 0})})
        else:
            return HttpResponse({json.dumps({'status': 1})})
    else:
        form = forms.In_repo()
        return render(request, 'In_assets_repo.html', {'form': form})


@csrf_exempt
def Out_assets_repo(request):
    if request.method == 'POST':
        form = forms.Out_repo(request.POST)
        if form.is_valid():
            use_people = request.POST['use_people']
            asset_id = request.POST['asset_id']
            create_date = request.POST['create_date']
            use_department = request.POST['use_department']
            create_type = '出库'
            # 更新状态
            status_data = models.Asset.objects.get(assets_id=asset_id)
            if status_data.asset_status == 1:
                return HttpResponse({json.dumps({'status': 2})})
            else:
                date_data = models.Asset_detial.objects.filter(assets_id=asset_id, create_type='入库').order_by('-create_date')[:1]
                if date_data:
                    if datetime.datetime.strptime(str(create_date), '%Y-%m-%d') < datetime.datetime.strptime(
                            str(date_data.values()[0]['create_date']), '%Y-%m-%d'):
                        return HttpResponse({json.dumps({'status': 3})})
                status_data.asset_status = 1
                status_data.save()
                # 写入出库数据
                models.Asset_detial.objects.create(
                    use_people=use_people,
                    assets_id=asset_id,
                    create_date=create_date,
                    use_department=use_department,
                    create_type=create_type
                )

                return HttpResponse({json.dumps({'status': 0})})
        else:
            return HttpResponse({json.dumps({'status': 1})})
    else:
        form = forms.Out_repo()
        return render(request, 'Out_assets_repo.html', {'form': form})


# 详情查询
@csrf_exempt
def get_info(request):
    if request.method == 'GET':
        assets_id = request.GET.get('assets_id', '')
        if request.GET.get('type', '') == 'onlygetdata':
            datalist = []
            getdata = models.Asset_detial.objects.filter(assets_id=assets_id).order_by('id')
            dic = {}
            id = 1
            endindex = len(getdata.values()) - 1
            for num in range(len(getdata.values())):
                i = getdata.values()[num]
                # 第一次即为入库的情况
                if num == 0 and i['create_type'] == '入库':
                    dic['id'], dic['department'], dic['people'], dic['indate'] = id, i['use_department'], i['use_people'], i['create_date'].strftime(
                        '%Y-%m-%d')
                    datalist.append(dic)
                    dic = {}
                    id += 1
                # 最后一次为出库的情况
                elif num == endindex and i['create_type'] == '出库':
                    dic['id'], dic['department'],  dic['people'], dic['outdate'] = id, i['use_department'], i['use_people'], i['create_date'].strftime(
                        '%Y-%m-%d')
                    id += 1
                    datalist.append(dic)
                    dic = {}
                # 出库
                elif i['create_type'] == '出库':
                    dic['outdate'] = i['create_date'].strftime('%Y-%m-%d')
                # 入库
                elif num != 0 and i['create_type'] == '入库':
                    dic['indate'] = i['create_date'].strftime('%Y-%m-%d')
                    id += 1
                    datalist.append(dic)
                    dic = {}
            return HttpResponse(json.dumps(datalist))
        else:
            assets_data = models.Asset.objects.filter(assets_id=assets_id).values()[0]
            # 处理价格
            if float(assets_data['buying_price']) != 0:
                assets_data['buying_price'] = float(assets_data['buying_price'])
            else:
                del assets_data['buying_price']
            # 处理日期
            if assets_data['buying_date'] != None:
                if type(assets_data['buying_date']) == str:
                    del assets_data['buying_date']
                else:
                    if assets_data['buying_date'].strftime('%Y-%m-%d') == '1997-01-01':
                        del assets_data['buying_date']
                    else:
                        assets_data['buying_date'] = assets_data['buying_date'].strftime('%Y-%m-%d')
            # 处理状态
            if assets_data['asset_status'] == 1:
                assets_data['asset_status'] = '使用中'
            elif assets_data['asset_status'] == 2:
                assets_data['asset_status'] = '仓库中'
            else:
                assets_data['asset_status'] = '未知'
            return render(request, 'get_info.html', {'data': assets_data})
