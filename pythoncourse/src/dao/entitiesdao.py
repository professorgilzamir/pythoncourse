from dao.db import *
from model import LocalizacaoGeografica

class LocalizacaoGeograficaDAO:
	def __init__(self):
		self.connection = createConnection()

	def create(self, locGeo):
		cursor = self.connection.cursor()		
		sql = 'insert into LocalizacaoGeografica(latitude, longitude) values (%s, %s)' % (locGeo.latitude, locGeo.longitude)
		l = self.cursor.execute(sql)
		self.connection.commit()
		cursor.close()

	def search(self, longitude, latitude):
		pass

	def delete(self, idLocGeo):
		pass

	def update(self, locGeo):
		pass

	def searchAll(self):
		cursor = self.connection.cursor()
		sql = "select * from LocalizacaoGeografica"
		cursor.execute(sql)
		result = []
		for row in cursor.fetchall():
			result.append(LocalizacaoGeografica(row[1], row[2]))
		cursor.close()
		return result