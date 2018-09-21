from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
import json

@login_required
@csrf_exempt
def add(request):
    username = request.user.username
    if request.method == 'POST':
        form = forms.Add(request.POST)
        if form.is_valid():
            print(request.POST)
            assets_name = request.POST['assets_name']
            assets_brand = request.POST['assets_brand']
            assets_version = request.POST['assets_version']
            if request.POST['buying_price']:
                buying_price = request.POST['buying_price']
            else:
                buying_price = 0
            if request.POST['buying_date']:
                buying_date = str(request.POST['buying_date'])
            else:
                buying_date = '1997-01-01'
            notes = str(request.POST['notes'])
            Last_assets_id = models.Asset.objects.values("assets_id").last()['assets_id']
            New_assets_id = 'GT-0{}'.format(int(Last_assets_id.split('GT-')[1]) + 1)
            # 写入数据
            models.Asset.objects.create(
                assets_id=New_assets_id,
                assets_name=assets_name,
                assets_brand=assets_brand,
                assets_version=assets_version,
                buying_price=buying_price,
                buying_date=buying_date,
                notes=notes,
                asset_status=2
            )
            return HttpResponse({json.dumps({'status': 0, 'assets_id': New_assets_id})})
    else:
        form = forms.Add()
        datadic = {'form': form, 'username': username}
        return render(request, 'Add.html', datadic)
