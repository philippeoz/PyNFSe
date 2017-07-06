from PyNFSe.utils.certificado import certificado as c
from PyNFSe.utils.assinatura import Assinatura
from PyNFSe.nfse.pi.teresina import serializacao as s
from PyNFSe.nfse.pi.teresina.comunicacao import Comunicacao


class Facade:

    def __init__(self, certificado_pfx, senha, producao=False):
        namespace = '{http://issteresina.teresina.pi.gov.br/iss/nfse.xsd}'
        url_homologacao = 'https://pilotoissteresina.teresina.pr.gov.br/nfse_ws/NfseWs.asmx?WSDL'
        url_producao = 'https://issteresina.teresina.pi.gov.br/Iss.NfseWebService/nfsews.asmx?WSDL'

        cert, cert_file, key, key_file = c(certificado_pfx, senha)
        url_ambiente = url_producao if producao else url_homologacao
        cert_file_and_key_file = (cert_file.name, key_file.name)

        self._assinador = Assinatura(cert, key, namespace)
        self._servicos_wsdl = Comunicacao(url_ambiente, cert_file_and_key_file, producao)

    def consultar_nfse_por_numero(self, dict_prestador, numero_nfse):
        xml = s.consulta_nfse_por_numero(dict_prestador, numero_nfse)
        xml_retorno = self._servicos_wsdl.consultar_nfse(xml)

        return xml_retorno

    def consultar_nfse_por_data(self, dict_prestador, data_inicial, data_final):
        xml = s.consulta_nfse_por_data(dict_prestador, data_inicial, data_final)
        xml_retorno = self._servicos_wsdl.consultar_nfse(xml)

        return xml_retorno

    def consultar_nfse_por_rps(self, dict_rps):
        xml = s.consulta_nfse_por_rps(dict_rps)
        xml_retorno = self._servicos_wsdl.consultar_nfse_por_rps(xml)

        return xml_retorno

    def consultar_situacao_lote_rps(self, dict_prestador, protocolo):
        xml = s.consulta_situacao_lote_rps(dict_prestador, protocolo)
        xml_retorno = self._servicos_wsdl.consultar_situacao_lote_rps(xml)

        return xml_retorno

    def consultar_lote_rps(self, dict_prestador, protocolo):
        xml = s.consulta_lote_rps(dict_prestador, protocolo)
        xml_retorno = self._servicos_wsdl.consultar_lote_rps(xml)

        return xml_retorno

    def recepcionar_lote_rps(self, dict_lote_rps):
        xml = s.envio_lote_rps(dict_lote_rps)
        xml = self._assinador.assinar_lote_rps(xml)
        xml_retorno = self._servicos_wsdl.recepcionar_lote_rps(xml)

        return xml_retorno

    def cancelar_nfse(self, dict_pedido_cancelamento_nfse):
        xml = s.cancela_nfse(dict_pedido_cancelamento_nfse)
        xml = self._assinador.assinar_cancelamento_nfse(xml)
        xml_retorno = self._servicos_wsdl.cancelar_nfse(xml)

        return xml_retorno

    def validar_xml(self, xml):
        retorno = self._servicos_wsdl.validar_xml(xml)

        return retorno
