from lxml import etree
from PyNFSe.utils.assinatura_base import AssinaturaBase


class Assinatura(AssinaturaBase):

    def assinar_lote_rps(self, xml_lote_rps):

        root = etree.fromstring(xml_lote_rps.encode())

        lote_rps = root.find('Lote')
        reference_uri = "{}".format(lote_rps.attrib.get('Id'))
        root = self._assinatura_xml(root, reference_uri)

        xml_lote_rps_assinado = etree.tostring(root, encoding='utf-8').decode()

        xml_lote_rps_assinado = xml_lote_rps_assinado.replace('ds:', '').replace(':ds', '')

        return xml_lote_rps_assinado

    def assinar_consulta_nota(self, xml_consulta_nota):

        root = etree.fromstring(xml_consulta_nota.encode())

        consulta_nota = root.find('Cabecalho')
        reference_uri = "{}".format(consulta_nota.attrib.get('Id'))
        root = self._assinatura_xml(root, reference_uri)

        xml_consulta_nota_assinado = etree.tostring(root, encoding='utf-8').decode()
        xml_consulta_nota_assinado = xml_consulta_nota_assinado.replace('ds:', '').replace(':ds', '')
        
        return xml_consulta_nota_assinado

    def _assinatura_xml(self, data, reference_uri):

        assinatura = self._assinador.sign(
            data=data,
            key=self.key,
            cert=self.cert,
            reference_uri='#{}'.format(reference_uri)
        )

        return assinatura
