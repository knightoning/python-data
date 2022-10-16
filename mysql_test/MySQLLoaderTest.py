from MySQLLoader import MySQLLoader

db_info = {
	
	'user' : '数据库用户名',

	'password' : '数据库密码',

	'host' : '数据库服务器地址',

	'database' : '数据库名称'

	'port' : 3306
}

loader = MySQLLoader('tmp001.tbl','table','my_table',db_info)

loader.set_sep(' ')

loader.load()

print('导入成功')