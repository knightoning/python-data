import pandas as pd
from sqlalchemy import create_engine

class MySQLLoader:

	def __int__(self,file,file_type,table_name,db_info):

		self.__file = file

		self.__type = file_type

		self.__table_name = table_name

		self.__db_info = db_info

		self.__sep = ','

		self.__data = []

		self.__engine = []

	def set_db_info(self,db_info):

		self.__db_info = db_info

	def set_sep(self,sep):

		self.__sep = sep

	def load(self):

		self.conn()

		if self.__type == 'csv':

			self.load_csv()

			self.save()

		elif self.__type == 'excel':

			self.load_excel()

			self.save()

		elif self.__type == 'table':

			self.load_table()

			self.save()

		elif selt.__type == 'fwf':

			self.load_fwf()

			self.save()

		else:
			print('type is not valid.')

	def load_csv(self):

		self.__data = pd.read_csv(self.__file)

    def load_excel(self):

    	self.__data = pd.read_excel(self.__file)

    def load_table(self):

    	self.__data = pd.read_csv(self.__file,self.__sep)

    def load_fwf(self):

    	self.__data = pd.read_fwf(self.__file)

    def save(self):

    	pd.io.sql.to_sql(self.__data, self.__table_name, 
    		con=sefl.__engine, index=False, if_exists='replace')
    
    def conn(self):

    	self.__engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % self.__db_info, encoding='utf-8')









