class LocalizacaoGeografica:
	def __init__(self, latitude, longitude):
		self._latidude = latitude
		self._longitude = longitude

	def mget(self, prop):
		return self.__dict__[prop]
	
	def mset(self, prop, value):
		self.__dict__[prop] = value
		
		
		
		
class Endereco:
	def __init__(self, logradouro, bairro, cidade, telefone):
		self._logradouro = logradouro
		self._bairro = bairro
		self._cidade = cidade
		self._telefone = telefone
	
	def mget(self, prop):
		return self.__dict__[prop]
	
	def mset(self, prop, value):
		self.__dict__[prop] = value
	
	def validarTelefone(self, telefone)
		if ((len(self._telefone) == 12 or len(self._telefone) == 13) and (self._telefone[0] == '(' and self._telefone[3] == ')'):
			return True
		else:
			return False
		

class UnidadeDeSaude(LocalizacaoGeografica):
	def __init__(self, latitude, longitude, codCid, codCnes, dscEstFisAmb, dscAdapFisldo, sitEquipamentos, endereco):
		super().__init__(latitude, longitude)
		self._codCid = codCid
		self._codCnes = codCnes
		self._dscEstFisAmb = dscEstFisAmb
		self._dscAdapFisldo = dscAdapFisldo
		self._sitEquipamentos = sitEquipamentos
		self._endereco = endereco

	def mget(self, prop):
		return self.__dict__[prop]
	
	def mset(self, prop, value):
		self.__dict__[prop] = value
	
class NumeroTelefoneInvalido(Exception):
	def __init__(self, numero, mensagem = "Numero de telefone invalido"):
		self._numero = numero
		self._mensagem = mensagem

	def mget(self, prop):
		return self.__dict__[prop]
	
	def mset(self, prop, value):
		self.__dict__[prop] = value
