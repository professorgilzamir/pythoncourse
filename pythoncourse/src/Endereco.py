class Endereco:

  def __init__ (self, logradouro, bairro, cidade, telefone):
    self._logradouro = logradouro
    self._bairro = bairro
    self._cidade = cidade
    self._telefone = telefone

  def getLogradouro (self):
    return self._logradouro

  def getBairro (self):
    return self._bairro

  def getCidade (self):
    return self._cidade

  def getTelefone (self):
    return self._telefone

  def setLogradouro (self, value):
    self._logradouro = value

  def setBairro (self, value):
    self._bairro = value

  def setCidade (self, value):
    self._cidade = value

  def setTelefone (self, value):
    self._telefone = value