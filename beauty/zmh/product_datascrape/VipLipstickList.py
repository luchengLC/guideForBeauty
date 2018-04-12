#!/usr/bin/python 
# -*- coding:utf-8 -*-
import urllib.request
import urllib
import json
import re
from bs4 import BeautifulSoup
import pymysql
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'guideForBeauty.settings'
django.setup()
from beauty.models import VipProductLipstick

class VipLipstickList:
    def __init__(self):
        self.product_list_urls = []
        self.product_urls = [] # 所有商品的url地址
        self.product_table = VipProductLipstick


    # 根据url下载html
    def gethtml(self,url):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req).read()
        htmltemp = ""
        try:
            response = urllib.request.urlopen(req)
            htmltemp = response.read()
            # htmltemp = htmltemp.decode('utf-8')
        except Exception as e:
            print(e)
        return htmltemp

    # 返回唯品会唇彩类商品列表的总页数
    def get_total_page(self):
        url = "https://category.vip.com/search-1-0-1.html?q=3|29810||&rp=30071|29733#J_catSite"
        html_body = self.gethtml(url)
        # 基于bs4得到 页数
        soup = BeautifulSoup(html_body, 'lxml')
        total_page = soup.find("span", class_="total-item-nums")
        print(total_page.text)
        total_page = total_page.text
        pages_num = total_page.split("共")[1].split("页")[0]
        # print(pages_num)
        return int(pages_num)

    # 得到某一页的productIds
    def get_productIds(self,html_body):
        html_body = html_body.decode('utf-8')
        res = re.search(r'^(.*)Var.set(.*?) .*', html_body, re.M | re.I)
        total_string = res.group().split("{")[1].split("}")[0]
        # print(total_string.split("[")[1].split("]")[0])
        productIds = total_string.split("[")[1].split("]")[0].split(",")
        print(productIds)
        print(len(productIds))
        return productIds

    # 得到所有的productIds
    def get_all_productIds(self,pages_number):
        # print(pages_number)
        # urls_list = []
        productIds = []
        for num in range(0, pages_number):
            print(num)
            url = "https://category.vip.com/search-1-0-" + str(num) + ".html?q=3|29810||&rp=30071|29733#J_catSite"
            # urls_list.append(url)
            html_body = self.gethtml(url)
            # 得到当前页面的所有productIds
            productIds_temp = self.get_productIds(html_body)
            productIds.extend(productIds_temp)

        print(productIds)
        print(len(productIds))
        return productIds

    def get_all_detail_url(self):
        # 得到商品列表总页数
        try:
            pages_number = self.get_total_page()
            # 得到所有的productIds
            productIds = self.get_all_productIds(pages_number)

            i = 0
            for pro_id in productIds:
                # 删除多余的”号，如"186718322" → 186718322
                i = i + 1
                print("第"+str(i)+"条数据")
                pro_id = pro_id.split("\"")[1]
                print(pro_id)
                # pro_id_url = "https://category.vip.com/ajax/mapi.php?service=product_info&callback=categoryMerchandiseInfo1&productIds="+pro_id+"&functions=brandShowName,surprisePrice,pcExtra&warehouse=VIP_NH&mobile_platform=1&app_name=shop_pc&app_version=4.0&mars_cid=1520750355433_e9ef7a59431a17e0468612bf07778c4c&fdc_area_id=&_=1521644787532"
                pro_id_url = "https://category.vip.com/ajax/mapi.php?service=product_info&productIds=" + str(
                    pro_id) + "&functions=brandShowName,surprisePrice,pcExtra&warehouse=VIP_NH&mobile_platform=1&app_name=shop_pc&app_version=4.0&mars_cid=1520750355433_e9ef7a59431a17e0468612bf07778c4c&fdc_area_id=&_=1521644787532"
                print(pro_id_url)
                pro_string = self.gethtml(pro_id_url).decode('utf-8')
                # pro_string = pro_string.split("(")[1].split(")")[0]
                # 截取json字符串
                # pro_string = re.split(r"\((.*)\)", pro_string)[1]

                print(pro_string)

                pro_json = json.loads(pro_string)
                print(str(pro_json))
                product = pro_json['data']['products']
                # print(product[0].keys())
                brand_id = product[0]['brandId']
                # 商品详情url
                detail_url = "https://detail.vip.com/detail-" + str(brand_id) + "-" + str(pro_id) + ".html"
                print(detail_url)

                # 商品价格、图片
                vip_shop_price = product[0]['vipshopPrice']
                img1_address = product[0]['smallImage']
                product_name = product[0]['productName']
                brand_name = product[0]['brandShowName']
                v_sku_id = product[0]['vSpuId']
                print(v_sku_id)
                platform = "唯品会"
                # 存进数据库
                product_obj = self.product_table(img1_address = img1_address,name=product_name,
                                                 address = detail_url,price=vip_shop_price,
                                                 brand = brand_name,platform = platform,v_sku_id= v_sku_id)
                product_obj.save()
                # self.product_table.save()
                #  detail_urls.append(detail_url)
        except:
            pass

if __name__ == '__main__':
    test = VipLipstickList()
    test.__init__()
    test.get_all_detail_url()


