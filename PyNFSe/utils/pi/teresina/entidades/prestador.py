from .base import Entidade


class Prestador(Entidade):
    inscricao_municipal_prestador = str()
    razao_social_prestador = str()
    ddd_prestador = str()
    telefone_prestador = str()

    campos_obrigatorios = [
        'inscricao_municipal_prestador',
        'razao_social_prestador'
    ]