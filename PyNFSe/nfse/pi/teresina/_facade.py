from PyNFSe.utils.certificado import certificado
from PyNFSe.utils.pi.teresina.assinatura import Assinatura
from PyNFSe.nfse.pi.teresina import serializacao
from PyNFSe.nfse.pi.teresina.comunicacao import Comunicacao


class Facade:

    def __init__(self, certificado_pfx, senha, producao=False):
        namespace = '{http://www.issdigitalthe.com.br/WsNFe2/LoteRps.jws}'
        url_producao = 'http://www.issdigitalthe.com.br/WsNFe2/LoteRps.jws?wsdl'

        cert, cert_file, key, key_file = certificado(certificado_pfx, senha)
        url_ambiente = url_producao #if producao else url_homologacao
        cert_file_and_key_file = (cert_file.name, key_file.name)

        self._assinador = Assinatura(cert, key, namespace)
        self._servicos_wsdl = Comunicacao(url_ambiente, cert_file_and_key_file, producao)


    def enviar_assincrono(self, dict_cabecalho, dict_lote_rps):
        xml = serializacao.enviar_assincrono(dict_cabecalho, dict_lote_rps)
        xml = self._assinador.assinar_xml(xml, 'Lote')
        return self._servicos_wsdl.enviar_assincrono(xml)

    def teste_enviar(self, dict_cabecalho, dict_lote_rps):
        xml = serializacao.enviar_assincrono(dict_cabecalho, dict_lote_rps)
        xml = self._assinador.assinar_xml(xml,  'Lote')
        return self._servicos_wsdl.teste_enviar(xml)

    def consultar_lote(self, dict_consulta_lote):
        xml = serializacao.consultar_lote(dict_cabecalho_consulta)
        return self._servicos_wsdl.consultar_lote(xml)

    def consultar_nota(self, dict_consulta_notas):
        xml = serializacao.consultar_nota(dict_consulta_notas)
        xml = self._assinador.assinar_xml(xml,  'Cabecalho')
        return self._servicos_wsdl.consultar_nota(xml)

    def consultar_sequencial_rps(self, dict_consulta_seq_rps):
        xml = serializacao.consultar_sequencial_rps(dict_consulta_seq_rps)
        return self._servicos_wsdl.consultar_sequencial_rps(xml)

    def cancelar_nfse(self, dict_cabecalho, dict_lote_nfse):
        xml = serializacao.cancelar_nfse(dict_cancela)
        xml = self._assinador.assinar_xml(xml, 'Lote')
        return self._servicos_wsdl.cancelar_nfse(xml)

    def consultar_nfse_rps()
