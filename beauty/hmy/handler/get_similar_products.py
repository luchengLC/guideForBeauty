#-*-coding=utf-8-*-
import urllib.request
import json
import pymysql
import haystack
import jieba
import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

#商品分类与数据库表映射关系

dicts={'底妆':'product_baseMakeup','乳液面霜':'product_baseMakeup','套装':'product_baseMakeup','爽肤水':'product_baseMakeup',
       '眼线':'product_eye','眉笔':'product_eye','睫毛膏':'product_eye','眼影':'product_eye',
       '唇部':'product_lipstick',
       '古龙水':'product_other_perfume','固体香水':'product_other_perfume',
       '香水':'product_perfume'}

'''
找相似商品功能
-nicole-
'''
from django.shortcuts import render
from sklearn.feature_extraction.text import CountVectorizer
import jieba
import math
from urllib import parse
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def getAllSimilarProducts(category,search_str):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #将输入的字符串进行结巴分词
    seg_list=jieba.cut_for_search(search_str)
    final_str=" ".join(seg_list)
    print(final_str)
    #确定在哪个数据表进行数据的查询
    table_name = dicts[category]
    #取出特定数据库表按照评论总数排序的前1000条数据
    #count--取数据库中前n条数据，top_n返回的列表最大数
    count=1000
    top_n=20
    #方法1
    getProductName_sql = "select name,number,price,img1_address,address,good_comment_percentage,comment_count,platform,description from" + ' ' + table_name + ' ' + "order by comment_count desc limit "+str(count)
    #print(getProductName_sql)
    #方法2
    #getProductName_sql="select name,number from"+' '+table_name+' '+"order by comment_count desc limit "+str(count)
    print(getProductName_sql)
    #链接数据库
    conn = pymysql.connect(host="39.108.185.66", port=3306, user='root', password='1234', db='beautyGirls_database',
                           charset='utf8mb4')
    cur=conn.cursor()
    cur.execute(getProductName_sql)
    res=cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
 #将商品名称文本放入list
    corpus = [res[i][0] for i in range(0,len(res))]
    #将当前点击的商品名称插入商品名称list
    corpus.insert(0,final_str)
    print(len(corpus))
    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值

    tfidf = transformer.fit_transform(
        vectorizer.fit_transform(corpus))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    juzhen=vectorizer.fit_transform(corpus).toarray()
    print(len(juzhen))
    #print(juzhen[0])
    word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    # print('词袋模型')
    # print(word)
#
#     #文本相似度比较
#     #简单比较文本的相似度
#     #     ##计算余弦值,第一个文本和第二个文本的相似度
#     #     #如果设置对角线的值都为1，不利于取最大值
    print(len(res))
    cos_list = [0 for i in range(len(res))]
    for w in range(1,len(res)+1):
        fenmu = 0
        fenzi_1 = 0
        fenzi_2 = 0
        for i in range(len(word)):
            fenmu=fenmu+juzhen[0][i]*juzhen[w][i]
            fenzi_1=fenzi_1+juzhen[0][i]*juzhen[0][i]
            fenzi_2=fenzi_2+juzhen[w][i]*juzhen[w][i]
        #print(fenzi_1,fenzi_2)
        if math.sqrt(fenzi_1)==0.0 or math.sqrt(fenzi_2)==0:
            cos=0
        else:
            cos=fenmu/(math.sqrt(fenzi_1)*math.sqrt(fenzi_2))
        cos_list[w-1]=cos

    #将文本相似度余弦值存入字典并排序
    index={}
    for i in range(len(res)):
        index[i]=cos_list[i]
    print(index)
    #排序
    index=sorted(index.items(),key=lambda x:x[1],reverse=True)
    print(index)
#取出相似度大的下标值index[i][0]

