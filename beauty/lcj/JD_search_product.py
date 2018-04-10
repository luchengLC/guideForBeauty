from lcj import JD_spider
from lcj import JD_hk_spider
from lcj import JD_item
import datetime
import pymysql
from bs4 import BeautifulSoup as bs

def updateDB_baseMakeup(item,tableName):
    db = pymysql.connect(host="39.108.185.66", user="root", password="1234", db="beautyGirls_database", port=3306,
                         charset="utf8")
    cur = db.cursor()  # 获取操作游标
    try:
        cur.execute(
            "INSERT INTO %s( first_category,third_category,second_category,"
            "img1_address,img2_address,img3_address,img4_address,img5_address,"
            "address,price,description,number,name,"
            "brand,produce_address,comment_count,kg,good_for_who,"
            "expiration_date,color,result_effectiveness,category,makeup_effectiveness,"
            "good_comment_percentage,who_handly,get_time,good_for_skin,SPF,"
            "PA)"
            "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s',%f,'%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s')"
            % (tableName,item.first_category, item.third_category, item.second_category,
               item.img1_address, item.img2_address, item.img3_address, item.img4_address, item.img5_address,
               item.address, item.price, item.description, item.number, item.name,
               item.brand, item.produce_address, item.comment_count, item.kg, item.good_for_who,
               item.expiration_date, item.color, item.result_effectiveness, item.category,
               item.makeup_effectiveness,
               item.good_comment_percentage, item.who_handly, item.get_time, item.good_for_skin, item.SPF,
               item.PA)
        )
        db.commit()
    except Exception as e:
        print(e)
        #raise e
    finally:
        db.close()  # 关闭连接

def updateDB_lipstick(item, tableName):
    db = pymysql.connect(host="39.108.185.66", user="root", password="1234", db="beautyGirls_database", port=3306,
                         charset="utf8")
    cur = db.cursor()  # 获取操作游标
    try:
        cur.execute(
            "INSERT INTO %s( first_category,third_category,second_category,"
            "img1_address,img2_address,img3_address,img4_address,img5_address,"
            "address,price,description,number,name,"
            "brand,produce_address,comment_count,kg,good_for_who,"
            "expiration_date,color,result_effectiveness,category,makeup_effectiveness,"
            "good_comment_percentage,who_handly,get_time)"
            "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s',%f,'%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s','%s','%s','%s','%s','%s','%s','%s')"
            % (tableName, item.first_category, item.third_category, item.second_category,
               item.img1_address, item.img2_address, item.img3_address, item.img4_address, item.img5_address,
               item.address, item.price, item.description, item.number, item.name,
               item.brand, item.produce_address, item.comment_count, item.kg, item.good_for_who,
               item.expiration_date, item.color, item.result_effectiveness, item.category,
               item.makeup_effectiveness,
               item.good_comment_percentage, item.who_handly, item.get_time)
        )
        db.commit()
    except Exception as e:
        print(e)
        # raise e
    finally:
        db.close()  # 关闭连接

def updateDB_eye(item, tableName):
    db = pymysql.connect(host="39.108.185.66", user="root", password="1234", db="beautyGirls_database", port=3306,
                         charset="utf8")
    cur = db.cursor()  # 获取操作游标
    try:
        cur.execute(
            "INSERT INTO %s( first_category,third_category,second_category,"
            "img1_address,img2_address,img3_address,img4_address,img5_address,"
            "address,price,description,number,name,"
            "brand,produce_address,comment_count,kg,good_for_who,"
            "expiration_date,color,result_effectiveness,category,makeup_effectiveness,"
            "good_comment_percentage,who_handly,get_time)"
            "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s',%f,'%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s','%s','%s','%s','%s','%s','%s','%s')"
            % (tableName, item.first_category, item.third_category, item.second_category,
               item.img1_address, item.img2_address, item.img3_address, item.img4_address, item.img5_address,
               item.address, item.price, item.description, item.number, item.name,
               item.brand, item.produce_address, item.comment_count, item.kg, item.good_for_who,
               item.expiration_date, item.color, item.result_effectiveness, item.category,
               item.makeup_effectiveness,
               item.good_comment_percentage, item.who_handly, item.get_time)
        )
        db.commit()
    except Exception as e:
        print(e)
    finally:
        db.close()  # 关闭连接

# 区分是否属于全球购
def isHK(page):
    soup = bs(page, 'html.parser')
    try:
        div = soup.find('div', class_="crumb fl clearfix")
        kind = div.find_all('div', class_="item")
    except Exception as e:
        print("全球购")
        return 1
    else:
        print('京东购物')
        return 0

