import re
import time
import requests
#from lxml import etree
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd
import csv
#from MySQLLoader import MySQLLoader
#python3 -m pip install requests
#python3 -m pip install BeautifulSoup4
#python3 -m pip install lxml 
#python3 -m pip install UserAgent
#python3 -m pip install fake-useragent

class DangDang:

	def __init__(self):

		self.url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1"

		self.ua = UserAgent(verify_ssl=False)

		self.headers={

		     "Cookie": "s_ViewType=10; _lxsdk_cuid=167ca93£5c2c8-0c73da94a9dd08-68151275-1fa400-167ca93£5c2c8;_lxsdk=167ca93f5c2c8-0c73da94a9dd08-68151275-1f400-167a93f5c2c8;_hc.v=232064fb-c9a6-d4e0-cc6b-d6303e5eed9b.1545291954;cy=16;cye=wuhan;td_cookie=686763714;_lxsdk_s=%7C%7CNaN",
		     "User-Agent" : self.ua.random #获取随机的User-Agent
		}

		self.dic = {} # class-digit字典

	    #self.to_writer

	def get_page(self, page):

		self.rand_list = []

		self.name_list = []

		self.comment_list = []

		self.publish_date_list = []

		self.publisher_list = []

		self.price_discount_list = []

		self.price_original_list = []

		url = '%s%s'%(self.url,page)

		res = requests.get(url,headers=self.headers)
		#print(res.text)
		#self.to_writer('TXT_COMMA3.txt',res.text)

		soup = BeautifulSoup(res.text, 'html.parser')
   
        #<ul class="bang_list clearfix bang_list_mode">
		tag = soup.find('ul','bang_list clearfix bang_list_mode')


		li_list = tag.find_all('li')
		print(li_list[1])

		for item in li_list:

			#排名
			rank = item.find('div', 'list_num')
			print(rank.string)
			self.rand_list.append(rank.string.replace('.',''))

			#书名
			name = item.find('div', 'name')
			print(name.a['title'])
			self.name_list.append(name.a['title'])

			#评论
			comment = item.find('div', 'star')
			print(comment.a.string)
			self.comment_list.append(comment.a.string.replace('条评论',''))

			#出版日期
			publish = item.find_all('div','publisher_info')
			print(publish[1].span.string)
			self.publish_date_list.append(publish[1].span.string)

			#出版社
			print(publish[1].a.string)
			self.publisher_list.append(publish[1].a.string)

			#折扣价
			price_discount = item.find('span','price_n')
			print(price_discount.string)
			self.price_discount_list.append(price_discount.string.replace('¥',''))

			#原价
			price_original = item.find('span','price_r')
			print(price_original.string)
			self.price_original_list.append(price_original.string.replace('¥',''))

		#def to_db(self, filename, tablename, dbinfo):

			#loader = MySQLLoader(filename,'csv',tablename,dbinfo)

			#loader.load()

	def save_to_csv(self, filename):

		df = pd.DataFrame({
				'rank': pd.Series(self.rand_list),
				'name': pd.Series(self.name_list),
				'comment': pd.Series(self.comment_list),
				'publish_date': pd.Series(self.publish_date_list),
				'publiser': pd.Series(self.publisher_list),
				'price_discount': pd.Series(self.price_discount_list),
				'price_original': pd.Series(self.price_original_list)
				})

		df.to_csv(filename,index = False,encoding='utf_8_sig')



	def to_writer(filename,context):

			with open(filename,newline='') as csvfile:

				htmlwriter = csv.writer(csvfile)

				htmlwriter.writerow(context)

				csvfile.close()


if __name__ == '__main__':

	dp = DangDang()

	#传入页码
	dp.get_page(1)

	#存为csv文件
	dp.save_to_csv('chap6.csv')

	#写入数据库
	db_info = {

	     'host': 'MySQl数据库服务器地址',
	     'port': 3306,
	     'user': '数据库用户名',
	     'password': '数据库密码',
	     'database': '数据库名称'
	}

	#dp.to_db('chap6.csv','tb_dd_rank',db_info)















