#-*-coding:utf-8-*-

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, ChangePasswordForm

def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/assets')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        if request.user.is_authenticated:
            return HttpResponseRedirect('/assets')
        return render(request, 'login.html', {'form': form})

@login_required
def changepassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/accounts/logout/")
    else:
        form = ChangePasswordForm(user=request.user)

    return render(request, 'changepassword.html', {
        'username': request.user.username,
        'form': form
    })