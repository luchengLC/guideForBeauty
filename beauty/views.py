from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json

from beauty.models import LcTest


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


# 尽量修改用POST
@require_http_methods(["GET"])
def add_student(request):
    response = {}
    try:
        stu = LcTest(stu=request.GET.get('stu'))
        stu.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
