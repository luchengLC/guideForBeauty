import pymysql
from django.shortcuts import render
import hashlib
from django.http import JsonResponse


def handle_check_login(request):

    data = {}
    # print('+++++++++++++++++++++++++')

    # username = '13411977340'
    # name = '卢程'
    # print(request.session['username'])
    # print(request.session['name'])
    if request.session.get('name',None):
        name = request.session['name']
        username = request.session['username']
        data['error_code'] = 0
        data['msg'] = 'State: Login'
        data['name'] = name
        data['username'] = username
    else:
        name = '游客'
        username = ''
        data['error_code'] = 1
        data['msg'] = 'State: NotLogin'
        data['name'] = name
        data['username'] = ''
    print('home用户名:', name)
    print('home用户账号:', username)
    return JsonResponse(data, safe=False)

