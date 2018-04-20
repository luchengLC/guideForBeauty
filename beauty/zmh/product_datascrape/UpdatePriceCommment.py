#!/usr/bin/python 
# -*- coding:utf-8 -*-

import threading
import time
import urllib.request
import urllib
import json
import django
from django.db.models.functions import Now
import os
# from beauty.zmh.dysms_python.dysms_python.demo_sms_send import send_sms
import uuid

os.environ['DJANGO_SETTINGS_MODULE'] = 'guideForBeauty.settings'
django.setup()
from beauty.models import ProductLipstick,UserCutPriceProduct
from django.db.models import Count, Avg, Max, Min, Sum


from beauty.lps.handler.updateTianMaoItem import updateTianMaoData


class UpdatePriceCommment:
    def __init__(self):
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
        if url.find('item.jd.com'):
            return 1
        elif url.find('detail.tmall.com'):
            return 2
        elif url.find("detail.vip.com"):
            return 3
        else:
            return 0

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
                print(url)
                new_price = ""
                old_price = ""
                new_comment_count = ""
                old_comment_count = ""
                new_good_comment_rate = ""

                if ("京东" in product.platform):
                    skuId = url.split('/')[-1].strip(".html")
                    print(skuId)
                    new_price = self.get_jd_price(skuId)
                    # print(new_price)
                    result = self.get_jd_comment(skuId)
                    new_comment_count = result['comment_count']
                    print(new_comment_count)
                    new_good_comment_rate = result['good_comment_rate']
                    # old_comment_count = product.new_comment_count
                    print(new_good_comment_rate)
                    # 更新评论总数
                    product.comment_increment = int(new_comment_count - product.comment_count)
                    product.comment_count = int(new_comment_count)

                    print("更新后的评论总数" + str(product.comment_count))
                    print("新增评论总数" + str(product.comment_increment))
                    # 更新好评率
                    product.good_comment_percentage = new_good_comment_rate
                    product.get_time = Now()
                    print("更新后的好评率" + str(new_good_comment_rate))
                    old_price = str(product.price)
                    product.price = new_price

                    product.save()

                elif("天猫" in product.platform):
                    updataUtil = updateTianMaoData()
                    new_price = updataUtil.update_tianmao(product.number, product.comment_count)


                # print("更新前的价格" + str(old_price))
                print("更新后的价格" + str(new_price))

                # 降价通知
                if new_price != old_price:
                    if new_price < old_price:
                        # 短信通知
                        self.inform_price_reduce(url)
                        pass
                    # 更新价格
                    print(product.price)

            except Exception as e:
                print(e)
                pass
            time.sleep(60)#自动休眠，每一小时爬一次数据
    # 获取商品并转换成list列表
    def get_products_list(self):
        try:
            max_id = 6
            products = self.product_table.objects.filter(platform="天猫")
            # products = self.product_table.objects.all()
            products = list(products)
            return products
        except Exception as e:
            print(e)
            # pass

    def inform_price_reduce(self,url = ""):
        # 获取关注该商品的用户
        product_users = UserCutPriceProduct.objects.filter(product_address=url)
        product_users = list(product_users)
        # user_phones = []
        user_phone = ""
        # for p_u in product_users:
        #     user_phone = p_u.user_phone
        #     __business_id = uuid.uuid1()
        #     params = p_u.product_name
        #     print(send_sms(__business_id, user_phone, "美妆商品导购系统", "SMS_130925712", params))
        # pass

if __name__ == '__main__':
    test = UpdatePriceCommment()
    test.__init__()
    # 唯品会id = 21204
    # url = "https://detail.vip.com/detail-2590192-464314661.html"

    # id = 1
    products = test.get_products_list()

    for product in products:
        test.update_price_comment(product)
    # threads = []
    # for product in products:
    #     threads.append(threading.Thread(target=test.update_price_comment, args=(product,)))
    #
    # for thread in threads:
    #     thread.start()
    # for thread in threads:
    #     thread.join()




