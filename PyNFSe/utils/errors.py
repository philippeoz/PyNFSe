# -*- coding: utf-8 -*-


class PyNFSeError(Exception):
    """Excessao base para o PyNFSe"""


class ConteudoInvalidoError(PyNFSeError):
    def __init__(self, campo):
        self.campo = campo
        super(ConteudoInvalidoError, self).__init__()

    def __str__(self):
        return 'Conteúdo inválido no campo "{}", verifique a documentação.'.format(
            self.campo
        )


class TipoInvalidoError(PyNFSeError):
    def __init__(self, campo, objeto, tipo_incorreto):
        self.campo = campo
        self.tipo = type(getattr(objeto, campo)).__name__
        self.classe = objeto.__class__.__name__
        self.tipo_incorreto = type(tipo_incorreto).__name__
        super(TipoInvalidoError, self).__init__()

    def __str__(self):
        return 'Tipo inválido no campo "{}" da classe "{}", tipo "{}" foi enviado, tipo "{}" era esperado.'.format(
            self.campo,
            self.classe,
            self.tipo_incorreto,
            self.tipo
        )


class CampoObrigatorioError(PyNFSeError):
    def __init__(self, campo, objeto):
        self.campo = campo
        self.tipo = type(getattr(objeto, campo)).__name__
        self.objeto = objeto.__class__.__name__
        super(CampoObrigatorioError, self).__init__()

    def __str__(self):
        return 'O campo "{}" da classe "{}" do tipo "{}" é obrigatório.'.format(
            self.campo,
            self.objeto,
            self.tipo
        )


class KeyObrigatoriaError(PyNFSeError):
    def __init__(self, key, dic):
        self.key = key
        self.dic = dic
        super(KeyObrigatoriaError, self).__init__()

    def __str__(self):
        return 'O envio de "{}" é obrigatório neste método.'.format(
            self.key
        )
