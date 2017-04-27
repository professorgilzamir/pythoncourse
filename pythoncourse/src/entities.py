import re

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

    latitude = property(_get_latitude, _set_latitude)
    longitude = property(_get_longitude, _set_longitude)

class UnidadeDeSaude(LocalizacaoGeografica):
    def __init__(self, latitude, longitude,
                 codigo, dscEstFisAmb, dscAdapFisdo, sitEquipamentos):
        super().__init__(latitude, longitude)
        self._codigo = codigo
        self._dscEstFisAmb = dscEstFisAmb
        self._dscAdapFisdo = dscAdapFisdo
        self._sitEquipamentos = sitEquipamentos

    def _get_codigo(self):
        return self._codigo

    def _set_codigo(self, codigo):
        self._codigo = codigo

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

    codigo = property(_get_codigo, _set_codigo)
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
        
    def validar_telefone(self, telefone):
        fone = re.compile('(d{2}) d{4,5}-d{4}')
        return fone.match(telefone)

    logadouro = property(_get_logadouro, _set_logadouro)
    bairro = property(_get_bairro, _set_bairro)
    cidade = property(_get_cidade, _set_cidade)
    telefone = property(_get_telefone, _set_telefone)
