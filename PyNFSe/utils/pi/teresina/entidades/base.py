from PyNFSe.utils.errors import CampoObrigatorioError, TipoInvalidoError
from datetime import datetime

class Entidade(object):
    campos_obrigatorios = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if type(getattr(self, key)) != type(value):
                raise TipoInvalidoError(key, self, value)
            setattr(self, key, value)
        self.check_obrigatorios(kwargs)

    def check_obrigatorios(self, kwargs):
        for campo in self.campos_obrigatorios:
            if campo not in kwargs.keys():
                raise CampoObrigatorioError(campo, self)