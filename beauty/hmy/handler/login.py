import pymysql
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
import hashlib

def handle_login(request):
    if request.method=='POST':
        user=request.POST.get("username",'')
        pwd=request.POST.get("password",'')
        data=check_login(user,pwd)
        if data['error_code']==0:
            request.session['username']=user
            data['username']=user
    return render(request,'',{'data':data})


def check_login(user,pwd):
    data={}
    m = hashlib.md5()
    m.update(pwd.encode('utf-8'))
    pwd = m.hexdigest()
    try:
        conn = pymysql.connect(host="39.108.185.66", port=3306, user='root', password='1234', db='beautyGirls_database',
                               charset='utf8mb4')
        cur = conn.cursor()
        select_sql="select * from users  where username='"+str(user)+"'"
        cur.execute(select_sql)
        res=cur.fetchone()
        cur.close()
        conn.commit()
        conn.close()
        if res is None:
            data['error_code']='1'
            data['msg']='此用户不存在！'
            return data
        elif pwd!=res[1]:
            data['error_code']='1'
            data['msg']='密码错误！'
            return data
    except Exception as err:
        print(err)
    data['error_code']='0'
    data['msg']='success'
    print(data)
    return data

print(check_login('114','12'))

