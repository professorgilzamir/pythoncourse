class Endereco():
    def __init__(self, logadouro, bairro, cidade, telefone):
        self._logadouro = logadouro
        self._bairro = bairro
        self._cidade = cidade
        self._telefone = telefone

    def _get_logadouro(self):
        return self._logadouro

    def _set_logadouro(self, logadouro):
        self._logadouro = logadouro

    def _get_bairro(self):
        return self._bairro

    def _set_bairro(self, bairro):
        self._bairro = bairro

    def _get_cidade(self):
        return self._cidade

    def _set_cidade(self, cidade):
        self._cidade = cidade

    def _get_telefone(self):
        return self._telefone

    def _set_telefone(self, telefone):
        self._telefone = telefone
