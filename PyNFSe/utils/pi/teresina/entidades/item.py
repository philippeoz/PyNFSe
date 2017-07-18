from .base import Entidade
from decimal import Decimal

class ItemRPS(Entidade):
    discriminacao_servico = str()
    quantidade = Decimal()
    valor_unitario = Decimal()
    valor_total = Decimal()
    tributavel = str()

    campos_obrigatorios = [
        'discriminacao_servico',
        'quantidade',
        'valor_unitario',
        'valor_total',
        'tributavel'
    ]