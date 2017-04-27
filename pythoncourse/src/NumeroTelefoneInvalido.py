class NumeroTelefoneInvalido(Exception):

  def __init__(self, numero, mensagem = "Numero de telefone invalido"):
    self._numero = numero
    self._mensagem = mensagem

  def getNumero (self):
    return self._numero

  def getMensagem (self):
    return self._mensagem

  def setNumero (self, value):
    self._numero = value

  def setMensagem (self, value):
    self._mensagem = value