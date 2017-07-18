from .base import Entidade


class Tomador(Entidade):
    inscricao_municipal_tomador = str()
    cpf_cnpj_tomador = str()
    razao_social_tomador = str()
    doc_tomador_estrangeiro = str()
    tipo_logradouro_tomador = '-'
    logradouro_tomador = '-'
    numero_endereco_tomador = str()
    complemento_endereco_tomador = str()
    tipo_bairro_tomador = '-'
    bairro_tomador = '-'
    cidade_tomador = int()
    cidade_tomador_descricao = str()
    cep_tomador = str()
    email_tomador = str()
    ddd_tomador = str()
    telefone_tomador = str()

    campos_obrigatorios = [
        'inscricao_municipal_tomador',
        'cpf_cnpj_tomador',
        'razao_social_tomador',
        'tipo_logradouro_tomador',
        'logradouro_tomador',
        'numero_endereco_tomador',
        'tipo_bairro_tomador',
        'bairro_tomador',
        'cidade_tomador',
        'cidade_tomador_descricao',
        'cep_tomador',
        'email_tomador'
    ]