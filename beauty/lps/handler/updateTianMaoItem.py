import requests
from bs4 import BeautifulSoup
import re
import json
import time
from beauty.lps.handler.SQL import save_mysql
# from SQL import save_mysql

'''
更新天猫的评论总数、价格、评论总数的新增数目
'''
class updateTianMaoData:
    #更新天猫数据
    def update_tianmao(self,number,old_comment_count):
        comment=self.get_new_comment(number)
        comment_increment = int(comment['comment_count'])-int(old_comment_count)
        price = self.get_new_price(number)
        localtime =time.asctime(time.localtime(time.time()))
        #将新的评论数保存到数据库中
        mysql = save_mysql()
        table = "product_lipstick"
        print("table=",table," price=", price, " comment_count=",comment['comment_count'], " comment_increment=",comment_increment," local_time=",localtime)
        sqlString = 'update {0} set price={1},comment_count={2},comment_increment={3},get_time="{5}" where number = "{4}" ' \
            .format(table, price, comment['comment_count'], comment_increment, number, localtime)
        #print("sqlString: ",sqlString)
        #更新数据库
        mysql.update_product(sqlString)
        return price

    #获取最新的评论总数
    def get_new_comment(self,number):
        comments = {}
        url = "https://dsr-rate.tmall.com/list_dsr_info.htm?itemId={}".format(number)
        html = requests.get(url).text
        tmp = re.search("\(.*\)", html).span()
        html = html[tmp[0]:tmp[1]][1:-1]
        datas = json.loads(html)
        #评论总数
        comments['comment_count'] = datas['dsr']['rateTotal']
        # 好评率
        comments['good_comment_percentage'] = round(float(datas['dsr']['gradeAvg']) / 5 * 100, 2)
       # print(comments)
        return comments

    #获取最新的价格
    def get_new_price(self,number):
        #url = "https://mdskip.taobao.com/core/initItemDetail.htm?&itemId={}".format(number)
        url = "https://mdskip.taobao.com/core/initItemDetail.htm?isUseInventoryCenter=false&cartEnable=true&service3C=false&isApparel=false&isSecKill=false&tmallBuySupport=true&isAreaSell=false&tryBeforeBuy=false&offlineShop=false&itemId=527562321013&showShopProm=false&cachedTimestamp=1524122646866&isPurchaseMallPage=false&isRegionLevel=false&household=false&sellerPreview=false&queryMemberRight=true&addressLevel=2&isForbidBuyItem=false&callback=setMdskip&timestamp=1524153059235&isg=null&isg2=BHNzIT54LcILj-GDZkqEq1joAncxvvS1jultZSUQ8RLJJJPGrHiXutH12lTKgF9i"
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Referer': "https://detail.tmall.com/item.htm?id={}".format(number) ,# 这里应对阿里云服务器的反爬虫策略
            'cookie':"miid=2064045362155919045; thw=cn; UM_distinctid=15f60fabe0a68-0646a2667dfadc-c303767-100200-15f60fabe178b; ali_ab=183.233.227.60.1509160562107.8; cna=PfJcEe0OL2cCAXkLEg6BD9Z8; ucn=unsz; hng=CN%7Czh-CN%7CCNY%7C156; t=37be738ed9cbc0b02db323167c9c98da; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; tracknick=%5Cu5B88%5Cu5019%5Cu661F%5Cu7A7A526; lgc=%5Cu5B88%5Cu5019%5Cu661F%5Cu7A7A526; enc=tpYp8wsD63OalqKivLeOd8DWzgTPSQH4xG%2FsIfN%2FWBdCDHZWPJez28l%2Fey7Rd6GzBdfDmMvDT1F0w1a%2FIeX3JA%3D%3D; cookie2=1ac65f635082d5408298ce73ed70fcf6; _tb_token_=3e17333e3eb13; v=0; uc1=cookie14=UoTeOonY9DFSuw%3D%3D&lng=zh_CN&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&tag=8&cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0; uc3=nk2=qUryzZZwAX4I2pw%3D&id2=Uone9meuUHQlNA%3D%3D&vt3=F8dBz4D%2F5SOdlmyFLzU%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTUyNDE1MzY0NQ%3D%3D; dnk=%E5%AE%88%E5%80%99%E6%98%9F%E7%A9%BA526; sg=676; csg=f306c286; mt=np=; cookie1=VFIaO0pjrhcKzRtJqbRCme7k60m7UpQBBR%2BbbwdDZ0w%3D; unb=1856428797; skt=9694dc4696f3c79e; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; _nk_=%5Cu5B88%5Cu5019%5Cu661F%5Cu7A7A526; cookie17=Uone9meuUHQlNA%3D%3D; isg=BPHxrPJ8D1jCKaBeDOwlhqfMAH0nyJaPQIcvn9MG7bjX-hFMGy51IJ8bGI6cNv2I"
        }
        html = requests.get(url, headers=header).text
        tmp = re.search("\(.*\)", html).span()
        html = html[tmp[0]:tmp[1]][1:-1]
        print("html:\n")
        print(html)
        datas = json.loads(html.strip())

        '''
        try:
            datas = json.loads(html.strip())
        except Exception as e:
            print(e)
            return None
        '''
        try:
            prices = datas['defaultModel']['itemPriceResultDO']['priceInfo']
            keys = list(prices.keys())
            result = None
            if keys is None:
                raise Exception('NullException')
            key = keys[0]
            results = prices[key]["promotionList"][0]['price']
            return results
        except (KeyError, Exception):
            prices = datas['defaultModel']['itemPriceResultDO']['priceInfo']
            keys = list(prices.keys())
            results = None
            key = keys[0]
            results = prices[key]['price']
            return results



    '''
    今日热搜，返回新增评论数目最多的20条
    '''
    def getHotProduct(self):
        table=["product_baseMakeup","product_eye","product_lipstick","product_perfume","product_other_perfume"]
        self.get20Products(table[2])
        pass

    def get20Products(self,table):
        mysql = save_mysql()
        sqlString = 'select * from {} order by comment_increment desc limit 5'.format(table)
        # 查询数据库
        result = mysql.get_product_data(sqlString)
        return result

if __name__=="__main__":
    updataUtil = updateTianMaoData()
    updataUtil.update_tianmao(527562321013, '69')
    #update_tianmao(1,543476146622,'1666')

    #getHotProduct()
