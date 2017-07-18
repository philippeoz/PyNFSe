from signxml import XMLSigner, methods


class AssinaturaBase:

    def __init__(self, certificado, chave, namespace):

        self.cert = certificado
        self.key = chave
        self.NAMESPACE = namespace

        self._assinador = XMLSigner(
            method=methods.detached,
            signature_algorithm="rsa-sha1",
            digest_algorithm='sha1',
            c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315'
        )
