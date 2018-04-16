#!/usr/bin/python 
# -*- coding:utf-8 -*-
#-*-coding=utf-8-*-
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'guideForBeauty.settings'
django.setup()
from beauty.models import UserCutPriceProduct
import  json
# 检查用户手机号码格式是否正确
def check_phone(user_phone):
    if((user_phone is None) or (user_phone == "")):
        return False
    else:
        return True

# 检查手机号码对应的用户是否已经注册
# def isExist_phone(user_phone):
#     # 测试，应该从用户表中获取用户的手机号码列表
#     users_phone = []
#     users_phone.append("13411984676")
#     users_phone.append("13411984673")
#     if(users_phone in users_phone):
#         return True
#     else:
#         return False

# 验证该用户是否重复点击同一个商品
def checkAdd(product_json):
    product = UserCutPriceProduct.objects.filter(Q(user_phone=product_json['user_phone'])&Q(product_address=product_json['item_url']))
    if product is not None:
        return True
    else:
        return False

# 从数据库获取用户关注的商品列表
def add_product_to_table(product_json):
    try:
        if(checkAdd(product_json)):
            product = UserCutPriceProduct(user_phone = product_json['user_phone'],
                                          product_address=product_json['item_url'],
                                          product_name=product_json['name'],
                                          product_price=product_json['price'],
                                          product_img_url=product_json['img_url'],
                                          product_comment_count=product_json['comment_count'],
                                          product_platform = product_json['platform']
                                          )
            #
            # product.user_phone = product_json['user_phone']
            # product.product_address = product_json['item_url']
            # product.product_name = product_json['name']
            # product.product_price = product_json['price']
            # product.product_img_url = product_json['img_url']
            # product.product_comment_count = product_json['comment_count']
            # product.product_platform = product_json['platform']
            product.save()
            return 0
        else:
            return 1
    except Exception as e:
        print(e)
        return -1


@require_http_methods(["POST"])
def handle_insert(request):
    body = {}
    body['user_phone'] = request.POST.get('user_phone')
    body['item_url'] = request.POST.get('item_url')
    body['price'] = request.POST.get('price')
    body['img_url'] = request.POST.get('img_url')
    body['comment_count'] = request.POST.get('comment_count')
    body['platform'] = request.POST.get('platform')
    body['name'] = request.POST.get('name')

    # body = {'name': '32432432','user_phone': '12321332322323', 'platform': '13221', 'img_url': 'fdfsad', 'comment_count': 'dfdf', 'price': '12312', 'item_url': 'dsdSDS'}
    print(body)
    result = {}
    if(check_phone(body['user_phone']) is False or add_product_to_table(body) ==-1):
        result['error_code'] = 1
        result['msg'] = "服务器异常"
    else:
        result['error_code'] = 0
        result['msg'] = "success"
    print (result)
    return JsonResponse(result,safe=False)

if __name__ == '__main__':
    # http://127.0.0.1:8000/beauty/productsList/getProductsPage?wd=卡姿兰蜗牛气垫调控霜&PageNo=1
    # keyword = '卡姿兰蜗牛气垫调控霜'
    j = handle_insert('er')

    print(j)