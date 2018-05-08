from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import forms
import json


# 故障展示
@login_required
@csrf_exempt
def show_assets_trouble(request):
    username = request.user.username
    if request.method == 'POST':
        Temp_data = []
        J_data = models.Asset.objects.filter(asset_status=3)
        for data in J_data.values():
            res_data = {}
            res_data['assets_name'] = data['assets_name']
            res_data['buying_price'] = float(data['buying_price'])
            res_data['assets_id'] = '<a href="/assets/get_info?assets_id={}">{}</a>'.format(data['assets_id'], data['assets_id'])
            t_data = models.Asset_trouble.objects.filter(assets_id=data['assets_id'])
            if t_data:
                # 获取责任人及部门
                if t_data.values()[0]['trouble_department'] and t_data.values()[0]['trouble_people']:
                    res_data['trouble_people'] = "{}-{}".format(t_data.values()[0]['trouble_department'], t_data.values()[0]['trouble_people'])
                elif t_data.values()[0]['trouble_department'] and not t_data.values()[0]['trouble_people']:
                    res_data['trouble_people'] = t_data.values()[0]['trouble_department']
                elif t_data.values()[0]['trouble_people'] and not t_data.values()[0]['trouble_department']:
                    res_data['trouble_people'] = t_data.values()[0]['trouble_department']
                else:
                    res_data['trouble_people'] = "无"
                # 获取故障详情
                res_data['trouble_info'] = t_data.values()[0]['trouble_info']
                # 获取故障日期
                if t_data.values()[0]['trouble_date'] != None:
                    res_data['trouble_date'] = t_data.values()[0]['trouble_date'].strftime('%Y-%m-%d')
                else:
                    res_data['trouble_date'] = "-"
                Temp_data.append(res_data)
        return HttpResponse({json.dumps(Temp_data)})
    else:
        return render(request, 'show_assets_trouble.html', {'username': username})


# 故障登记
@login_required
@csrf_exempt
def trouble_note(request):
    if request.method == 'POST':
        form = forms.Trouble(request.POST)
        if form.is_valid():
            assets_id = request.POST['asset_id']
            trouble_date = request.POST['trouble_date']
            trouble_department = request.POST['trouble_department']
            trouble_people = request.POST['trouble_people']
            Troubles_info = str(request.POST['Troubles_info'])
            username = request.user.username
            # 获取设备状态
            status_data = models.Asset.objects.get(assets_id=assets_id)
            if status_data.asset_status == 3:
                return HttpResponse({json.dumps({'status': 1, 'errormessage': u'设备已经处于故障状态'})})
            else:
                # 更新状态
                status_data.asset_status = 3
                status_data.save()
                # 写入故障记录
                models.Asset_trouble.objects.create(
                    assets_id=assets_id,
                    trouble_date=trouble_date,
                    trouble_department=trouble_department,
                    trouble_people=trouble_people,
                    trouble_info=Troubles_info,
                    operator_user=username
                )

                return HttpResponse({json.dumps({'status': 0})})
        else:
            return HttpResponse({json.dumps({'status': 2, 'errormessage': u'输入验证错误，请重试'})})
    else:
        username = request.user.username
        form = forms.Trouble()
        datadic = {'form': form, 'username': username}
        return render(request, 'trouble.html', datadic)