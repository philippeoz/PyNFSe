from lxml import etree
from PyNFSe.utils.assinatura_base import AssinaturaBase


class Assinatura(AssinaturaBase):

    def assinar_xml(self, xml, node):
        root = etree.fromstring(xml.encode())
        node_ref_uri = root.find(node)
        reference_uri = "{}".format(node_ref_uri.attrib.get('Id'))
        root = self._assinatura_xml(root, reference_uri)
        xml_assinado = etree.tostring(root, encoding='utf-8').decode()
        return xml_assinado.replace('ds:', '').replace(':ds', '')


    def _assinatura_xml(self, data, reference_uri):

        assinatura = self._assinador.sign(
            data=data,
            key=self.key,
            cert=self.cert,
            reference_uri='#{}'.format(reference_uri)
        )

        return assinatura
