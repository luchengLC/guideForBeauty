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
from beauty.models import ProductBasemakeup,ProductEye,ProductLipstick
from django.db.models import F
from django.db.models.functions import Now
class DataClean:
    def __init__(self):
        self.table = ProductLipstick

if __name__ == "__main__":
    test = DataClean()
    min_id = 1
    # max_id = 7
    max_id = 53049
    for id in range(min_id, max_id):
        print(str(id))
        try:
            product = test.table.objects.get(id=id)
            # 将好评率转换成小数
            product.good_comment_percentage = int(product.good_comment_percentage.split("%")[0])/100
            print(product.good_comment_percentage)
            # 将好评数转换成数字
            comment_count = product.comment_count
            if (comment_count.find("万") != -1):
                comment_count = comment_count.split("万")
                comment_count = float(comment_count[0])*10000
                product.comment_count = comment_count
            else:
                if(comment_count.find("+") !=-1):
                    comment_count = comment_count.split("+")[0]
                    product.comment_count = comment_count
            product.get_time = Now()
            product.save()
        except:
            pass
            continue


