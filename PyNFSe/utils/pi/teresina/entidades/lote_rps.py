from .base import Entidade


class LoteRPS(Entidade):
    id = str()
    lista_rps = []

    campos_obrigatorios = [
        'id',
        'lista_rps'
    ]
