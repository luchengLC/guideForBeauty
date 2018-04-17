import pymysql
from django.shortcuts import render
import hashlib
from django.http import JsonResponse


# @require_http_methods(["GET"])
def handle_logout(request):
    data = {}
    if request.session.get(['username'], none):
        username = request.session['username']
        data['error_code'] = 0
        data['msg'] = 'success'
        data['username'] = username
    else:
        username = '游客'
        data['error_code'] = 0
        data['msg'] = 'success'
        data['username'] = username
    print('home用户名:', username)
    return JsonResponse(data, safe=False)
