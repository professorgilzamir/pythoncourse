from src.LocalizacaoGeografica import LocalizacaoGeografica

class UnidadeDeSaude (LocalizacaoGeografica):

  def __init__(self, latitude, longitude, codCid, codCnes, dscEstFisAmb, dscAdapFisldo, sitEquipamentos, endereco):
    super().__init__(latitude, longitude)
    self._codCid = codCid
    self._codCnes = codCnes
    self._dscEstFisAmb = dscEstFisAmb
    self._dscAdapFisldo = dscAdapFisldo
    self._sitEquipamentos = sitEquipamentos
    self._endereco = endereco

  def getLatitude (self):
    return self._latitude

  def getLongitude (self):
    return self._longitude

  def getCodCid (self):
    return self._codCid

  def getCodCnes (self):
    return self._codCnes

  def getDscEstFisAmb (self):
    return self._dscEstFisAmb

  def getDscAdapFisldo (self):
    return self._dscAdapFisldo

  def getSitEquipamentos (self):
    return self._sitEquipamentos

  def getEndereco (self):
    return self._endereco

  def setLatitude (self, value):
    self._latitude = value

  def setLongitude (self, value):
    self._longitude = value

  def setCodCid (self, value):
    self._codCid = value

  def setCodCnes (self, value):
    self._codCnes = value

  def setDscEstFisAmb (self, value):
    self._dscEstFisAmb = value

  def setDscAdapFisldo (self, value):
    self._dscAdapFisldo = value

  def setSitEquipamentos (self, value):
    self._sitEquipamentos = value

  def setEndereco (self, value):
    self._endereco = value