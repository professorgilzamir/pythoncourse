import pymysql

def createConnection(forcenew=False):
	return pymysql.connect("localhost", "root","","socialink")

