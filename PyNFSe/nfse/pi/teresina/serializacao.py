from pyxb import BIND
from PyNFSe.nfse.pi.teresina import _schema as nfse_schema
from PyNFSe.nfse.pi.teresina import _tipos as nfse_tipos
from PyNFSe.utils.pi.teresina.entidades import Prestador, Tomador, ItemRPS, RPS, LoteRPS
from PyNFSe.utils.pi.teresina.options import tipo_logradouro, tipo_bairro
from PyNFSe.utils.errors import *


def enviar_assincrono(dict_cabecalho, dict_lote_rps):
    envio = nfse_schema.ReqEnvioLoteRPS()
    envio.Cabecalho = BIND()

    dict_cabecalho['metodo_envio'] = 'WS'
    dict_cabecalho['versao'] = 1
    
    try:
        envio.Cabecalho.CodCidade = dict_cabecalho['cod_cidade']
        envio.Cabecalho.CPFCNPJRemetente = dict_cabecalho['cpf_cnpj_remetente']
        envio.Cabecalho.RazaoSocialRemetente = dict_cabecalho['razao_social_remetente']
        envio.Cabecalho.transacao = 'true' if 'transacao' in dict_cabecalho.keys() else 'false'
        envio.Cabecalho.dtInicio = parse_date(dict_cabecalho['dt_inicio'])
        envio.Cabecalho.dtFim = parse_date(dict_cabecalho['dt_fim'])
        envio.Cabecalho.QtdRPS = nfse_tipos.tpQtdRpsLote(dict_cabecalho['qtd_rps'])
        envio.Cabecalho.ValorTotalServicos = dict_cabecalho['valor_total_servicos']#)
        envio.Cabecalho.ValorTotalDeducoes = dict_cabecalho['valor_total_deducoes']#)
        envio.Cabecalho.Versao = dict_cabecalho['versao']
        envio.Cabecalho.MetodoEnvio = dict_cabecalho['metodo_envio']
    except KeyError as err:
        raise KeyObrigatoriaError(err)

    envio.Lote = BIND()

    lote_rps = LoteRPS(**dict_lote_rps)

    envio.Lote.Id = lote_rps.id

    for rps in lote_rps.lista_rps:
        envio.Lote.append(_serial_rps(rps))
    
    xml = envio.toxml()

    xml = write_attr_string(xml, 'ReqEnvioLoteRPS', 'xmlns:xsi', 
        'http://www.w3.org/2001/XMLSchema-instance')
    
    xml = write_attr_string(xml, 'ReqEnvioLoteRPS', 'xsi:schemaLocation', 
        'http://localhost:8080/WsNFe2/lote '+
        'http://localhost:8080/WsNFe2/xsd/ReqEnvioLoteRPS.xsd')
    
    xml = write_attr_string(xml, 'ReqEnvioLoteRPS', 'xmlns:tipos', 
        'http://localhost:8080/WsNFe2/tp')
    
    xml = _clean_xml(xml)

    return xml


def consultar_lote(dict_cabecalho):
    consulta = nfse_schema.ReqConsultaLote()
    consulta.Cabecalho = BIND()

    try:
        consulta.Cabecalho.CodCidade = dict_cabecalho['cod_cidade']
        consulta.Cabecalho.CPFCNPJRemetente = dict_cabecalho['cpf_cnpj_remetente']
        consulta.Cabecalho.NumeroLote = dict_cabecalho['numero_lote']
        consulta.Cabecalho.Versao = 1
    except KeyError as err:
        raise KeyObrigatoriaError(err)

    xml = consulta.toxml()
    
    xml = write_attr_string(xml, 'ReqConsultaLote', 'xsi:schemaLocation', 
    'http://localhost:8080/WsNFe2/lote '+
    'http://localhost:8080/WsNFe2/xsd/ReqConsultaLote.xsd')

    xml = write_attr_string(xml, 'ReqConsultaLote', 'xmlns:tipos', 
        'http://localhost:8080/WsNFe2/tp')

    xml = _clean_xml(xml)
    return xml


