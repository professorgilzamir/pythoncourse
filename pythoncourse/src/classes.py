class LocalizacaoGeografica:
	def __init__(self, latitude, longitude):
		self._latidude = latitude
		self._longitude = longitude

	def magicGet(self, atrib):
		if atrib == 'latitude':
			return self._latidude
		elif atrib == 'longitude':
			return self._longitude
		else:
			return None

	def magicSet(self, atrib, value):
		if atrib == 'latitude':
			self._latitude = value
		elif atrib == 'longitude':
			self._longitude = value

class UnidadeDeSaude(LocalizacaoGeografica):
	def __init__(self, latitude, longitude, codCid, codCnes, dscEstFisAmb, dscAdapFisldo, sitEquipamentos, endereco):
		super().__init__(latitude, longitude)
		self._dscEstFisAmb = dscEstFisAmb
		self._dscAdapFisldo = dscAdapFisldo
		self._sitEquipamentos = sitEquipamentos
		self._endereco = endereco
		self._codCid = codCid
		self._codCnes = codCnes

	def magicGet(self, atrib):
		if atrib == 'latitude':
			return self._latitude
		elif atrib == 'longitude':
			return self._longitude
		elif atrib == 'codCid':
			return self._codCid
		elif atrib == 'codCnes':
			return self._codCnes
		elif atrib == 'dscEstFisAmb':
			return self._dscEstFisAmb
		elif atrib == 'dscAdapFisldo':
			return self._dscAdapFisldo
		elif atrib == 'sitEquipamentos':
			return self._sitEquipamentos
		elif atrib == 'endereco':
			return self._endereco
		else:
			return None

	def magicSet(self, atrib, value):
		if atrib == 'latitude':
			self._latitude = value
		elif atrib == 'longitude':
			self._longitude = value
		elif atrib == 'codCid':
			self._codCid = value
		elif atrib == 'codCnes':
			self._codCnes = value
		elif atrib == 'dscEstFisAmb':
			self._dscEstFisAmb = value
		elif atrib == 'dscAdapFisldo':
			self._dscAdapFisldo = value
		elif atrib == 'sitEquipamentos':
			self._sitEquipamentos = value
		elif atrib == 'endereco':
			self._endereco = value


class UnidadeDeSaude(LocalizacaoGeografica):
	def __init__(self, latitude, longitude, codCid, codCnes, dscEstFisAmb, dscAdapFisldo, sitEquipamentos, endereco):
		super().__init__(latitude, longitude)
		self._codCid = codCid
		self._codCnes = codCnes
		self._dscEstFisAmb = dscEstFisAmb
		self._dscAdapFisldo = dscAdapFisldo
		self._sitEquipamentos = sitEquipamentos
		self._endereco = endereco

	def magicGet(self, atrib):
		if atrib == 'latitude':
			return self._latitude
		elif atrib == 'longitude':
			return self._longitude
		elif atrib == 'codCid':
			return self._codCid
		elif atrib == 'codCnes':
			return self._codCnes
		elif atrib == 'dscEstFisAmb':
			return self._dscEstFisAmb
		elif atrib == 'dscAdapFisldo':
			return self._dscAdapFisldo
		elif atrib == 'sitEquipamentos':
			return self._sitEquipamentos
		elif atrib == 'endereco':
			return self._endereco
		else:
			return None

	def magicSet(self, atrib, value):
		if atrib == 'latitude':
			self._latitude = value
		elif atrib == 'longitude':
			self._longitude = value
		elif atrib == 'codCid':
			self._codCid = value
		elif atrib == 'codCnes':
			self._codCnes = value
		elif atrib == 'dscEstFisAmb':
			self._dscEstFisAmb = value
		elif atrib == 'dscAdapFisldo':
			self._dscAdapFisldo = value
		elif atrib == 'sitEquipamentos':
			self._sitEquipamentos = value
		elif atrib == 'endereco':
			self._endereco = value

class NumeroTelefoneInvalido(Exception):
	def __init__(self, numero, mensagem = "Numero de telefone invalido"):
		self._numero = numero
		self._mensagem = mensagem

	def magicGet(self, atrib):
		if atrib == 'numero':
			return self._numero	
		elif atrib == 'mensagem':
			return self._mensagem
		else:
			return None

	def magicSet(self, atrib, value):
		if atrib == 'numero'
			self._numero = value
		elif atrib == 'mensagem'
			self._mensagem = value
