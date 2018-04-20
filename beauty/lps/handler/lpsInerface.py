import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json

from beauty.models import ProductLipstick, ProductEye, ProductBasemakeup, ProductOtherPerfume, ProductPerfume
from beauty.lps.handler.updateTianMaoItem import updateTianMaoData


# -----------------------------------更新天猫数据--------------------------------------
def update_tianmao(request):
    response = {}
    try:
       # id = request.GET.get('id')
        number = request.GET.get('number')
        old_comment_count = request.GET.get('old_comment_count')
        updataUtil = updateTianMaoData()
       # updataUtil.update_tianmao(id, number, old_comment_count)
        updataUtil.update_tianmao(number, old_comment_count)
        response["status"] = "success"
    except Exception as e:
        print(e)
        response["status"] = "server error!"
    return JsonResponse(response)


# -----------------------------------  今日热搜  --------------------------------------
def getHotProduct(request):
    response = {}
    try:
        hotDatas = get20HotProducts()
        response['error_code'] = 0
        response['msg'] = 'success'
        datalist = []
        for hotData in hotDatas:
            data = {}
            # data['description'] = hotData.description
            data['item_url'] = hotData.address
            data['img_url'] = hotData.img1_address
            # data['img2_address'] = hotData.img2_address
            data['brand'] = hotData.brand
            data['price'] = hotData.price
            data['name'] = hotData.name
            data['platform'] = hotData.platform
            datalist.append(data)
        response['data'] = {'item_list': datalist, "product_count": 20}

    except Exception as e:
        print(e)
        response['error_code'] = 1
        response['msg'] = 'Server Error!'

    return JsonResponse(response)


def get20HotProducts():
    # 获取lipstick的数据
    print("\nother lipstick:")
    results = list(ProductLipstick.objects.order_by("-comment_increment")[0:20])
    # 获取otherPerfume 的数据
    datas = list(ProductOtherPerfume.objects.order_by("-comment_increment")[0:20])
    sort_product(results, datas)
    # 获取eye的数据
    datas = list(ProductEye.objects.order_by("-comment_increment")[0:20])
    sort_product(results, datas)
    # 获取perfume的数据
    datas = list(ProductPerfume.objects.order_by("-comment_increment")[0:20])
    sort_product(results, datas)
    # 获取baseMakeup的数据
    datas = list(ProductBasemakeup.objects.order_by("-comment_increment")[0:20])
    sort_product(results, datas)
    return results[0:20]


# 将商品按照新增评论从多到少排序
def sort_product(dest, source):
    for i in range(len(source)):
        j = 0
        while j < len(dest) and dest[j].comment_increment > source[i].comment_increment:
            j += 1
        dest.insert(j, source[i])
