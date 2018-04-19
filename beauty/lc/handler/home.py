import pymysql
from django.shortcuts import render
import hashlib
from django.http import JsonResponse


def handle_check_login(request):

    data = {}
    # print('+++++++++++++++++++++++++')

    username = '13411977340'
    name = '卢程'
    # print(request.session['username'])
    # print(request.session['name'])
    if request.session.get('username',None):
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
