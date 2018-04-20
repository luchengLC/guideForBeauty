import requests
from bs4 import BeautifulSoup
import re
import json
from SQL import save_mysql

class TianMaoMeiZhuang:
	def __init__(self,url,id,soup,referer):
		self.platform="淘宝"
		self.id=id
		self.address=url+id
		self.headers={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
			"referer":referer}
			
		self.pageSoup = soup
		self.description=None
		self.sql = save_mysql()
		
	#获取标题
	def __getDescription(self):
		if self.pageSoup is not None:
			title=self.pageSoup.find("div",class_="tb-detail-hd").find("h1").string.strip()
			return title
		else:
			print("获取标题出错了，soup不应该为空")
			return None
	
	#获取商品图片链接
	def __getImages(self):
		if self.pageSoup is not None:
			results=[]
			imgs=self.pageSoup.find("ul",attrs={"id":"J_UlThumb"}).find_all("li")
			num=0
			for img in imgs:
				results.append("https:"+img.find('img')['src'])
			while num < 5:
				results.append("null")
				num+=1
			return results
		else:
			print("获取图片出错了，soup不应该为空")
			return None
	
	#获取产品名称、颜色分类、保质期、功效、适合肤质、产地
	def __getProductDetail(self):
		if self.pageSoup is not None:
			params=["产品名称","颜色分类","保质期","功效","适合肤质","产地"]
			results={}
			for param in params :
				results[param]="null"
			try:
				attributes = self.pageSoup.find('ul',attrs={"id":"J_AttrUL"}).find_all("li")
				for attr in attributes:
					if '\xa0' in attr:
						attr=attr.replace(u'\xa0',u'')
					attr = attr.string.strip()
					for i in range(len(params)):
						strIndex = re.search(params[i],attr)
						if strIndex is not None:
							end = strIndex.span()[1]  #因可能出现“化妆品保质期：36个月”这种情况，所以需要知道“保质期”的最后匹配位置，然后截取，才能得到干净的字段
							#results[ params[i] ] = attr[len(params[i])+1:]
							results[ params[i] ] = attr[end+1:]
							del params[i]
							break
			except AttributeError as e:
				pass
			return results
		else :
			return None
	
	#获取每一种型号的价格
	def __getPrices(self):
		url="https://mdskip.taobao.com/core/initItemDetail.htm?&itemId={}".format(self.id)
		header={
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
			'Referer':"https://detail.tmall.com/item.htm?id={}".format(self.id)  #这里应对阿里云服务器的反爬虫策略
		}
		html=requests.get(url,headers=header).text
		#print(html)
		try:
			datas=json.loads(html.strip())
		except(JSONDecodeError,Exception):
			print("JSONDecodeError")
			return None
		try :
			prices = datas['defaultModel']['itemPriceResultDO']['priceInfo']
			keys = list(prices.keys())
			result = None
			if keys is None:
				raise Exception('NullException')
			key = keys[0]
			results=prices[key]["promotionList"][0]['price']
			return results
		except (KeyError,Exception):
			prices = datas['defaultModel']['itemPriceResultDO']['priceInfo']
			keys = list(prices.keys())
			results=None
			key=keys[0]
			results=prices[key]['price']
			return results
	
			
	#获取商品评价总数和好评率
	def __getComments(self):
		comments={}
		url="https://dsr-rate.tmall.com/list_dsr_info.htm?itemId={}".format(self.id)
		html=requests.get(url).text
		tmp = re.search("\(.*\)",html).span()
		html = html[tmp[0]:tmp[1]][1:-1]
		datas=json.loads(html)
		comments['评论总数']=datas['dsr']['rateTotal']
		comments['好评率'] = round(float(datas['dsr']['gradeAvg'])/5*100,2)
		print(comments)
		return comments
		
	def __saveInDataBase(self,images,address,price,description,number,name,produce_address,comment_count,good_for_who,expiration_date,color,result_effectiveness,good_comment_percentage):
		table = "product_lipstick"
		sqlString = "insert into "+table+" ("+"first_category,second_category,third_category,"+"img1_address,img2_address,img3_address,img4_address,img5_address,"+"address,price,description,number,name,produce_address,"+"comment_count,good_for_who,expiration_date,color,"+"result_effectiveness,category,good_comment_percentage,who_handly,platform"+") values('美妆/个人护理','彩妆','唇彩','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','唇彩','{}','林鹏珊','天猫')".format(images[0],images[1],images[2],images[3],images[4],address,price,description,number,name,produce_address,comment_count,good_for_who,expiration_date,color,result_effectiveness,good_comment_percentage)
		self.sql.save_product(sqlString)
		
	def main(self):
		images=self.__getImages()
		address = self.address
		price=float(self.__getPrices())
		description=self.__getDescription()
		number = self.id
		detail=self.__getProductDetail()
		name = detail["产品名称"]
		produce_address = detail["产地"]
		good_for_who = detail["适合肤质"]
		expiration_date = detail["保质期"]
		color = detail["颜色分类"]
		result_effectiveness = detail["功效"]
		comments=self.__getComments()
		comment_count = comments['评论总数']
		good_comment_percentage = comments["好评率"]
		
		self.__saveInDataBase(images,address,price,description,number,name,produce_address,comment_count,good_for_who,expiration_date,color,result_effectiveness,good_comment_percentage)
		'''
		print(description,end='\n\n')
		print(images,end='\n\n')
		print(detail,end='\n\n')
		print(price,end='\n\n')
		print(comments,end='\n\n')
		'''
		
