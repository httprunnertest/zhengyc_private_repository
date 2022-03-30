from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def index(request):
    account = request.session.get('username')
    try:
        login_date = models.User_info.objects.get(user_account=account)
    except ObjectDoesNotExist:
        return redirect(login)
    if request.session.has_key('isLogin'):
        userinfo = models.User_info.objects.all()
        return render(request, 'index.html', {'user_info': userinfo, 'loginedUser': login_date, 'user_id':login_date.user_id})
    else:
        return redirect(login)


def login(request):
    if 'username' in request.COOKIES:
        u_name = request.COOKIES['username'].split("|")[0]
        checked = 'checked'
    else:
        u_name = ''
        checked = ''
    return render(request, 'login.html', {'cookie_username': u_name, 'checked': checked})


def register(request):
    if request.method == 'POST':
        account_is_exist = models.User_info.objects.filter(user_account=request.POST.get('account'))
        if not account_is_exist:
            userInfo = models.User_info.objects.create(
                user_account=request.POST.get('account'),
                user_birthday=request.POST.get('birthday'),
                user_sex=request.POST.get('sex'),
                user_password=request.POST.get('password'),
                user_name=request.POST.get('nickname')
            )

            # 自动在个人物品中创建信息
            for storeid in models.Lucky_award.objects.all():
                models.User_stores.objects.create(
                    user_name=userInfo,
                    store_name=storeid
                )
            return redirect(login)
        else:
            return redirect(register)
    else:
        return render(request, 'register.html')


def edit_date(request, edit_user_id):
    old_date = models.User_info.objects.get(user_id=edit_user_id)
    return render(request, 'edit.html',{'old_date': old_date})


def stores(request):
    userId = models.User_info.objects.get(user_account=request.session.get('username')).user_id
    userStores = models.User_stores.objects.filter(user_name=userId).values('store_name__award_name', 'store_num').exclude(store_num=0)
    return render(request, 'stores.html', {'stores': userStores})