def _serial_item(item_rps):
    inf_item = nfse_tipos.tpItens()
    inf_item.DiscriminacaoServico = item_rps.discriminacao_servico
    inf_item.Quantidade = "{:.4f}".format(item_rps.quantidade)
    inf_item.ValorUnitario = "{:.4f}".format(item_rps.valor_unitario)
    inf_item.ValorTotal = "{:.2f}".format(item_rps.valor_total)
    inf_item.Tributavel = item_rps.tributavel
    return inf_item


def _serial_deducao(deducao_rps):
    inf_deducao = nfse_tipos.tpDeducoes()
    inf_deducao.DeducaoPor = deducao_rps.deducao_por
    inf_deducao.TipoDeducao = deducao_rps.tipo_deducao
    if deducao_rps.cpf_cnpj_referencia:
        inf_deducao.CPFCNPJReferencia = deducao_rps.cpf_cnpj_referencia
    if deducao_rps.numero_nf_referencia:
        inf_deducao.NumeroNFReferencia = deducao_rps.numero_nf_referencia
    if deducao_rps.valor_total_referencia:
        inf_deducao.ValorTotalReferencia = "{:.2f}".format(deducao_rps.valor_total_referencia)
    inf_deducao.PercentualDeduzir = "{:.2f}".format(deducao_rps.percentual_deduzir)
    inf_deducao.ValorDeduzir = "{:.2f}".format(deducao_rps.valor_deduzir)
    return inf_deducao


