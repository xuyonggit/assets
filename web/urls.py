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
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^show_assets/', views.show_assets, name='show_assets'),
    url(r'^show_assets_free/', views.show_assets_free, name='show_assets_free'),
    url(r'^show_assets_used/', views.show_assets_used, name='show_assets_used'),
    url(r'^show_table/', views.show_table, name='show_table'),
    url(r'^show_table_free/', views.show_table_free, name='show_table_free'),
    url(r'^show_table_used/', views.show_table_used, name='show_table_used'),
    url(r'^admin/', admin.site.urls),
]