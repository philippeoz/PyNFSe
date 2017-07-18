from PyNFSe.utils.cliente_comunicacao import ClienteComunicacao


class Comunicacao:

    def __init__(self, url_ambiente, certificado, producao):
        self._cliente = ClienteComunicacao(url_ambiente, certificado, producao)

    def enviar_assincrono(self, xml):
        return self._cliente.service.enviar(xml)

    def enviar_sincrono(self, xml):
        return self._cliente.service.enviarSincrono(xml)

    def teste_enviar(self, xml):
        return self._cliente.service.testeEnviar(xml)

    def consultar_lote(self, xml):
        return self._cliente.service.consultarLote(xml)

    def consultar_nota(self, xml):
        return self._cliente.service.consultarNota(xml)

    def consultar_sequencial_rps(self, xml):
        return self._cliente.service.consultarSequencialRps(xml)

    def cancelar_nfse(self, xml):
        return self._cliente.service.Cancelar(xml)

    def consultar_nfse_rps(self, xml):
        return self._cliente.service.consultarNFSeRps(xml)
