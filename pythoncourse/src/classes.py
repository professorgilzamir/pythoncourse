class UnidadeDeSaude():
	def __init__(self, latitude, longitude, codCid, codCnes, dscEstFisAmb, dscAdapFisldo, sitEquipamentos, endereco):
		super().__init__(latitude, longitude)
		self._codCid = codCid
		self._codCnes = codCnes
		self._dscEstFisAmb = dscEstFisAmb
		self._dscAdapFisldo = dscAdapFisldo
		self._sitEquipamentos = sitEquipamentos
		self._endereco = endereco

	def setLatitude(self, latitude):
		self.latitude = latitude

	def setLongitude(self, longitude):
		self.longitude = longitude

	def setCodCid(self, codCid):
		self.codCid = codCid

	def setCodCnes(self, codCnes):
		self.codCnes = codCnes

	def setDscEstFisAmb(self, dscEstFisAmb):
		self.dscEstFisAmb = dscEstFisAmb

	def setDscAdapFisldo(self, dscAdapFisldo):
		self.dscAdapFisldo = dscAdapFisldo

	def setSitEquipamentos(self, sitEquipamentos):
		self.sitEquipamentos = sitEquipamentos

	def setEndereco(self, endereco):
		self.endereco = endereco


	def getLatitude(self, latitude):
		return self.latitude

	def getLongitude(self, longitude):
		return self.longitude

	def getCodCid(self, codCid):
		return self.codCid

	def getCodCnes(self, codCnes):
		return self.codCnes

	def getDscEstFisAmb(self, dscEstFisAmb):
		return self.dscEstFisAmb

	def getDscAdapFisldo(self, dscAdapFisldo):
		return self.dscAdapFisldo

	def getSitEquipamentos(self, sitEquipamentos):
		return self.sitEquipamentos

	def getEndereco(self, endereco):
		return self.endereco

class LocalizacaoGeografica():
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def setLatitude(self, latitude):
		self.latitude = latitude

	def setLongitude(self, longitude):
		self.longitude = longitude

	def getLatitude(self, latitude):
		return self.latitude

	def getLongitude(self, longitude):
		return self.longitude

class Endereco():
	def __init__(self, logradouro, bairro, cidade, telefone):
		self.logradouro = logradouro
		self.bairro = bairro
		self.cidade = cidade
		self.telefone = telefone

	def setLogradouro(self, logradouro):
		self.logradouro = logradouro

	def setBairro(self, bairro):
		self.bairro = bairro

	def setCidade(self, cidade):
		self.cidade = cidade

	def setTelefone(self, telefone):
		self.telefone = telefone

	def getLogradouro(self, logradouro):
		return self.logradouro

	def getBairro(self, bairro):
		return self.bairro

	def getCidade(self, cidade):
		return self.cidade

	def getTelefone(self, telefone):
		return self.telefone
