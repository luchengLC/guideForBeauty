import requests
from bs4 import BeautifulSoup
import re
import json
from TianMaoMeiZhuang import TianMaoMeiZhuang
from TianMaoMall import  TianMaoMall
import threading

class TianMaoSpider:
	def __init__(self):
		self.headers={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
		
	#商品详情页建立链接
	def connectProduct(self,url,id):
		address = url+id
		try:
			pageHtml=requests.get(address,headers=self.headers).text
			pageSoup=BeautifulSoup(pageHtml,"lxml")
			return pageSoup
		except requests.exceptions.ConnectTimeout:
			#连接超时
			return None
		except requests.exceptions.ConnectionError:
			#无法建立链接
			return None
		return None
	
	#从页面中读取每个商品的id
	def getIds(self,page):
		#q="%B4%BD%B2%CA"
		q="%B4%BD%B2%CA+%B4%BD%C3%DB"
		#url="https://list.tmall.com/search_product.htm?q={}&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton&s={}".format(q,page)
		url="https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.11.b9e54ff6k8I8ml&cat=50031573&s={}&sort=s&style=g&active=2&industryCatId=50031573&theme=344&smAreaId=440500&type=pc#J_Filter".format(page)
		header={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
		#'cookie':"_med=dw:1366&dh:768&pw:1366&ph:768&ist:0; x=__ll%3D-1%26_ato%3D0; cna=PfJcEe0OL2cCAXkLEg6BD9Z8; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; hng=CN%7Czh-CN%7CCNY%7C156; enc=zQDXVm6q6VcmBm%2BdpRa4w3VvPAW0RST%2BNVjt26fyPrEX7BrdPzjIjHWd2tQPYSe2e0SyxGqDGCzwfYzR0%2B5HIw%3D%3D; sm4=440500; cq=ccp%3D1; _m_h5_tk=957f59dda77069461b04d918f3ea487f_1523451079006; _m_h5_tk_enc=e54b45da8dba24b50f2dc92baca03c13; t=37be738ed9cbc0b02db323167c9c98da; uc3=nk2=qUryzZZwAX4I2pw%3D&id2=Uone9meuUHQlNA%3D%3D&vt3=F8dBz4PAjdw%2Fm1afKr4%3D&lg2=URm48syIIVrSKA%3D%3D; tracknick=%5Cu5B88%5Cu5019%5Cu661F%5Cu7A7A526; lid=%E5%AE%88%E5%80%99%E6%98%9F%E7%A9%BA526; lgc=%5Cu5B88%5Cu5019%5Cu661F%5Cu7A7A526; _tb_token_=d8367e3e6e61; cookie2=18d8457284cd68d9a3a68ba92ec812ed; swfstore=142078; res=scroll%3A1349*5879-client%3A1349*637-offset%3A1349*5879-screen%3A1366*768; pnm_cku822=098%23E1hv%2BvvUvbpvUpCkvvvvvjiPPFMwAjDRR2zO1jEUPmPv0jEbPFLZ6jDvP2M9QjlWPuwCvvpvvUmm2QhvCPMMvvvCvpvVvvpvvhCvmphvLCB9Zvvj8txrgj7JhLEaAwexKfwBfvDrAjc6%2BulgEfFnQfV6Re38k8oQD46wjomxfw3lHsyDZtcEsXZZDVQEfw3lYb8rJm7guf0Dn1otvpvIvvvvvhCvvvvvvUUdphvUYpvv9krvpvQvvvmm86CvmVWvvUUdphvUOTyCvv9vvUv13jJN0OyCvvOUvvVvayWtvpvhvvvvvv%3D%3D; isg=BLOzYpa27YjYVKFDJorEaxgoQrcdQGwfTqmtJWVQDVIJZNMG7LjX-hH2GpSKRJ-i"
		}
		html=requests.get(url,headers=header).text
		#print(html)
		soup = BeautifulSoup(html,"html5lib")
		urls = soup.find_all("div",attrs={"class":"productTitle productTitle-spu"})
		results=set()
		for u in urls:
			for a in u.find_all('a'):
				url=a['href']
				#print(url)
				ids = re.search("id=[0-9]*",url).span()
				begin = ids[0]  #匹配的左下标
				end=ids[1] #匹配的右下标
				ids = url[begin:end][3:]
				results.add(ids)
		return results
		
	def startCrawl(self,page):
		ids=self.getIds(page)
		#ids=["35246198378"] #天猫美妆
		#ids=["520828694464"] #天猫超市
		print("page:{} ids:{}".format(page,ids))
		for id in ids:
			print("正在访问：",url+id)
			soup = self.connectProduct(url,id)
			if soup is not None :
				logo = soup.find("span",class_="mlogo").find('a')['title']
				if  "天猫美妆" in logo:
					#referer="https://list.tmall.com/search_product.htm?q=%B4%BD%B2%CA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton&s={}".format(page)
					referer="https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.11.b9e54ff6k8I8ml&cat=50031573&s={}&sort=s&style=g&active=2&industryCatId=50031573&theme=344&smAreaId=440500&type=pc".format(page)
					tmmz = TianMaoMeiZhuang(url,id,soup,referer)
					print("正在访问天猫美妆：",url+id)
					t = threading.Thread(target=tmmz.main)
					t.start()
					#tmmz.main()
				elif "天猫超市" in logo:
					#referer="https://list.tmall.com/search_product.htm?q=%B4%BD%B2%CA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton&s={}".format(page)
					referer="https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.11.b9e54ff6k8I8ml&cat=50031573&s={}&sort=s&style=g&active=2&industryCatId=50031573&theme=344&smAreaId=440500&type=pc".format(page)
					tmmz = TianMaoMall(url,id,soup,referer)
					print("正在访问天猫超市：",url+id)
					t = threading.Thread(target=tmmz.main)
					t.start()

if __name__=="__main__":
	url="https://detail.tmall.com/item.htm?id="  #单个商品详情的url
	#id = "3107804524915" #天猫美妆的商品
	#id="520828694464"
	#id= "529085064706"
	#id="561560180557"
	page = 30
	pages = [x*30 for x in range(8,17)]
	spider=TianMaoSpider()
	for page in pages:
		#spider.startCrawl(page)
		t = threading.Thread(target=spider.startCrawl,args=(page,))
		t.start()