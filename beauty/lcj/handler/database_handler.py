#!/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql

def execute_sql(sql,data):
    # print (sql)
    try:
        db = ''
        db = pymysql.connect(host="39.108.185.66", user="root", password="1234", db="beautyGirls_database", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql,data)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        # if len(results) <= 0:
        #     print("no such items in this table")
        return 1,results
    except Exception as err:
        print("handler err:"+str(err))
        return -1,str(err)
    finally:
        if db!='':
            db.close()  # 关闭连接