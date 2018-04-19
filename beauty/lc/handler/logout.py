import pymysql
from django.shortcuts import render
import hashlib
from django.http import JsonResponse


# @require_http_methods(["GET"])
def handle_logout(request):
    data = {}
    if request.session['username']:
        request.session.flush()
        data['error_code'] = 0
        data['msg'] = 'success'
    else:
        data['error_code'] = 1
        data['msg'] = '未登录！'
    return JsonResponse(data, safe=False)
