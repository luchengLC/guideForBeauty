#!/usr/bin/python 
# -*- coding:utf-8 -*-
import  os
import  sys
import urllib.request
import urllib
import socket
import json
import re
from bs4 import BeautifulSoup
import pymysql
import django
django.setup()
from beauty.models import JdPerfumeList

class JDPerfumeList:
    def __init__(self):
        self.productListUrls = []
        self.productUrls = set() # 所有商品的url地址
        self.headers = {"Host": "ss.3.cn",
                   "Origin": "http://www.jd.com/",
                   "Referer": "http://www.jd.com/",
                   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "Accept": "*/*",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                   }
        self.perfumeTable = JdPerfumeList

    # 根据url下载html
    def get_html(self,url):
        # 定义http头部，很多网站对于你不携带User-Agent及Referer等情况，是不允许你爬取。
        # 具体的http的头部有些啥信息，你可以看chrome，右键审查元素，点击network，点击其中一个链接，查看request header
        # 先需要判断url是否合法
        get_time = 3 # 重复发送http请求的最大次数
        # if(isLegalUrl(url)):
        if(url != None):
            req = urllib.request.Request(url)
            req.add_header("Referer", "http://www.jd.com/")
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

            while(get_time > 0):
                try:
                    response = urllib.request.urlopen(req)
                    html = response.read()
                    # print(html)
                    return html
                    break # 成功获取html，跳出循环
                except urllib.error.HTTPError as e:
                    print("Download error: ", e.reason)
                    if 500 <= e.code and e.code < 600:  # 5XX:当错误发生在服务端时,重新发送2次
                        get_time = get_time-1
                    else:
                        break


    # 返回商品列表的总页数
    def get_product_list_total_pages(self,startUrl):
        # 从第一页的商品列表的html页面中得到商品列表的总页数
        # startUrl = "https://coll.jd.com/list.html?sub=12469&page=1&JL=6_0_0"
        firstListHtml = self.get_html(startUrl)
        # with open("list.html", 'wb') as file_object:
        #     file_object.write(firstHtml)
        #     file_object.flush()
        # with open("list.html", 'rb') as file:
        #     firstListHtml = file.read()
        firstListHtml = firstListHtml.decode('utf8')
        print(firstListHtml)
        # 通过正则表达式从html页面中得到商品列表总页数
        list_pages_tag = re.search(r"共<b>(.*?)<\/b>页", firstListHtml)
        total_list_pages = re.search(r"\d+",list_pages_tag.group())
        total_list_pages = total_list_pages.group()
        if (total_list_pages!=None):
            return total_list_pages
        else:
            return -1
    # 返回商品列表的全部url
    def get_product_list_urls(self,startUrl):
        # startUrl = "https://coll.jd.com/list.html?sub=12469&page=1&JL=6_0_0"
        startUrlSub = startUrl.split("&")[0].split("+")[1]
        startUrlSub = int(startUrlSub)
        print(startUrlSub)
        list_total_pages = self.get_product_list_total_pages(startUrl)
        if(list_total_pages == -1):
            print("无法得到商品总页数，请检查url是否正确")
            return None
        elif(list_total_pages == 0):
            print("商品总页数等于0,没有商品")
            return None
        else:
            for page in range(1, int(list_total_pages)+1):
                list_page = "https://coll.jd.com/list.html?sub={}&page={}&JL=6_0_0".format(startUrlSub,page)
                print(list_page)
                self.productListUrls.append(list_page)
            print(self.productListUrls)
            return self.productListUrls

    # 得到一类商品的url并存进数据库
    def get_product_urls(self,product_list_urls = [],category=""):

        for product_list in product_list_urls:
            print(product_list)
            list_html = self.get_html(product_list)
            list_html = list_html.decode('utf8')
            res = re.search(r'^(.*)var attrList(.*?) .*', list_html, re.M | re.I)
            attrString = res.group().strip(';').split("=")[1]
            attrDict = eval(attrString)
            # print(type(attrDict))
            attrkeys = attrDict.keys()

            for product_url_id in attrkeys:
                product_url = "https://item.jd.com/{}.html".format(product_url_id)
                self.productUrls.add(product_url)
                self.perfumeTable.save(category=category,product_address = product_url, finish_scrape = 0)
            print(self.productUrls)

if __name__ == '__main__':
    test = JDPerfumeList()
    test.__init__()
    # test.get_product_list_urls()
    a = "test"
    list_test = []
    list_test.append("https://coll.jd.com/list.html?sub=12473&page=2&JL=6_0_0")
    # list_test.append("https://coll.jd.com/list.html?sub=12473&page=1&JL=6_0_0")
    test.get_product_urls(list_test)
