#!/usr/bin/python 
# -*- coding:utf-8 -*-
#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib.request
import urllib
import json
import re
from bs4 import BeautifulSoup
import django
import os
from django.db.models.functions import Now
os.environ['DJANGO_SETTINGS_MODULE'] = 'guideForBeauty.settings'
django.setup()
from beauty.models import ProductPerfume
from django.db.models import Q
import time

class JDProductData:
    def __init__(self):

        # self.commentUrl = self.getCommentUrl()
        # self.html = self.getHtml(self.url)
        # self.soup = self.getSoup()
        # self.platform = self.getSource()
        self.product_table = ProductPerfume


    def getCommentUrl(self,skuId):
        commentUrl = ""
        if skuId is not None:
            commentUrl = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds="+skuId
        else:
            print("没有商品具体id，无法获得评论")
        return commentUrl

    # 检查url是否合法
    def checkUrl(self,url):
        flag = False
        if url is None:
            print("该商品的url为null")
        else:
            reg = "^https?:/{2}\w+(\.\w+)+([/?].*)?$"
            if re.match(reg,url):
                flag = True
        return flag

    def getHtml(self,url):
        # 定义http头部，很多网站对于你不携带User-Agent及Referer等情况，是不允许你爬取。
        # 具体的http的头部有些啥信息，你可以看chrome，右键审查元素，点击network，点击其中一个链接，查看request header
        # 先需要判断url是否合法
        get_time = 3 # 重复发送http请求的最大次数
        # 先检查url是否合法
        html = None
        if self.checkUrl(url):
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
        else:
            print("该url不合法")
            exit()
        return html

    def getSoup(self,html):
        if html is not None:
            return BeautifulSoup(html,'lxml')
        else:
            print("该商品的html内容为空")
            exit()

    # 获取商品来源：“京东”还是“京东全球购”
    def getSource(self,soup = BeautifulSoup):
        if soup is None:
            print("获取soup失败")

        hklogo = soup.find('div', class_="logo-head")
        platform = ""
        if hklogo is not None:
            print("该商品属于京东全球购")
            platform = hklogo.find('a')['alt']
            print(platform)
        else:
            print("该商品属于京东")
            platform = "京东购物"
        return platform
    # 获取"京东"商品介绍
    def crawlProductDescription(self, names=[],soup = BeautifulSoup):
        if soup is None:
            print("获取soup失败")
        results = {}
        try:
            # 因为不管是京东还是京东全球购，其商品介绍都是放在"p-parameter"这一div中，所以通过其来定位
            divSoup = soup.find('div',class_="p-parameter")
            if divSoup is not None:
                lis = divSoup.find_all('li')
                for li in lis:
                    # print(li.getText().strip(" ").strip())
                    line = li.getText().strip(" ").strip()
                    lineToArray = line.split("：")
                    results[lineToArray[0]] = lineToArray[1]
                # 将剩余的name设置为null
                for name in names:
                    if name not in results.keys():
                        results[name] = "null"
            else:
                for name in names:
                    if name not in results.keys():
                        results[name] = "null"
        except AttributeError as e:
            for name in names:
                results[name] = "null"
        return results


    # 获取"京东"商品规格
    def crawlJDProductFormat(self, soup = BeautifulSoup, names=[]):
        if soup is None:
            print("获取soup失败")
        results = {}
        try:
            items = soup.find("div", class_="Ptable-item").find_all("dt")
            if items is not None:
                for item in items:
                    for index in range(len(names)):
                        if names[index] in item.string:
                            results[names[index]] = item.next_sibling.string
                            del names[index]
                            break
                # 将剩余的没有被匹配到的数据全部设置为null
                for name in names:
                    results[name] = "null"
            else:
                for name in names:
                    results[name] = "null"
        except AttributeError as e:
            for name in names:
                results[name] = "null"
        return results

    # 获取价格
    def crawlProductPrice(self,skuId):
        if id is not None:
            price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + skuId
            result = ""
            content = json.loads(self.getHtml(price_url).decode("utf-8"))
            result = content[0]['op']
        else:
            print("The skuId is None.")
        return result

    # 获取评论总数和好评率
    def crawlProductComment(self,commentUrl):
        # url = self.scriptUrl
        result = {}
        if commentUrl is not None:
            try:
                # jsondata = urllib.request.urlopen(url).read().decode("gbk")  #返回的是json
                # jsondata = html[0:-2]
                jsondata = self.getHtml(commentUrl).decode("gbk")

                data = json.loads(jsondata)

                commentNum = data['CommentsCount'][0]["CommentCount"]
                favourableComment = data['CommentsCount'][0]["GoodRate"]
                result["评价总数"] = commentNum
                result["好评率"] = favourableComment
            except urllib.error.URLError as e:
                print(e.reason)
        return result


    # 获取商品全称
    def crawlTotalName(self,soup = BeautifulSoup):
        data = ""
        if soup is None:
            print("获取soup失败")
        divSoup = soup.find('div', class_="sku-name")
        product_decsription = " "
        if divSoup is not None:
            product_decsription = divSoup.getText()
            product_decsription = product_decsription.strip(" ").strip()
            print(product_decsription)
        return product_decsription
        # element = self.soup.find("div", class_="sku-name", recursive=True)
        # for string in element.stripped_strings:
        #     data = string
        # # print("商品全称：\t"+data)
        # return data
    # 获取图片
    def crawlPicture(self,soup):
        if soup is None:
            print("获取soup失败")
        divSoup =soup.find('div', class_="spec-items")
        imgAddresses = [None] * 10  # 生成长度为5，初始值为None的列表

        if divSoup is not None:
            divSoup = divSoup.find('ul')
            imgSoup = divSoup.find_all('li')
            i = 0
            for li in imgSoup:
                imgsrc = li.find('img')['src']
                imgAddresses[i] = imgsrc
                i = i+1

            print(imgAddresses)
        return imgAddresses

    # 根据url更新数据库的商品信息
    def update_product_data(self):
        min_id = 6320
        max_id = 7320
        for id in range(min_id, max_id):
            try:
                print(id)
                time.sleep(1.0)
                product = ProductPerfume.objects.get(id=id)
                print(product.address)
                url = product.address
                print(url)

                skuId = url.split('/')[-1].strip(".html")
                print(skuId)
                # 爬取商品详情页面html内容
                html = self.getHtml(url)
                soup = self.getSoup(html)


                # 获取商品来源
                product.platform = self.getSource(soup)
                # test.__init__("https://item.jd.com/1024127744.html", 1024127744)
                name = ["品牌", "商品名称", "商品编号", "店铺", "商品毛重", "商品产地", "包装", "香调",
                        "净含量", "分类", "性别", "适用场景"]
                # 获取商品介绍

                results = self.crawlProductDescription(name,soup)
                print(results)
                product.brand = results["品牌"]
                product.name = results["商品名称"]
                product.number = results["商品编号"]
                product.store = results["店铺"]
                product.kg = results["商品毛重"]
                product.produce_address = results["商品产地"]
                product.package = results["包装"]
                product.fragrance = results["香调"]
                product.clean_weight = results["净含量"]
                product.category = results["分类"]
                product.sex = results["性别"]
                product.first_category = "美妆个护"
                product.second_category = "香水"
                product.third_category = "香水彩妆"
                # 获取商品价格
                product.price = float(self.crawlProductPrice(skuId))
                print("商品价格：" + str(product.price))

                # 获取商品的好评率和评论总数
                # url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=1458843"
                comment_url = self.getCommentUrl(skuId)
                results = self.crawlProductComment(comment_url)

                product.comment_count = results["评价总数"]
                product.good_comment_percentage = results["好评率"]
                print(results)

                # 获取商品的全称

                product.description = self.crawlTotalName(soup)
                print("商品全称：" + product.description)
                # 获取图片
                imageUrls = self.crawlPicture(soup)
                product.img1_address = imageUrls[0]
                product.img2_address = imageUrls[1]
                product.img3_address = imageUrls[2]
                product.img4_address = imageUrls[3]
                product.img5_address = imageUrls[4]
                print("第五张图片{}".format(product.img5_address))

                if (product.platform == "京东购物"):
                    name = ["保质期", "适用人群", "香型"]
                    results = self.crawlJDProductFormat(soup,name)
                    product.expiration_date = results["保质期"]
                    product.good_for_who = results["适用人群"]
                    product.fragrance_type = results["香型"]
                    print(results)
                    # 类别
                    if self.soup.find('a', clstag='shangpin|keycount|product|mbNav-1') is not None:
                        product.first_category = soup.find('a', clstag='shangpin|keycount|product|mbNav-1').getText()
                        print(product.first_category)
                        product.second_category = soup.find('a', clstag='shangpin|keycount|product|mbNav-2').getText()
                        print(product.second_category)
                        product.third_category = soup.find('a', clstag='shangpin|keycount|product|mbNav-3').getText()
                        print(product.third_category)
                product.get_time = Now()
                product.who_handly = "张敏华"
                product.finish_get_data = 1
                product.save()
            except Exception as e:
                print("error")
                print(e)
                continue


if __name__ == "__main__":
    # 不能获取的有26、98、166、189,200,261,443,547,548
    # 569，620,2141,2166,2197,2228,2283,2356，2641
    # 2777，2885
    # 7393
    test = JDProductData()
    test.update_product_data()




