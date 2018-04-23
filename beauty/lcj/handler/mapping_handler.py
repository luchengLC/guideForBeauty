#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from operator import itemgetter
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from beauty.lcj.handler import database_handler
from beauty.lcj.handler import similarity_util
from beauty.lcj.handler import file_util
import jieba

file_path = (os.path.dirname(os.path.abspath("mapping_handler.py")) + '/beauty/lcj/data/').replace('\\','/')

#获取应该去哪些数据库表中查询
def get_tables_and_keywords(keyword):
    #获取需要模糊匹配的单词
    file_util.del_duplicate('train_files/dictionary.txt')
    jieba.load_userdict(file_path + 'train_files/dictionary.txt')
    temp = list(jieba.cut(keyword))
    first_keywprd = temp[0]
    keywords = ''
    for i in temp:
        if i !=' ':
            keywords = keywords+'+'+i+' '
    print (keywords)

    if keyword.find('唇')>=0 or keyword.find('口')>=0 or keyword.find('嘴')>=0:
        tables = ['product_lipstick']
    elif keyword.find('眼')>=0 or keyword.find('睫毛')>=0 or keyword.find('眉')>=0:
        tables = ['product_eye']
    elif keyword.find('香水')>=0:
        tables = ['product_perfume','product_other_perfume']
    elif keyword.find('霜')>=0 or keyword.find('乳')>=0 or keyword.find('液')>=0 or keyword.find('水')>=0:
        tables = ['product_baseMakeup']
    else:
        tables = similarity_util.get_similar_type(first_keywprd)
    return tables,keywords

def get_other_tables(tables):
    kinds = ['product_lipstick','product_eye','product_perfume', 'product_baseMakeup','product_other_perfume']
    for i in tables:
        kinds.remove(i)
    return kinds

def handle_sql_results(tables,keywords,page_no,order):
    #获取需要进行查询的sql语句
    sql_list = []
    for i in tables:
        sql = 'select name,price,img1_address,address,good_comment_percentage,comment_count,platform,description,third_category from '+i+' ' \
       'where match(key_words) against(%s in boolean mode);'
        sql_list.append(sql)

    #进行sql查询并处理查询结果
    result = {}
    all_list = []
    for i in sql_list:
        temp = database_handler.search_sql(i,keywords)
        code = int(temp[0])
        if code==-1:
            result['error_code'] = 1
            result['msg'] = temp[1]
            result['page_count'] = 0
            continue
        temp = list(temp[1])
        if len(temp)==0:
            continue

        for j in temp:
            item = list(j)
            comment_num = item[5]
            index = comment_num.find('.')
            if index > 0:
                item[5] = int(comment_num[0:index])
            item[4] = float(item[4])
            all_list.append(item)

    if len(all_list) ==0:
        result['error_code'] = 1
        result['msg'] = '搜索不出对应的产品!'
        result['page_count'] = 0
        return result

    if order=='df':
        all_list.sort(key=itemgetter(5,4), reverse=True)
    elif order=='pu':
        all_list.sort(key=itemgetter(1))
    else:
        all_list.sort(key=itemgetter(1), reverse=True)

    items = []
    start = (page_no-1)*20
    for i in range(start,start+20):
        if(i<len(all_list)):
            temp = {}
            temp["name"] = all_list[i][0]
            temp["price"] = float(all_list[i][1])
            temp["img1_address"] = all_list[i][2]
            temp["address"] = all_list[i][3]
            temp["good_comment_percentage"] = all_list[i][4]
            temp["comment_count"] = int(all_list[i][5])
            temp["platform"] = all_list[i][6]
            temp["description"] = all_list[i][7]
            temp["category"] = all_list[i][8]
            items.append(temp)

    data = {}
    data['item_list'] = items
    result['error_code'] = 0
    result['msg'] = 'success'
    result['data'] = data

    page_count = int(len(all_list)/20)
    if len(all_list)%20>0 :
        page_count +=1
    result['page_count'] = page_count

    if page_no>page_count:
        result['error_code'] = 1
        result['msg'] = '输入的页数超过范围啦！'
    return result

def get_products_page(keyword,page_no,order):
    result = get_tables_and_keywords(keyword)
    tables = result[0]
    keywords = result[1]
    result = handle_sql_results(tables, keywords, page_no,order)
    # page_count = int(result['page_count'])
    # if page_count<=1:
    #     tables = get_other_tables(tables)
    #     result = handle_sql_results(tables, keywords, page_no,order)
    return result

@require_http_methods(["GET"])
def handle_search(request):
        keywords = request.GET.get('wd').replace('%20','')
        page_no = request.GET.get('PageNo')
        order = request.GET.get('order')
        results = get_products_page(keywords,int(page_no),order)
        return JsonResponse(results,safe=False)

if __name__ == '__main__':
    #http://127.0.0.1:8000/beauty/productsList/getProductsPage?wd=卡姿兰蜗牛气垫调控霜&PageNo=1&order=pu
    #http://127.0.0.1:8000/beauty/productsList/getProductsPage?wd=美宝莲%20唇妆%20滋润&PageNo=1&order=df
    #http://127.0.0.1:8000/beauty/productsList/getProductsPage?wd=kissme&PageNo=1&order=pd
    # keyword = '卡姿兰蜗牛气垫调控霜'
    keyword = '卡姿兰'
    page_no = 1
    get_products_page(keyword,page_no)
    # E:\ComputerScience\4.2 - Senior\Mine\guideForBeauty\beauty\lcj\handler\mapping_handler.py
    #select key_words from product_lipstick where key_words like '%礼袋%'  and key_words like '%唇膏%' and key_words like '%迪奥%' and key_words like '%哑光%'
