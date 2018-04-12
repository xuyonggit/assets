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


@csrf_exempt
def show_assets(request):
    if request.method == 'POST':
        Temp_data = []
        J_data = models.Asset.objects.all()
        for data in J_data.values():
            data['buying_price'] = float(data['buying_price'])
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


@csrf_exempt
def show_assets_free(request):
    if request.method == 'POST':
        Temp_data = []
        J_data = models.Asset.objects.all()
        for data in J_data.values():
            data['buying_price'] = float(data['buying_price'])
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


@csrf_exempt
def show_assets_used(request):
    if request.method == 'POST':
        Temp_data = []
        J_data = models.Asset.objects.all()
        for data in J_data.values():
            data['buying_price'] = float(data['buying_price'])
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