def getItemURL(url,filename):
    spider = JD_spider.getSpider()
    home_page_url = url  #'https://list.jd.com/list.html?cat=1316,1387,1420'
    page = spider.getPage(home_page_url)
    page_num = int(spider.getPageNum(page))
    fsock = open(filename, "a")
    for i in range(90,page_num+1):
        html_page = spider.getPage(home_page_url+ "&page=" + str(i))
        itemDetails = spider.getDetailURL(html_page)
        print('page:%s' % i)
        print(itemDetails)
        for i in itemDetails:
            fsock.write(i+'\n')
    fsock.close()


def searchItem(filename,one,two,three,db1,db2,method):
    file = open(filename, "r")
    while 1:
        line = file.readline()
        if not line:
            break
        line = line.strip("\n")
        spider = JD_spider.getSpider()
        curItem = JD_item.getItem()
        try:
            item_page = spider.getPage(line)
            curItem.address = line
            curItem.get_time = datetime.datetime.now()
            category = isHK(item_page)
            if category==0:
                spider = JD_spider.getSpider()
            else:
                spider = JD_hk_spider.getSpider()
            curItem = spider.getAttr(item_page,curItem,one,two,three)
            curItem = spider.getPriceByProxy(curItem)
        except Exception as err:
            print(err)
        else:
            try:
                print("商品链接："+curItem.address)
                print("商品全称："+curItem.description)
                print("商品价格：%s\n" %str(curItem.price))
                if category == 0:
                    if method=='baseMakeup':
                        updateDB_baseMakeup(curItem,db1)
                    elif method=='lipstick':
                        updateDB_lipstick(curItem, db1)
                    elif method=='eye':
                        updateDB_eye(curItem, db1)
                else:
                    if method=='baseMakeup':
                        updateDB_baseMakeup(curItem,db2)
                    elif method=='lipstick':
                        updateDB_lipstick(curItem, db2)
                    elif method=='eye':
                        updateDB_eye(curItem,db2)
            except Exception as err:
                print(err)
    file.close()


#getItemURL('https://list.jd.com/list.html?cat=1316,1387,1425',"D:/itemDetailURL_lipstick.txt")
#getItemURL('https://list.jd.com/list.html?cat=1316,1387,1420',"D:/itemDetailURL.txt")
searchItem("D:/itemDetailURL.txt",'美妆个护','香水彩妆','底妆','jd_product_baseMakeup','jd_hk_product_baseMakeup','baseMakeup')


#记住要先修改数据库表的内容
#getItemURL('https://list.jd.com/list.html?cat=1316,1387,1425',"D:/itemDetailURL_lipstick.txt")
#searchItem("D:/itemDetailURL_lipstick.txt",'美妆个护','香水彩妆','唇部','jd_product_lipstick','jd_hk_product_lipstick','lipstick')


#记住要先修改数据库表的内容
#getItemURL('https://list.jd.com/list.html?cat=1316,1387,13549',"D:/itemDetailURL_eye.txt")
#searchItem("D:/itemDetailURL_eye.txt",'美妆个护','香水彩妆','眼线','jd_product_eye','jd_hk_product_eye','eye')




    # for detail in itemDetails:
    #     item_page = spider.getPage(detail)
    #     curItem = JD_item.getItem()
    #     curItem.address = detail
    #     curItem.get_time = datetime.datetime.now()
    #     try:
    #         category = isHK(item_page)
    #         if category==0:
    #             spider = JD_spider.getSpider()
    #         else:
    #             spider = JD_hk_spider.getSpider()
    #         curItem = spider.getAttr(item_page,curItem)
    #         #curItem = spider.getPrice(curItem)
    #
    #         # print("类别："+curItem.first_category,curItem.second_category,curItem.third_category)
    #         # print("图片链接："+curItem.img1_address,curItem.img2_address,curItem.img3_address,curItem.img4_address,curItem.img5_address)
    #         # print("品牌："+curItem.brand)
    #         # print("名字：" + curItem.name)
    #         # print("编号："+curItem.number)
    #         # print("毛重："+curItem.kg)
    #         # print("产地："+curItem.produce_address)
    #         # print("适用人群：" + curItem.good_for_who)
    #         # print("适用肤质："+curItem.good_for_skin)
    #         # print("保质期："+curItem.expiration_date)
    #         # print("颜色："+curItem.color)
    #         # print("功效："+curItem.result_effectiveness)
    #         # print("分类："+curItem.category)
    #         # print("妆效："+curItem.makeup_effectiveness)
    #         # print("防晒指数：" + curItem.SPF)
    #         # print("PA值：" + curItem.PA)
    #         # print("好评率：" + curItem.good_comment_percentage)
    #         # print("评价总数：" + curItem.comment_count)
    #         # print('处理人：'+curItem.who_handly)
    #         # print('获取时间：'+str(curItem.get_time))
    #         # updateDB(curItem)
    #     except Exception as err:
    #         print(err)
    #     else:
    #         print("商品链接："+curItem.address)
    #         print("商品全称："+curItem.description)
    #         print("商品价格：" + str(curItem.price))
    #         print("success!!\n")

