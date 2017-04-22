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