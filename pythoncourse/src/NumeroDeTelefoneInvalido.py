class NumeroTelefoneInvalido(Exception):
    def __init__(self, numero, mensagem="Numero de telefone invalido"):
        self._numero = numero
        self._mensagem = mensagem

    def _get_numero(self):
        return self._numero

    def _set_numero(self, numero):
        self._numero = numero

    def _get_mensagem(self):
        return self._mensagem

    def _set_mensagem(self, mensagem):
        self._mensagem = mensagem