"""assets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views, count, account, echartdata, Trouble
from django.contrib.auth.views import logout
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^show_assets_free/$', views.show_assets_free, name='show_assets_free'),
    url(r'^show_assets_used/$', views.show_assets_used, name='show_assets_used'),
    url(r'^show_assets/$', views.show_assets, name='show_assets'),
    url(r'^in_repo/$', views.In_repo, name='In_repo'),
    url(r'^in_assets_repo/$', views.In_assets_repo, name='In_assets_repo'),
    url(r'^in_assets_repo/GT-(?P<aid>\d+)/$', views.In_assets_repo, name='In_assets_repo'),
    url(r'^in_assets_repo/GT-(?P<aid>\d+)-(?P<aid2>\d+)/$', views.In_assets_repo, name='In_assets_repo'),
    url(r'^out_assets_repo/$', views.Out_assets_repo, name='Out_assets_repo'),
    url(r'^out_assets_repo/GT-(?P<aid>\d+)/$', views.Out_assets_repo, name='Out_assets_repo'),
    url(r'^out_assets_repo/GT-(?P<aid>\d+)-(?P<aid2>\d+)/$', views.Out_assets_repo, name='Out_assets_repo'),
    url(r'^get_info/$', views.get_info, name='get_info'),
    url(r'^count/$', count.Info, name='Info'),
    url(r'^count/getdata/$', count.Getdata, name='Getdata'),
    # 首页库存状态一览图数据
    url(r'^echart/getdata/$', echartdata.getdata1),
    url(r'^echart/getdata2/$',echartdata.getdata2),
    # 故障接口
    url(r'show_assets_trouble/$', Trouble.show_assets_trouble, name='show_assets_trouble'),
    url(r'trouble/$', Trouble.trouble_note, name='trouble'),
]
