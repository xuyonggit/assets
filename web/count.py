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


@csrf_exempt
def Info(request):
    return render(request, 'index.html')