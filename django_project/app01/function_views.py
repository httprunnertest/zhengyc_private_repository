import time
from django.shortcuts import render, HttpResponse, redirect
from app01 import models, views
from django.core.exceptions import ObjectDoesNotExist


def lucky(request):
    account = request.session.get('username')
    try:
        login_date = models.User_info.objects.get(user_account=account)
    except ObjectDoesNotExist:
        return redirect(views.login)
    if request.session.has_key('isLogin'):
        return render(request, 'lucky.html', {'money': login_date.user_money})
    else:
        return redirect(views.login)


def danmu(request):
    if request.method == 'POST':
        file = request.FILES.get('upload')
        print(type(file))
        with open(rf'./app01/uploads/{file.name}','wb')as f:
            for chunk in file.chunks():
                f.write(chunk)
    account = request.session.get('username')
    try:
        models.User_info.objects.get(user_account=account)
    except ObjectDoesNotExist:
        return redirect(views.login)
    if request.session.has_key('isLogin'):
        return render(request, 'danmu.html')
    else:
        return redirect(views.login)

