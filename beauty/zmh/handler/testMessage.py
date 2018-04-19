#!/usr/bin/python 
# -*- coding:utf-8 -*-

from beauty.zmh.dysms_python.dysms_python.demo_sms_send import send_sms
import uuid

def send_test():
    __business_id = uuid.uuid1()
    params = u'{"productName":"曼秀雷敦唇膏玫瑰色 4g"}'
    print(send_sms(__business_id, "13411989237", "美妆商品导购系统", "SMS_130925712", params))

if __name__ == "__main__":
    send_test()