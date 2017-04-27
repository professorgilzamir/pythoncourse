from LocalizacaoGeografica import LocalizacaoGeografica

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

