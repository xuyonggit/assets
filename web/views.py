from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import forms
import json
import datetime


# Create your views here.
@login_required
def index(request):
    username = request.user.username
    dynamic_data = []
    datainfo = models.Asset_detial.objects.all().order_by('-id')[:20]
    for i in datainfo.values():
        i['create_date'] = i['create_date'].strftime('%Y-%m-%d')
        dynamic_data.append(i)
    return render(request, 'index.html', {'username': username, 'dynamic_data': dynamic_data})


# 所有资产展示
@login_required
@csrf_exempt
def show_assets(request):
    username = request.user.username
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
        return render(request, 'show_assets.html', {'username': username})


# 闲置资产展示
@login_required
@csrf_exempt
def show_assets_free(request):
    username = request.user.username
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
        return render(request, 'show_assets_free.html', {'username': username})


# 使用中资产展示
@login_required
@csrf_exempt
def show_assets_used(request):
    username = request.user.username
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
        return render(request, 'show_assets_used.html', {'username': username})


@login_required
def In_assets_repo(request, aid="", aid2=""):
    if aid != "" and aid2 == "":
        ass_id = 'GT-{}'.format(aid)
    elif aid != "" and aid2 != "":
        ass_id = 'GT-{}-{}'.format(aid, aid2)
    if request.method == 'POST':
        form = forms.In_repo(request.POST)
        if form.is_valid():
            use_people = request.POST['use_people']
            asset_id = request.POST['asset_id']
            create_date = request.POST['create_date']
            use_department = models.department.objects.get(id=request.POST['use_department'])
            create_type = '入库'
            username = request.user.username
            # 更新状态
            status_data = models.Asset.objects.get(assets_id=asset_id)
            if status_data.asset_status == 2:
                return HttpResponse({json.dumps({'status': 2, 'errormessage': u'入库失败！<br>该设备已在仓库中！'})})
            else:
                date_data = models.Asset_detial.objects.filter(assets_id=asset_id, create_type='入库').order_by(
                    '-create_date')[:1]
                if date_data:
                    if datetime.datetime.strptime(str(create_date), '%Y-%m-%d') < datetime.datetime.strptime(
                            str(date_data.values()[0]['create_date']), '%Y-%m-%d'):
                        return HttpResponse({json.dumps({'status': 3, 'errormessage': u'入库失败！<br>入库时间不能小于上次出库时间'})})
                status_data.asset_status = 2
                status_data.save()

                # 写入出库数据
                models.Asset_detial.objects.create(
                    use_people=use_people,
                    assets_id=asset_id,
                    create_date=create_date,
                    use_department=use_department,
                    create_type=create_type,
                    operuser=username
                )
                # 更新资产统计表数据
                data_count = models.baseall.objects.filter(pname=use_people)
                new_count = data_count.values()[0]['assets_count'] - 1
                data_count.update(assets_count=new_count)
                return HttpResponse({json.dumps({'status': 0})})
        else:
            return HttpResponse({json.dumps({'status': 1, 'errormessage': u'入库失败！'})})
    else:
        username = request.user.username
        form = forms.In_repo()
        datadic = {'form': form, 'username': username}
        try:
            datadic['ass_id'] = ass_id
        except UnboundLocalError as err:
            pass
        finally:
            return render(request, 'In_assets_repo.html', datadic)


@login_required
def In_repo(request):
    if request.method == 'POST':
        form = forms.In_repo2(request.POST)
        if form.is_valid():
            asset_id = 'GT-020' + str(request.POST['asset_id'])
            # 更新状态
            status_data = models.Asset.objects.get(assets_id=asset_id)
            if status_data.asset_status == 2:
                return HttpResponse({json.dumps({'status': 2})})
            else:
                status_data.asset_status = 2
                status_data.save()
                return HttpResponse({json.dumps({'status': 0})})
        else:
            return HttpResponse({json.dumps({'status': 1})})
    else:
        username = request.user.username
        form = forms.In_repo2()
        datadic = {'form': form, 'username': username}
        return render(request, 'In_repo.html', datadic)


@login_required
def Out_assets_repo(request, aid="", aid2=""):
    if aid != "" and aid2 == "":
        ass_id = 'GT-{}'.format(aid)
    elif aid != "" and aid2 != "":
        ass_id = 'GT-{}-{}'.format(aid, aid2)
    if request.method == 'POST':
        form = forms.Out_repo(request.POST)
        if form.is_valid():
            use_people = request.POST['use_people']
            asset_id = request.POST['asset_id']
            create_date = request.POST['create_date']
            use_department = models.department.objects.get(id=request.POST['use_department'])
            create_type = '出库'
            username = request.user.username
            # 更新状态
            status_data = models.Asset.objects.get(assets_id=asset_id)
            if status_data.asset_status == 1:
                return HttpResponse({json.dumps({'status': 2, 'errormessage': u'出库失败！<br>该设备已被其他人使用,如有疑问，请联系管理员'})})
            elif status_data.asset_status == 3:
                return HttpResponse({json.dumps({'status': 3, 'errormessage': u'出库失败！<br>该设备为故障设备,如需使用,请确认设备可正常使用'})})
            else:
                date_data = models.Asset_detial.objects.filter(assets_id=asset_id, create_type='入库').order_by('-create_date')[:1]
                if date_data:
                    if datetime.datetime.strptime(str(create_date), '%Y-%m-%d') < datetime.datetime.strptime(
                            str(date_data.values()[0]['create_date']), '%Y-%m-%d'):
                        return HttpResponse({json.dumps({'status': 3, 'errormessage': u'出库失败！<br>出库时间不能小于上次入库时间'})})
                status_data.asset_status = 1
                status_data.save()
                # 写入出库数据
                models.Asset_detial.objects.create(
                    use_people=use_people,
                    assets_id=asset_id,
                    create_date=create_date,
                    use_department=use_department,
                    create_type=create_type,
                    operuser=username
                )
                # 更新资产统计表数据
                data_count = models.baseall.objects.filter(pname=use_people)
                if len(data_count) == 1:
                    new_count = data_count.values()[0]['assets_count'] + 1
                    data_count.update(assets_count=new_count)
                else:
                    models.baseall.objects.create(
                        pname=use_people,
                        department_name=use_department,
                        assets_count=1
                    )
                return HttpResponse({json.dumps({'status': 0})})
        else:
            return HttpResponse({json.dumps({'status': 1, 'errormessage': u'出库失败！'})})
    else:
        form = forms.Out_repo()
        username = request.user.username
        datadic = {'form': form, 'username': username}
        try:
            datadic['ass_id'] = ass_id
        except UnboundLocalError as err:
            pass
        finally:
            return render(request, 'Out_assets_repo.html', datadic)


# 详情查询
@login_required
def get_info(request):
    username = request.user.username
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
                    dic['outdate'], dic['id'], dic['department'],  dic['people'] = i['create_date'].strftime('%Y-%m-%d'), id, i['use_department'], i['use_people']
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
                assets_data['edit'] = [{'入库': '/assets/in_assets_repo/{}'.format(assets_id)}]
            elif assets_data['asset_status'] == 2:
                assets_data['asset_status'] = '仓库中'
                assets_data['edit'] = [{'出库': '/assets/out_assets_repo/{}'.format(assets_id)}]
            else:
                assets_data['asset_status'] = '未知'
                assets_data['edit'] = [{'入库': '/assets/in_assets_repo/{}'.format(assets_id)}]
                assets_data['edit'].append({'出库': '/assets/out_assets_repo/{}'.format(assets_id)})
            return render(request, 'get_info.html', {'data': assets_data, 'username': username})
