from .base import  Entidade
from decimal import Decimal
from .prestador import Prestador
from .tomador import Tomador
from .item import ItemRPS
from .deducao import DeducaoRPS
from datetime import datetime
import hashlib

class RPS(Entidade):
    id = int()
    assinatura = str()
    tipo_rps = str()
    serie_rps = str()
    numero_rps = int()
    data_emissao_rps = datetime.now()
    situacao_rps = str()
    serie_rps_substituido = str()
    numero_nfse_substituida = int()
    numero_rps_substituido = int()
    data_emissao_nfse_substituida = datetime(1990,1,1)
    serie_prestacao = 99
    codigo_atividade = str()
    aliquota_atividade = Decimal()
    tipo_recolhimento = str()
    municipio_prestacao = int()
    municipio_prestacao_descricao = str()
    operacao = str()
    tributacao = str()
    valor_pis = Decimal()
    valor_cofins = Decimal()
    valor_inss = Decimal()
    valor_ir = Decimal()
    valor_csll = Decimal()
    aliquota_pis = Decimal()
    aliquota_cofins = Decimal()
    aliquota_inss = Decimal()
    aliquota_ir = Decimal()
    aliquota_csll = Decimal()
    descricao_rps = str()
    mot_cancelamento = str()
    cpf_cnpj_intermediario = str()
    prestador = dict()
    tomador = dict()
    deducoes = []
    itens = []

    campos_obrigatorios = [
        'id',
        'tipo_rps',
        'serie_rps',
        'numero_rps',
        'data_emissao_rps',
        'situacao_rps',
        'serie_prestacao',
        'codigo_atividade',
        'aliquota_atividade',
        'tipo_recolhimento',
        'municipio_prestacao',
        'municipio_prestacao_descricao',
        'operacao',
        'tributacao',
        'valor_pis',
        'valor_cofins',
        'valor_inss',
        'valor_ir',
        'valor_csll',
        'aliquota_pis',
        'aliquota_cofins',
        'aliquota_inss',
        'aliquota_ir',
        'aliquota_csll',
        'descricao_rps',
        'prestador',
        'tomador',
        'itens'
    ]

    def __init__(self, **kwargs):
        super(RPS, self).__init__(**kwargs)
        self.prestador = Prestador(**self.prestador)
        self.tomador = Tomador(**self.tomador)
        
        if len(self.itens) > 25:
            raise Exception('São pemitidos no máximo 25 itens por RPS.')
        if len(self.deducoes) > 200:
            raise Exception('São pemitidos no máximo 200 deduções por RPS.')

        self.itens = [ItemRPS(**item) for item in self.itens]
        if self.deducoes:
            self.deducoes = [DeducaoRPS(**deducao) for deducao in self.deducoes]

        self.set_assinatura()

    def set_assinatura(self):
        total_servicos = sum([item.valor_total for item in self.itens])
        if self.deducoes:
            total_deducoes = sum([deducao.valor_deduzir for deducao in self.deducoes])
        else:
            total_deducoes = Decimal(0)

        sign = "{}{}{}{}{}{}{}{}{}{}{}".format(
            self.prestador.inscricao_municipal_prestador.zfill(11),
            self.serie_rps.ljust(5),
            "{}".format(self.numero_rps).zfill(12),
            self.data_emissao_rps.strftime('%Y%m%d'),
            self.tributacao.ljust(2),
            self.situacao_rps,
            'N' if self.tipo_recolhimento == 'A' else 'S',
            "{:.2f}".format(total_servicos - total_deducoes).zfill(15),
            "{:.2f}".format(total_deducoes).zfill(15),
            self.codigo_atividade.zfill(10),
            self.tomador.cpf_cnpj_tomador.zfill(14)
        )

        self.assinatura = hashlib.sha1(sign.encode()).hexdigest().encode()


    