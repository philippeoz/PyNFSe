from lxml import etree
from PyNFSe.utils.assinatura_base import AssinaturaBase


class Assinatura(AssinaturaBase):

    def assinar_lote_rps(self, xml_lote_rps):

        root = etree.fromstring(xml_lote_rps.encode())

        lote_rps = root.find('Lote')
        reference_uri = "lote:{}".format(lote_rps.attrib.get('Id'))
        assinatura = self._assinatura_xml(root, reference_uri)

        root.append(assinatura)

        xml_lote_rps_assinado = etree.tostring(root, encoding='utf-8').decode()

        xml_lote_rps_assinado = xml_lote_rps_assinado.replace('ds:', '').replace(':ds', '')

        return xml_lote_rps_assinado

    def assinar_cancelamento_nfse(self, xml_cancelamento_nfse):

        root = etree.fromstring(xml_cancelamento_nfse.encode())
        pedido = root.find('{0}Pedido'.format(self.NAMESPACE))
        inf_pedido = pedido.find('{0}InfPedidoCancelamento'.format(self.NAMESPACE))
        reference_uri = inf_pedido.attrib.get('id')

        assinatura = self._assinatura_xml(pedido, reference_uri)

        pedido.append(assinatura)

        xml_pedido_cancelamento_assinado = etree.tostring(root, encoding='utf-8').decode()

        xml_pedido_cancelamento_assinado = xml_pedido_cancelamento_assinado.replace('ds:', '').replace(':ds', '')

        return xml_pedido_cancelamento_assinado

    def _assinatura_xml(self, data, reference_uri):

        assinatura = self._assinador.sign(
            data=data,
            key=self.key,
            cert=self.cert,
            reference_uri='#{}'.format(reference_uri)
        )

        return assinatura
