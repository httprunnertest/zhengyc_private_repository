from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from app01 import models
import random
import datetime


def logout(request):
    request.session.clear()
    logout_json = {'session_delete': True}
    return JsonResponse(logout_json)


def login_check(request):
    res_json = [
        {
            "res_success": None,
        },
        {
            "res_success": True,
        },
        {
            "res_success": False,
        }
    ]
    # 接受ajax传过来的username，password，remember
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    if username == '' or password == '':
        return JsonResponse(res_json[0])
    # print(username)
    is_exist = models.User_info.objects.filter(user_account=username, user_password=password)
    # print(is_exist)
    if is_exist.exists():
        request.session['username'] = username
        request.session['password'] = password
        request.session['isLogin'] = True
        request.session.set_expiry(0)
        ret = JsonResponse(res_json[1])
        if remember == 'true':
            ret.set_cookie('username', username + '|' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return ret
    else:
        return JsonResponse(res_json[2])


def delete_date(request):
    delete_id = request.POST.get('delete_id')
    models.User_info.objects.filter(user_id=delete_id).delete()
    date_is_delete = {'isdelete': True}
    return JsonResponse(date_is_delete)


def touch_prize(request):
    count = int(request.POST.get('count'))
    username = request.session.get('username')
    try:
        account = models.User_info.objects.get(user_account=username)
    except ObjectDoesNotExist:
        return JsonResponse({'success': False, 'log': '登录已过期，请重新登录'})
    if account.user_money < count * 100:
        return JsonResponse({'success': False, 'log': '点券不足，请充值'})
    '''
        抽奖的算法
        10连必出A
        随机数（1-1000）
        1-300是金币
        301-500是砖石
        501-700是改名卡
        701-820 B英雄
        821-900 B皮肤
        901-930 A英雄
        931-955 S英雄
        956-975  A皮肤
        976-990 S皮肤
        991-1000 SSR 英雄
    '''
    prize = {}

    def one_prize():
        # 数组，10个，每个元素是一个字典，字典有id，name,rate键
        awards_rate = models.Lucky_award.objects.all()
        sum = 0
        random_num = random.randint(1, 1000)
        for ele in awards_rate:
            if ele.award_rate * 1000 + sum >= random_num >= sum:
                return ele.award_name
            sum += ele.award_rate * 1000

    if count == 10:
        for i in range(1, 11):
            prize[i] = one_prize()
        account.user_money = account.user_money - count * 100
        account.save()
    else:
        prize[1] = one_prize()
        account.user_money = account.user_money - count * 100
        account.save()
    # 抽完奖需要把物品保存到个人物品
    # prize抽奖字典，account 账户信息
    for award in prize.values():
        store = models.User_stores.objects.get(user_name=account.user_id,
                                               store_name=models.Lucky_award.objects.get(award_name=award).award_id)
        store.store_num = store.store_num + 1
        store.save()
    return JsonResponse({'success': True, 'user_money': account.user_money, 'prize': prize})


def danmu_send(request):
    # 弹幕值
    userId = models.User_info.objects.get(user_account=request.session.get('username'))
    if not userId:
        return JsonResponse({'res_success': False})
    danmu_value = request.GET.get('danmu_value')
    # 服务器时间
    danmu_time = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%Y-%m-%d %H:%M:%S")  # 服务器时间
    is_success = models.Danmu.objects.create(
        user_id=userId,
        danmu_name=danmu_value,
        danmu_time=danmu_time
    )
    if is_success:
        return JsonResponse({'res_success': True})


def get_danmu(request):
    try:
        models.User_info.objects.get(user_account=request.session.get('username'))
    except ObjectDoesNotExist:
        return JsonResponse({'message': False})
    get_time = request.GET.get('get_time')
    # get_time = '2022-01-27 16:01:28'
    # print('获取时间为',get_time,'的弹幕')
    # 外键名称__母表字段
    list_danmu = list(models.Danmu.objects.filter(danmu_time=get_time).values('user_id__user_name', 'danmu_name'))
    return JsonResponse({'message': True, 'content': list_danmu})
