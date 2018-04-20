#encoding=UTF-8
import pymysql
import datetime

class save_mysql:
	def __init__(self):
		self.user = "root"
		#self.passwd = "root" #"1234"
		self.passwd = "1234"  # "1234"
		#self.host = "localhost" #"39.108.185.66"
		self.host = "39.108.185.66"
		#self.database = "beautyGrils_database" #"beautyGirls_database"
		self.database ="beautyGirls_database"
		db = None
	
	def get_connection(self):
		return pymysql.connect(self.host,self.user,self.passwd,self.database,charset="utf8")
	
	def save_product(self,sql):
		db = self.get_connection()
		#localtime = time.asctime(time.localtime(time.time()))
		#print(pro.color)
		cursor = db.cursor()		
		cursor.execute(sql)
		#print("OK")
		db.commit()

	def update_product(self,sql):
		db = self.get_connection()
		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()

#查询数据库
	def get_product_data(self,sql):
		result =[]
		db = self.get_connection()
		cursor=db.cursor()
		cursor.execute(sql)
		#获取返回的结果记录
		rows = cursor.fetchall()
		print("rows type: ",type(rows) )
		for row in rows:
			print("row type: ",type(row))
			print("row: ",row)
			result.append(row)
			description = row[11]
			price = row[10]
			comment_count = row[16]
			comment_increment = row[17]
			print("description= "+description,"  price="+str(price)," comment_count="+str(comment_count)," comment_increment="+str(comment_increment))
		return result


		
		
	
		