def _serial_rps(dict_rps):
    rps = RPS(**dict_rps)

    inf_rps = nfse_tipos.tpRPS()
    inf_rps.Id = rps.id
    inf_rps.Assinatura = rps.assinatura
    inf_rps.InscricaoMunicipalPrestador = rps.prestador.inscricao_municipal_prestador.zfill(7)
    inf_rps.RazaoSocialPrestador = rps.prestador.razao_social_prestador
    inf_rps.TipoRPS = rps.tipo_rps
    inf_rps.SerieRPS = rps.serie_rps
    inf_rps.NumeroRPS = rps.numero_rps
    inf_rps.DataEmissaoRPS = rps.data_emissao_rps.strftime("%Y-%m-%dT%H:%M:%S")
    inf_rps.SituacaoRPS = rps.situacao_rps
    if rps.serie_rps_substituido:
        inf_rps.SerieRPSSubstituido = BIND()
        inf_rps.SerieRPSSubstituido.Factory(rps.serie_rps_substituido)
    if rps.numero_nfse_substituida:
        inf_rps.NumeroNFSeSubstituida = rps.numero_nfse_substituida
    if rps.numero_rps_substituido:
        inf_rps.NumeroRPSSubstituido = rps.numero_rps_substituido
    if rps.data_emissao_nfse_substituida:
        inf_rps.DataEmissaoNFSeSubstituida = rps.data_emissao_nfse_substituida
    inf_rps.SeriePrestacao = rps.serie_prestacao
    inf_rps.InscricaoMunicipalTomador = BIND(rps.tomador.inscricao_municipal_tomador)
    inf_rps.CPFCNPJTomador = rps.tomador.cpf_cnpj_tomador
    inf_rps.RazaoSocialTomador = rps.tomador.razao_social_tomador
    if rps.tomador.doc_tomador_estrangeiro:
        inf_rps.DocTomadorEstrangeiro = rps.tomador.doc_tomador_estrangeiro
    inf_rps.TipoLogradouroTomador = rps.tomador.tipo_logradouro_tomador
    inf_rps.LogradouroTomador = rps.tomador.logradouro_tomador
    inf_rps.NumeroEnderecoTomador = rps.tomador.numero_endereco_tomador
    if rps.tomador.complemento_endereco_tomador:
        inf_rps.ComplementoEnderecoTomador = rps.tomador.complemento_endereco_tomador
    if rps.tomador.tipo_bairro_tomador in tipo_bairro.options:    
        inf_rps.TipoBairroTomador = rps.tomador.tipo_bairro_tomador
    else:
        raise ConteudoInvalidoError('tipo_bairro_tomador')
    inf_rps.BairroTomador = rps.tomador.bairro_tomador
    inf_rps.CidadeTomador = rps.tomador.cidade_tomador
    inf_rps.CidadeTomadorDescricao = rps.tomador.cidade_tomador_descricao
    inf_rps.CEPTomador = rps.tomador.cep_tomador
    inf_rps.EmailTomador = rps.tomador.email_tomador
    inf_rps.CodigoAtividade = rps.codigo_atividade
    inf_rps.AliquotaAtividade = rps.aliquota_atividade
    inf_rps.TipoRecolhimento = rps.tipo_recolhimento
    inf_rps.MunicipioPrestacao = rps.municipio_prestacao
    inf_rps.MunicipioPrestacaoDescricao = rps.municipio_prestacao_descricao
    inf_rps.Operacao = rps.operacao
    inf_rps.Tributacao = rps.tributacao
    inf_rps.ValorPIS = "{:.2f}".format(rps.valor_pis)
    inf_rps.ValorCOFINS = "{:.2f}".format(rps.valor_cofins)
    inf_rps.ValorINSS = "{:.2f}".format(rps.valor_inss)
    inf_rps.ValorIR = "{:.2f}".format(rps.valor_ir)
    inf_rps.ValorCSLL = "{:.2f}".format(rps.valor_csll)
    inf_rps.AliquotaPIS = "{:.4f}".format(rps.aliquota_pis)
    inf_rps.AliquotaCOFINS = "{:.4f}".format(rps.aliquota_cofins)
    inf_rps.AliquotaINSS = "{:.4f}".format(rps.aliquota_inss)
    inf_rps.AliquotaIR = "{:.4f}".format(rps.aliquota_ir)
    inf_rps.AliquotaCSLL = "{:.4f}".format(rps.aliquota_csll)
    inf_rps.DescricaoRPS = rps.descricao_rps
    if rps.prestador.ddd_prestador:
        inf_rps.DDDPrestador = BIND()
        inf_rps.DDDPrestador.Factory(rps.prestador.ddd_prestador)
    if rps.prestador.telefone_prestador:
        inf_rps.TelefonePrestador = BIND()
        inf_rps.TelefonePrestador.Factory(rps.prestador.telefone_prestador)
    if rps.tomador.ddd_tomador:
        inf_rps.DDDTomador = BIND()
        inf_rps.DDDTomador.Factory(rps.tomador.ddd_tomador)
    if rps.tomador.telefone_tomador:
        inf_rps.TelefoneTomador = BIND()
        inf_rps.TelefoneTomador.Factory(rps.tomador.telefone_tomador)
    if rps.mot_cancelamento:
        inf_rps.MotCancelamento = rps.mot_cancelamento
    if rps.cpf_cnpj_intermediario:
        inf_rps.CpfCnpjIntermediario = rps.cpf_cnpj_intermediario

    inf_rps.Itens = nfse_tipos.tpListaItens()
    inf_rps.Deducoes = nfse_tipos.tpListaDeducoes()

    for item in rps.itens:
        inf_rps.Itens.append(_serial_item(item))

    for deducao in rps.deducoes:
        inf_rps.Deducoes.append(_serial_deducao(deducao))

    return inf_rps


def parse_date(value):
    try:
        return value.strftime('%Y-%m-%d')
    except:
        raise Exception('Formato de data incorreto, utilize "datetime".')


def write_attr_string(xml, elem, attr, value):
    elem = '<ns1:{}'.format(elem)
    return xml.replace(elem, '{} {}="{}"'.format(
            elem, attr, value
        )
    )


def _clean_xml(xml):
    return xml.replace('<?xml version="1.0" ?>','')
    # return xml.replace('ns1:', '').replace(':ns1', '').replace('<?xml version="1.0" ?>','')
                                                               # '<?xml version="1.0" encoding="UTF-8"?>')
