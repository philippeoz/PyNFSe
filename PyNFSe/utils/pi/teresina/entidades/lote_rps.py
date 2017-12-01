from .base import Entidade


class LoteRPS(Entidade):
    _id = str()
    lista_rps = []

    campos_obrigatorios = [
        'id',
        'lista_rps'
    ]

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = "lote:{}".format(value)

    @property
    def lista_nfse(self):
        return self.lista_rps

    @lista_nfse.setter
    def lista_nfse(self, value)
        self.lista_rps = value