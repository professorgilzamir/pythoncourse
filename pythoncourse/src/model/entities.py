class LocalizacaoGeografica():
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude

    def _get_latitude(self):
        return self._latitude

    def _set_latitude(self, latitude):
        self._latitude = latitude

    def _get_longitude(self):
        return self._longitude

    def _set_longitude(self, longitude):
        self._longitude = longitude

    def dist(self, objLocGeo):
    	pass

    latitude = property(_get_latitude, _set_latitude)
    longitude = property(_get_longitude, _set_longitude)

class UnidadeDeSaude(LocalizacaoGeografica):
    def __init__(self, latitude, longitude, codCidade, cnes, nome, ender, dscEstFisAmb, dscAdapFisdo, sitEquipamentos, dscMedicamentos):
        super().__init__(latitude, longitude)
        self._dscEstFisAmb = dscEstFisAmb
        self._dscAdapFisdo = dscAdapFisdo
        self._sitEquipamentos = sitEquipamentos
        self._dscMedicamentos = dscMedicamentos
        self._nome = nome
        self._endereco = ender
        self._cnes = cnes
        self._codCidade = codCidade

    def _get_dscMedicamentos(self):
        return self._dscMedicamentos

    def _set_dscMedicamentos(self, dscMedicamentos):
        self._dscMedicamentos = dscMedicamentos

    def _get_cnes(self):
        return self._cnes

    def _set_cnes(self, cnes):
        self._cnes = cnes

    def _get_codigo_cidade(self):
        return self._codCidade

    def _set_codigo_cidade(self, codigo):
        self._codCidade = codigo

    def _get_dscEstFisAmb(self):
        return self._dscEstFisAmb

    def _set_dscEstFisAmb(self, dscEstFisAmb):
        self._dscEstFisAmb = dscEstFisAmb

    def _get_dscAdapFisdo(self):
        return self._dscAdapFisdo

    def _set_dscAdapFisdo(self, dscAdapFisdo):
        self._dscAdapFisdo = dscAdapFisdo

    def _get_sitEquipamentos(self):
        return self._sitEquipamentos

    def _set_sitEquipamentos(self, sitEquipamentos):
        self._sitEquipamentos = sitEquipamentos

    codCidade = property(_get_codigo_cidade, _set_codigo_cidade)
    dscMedicamentos = property(_get_dscMedicamentos, _set_dscMedicamentos)
    cnes = property(_get_cnes, _set_cnes)
    dscEstFisAmb = property(_get_dscEstFisAmb, _set_dscEstFisAmb)
    dscAdapFisdo = property(_get_dscAdapFisdo, _set_dscAdapFisdo)
    sitEquipamentos = property(_get_sitEquipamentos, _set_sitEquipamentos)


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

    logadouro = property(_get_logadouro, _set_logadouro)
    bairro = property(_get_bairro, _set_bairro)
    cidade = property(_get_cidade, _set_cidade)
    telefone = property(_get_telefone, _set_telefone)

class NumeroTelefoneInvalido(Exception):
    def __init__(self, numero, mensagem = "Numero de telefone invalido"):
        super().__init__(mensagem)
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
        if atrib == 'numero':
            self._numero = value
        elif atrib == 'mensagem':
            self._mensagem = value