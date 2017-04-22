class Endereco:
    def __init__(self, logradouro, bairro, cidade, telefone):
        self._logradouro = logradouro
        self._bairro = bairro
        self._cidade = cidade
        self._telefone = telefone
    
    def magicGet(self, atrib):
        if atrib == 'logradouro':
            return self._logradouro
        elif atrib == 'bairro':
            return self._bairro
        elif atrib == 'cidade':
            return self._cidade
        elif atrib == 'telefone':
            return self._telefone
        else:
            return None
        
    def magicSet(self, atrib, value):
        if atrib == 'logradouro':
            self._logradouro = value
        elif atrib == 'bairro':
            self._bairro = value
        elif atrib == 'cidade':
            self._cidade = value
        elif atrib == 'telefone':
            self._telefone = value