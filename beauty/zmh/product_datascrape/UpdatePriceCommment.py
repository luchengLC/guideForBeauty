#!/usr/bin/python 
# -*- coding:utf-8 -*-

# !/usr/bin/python
# -*- coding:utf-8 -*-
# !/usr/bin/python
# -*- coding:utf-8 -*-
import threading
import time
import urllib.request
import urllib
import json
import re
from bs4 import BeautifulSoup
import pymysql
import django
from django.db.models.functions import Now
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'guideForBeauty.settings'
django.setup()
from beauty.models import ProductLipstick
from django.db.models import Count, Avg, Max, Min, Sum


class UpdatePriceCommment:
    def __init__(self):
        # self.url = ""
        # self.html = ""
        # self.product_table = ProductLipstick
        self.product_table = ProductLipstick

    # 根据url下载html
    def gethtml(self, url):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req).read()
        # htmltemp = ""
        try:
            response = urllib.request.urlopen(req)
            self.html = response.read()
            # htmltemp = htmltemp.decode('utf-8')
        except Exception as e:
            print(e)
        return self.html

        # 判断url是唯品会还是京东的商品详情url
        # 返回1 是京东,返回2 是天猫，返回3 是唯品会
        def checkUrl(self, url):
            return 1

    # 判断商品来源，
    # 若是京东，返回1，若是天猫，返回2，若是唯品会，返回3，都不是返回0
    def checkPlatfrom(self,url=""):
        if url.find('jd'):
            return 1

    # 获取京东价格
    def get_jd_price(self,skuId):
        # 缺失异常处理
        if skuId is None:
            print("The skuId is error.the returned price is empty string")
            return ""
        else:
            try:
                price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + skuId
                price = ""
                content = json.loads(self.gethtml(price_url).decode("utf-8"))
                price = content[0]['op']
                return price
            except Exception as e:
                print(e)

    # 获取京东评论总数
    def get_jd_comment(self, skuId):
        result = {}
        result["comment_count"] = ""
        result["good_comment_rate"] = ""
        try:
            commentUrl = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + skuId
            jsondata = self.gethtml(commentUrl).decode("gbk")
            data = json.loads(jsondata)
            comment_count = data['CommentsCount'][0]["CommentCount"]
            good_comment_rate = data['CommentsCount'][0]["GoodRate"]
            result["comment_count"] = comment_count
            result["good_comment_rate"] = good_comment_rate
            print(result)
            return result
        except Exception as e:
            print(e)
            return result
            pass

    # 每小时更新一次商品价格
    def update_price_comment(self,product = ProductLipstick):
        while True:
            try:
                url = product.address
                new_price = ""
                new_comment_count = ""
                old_comment_count = ""
                new_good_comment_rate = ""

                if (self.checkPlatfrom(url) == 1):
                    skuId = url.split('/')[-1].strip(".html")
                    print(skuId)
                    new_price = self.get_jd_price(skuId)
                    # print(new_price)
                    result = self.get_jd_comment(skuId)
                    new_comment_count = result['comment_count']
                    print(new_comment_count)
                    new_good_comment_rate = result['good_comment_rate']
                    old_comment_count = product.new_comment_count
                    print(old_comment_count)
                new_price = float(new_price)
                old_price = float(product.price)

                print("更新前的价格" + str(old_price))
                print("更新后的价格" + str(new_price))
                print("更新前的评论总数" + str(product.comment_count)+"第2次"+str(product.new_comment_count))

                # 更新价格和降价通知
                if new_price != old_price:
                    if new_price < old_price:
                        pass
                    # 短信通知
                    # 更新价格
                    product.price = new_price
                    print(product.price)
                # 更新评论总数
                product.comment_count = product.new_comment_count
                product.new_comment_count = new_comment_count
                print("更新后的评论总数" + str(product.comment_count) + str(product.new_comment_count))
                # 更新好评率
                product.good_comment_percentage = new_good_comment_rate
                product.get_time = Now()
                print("更新后的好评率" + str(new_good_comment_rate))
                product.save()
            except Exception as e:
                print(e)
                pass
            time.sleep(60)#自动休眠，每一小时爬一次数据
    # 获取商品并转换成list列表
    def get_products_list(self):
        try:
            max_id = 6
            products = self.product_table.objects.filter(id__lt=max_id)
            # products = self.product_table.objects.all()
            products = list(products)
            return products
        except Exception as e:
            print(e)
            # pass
if __name__ == '__main__':
    test = UpdatePriceCommment()
    test.__init__()
    # 唯品会id = 21204
    # url = "https://detail.vip.com/detail-2590192-464314661.html"

    # id = 1
    products = test.get_products_list()
    threads = []
    for product in products:
        threads.append(threading.Thread(target=test.update_price_comment, args=(product,)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()




