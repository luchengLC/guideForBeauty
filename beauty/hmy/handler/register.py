import pymysql
from django.http import JsonResponse
import hashlib
def handle_register(request):
    user_info={}
    if request.method=='POST':
        user_info['user']=request.POST.get("username",'')
        user_info['pwd']=request.POST.get("password",'')
        user_info['name']=request.POST.get('name','')
        user_info['email']=request.POST.get('email','')
        data=check_register(user_info)
        if data['error_code']==0:
            request.session['username']=user_info['user']
    return JsonResponse(data, safe=False)

def check_register(user_info):
    conn = pymysql.connect(host="39.108.185.66", port=3306, user='root', password='1234', db='beautyGirls_database',
                           charset='utf8mb4')
    cur = conn.cursor()
    select_sql = "select * from users  where username='" + str(user_info['user']) + "'"
    data={}
    try:
        cur.execute(select_sql)
        res = cur.fetchone()
        if  res is not None:
            data['error_code'] = 1
            data['msg'] = '此手机号已被注册！'
            return data
    except Exception as err:
        cur.close()
        conn.commit()

    try:
        cur=conn.cursor()
        m=hashlib.md5()
        m.update(user_info['pwd'].encode('utf-8'))
        user_info['pwd']=m.hexdigest()
        print(user_info)
        insert_sql="insert into users values('"+user_info['user']+"','"+user_info['pwd']+"','"+user_info['name']+"','"+user_info['email']+"')"
        print(insert_sql)
        cur.execute(insert_sql)
        cur.close()
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)
        data['error_code'] = 1
        data['msg'] = '信息录入异常！'
        return data

    data['error_code']=0
    data['msg']='注册成功！'
    data['username'] = user_info['name']
    return data


# user_info={}
# user_info['user']='13411989234'
# user_info['pwd']='123456'
# user_info['name']='nicole'
# user_info['email']='14nicole'
# print(check_register(user_info))

