from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
import json


@login_required
def baseall(request):
    dataDic = {}
    data_department = models.department.objects.all()
    for d_data in data_department.values():
        _T = d_data["Tixi_name"]
        _D = d_data['department_name']
        if _T not in dataDic.keys():
            dataDic[_T] = {}
        dataDic[_T][_D] = {}
    data_data = models.baseall.objects.all()
    for d in data_data.values():
        del d['id']
        department_name = d.pop("department_name")
        for tixi,values in dataDic.items():
            if department_name in values.keys():
                people_name = d.pop("pname")
                dataDic[tixi][department_name][people_name] = d
    print(dataDic)
    return render(request, 'Baseall.html', {"department": data_department, "dataDic": dataDic})