#方法1---------处理返回的数据
    #name,number,price,img1_address,address,
    # good_comment_percentage,comment_count,platform,description
    dict_data = {}
    datas=[]
    for i in range(top_n):
        if index[i][1]==0.0:
            break
        sample = {}
        try:
            sample['name'] = res[index[i][0]][0]
            sample['price'] = float(str(res[index[i][0]][2]))
            sample['img1_address']=res[index[i][0]][3]
            sample['address'] = res[index[i][0]][4]
            if float(res[index[i][0]][5])==0.0:
                sample['good_comment_percentage']=0
            else:
                sample['good_comment_percentage']=str(int(float(res[index[i][0]][5])*100))+'%'
            sample['comment_count']=int(res[index[i][0]][6])
            sample['platform']=res[index[i][0]][7]
            sample['description']=res[index[i][0]][8]
            datas.append(sample)
        except:
            pass
    dict_data['data'] = datas
    if len(dict_data['data'])==0:
        dict_data['error_code'] = 1
        dict_data['msg'] = '抱歉,搜索不到相似商品！'
        return dict_data
    dict_data['error_code'] = 0
    dict_data['msg'] = 'success'
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(len(dict_data['data']))
    return dict_data


#方法2
    # print(final_str)
    # num_set_str = ''
    # for i in range(top_n):
    #     # 输入positionId
    #     print(res[index[i][0]][1], res[index[i][0]][0])
    #     if index[i][1]==0.0:
    #         break
    #     num_set_str = num_set_str + "'" + res[index[i][0]][1] + "',"
    # print(num_set_str[0:-1])
    # select_sql="select name,price,img1_address,address,good_comment_percentage,comment_count,platform,description from "+table_name+" where number in("+num_set_str[0:-1]+")"
    # conn = pymysql.connect(host="39.108.185.66", port=3306, user='root', password='1234', db='beautyGirls_database',
    #                        charset='utf8mb4')
    # print (select_sql)
    # #游标
    # cur = conn.cursor()
    # #执行语句
    # cur.execute(select_sql)
    # #获取查询结果
    # num_list=cur.fetchall()
    # #存储要返回的数据对象
    # dict_data ={}
    # if len(num_list)==0:
    #     dict_data['error_code']=1
    #     dict_data['msg']='error'
    #     print("抱歉，无搜索到相关商品！")
    #     return dict_data
    #
    # dict_data['error_code'] = 0
    # dict_data['msg'] = 'success'
    # #将查询结果转化为列表类型
    # num_list=list(num_list)
    # #列表转为字典
    # datas=[]
    # for i in num_list:
    #     sample={}
    #     sample['name'] = i[0]
    #     sample['price'] = float(str(i[1]))
    #     sample['img1_address']=i[2]
    #     sample['address'] = i[3]
    #     if float(i[4])==0.0:
    #         sample['good_comment_percentage']=0
    #     else:
    #         sample['good_comment_percentage']=str(int(float(i[4])*100))+'%'
    #     sample['comment_count']=int(i[5])
    #     sample['platform']=i[6]
    #     sample['description']=i[7]
    #     datas.append(sample)
    # dict_data['data']=datas
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # return dict_data

@require_http_methods(["GET"])
def handle_search(request):
    pname= '阿玛尼（ARMANI）%20阿玛尼ARMANI%20口红%20唇膏%20唇釉%20红管#501%20玫瑰豆沙色%20热卖'
    category='唇部'
    res = getAllSimilarProducts(category, parse.unquote(str(pname)))
    return JsonResponse(res, safe=False)


#如何根据键入的关键词确定在哪个表查找
if __name__=='__main__':
    str_emm='阿玛尼（ARMANI）%20阿玛尼ARMANI%20口红%20唇膏%20唇釉%20红管#501%20玫瑰豆沙色%20热卖'
    res=getAllSimilarProducts('唇部',parse.unquote(str(str_emm)))
    #print(res['data'][0]['img1_address'])
    #print(res['error_code'])
    #print(res['msg'])
    print(res['data'])
    #print(str_emm)
    for i in range(10):
        print(res['data'][i]['name'],res['data'][i]['address'])
