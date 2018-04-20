import pymysql
from django.shortcuts import render
import hashlib
from django.http import JsonResponse, HttpResponse


# @require_http_methods(["GET"])
def handle_logout(request):
    data = {}
    if request.session.get('name',None):
        request.session.flush()
        data['error_code'] = 0
        data['msg'] = 'success'
        data['username'] = '游客'
    else:
        request.session.flush()
        data['error_code'] = 0
        data['msg'] = '未登录！'
        data['username'] = '游客'
    return JsonResponse(data, safe=False)
