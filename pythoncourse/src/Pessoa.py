class Pessoa:
	def __init__(self):
		self.nome = "Luis"

	def mget(self, prop):
		return self.__dict__[prop]
	
	def mset(self, prop, value):
		self.__dict__[prop] = value								

