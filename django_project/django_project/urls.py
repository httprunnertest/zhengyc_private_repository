"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from app01 import views, ajax_views, function_views


urlpatterns = [
    path('admin', admin.site.urls),
    # path('login', views.LoginView.as_view()),
    path('', views.index),
    path('index', views.index),
    path('login', views.login),
    path('register', views.register),
    path('login_check', ajax_views.login_check),
    path('logout', ajax_views.logout),
    path('delete_date', ajax_views.delete_date),
    re_path(r'edit_date/(\d+)', views.edit_date, name='edit_date'),
    path('lucky',function_views.lucky, name='lucky'),
    path('danmu',function_views.danmu, name='danmu'),
    path('touch_prize',ajax_views.touch_prize),
    path('stores',views.stores, name='stores'),
    path('danmu_send',ajax_views.danmu_send),
    path('get_danmu',ajax_views.get_danmu)
]
