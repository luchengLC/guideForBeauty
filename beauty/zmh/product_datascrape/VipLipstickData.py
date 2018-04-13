#!/usr/bin/python 
# -*- coding:utf-8 -*-
#!/usr/bin/python
# -*- coding:utf-8 -*-
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
from beauty.models import VipProductLipstick
from django.db.models import Count, Avg, Max, Min, Sum


class VipLipstickData:
    def __init__(self):
        self.url = ""
        self.html = ""
        self.product_table = VipProductLipstick

    # 根据url下载html
    def gethtml(self,url):
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

    # 根据商品详情url存储商品信息
    def get_product_data(self,html,product_obj = VipProductLipstick,sku_id = ""):
        try:
            # 基于bs4得到商品描述
            soup = BeautifulSoup(html, 'lxml')
            description = soup.find("span", class_="goods-description-title").text
            print(description)
            dict = {}
            para = soup.find_all("span", class_="g-parameter-title")
            para_content = soup.find_all("span", class_="g-parameter-content")
            para_number = 7
            for i in range(0, para_number):
                dict[para[i].text] = para_content[i].text
            print(dict)
            # 获取商品编号、规格、有效期
            number = ""
            kg = ""
            expiration_data = ""
            try:
                number = dict['商品编号：']
                kg = dict['规格：']
                expiration_data = dict[ '有效期：']
            except:
                pass
            # 颜色
            color = ""
            result_effectiveness = ""
            try:
                table_tr = soup.find_all("tr")
                result_effectiveness = table_tr[1].find_all("td")[1].text
                color = table_tr[0].find_all("td")[1].text
                print("颜色："+color)
                print("功效："+result_effectiveness)
            except:
                pass

            total_count = 1
            good_count = 0
            good_comment_percentage = 0
            # 获取商品评论信息
            try:
                html = html.decode('utf-8')
                res = re.search(r'^(.*)var PG(.*?) .*', html , re.M | re.I)
                total_string = res.group().split("=")[1]
                total_json = json.loads(total_string)
                skuList = total_json['product']['skuList']
                category_id = total_json['product']['categoryId']
                # 根据sku_id 和category_id获取评论url
                comment_url = "https://pcapi.vip.com/comment/getSumInfo.php?spuId="+str(sku_id)+"&catId="+str(category_id)
                # comment_url = 'https://pcapi.vip.com/comment/getSumInfo.php?spuId='+str(sku_id)+'&catId='+str(category_id)+'&_=1522508548556'
                print(comment_url)
                comment_para = self.gethtml(comment_url)
                # 解码成字符串
                comment_str = comment_para.decode('utf-8')
                print(comment_str)
                # 转换成json格式
                comment_json = json.loads(comment_str)
                total_count = comment_json['total_count']
                good_count = comment_json['good_count']
                good_comment_percentage = round(good_count/total_count,3)
                print(good_comment_percentage)
            except:
                pass
            # # 存进数据库
            product_obj.first_category = "美妆个护"
            product_obj.second_category = "唇部"
            product_obj.third_category = "香水彩妆"
            product_obj.description = description
            product_obj.number = number
            product_obj.comment_count = total_count
            product_obj.kg = kg
            product_obj.expiration_date = expiration_data
            product_obj.color = color
            product_obj.result_effectiveness = result_effectiveness
            product_obj.category = "唇膏/口红"
            product_obj.good_comment_percentage = good_comment_percentage
            product_obj.who_handly="张敏华"
            product_obj.get_time=Now()
            product_obj.save()
            print("保存成功")

        except Exception as e:
            print(e)
    # 获取全部商品的商品信息并存进数据库
    def get_products_data(self):
        min_id = 0
        max_id = 0
        # 获取最小id的记录
        min_record = VipProductLipstick.objects.values('platform').annotate(min_id=Min('id')).filter(platform='唯品会')
        # 将QuerySet对象转换成list 并获得最小id编号
        min_id = list(min_record)[0]['min_id']
        # 获取最大id的记录
        max_record = VipProductLipstick.objects.values('platform').annotate(max_id=Max('id')).filter(platform='唯品会')
        # 将QuerySet对象转换成list 并获得最小id编号
        max_id = list(max_record)[0]['max_id']
        print("最小id"+str(min_id))
        print("最大id" + str(max_id))

        for id in range(min_id, max_id+1):
            try:
                print(id)
                product = self.product_table.objects.get(id=id)
                print(product.address)
                url = product.address
                print(url)
                skuId = product.v_sku_id
                html = self.gethtml(url)
                self.get_product_data(html,product,skuId)
            except Exception as e:
                print("error")
                print(e)
                continue


if __name__ == '__main__':
    test = VipLipstickData()
    test.__init__()
    url = "https://detail.vip.com/detail-2473661-443210235.html"
    test.get_products_data()



