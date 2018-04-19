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


# 检查用户手机号码格式是否正确
def check_phone(user_phone):
    if((user_phone is None) or (user_phone == "")):
        return False
    else:
        return True

# 从数据库获取用户关注的商品列表
def get_products_list(user_phone = ""):
    products_list = []
    if(check_phone(user_phone) is False):
        print("手机号码不合法")
        return None

    try:
        products = UserCutPriceProduct.objects.filter(user_phone=user_phone)
        if products is not None:
            products_list = list(products)
            # print(products_list)
            return products_list
    except Exception as e:
        print(e)
        return -1

# 将查询结果的商品列表转换成json格式
def get_result_list(products_list=[]):
    result = {}
    result['error_code'] = 0
    result['msg'] = "该用户没有任何降价通知商品"
    data = {}
    data['item_list'] = []
    result['data'] = data
    result['product_count'] = 0
    if (products_list.__len__()!=0):
        result['msg'] = 'success'
        result['product_count'] = products_list.__len__()
        item_list = []
        product_dict = {}
        for product in products_list:
            product_dict['name'] = product.product_name
            product_dict['item_url'] = product.product_address
            product_dict['img_url'] = product.product_img_url
            product_dict['price'] = product.product_price
            product_dict['platform'] = product.product_platform
            product_dict['comment_count'] = product.product_comment_count
            item_list.append(product_dict)
        print("item_list" + str(item_list))
        data['item_list'] = item_list
        result['data'] = data
    return result


@require_http_methods(["GET"])
def handle_search(request):
        user_phone = request.GET.get('user_phone')
        # user_phone = '13411984677'
        print (user_phone)
        result = {}
        products_list = get_products_list(user_phone)
        if products_list == -1:
            result['error_code'] = 1
            result['msg'] = "服务器异常"
        else:
            result = get_result_list(products_list)
        print (result)
        return JsonResponse(result,safe=False)

if __name__ == '__main__':
    # http://127.0.0.1:8000/beauty/productsList/getProductsPage?wd=卡姿兰蜗牛气垫调控霜&PageNo=1
    # keyword = '卡姿兰蜗牛气垫调控霜'
    j = handle_search("e")
    print(j.content)