import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json

from beauty.models import LcTest, JdHkProductBasemakeup

# 测试
@require_http_methods(["GET"])
def show_student(request):
    response = {}
    try:
        stu = LcTest.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", stu))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 测试                   尽量修改用POST
@require_http_methods(["GET"])
def add_student(request):
    response = {}
    try:
        stu = LcTest(sno=request.GET.get('sno'))
        stu.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 底妆
@require_http_methods(["GET"])
def show_baseMakeup(request):
    response = {}
    try:
        baseMakeup = JdHkProductBasemakeup.objects.all()[:50]
        response['list'] = json.loads(serializers.serialize("json", baseMakeup))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 请求列表总方法，封装其他的
@require_http_methods(["GET"])
def show_list(request):
    global req
    req = request
    cID = request.GET.get('cID')
    print("cID = ", cID)

    # 这里偷懒一下，先给个ID来区别，以后换成数字，或者直接在数据库中存一张表，从表中获取对应关系
    # 以下的顺序是跟前端页面的编码对应的
    # 这方法 耦合性太高，一定要改！
    # if cID == 0:
    #     return show_baseMakeup(req)
    # elif cID == 1:
    #     return show_baseMakeup(req)
    # elif cID == 2:
    #     return show_baseMakeup(req)
    # elif cID == 3:
    #     return show_baseMakeup(req)
    # elif cID == 4:
    #     return show_baseMakeup(req)
    return show_baseMakeup(req)



