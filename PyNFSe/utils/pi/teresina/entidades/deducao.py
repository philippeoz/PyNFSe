from .base import Entidade
from decimal import Decimal
from PyNFSe.utils.pi.teresina.options import tipo_deducao
from PyNFSe.utils.errors import ConteudoInvalidoError

class DeducaoRPS(Entidade):
    deducao_por = str()
    tipo_deducao = str()
    cpf_cnpj_referencia = str()
    numero_nf_referencia = int()
    valor_total_referencia = Decimal()
    percentual_deduzir = Decimal()
    valor_deduzir = Decimal()

    campos_obrigatorios = [
        'deducao_por',
        'tipo_deducao',
        'percentual_deduzir',
        'valor_deduzir'
    ]

    def __init__(self, **kwargs):
        super(DeducaoRPS, self).__init__(**kwargs)
        set_tipo_deducao()


    def set_tipo_deducao(self):
        if self.deducao_por == 'Valor':
            if self.tipo_deducao not in tipo_deducao.options:
                raise ConteudoInvalidoError('tipo_deducao')
        else:
            self.tipo_deducao = ''
