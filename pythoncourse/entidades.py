class Endereco:
	def __init__(self, logradouro, bairo, cidade, telefone):
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

	def getLogradouro():
		return self.logradouro
	
	def getBairro():
		return self.bairro

	def getCidade():
		return self.cidade

	def getTelefone():
		return self.telefone


class UnidadeDeSaude:
	
	def __init__(self, codigo, dscEstFisAmb, dscAdapFisIdo, sitEquipamentos):
		self.codigo = codigo
		self.dscEstFisAmb = dscEstFisAmb
		self.codigo = codigo
		self.codigo = codigo
		
	def setCodigo(self, codigo):
		self.codigo = codigo

	def setSitEquipamentos(self, sitEquipamentos):
		self.sitEquipamentos = sitEquipamentos
	
	def setDscAdapFisIdo(self, dscAdapFisIdo):
		self.dscAdapFisIdo = dscAdapFisIdo

	def setDscEstFisAmb(self, dscEstFisAmb):
		self.dscEstFisAmb = dscEstFisAmb

	def getCodigo():
		return self.codigo

	def getSitEquipamentos():
		return self.sitEquipamentos
	
	def getDscAdapFisIdo():
		return self.dscAdapFisIdo

	def getDscEstFisAmb():
    return self.dscEstFisAmb

class LocalizacaoGeografica:
	
	def __init__(self, codigo, dscEstFisAmb, dscAdapFisIdo, sitEquipamentos):
		self.logradouro = logradouro
		
	def setCodigo(self, codigo):
		self.codigo = codigo

	def setSitEquipamentos(self, sitEquipamentos):
		self.sitEquipamentos = sitEquipamentos
	
	def setDscAdapFisIdo(self, dscAdapFisIdo):
		self.dscAdapFisIdo = dscAdapFisIdo

	def setDscEstFisAmb(self, dscEstFisAmb):
		self.dscEstFisAmb = dscEstFisAmb

	def getCodigo():
		return self.codigo

	def getSitEquipamentos():
		return self.sitEquipamentos
	
	def getDscAdapFisIdo():
		return self.dscAdapFisIdo

	def getDscEstFisAmb():
    return self.dscEstFisAmb

