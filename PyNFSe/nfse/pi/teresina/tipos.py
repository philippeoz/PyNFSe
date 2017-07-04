# ./tipos.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:af553f9b32046b46bad23e227520f6cea39c12b4
# Generated 2017-07-04 11:52:35.944177 by PyXB version 1.2.5 using Python 3.5.3.final.0
# Namespace http://localhost:8080/WsNFe2/tp [xmlns:tipos]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6a62ca60-60c8-11e7-bdae-6241da4ed12b')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://localhost:8080/WsNFe2/tp', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://localhost:8080/WsNFe2/tp}nulo
class nulo (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """Definição para aceitar dado tipo nulo
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 9, 1)
    _Documentation = 'Definição para aceitar dado tipo nulo\n\t\t\t'
nulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nulo, enum_prefix=None)
nulo.emptyString = nulo._CF_enumeration.addEnumeration(unicode_value='', tag='emptyString')
nulo._InitializeFacetMap(nulo._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'nulo', nulo)
_module_typeBindings.nulo = nulo

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpMetodoEnvio
class tpMetodoEnvio (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Metodo de Envio."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpMetodoEnvio')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 18, 1)
    _Documentation = 'Metodo de Envio.'
tpMetodoEnvio._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpMetodoEnvio, enum_prefix=None)
tpMetodoEnvio.WS = tpMetodoEnvio._CF_enumeration.addEnumeration(unicode_value='WS', tag='WS')
tpMetodoEnvio.DLL = tpMetodoEnvio._CF_enumeration.addEnumeration(unicode_value='DLL', tag='DLL')
tpMetodoEnvio.DMS = tpMetodoEnvio._CF_enumeration.addEnumeration(unicode_value='DMS', tag='DMS')
tpMetodoEnvio._InitializeFacetMap(tpMetodoEnvio._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpMetodoEnvio', tpMetodoEnvio)
_module_typeBindings.tpMetodoEnvio = tpMetodoEnvio

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpVersaoComponente
class tpVersaoComponente (pyxb.binding.datatypes.string):

    """Tipo Versão do Componente de Envio.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpVersaoComponente')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 41, 1)
    _Documentation = 'Tipo Versão do Componente de Envio.\n\t\t\t'
tpVersaoComponente._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
tpVersaoComponente._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpVersaoComponente._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpVersaoComponente._InitializeFacetMap(tpVersaoComponente._CF_maxLength,
   tpVersaoComponente._CF_minLength,
   tpVersaoComponente._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpVersaoComponente', tpVersaoComponente)
_module_typeBindings.tpVersaoComponente = tpVersaoComponente

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpQtdRpsLote
class tpQtdRpsLote (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpQtdRpsLote')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 52, 1)
    _Documentation = None
tpQtdRpsLote._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpQtdRpsLote, value=pyxb.binding.datatypes.integer(1))
tpQtdRpsLote._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=tpQtdRpsLote, value=pyxb.binding.datatypes.integer(250))
tpQtdRpsLote._InitializeFacetMap(tpQtdRpsLote._CF_minInclusive,
   tpQtdRpsLote._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'tpQtdRpsLote', tpQtdRpsLote)
_module_typeBindings.tpQtdRpsLote = tpQtdRpsLote

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}numTam8Tipo
class numTam8Tipo (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'numTam8Tipo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 58, 1)
    _Documentation = None
numTam8Tipo._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=numTam8Tipo, value=pyxb.binding.datatypes.integer(99999999))
numTam8Tipo._InitializeFacetMap(numTam8Tipo._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'numTam8Tipo', numTam8Tipo)
_module_typeBindings.numTam8Tipo = numTam8Tipo

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpAliquota
class tpAliquota (pyxb.binding.datatypes.decimal):

    """Tipo Aliquota."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpAliquota')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 71, 1)
    _Documentation = 'Tipo Aliquota.'
tpAliquota._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpAliquota, value=pyxb.binding.datatypes.decimal('0.0'))
tpAliquota._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4))
tpAliquota._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(6))
tpAliquota._InitializeFacetMap(tpAliquota._CF_minInclusive,
   tpAliquota._CF_fractionDigits,
   tpAliquota._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tpAliquota', tpAliquota)
_module_typeBindings.tpAliquota = tpAliquota

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpAssinatura
class tpAssinatura (pyxb.binding.datatypes.base64Binary):

    """Assinatura digital do RPS emitido.
			O RPS deverá ser assinado digitalmente. O
				contribuinte deverá assinar uma cadeia de caracteres (ASCII) com
				informações do RPS emitido.O certificado digital utilizado na assinatura de
				cancelamento deverá ser o mesmo utilizado na assinatura da mensagem
				XML. A cadeia de caracteres a ser assinada deverá conter 85 posições
				com as informações apresentadas a seguir:Inscrição Municipal (CCM) do Prestador com
				11 caracteres. Caso o CCM do Prestador tenha menos de 8 caracteres,
				o mesmo deverá ser completado com zeros à esquerda.
			Série do RPS com 5 posições. Caso a Série do
				RPS tenha menos de 5 caracteres, o mesmo deverá ser completado com
				espaços em branco à direita.Número do RPS com 12 posições. Caso o Número
				do RPS tenha menos de 12 caracteres, o mesmo deverá ser completado
				com zeros à esquerda.Data da emissão do RPS no formato AAAAMMDD.
			Tipo de Tributação do RPS com 2 posições (sendo
				T: para Tributação no municipio de São Paulo; F: para Tributação
				fora do municipio de São Paulo; I: para Isento; J: para ISS Suspenso
				por Decisão Judicial).Status do RPS com uma posição (sendo N:
				Normal, C: Cancelado; E: Extraviado).ISS Retido com uma posição (sendo S: ISS Retido;
				N: Nota Fiscal sem ISS Retido).Valor dos Serviços com 15 posições e sem
				separador de milhar e decimal.Valor das Deduções com 15 posições e sem
				separador de milhar e decimal.Código da Atividade com 10 posições.
			CPF/CNPJ do tomador com 14 posições. Sem
				formatação (ponto, traço, barra, ....). Completar com zeros à
				esquerda caso seja necessário. Se o Indicador do CPF/CNPJ for 3
				(não-informado), preencher com 14 zeros."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpAssinatura')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 81, 1)
    _Documentation = 'Assinatura digital do RPS emitido.\n\t\t\tO RPS deverá ser assinado digitalmente. O\n\t\t\t\tcontribuinte deverá assinar uma cadeia de caracteres (ASCII) com\n\t\t\t\tinformações do RPS emitido.O certificado digital utilizado na assinatura de\n\t\t\t\tcancelamento deverá ser o mesmo utilizado na assinatura da mensagem\n\t\t\t\tXML. A cadeia de caracteres a ser assinada deverá conter 85 posições\n\t\t\t\tcom as informações apresentadas a seguir:Inscrição Municipal (CCM) do Prestador com\n\t\t\t\t11 caracteres. Caso o CCM do Prestador tenha menos de 8 caracteres,\n\t\t\t\to mesmo deverá ser completado com zeros à esquerda.\n\t\t\tSérie do RPS com 5 posições. Caso a Série do\n\t\t\t\tRPS tenha menos de 5 caracteres, o mesmo deverá ser completado com\n\t\t\t\tespaços em branco à direita.Número do RPS com 12 posições. Caso o Número\n\t\t\t\tdo RPS tenha menos de 12 caracteres, o mesmo deverá ser completado\n\t\t\t\tcom zeros à esquerda.Data da emissão do RPS no formato AAAAMMDD.\n\t\t\tTipo de Tributação do RPS com 2 posições (sendo\n\t\t\t\tT: para Tributação no municipio de São Paulo; F: para Tributação\n\t\t\t\tfora do municipio de São Paulo; I: para Isento; J: para ISS Suspenso\n\t\t\t\tpor Decisão Judicial).Status do RPS com uma posição (sendo N:\n\t\t\t\tNormal, C: Cancelado; E: Extraviado).ISS Retido com uma posição (sendo S: ISS Retido;\n\t\t\t\tN: Nota Fiscal sem ISS Retido).Valor dos Serviços com 15 posições e sem\n\t\t\t\tseparador de milhar e decimal.Valor das Deduções com 15 posições e sem\n\t\t\t\tseparador de milhar e decimal.Código da Atividade com 10 posições.\n\t\t\tCPF/CNPJ do tomador com 14 posições. Sem\n\t\t\t\tformatação (ponto, traço, barra, ....). Completar com zeros à\n\t\t\t\tesquerda caso seja necessário. Se o Indicador do CPF/CNPJ for 3\n\t\t\t\t(não-informado), preencher com 14 zeros.'
tpAssinatura._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tpAssinatura', tpAssinatura)
_module_typeBindings.tpAssinatura = tpAssinatura

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpAssinaturaCancelamento
class tpAssinaturaCancelamento (pyxb.binding.datatypes.base64Binary):

    """Assinatura digital de cancelamento da
				NF-e.Cada NF-e a ser cancelada deverá ter sua
				respectiva assinatura de cancelamento. O contribuinte deverá assinar
				uma cadeia de caracteres (ASCII) com informações da NF-e a ser
				cancelada.O certificado digital utilizado na assinatura de
				cancelamento deverá ser o mesmo utilizado na assinatura da mensagem
				XML. A cadeia de caracteres a ser assinada deverá conter 20 posições
				com as informações apresentadas a seguir:Inscrição Municipal (CCM) do Prestador com
				8 caracteres. Caso o CCM do Prestador tenha menos de 8 caracteres, o
				mesmo deverá ser completado com zeros à esquerda.Número da NF-e RPS com 12 posições. Caso o
				Número da NF-e tenha menos de 12 caracteres, o mesmo deverá ser
				completado com zeros à esquerda."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpAssinaturaCancelamento')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 125, 1)
    _Documentation = 'Assinatura digital de cancelamento da\n\t\t\t\tNF-e.Cada NF-e a ser cancelada deverá ter sua\n\t\t\t\trespectiva assinatura de cancelamento. O contribuinte deverá assinar\n\t\t\t\tuma cadeia de caracteres (ASCII) com informações da NF-e a ser\n\t\t\t\tcancelada.O certificado digital utilizado na assinatura de\n\t\t\t\tcancelamento deverá ser o mesmo utilizado na assinatura da mensagem\n\t\t\t\tXML. A cadeia de caracteres a ser assinada deverá conter 20 posições\n\t\t\t\tcom as informações apresentadas a seguir:Inscrição Municipal (CCM) do Prestador com\n\t\t\t\t8 caracteres. Caso o CCM do Prestador tenha menos de 8 caracteres, o\n\t\t\t\tmesmo deverá ser completado com zeros à esquerda.Número da NF-e RPS com 12 posições. Caso o\n\t\t\t\tNúmero da NF-e tenha menos de 12 caracteres, o mesmo deverá ser\n\t\t\t\tcompletado com zeros à esquerda.'
tpAssinaturaCancelamento._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tpAssinaturaCancelamento', tpAssinaturaCancelamento)
_module_typeBindings.tpAssinaturaCancelamento = tpAssinaturaCancelamento

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCodCidade
class tpCodCidade (pyxb.binding.datatypes.unsignedInt):

    """Código da cidade padrão SIAFI
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCodCidade')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 146, 1)
    _Documentation = 'Código da cidade padrão SIAFI\n\t\t\t'
tpCodCidade._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpCodCidade, value=pyxb.binding.datatypes.unsignedInt(1))
tpCodCidade._InitializeFacetMap(tpCodCidade._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'tpCodCidade', tpCodCidade)
_module_typeBindings.tpCodCidade = tpCodCidade

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpBairro
class tpBairro (pyxb.binding.datatypes.string):

    """Tipo bairro."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpBairro')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 155, 1)
    _Documentation = 'Tipo bairro.'
tpBairro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
tpBairro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpBairro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpBairro._InitializeFacetMap(tpBairro._CF_maxLength,
   tpBairro._CF_minLength,
   tpBairro._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpBairro', tpBairro)
_module_typeBindings.tpBairro = tpBairro

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCEP
class tpCEP (pyxb.binding.datatypes.int):

    """Tipo CEP."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCEP')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 165, 1)
    _Documentation = 'Tipo CEP.'
tpCEP._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCEP._CF_pattern.addPattern(pattern='[0-9]{0,8}')
tpCEP._InitializeFacetMap(tpCEP._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCEP', tpCEP)
_module_typeBindings.tpCEP = tpCEP

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCidade
class tpCidade (pyxb.binding.datatypes.unsignedInt):

    """Código da cidade padrão IBGE
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCidade')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 179, 1)
    _Documentation = 'Código da cidade padrão IBGE\n\t\t\t'
tpCidade._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCidade._CF_pattern.addPattern(pattern='[0-9]')
tpCidade._InitializeFacetMap(tpCidade._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCidade', tpCidade)
_module_typeBindings.tpCidade = tpCidade

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCidadeDescricao
class tpCidadeDescricao (pyxb.binding.datatypes.string):

    """Descricao da Cidade."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCidadeDescricao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 188, 1)
    _Documentation = 'Descricao da Cidade.'
tpCidadeDescricao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
tpCidadeDescricao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpCidadeDescricao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpCidadeDescricao._InitializeFacetMap(tpCidadeDescricao._CF_maxLength,
   tpCidadeDescricao._CF_minLength,
   tpCidadeDescricao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpCidadeDescricao', tpCidadeDescricao)
_module_typeBindings.tpCidadeDescricao = tpCidadeDescricao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCidadeTomadorDescricao
class tpCidadeTomadorDescricao (pyxb.binding.datatypes.string):

    """Descricao da Cidade."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCidadeTomadorDescricao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 198, 1)
    _Documentation = 'Descricao da Cidade.'
tpCidadeTomadorDescricao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
tpCidadeTomadorDescricao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpCidadeTomadorDescricao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpCidadeTomadorDescricao._InitializeFacetMap(tpCidadeTomadorDescricao._CF_maxLength,
   tpCidadeTomadorDescricao._CF_minLength,
   tpCidadeTomadorDescricao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpCidadeTomadorDescricao', tpCidadeTomadorDescricao)
_module_typeBindings.tpCidadeTomadorDescricao = tpCidadeTomadorDescricao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCNPJ
class tpCNPJ (pyxb.binding.datatypes.string):

    """Tipo CNPJ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCNPJ')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 208, 1)
    _Documentation = 'Tipo CNPJ.'
tpCNPJ._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCNPJ._CF_pattern.addPattern(pattern='[0-9]{14}')
tpCNPJ._InitializeFacetMap(tpCNPJ._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCNPJ', tpCNPJ)
_module_typeBindings.tpCNPJ = tpCNPJ

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCPFCNPJ
class tpCPFCNPJ (pyxb.binding.datatypes.string):

    """Tipo CPFCNPJ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCPFCNPJ')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 216, 1)
    _Documentation = 'Tipo CPFCNPJ.'
tpCPFCNPJ._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCPFCNPJ._CF_pattern.addPattern(pattern='[0-9]{11}|[0-9]{14}')
tpCPFCNPJ._InitializeFacetMap(tpCPFCNPJ._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCPFCNPJ', tpCPFCNPJ)
_module_typeBindings.tpCPFCNPJ = tpCPFCNPJ

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCodigoAtividade
class tpCodigoAtividade (pyxb.binding.datatypes.int):

    """Tipo código da atividade CNAE
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCodigoAtividade')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 231, 1)
    _Documentation = 'Tipo código da atividade CNAE\n\t\t\t'
tpCodigoAtividade._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCodigoAtividade._CF_pattern.addPattern(pattern='[0-9]{9}')
tpCodigoAtividade._InitializeFacetMap(tpCodigoAtividade._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCodigoAtividade', tpCodigoAtividade)
_module_typeBindings.tpCodigoAtividade = tpCodigoAtividade

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCodigoServico
class tpCodigoServico (pyxb.binding.datatypes.int):

    """Tipo código de serviço."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCodigoServico')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 240, 1)
    _Documentation = 'Tipo código de serviço.'
tpCodigoServico._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCodigoServico._CF_pattern.addPattern(pattern='[0-9]{4,5}')
tpCodigoServico._InitializeFacetMap(tpCodigoServico._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCodigoServico', tpCodigoServico)
_module_typeBindings.tpCodigoServico = tpCodigoServico

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCodigoEvento
class tpCodigoEvento (pyxb.binding.datatypes.short):

    """Tipo código de evento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCodigoEvento')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 248, 1)
    _Documentation = 'Tipo código de evento.'
tpCodigoEvento._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCodigoEvento._CF_pattern.addPattern(pattern='[0-9]{3,4}')
tpCodigoEvento._InitializeFacetMap(tpCodigoEvento._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCodigoEvento', tpCodigoEvento)
_module_typeBindings.tpCodigoEvento = tpCodigoEvento

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCodigoVerificacao
class tpCodigoVerificacao (pyxb.binding.datatypes.string):

    """Tipo Código de verificação da NF-e.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCodigoVerificacao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 256, 1)
    _Documentation = 'Tipo Código de verificação da NF-e.\n\t\t\t'
tpCodigoVerificacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
tpCodigoVerificacao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tpCodigoVerificacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpCodigoVerificacao._InitializeFacetMap(tpCodigoVerificacao._CF_maxLength,
   tpCodigoVerificacao._CF_minLength,
   tpCodigoVerificacao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpCodigoVerificacao', tpCodigoVerificacao)
_module_typeBindings.tpCodigoVerificacao = tpCodigoVerificacao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpComplementoEndereco
class tpComplementoEndereco (pyxb.binding.datatypes.string):

    """Tipo complemento do endereço.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpComplementoEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 267, 1)
    _Documentation = 'Tipo complemento do endereço.\n\t\t\t'
tpComplementoEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
tpComplementoEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpComplementoEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpComplementoEndereco._InitializeFacetMap(tpComplementoEndereco._CF_maxLength,
   tpComplementoEndereco._CF_minLength,
   tpComplementoEndereco._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpComplementoEndereco', tpComplementoEndereco)
_module_typeBindings.tpComplementoEndereco = tpComplementoEndereco

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpMotivoRetencao
class tpMotivoRetencao (pyxb.binding.datatypes.string):

    """Tipo Motivo da Retenção."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpMotivoRetencao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 278, 1)
    _Documentation = 'Tipo Motivo da Retenção.'
tpMotivoRetencao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
tpMotivoRetencao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpMotivoRetencao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpMotivoRetencao._InitializeFacetMap(tpMotivoRetencao._CF_maxLength,
   tpMotivoRetencao._CF_minLength,
   tpMotivoRetencao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpMotivoRetencao', tpMotivoRetencao)
_module_typeBindings.tpMotivoRetencao = tpMotivoRetencao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpCPF
class tpCPF (pyxb.binding.datatypes.string):

    """Tipo CPF."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCPF')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 288, 1)
    _Documentation = 'Tipo CPF.'
tpCPF._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCPF._CF_pattern.addPattern(pattern='[0-9]{0}|[0-9]{11}')
tpCPF._InitializeFacetMap(tpCPF._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCPF', tpCPF)
_module_typeBindings.tpCPF = tpCPF

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpDocTomadorEstrangeiro
class tpDocTomadorEstrangeiro (pyxb.binding.datatypes.string):

    """Indentificação de Tomador Estrangeiro."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDocTomadorEstrangeiro')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 296, 1)
    _Documentation = 'Indentificação de Tomador Estrangeiro.'
tpDocTomadorEstrangeiro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
tpDocTomadorEstrangeiro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpDocTomadorEstrangeiro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpDocTomadorEstrangeiro._InitializeFacetMap(tpDocTomadorEstrangeiro._CF_maxLength,
   tpDocTomadorEstrangeiro._CF_minLength,
   tpDocTomadorEstrangeiro._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpDocTomadorEstrangeiro', tpDocTomadorEstrangeiro)
_module_typeBindings.tpDocTomadorEstrangeiro = tpDocTomadorEstrangeiro

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpData
class tpData (pyxb.binding.datatypes.date):

    """Tipo padrão data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpData')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 306, 1)
    _Documentation = 'Tipo padrão data.'
tpData._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpData._InitializeFacetMap(tpData._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpData', tpData)
_module_typeBindings.tpData = tpData

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpDataHora
class tpDataHora (pyxb.binding.datatypes.dateTime):

    """Tipo padrão data e hora."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDataHora')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 321, 1)
    _Documentation = 'Tipo padrão data e hora.'
tpDataHora._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tpDataHora', tpDataHora)
_module_typeBindings.tpDataHora = tpDataHora

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpDeducaoPor
class tpDeducaoPor (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo que representa o modo de Dedução.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDeducaoPor')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 334, 1)
    _Documentation = 'Tipo que representa o modo de Dedução.\n\t\t\t'
tpDeducaoPor._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpDeducaoPor, enum_prefix=None)
tpDeducaoPor.Valor = tpDeducaoPor._CF_enumeration.addEnumeration(unicode_value='Valor', tag='Valor')
tpDeducaoPor.Percentual = tpDeducaoPor._CF_enumeration.addEnumeration(unicode_value='Percentual', tag='Percentual')
tpDeducaoPor._InitializeFacetMap(tpDeducaoPor._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpDeducaoPor', tpDeducaoPor)
_module_typeBindings.tpDeducaoPor = tpDeducaoPor

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpTipoDeducao
class tpTipoDeducao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo que representa as descrições das deduções
				permitidas."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTipoDeducao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 355, 1)
    _Documentation = 'Tipo que representa as descrições das deduções\n\t\t\t\tpermitidas.'
tpTipoDeducao._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpTipoDeducao, enum_prefix=None)
tpTipoDeducao.Despesas_com_Materiais = tpTipoDeducao._CF_enumeration.addEnumeration(unicode_value='Despesas com Materiais', tag='Despesas_com_Materiais')
tpTipoDeducao.Despesas_com_Subempreitada = tpTipoDeducao._CF_enumeration.addEnumeration(unicode_value='Despesas com Subempreitada', tag='Despesas_com_Subempreitada')
tpTipoDeducao.Despesas_com_Mercadorias = tpTipoDeducao._CF_enumeration.addEnumeration(unicode_value='Despesas com Mercadorias', tag='Despesas_com_Mercadorias')
tpTipoDeducao.Servicos_de_Veiculacao_e_Divulgacao = tpTipoDeducao._CF_enumeration.addEnumeration(unicode_value='Servicos de Veiculacao e Divulgacao', tag='Servicos_de_Veiculacao_e_Divulgacao')
tpTipoDeducao.Servicos = tpTipoDeducao._CF_enumeration.addEnumeration(unicode_value='Servicos', tag='Servicos')
tpTipoDeducao.Mapa_de_Const__Civil = tpTipoDeducao._CF_enumeration.addEnumeration(unicode_value='Mapa de Const. Civil', tag='Mapa_de_Const__Civil')
tpTipoDeducao.emptyString = tpTipoDeducao._CF_enumeration.addEnumeration(unicode_value='', tag='emptyString')
tpTipoDeducao._InitializeFacetMap(tpTipoDeducao._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpTipoDeducao', tpTipoDeducao)
_module_typeBindings.tpTipoDeducao = tpTipoDeducao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpDescricaoEvento
class tpDescricaoEvento (pyxb.binding.datatypes.string):

    """Tipo descrição do evento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDescricaoEvento')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 405, 1)
    _Documentation = 'Tipo descrição do evento.'
tpDescricaoEvento._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(300))
tpDescricaoEvento._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpDescricaoEvento._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpDescricaoEvento._InitializeFacetMap(tpDescricaoEvento._CF_maxLength,
   tpDescricaoEvento._CF_minLength,
   tpDescricaoEvento._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpDescricaoEvento', tpDescricaoEvento)
_module_typeBindings.tpDescricaoEvento = tpDescricaoEvento

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpItemTributavel
class tpItemTributavel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Informa se o Item de serviço é tributavel ou
				nao"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpItemTributavel')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 415, 1)
    _Documentation = 'Informa se o Item de serviço é tributavel ou\n\t\t\t\tnao'
tpItemTributavel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpItemTributavel, enum_prefix=None)
tpItemTributavel.S = tpItemTributavel._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
tpItemTributavel.N = tpItemTributavel._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
tpItemTributavel._InitializeFacetMap(tpItemTributavel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpItemTributavel', tpItemTributavel)
_module_typeBindings.tpItemTributavel = tpItemTributavel

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpDiscriminacao
class tpDiscriminacao (pyxb.binding.datatypes.string):

    """Tipo Discriminação Serviços."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDiscriminacao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 434, 1)
    _Documentation = 'Tipo Discriminação Serviços.'
tpDiscriminacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(250))
tpDiscriminacao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tpDiscriminacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpDiscriminacao._InitializeFacetMap(tpDiscriminacao._CF_maxLength,
   tpDiscriminacao._CF_minLength,
   tpDiscriminacao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpDiscriminacao', tpDiscriminacao)
_module_typeBindings.tpDiscriminacao = tpDiscriminacao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpDescricaoRPS
class tpDescricaoRPS (pyxb.binding.datatypes.string):

    """Tipo Descricao do RPS."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDescricaoRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 444, 1)
    _Documentation = 'Tipo Descricao do RPS.'
tpDescricaoRPS._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1500))
tpDescricaoRPS._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpDescricaoRPS._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpDescricaoRPS._InitializeFacetMap(tpDescricaoRPS._CF_maxLength,
   tpDescricaoRPS._CF_minLength,
   tpDescricaoRPS._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpDescricaoRPS', tpDescricaoRPS)
_module_typeBindings.tpDescricaoRPS = tpDescricaoRPS

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpEmail
class tpEmail (pyxb.binding.datatypes.string):

    """Tipo E-mail."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpEmail')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 454, 1)
    _Documentation = 'Tipo E-mail.'
tpEmail._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
tpEmail._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpEmail._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpEmail._InitializeFacetMap(tpEmail._CF_maxLength,
   tpEmail._CF_minLength,
   tpEmail._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpEmail', tpEmail)
_module_typeBindings.tpEmail = tpEmail

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpInscricaoEstadual
class tpInscricaoEstadual (pyxb.binding.datatypes.long):

    """Tipo Inscrição Estadual."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpInscricaoEstadual')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 465, 1)
    _Documentation = 'Tipo Inscrição Estadual.'
tpInscricaoEstadual._CF_pattern = pyxb.binding.facets.CF_pattern()
tpInscricaoEstadual._CF_pattern.addPattern(pattern='[0-9]{1,19}')
tpInscricaoEstadual._InitializeFacetMap(tpInscricaoEstadual._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpInscricaoEstadual', tpInscricaoEstadual)
_module_typeBindings.tpInscricaoEstadual = tpInscricaoEstadual

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpInscricaoMunicipal
class tpInscricaoMunicipal (pyxb.binding.datatypes.long):

    """Tipo inscrição municipal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpInscricaoMunicipal')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 473, 1)
    _Documentation = 'Tipo inscrição municipal.'
tpInscricaoMunicipal._CF_pattern = pyxb.binding.facets.CF_pattern()
tpInscricaoMunicipal._CF_pattern.addPattern(pattern='[0-9]{6,11}')
tpInscricaoMunicipal._InitializeFacetMap(tpInscricaoMunicipal._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpInscricaoMunicipal', tpInscricaoMunicipal)
_module_typeBindings.tpInscricaoMunicipal = tpInscricaoMunicipal

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpRazaoSocialPrestador
class tpRazaoSocialPrestador (pyxb.binding.datatypes.string):

    """Razao social."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpRazaoSocialPrestador')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 487, 1)
    _Documentation = 'Razao social.'
tpRazaoSocialPrestador._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
tpRazaoSocialPrestador._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tpRazaoSocialPrestador._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpRazaoSocialPrestador._InitializeFacetMap(tpRazaoSocialPrestador._CF_maxLength,
   tpRazaoSocialPrestador._CF_minLength,
   tpRazaoSocialPrestador._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpRazaoSocialPrestador', tpRazaoSocialPrestador)
_module_typeBindings.tpRazaoSocialPrestador = tpRazaoSocialPrestador

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpLogradouro
class tpLogradouro (pyxb.binding.datatypes.string):

    """Endereço."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpLogradouro')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 498, 1)
    _Documentation = 'Endereço.'
tpLogradouro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
tpLogradouro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpLogradouro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpLogradouro._InitializeFacetMap(tpLogradouro._CF_maxLength,
   tpLogradouro._CF_minLength,
   tpLogradouro._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpLogradouro', tpLogradouro)
_module_typeBindings.tpLogradouro = tpLogradouro

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpMoeda
class tpMoeda (pyxb.binding.datatypes.decimal):

    """Tipo utilizado para valores com 15 dígitos,
				sendo 13 de corpo e 2 decimais."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpMoeda')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 508, 1)
    _Documentation = 'Tipo utilizado para valores com 15 dígitos,\n\t\t\t\tsendo 13 de corpo e 2 decimais.'
tpMoeda._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tpMoeda._CF_pattern = pyxb.binding.facets.CF_pattern()
tpMoeda._CF_pattern.addPattern(pattern='[0-9]{0,12}(\\.[0-9]{0,2})')
tpMoeda._InitializeFacetMap(tpMoeda._CF_fractionDigits,
   tpMoeda._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpMoeda', tpMoeda)
_module_typeBindings.tpMoeda = tpMoeda

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpMotivoPagamento
class tpMotivoPagamento (pyxb.binding.datatypes.string):

    """Motivo do Pagamento caso ISS Retido tenha
				sido Recolhido pelo Prestador."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpMotivoPagamento')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 518, 1)
    _Documentation = 'Motivo do Pagamento caso ISS Retido tenha\n\t\t\t\tsido Recolhido pelo Prestador.'
tpMotivoPagamento._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
tpMotivoPagamento._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpMotivoPagamento._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpMotivoPagamento._InitializeFacetMap(tpMotivoPagamento._CF_maxLength,
   tpMotivoPagamento._CF_minLength,
   tpMotivoPagamento._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpMotivoPagamento', tpMotivoPagamento)
_module_typeBindings.tpMotivoPagamento = tpMotivoPagamento

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpNumero
class tpNumero (pyxb.binding.datatypes.long):

    """Tipo número."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNumero')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 529, 1)
    _Documentation = 'Tipo número.'
tpNumero._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpNumero, value=pyxb.binding.datatypes.long(0))
tpNumero._CF_pattern = pyxb.binding.facets.CF_pattern()
tpNumero._CF_pattern.addPattern(pattern='[0-9]{1,12}')
tpNumero._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=tpNumero, value=pyxb.binding.datatypes.long(2147483647))
tpNumero._InitializeFacetMap(tpNumero._CF_minInclusive,
   tpNumero._CF_pattern,
   tpNumero._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'tpNumero', tpNumero)
_module_typeBindings.tpNumero = tpNumero

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpNumeroComZero
class tpNumeroComZero (pyxb.binding.datatypes.long):

    """Tipo número."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNumeroComZero')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 539, 1)
    _Documentation = 'Tipo número.'
tpNumeroComZero._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpNumeroComZero, value=pyxb.binding.datatypes.long(0))
tpNumeroComZero._CF_pattern = pyxb.binding.facets.CF_pattern()
tpNumeroComZero._CF_pattern.addPattern(pattern='[0-9]{1,12}')
tpNumeroComZero._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=tpNumeroComZero, value=pyxb.binding.datatypes.long(2147483647))
tpNumeroComZero._InitializeFacetMap(tpNumeroComZero._CF_minInclusive,
   tpNumeroComZero._CF_pattern,
   tpNumeroComZero._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'tpNumeroComZero', tpNumeroComZero)
_module_typeBindings.tpNumeroComZero = tpNumeroComZero

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpNumeroNFReferencia
class tpNumeroNFReferencia (pyxb.binding.datatypes.long):

    """Número da Nota Fiscal Referência.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNumeroNFReferencia')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 549, 1)
    _Documentation = 'Número da Nota Fiscal Referência.\n\t\t\t'
tpNumeroNFReferencia._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpNumeroNFReferencia, value=pyxb.binding.datatypes.long(0))
tpNumeroNFReferencia._CF_pattern = pyxb.binding.facets.CF_pattern()
tpNumeroNFReferencia._CF_pattern.addPattern(pattern='[0-9]{1,10}')
tpNumeroNFReferencia._InitializeFacetMap(tpNumeroNFReferencia._CF_minInclusive,
   tpNumeroNFReferencia._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpNumeroNFReferencia', tpNumeroNFReferencia)
_module_typeBindings.tpNumeroNFReferencia = tpNumeroNFReferencia

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpNumeroEndereco
class tpNumeroEndereco (pyxb.binding.datatypes.string):

    """Tipo número do endereço."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNumeroEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 561, 1)
    _Documentation = 'Tipo número do endereço.'
tpNumeroEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
tpNumeroEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpNumeroEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpNumeroEndereco._InitializeFacetMap(tpNumeroEndereco._CF_maxLength,
   tpNumeroEndereco._CF_minLength,
   tpNumeroEndereco._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpNumeroEndereco', tpNumeroEndereco)
_module_typeBindings.tpNumeroEndereco = tpNumeroEndereco

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpOpcaoSimples
class tpOpcaoSimples (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente às possíveis opções de escolha
				pelo Simples."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpOpcaoSimples')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 571, 1)
    _Documentation = 'Tipo referente às possíveis opções de escolha\n\t\t\t\tpelo Simples.'
tpOpcaoSimples._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpOpcaoSimples, enum_prefix=None)
tpOpcaoSimples.n0 = tpOpcaoSimples._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
tpOpcaoSimples.n1 = tpOpcaoSimples._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
tpOpcaoSimples.n2 = tpOpcaoSimples._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
tpOpcaoSimples.n3 = tpOpcaoSimples._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
tpOpcaoSimples._InitializeFacetMap(tpOpcaoSimples._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpOpcaoSimples', tpOpcaoSimples)
_module_typeBindings.tpOpcaoSimples = tpOpcaoSimples

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpOperacao
class tpOperacao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo Operação."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpOperacao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 601, 1)
    _Documentation = 'Tipo Operação.'
tpOperacao._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpOperacao, enum_prefix=None)
tpOperacao.A = tpOperacao._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
tpOperacao.B = tpOperacao._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
tpOperacao.C = tpOperacao._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
tpOperacao.D = tpOperacao._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
tpOperacao.J = tpOperacao._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
tpOperacao._InitializeFacetMap(tpOperacao._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpOperacao', tpOperacao)
_module_typeBindings.tpOperacao = tpOperacao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpPercentual
class tpPercentual (pyxb.binding.datatypes.decimal):

    """Tipo padrão para índices percentuais."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpPercentual')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 635, 1)
    _Documentation = 'Tipo padrão para índices percentuais.'
tpPercentual._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpPercentual, value=pyxb.binding.datatypes.decimal('0.0'))
tpPercentual._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tpPercentual._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5))
tpPercentual._InitializeFacetMap(tpPercentual._CF_minInclusive,
   tpPercentual._CF_fractionDigits,
   tpPercentual._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tpPercentual', tpPercentual)
_module_typeBindings.tpPercentual = tpPercentual

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpQuantidade
class tpQuantidade (pyxb.binding.datatypes.decimal):

    """Tipo padrão para quantidades."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpQuantidade')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 645, 1)
    _Documentation = 'Tipo padrão para quantidades.'
tpQuantidade._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpQuantidade, value=pyxb.binding.datatypes.decimal('0.0'))
tpQuantidade._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4))
tpQuantidade._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(10))
tpQuantidade._InitializeFacetMap(tpQuantidade._CF_minInclusive,
   tpQuantidade._CF_fractionDigits,
   tpQuantidade._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tpQuantidade', tpQuantidade)
_module_typeBindings.tpQuantidade = tpQuantidade

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpRazaoSocial
class tpRazaoSocial (pyxb.binding.datatypes.string):

    """Tipo Razão Social."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpRazaoSocial')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 655, 1)
    _Documentation = 'Tipo Razão Social.'
tpRazaoSocial._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
tpRazaoSocial._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tpRazaoSocial._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpRazaoSocial._InitializeFacetMap(tpRazaoSocial._CF_maxLength,
   tpRazaoSocial._CF_minLength,
   tpRazaoSocial._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpRazaoSocial', tpRazaoSocial)
_module_typeBindings.tpRazaoSocial = tpRazaoSocial

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpSerieRPS
class tpSerieRPS (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo série de documento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpSerieRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 665, 1)
    _Documentation = 'Tipo série de documento.'
tpSerieRPS._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpSerieRPS, enum_prefix=None)
tpSerieRPS.NF = tpSerieRPS._CF_enumeration.addEnumeration(unicode_value='NF', tag='NF')
tpSerieRPS._InitializeFacetMap(tpSerieRPS._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpSerieRPS', tpSerieRPS)
_module_typeBindings.tpSerieRPS = tpSerieRPS

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpSituacaoRPS
class tpSituacaoRPS (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente aos possíveis status de RPS."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpSituacaoRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 684, 1)
    _Documentation = 'Tipo referente aos possíveis status de RPS.'
tpSituacaoRPS._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpSituacaoRPS, enum_prefix=None)
tpSituacaoRPS.N = tpSituacaoRPS._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
tpSituacaoRPS.C = tpSituacaoRPS._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
tpSituacaoRPS._InitializeFacetMap(tpSituacaoRPS._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpSituacaoRPS', tpSituacaoRPS)
_module_typeBindings.tpSituacaoRPS = tpSituacaoRPS

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpStatusNFe
class tpStatusNFe (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente aos possíveis status de NFSe."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpStatusNFe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 701, 1)
    _Documentation = 'Tipo referente aos possíveis status de NFSe.'
tpStatusNFe._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpStatusNFe, enum_prefix=None)
tpStatusNFe.n1 = tpStatusNFe._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
tpStatusNFe.n2 = tpStatusNFe._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
tpStatusNFe.n3 = tpStatusNFe._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
tpStatusNFe._InitializeFacetMap(tpStatusNFe._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpStatusNFe', tpStatusNFe)
_module_typeBindings.tpStatusNFe = tpStatusNFe

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpSucesso
class tpSucesso (pyxb.binding.datatypes.boolean):

    """Tipo que indica se o pedido do serviço obteve sucesso."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpSucesso')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 723, 1)
    _Documentation = 'Tipo que indica se o pedido do serviço obteve sucesso.'
tpSucesso._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tpSucesso', tpSucesso)
_module_typeBindings.tpSucesso = tpSucesso

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpTempoProcessamento
class tpTempoProcessamento (pyxb.binding.datatypes.long):

    """Tipo referente ao tempo de processamento do lote."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTempoProcessamento')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 729, 1)
    _Documentation = 'Tipo referente ao tempo de processamento do lote.'
tpTempoProcessamento._CF_pattern = pyxb.binding.facets.CF_pattern()
tpTempoProcessamento._CF_pattern.addPattern(pattern='[0-9]{1,15}')
tpTempoProcessamento._InitializeFacetMap(tpTempoProcessamento._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpTempoProcessamento', tpTempoProcessamento)
_module_typeBindings.tpTempoProcessamento = tpTempoProcessamento

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpAssincrono
class tpAssincrono (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo de processamento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpAssincrono')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 737, 1)
    _Documentation = 'Tipo de processamento.'
tpAssincrono._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpAssincrono, enum_prefix=None)
tpAssincrono.S = tpAssincrono._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
tpAssincrono.N = tpAssincrono._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
tpAssincrono._InitializeFacetMap(tpAssincrono._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpAssincrono', tpAssincrono)
_module_typeBindings.tpAssincrono = tpAssincrono

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpTipoBairro
class tpTipoBairro (pyxb.binding.datatypes.string):

    """Tipo do Bairro (Bairro, Vila, ...)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTipoBairro')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 754, 1)
    _Documentation = 'Tipo do Bairro (Bairro, Vila, ...).'
tpTipoBairro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
tpTipoBairro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpTipoBairro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpTipoBairro._InitializeFacetMap(tpTipoBairro._CF_maxLength,
   tpTipoBairro._CF_minLength,
   tpTipoBairro._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpTipoBairro', tpTipoBairro)
_module_typeBindings.tpTipoBairro = tpTipoBairro

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpTipoLogradouro
class tpTipoLogradouro (pyxb.binding.datatypes.string):

    """Tipo do endereço (Rua, Av, ...)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTipoLogradouro')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 764, 1)
    _Documentation = 'Tipo do endereço (Rua, Av, ...).'
tpTipoLogradouro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
tpTipoLogradouro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpTipoLogradouro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpTipoLogradouro._InitializeFacetMap(tpTipoLogradouro._CF_maxLength,
   tpTipoLogradouro._CF_minLength,
   tpTipoLogradouro._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpTipoLogradouro', tpTipoLogradouro)
_module_typeBindings.tpTipoLogradouro = tpTipoLogradouro

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpTipoRecolhimento
class tpTipoRecolhimento (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente ao recolhimento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTipoRecolhimento')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 774, 1)
    _Documentation = 'Tipo referente ao recolhimento.'
tpTipoRecolhimento._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpTipoRecolhimento, enum_prefix=None)
tpTipoRecolhimento.A = tpTipoRecolhimento._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
tpTipoRecolhimento.R = tpTipoRecolhimento._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
tpTipoRecolhimento._InitializeFacetMap(tpTipoRecolhimento._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpTipoRecolhimento', tpTipoRecolhimento)
_module_typeBindings.tpTipoRecolhimento = tpTipoRecolhimento

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpTipoRPS
class tpTipoRPS (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente aos possíveis tipos de RPS."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTipoRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 791, 1)
    _Documentation = 'Tipo referente aos possíveis tipos de RPS.'
tpTipoRPS._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpTipoRPS, enum_prefix=None)
tpTipoRPS.RPS = tpTipoRPS._CF_enumeration.addEnumeration(unicode_value='RPS', tag='RPS')
tpTipoRPS._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
tpTipoRPS._InitializeFacetMap(tpTipoRPS._CF_enumeration,
   tpTipoRPS._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tpTipoRPS', tpTipoRPS)
_module_typeBindings.tpTipoRPS = tpTipoRPS

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpSeriePrestacao
class tpSeriePrestacao (pyxb.binding.datatypes.byte):

    """Tipo serie de Prestacao."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpSeriePrestacao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 804, 2)
    _Documentation = 'Tipo serie de Prestacao.'
tpSeriePrestacao._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpSeriePrestacao, value=pyxb.binding.datatypes.byte(1))
tpSeriePrestacao._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=tpSeriePrestacao, value=pyxb.binding.datatypes.byte(99))
tpSeriePrestacao._InitializeFacetMap(tpSeriePrestacao._CF_minInclusive,
   tpSeriePrestacao._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'tpSeriePrestacao', tpSeriePrestacao)
_module_typeBindings.tpSeriePrestacao = tpSeriePrestacao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpTributacao
class tpTributacao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente aos modos de tributação."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTributacao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 813, 1)
    _Documentation = 'Tipo referente aos modos de tributação.'
tpTributacao._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpTributacao, enum_prefix=None)
tpTributacao.C = tpTributacao._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
tpTributacao.F = tpTributacao._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
tpTributacao.K = tpTributacao._CF_enumeration.addEnumeration(unicode_value='K', tag='K')
tpTributacao.E = tpTributacao._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
tpTributacao.T = tpTributacao._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
tpTributacao.H = tpTributacao._CF_enumeration.addEnumeration(unicode_value='H', tag='H')
tpTributacao.G = tpTributacao._CF_enumeration.addEnumeration(unicode_value='G', tag='G')
tpTributacao.N = tpTributacao._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
tpTributacao.M = tpTributacao._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
tpTributacao._InitializeFacetMap(tpTributacao._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpTributacao', tpTributacao)
_module_typeBindings.tpTributacao = tpTributacao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpTributacaoNFe
class tpTributacaoNFe (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo referente aos modos de tributação da NFe."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpTributacaoNFe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 865, 1)
    _Documentation = 'Tipo referente aos modos de tributação da NFe.'
tpTributacaoNFe._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpTributacaoNFe, enum_prefix=None)
tpTributacaoNFe.T = tpTributacaoNFe._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
tpTributacaoNFe.F = tpTributacaoNFe._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
tpTributacaoNFe.I = tpTributacaoNFe._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
tpTributacaoNFe.J = tpTributacaoNFe._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
tpTributacaoNFe._InitializeFacetMap(tpTributacaoNFe._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tpTributacaoNFe', tpTributacaoNFe)
_module_typeBindings.tpTributacaoNFe = tpTributacaoNFe

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpUF
class tpUF (pyxb.binding.datatypes.string):

    """Tipo UF."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpUF')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 892, 1)
    _Documentation = 'Tipo UF.'
tpUF._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tpUF._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tpUF._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tpUF._InitializeFacetMap(tpUF._CF_maxLength,
   tpUF._CF_minLength,
   tpUF._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpUF', tpUF)
_module_typeBindings.tpUF = tpUF

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpValor
class tpValor (pyxb.binding.datatypes.decimal):

    """Tipo utilizado para valores com 15 dígitos, sendo 13 de corpo e 2 decimais."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpValor')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 902, 1)
    _Documentation = 'Tipo utilizado para valores com 15 dígitos, sendo 13 de corpo e 2 decimais.'
tpValor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpValor, value=pyxb.binding.datatypes.decimal('0.0'))
tpValor._CF_pattern = pyxb.binding.facets.CF_pattern()
tpValor._CF_pattern.addPattern(pattern='0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\\.[0-9]{0,2})?')
tpValor._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tpValor._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15))
tpValor._InitializeFacetMap(tpValor._CF_minInclusive,
   tpValor._CF_pattern,
   tpValor._CF_fractionDigits,
   tpValor._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tpValor', tpValor)
_module_typeBindings.tpValor = tpValor

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpValor4d
class tpValor4d (pyxb.binding.datatypes.decimal):

    """Tipo utilizado para valores com 15 dígitos, sendo 13 de corpo e 4 decimais."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpValor4d')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 913, 1)
    _Documentation = 'Tipo utilizado para valores com 15 dígitos, sendo 13 de corpo e 4 decimais.'
tpValor4d._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=tpValor4d, value=pyxb.binding.datatypes.decimal('0.0'))
tpValor4d._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4))
tpValor4d._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15))
tpValor4d._InitializeFacetMap(tpValor4d._CF_minInclusive,
   tpValor4d._CF_fractionDigits,
   tpValor4d._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tpValor4d', tpValor4d)
_module_typeBindings.tpValor4d = tpValor4d

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpVersao
class tpVersao (pyxb.binding.datatypes.long):

    """Tipo Versão do Schema."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpVersao')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 923, 1)
    _Documentation = 'Tipo Versão do Schema.'
tpVersao._CF_pattern = pyxb.binding.facets.CF_pattern()
tpVersao._CF_pattern.addPattern(pattern='[0-9]{1,3}')
tpVersao._InitializeFacetMap(tpVersao._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpVersao', tpVersao)
_module_typeBindings.tpVersao = tpVersao

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpMotCancelamento
class tpMotCancelamento (pyxb.binding.datatypes.string):

    """Motivo do Cancelamento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpMotCancelamento')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 982, 1)
    _Documentation = 'Motivo do Cancelamento.'
tpMotCancelamento._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(80))
tpMotCancelamento._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
tpMotCancelamento._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
tpMotCancelamento._InitializeFacetMap(tpMotCancelamento._CF_maxLength,
   tpMotCancelamento._CF_minLength,
   tpMotCancelamento._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'tpMotCancelamento', tpMotCancelamento)
_module_typeBindings.tpMotCancelamento = tpMotCancelamento

# Atomic simple type: {http://localhost:8080/WsNFe2/tp}tpDDD
class tpDDD (pyxb.binding.datatypes.long):

    """DDD."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDDD')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1315, 1)
    _Documentation = 'DDD.'
tpDDD._CF_pattern = pyxb.binding.facets.CF_pattern()
tpDDD._CF_pattern.addPattern(pattern='[0-9]{0,3}')
tpDDD._InitializeFacetMap(tpDDD._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpDDD', tpDDD)
_module_typeBindings.tpDDD = tpDDD

# Union simple type: {http://localhost:8080/WsNFe2/tp}numTam8TipoNulo
# superclasses pyxb.binding.datatypes.anySimpleType
class numTam8TipoNulo (pyxb.binding.basis.STD_union):

    """Sequencial numérico com até 8 posições.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'numTam8TipoNulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 63, 1)
    _Documentation = 'Sequencial numérico com até 8 posições.\n\t\t\t'

    _MemberTypes = ( numTam8Tipo, nulo, )
numTam8TipoNulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=numTam8TipoNulo)
numTam8TipoNulo._CF_pattern = pyxb.binding.facets.CF_pattern()
numTam8TipoNulo.emptyString = ''                  # originally nulo.emptyString
numTam8TipoNulo._InitializeFacetMap(numTam8TipoNulo._CF_enumeration,
   numTam8TipoNulo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'numTam8TipoNulo', numTam8TipoNulo)
_module_typeBindings.numTam8TipoNulo = numTam8TipoNulo

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpCEPNulo
# superclasses pyxb.binding.datatypes.anySimpleType
class tpCEPNulo (pyxb.binding.basis.STD_union):

    """Tipo CEP."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCEPNulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 173, 1)
    _Documentation = 'Tipo CEP.'

    _MemberTypes = ( tpCEP, nulo, )
tpCEPNulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpCEPNulo)
tpCEPNulo._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCEPNulo.emptyString = ''                        # originally nulo.emptyString
tpCEPNulo._InitializeFacetMap(tpCEPNulo._CF_enumeration,
   tpCEPNulo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCEPNulo', tpCEPNulo)
_module_typeBindings.tpCEPNulo = tpCEPNulo

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpCPFCNPJnulo
# superclasses pyxb.binding.datatypes.anySimpleType
class tpCPFCNPJnulo (pyxb.binding.basis.STD_union):

    """Tipo CPFCNPJ permitindo valor nulo.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCPFCNPJnulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 224, 1)
    _Documentation = 'Tipo CPFCNPJ permitindo valor nulo.\n\t\t\t'

    _MemberTypes = ( tpCPFCNPJ, nulo, )
tpCPFCNPJnulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpCPFCNPJnulo)
tpCPFCNPJnulo._CF_pattern = pyxb.binding.facets.CF_pattern()
tpCPFCNPJnulo.emptyString = ''                    # originally nulo.emptyString
tpCPFCNPJnulo._InitializeFacetMap(tpCPFCNPJnulo._CF_enumeration,
   tpCPFCNPJnulo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpCPFCNPJnulo', tpCPFCNPJnulo)
_module_typeBindings.tpCPFCNPJnulo = tpCPFCNPJnulo

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpDataNulo
# superclasses pyxb.binding.datatypes.anySimpleType
class tpDataNulo (pyxb.binding.basis.STD_union):

    """Tipo padrão data aceitando valor nulo.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDataNulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 314, 1)
    _Documentation = 'Tipo padrão data aceitando valor nulo.\n\t\t\t'

    _MemberTypes = ( tpData, nulo, )
tpDataNulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpDataNulo)
tpDataNulo._CF_pattern = pyxb.binding.facets.CF_pattern()
tpDataNulo.emptyString = ''                       # originally nulo.emptyString
tpDataNulo._InitializeFacetMap(tpDataNulo._CF_enumeration,
   tpDataNulo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpDataNulo', tpDataNulo)
_module_typeBindings.tpDataNulo = tpDataNulo

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpDataHoraNulo
# superclasses pyxb.binding.datatypes.anySimpleType
class tpDataHoraNulo (pyxb.binding.basis.STD_union):

    """Tipo padrão data e hora aceitando valor nulo.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDataHoraNulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 327, 1)
    _Documentation = 'Tipo padrão data e hora aceitando valor nulo.\n\t\t\t'

    _MemberTypes = ( tpDataHora, nulo, )
tpDataHoraNulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpDataHoraNulo)
tpDataHoraNulo._CF_pattern = pyxb.binding.facets.CF_pattern()
tpDataHoraNulo.emptyString = ''                   # originally nulo.emptyString
tpDataHoraNulo._InitializeFacetMap(tpDataHoraNulo._CF_enumeration,
   tpDataHoraNulo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpDataHoraNulo', tpDataHoraNulo)
_module_typeBindings.tpDataHoraNulo = tpDataHoraNulo

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpInscricaoMunicipalNulo
# superclasses pyxb.binding.datatypes.anySimpleType
class tpInscricaoMunicipalNulo (pyxb.binding.basis.STD_union):

    """Tipo inscrição municipal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpInscricaoMunicipalNulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 481, 1)
    _Documentation = 'Tipo inscrição municipal.'

    _MemberTypes = ( tpInscricaoMunicipal, nulo, )
tpInscricaoMunicipalNulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpInscricaoMunicipalNulo)
tpInscricaoMunicipalNulo._CF_pattern = pyxb.binding.facets.CF_pattern()
tpInscricaoMunicipalNulo.emptyString = ''         # originally nulo.emptyString
tpInscricaoMunicipalNulo._InitializeFacetMap(tpInscricaoMunicipalNulo._CF_enumeration,
   tpInscricaoMunicipalNulo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpInscricaoMunicipalNulo', tpInscricaoMunicipalNulo)
_module_typeBindings.tpInscricaoMunicipalNulo = tpInscricaoMunicipalNulo

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpSerieRPSSubstituido
# superclasses pyxb.binding.datatypes.anySimpleType
class tpSerieRPSSubstituido (pyxb.binding.basis.STD_union):

    """Tipo série de documento."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpSerieRPSSubstituido')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 678, 1)
    _Documentation = 'Tipo série de documento.'

    _MemberTypes = ( tpSerieRPS, nulo, )
tpSerieRPSSubstituido._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpSerieRPSSubstituido)
tpSerieRPSSubstituido._CF_pattern = pyxb.binding.facets.CF_pattern()
tpSerieRPSSubstituido.NF = 'NF'                   # originally tpSerieRPS.NF
tpSerieRPSSubstituido.emptyString = ''            # originally nulo.emptyString
tpSerieRPSSubstituido._InitializeFacetMap(tpSerieRPSSubstituido._CF_enumeration,
   tpSerieRPSSubstituido._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpSerieRPSSubstituido', tpSerieRPSSubstituido)
_module_typeBindings.tpSerieRPSSubstituido = tpSerieRPSSubstituido

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpDDDNulo
# superclasses pyxb.binding.datatypes.anySimpleType
class tpDDDNulo (pyxb.binding.basis.STD_union):

    """DDD."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDDDNulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1323, 1)
    _Documentation = 'DDD.'

    _MemberTypes = ( tpDDD, nulo, )
tpDDDNulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpDDDNulo)
tpDDDNulo._CF_pattern = pyxb.binding.facets.CF_pattern()
tpDDDNulo.emptyString = ''                        # originally nulo.emptyString
tpDDDNulo._InitializeFacetMap(tpDDDNulo._CF_enumeration,
   tpDDDNulo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpDDDNulo', tpDDDNulo)
_module_typeBindings.tpDDDNulo = tpDDDNulo

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpFone
# superclasses pyxb.binding.datatypes.anySimpleType
class tpFone (pyxb.binding.basis.STD_union):

    """Telefone."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpFone')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1329, 1)
    _Documentation = 'Telefone.'

    _MemberTypes = ( numTam8Tipo, )
tpFone._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpFone)
tpFone._CF_pattern = pyxb.binding.facets.CF_pattern()
tpFone._InitializeFacetMap(tpFone._CF_enumeration,
   tpFone._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpFone', tpFone)
_module_typeBindings.tpFone = tpFone

# Union simple type: {http://localhost:8080/WsNFe2/tp}tpFoneNulo
# superclasses pyxb.binding.datatypes.anySimpleType
class tpFoneNulo (pyxb.binding.basis.STD_union):

    """Telefone."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpFoneNulo')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1335, 1)
    _Documentation = 'Telefone.'

    _MemberTypes = ( numTam8Tipo, nulo, )
tpFoneNulo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tpFoneNulo)
tpFoneNulo._CF_pattern = pyxb.binding.facets.CF_pattern()
tpFoneNulo.emptyString = ''                       # originally nulo.emptyString
tpFoneNulo._InitializeFacetMap(tpFoneNulo._CF_enumeration,
   tpFoneNulo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tpFoneNulo', tpFoneNulo)
_module_typeBindings.tpFoneNulo = tpFoneNulo

# Complex type {http://localhost:8080/WsNFe2/tp}tpBairroCompleto with content type ELEMENT_ONLY
class tpBairroCompleto (pyxb.binding.basis.complexTypeDefinition):
    """Informações do Bairro com o seu Tipo."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpBairroCompleto')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 932, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TipoBairro uses Python identifier TipoBairro
    __TipoBairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoBairro'), 'TipoBairro', '__httplocalhost8080WsNFe2tp_tpBairroCompleto_TipoBairro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 937, 3), )

    
    TipoBairro = property(__TipoBairro.value, __TipoBairro.set, None, 'Tipo do Bairro (Bairro, Vila etc)')

    
    # Element NomeBairro uses Python identifier NomeBairro
    __NomeBairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NomeBairro'), 'NomeBairro', '__httplocalhost8080WsNFe2tp_tpBairroCompleto_NomeBairro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 942, 3), )

    
    NomeBairro = property(__NomeBairro.value, __NomeBairro.set, None, 'Nome do Bairro.')

    _ElementMap.update({
        __TipoBairro.name() : __TipoBairro,
        __NomeBairro.name() : __NomeBairro
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpBairroCompleto = tpBairroCompleto
Namespace.addCategoryObject('typeBinding', 'tpBairroCompleto', tpBairroCompleto)


# Complex type {http://localhost:8080/WsNFe2/tp}tpEvento with content type ELEMENT_ONLY
class tpEvento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://localhost:8080/WsNFe2/tp}tpEvento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpEvento')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 949, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Codigo'), 'Codigo', '__httplocalhost8080WsNFe2tp_tpEvento_Codigo', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 951, 3), )

    
    Codigo = property(__Codigo.value, __Codigo.set, None, 'Código do evento.')

    
    # Element Descricao uses Python identifier Descricao
    __Descricao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Descricao'), 'Descricao', '__httplocalhost8080WsNFe2tp_tpEvento_Descricao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 956, 3), )

    
    Descricao = property(__Descricao.value, __Descricao.set, None, 'Descrição do enveto.')

    
    # Element ChaveRPS uses Python identifier ChaveRPS
    __ChaveRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), 'ChaveRPS', '__httplocalhost8080WsNFe2tp_tpEvento_ChaveRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 961, 3), )

    
    ChaveRPS = property(__ChaveRPS.value, __ChaveRPS.set, None, 'Chave do RPS.')

    
    # Element ChaveNFe uses Python identifier ChaveNFe
    __ChaveNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), 'ChaveNFe', '__httplocalhost8080WsNFe2tp_tpEvento_ChaveNFe', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 966, 3), )

    
    ChaveNFe = property(__ChaveNFe.value, __ChaveNFe.set, None, 'Chave da NFe.')

    _ElementMap.update({
        __Codigo.name() : __Codigo,
        __Descricao.name() : __Descricao,
        __ChaveRPS.name() : __ChaveRPS,
        __ChaveNFe.name() : __ChaveNFe
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpEvento = tpEvento
Namespace.addCategoryObject('typeBinding', 'tpEvento', tpEvento)


# Complex type {http://localhost:8080/WsNFe2/tp}tpCPFCNPJ2 with content type ELEMENT_ONLY
class tpCPFCNPJ2 (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que representa um CPF/CNPJ."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpCPFCNPJ2')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 973, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CPF uses Python identifier CPF
    __CPF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPF'), 'CPF', '__httplocalhost8080WsNFe2tp_tpCPFCNPJ2_CPF', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 978, 3), )

    
    CPF = property(__CPF.value, __CPF.set, None, None)

    
    # Element CNPJ uses Python identifier CNPJ
    __CNPJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CNPJ'), 'CNPJ', '__httplocalhost8080WsNFe2tp_tpCPFCNPJ2_CNPJ', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 979, 3), )

    
    CNPJ = property(__CNPJ.value, __CNPJ.set, None, None)

    _ElementMap.update({
        __CPF.name() : __CPF,
        __CNPJ.name() : __CNPJ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpCPFCNPJ2 = tpCPFCNPJ2
Namespace.addCategoryObject('typeBinding', 'tpCPFCNPJ2', tpCPFCNPJ2)


# Complex type {http://localhost:8080/WsNFe2/tp}tpConsultaNFSe with content type ELEMENT_ONLY
class tpConsultaNFSe (pyxb.binding.basis.complexTypeDefinition):
    """NFSe de retorno de consulta."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpConsultaNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 992, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_InscricaoPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 997, 3), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscrição municipal do prestador de serviços.')

    
    # Element NumeroNFe uses Python identifier NumeroNFe
    __NumeroNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNFe'), 'NumeroNFe', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_NumeroNFe', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1002, 3), )

    
    NumeroNFe = property(__NumeroNFe.value, __NumeroNFe.set, None, 'Número da NF-e.')

    
    # Element CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), 'CodigoVerificacao', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_CodigoVerificacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1007, 3), )

    
    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, 'Código de verificação da NF-e.')

    
    # Element SerieRPS uses Python identifier SerieRPS
    __SerieRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SerieRPS'), 'SerieRPS', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_SerieRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1012, 3), )

    
    SerieRPS = property(__SerieRPS.value, __SerieRPS.set, None, 'Série do RPS.')

    
    # Element NumeroRPS uses Python identifier NumeroRPS
    __NumeroRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), 'NumeroRPS', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_NumeroRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1017, 3), )

    
    NumeroRPS = property(__NumeroRPS.value, __NumeroRPS.set, None, 'Número do RPS.')

    
    # Element DataEmissaoRPS uses Python identifier DataEmissaoRPS
    __DataEmissaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), 'DataEmissaoRPS', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_DataEmissaoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1023, 3), )

    
    DataEmissaoRPS = property(__DataEmissaoRPS.value, __DataEmissaoRPS.set, None, 'Data de Emissão do RPS.')

    
    # Element RazaoSocialPrestador uses Python identifier RazaoSocialPrestador
    __RazaoSocialPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), 'RazaoSocialPrestador', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_RazaoSocialPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1028, 3), )

    
    RazaoSocialPrestador = property(__RazaoSocialPrestador.value, __RazaoSocialPrestador.set, None, 'Razão Social do Prestador do Serviço.')

    
    # Element TipoRecolhimento uses Python identifier TipoRecolhimento
    __TipoRecolhimento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento'), 'TipoRecolhimento', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_TipoRecolhimento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1033, 3), )

    
    TipoRecolhimento = property(__TipoRecolhimento.value, __TipoRecolhimento.set, None, 'Tipo do Recolhimento do Serviço.')

    
    # Element ValorDeduzir uses Python identifier ValorDeduzir
    __ValorDeduzir = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorDeduzir'), 'ValorDeduzir', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_ValorDeduzir', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1038, 3), )

    
    ValorDeduzir = property(__ValorDeduzir.value, __ValorDeduzir.set, None, 'Valor total de deduções.')

    
    # Element ValorTotal uses Python identifier ValorTotal
    __ValorTotal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotal'), 'ValorTotal', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_ValorTotal', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1043, 3), )

    
    ValorTotal = property(__ValorTotal.value, __ValorTotal.set, None, 'Valor total de Itens de Nota.')

    
    # Element Aliquota uses Python identifier Aliquota
    __Aliquota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Aliquota'), 'Aliquota', '__httplocalhost8080WsNFe2tp_tpConsultaNFSe_Aliquota', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1048, 3), )

    
    Aliquota = property(__Aliquota.value, __Aliquota.set, None, 'Valor total de Itens de Nota.')

    _ElementMap.update({
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __NumeroNFe.name() : __NumeroNFe,
        __CodigoVerificacao.name() : __CodigoVerificacao,
        __SerieRPS.name() : __SerieRPS,
        __NumeroRPS.name() : __NumeroRPS,
        __DataEmissaoRPS.name() : __DataEmissaoRPS,
        __RazaoSocialPrestador.name() : __RazaoSocialPrestador,
        __TipoRecolhimento.name() : __TipoRecolhimento,
        __ValorDeduzir.name() : __ValorDeduzir,
        __ValorTotal.name() : __ValorTotal,
        __Aliquota.name() : __Aliquota
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpConsultaNFSe = tpConsultaNFSe
Namespace.addCategoryObject('typeBinding', 'tpConsultaNFSe', tpConsultaNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpChaveNFeRPS with content type ELEMENT_ONLY
class tpChaveNFeRPS (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que representa a chave de uma NFSe e a Chave do RPS que a mesma substitui."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpChaveNFeRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1055, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ChaveNFe uses Python identifier ChaveNFe
    __ChaveNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), 'ChaveNFe', '__httplocalhost8080WsNFe2tp_tpChaveNFeRPS_ChaveNFe', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1060, 3), )

    
    ChaveNFe = property(__ChaveNFe.value, __ChaveNFe.set, None, 'Chave da NFSe gerada.')

    
    # Element ChaveRPS uses Python identifier ChaveRPS
    __ChaveRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), 'ChaveRPS', '__httplocalhost8080WsNFe2tp_tpChaveNFeRPS_ChaveRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1065, 3), )

    
    ChaveRPS = property(__ChaveRPS.value, __ChaveRPS.set, None, 'Chave do RPS substituído.')

    _ElementMap.update({
        __ChaveNFe.name() : __ChaveNFe,
        __ChaveRPS.name() : __ChaveRPS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpChaveNFeRPS = tpChaveNFeRPS
Namespace.addCategoryObject('typeBinding', 'tpChaveNFeRPS', tpChaveNFeRPS)


# Complex type {http://localhost:8080/WsNFe2/tp}tpChaveNFe with content type ELEMENT_ONLY
class tpChaveNFe (pyxb.binding.basis.complexTypeDefinition):
    """Chave de identificação da NF-e."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpChaveNFe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1072, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httplocalhost8080WsNFe2tp_tpChaveNFe_InscricaoPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1077, 3), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscrição municipal do prestador de serviços.')

    
    # Element NumeroNFe uses Python identifier NumeroNFe
    __NumeroNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNFe'), 'NumeroNFe', '__httplocalhost8080WsNFe2tp_tpChaveNFe_NumeroNFe', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1082, 3), )

    
    NumeroNFe = property(__NumeroNFe.value, __NumeroNFe.set, None, 'Número da NF-e.')

    
    # Element CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), 'CodigoVerificacao', '__httplocalhost8080WsNFe2tp_tpChaveNFe_CodigoVerificacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1087, 3), )

    
    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, 'Código de verificação da NF-e.')

    
    # Element RazaoSocialPrestador uses Python identifier RazaoSocialPrestador
    __RazaoSocialPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), 'RazaoSocialPrestador', '__httplocalhost8080WsNFe2tp_tpChaveNFe_RazaoSocialPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1092, 3), )

    
    RazaoSocialPrestador = property(__RazaoSocialPrestador.value, __RazaoSocialPrestador.set, None, 'Razão Social do Prestador do RPS.')

    _ElementMap.update({
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __NumeroNFe.name() : __NumeroNFe,
        __CodigoVerificacao.name() : __CodigoVerificacao,
        __RazaoSocialPrestador.name() : __RazaoSocialPrestador
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpChaveNFe = tpChaveNFe
Namespace.addCategoryObject('typeBinding', 'tpChaveNFe', tpChaveNFe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpChaveRPS with content type ELEMENT_ONLY
class tpChaveRPS (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que define a chave identificadora de um RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpChaveRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1099, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httplocalhost8080WsNFe2tp_tpChaveRPS_InscricaoPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1104, 3), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscrição municipal do prestador de serviços.')

    
    # Element SerieRPS uses Python identifier SerieRPS
    __SerieRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SerieRPS'), 'SerieRPS', '__httplocalhost8080WsNFe2tp_tpChaveRPS_SerieRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1109, 3), )

    
    SerieRPS = property(__SerieRPS.value, __SerieRPS.set, None, 'Série do RPS.')

    
    # Element NumeroRPS uses Python identifier NumeroRPS
    __NumeroRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), 'NumeroRPS', '__httplocalhost8080WsNFe2tp_tpChaveRPS_NumeroRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1114, 3), )

    
    NumeroRPS = property(__NumeroRPS.value, __NumeroRPS.set, None, 'Número do RPS.')

    
    # Element DataEmissaoRPS uses Python identifier DataEmissaoRPS
    __DataEmissaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), 'DataEmissaoRPS', '__httplocalhost8080WsNFe2tp_tpChaveRPS_DataEmissaoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1119, 3), )

    
    DataEmissaoRPS = property(__DataEmissaoRPS.value, __DataEmissaoRPS.set, None, 'Data de Emissao do RPS.')

    
    # Element RazaoSocialPrestador uses Python identifier RazaoSocialPrestador
    __RazaoSocialPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), 'RazaoSocialPrestador', '__httplocalhost8080WsNFe2tp_tpChaveRPS_RazaoSocialPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1124, 3), )

    
    RazaoSocialPrestador = property(__RazaoSocialPrestador.value, __RazaoSocialPrestador.set, None, 'Razão Social do Prestador do RPS.')

    _ElementMap.update({
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __SerieRPS.name() : __SerieRPS,
        __NumeroRPS.name() : __NumeroRPS,
        __DataEmissaoRPS.name() : __DataEmissaoRPS,
        __RazaoSocialPrestador.name() : __RazaoSocialPrestador
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpChaveRPS = tpChaveRPS
Namespace.addCategoryObject('typeBinding', 'tpChaveRPS', tpChaveRPS)


# Complex type {http://localhost:8080/WsNFe2/tp}tpChaveSubstituicaoNFSe with content type ELEMENT_ONLY
class tpChaveSubstituicaoNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Chave de identificação para Substituição de uma NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpChaveSubstituicaoNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1131, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httplocalhost8080WsNFe2tp_tpChaveSubstituicaoNFSe_InscricaoPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1136, 3), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscrição municipal do prestador de serviços.')

    
    # Element CPFCNPJTomador uses Python identifier CPFCNPJTomador
    __CPFCNPJTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), 'CPFCNPJTomador', '__httplocalhost8080WsNFe2tp_tpChaveSubstituicaoNFSe_CPFCNPJTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1141, 3), )

    
    CPFCNPJTomador = property(__CPFCNPJTomador.value, __CPFCNPJTomador.set, None, 'CPF/CNPJ do Tomador.')

    
    # Element NumeroNFSeSubstituida uses Python identifier NumeroNFSeSubstituida
    __NumeroNFSeSubstituida = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida'), 'NumeroNFSeSubstituida', '__httplocalhost8080WsNFe2tp_tpChaveSubstituicaoNFSe_NumeroNFSeSubstituida', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1146, 3), )

    
    NumeroNFSeSubstituida = property(__NumeroNFSeSubstituida.value, __NumeroNFSeSubstituida.set, None, 'Número da NFSe a ser substituida.')

    
    # Element DataEmissaoNFSeSubstituida uses Python identifier DataEmissaoNFSeSubstituida
    __DataEmissaoNFSeSubstituida = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida'), 'DataEmissaoNFSeSubstituida', '__httplocalhost8080WsNFe2tp_tpChaveSubstituicaoNFSe_DataEmissaoNFSeSubstituida', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1151, 3), )

    
    DataEmissaoNFSeSubstituida = property(__DataEmissaoNFSeSubstituida.value, __DataEmissaoNFSeSubstituida.set, None, 'Data da Emissão da NFSe a ser substituida.')

    _ElementMap.update({
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __CPFCNPJTomador.name() : __CPFCNPJTomador,
        __NumeroNFSeSubstituida.name() : __NumeroNFSeSubstituida,
        __DataEmissaoNFSeSubstituida.name() : __DataEmissaoNFSeSubstituida
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpChaveSubstituicaoNFSe = tpChaveSubstituicaoNFSe
Namespace.addCategoryObject('typeBinding', 'tpChaveSubstituicaoNFSe', tpChaveSubstituicaoNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpDeducoes with content type ELEMENT_ONLY
class tpDeducoes (pyxb.binding.basis.complexTypeDefinition):
    """Tipo deduções de nota fiscal."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDeducoes')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1158, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DeducaoPor uses Python identifier DeducaoPor
    __DeducaoPor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DeducaoPor'), 'DeducaoPor', '__httplocalhost8080WsNFe2tp_tpDeducoes_DeducaoPor', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1163, 3), )

    
    DeducaoPor = property(__DeducaoPor.value, __DeducaoPor.set, None, None)

    
    # Element TipoDeducao uses Python identifier TipoDeducao
    __TipoDeducao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoDeducao'), 'TipoDeducao', '__httplocalhost8080WsNFe2tp_tpDeducoes_TipoDeducao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1164, 3), )

    
    TipoDeducao = property(__TipoDeducao.value, __TipoDeducao.set, None, None)

    
    # Element CPFCNPJReferencia uses Python identifier CPFCNPJReferencia
    __CPFCNPJReferencia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJReferencia'), 'CPFCNPJReferencia', '__httplocalhost8080WsNFe2tp_tpDeducoes_CPFCNPJReferencia', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1165, 3), )

    
    CPFCNPJReferencia = property(__CPFCNPJReferencia.value, __CPFCNPJReferencia.set, None, None)

    
    # Element NumeroNFReferencia uses Python identifier NumeroNFReferencia
    __NumeroNFReferencia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNFReferencia'), 'NumeroNFReferencia', '__httplocalhost8080WsNFe2tp_tpDeducoes_NumeroNFReferencia', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1166, 3), )

    
    NumeroNFReferencia = property(__NumeroNFReferencia.value, __NumeroNFReferencia.set, None, None)

    
    # Element ValorTotalReferencia uses Python identifier ValorTotalReferencia
    __ValorTotalReferencia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalReferencia'), 'ValorTotalReferencia', '__httplocalhost8080WsNFe2tp_tpDeducoes_ValorTotalReferencia', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1167, 3), )

    
    ValorTotalReferencia = property(__ValorTotalReferencia.value, __ValorTotalReferencia.set, None, None)

    
    # Element PercentualDeduzir uses Python identifier PercentualDeduzir
    __PercentualDeduzir = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PercentualDeduzir'), 'PercentualDeduzir', '__httplocalhost8080WsNFe2tp_tpDeducoes_PercentualDeduzir', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1168, 3), )

    
    PercentualDeduzir = property(__PercentualDeduzir.value, __PercentualDeduzir.set, None, None)

    
    # Element ValorDeduzir uses Python identifier ValorDeduzir
    __ValorDeduzir = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorDeduzir'), 'ValorDeduzir', '__httplocalhost8080WsNFe2tp_tpDeducoes_ValorDeduzir', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1169, 3), )

    
    ValorDeduzir = property(__ValorDeduzir.value, __ValorDeduzir.set, None, None)

    _ElementMap.update({
        __DeducaoPor.name() : __DeducaoPor,
        __TipoDeducao.name() : __TipoDeducao,
        __CPFCNPJReferencia.name() : __CPFCNPJReferencia,
        __NumeroNFReferencia.name() : __NumeroNFReferencia,
        __ValorTotalReferencia.name() : __ValorTotalReferencia,
        __PercentualDeduzir.name() : __PercentualDeduzir,
        __ValorDeduzir.name() : __ValorDeduzir
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpDeducoes = tpDeducoes
Namespace.addCategoryObject('typeBinding', 'tpDeducoes', tpDeducoes)


# Complex type {http://localhost:8080/WsNFe2/tp}tpNotaCancelamentoNFSe with content type ELEMENT_ONLY
class tpNotaCancelamentoNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Tipo Detalhes do Cancelamento de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNotaCancelamentoNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1172, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoMunicipalPrestador uses Python identifier InscricaoMunicipalPrestador
    __InscricaoMunicipalPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), 'InscricaoMunicipalPrestador', '__httplocalhost8080WsNFe2tp_tpNotaCancelamentoNFSe_InscricaoMunicipalPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1177, 3), )

    
    InscricaoMunicipalPrestador = property(__InscricaoMunicipalPrestador.value, __InscricaoMunicipalPrestador.set, None, 'Inscrição municipal do prestador de serviços.')

    
    # Element NumeroNota uses Python identifier NumeroNota
    __NumeroNota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNota'), 'NumeroNota', '__httplocalhost8080WsNFe2tp_tpNotaCancelamentoNFSe_NumeroNota', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1182, 3), )

    
    NumeroNota = property(__NumeroNota.value, __NumeroNota.set, None, 'Número da NF-e.')

    
    # Element CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), 'CodigoVerificacao', '__httplocalhost8080WsNFe2tp_tpNotaCancelamentoNFSe_CodigoVerificacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1187, 3), )

    
    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, 'Código de verificação da NF-e.')

    
    # Element MotivoCancelamento uses Python identifier MotivoCancelamento
    __MotivoCancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MotivoCancelamento'), 'MotivoCancelamento', '__httplocalhost8080WsNFe2tp_tpNotaCancelamentoNFSe_MotivoCancelamento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1192, 3), )

    
    MotivoCancelamento = property(__MotivoCancelamento.value, __MotivoCancelamento.set, None, 'Motivo do Cancelamento da Nota Fiscal.')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httplocalhost8080WsNFe2tp_tpNotaCancelamentoNFSe_Id', pyxb.binding.datatypes.string)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1198, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1198, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __InscricaoMunicipalPrestador.name() : __InscricaoMunicipalPrestador,
        __NumeroNota.name() : __NumeroNota,
        __CodigoVerificacao.name() : __CodigoVerificacao,
        __MotivoCancelamento.name() : __MotivoCancelamento
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.tpNotaCancelamentoNFSe = tpNotaCancelamentoNFSe
Namespace.addCategoryObject('typeBinding', 'tpNotaCancelamentoNFSe', tpNotaCancelamentoNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpDetalhesConsultaRPS with content type ELEMENT_ONLY
class tpDetalhesConsultaRPS (pyxb.binding.basis.complexTypeDefinition):
    """Tipo Detalhes da Consulta de RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpDetalhesConsultaRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1200, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httplocalhost8080WsNFe2tp_tpDetalhesConsultaRPS_InscricaoPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1205, 3), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscrição municipal do prestador de serviços.')

    
    # Element SerieRPS uses Python identifier SerieRPS
    __SerieRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SerieRPS'), 'SerieRPS', '__httplocalhost8080WsNFe2tp_tpDetalhesConsultaRPS_SerieRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1210, 3), )

    
    SerieRPS = property(__SerieRPS.value, __SerieRPS.set, None, 'Série do RPS.')

    
    # Element NumeroRPS uses Python identifier NumeroRPS
    __NumeroRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), 'NumeroRPS', '__httplocalhost8080WsNFe2tp_tpDetalhesConsultaRPS_NumeroRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1215, 3), )

    
    NumeroRPS = property(__NumeroRPS.value, __NumeroRPS.set, None, 'Número do RPS.')

    _ElementMap.update({
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __SerieRPS.name() : __SerieRPS,
        __NumeroRPS.name() : __NumeroRPS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpDetalhesConsultaRPS = tpDetalhesConsultaRPS
Namespace.addCategoryObject('typeBinding', 'tpDetalhesConsultaRPS', tpDetalhesConsultaRPS)


# Complex type {http://localhost:8080/WsNFe2/tp}tpItens with content type ELEMENT_ONLY
class tpItens (pyxb.binding.basis.complexTypeDefinition):
    """Tipo Itens de Nota Fiscal."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpItens')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1222, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DiscriminacaoServico uses Python identifier DiscriminacaoServico
    __DiscriminacaoServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DiscriminacaoServico'), 'DiscriminacaoServico', '__httplocalhost8080WsNFe2tp_tpItens_DiscriminacaoServico', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1227, 3), )

    
    DiscriminacaoServico = property(__DiscriminacaoServico.value, __DiscriminacaoServico.set, None, None)

    
    # Element Quantidade uses Python identifier Quantidade
    __Quantidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Quantidade'), 'Quantidade', '__httplocalhost8080WsNFe2tp_tpItens_Quantidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1228, 3), )

    
    Quantidade = property(__Quantidade.value, __Quantidade.set, None, None)

    
    # Element ValorUnitario uses Python identifier ValorUnitario
    __ValorUnitario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorUnitario'), 'ValorUnitario', '__httplocalhost8080WsNFe2tp_tpItens_ValorUnitario', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1229, 3), )

    
    ValorUnitario = property(__ValorUnitario.value, __ValorUnitario.set, None, None)

    
    # Element ValorTotal uses Python identifier ValorTotal
    __ValorTotal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotal'), 'ValorTotal', '__httplocalhost8080WsNFe2tp_tpItens_ValorTotal', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1230, 3), )

    
    ValorTotal = property(__ValorTotal.value, __ValorTotal.set, None, None)

    
    # Element Tributavel uses Python identifier Tributavel
    __Tributavel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Tributavel'), 'Tributavel', '__httplocalhost8080WsNFe2tp_tpItens_Tributavel', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1231, 3), )

    
    Tributavel = property(__Tributavel.value, __Tributavel.set, None, None)

    _ElementMap.update({
        __DiscriminacaoServico.name() : __DiscriminacaoServico,
        __Quantidade.name() : __Quantidade,
        __ValorUnitario.name() : __ValorUnitario,
        __ValorTotal.name() : __ValorTotal,
        __Tributavel.name() : __Tributavel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpItens = tpItens
Namespace.addCategoryObject('typeBinding', 'tpItens', tpItens)


# Complex type {http://localhost:8080/WsNFe2/tp}tpEndereco with content type ELEMENT_ONLY
class tpEndereco (pyxb.binding.basis.complexTypeDefinition):
    """Tipo Endereço."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1234, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TipoLogradouro uses Python identifier TipoLogradouro
    __TipoLogradouro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoLogradouro'), 'TipoLogradouro', '__httplocalhost8080WsNFe2tp_tpEndereco_TipoLogradouro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1239, 3), )

    
    TipoLogradouro = property(__TipoLogradouro.value, __TipoLogradouro.set, None, None)

    
    # Element Logradouro uses Python identifier Logradouro
    __Logradouro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Logradouro'), 'Logradouro', '__httplocalhost8080WsNFe2tp_tpEndereco_Logradouro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1240, 3), )

    
    Logradouro = property(__Logradouro.value, __Logradouro.set, None, None)

    
    # Element NumeroEndereco uses Python identifier NumeroEndereco
    __NumeroEndereco = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroEndereco'), 'NumeroEndereco', '__httplocalhost8080WsNFe2tp_tpEndereco_NumeroEndereco', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1241, 3), )

    
    NumeroEndereco = property(__NumeroEndereco.value, __NumeroEndereco.set, None, None)

    
    # Element ComplementoEndereco uses Python identifier ComplementoEndereco
    __ComplementoEndereco = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ComplementoEndereco'), 'ComplementoEndereco', '__httplocalhost8080WsNFe2tp_tpEndereco_ComplementoEndereco', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1242, 3), )

    
    ComplementoEndereco = property(__ComplementoEndereco.value, __ComplementoEndereco.set, None, None)

    
    # Element TipoBairro uses Python identifier TipoBairro
    __TipoBairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoBairro'), 'TipoBairro', '__httplocalhost8080WsNFe2tp_tpEndereco_TipoBairro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1243, 3), )

    
    TipoBairro = property(__TipoBairro.value, __TipoBairro.set, None, None)

    
    # Element Bairro uses Python identifier Bairro
    __Bairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Bairro'), 'Bairro', '__httplocalhost8080WsNFe2tp_tpEndereco_Bairro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1244, 3), )

    
    Bairro = property(__Bairro.value, __Bairro.set, None, None)

    
    # Element Cidade uses Python identifier Cidade
    __Cidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cidade'), 'Cidade', '__httplocalhost8080WsNFe2tp_tpEndereco_Cidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1245, 3), )

    
    Cidade = property(__Cidade.value, __Cidade.set, None, None)

    
    # Element UF uses Python identifier UF
    __UF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UF'), 'UF', '__httplocalhost8080WsNFe2tp_tpEndereco_UF', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1246, 3), )

    
    UF = property(__UF.value, __UF.set, None, None)

    
    # Element CEP uses Python identifier CEP
    __CEP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CEP'), 'CEP', '__httplocalhost8080WsNFe2tp_tpEndereco_CEP', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1247, 3), )

    
    CEP = property(__CEP.value, __CEP.set, None, None)

    _ElementMap.update({
        __TipoLogradouro.name() : __TipoLogradouro,
        __Logradouro.name() : __Logradouro,
        __NumeroEndereco.name() : __NumeroEndereco,
        __ComplementoEndereco.name() : __ComplementoEndereco,
        __TipoBairro.name() : __TipoBairro,
        __Bairro.name() : __Bairro,
        __Cidade.name() : __Cidade,
        __UF.name() : __UF,
        __CEP.name() : __CEP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpEndereco = tpEndereco
Namespace.addCategoryObject('typeBinding', 'tpEndereco', tpEndereco)


# Complex type {http://localhost:8080/WsNFe2/tp}tpInformacoesLote with content type ELEMENT_ONLY
class tpInformacoesLote (pyxb.binding.basis.complexTypeDefinition):
    """Informações do lote processado."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpInformacoesLote')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1250, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroLote'), 'NumeroLote', '__httplocalhost8080WsNFe2tp_tpInformacoesLote_NumeroLote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1255, 3), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, 'Número de lote.')

    
    # Element InscricaoPrestador uses Python identifier InscricaoPrestador
    __InscricaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), 'InscricaoPrestador', '__httplocalhost8080WsNFe2tp_tpInformacoesLote_InscricaoPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1260, 3), )

    
    InscricaoPrestador = property(__InscricaoPrestador.value, __InscricaoPrestador.set, None, 'Inscrição municipal do prestador dos RPS contidos no lote.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2tp_tpInformacoesLote_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1265, 3), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'CNPJ do remetente autorizado a transmitir a mensagem XML.')

    
    # Element DataEnvioLote uses Python identifier DataEnvioLote
    __DataEnvioLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEnvioLote'), 'DataEnvioLote', '__httplocalhost8080WsNFe2tp_tpInformacoesLote_DataEnvioLote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1270, 3), )

    
    DataEnvioLote = property(__DataEnvioLote.value, __DataEnvioLote.set, None, 'Data/hora de envio do lote.')

    
    # Element QtdNotasProcessadas uses Python identifier QtdNotasProcessadas
    __QtdNotasProcessadas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas'), 'QtdNotasProcessadas', '__httplocalhost8080WsNFe2tp_tpInformacoesLote_QtdNotasProcessadas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1275, 3), )

    
    QtdNotasProcessadas = property(__QtdNotasProcessadas.value, __QtdNotasProcessadas.set, None, 'Quantidade de RPS do lote.')

    
    # Element TempoProcessamento uses Python identifier TempoProcessamento
    __TempoProcessamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TempoProcessamento'), 'TempoProcessamento', '__httplocalhost8080WsNFe2tp_tpInformacoesLote_TempoProcessamento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1280, 3), )

    
    TempoProcessamento = property(__TempoProcessamento.value, __TempoProcessamento.set, None, 'Tempo de processamento do lote.')

    
    # Element ValorTotalServicos uses Python identifier ValorTotalServicos
    __ValorTotalServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), 'ValorTotalServicos', '__httplocalhost8080WsNFe2tp_tpInformacoesLote_ValorTotalServicos', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1285, 3), )

    
    ValorTotalServicos = property(__ValorTotalServicos.value, __ValorTotalServicos.set, None, 'Valor total dos serviços dos RPS contidos na mensagem XML.')

    
    # Element ValorTotalDeducoes uses Python identifier ValorTotalDeducoes
    __ValorTotalDeducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), 'ValorTotalDeducoes', '__httplocalhost8080WsNFe2tp_tpInformacoesLote_ValorTotalDeducoes', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1290, 3), )

    
    ValorTotalDeducoes = property(__ValorTotalDeducoes.value, __ValorTotalDeducoes.set, None, 'Valor total das deduções dos RPS contidos na mensagem XML.')

    _ElementMap.update({
        __NumeroLote.name() : __NumeroLote,
        __InscricaoPrestador.name() : __InscricaoPrestador,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __DataEnvioLote.name() : __DataEnvioLote,
        __QtdNotasProcessadas.name() : __QtdNotasProcessadas,
        __TempoProcessamento.name() : __TempoProcessamento,
        __ValorTotalServicos.name() : __ValorTotalServicos,
        __ValorTotalDeducoes.name() : __ValorTotalDeducoes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpInformacoesLote = tpInformacoesLote
Namespace.addCategoryObject('typeBinding', 'tpInformacoesLote', tpInformacoesLote)


# Complex type {http://localhost:8080/WsNFe2/tp}tpLogradouroCompleto with content type ELEMENT_ONLY
class tpLogradouroCompleto (pyxb.binding.basis.complexTypeDefinition):
    """Informações do Logradouro com o seu Tipo."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpLogradouroCompleto')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1297, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TipoLogradouro uses Python identifier TipoLogradouro
    __TipoLogradouro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoLogradouro'), 'TipoLogradouro', '__httplocalhost8080WsNFe2tp_tpLogradouroCompleto_TipoLogradouro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1302, 3), )

    
    TipoLogradouro = property(__TipoLogradouro.value, __TipoLogradouro.set, None, 'Tipo do Logradouro (Rua, Avenida etc)')

    
    # Element NomeLogradouro uses Python identifier NomeLogradouro
    __NomeLogradouro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NomeLogradouro'), 'NomeLogradouro', '__httplocalhost8080WsNFe2tp_tpLogradouroCompleto_NomeLogradouro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1307, 3), )

    
    NomeLogradouro = property(__NomeLogradouro.value, __NomeLogradouro.set, None, 'Nome do Logradouro.')

    _ElementMap.update({
        __TipoLogradouro.name() : __TipoLogradouro,
        __NomeLogradouro.name() : __NomeLogradouro
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpLogradouroCompleto = tpLogradouroCompleto
Namespace.addCategoryObject('typeBinding', 'tpLogradouroCompleto', tpLogradouroCompleto)


# Complex type {http://localhost:8080/WsNFe2/tp}tpListaAlertas with content type ELEMENT_ONLY
class tpListaAlertas (pyxb.binding.basis.complexTypeDefinition):
    """Alertas."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpListaAlertas')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1342, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Alerta uses Python identifier Alerta
    __Alerta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Alerta'), 'Alerta', '__httplocalhost8080WsNFe2tp_tpListaAlertas_Alerta', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1347, 3), )

    
    Alerta = property(__Alerta.value, __Alerta.set, None, None)

    _ElementMap.update({
        __Alerta.name() : __Alerta
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpListaAlertas = tpListaAlertas
Namespace.addCategoryObject('typeBinding', 'tpListaAlertas', tpListaAlertas)


# Complex type {http://localhost:8080/WsNFe2/tp}tpListaDeducoes with content type ELEMENT_ONLY
class tpListaDeducoes (pyxb.binding.basis.complexTypeDefinition):
    """Deduções."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpListaDeducoes')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1350, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Deducao uses Python identifier Deducao
    __Deducao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Deducao'), 'Deducao', '__httplocalhost8080WsNFe2tp_tpListaDeducoes_Deducao', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1355, 3), )

    
    Deducao = property(__Deducao.value, __Deducao.set, None, None)

    _ElementMap.update({
        __Deducao.name() : __Deducao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpListaDeducoes = tpListaDeducoes
Namespace.addCategoryObject('typeBinding', 'tpListaDeducoes', tpListaDeducoes)


# Complex type {http://localhost:8080/WsNFe2/tp}tpLoteCancelamentoNFSe with content type ELEMENT_ONLY
class tpLoteCancelamentoNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Lista de Detalhes do Cancelamento de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpLoteCancelamentoNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1358, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Nota uses Python identifier Nota
    __Nota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nota'), 'Nota', '__httplocalhost8080WsNFe2tp_tpLoteCancelamentoNFSe_Nota', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1363, 3), )

    
    Nota = property(__Nota.value, __Nota.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httplocalhost8080WsNFe2tp_tpLoteCancelamentoNFSe_Id', pyxb.binding.datatypes.string)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1365, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1365, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Nota.name() : __Nota
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.tpLoteCancelamentoNFSe = tpLoteCancelamentoNFSe
Namespace.addCategoryObject('typeBinding', 'tpLoteCancelamentoNFSe', tpLoteCancelamentoNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpNotasCancelamentoNFSe with content type ELEMENT_ONLY
class tpNotasCancelamentoNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Lista de Detalhes do Cancelamento de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNotasCancelamentoNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1367, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Nota uses Python identifier Nota
    __Nota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nota'), 'Nota', '__httplocalhost8080WsNFe2tp_tpNotasCancelamentoNFSe_Nota', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1372, 3), )

    
    Nota = property(__Nota.value, __Nota.set, None, None)

    _ElementMap.update({
        __Nota.name() : __Nota
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpNotasCancelamentoNFSe = tpNotasCancelamentoNFSe
Namespace.addCategoryObject('typeBinding', 'tpNotasCancelamentoNFSe', tpNotasCancelamentoNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpRetornoNotasCancelamentoNFSe with content type ELEMENT_ONLY
class tpRetornoNotasCancelamentoNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Lista de Detalhes do Cancelamento de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpRetornoNotasCancelamentoNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1375, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Nota uses Python identifier Nota
    __Nota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nota'), 'Nota', '__httplocalhost8080WsNFe2tp_tpRetornoNotasCancelamentoNFSe_Nota', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1380, 3), )

    
    Nota = property(__Nota.value, __Nota.set, None, None)

    _ElementMap.update({
        __Nota.name() : __Nota
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpRetornoNotasCancelamentoNFSe = tpRetornoNotasCancelamentoNFSe
Namespace.addCategoryObject('typeBinding', 'tpRetornoNotasCancelamentoNFSe', tpRetornoNotasCancelamentoNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpLoteConsultaNFSe with content type ELEMENT_ONLY
class tpLoteConsultaNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Lista de Detalhes da Consulta de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpLoteConsultaNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1384, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NotaConsulta uses Python identifier NotaConsulta
    __NotaConsulta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NotaConsulta'), 'NotaConsulta', '__httplocalhost8080WsNFe2tp_tpLoteConsultaNFSe_NotaConsulta', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1389, 3), )

    
    NotaConsulta = property(__NotaConsulta.value, __NotaConsulta.set, None, None)

    
    # Element RPSConsulta uses Python identifier RPSConsulta
    __RPSConsulta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RPSConsulta'), 'RPSConsulta', '__httplocalhost8080WsNFe2tp_tpLoteConsultaNFSe_RPSConsulta', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1390, 3), )

    
    RPSConsulta = property(__RPSConsulta.value, __RPSConsulta.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httplocalhost8080WsNFe2tp_tpLoteConsultaNFSe_Id', pyxb.binding.datatypes.string)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1392, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1392, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __NotaConsulta.name() : __NotaConsulta,
        __RPSConsulta.name() : __RPSConsulta
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.tpLoteConsultaNFSe = tpLoteConsultaNFSe
Namespace.addCategoryObject('typeBinding', 'tpLoteConsultaNFSe', tpLoteConsultaNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpNotasConsultaNFSe with content type ELEMENT_ONLY
class tpNotasConsultaNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Lista de Detalhes da Consulta de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNotasConsultaNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1395, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Nota uses Python identifier Nota
    __Nota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nota'), 'Nota', '__httplocalhost8080WsNFe2tp_tpNotasConsultaNFSe_Nota', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1400, 3), )

    
    Nota = property(__Nota.value, __Nota.set, None, None)

    _ElementMap.update({
        __Nota.name() : __Nota
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpNotasConsultaNFSe = tpNotasConsultaNFSe
Namespace.addCategoryObject('typeBinding', 'tpNotasConsultaNFSe', tpNotasConsultaNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpNotaConsultaNFSe with content type ELEMENT_ONLY
class tpNotaConsultaNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Tipo Detalhes da Nota da Consulta de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNotaConsultaNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1404, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoMunicipalPrestador uses Python identifier InscricaoMunicipalPrestador
    __InscricaoMunicipalPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), 'InscricaoMunicipalPrestador', '__httplocalhost8080WsNFe2tp_tpNotaConsultaNFSe_InscricaoMunicipalPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1409, 3), )

    
    InscricaoMunicipalPrestador = property(__InscricaoMunicipalPrestador.value, __InscricaoMunicipalPrestador.set, None, 'Inscrição municipal do prestador de serviços.')

    
    # Element NumeroNota uses Python identifier NumeroNota
    __NumeroNota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNota'), 'NumeroNota', '__httplocalhost8080WsNFe2tp_tpNotaConsultaNFSe_NumeroNota', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1414, 3), )

    
    NumeroNota = property(__NumeroNota.value, __NumeroNota.set, None, 'Número da NF-e.')

    
    # Element CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), 'CodigoVerificacao', '__httplocalhost8080WsNFe2tp_tpNotaConsultaNFSe_CodigoVerificacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1419, 3), )

    
    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, 'Código de verificação da NF-e.')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httplocalhost8080WsNFe2tp_tpNotaConsultaNFSe_Id', pyxb.binding.datatypes.string)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1425, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1425, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __InscricaoMunicipalPrestador.name() : __InscricaoMunicipalPrestador,
        __NumeroNota.name() : __NumeroNota,
        __CodigoVerificacao.name() : __CodigoVerificacao
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.tpNotaConsultaNFSe = tpNotaConsultaNFSe
Namespace.addCategoryObject('typeBinding', 'tpNotaConsultaNFSe', tpNotaConsultaNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpRPSsConsultaNFSe with content type ELEMENT_ONLY
class tpRPSsConsultaNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Lista de Detalhes da Consulta de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpRPSsConsultaNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1429, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RPS uses Python identifier RPS
    __RPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RPS'), 'RPS', '__httplocalhost8080WsNFe2tp_tpRPSsConsultaNFSe_RPS', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1434, 3), )

    
    RPS = property(__RPS.value, __RPS.set, None, None)

    _ElementMap.update({
        __RPS.name() : __RPS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpRPSsConsultaNFSe = tpRPSsConsultaNFSe
Namespace.addCategoryObject('typeBinding', 'tpRPSsConsultaNFSe', tpRPSsConsultaNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpRPSConsultaNFSe with content type ELEMENT_ONLY
class tpRPSConsultaNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Tipo Detalhes do RPSSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpRPSConsultaNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1437, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element InscricaoMunicipalPrestador uses Python identifier InscricaoMunicipalPrestador
    __InscricaoMunicipalPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), 'InscricaoMunicipalPrestador', '__httplocalhost8080WsNFe2tp_tpRPSConsultaNFSe_InscricaoMunicipalPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1442, 3), )

    
    InscricaoMunicipalPrestador = property(__InscricaoMunicipalPrestador.value, __InscricaoMunicipalPrestador.set, None, 'Inscrição municipal do prestador de serviços.')

    
    # Element NumeroRPS uses Python identifier NumeroRPS
    __NumeroRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), 'NumeroRPS', '__httplocalhost8080WsNFe2tp_tpRPSConsultaNFSe_NumeroRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1447, 3), )

    
    NumeroRPS = property(__NumeroRPS.value, __NumeroRPS.set, None, 'Número RPS.')

    
    # Element SeriePrestacao uses Python identifier SeriePrestacao
    __SeriePrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), 'SeriePrestacao', '__httplocalhost8080WsNFe2tp_tpRPSConsultaNFSe_SeriePrestacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1452, 3), )

    
    SeriePrestacao = property(__SeriePrestacao.value, __SeriePrestacao.set, None, 'Serie RPS.')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httplocalhost8080WsNFe2tp_tpRPSConsultaNFSe_Id', pyxb.binding.datatypes.string)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1458, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1458, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __InscricaoMunicipalPrestador.name() : __InscricaoMunicipalPrestador,
        __NumeroRPS.name() : __NumeroRPS,
        __SeriePrestacao.name() : __SeriePrestacao
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.tpRPSConsultaNFSe = tpRPSConsultaNFSe
Namespace.addCategoryObject('typeBinding', 'tpRPSConsultaNFSe', tpRPSConsultaNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpListaDetalhesConsultaRPS with content type ELEMENT_ONLY
class tpListaDetalhesConsultaRPS (pyxb.binding.basis.complexTypeDefinition):
    """Lista de Detalhes da Consulta RPS"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpListaDetalhesConsultaRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1464, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Detalhe uses Python identifier Detalhe
    __Detalhe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Detalhe'), 'Detalhe', '__httplocalhost8080WsNFe2tp_tpListaDetalhesConsultaRPS_Detalhe', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1469, 3), )

    
    Detalhe = property(__Detalhe.value, __Detalhe.set, None, None)

    _ElementMap.update({
        __Detalhe.name() : __Detalhe
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpListaDetalhesConsultaRPS = tpListaDetalhesConsultaRPS
Namespace.addCategoryObject('typeBinding', 'tpListaDetalhesConsultaRPS', tpListaDetalhesConsultaRPS)


# Complex type {http://localhost:8080/WsNFe2/tp}tpListaErros with content type ELEMENT_ONLY
class tpListaErros (pyxb.binding.basis.complexTypeDefinition):
    """Erros."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpListaErros')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1472, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Erro uses Python identifier Erro
    __Erro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Erro'), 'Erro', '__httplocalhost8080WsNFe2tp_tpListaErros_Erro', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1477, 3), )

    
    Erro = property(__Erro.value, __Erro.set, None, None)

    _ElementMap.update({
        __Erro.name() : __Erro
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpListaErros = tpListaErros
Namespace.addCategoryObject('typeBinding', 'tpListaErros', tpListaErros)


# Complex type {http://localhost:8080/WsNFe2/tp}tpListaItens with content type ELEMENT_ONLY
class tpListaItens (pyxb.binding.basis.complexTypeDefinition):
    """Itens de Serviço."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpListaItens')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1480, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Item uses Python identifier Item
    __Item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Item'), 'Item', '__httplocalhost8080WsNFe2tp_tpListaItens_Item', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1485, 3), )

    
    Item = property(__Item.value, __Item.set, None, None)

    _ElementMap.update({
        __Item.name() : __Item
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpListaItens = tpListaItens
Namespace.addCategoryObject('typeBinding', 'tpListaItens', tpListaItens)


# Complex type {http://localhost:8080/WsNFe2/tp}tpListaNFSeRPS with content type ELEMENT_ONLY
class tpListaNFSeRPS (pyxb.binding.basis.complexTypeDefinition):
    """NFSE e seu respectivo RPS"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpListaNFSeRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1488, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ChaveNFSeRPS uses Python identifier ChaveNFSeRPS
    __ChaveNFSeRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChaveNFSeRPS'), 'ChaveNFSeRPS', '__httplocalhost8080WsNFe2tp_tpListaNFSeRPS_ChaveNFSeRPS', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1493, 3), )

    
    ChaveNFSeRPS = property(__ChaveNFSeRPS.value, __ChaveNFSeRPS.set, None, None)

    _ElementMap.update({
        __ChaveNFSeRPS.name() : __ChaveNFSeRPS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpListaNFSeRPS = tpListaNFSeRPS
Namespace.addCategoryObject('typeBinding', 'tpListaNFSeRPS', tpListaNFSeRPS)


# Complex type {http://localhost:8080/WsNFe2/tp}tpListaNFSe with content type ELEMENT_ONLY
class tpListaNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Lista de NFSE consultada"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpListaNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1496, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ConsultaNFSe uses Python identifier ConsultaNFSe
    __ConsultaNFSe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ConsultaNFSe'), 'ConsultaNFSe', '__httplocalhost8080WsNFe2tp_tpListaNFSe_ConsultaNFSe', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1501, 3), )

    
    ConsultaNFSe = property(__ConsultaNFSe.value, __ConsultaNFSe.set, None, None)

    _ElementMap.update({
        __ConsultaNFSe.name() : __ConsultaNFSe
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpListaNFSe = tpListaNFSe
Namespace.addCategoryObject('typeBinding', 'tpListaNFSe', tpListaNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpListaNFSeConsultaNota with content type ELEMENT_ONLY
class tpListaNFSeConsultaNota (pyxb.binding.basis.complexTypeDefinition):
    """Lista de NFSE consultada"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpListaNFSeConsultaNota')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1504, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Nota uses Python identifier Nota
    __Nota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Nota'), 'Nota', '__httplocalhost8080WsNFe2tp_tpListaNFSeConsultaNota_Nota', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1509, 3), )

    
    Nota = property(__Nota.value, __Nota.set, None, None)

    _ElementMap.update({
        __Nota.name() : __Nota
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpListaNFSeConsultaNota = tpListaNFSeConsultaNota
Namespace.addCategoryObject('typeBinding', 'tpListaNFSeConsultaNota', tpListaNFSeConsultaNota)


# Complex type {http://localhost:8080/WsNFe2/tp}tpLote with content type ELEMENT_ONLY
class tpLote (pyxb.binding.basis.complexTypeDefinition):
    """Lote de RPS"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpLote')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1512, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RPS uses Python identifier RPS
    __RPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RPS'), 'RPS', '__httplocalhost8080WsNFe2tp_tpLote_RPS', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1517, 3), )

    
    RPS = property(__RPS.value, __RPS.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httplocalhost8080WsNFe2tp_tpLote_Id', pyxb.binding.datatypes.string)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1520, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1520, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __RPS.name() : __RPS
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.tpLote = tpLote
Namespace.addCategoryObject('typeBinding', 'tpLote', tpLote)


# Complex type {http://localhost:8080/WsNFe2/tp}tpNFSe with content type ELEMENT_ONLY
class tpNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que representa uma NFSe"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpNFSe')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1522, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NumeroNota uses Python identifier NumeroNota
    __NumeroNota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNota'), 'NumeroNota', '__httplocalhost8080WsNFe2tp_tpNFSe_NumeroNota', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1527, 3), )

    
    NumeroNota = property(__NumeroNota.value, __NumeroNota.set, None, 'Número da Nota Fiscal')

    
    # Element DataProcessamento uses Python identifier DataProcessamento
    __DataProcessamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataProcessamento'), 'DataProcessamento', '__httplocalhost8080WsNFe2tp_tpNFSe_DataProcessamento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1532, 3), )

    
    DataProcessamento = property(__DataProcessamento.value, __DataProcessamento.set, None, 'Data que a Nota Fiscal foi Processada')

    
    # Element NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroLote'), 'NumeroLote', '__httplocalhost8080WsNFe2tp_tpNFSe_NumeroLote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1538, 3), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, 'Número do Lote')

    
    # Element CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), 'CodigoVerificacao', '__httplocalhost8080WsNFe2tp_tpNFSe_CodigoVerificacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1543, 3), )

    
    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, 'Código de Verificacao')

    
    # Element Assinatura uses Python identifier Assinatura
    __Assinatura = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Assinatura'), 'Assinatura', '__httplocalhost8080WsNFe2tp_tpNFSe_Assinatura', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1548, 3), )

    
    Assinatura = property(__Assinatura.value, __Assinatura.set, None, 'Assinatura digital do RPS.')

    
    # Element InscricaoMunicipalPrestador uses Python identifier InscricaoMunicipalPrestador
    __InscricaoMunicipalPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), 'InscricaoMunicipalPrestador', '__httplocalhost8080WsNFe2tp_tpNFSe_InscricaoMunicipalPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1554, 3), )

    
    InscricaoMunicipalPrestador = property(__InscricaoMunicipalPrestador.value, __InscricaoMunicipalPrestador.set, None, 'Informe a Inscrição Municipal do Prestador')

    
    # Element RazaoSocialPrestador uses Python identifier RazaoSocialPrestador
    __RazaoSocialPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), 'RazaoSocialPrestador', '__httplocalhost8080WsNFe2tp_tpNFSe_RazaoSocialPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1559, 3), )

    
    RazaoSocialPrestador = property(__RazaoSocialPrestador.value, __RazaoSocialPrestador.set, None, 'Informe a Razao Social do Prestador')

    
    # Element TipoRPS uses Python identifier TipoRPS
    __TipoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoRPS'), 'TipoRPS', '__httplocalhost8080WsNFe2tp_tpNFSe_TipoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1564, 3), )

    
    TipoRPS = property(__TipoRPS.value, __TipoRPS.set, None, 'Informe o Tipo do RPS emitido.')

    
    # Element SerieRPS uses Python identifier SerieRPS
    __SerieRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SerieRPS'), 'SerieRPS', '__httplocalhost8080WsNFe2tp_tpNFSe_SerieRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1569, 3), )

    
    SerieRPS = property(__SerieRPS.value, __SerieRPS.set, None, 'Informe a Série do RPS emitido.')

    
    # Element NumeroRPS uses Python identifier NumeroRPS
    __NumeroRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), 'NumeroRPS', '__httplocalhost8080WsNFe2tp_tpNFSe_NumeroRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1574, 3), )

    
    NumeroRPS = property(__NumeroRPS.value, __NumeroRPS.set, None, 'Informe o Número do RPS emitido.')

    
    # Element DataEmissaoRPS uses Python identifier DataEmissaoRPS
    __DataEmissaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), 'DataEmissaoRPS', '__httplocalhost8080WsNFe2tp_tpNFSe_DataEmissaoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1579, 3), )

    
    DataEmissaoRPS = property(__DataEmissaoRPS.value, __DataEmissaoRPS.set, None, 'Informe a Data de emissão do RPS.')

    
    # Element SituacaoRPS uses Python identifier SituacaoRPS
    __SituacaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SituacaoRPS'), 'SituacaoRPS', '__httplocalhost8080WsNFe2tp_tpNFSe_SituacaoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1584, 3), )

    
    SituacaoRPS = property(__SituacaoRPS.value, __SituacaoRPS.set, None, 'Informe o Status do RPS.')

    
    # Element SerieRPSSubstituido uses Python identifier SerieRPSSubstituido
    __SerieRPSSubstituido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SerieRPSSubstituido'), 'SerieRPSSubstituido', '__httplocalhost8080WsNFe2tp_tpNFSe_SerieRPSSubstituido', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1589, 3), )

    
    SerieRPSSubstituido = property(__SerieRPSSubstituido.value, __SerieRPSSubstituido.set, None, 'Informe a Série do RPS substituído.')

    
    # Element NumeroRPSSubstituido uses Python identifier NumeroRPSSubstituido
    __NumeroRPSSubstituido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPSSubstituido'), 'NumeroRPSSubstituido', '__httplocalhost8080WsNFe2tp_tpNFSe_NumeroRPSSubstituido', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1594, 3), )

    
    NumeroRPSSubstituido = property(__NumeroRPSSubstituido.value, __NumeroRPSSubstituido.set, None, 'Informe o Número do RPS substituído.')

    
    # Element NumeroNFSeSubstituida uses Python identifier NumeroNFSeSubstituida
    __NumeroNFSeSubstituida = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida'), 'NumeroNFSeSubstituida', '__httplocalhost8080WsNFe2tp_tpNFSe_NumeroNFSeSubstituida', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1599, 3), )

    
    NumeroNFSeSubstituida = property(__NumeroNFSeSubstituida.value, __NumeroNFSeSubstituida.set, None, 'Informe o Número da NFSe substituída.')

    
    # Element DataEmissaoNFSeSubstituida uses Python identifier DataEmissaoNFSeSubstituida
    __DataEmissaoNFSeSubstituida = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida'), 'DataEmissaoNFSeSubstituida', '__httplocalhost8080WsNFe2tp_tpNFSe_DataEmissaoNFSeSubstituida', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1604, 3), )

    
    DataEmissaoNFSeSubstituida = property(__DataEmissaoNFSeSubstituida.value, __DataEmissaoNFSeSubstituida.set, None, 'Informe a Data de Emissão da NFSe substituída.')

    
    # Element SeriePrestacao uses Python identifier SeriePrestacao
    __SeriePrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), 'SeriePrestacao', '__httplocalhost8080WsNFe2tp_tpNFSe_SeriePrestacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1609, 3), )

    
    SeriePrestacao = property(__SeriePrestacao.value, __SeriePrestacao.set, None, 'Série de prestação')

    
    # Element InscricaoMunicipalTomador uses Python identifier InscricaoMunicipalTomador
    __InscricaoMunicipalTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador'), 'InscricaoMunicipalTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_InscricaoMunicipalTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1614, 3), )

    
    InscricaoMunicipalTomador = property(__InscricaoMunicipalTomador.value, __InscricaoMunicipalTomador.set, None, 'Informe a Inscrição Municipal do Tomador. ATENÇÃO: Este campo só deverá ser preenchido para tomadores estabelecidos no município. Quando este campo for preenchido, seu conteúdo será considerado como prioritário com relação ao campo de CPF/CNPJ do Tomador, sendo utilizado para identificar o Tomador e recuperar seus dados da base de dados da Prefeitura.')

    
    # Element CPFCNPJTomador uses Python identifier CPFCNPJTomador
    __CPFCNPJTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), 'CPFCNPJTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_CPFCNPJTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1619, 3), )

    
    CPFCNPJTomador = property(__CPFCNPJTomador.value, __CPFCNPJTomador.set, None, 'Informe o CPF/CNPJ do tomador do serviço. O conteúdo deste campo será ignorado caso o campo InscricaoMunicipalTomador esteja preenchido.')

    
    # Element RazaoSocialTomador uses Python identifier RazaoSocialTomador
    __RazaoSocialTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador'), 'RazaoSocialTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_RazaoSocialTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1624, 3), )

    
    RazaoSocialTomador = property(__RazaoSocialTomador.value, __RazaoSocialTomador.set, None, 'Informe o Nome/Razão Social do tomador. Este campo é obrigatório apenas para tomadores Pessoa Jurídica (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ ou a Inscrição Municipal do tomador pertença ao município.')

    
    # Element DocTomadorEstrangeiro uses Python identifier DocTomadorEstrangeiro
    __DocTomadorEstrangeiro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DocTomadorEstrangeiro'), 'DocTomadorEstrangeiro', '__httplocalhost8080WsNFe2tp_tpNFSe_DocTomadorEstrangeiro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1629, 3), )

    
    DocTomadorEstrangeiro = property(__DocTomadorEstrangeiro.value, __DocTomadorEstrangeiro.set, None, 'Informe o Documento de Identificação do tomador. Este campo é obrigatório apenas para tomadores estrageiros, ou seja quando no CidadeTomador que indica o Codigo SIAFI da cidade do tomador for informado 0009999')

    
    # Element TipoLogradouroTomador uses Python identifier TipoLogradouroTomador
    __TipoLogradouroTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoLogradouroTomador'), 'TipoLogradouroTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_TipoLogradouroTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1634, 3), )

    
    TipoLogradouroTomador = property(__TipoLogradouroTomador.value, __TipoLogradouroTomador.set, None, 'Informe o Tipo do Logradouro do Endereço do Tomador.')

    
    # Element LogradouroTomador uses Python identifier LogradouroTomador
    __LogradouroTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LogradouroTomador'), 'LogradouroTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_LogradouroTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1639, 3), )

    
    LogradouroTomador = property(__LogradouroTomador.value, __LogradouroTomador.set, None, 'Informe o Logradouro do Endereço do Tomador.')

    
    # Element NumeroEnderecoTomador uses Python identifier NumeroEnderecoTomador
    __NumeroEnderecoTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroEnderecoTomador'), 'NumeroEnderecoTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_NumeroEnderecoTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1644, 3), )

    
    NumeroEnderecoTomador = property(__NumeroEnderecoTomador.value, __NumeroEnderecoTomador.set, None, 'Informe o Número do Endereço do Tomador.')

    
    # Element ComplementoEnderecoTomador uses Python identifier ComplementoEnderecoTomador
    __ComplementoEnderecoTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ComplementoEnderecoTomador'), 'ComplementoEnderecoTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_ComplementoEnderecoTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1649, 3), )

    
    ComplementoEnderecoTomador = property(__ComplementoEnderecoTomador.value, __ComplementoEnderecoTomador.set, None, 'Informe o Comlpemento do Endereço do Tomador.')

    
    # Element TipoBairroTomador uses Python identifier TipoBairroTomador
    __TipoBairroTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoBairroTomador'), 'TipoBairroTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_TipoBairroTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1654, 3), )

    
    TipoBairroTomador = property(__TipoBairroTomador.value, __TipoBairroTomador.set, None, 'Informe o Tipo do Bairro do Endereço do Tomador.')

    
    # Element BairroTomador uses Python identifier BairroTomador
    __BairroTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BairroTomador'), 'BairroTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_BairroTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1659, 3), )

    
    BairroTomador = property(__BairroTomador.value, __BairroTomador.set, None, 'Informe o Bairro do Endereço do Tomador.')

    
    # Element CidadeTomador uses Python identifier CidadeTomador
    __CidadeTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CidadeTomador'), 'CidadeTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_CidadeTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1664, 3), )

    
    CidadeTomador = property(__CidadeTomador.value, __CidadeTomador.set, None, 'Informe a Cidade do Tomador.')

    
    # Element CidadeTomadorDescricao uses Python identifier CidadeTomadorDescricao
    __CidadeTomadorDescricao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CidadeTomadorDescricao'), 'CidadeTomadorDescricao', '__httplocalhost8080WsNFe2tp_tpNFSe_CidadeTomadorDescricao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1669, 3), )

    
    CidadeTomadorDescricao = property(__CidadeTomadorDescricao.value, __CidadeTomadorDescricao.set, None, 'Informe a Descricao Cidade do Tomador.')

    
    # Element CEPTomador uses Python identifier CEPTomador
    __CEPTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CEPTomador'), 'CEPTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_CEPTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1674, 3), )

    
    CEPTomador = property(__CEPTomador.value, __CEPTomador.set, None, 'Informe o CEP do Tomador.')

    
    # Element EmailTomador uses Python identifier EmailTomador
    __EmailTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EmailTomador'), 'EmailTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_EmailTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1679, 3), )

    
    EmailTomador = property(__EmailTomador.value, __EmailTomador.set, None, 'Informe o e-mail do tomador.')

    
    # Element CodigoAtividade uses Python identifier CodigoAtividade
    __CodigoAtividade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoAtividade'), 'CodigoAtividade', '__httplocalhost8080WsNFe2tp_tpNFSe_CodigoAtividade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1684, 3), )

    
    CodigoAtividade = property(__CodigoAtividade.value, __CodigoAtividade.set, None, 'Informe o código da atividade do RPS. Este código deve pertencer à lista CNAE.')

    
    # Element AliquotaAtividade uses Python identifier AliquotaAtividade
    __AliquotaAtividade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaAtividade'), 'AliquotaAtividade', '__httplocalhost8080WsNFe2tp_tpNFSe_AliquotaAtividade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1689, 3), )

    
    AliquotaAtividade = property(__AliquotaAtividade.value, __AliquotaAtividade.set, None, 'Informe o valor da alíquota.')

    
    # Element TipoRecolhimento uses Python identifier TipoRecolhimento
    __TipoRecolhimento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento'), 'TipoRecolhimento', '__httplocalhost8080WsNFe2tp_tpNFSe_TipoRecolhimento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1694, 3), )

    
    TipoRecolhimento = property(__TipoRecolhimento.value, __TipoRecolhimento.set, None, 'Informe a retenção.')

    
    # Element MunicipioPrestacao uses Python identifier MunicipioPrestacao
    __MunicipioPrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao'), 'MunicipioPrestacao', '__httplocalhost8080WsNFe2tp_tpNFSe_MunicipioPrestacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1699, 3), )

    
    MunicipioPrestacao = property(__MunicipioPrestacao.value, __MunicipioPrestacao.set, None, 'Informe o Município da Prestação do Serviço.')

    
    # Element MunicipioPrestacaoDescricao uses Python identifier MunicipioPrestacaoDescricao
    __MunicipioPrestacaoDescricao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacaoDescricao'), 'MunicipioPrestacaoDescricao', '__httplocalhost8080WsNFe2tp_tpNFSe_MunicipioPrestacaoDescricao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1704, 3), )

    
    MunicipioPrestacaoDescricao = property(__MunicipioPrestacaoDescricao.value, __MunicipioPrestacaoDescricao.set, None, 'Informe o Município da Prestação do Serviço.')

    
    # Element Operacao uses Python identifier Operacao
    __Operacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Operacao'), 'Operacao', '__httplocalhost8080WsNFe2tp_tpNFSe_Operacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1709, 3), )

    
    Operacao = property(__Operacao.value, __Operacao.set, None, 'Informe a Operação da Prestação do Serviço.')

    
    # Element Tributacao uses Python identifier Tributacao
    __Tributacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Tributacao'), 'Tributacao', '__httplocalhost8080WsNFe2tp_tpNFSe_Tributacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1714, 3), )

    
    Tributacao = property(__Tributacao.value, __Tributacao.set, None, 'Informe o tipo de tributação do RPS.')

    
    # Element ValorPIS uses Python identifier ValorPIS
    __ValorPIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorPIS'), 'ValorPIS', '__httplocalhost8080WsNFe2tp_tpNFSe_ValorPIS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1719, 3), )

    
    ValorPIS = property(__ValorPIS.value, __ValorPIS.set, None, 'Informe o valor da retenção do PIS.')

    
    # Element ValorCOFINS uses Python identifier ValorCOFINS
    __ValorCOFINS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCOFINS'), 'ValorCOFINS', '__httplocalhost8080WsNFe2tp_tpNFSe_ValorCOFINS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1724, 3), )

    
    ValorCOFINS = property(__ValorCOFINS.value, __ValorCOFINS.set, None, 'Informe o valor da retenção do COFINS.')

    
    # Element ValorINSS uses Python identifier ValorINSS
    __ValorINSS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorINSS'), 'ValorINSS', '__httplocalhost8080WsNFe2tp_tpNFSe_ValorINSS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1729, 3), )

    
    ValorINSS = property(__ValorINSS.value, __ValorINSS.set, None, 'Informe o valor da retenção do INSS.')

    
    # Element ValorIR uses Python identifier ValorIR
    __ValorIR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorIR'), 'ValorIR', '__httplocalhost8080WsNFe2tp_tpNFSe_ValorIR', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1734, 3), )

    
    ValorIR = property(__ValorIR.value, __ValorIR.set, None, 'Informe o valor da retenção do IR.')

    
    # Element ValorCSLL uses Python identifier ValorCSLL
    __ValorCSLL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCSLL'), 'ValorCSLL', '__httplocalhost8080WsNFe2tp_tpNFSe_ValorCSLL', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1739, 3), )

    
    ValorCSLL = property(__ValorCSLL.value, __ValorCSLL.set, None, 'Informe o valor da retenção do CSLL.')

    
    # Element AliquotaPIS uses Python identifier AliquotaPIS
    __AliquotaPIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaPIS'), 'AliquotaPIS', '__httplocalhost8080WsNFe2tp_tpNFSe_AliquotaPIS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1744, 3), )

    
    AliquotaPIS = property(__AliquotaPIS.value, __AliquotaPIS.set, None, 'Informe a Alíquota da retenção do PIS.')

    
    # Element AliquotaCOFINS uses Python identifier AliquotaCOFINS
    __AliquotaCOFINS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaCOFINS'), 'AliquotaCOFINS', '__httplocalhost8080WsNFe2tp_tpNFSe_AliquotaCOFINS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1749, 3), )

    
    AliquotaCOFINS = property(__AliquotaCOFINS.value, __AliquotaCOFINS.set, None, 'Informe a Alíquota da retenção do COFINS.')

    
    # Element AliquotaINSS uses Python identifier AliquotaINSS
    __AliquotaINSS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaINSS'), 'AliquotaINSS', '__httplocalhost8080WsNFe2tp_tpNFSe_AliquotaINSS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1754, 3), )

    
    AliquotaINSS = property(__AliquotaINSS.value, __AliquotaINSS.set, None, 'Informe a Alíquota da retenção do INSS.')

    
    # Element AliquotaIR uses Python identifier AliquotaIR
    __AliquotaIR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaIR'), 'AliquotaIR', '__httplocalhost8080WsNFe2tp_tpNFSe_AliquotaIR', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1759, 3), )

    
    AliquotaIR = property(__AliquotaIR.value, __AliquotaIR.set, None, 'Informe a Alíquota da retenção do IR.')

    
    # Element AliquotaCSLL uses Python identifier AliquotaCSLL
    __AliquotaCSLL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaCSLL'), 'AliquotaCSLL', '__httplocalhost8080WsNFe2tp_tpNFSe_AliquotaCSLL', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1764, 3), )

    
    AliquotaCSLL = property(__AliquotaCSLL.value, __AliquotaCSLL.set, None, 'Informe a Alíquota da retenção do CSLL.')

    
    # Element DescricaoRPS uses Python identifier DescricaoRPS
    __DescricaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DescricaoRPS'), 'DescricaoRPS', '__httplocalhost8080WsNFe2tp_tpNFSe_DescricaoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1769, 3), )

    
    DescricaoRPS = property(__DescricaoRPS.value, __DescricaoRPS.set, None, 'Descrição da Nota.')

    
    # Element DDDPrestador uses Python identifier DDDPrestador
    __DDDPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DDDPrestador'), 'DDDPrestador', '__httplocalhost8080WsNFe2tp_tpNFSe_DDDPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1774, 3), )

    
    DDDPrestador = property(__DDDPrestador.value, __DDDPrestador.set, None, 'DDD do Prestador.')

    
    # Element TelefonePrestador uses Python identifier TelefonePrestador
    __TelefonePrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TelefonePrestador'), 'TelefonePrestador', '__httplocalhost8080WsNFe2tp_tpNFSe_TelefonePrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1779, 3), )

    
    TelefonePrestador = property(__TelefonePrestador.value, __TelefonePrestador.set, None, 'Telefone do Prestador.')

    
    # Element DDDTomador uses Python identifier DDDTomador
    __DDDTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DDDTomador'), 'DDDTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_DDDTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1784, 3), )

    
    DDDTomador = property(__DDDTomador.value, __DDDTomador.set, None, 'DDD do Tomador.')

    
    # Element TelefoneTomador uses Python identifier TelefoneTomador
    __TelefoneTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TelefoneTomador'), 'TelefoneTomador', '__httplocalhost8080WsNFe2tp_tpNFSe_TelefoneTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1789, 3), )

    
    TelefoneTomador = property(__TelefoneTomador.value, __TelefoneTomador.set, None, 'Telefone do Tomador.')

    
    # Element MotCancelamento uses Python identifier MotCancelamento
    __MotCancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MotCancelamento'), 'MotCancelamento', '__httplocalhost8080WsNFe2tp_tpNFSe_MotCancelamento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1794, 3), )

    
    MotCancelamento = property(__MotCancelamento.value, __MotCancelamento.set, None, 'Informe o Motivo do Cancelamento.')

    
    # Element CPFCNPJIntermediario uses Python identifier CPFCNPJIntermediario
    __CPFCNPJIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario'), 'CPFCNPJIntermediario', '__httplocalhost8080WsNFe2tp_tpNFSe_CPFCNPJIntermediario', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1799, 3), )

    
    CPFCNPJIntermediario = property(__CPFCNPJIntermediario.value, __CPFCNPJIntermediario.set, None, 'CPF/CNPJ do intermediário do serviço. Campo não é obrigatório, deve ser informado quando houver um intermediário entre o tomador e o prestador.')

    
    # Element Deducoes uses Python identifier Deducoes
    __Deducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Deducoes'), 'Deducoes', '__httplocalhost8080WsNFe2tp_tpNFSe_Deducoes', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1804, 3), )

    
    Deducoes = property(__Deducoes.value, __Deducoes.set, None, 'Lista de Deduções.')

    
    # Element Itens uses Python identifier Itens
    __Itens = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Itens'), 'Itens', '__httplocalhost8080WsNFe2tp_tpNFSe_Itens', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1809, 3), )

    
    Itens = property(__Itens.value, __Itens.set, None, 'Lista de Itens.')

    _ElementMap.update({
        __NumeroNota.name() : __NumeroNota,
        __DataProcessamento.name() : __DataProcessamento,
        __NumeroLote.name() : __NumeroLote,
        __CodigoVerificacao.name() : __CodigoVerificacao,
        __Assinatura.name() : __Assinatura,
        __InscricaoMunicipalPrestador.name() : __InscricaoMunicipalPrestador,
        __RazaoSocialPrestador.name() : __RazaoSocialPrestador,
        __TipoRPS.name() : __TipoRPS,
        __SerieRPS.name() : __SerieRPS,
        __NumeroRPS.name() : __NumeroRPS,
        __DataEmissaoRPS.name() : __DataEmissaoRPS,
        __SituacaoRPS.name() : __SituacaoRPS,
        __SerieRPSSubstituido.name() : __SerieRPSSubstituido,
        __NumeroRPSSubstituido.name() : __NumeroRPSSubstituido,
        __NumeroNFSeSubstituida.name() : __NumeroNFSeSubstituida,
        __DataEmissaoNFSeSubstituida.name() : __DataEmissaoNFSeSubstituida,
        __SeriePrestacao.name() : __SeriePrestacao,
        __InscricaoMunicipalTomador.name() : __InscricaoMunicipalTomador,
        __CPFCNPJTomador.name() : __CPFCNPJTomador,
        __RazaoSocialTomador.name() : __RazaoSocialTomador,
        __DocTomadorEstrangeiro.name() : __DocTomadorEstrangeiro,
        __TipoLogradouroTomador.name() : __TipoLogradouroTomador,
        __LogradouroTomador.name() : __LogradouroTomador,
        __NumeroEnderecoTomador.name() : __NumeroEnderecoTomador,
        __ComplementoEnderecoTomador.name() : __ComplementoEnderecoTomador,
        __TipoBairroTomador.name() : __TipoBairroTomador,
        __BairroTomador.name() : __BairroTomador,
        __CidadeTomador.name() : __CidadeTomador,
        __CidadeTomadorDescricao.name() : __CidadeTomadorDescricao,
        __CEPTomador.name() : __CEPTomador,
        __EmailTomador.name() : __EmailTomador,
        __CodigoAtividade.name() : __CodigoAtividade,
        __AliquotaAtividade.name() : __AliquotaAtividade,
        __TipoRecolhimento.name() : __TipoRecolhimento,
        __MunicipioPrestacao.name() : __MunicipioPrestacao,
        __MunicipioPrestacaoDescricao.name() : __MunicipioPrestacaoDescricao,
        __Operacao.name() : __Operacao,
        __Tributacao.name() : __Tributacao,
        __ValorPIS.name() : __ValorPIS,
        __ValorCOFINS.name() : __ValorCOFINS,
        __ValorINSS.name() : __ValorINSS,
        __ValorIR.name() : __ValorIR,
        __ValorCSLL.name() : __ValorCSLL,
        __AliquotaPIS.name() : __AliquotaPIS,
        __AliquotaCOFINS.name() : __AliquotaCOFINS,
        __AliquotaINSS.name() : __AliquotaINSS,
        __AliquotaIR.name() : __AliquotaIR,
        __AliquotaCSLL.name() : __AliquotaCSLL,
        __DescricaoRPS.name() : __DescricaoRPS,
        __DDDPrestador.name() : __DDDPrestador,
        __TelefonePrestador.name() : __TelefonePrestador,
        __DDDTomador.name() : __DDDTomador,
        __TelefoneTomador.name() : __TelefoneTomador,
        __MotCancelamento.name() : __MotCancelamento,
        __CPFCNPJIntermediario.name() : __CPFCNPJIntermediario,
        __Deducoes.name() : __Deducoes,
        __Itens.name() : __Itens
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tpNFSe = tpNFSe
Namespace.addCategoryObject('typeBinding', 'tpNFSe', tpNFSe)


# Complex type {http://localhost:8080/WsNFe2/tp}tpRPS with content type ELEMENT_ONLY
class tpRPS (pyxb.binding.basis.complexTypeDefinition):
    """Tipo que representa um RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tpRPS')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1816, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Assinatura uses Python identifier Assinatura
    __Assinatura = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Assinatura'), 'Assinatura', '__httplocalhost8080WsNFe2tp_tpRPS_Assinatura', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1821, 3), )

    
    Assinatura = property(__Assinatura.value, __Assinatura.set, None, 'Assinatura digital do RPS.')

    
    # Element InscricaoMunicipalPrestador uses Python identifier InscricaoMunicipalPrestador
    __InscricaoMunicipalPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), 'InscricaoMunicipalPrestador', '__httplocalhost8080WsNFe2tp_tpRPS_InscricaoMunicipalPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1826, 3), )

    
    InscricaoMunicipalPrestador = property(__InscricaoMunicipalPrestador.value, __InscricaoMunicipalPrestador.set, None, 'Informe a Inscrição Municipal do Prestador')

    
    # Element RazaoSocialPrestador uses Python identifier RazaoSocialPrestador
    __RazaoSocialPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), 'RazaoSocialPrestador', '__httplocalhost8080WsNFe2tp_tpRPS_RazaoSocialPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1831, 3), )

    
    RazaoSocialPrestador = property(__RazaoSocialPrestador.value, __RazaoSocialPrestador.set, None, 'Informe a Razao Social do Prestador')

    
    # Element TipoRPS uses Python identifier TipoRPS
    __TipoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoRPS'), 'TipoRPS', '__httplocalhost8080WsNFe2tp_tpRPS_TipoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1836, 3), )

    
    TipoRPS = property(__TipoRPS.value, __TipoRPS.set, None, 'Informe o Tipo do RPS emitido.')

    
    # Element SerieRPS uses Python identifier SerieRPS
    __SerieRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SerieRPS'), 'SerieRPS', '__httplocalhost8080WsNFe2tp_tpRPS_SerieRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1841, 3), )

    
    SerieRPS = property(__SerieRPS.value, __SerieRPS.set, None, 'Informe a Série do RPS emitido.')

    
    # Element NumeroRPS uses Python identifier NumeroRPS
    __NumeroRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), 'NumeroRPS', '__httplocalhost8080WsNFe2tp_tpRPS_NumeroRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1846, 3), )

    
    NumeroRPS = property(__NumeroRPS.value, __NumeroRPS.set, None, 'Informe o Número do RPS emitido.')

    
    # Element DataEmissaoRPS uses Python identifier DataEmissaoRPS
    __DataEmissaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), 'DataEmissaoRPS', '__httplocalhost8080WsNFe2tp_tpRPS_DataEmissaoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1851, 3), )

    
    DataEmissaoRPS = property(__DataEmissaoRPS.value, __DataEmissaoRPS.set, None, 'Informe a Data de emissão do RPS.')

    
    # Element SituacaoRPS uses Python identifier SituacaoRPS
    __SituacaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SituacaoRPS'), 'SituacaoRPS', '__httplocalhost8080WsNFe2tp_tpRPS_SituacaoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1856, 3), )

    
    SituacaoRPS = property(__SituacaoRPS.value, __SituacaoRPS.set, None, 'Informe o Status do RPS.')

    
    # Element SerieRPSSubstituido uses Python identifier SerieRPSSubstituido
    __SerieRPSSubstituido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SerieRPSSubstituido'), 'SerieRPSSubstituido', '__httplocalhost8080WsNFe2tp_tpRPS_SerieRPSSubstituido', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1861, 3), )

    
    SerieRPSSubstituido = property(__SerieRPSSubstituido.value, __SerieRPSSubstituido.set, None, 'Informe a Série do RPS substituído.')

    
    # Element NumeroRPSSubstituido uses Python identifier NumeroRPSSubstituido
    __NumeroRPSSubstituido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroRPSSubstituido'), 'NumeroRPSSubstituido', '__httplocalhost8080WsNFe2tp_tpRPS_NumeroRPSSubstituido', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1866, 3), )

    
    NumeroRPSSubstituido = property(__NumeroRPSSubstituido.value, __NumeroRPSSubstituido.set, None, 'Informe o Número do RPS substituído.')

    
    # Element NumeroNFSeSubstituida uses Python identifier NumeroNFSeSubstituida
    __NumeroNFSeSubstituida = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida'), 'NumeroNFSeSubstituida', '__httplocalhost8080WsNFe2tp_tpRPS_NumeroNFSeSubstituida', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1871, 3), )

    
    NumeroNFSeSubstituida = property(__NumeroNFSeSubstituida.value, __NumeroNFSeSubstituida.set, None, 'Informe o Número da NFSe substituída.')

    
    # Element DataEmissaoNFSeSubstituida uses Python identifier DataEmissaoNFSeSubstituida
    __DataEmissaoNFSeSubstituida = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida'), 'DataEmissaoNFSeSubstituida', '__httplocalhost8080WsNFe2tp_tpRPS_DataEmissaoNFSeSubstituida', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1876, 3), )

    
    DataEmissaoNFSeSubstituida = property(__DataEmissaoNFSeSubstituida.value, __DataEmissaoNFSeSubstituida.set, None, 'Informe a Data de Emissão da NFSe substituída.')

    
    # Element SeriePrestacao uses Python identifier SeriePrestacao
    __SeriePrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), 'SeriePrestacao', '__httplocalhost8080WsNFe2tp_tpRPS_SeriePrestacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1881, 3), )

    
    SeriePrestacao = property(__SeriePrestacao.value, __SeriePrestacao.set, None, 'Informe o Documento de Prestação')

    
    # Element InscricaoMunicipalTomador uses Python identifier InscricaoMunicipalTomador
    __InscricaoMunicipalTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador'), 'InscricaoMunicipalTomador', '__httplocalhost8080WsNFe2tp_tpRPS_InscricaoMunicipalTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1886, 3), )

    
    InscricaoMunicipalTomador = property(__InscricaoMunicipalTomador.value, __InscricaoMunicipalTomador.set, None, 'Informe a Inscrição Municipal do Tomador. ATENÇÃO: Este campo só deverá ser preenchido para tomadores estabelecidos no município. Quando este campo for preenchido, seu conteúdo será considerado como prioritário com relação ao campo de CPF/CNPJ do Tomador, sendo utilizado para identificar o Tomador e recuperar seus dados da base de dados da Prefeitura.')

    
    # Element CPFCNPJTomador uses Python identifier CPFCNPJTomador
    __CPFCNPJTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), 'CPFCNPJTomador', '__httplocalhost8080WsNFe2tp_tpRPS_CPFCNPJTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1891, 3), )

    
    CPFCNPJTomador = property(__CPFCNPJTomador.value, __CPFCNPJTomador.set, None, 'Informe o CPF/CNPJ do tomador do serviço. O conteúdo deste campo será ignorado caso o campo InscricaoMunicipalTomador esteja preenchido.')

    
    # Element RazaoSocialTomador uses Python identifier RazaoSocialTomador
    __RazaoSocialTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador'), 'RazaoSocialTomador', '__httplocalhost8080WsNFe2tp_tpRPS_RazaoSocialTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1896, 3), )

    
    RazaoSocialTomador = property(__RazaoSocialTomador.value, __RazaoSocialTomador.set, None, 'Informe o Nome/Razão Social do tomador. Este campo é obrigatório apenas para tomadores Pessoa Jurídica (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ ou a Inscrição Municipal do tomador pertença ao município.')

    
    # Element DocTomadorEstrangeiro uses Python identifier DocTomadorEstrangeiro
    __DocTomadorEstrangeiro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DocTomadorEstrangeiro'), 'DocTomadorEstrangeiro', '__httplocalhost8080WsNFe2tp_tpRPS_DocTomadorEstrangeiro', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1901, 3), )

    
    DocTomadorEstrangeiro = property(__DocTomadorEstrangeiro.value, __DocTomadorEstrangeiro.set, None, 'Informe o Documento de Identificação do tomador. Este campo é obrigatório apenas para tomadores estrageiros, ou seja quando no CidadeTomador que indica o Codigo SIAFI da cidade do tomador for informado 0009999')

    
    # Element TipoLogradouroTomador uses Python identifier TipoLogradouroTomador
    __TipoLogradouroTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoLogradouroTomador'), 'TipoLogradouroTomador', '__httplocalhost8080WsNFe2tp_tpRPS_TipoLogradouroTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1906, 3), )

    
    TipoLogradouroTomador = property(__TipoLogradouroTomador.value, __TipoLogradouroTomador.set, None, 'Informe o Tipo do Logradouro do Endereço do Tomador.')

    
    # Element LogradouroTomador uses Python identifier LogradouroTomador
    __LogradouroTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LogradouroTomador'), 'LogradouroTomador', '__httplocalhost8080WsNFe2tp_tpRPS_LogradouroTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1911, 3), )

    
    LogradouroTomador = property(__LogradouroTomador.value, __LogradouroTomador.set, None, 'Informe o Logradouro do Endereço do Tomador.')

    
    # Element NumeroEnderecoTomador uses Python identifier NumeroEnderecoTomador
    __NumeroEnderecoTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroEnderecoTomador'), 'NumeroEnderecoTomador', '__httplocalhost8080WsNFe2tp_tpRPS_NumeroEnderecoTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1916, 3), )

    
    NumeroEnderecoTomador = property(__NumeroEnderecoTomador.value, __NumeroEnderecoTomador.set, None, 'Informe o Número do Endereço do Tomador.')

    
    # Element ComplementoEnderecoTomador uses Python identifier ComplementoEnderecoTomador
    __ComplementoEnderecoTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ComplementoEnderecoTomador'), 'ComplementoEnderecoTomador', '__httplocalhost8080WsNFe2tp_tpRPS_ComplementoEnderecoTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1921, 3), )

    
    ComplementoEnderecoTomador = property(__ComplementoEnderecoTomador.value, __ComplementoEnderecoTomador.set, None, 'Informe o Comlpemento do Endereço do Tomador.')

    
    # Element TipoBairroTomador uses Python identifier TipoBairroTomador
    __TipoBairroTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoBairroTomador'), 'TipoBairroTomador', '__httplocalhost8080WsNFe2tp_tpRPS_TipoBairroTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1926, 3), )

    
    TipoBairroTomador = property(__TipoBairroTomador.value, __TipoBairroTomador.set, None, 'Informe o Tipo do Bairro do Endereço do Tomador.')

    
    # Element BairroTomador uses Python identifier BairroTomador
    __BairroTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BairroTomador'), 'BairroTomador', '__httplocalhost8080WsNFe2tp_tpRPS_BairroTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1931, 3), )

    
    BairroTomador = property(__BairroTomador.value, __BairroTomador.set, None, 'Informe o Bairro do Endereço do Tomador.')

    
    # Element CidadeTomador uses Python identifier CidadeTomador
    __CidadeTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CidadeTomador'), 'CidadeTomador', '__httplocalhost8080WsNFe2tp_tpRPS_CidadeTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1936, 3), )

    
    CidadeTomador = property(__CidadeTomador.value, __CidadeTomador.set, None, 'Informe a Cidade do Tomador.')

    
    # Element CidadeTomadorDescricao uses Python identifier CidadeTomadorDescricao
    __CidadeTomadorDescricao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CidadeTomadorDescricao'), 'CidadeTomadorDescricao', '__httplocalhost8080WsNFe2tp_tpRPS_CidadeTomadorDescricao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1941, 3), )

    
    CidadeTomadorDescricao = property(__CidadeTomadorDescricao.value, __CidadeTomadorDescricao.set, None, 'Informe a Descricao da Cidade do Tomador.')

    
    # Element CEPTomador uses Python identifier CEPTomador
    __CEPTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CEPTomador'), 'CEPTomador', '__httplocalhost8080WsNFe2tp_tpRPS_CEPTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1946, 3), )

    
    CEPTomador = property(__CEPTomador.value, __CEPTomador.set, None, 'Informe o CEP do Tomador.')

    
    # Element EmailTomador uses Python identifier EmailTomador
    __EmailTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EmailTomador'), 'EmailTomador', '__httplocalhost8080WsNFe2tp_tpRPS_EmailTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1951, 3), )

    
    EmailTomador = property(__EmailTomador.value, __EmailTomador.set, None, 'Informe o e-mail do tomador.')

    
    # Element CodigoAtividade uses Python identifier CodigoAtividade
    __CodigoAtividade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodigoAtividade'), 'CodigoAtividade', '__httplocalhost8080WsNFe2tp_tpRPS_CodigoAtividade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1956, 3), )

    
    CodigoAtividade = property(__CodigoAtividade.value, __CodigoAtividade.set, None, 'Informe o código da atividade do RPS. Este código deve pertencer à lista CNAE.')

    
    # Element AliquotaAtividade uses Python identifier AliquotaAtividade
    __AliquotaAtividade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaAtividade'), 'AliquotaAtividade', '__httplocalhost8080WsNFe2tp_tpRPS_AliquotaAtividade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1961, 3), )

    
    AliquotaAtividade = property(__AliquotaAtividade.value, __AliquotaAtividade.set, None, 'Informe o valor da alíquota.')

    
    # Element TipoRecolhimento uses Python identifier TipoRecolhimento
    __TipoRecolhimento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento'), 'TipoRecolhimento', '__httplocalhost8080WsNFe2tp_tpRPS_TipoRecolhimento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1966, 3), )

    
    TipoRecolhimento = property(__TipoRecolhimento.value, __TipoRecolhimento.set, None, 'Informe a retenção.')

    
    # Element MunicipioPrestacao uses Python identifier MunicipioPrestacao
    __MunicipioPrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao'), 'MunicipioPrestacao', '__httplocalhost8080WsNFe2tp_tpRPS_MunicipioPrestacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1971, 3), )

    
    MunicipioPrestacao = property(__MunicipioPrestacao.value, __MunicipioPrestacao.set, None, 'Informe o Município da Prestação do Serviço.')

    
    # Element MunicipioPrestacaoDescricao uses Python identifier MunicipioPrestacaoDescricao
    __MunicipioPrestacaoDescricao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacaoDescricao'), 'MunicipioPrestacaoDescricao', '__httplocalhost8080WsNFe2tp_tpRPS_MunicipioPrestacaoDescricao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1976, 3), )

    
    MunicipioPrestacaoDescricao = property(__MunicipioPrestacaoDescricao.value, __MunicipioPrestacaoDescricao.set, None, 'Informe o Município da Prestação do Serviço.')

    
    # Element Operacao uses Python identifier Operacao
    __Operacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Operacao'), 'Operacao', '__httplocalhost8080WsNFe2tp_tpRPS_Operacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1981, 3), )

    
    Operacao = property(__Operacao.value, __Operacao.set, None, 'Informe a Operação da Prestação do Serviço.')

    
    # Element Tributacao uses Python identifier Tributacao
    __Tributacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Tributacao'), 'Tributacao', '__httplocalhost8080WsNFe2tp_tpRPS_Tributacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1986, 3), )

    
    Tributacao = property(__Tributacao.value, __Tributacao.set, None, 'Informe o tipo de tributação do RPS.')

    
    # Element ValorPIS uses Python identifier ValorPIS
    __ValorPIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorPIS'), 'ValorPIS', '__httplocalhost8080WsNFe2tp_tpRPS_ValorPIS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1991, 3), )

    
    ValorPIS = property(__ValorPIS.value, __ValorPIS.set, None, 'Informe o valor da retenção do PIS.')

    
    # Element ValorCOFINS uses Python identifier ValorCOFINS
    __ValorCOFINS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCOFINS'), 'ValorCOFINS', '__httplocalhost8080WsNFe2tp_tpRPS_ValorCOFINS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1996, 3), )

    
    ValorCOFINS = property(__ValorCOFINS.value, __ValorCOFINS.set, None, 'Informe o valor da retenção do COFINS.')

    
    # Element ValorINSS uses Python identifier ValorINSS
    __ValorINSS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorINSS'), 'ValorINSS', '__httplocalhost8080WsNFe2tp_tpRPS_ValorINSS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2001, 3), )

    
    ValorINSS = property(__ValorINSS.value, __ValorINSS.set, None, 'Informe o valor da retenção do INSS.')

    
    # Element ValorIR uses Python identifier ValorIR
    __ValorIR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorIR'), 'ValorIR', '__httplocalhost8080WsNFe2tp_tpRPS_ValorIR', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2006, 3), )

    
    ValorIR = property(__ValorIR.value, __ValorIR.set, None, 'Informe o valor da retenção do IR.')

    
    # Element ValorCSLL uses Python identifier ValorCSLL
    __ValorCSLL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorCSLL'), 'ValorCSLL', '__httplocalhost8080WsNFe2tp_tpRPS_ValorCSLL', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2011, 3), )

    
    ValorCSLL = property(__ValorCSLL.value, __ValorCSLL.set, None, 'Informe o valor da retenção do CSLL.')

    
    # Element AliquotaPIS uses Python identifier AliquotaPIS
    __AliquotaPIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaPIS'), 'AliquotaPIS', '__httplocalhost8080WsNFe2tp_tpRPS_AliquotaPIS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2016, 3), )

    
    AliquotaPIS = property(__AliquotaPIS.value, __AliquotaPIS.set, None, 'Informe a Alíquota da retenção do PIS.')

    
    # Element AliquotaCOFINS uses Python identifier AliquotaCOFINS
    __AliquotaCOFINS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaCOFINS'), 'AliquotaCOFINS', '__httplocalhost8080WsNFe2tp_tpRPS_AliquotaCOFINS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2021, 3), )

    
    AliquotaCOFINS = property(__AliquotaCOFINS.value, __AliquotaCOFINS.set, None, 'Informe a Alíquota da retenção do COFINS.')

    
    # Element AliquotaINSS uses Python identifier AliquotaINSS
    __AliquotaINSS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaINSS'), 'AliquotaINSS', '__httplocalhost8080WsNFe2tp_tpRPS_AliquotaINSS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2026, 3), )

    
    AliquotaINSS = property(__AliquotaINSS.value, __AliquotaINSS.set, None, 'Informe a Alíquota da retenção do INSS.')

    
    # Element AliquotaIR uses Python identifier AliquotaIR
    __AliquotaIR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaIR'), 'AliquotaIR', '__httplocalhost8080WsNFe2tp_tpRPS_AliquotaIR', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2031, 3), )

    
    AliquotaIR = property(__AliquotaIR.value, __AliquotaIR.set, None, 'Informe a Alíquota da retenção do IR.')

    
    # Element AliquotaCSLL uses Python identifier AliquotaCSLL
    __AliquotaCSLL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AliquotaCSLL'), 'AliquotaCSLL', '__httplocalhost8080WsNFe2tp_tpRPS_AliquotaCSLL', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2036, 3), )

    
    AliquotaCSLL = property(__AliquotaCSLL.value, __AliquotaCSLL.set, None, 'Informe a Alíquota da retenção do CSLL.')

    
    # Element DescricaoRPS uses Python identifier DescricaoRPS
    __DescricaoRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DescricaoRPS'), 'DescricaoRPS', '__httplocalhost8080WsNFe2tp_tpRPS_DescricaoRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2041, 3), )

    
    DescricaoRPS = property(__DescricaoRPS.value, __DescricaoRPS.set, None, 'Descrição da Nota.')

    
    # Element DDDPrestador uses Python identifier DDDPrestador
    __DDDPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DDDPrestador'), 'DDDPrestador', '__httplocalhost8080WsNFe2tp_tpRPS_DDDPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2046, 3), )

    
    DDDPrestador = property(__DDDPrestador.value, __DDDPrestador.set, None, 'DDD do Prestador.')

    
    # Element TelefonePrestador uses Python identifier TelefonePrestador
    __TelefonePrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TelefonePrestador'), 'TelefonePrestador', '__httplocalhost8080WsNFe2tp_tpRPS_TelefonePrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2051, 3), )

    
    TelefonePrestador = property(__TelefonePrestador.value, __TelefonePrestador.set, None, 'Telefone do Prestador.')

    
    # Element DDDTomador uses Python identifier DDDTomador
    __DDDTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DDDTomador'), 'DDDTomador', '__httplocalhost8080WsNFe2tp_tpRPS_DDDTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2056, 3), )

    
    DDDTomador = property(__DDDTomador.value, __DDDTomador.set, None, 'DDD do Tomador.')

    
    # Element TelefoneTomador uses Python identifier TelefoneTomador
    __TelefoneTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TelefoneTomador'), 'TelefoneTomador', '__httplocalhost8080WsNFe2tp_tpRPS_TelefoneTomador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2061, 3), )

    
    TelefoneTomador = property(__TelefoneTomador.value, __TelefoneTomador.set, None, 'Telefone do Tomador.')

    
    # Element MotCancelamento uses Python identifier MotCancelamento
    __MotCancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MotCancelamento'), 'MotCancelamento', '__httplocalhost8080WsNFe2tp_tpRPS_MotCancelamento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2066, 3), )

    
    MotCancelamento = property(__MotCancelamento.value, __MotCancelamento.set, None, 'Informe o Motivo do Cancelamento.')

    
    # Element CPFCNPJIntermediario uses Python identifier CPFCNPJIntermediario
    __CPFCNPJIntermediario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario'), 'CPFCNPJIntermediario', '__httplocalhost8080WsNFe2tp_tpRPS_CPFCNPJIntermediario', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2071, 3), )

    
    CPFCNPJIntermediario = property(__CPFCNPJIntermediario.value, __CPFCNPJIntermediario.set, None, 'Informe o CPF/CNPJ do intermediário do serviço. Campo não é obrigatório, deve ser informado quando houver um intermediário entre o tomador e o prestador.')

    
    # Element Deducoes uses Python identifier Deducoes
    __Deducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Deducoes'), 'Deducoes', '__httplocalhost8080WsNFe2tp_tpRPS_Deducoes', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2076, 3), )

    
    Deducoes = property(__Deducoes.value, __Deducoes.set, None, 'Lista de Deduções.')

    
    # Element Itens uses Python identifier Itens
    __Itens = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Itens'), 'Itens', '__httplocalhost8080WsNFe2tp_tpRPS_Itens', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2081, 3), )

    
    Itens = property(__Itens.value, __Itens.set, None, 'Lista de Itens.')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httplocalhost8080WsNFe2tp_tpRPS_Id', pyxb.binding.datatypes.string)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2087, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2087, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Assinatura.name() : __Assinatura,
        __InscricaoMunicipalPrestador.name() : __InscricaoMunicipalPrestador,
        __RazaoSocialPrestador.name() : __RazaoSocialPrestador,
        __TipoRPS.name() : __TipoRPS,
        __SerieRPS.name() : __SerieRPS,
        __NumeroRPS.name() : __NumeroRPS,
        __DataEmissaoRPS.name() : __DataEmissaoRPS,
        __SituacaoRPS.name() : __SituacaoRPS,
        __SerieRPSSubstituido.name() : __SerieRPSSubstituido,
        __NumeroRPSSubstituido.name() : __NumeroRPSSubstituido,
        __NumeroNFSeSubstituida.name() : __NumeroNFSeSubstituida,
        __DataEmissaoNFSeSubstituida.name() : __DataEmissaoNFSeSubstituida,
        __SeriePrestacao.name() : __SeriePrestacao,
        __InscricaoMunicipalTomador.name() : __InscricaoMunicipalTomador,
        __CPFCNPJTomador.name() : __CPFCNPJTomador,
        __RazaoSocialTomador.name() : __RazaoSocialTomador,
        __DocTomadorEstrangeiro.name() : __DocTomadorEstrangeiro,
        __TipoLogradouroTomador.name() : __TipoLogradouroTomador,
        __LogradouroTomador.name() : __LogradouroTomador,
        __NumeroEnderecoTomador.name() : __NumeroEnderecoTomador,
        __ComplementoEnderecoTomador.name() : __ComplementoEnderecoTomador,
        __TipoBairroTomador.name() : __TipoBairroTomador,
        __BairroTomador.name() : __BairroTomador,
        __CidadeTomador.name() : __CidadeTomador,
        __CidadeTomadorDescricao.name() : __CidadeTomadorDescricao,
        __CEPTomador.name() : __CEPTomador,
        __EmailTomador.name() : __EmailTomador,
        __CodigoAtividade.name() : __CodigoAtividade,
        __AliquotaAtividade.name() : __AliquotaAtividade,
        __TipoRecolhimento.name() : __TipoRecolhimento,
        __MunicipioPrestacao.name() : __MunicipioPrestacao,
        __MunicipioPrestacaoDescricao.name() : __MunicipioPrestacaoDescricao,
        __Operacao.name() : __Operacao,
        __Tributacao.name() : __Tributacao,
        __ValorPIS.name() : __ValorPIS,
        __ValorCOFINS.name() : __ValorCOFINS,
        __ValorINSS.name() : __ValorINSS,
        __ValorIR.name() : __ValorIR,
        __ValorCSLL.name() : __ValorCSLL,
        __AliquotaPIS.name() : __AliquotaPIS,
        __AliquotaCOFINS.name() : __AliquotaCOFINS,
        __AliquotaINSS.name() : __AliquotaINSS,
        __AliquotaIR.name() : __AliquotaIR,
        __AliquotaCSLL.name() : __AliquotaCSLL,
        __DescricaoRPS.name() : __DescricaoRPS,
        __DDDPrestador.name() : __DDDPrestador,
        __TelefonePrestador.name() : __TelefonePrestador,
        __DDDTomador.name() : __DDDTomador,
        __TelefoneTomador.name() : __TelefoneTomador,
        __MotCancelamento.name() : __MotCancelamento,
        __CPFCNPJIntermediario.name() : __CPFCNPJIntermediario,
        __Deducoes.name() : __Deducoes,
        __Itens.name() : __Itens
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.tpRPS = tpRPS
Namespace.addCategoryObject('typeBinding', 'tpRPS', tpRPS)




tpBairroCompleto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoBairro'), tpTipoBairro, scope=tpBairroCompleto, documentation='Tipo do Bairro (Bairro, Vila etc)', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 937, 3)))

tpBairroCompleto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NomeBairro'), tpBairro, scope=tpBairroCompleto, documentation='Nome do Bairro.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 942, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpBairroCompleto._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoBairro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 937, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpBairroCompleto._UseForTag(pyxb.namespace.ExpandedName(None, 'NomeBairro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 942, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpBairroCompleto._Automaton = _BuildAutomaton()




tpEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Codigo'), tpCodigoEvento, scope=tpEvento, documentation='Código do evento.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 951, 3)))

tpEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Descricao'), tpDescricaoEvento, scope=tpEvento, documentation='Descrição do enveto.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 956, 3)))

tpEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), tpChaveRPS, scope=tpEvento, documentation='Chave do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 961, 3)))

tpEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), tpChaveNFe, scope=tpEvento, documentation='Chave da NFe.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 966, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 956, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 961, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 966, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpEvento._UseForTag(pyxb.namespace.ExpandedName(None, 'Codigo')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 951, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpEvento._UseForTag(pyxb.namespace.ExpandedName(None, 'Descricao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 956, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpEvento._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 961, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(tpEvento._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveNFe')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 966, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpEvento._Automaton = _BuildAutomaton_()




tpCPFCNPJ2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPF'), tpCPF, scope=tpCPFCNPJ2, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 978, 3)))

tpCPFCNPJ2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CNPJ'), tpCNPJ, scope=tpCPFCNPJ2, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 979, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpCPFCNPJ2._UseForTag(pyxb.namespace.ExpandedName(None, 'CPF')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 978, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpCPFCNPJ2._UseForTag(pyxb.namespace.ExpandedName(None, 'CNPJ')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 979, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpCPFCNPJ2._Automaton = _BuildAutomaton_2()




tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpConsultaNFSe, documentation='Inscrição municipal do prestador de serviços.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 997, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNFe'), tpNumero, scope=tpConsultaNFSe, documentation='Número da NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1002, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), tpCodigoVerificacao, scope=tpConsultaNFSe, documentation='Código de verificação da NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1007, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SerieRPS'), tpSerieRPS, scope=tpConsultaNFSe, documentation='Série do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1012, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), tpNumero, scope=tpConsultaNFSe, documentation='Número do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1017, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), tpDataHora, scope=tpConsultaNFSe, documentation='Data de Emissão do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1023, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), tpRazaoSocial, scope=tpConsultaNFSe, documentation='Razão Social do Prestador do Serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1028, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento'), tpTipoRecolhimento, scope=tpConsultaNFSe, documentation='Tipo do Recolhimento do Serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1033, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorDeduzir'), tpValor, scope=tpConsultaNFSe, documentation='Valor total de deduções.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1038, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotal'), tpValor, scope=tpConsultaNFSe, documentation='Valor total de Itens de Nota.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1043, 3)))

tpConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Aliquota'), tpAliquota, scope=tpConsultaNFSe, documentation='Valor total de Itens de Nota.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1048, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1038, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 997, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNFe')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1002, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1007, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'SerieRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1012, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1017, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1023, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1028, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1033, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorDeduzir')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1038, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotal')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1043, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Aliquota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1048, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpConsultaNFSe._Automaton = _BuildAutomaton_3()




tpChaveNFeRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveNFe'), tpChaveNFe, scope=tpChaveNFeRPS, documentation='Chave da NFSe gerada.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1060, 3)))

tpChaveNFeRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveRPS'), tpChaveRPS, scope=tpChaveNFeRPS, documentation='Chave do RPS substituído.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1065, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1060, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1065, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpChaveNFeRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveNFe')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1060, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpChaveNFeRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1065, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpChaveNFeRPS._Automaton = _BuildAutomaton_4()




tpChaveNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpChaveNFe, documentation='Inscrição municipal do prestador de serviços.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1077, 3)))

tpChaveNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNFe'), tpNumero, scope=tpChaveNFe, documentation='Número da NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1082, 3)))

tpChaveNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), tpCodigoVerificacao, scope=tpChaveNFe, documentation='Código de verificação da NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1087, 3)))

tpChaveNFe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), tpRazaoSocial, scope=tpChaveNFe, documentation='Razão Social do Prestador do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1092, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1077, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNFe')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1082, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1087, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpChaveNFe._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1092, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpChaveNFe._Automaton = _BuildAutomaton_5()




tpChaveRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpChaveRPS, documentation='Inscrição municipal do prestador de serviços.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1104, 3)))

tpChaveRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SerieRPS'), tpSerieRPS, scope=tpChaveRPS, documentation='Série do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1109, 3)))

tpChaveRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), tpNumero, scope=tpChaveRPS, documentation='Número do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1114, 3)))

tpChaveRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), pyxb.binding.datatypes.dateTime, scope=tpChaveRPS, documentation='Data de Emissao do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1119, 3)))

tpChaveRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), tpRazaoSocial, scope=tpChaveRPS, documentation='Razão Social do Prestador do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1124, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1104, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'SerieRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1109, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1114, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1119, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpChaveRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1124, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpChaveRPS._Automaton = _BuildAutomaton_6()




tpChaveSubstituicaoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpChaveSubstituicaoNFSe, documentation='Inscrição municipal do prestador de serviços.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1136, 3)))

tpChaveSubstituicaoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), tpCPFCNPJ, scope=tpChaveSubstituicaoNFSe, documentation='CPF/CNPJ do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1141, 3)))

tpChaveSubstituicaoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida'), tpNumero, scope=tpChaveSubstituicaoNFSe, documentation='Número da NFSe a ser substituida.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1146, 3)))

tpChaveSubstituicaoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida'), tpData, scope=tpChaveSubstituicaoNFSe, documentation='Data da Emissão da NFSe a ser substituida.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1151, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveSubstituicaoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1136, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveSubstituicaoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1141, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpChaveSubstituicaoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1146, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpChaveSubstituicaoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1151, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpChaveSubstituicaoNFSe._Automaton = _BuildAutomaton_7()




tpDeducoes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DeducaoPor'), tpDeducaoPor, scope=tpDeducoes, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1163, 3)))

tpDeducoes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoDeducao'), tpTipoDeducao, scope=tpDeducoes, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1164, 3)))

tpDeducoes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJReferencia'), tpCPFCNPJnulo, scope=tpDeducoes, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1165, 3)))

tpDeducoes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNFReferencia'), tpNumeroNFReferencia, scope=tpDeducoes, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1166, 3)))

tpDeducoes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalReferencia'), tpValor, scope=tpDeducoes, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1167, 3)))

tpDeducoes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PercentualDeduzir'), tpPercentual, scope=tpDeducoes, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1168, 3)))

tpDeducoes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorDeduzir'), tpValor, scope=tpDeducoes, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1169, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1165, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1166, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1167, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpDeducoes._UseForTag(pyxb.namespace.ExpandedName(None, 'DeducaoPor')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1163, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpDeducoes._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoDeducao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1164, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpDeducoes._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJReferencia')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1165, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpDeducoes._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNFReferencia')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1166, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpDeducoes._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalReferencia')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1167, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpDeducoes._UseForTag(pyxb.namespace.ExpandedName(None, 'PercentualDeduzir')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1168, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpDeducoes._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorDeduzir')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1169, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpDeducoes._Automaton = _BuildAutomaton_8()




tpNotaCancelamentoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), tpInscricaoMunicipal, scope=tpNotaCancelamentoNFSe, documentation='Inscrição municipal do prestador de serviços.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1177, 3)))

tpNotaCancelamentoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNota'), tpNumero, scope=tpNotaCancelamentoNFSe, documentation='Número da NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1182, 3)))

tpNotaCancelamentoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), tpCodigoVerificacao, scope=tpNotaCancelamentoNFSe, documentation='Código de verificação da NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1187, 3)))

tpNotaCancelamentoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MotivoCancelamento'), tpMotCancelamento, scope=tpNotaCancelamentoNFSe, documentation='Motivo do Cancelamento da Nota Fiscal.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1192, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNotaCancelamentoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1177, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNotaCancelamentoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1182, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNotaCancelamentoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1187, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpNotaCancelamentoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'MotivoCancelamento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1192, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpNotaCancelamentoNFSe._Automaton = _BuildAutomaton_9()




tpDetalhesConsultaRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpDetalhesConsultaRPS, documentation='Inscrição municipal do prestador de serviços.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1205, 3)))

tpDetalhesConsultaRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SerieRPS'), tpSerieRPS, scope=tpDetalhesConsultaRPS, documentation='Série do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1210, 3)))

tpDetalhesConsultaRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), tpNumero, scope=tpDetalhesConsultaRPS, documentation='Número do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1215, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1210, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpDetalhesConsultaRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1205, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpDetalhesConsultaRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'SerieRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1210, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpDetalhesConsultaRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1215, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpDetalhesConsultaRPS._Automaton = _BuildAutomaton_10()




tpItens._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DiscriminacaoServico'), tpDiscriminacao, scope=tpItens, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1227, 3)))

tpItens._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Quantidade'), tpQuantidade, scope=tpItens, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1228, 3)))

tpItens._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorUnitario'), tpValor4d, scope=tpItens, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1229, 3)))

tpItens._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotal'), tpValor, scope=tpItens, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1230, 3)))

tpItens._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Tributavel'), tpItemTributavel, scope=tpItens, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1231, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1231, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpItens._UseForTag(pyxb.namespace.ExpandedName(None, 'DiscriminacaoServico')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1227, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpItens._UseForTag(pyxb.namespace.ExpandedName(None, 'Quantidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1228, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpItens._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorUnitario')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1229, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpItens._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotal')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1230, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpItens._UseForTag(pyxb.namespace.ExpandedName(None, 'Tributavel')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1231, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpItens._Automaton = _BuildAutomaton_11()




tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoLogradouro'), tpTipoLogradouro, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1239, 3)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Logradouro'), tpLogradouro, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1240, 3)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroEndereco'), tpNumeroEndereco, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1241, 3)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ComplementoEndereco'), tpComplementoEndereco, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1242, 3)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoBairro'), tpTipoBairro, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1243, 3)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Bairro'), tpBairro, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1244, 3)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cidade'), tpCidade, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1245, 3)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UF'), tpUF, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1246, 3)))

tpEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CEP'), tpCEP, scope=tpEndereco, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1247, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1239, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1240, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1241, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1242, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1243, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1244, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1245, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1246, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1247, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoLogradouro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1239, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'Logradouro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1240, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroEndereco')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1241, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'ComplementoEndereco')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1242, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoBairro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1243, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'Bairro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1244, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'Cidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1245, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'UF')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1246, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(tpEndereco._UseForTag(pyxb.namespace.ExpandedName(None, 'CEP')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1247, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpEndereco._Automaton = _BuildAutomaton_12()




tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroLote'), tpNumero, scope=tpInformacoesLote, documentation='Número de lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1255, 3)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador'), tpInscricaoMunicipal, scope=tpInformacoesLote, documentation='Inscrição municipal do prestador dos RPS contidos no lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1260, 3)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), tpCPFCNPJ, scope=tpInformacoesLote, documentation='CNPJ do remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1265, 3)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEnvioLote'), pyxb.binding.datatypes.dateTime, scope=tpInformacoesLote, documentation='Data/hora de envio do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1270, 3)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas'), tpQuantidade, scope=tpInformacoesLote, documentation='Quantidade de RPS do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1275, 3)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TempoProcessamento'), tpTempoProcessamento, scope=tpInformacoesLote, documentation='Tempo de processamento do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1280, 3)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), tpValor, scope=tpInformacoesLote, documentation='Valor total dos serviços dos RPS contidos na mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1285, 3)))

tpInformacoesLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), tpValor, scope=tpInformacoesLote, documentation='Valor total das deduções dos RPS contidos na mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1290, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1255, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1290, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroLote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1255, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1260, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1265, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEnvioLote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1270, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1275, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'TempoProcessamento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1280, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1285, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpInformacoesLote._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1290, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpInformacoesLote._Automaton = _BuildAutomaton_13()




tpLogradouroCompleto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoLogradouro'), tpTipoLogradouro, scope=tpLogradouroCompleto, documentation='Tipo do Logradouro (Rua, Avenida etc)', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1302, 3)))

tpLogradouroCompleto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NomeLogradouro'), tpLogradouro, scope=tpLogradouroCompleto, documentation='Nome do Logradouro.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1307, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpLogradouroCompleto._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoLogradouro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1302, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpLogradouroCompleto._UseForTag(pyxb.namespace.ExpandedName(None, 'NomeLogradouro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1307, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpLogradouroCompleto._Automaton = _BuildAutomaton_14()




tpListaAlertas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Alerta'), tpEvento, scope=tpListaAlertas, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1347, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1347, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpListaAlertas._UseForTag(pyxb.namespace.ExpandedName(None, 'Alerta')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1347, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpListaAlertas._Automaton = _BuildAutomaton_15()




tpListaDeducoes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Deducao'), tpDeducoes, scope=tpListaDeducoes, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1355, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=200, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1355, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpListaDeducoes._UseForTag(pyxb.namespace.ExpandedName(None, 'Deducao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1355, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpListaDeducoes._Automaton = _BuildAutomaton_16()




tpLoteCancelamentoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nota'), tpNotaCancelamentoNFSe, scope=tpLoteCancelamentoNFSe, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1363, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=50, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1363, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpLoteCancelamentoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Nota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1363, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpLoteCancelamentoNFSe._Automaton = _BuildAutomaton_17()




tpNotasCancelamentoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nota'), tpNotaCancelamentoNFSe, scope=tpNotasCancelamentoNFSe, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1372, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=50, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1372, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpNotasCancelamentoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Nota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1372, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpNotasCancelamentoNFSe._Automaton = _BuildAutomaton_18()




tpRetornoNotasCancelamentoNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nota'), tpNotaCancelamentoNFSe, scope=tpRetornoNotasCancelamentoNFSe, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1380, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1380, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpRetornoNotasCancelamentoNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Nota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1380, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpRetornoNotasCancelamentoNFSe._Automaton = _BuildAutomaton_19()




tpLoteConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NotaConsulta'), tpNotasConsultaNFSe, scope=tpLoteConsultaNFSe, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1389, 3)))

tpLoteConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RPSConsulta'), tpRPSsConsultaNFSe, scope=tpLoteConsultaNFSe, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1390, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1389, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1390, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpLoteConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NotaConsulta')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1389, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tpLoteConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'RPSConsulta')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1390, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpLoteConsultaNFSe._Automaton = _BuildAutomaton_20()




tpNotasConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nota'), tpNotaConsultaNFSe, scope=tpNotasConsultaNFSe, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1400, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=50, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1400, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpNotasConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Nota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1400, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpNotasConsultaNFSe._Automaton = _BuildAutomaton_21()




tpNotaConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), tpInscricaoMunicipal, scope=tpNotaConsultaNFSe, documentation='Inscrição municipal do prestador de serviços.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1409, 3)))

tpNotaConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNota'), tpNumero, scope=tpNotaConsultaNFSe, documentation='Número da NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1414, 3)))

tpNotaConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), tpCodigoVerificacao, scope=tpNotaConsultaNFSe, documentation='Código de verificação da NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1419, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNotaConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1409, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNotaConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1414, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpNotaConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1419, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpNotaConsultaNFSe._Automaton = _BuildAutomaton_22()




tpRPSsConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RPS'), tpRPSConsultaNFSe, scope=tpRPSsConsultaNFSe, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1434, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=50, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1434, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpRPSsConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'RPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1434, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpRPSsConsultaNFSe._Automaton = _BuildAutomaton_23()




tpRPSConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), tpInscricaoMunicipal, scope=tpRPSConsultaNFSe, documentation='Inscrição municipal do prestador de serviços.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1442, 3)))

tpRPSConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), tpNumero, scope=tpRPSConsultaNFSe, documentation='Número RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1447, 3)))

tpRPSConsultaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), tpSeriePrestacao, scope=tpRPSConsultaNFSe, documentation='Serie RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1452, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPSConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1442, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPSConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1447, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpRPSConsultaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'SeriePrestacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1452, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpRPSConsultaNFSe._Automaton = _BuildAutomaton_24()




tpListaDetalhesConsultaRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Detalhe'), tpDetalhesConsultaRPS, scope=tpListaDetalhesConsultaRPS, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1469, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=50, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1469, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpListaDetalhesConsultaRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'Detalhe')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1469, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpListaDetalhesConsultaRPS._Automaton = _BuildAutomaton_25()




tpListaErros._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Erro'), tpEvento, scope=tpListaErros, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1477, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1477, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpListaErros._UseForTag(pyxb.namespace.ExpandedName(None, 'Erro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1477, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpListaErros._Automaton = _BuildAutomaton_26()




tpListaItens._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Item'), tpItens, scope=tpListaItens, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1485, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=25, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1485, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpListaItens._UseForTag(pyxb.namespace.ExpandedName(None, 'Item')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1485, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpListaItens._Automaton = _BuildAutomaton_27()




tpListaNFSeRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChaveNFSeRPS'), tpChaveNFeRPS, scope=tpListaNFSeRPS, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1493, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1493, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpListaNFSeRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ChaveNFSeRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1493, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpListaNFSeRPS._Automaton = _BuildAutomaton_28()




tpListaNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ConsultaNFSe'), tpConsultaNFSe, scope=tpListaNFSe, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1501, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1501, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpListaNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ConsultaNFSe')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1501, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpListaNFSe._Automaton = _BuildAutomaton_29()




tpListaNFSeConsultaNota._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Nota'), tpNFSe, scope=tpListaNFSeConsultaNota, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1509, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1509, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tpListaNFSeConsultaNota._UseForTag(pyxb.namespace.ExpandedName(None, 'Nota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1509, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tpListaNFSeConsultaNota._Automaton = _BuildAutomaton_30()




tpLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RPS'), tpRPS, scope=tpLote, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1517, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpLote._UseForTag(pyxb.namespace.ExpandedName(None, 'RPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1517, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpLote._Automaton = _BuildAutomaton_31()




tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNota'), tpNumero, scope=tpNFSe, documentation='Número da Nota Fiscal', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1527, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataProcessamento'), pyxb.binding.datatypes.dateTime, scope=tpNFSe, documentation='Data que a Nota Fiscal foi Processada', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1532, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroLote'), tpNumero, scope=tpNFSe, documentation='Número do Lote', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1538, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao'), tpCodigoVerificacao, scope=tpNFSe, documentation='Código de Verificacao', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1543, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Assinatura'), tpAssinatura, scope=tpNFSe, documentation='Assinatura digital do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1548, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), tpInscricaoMunicipal, scope=tpNFSe, documentation='Informe a Inscrição Municipal do Prestador', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1554, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), tpRazaoSocialPrestador, scope=tpNFSe, documentation='Informe a Razao Social do Prestador', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1559, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoRPS'), tpTipoRPS, scope=tpNFSe, documentation='Informe o Tipo do RPS emitido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1564, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SerieRPS'), tpSerieRPS, scope=tpNFSe, documentation='Informe a Série do RPS emitido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1569, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), tpNumero, scope=tpNFSe, documentation='Informe o Número do RPS emitido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1574, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), tpDataHora, scope=tpNFSe, documentation='Informe a Data de emissão do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1579, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SituacaoRPS'), tpSituacaoRPS, scope=tpNFSe, documentation='Informe o Status do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1584, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SerieRPSSubstituido'), tpSerieRPSSubstituido, scope=tpNFSe, documentation='Informe a Série do RPS substituído.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1589, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPSSubstituido'), tpNumeroComZero, scope=tpNFSe, documentation='Informe o Número do RPS substituído.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1594, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida'), tpNumeroComZero, scope=tpNFSe, documentation='Informe o Número da NFSe substituída.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1599, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida'), tpDataHoraNulo, scope=tpNFSe, documentation='Informe a Data de Emissão da NFSe substituída.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1604, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), tpSeriePrestacao, scope=tpNFSe, documentation='Série de prestação', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1609, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador'), tpInscricaoMunicipalNulo, scope=tpNFSe, documentation='Informe a Inscrição Municipal do Tomador. ATENÇÃO: Este campo só deverá ser preenchido para tomadores estabelecidos no município. Quando este campo for preenchido, seu conteúdo será considerado como prioritário com relação ao campo de CPF/CNPJ do Tomador, sendo utilizado para identificar o Tomador e recuperar seus dados da base de dados da Prefeitura.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1614, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), tpCPFCNPJ, scope=tpNFSe, documentation='Informe o CPF/CNPJ do tomador do serviço. O conteúdo deste campo será ignorado caso o campo InscricaoMunicipalTomador esteja preenchido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1619, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador'), tpRazaoSocial, scope=tpNFSe, documentation='Informe o Nome/Razão Social do tomador. Este campo é obrigatório apenas para tomadores Pessoa Jurídica (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ ou a Inscrição Municipal do tomador pertença ao município.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1624, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DocTomadorEstrangeiro'), tpDocTomadorEstrangeiro, scope=tpNFSe, documentation='Informe o Documento de Identificação do tomador. Este campo é obrigatório apenas para tomadores estrageiros, ou seja quando no CidadeTomador que indica o Codigo SIAFI da cidade do tomador for informado 0009999', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1629, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoLogradouroTomador'), tpTipoLogradouro, scope=tpNFSe, documentation='Informe o Tipo do Logradouro do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1634, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LogradouroTomador'), tpLogradouro, scope=tpNFSe, documentation='Informe o Logradouro do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1639, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroEnderecoTomador'), tpNumeroEndereco, scope=tpNFSe, documentation='Informe o Número do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1644, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ComplementoEnderecoTomador'), tpComplementoEndereco, scope=tpNFSe, documentation='Informe o Comlpemento do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1649, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoBairroTomador'), tpTipoBairro, scope=tpNFSe, documentation='Informe o Tipo do Bairro do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1654, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BairroTomador'), tpBairro, scope=tpNFSe, documentation='Informe o Bairro do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1659, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CidadeTomador'), tpCodCidade, scope=tpNFSe, documentation='Informe a Cidade do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1664, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CidadeTomadorDescricao'), tpCidadeTomadorDescricao, scope=tpNFSe, documentation='Informe a Descricao Cidade do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1669, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CEPTomador'), tpCEPNulo, scope=tpNFSe, documentation='Informe o CEP do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1674, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EmailTomador'), tpEmail, scope=tpNFSe, documentation='Informe o e-mail do tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1679, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoAtividade'), tpCodigoAtividade, scope=tpNFSe, documentation='Informe o código da atividade do RPS. Este código deve pertencer à lista CNAE.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1684, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaAtividade'), tpAliquota, scope=tpNFSe, documentation='Informe o valor da alíquota.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1689, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento'), tpTipoRecolhimento, scope=tpNFSe, documentation='Informe a retenção.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1694, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao'), tpCodCidade, scope=tpNFSe, documentation='Informe o Município da Prestação do Serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1699, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacaoDescricao'), tpCidadeDescricao, scope=tpNFSe, documentation='Informe o Município da Prestação do Serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1704, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Operacao'), tpOperacao, scope=tpNFSe, documentation='Informe a Operação da Prestação do Serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1709, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Tributacao'), tpTributacao, scope=tpNFSe, documentation='Informe o tipo de tributação do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1714, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorPIS'), tpValor, scope=tpNFSe, documentation='Informe o valor da retenção do PIS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1719, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCOFINS'), tpValor, scope=tpNFSe, documentation='Informe o valor da retenção do COFINS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1724, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorINSS'), tpValor, scope=tpNFSe, documentation='Informe o valor da retenção do INSS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1729, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorIR'), tpValor, scope=tpNFSe, documentation='Informe o valor da retenção do IR.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1734, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCSLL'), tpValor, scope=tpNFSe, documentation='Informe o valor da retenção do CSLL.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1739, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaPIS'), tpAliquota, scope=tpNFSe, documentation='Informe a Alíquota da retenção do PIS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1744, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaCOFINS'), tpAliquota, scope=tpNFSe, documentation='Informe a Alíquota da retenção do COFINS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1749, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaINSS'), tpAliquota, scope=tpNFSe, documentation='Informe a Alíquota da retenção do INSS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1754, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaIR'), tpAliquota, scope=tpNFSe, documentation='Informe a Alíquota da retenção do IR.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1759, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaCSLL'), tpAliquota, scope=tpNFSe, documentation='Informe a Alíquota da retenção do CSLL.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1764, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DescricaoRPS'), tpDescricaoRPS, scope=tpNFSe, documentation='Descrição da Nota.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1769, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DDDPrestador'), tpDDDNulo, scope=tpNFSe, documentation='DDD do Prestador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1774, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TelefonePrestador'), tpFoneNulo, scope=tpNFSe, documentation='Telefone do Prestador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1779, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DDDTomador'), tpDDDNulo, scope=tpNFSe, documentation='DDD do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1784, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TelefoneTomador'), tpFoneNulo, scope=tpNFSe, documentation='Telefone do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1789, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MotCancelamento'), tpMotCancelamento, scope=tpNFSe, documentation='Informe o Motivo do Cancelamento.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1794, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario'), tpCPFCNPJnulo, scope=tpNFSe, documentation='CPF/CNPJ do intermediário do serviço. Campo não é obrigatório, deve ser informado quando houver um intermediário entre o tomador e o prestador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1799, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Deducoes'), tpListaDeducoes, scope=tpNFSe, documentation='Lista de Deduções.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1804, 3)))

tpNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Itens'), tpListaItens, scope=tpNFSe, documentation='Lista de Itens.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1809, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1532, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1538, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1548, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1589, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1594, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1599, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1604, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1609, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1614, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1629, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1649, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1674, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1679, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1719, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1724, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1729, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1734, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1739, 3))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1744, 3))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1749, 3))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1754, 3))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1759, 3))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1764, 3))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1769, 3))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1774, 3))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1779, 3))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1784, 3))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1789, 3))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1794, 3))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1799, 3))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1804, 3))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1809, 3))
    counters.add(cc_31)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNota')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1527, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataProcessamento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1532, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroLote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1538, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoVerificacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1543, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Assinatura')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1548, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1554, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1559, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1564, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'SerieRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1569, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1574, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1579, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'SituacaoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1584, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'SerieRPSSubstituido')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1589, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPSSubstituido')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1594, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1599, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1604, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'SeriePrestacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1609, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1614, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1619, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1624, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DocTomadorEstrangeiro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1629, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoLogradouroTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1634, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'LogradouroTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1639, 3))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroEnderecoTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1644, 3))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ComplementoEnderecoTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1649, 3))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoBairroTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1654, 3))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'BairroTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1659, 3))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CidadeTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1664, 3))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CidadeTomadorDescricao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1669, 3))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CEPTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1674, 3))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'EmailTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1679, 3))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoAtividade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1684, 3))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaAtividade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1689, 3))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1694, 3))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1699, 3))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacaoDescricao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1704, 3))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Operacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1709, 3))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Tributacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1714, 3))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorPIS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1719, 3))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCOFINS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1724, 3))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorINSS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1729, 3))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorIR')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1734, 3))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCSLL')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1739, 3))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaPIS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1744, 3))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaCOFINS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1749, 3))
    st_44 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaINSS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1754, 3))
    st_45 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaIR')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1759, 3))
    st_46 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaCSLL')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1764, 3))
    st_47 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_47)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DescricaoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1769, 3))
    st_48 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_48)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DDDPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1774, 3))
    st_49 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_49)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'TelefonePrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1779, 3))
    st_50 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_50)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'DDDTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1784, 3))
    st_51 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_51)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'TelefoneTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1789, 3))
    st_52 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_52)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'MotCancelamento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1794, 3))
    st_53 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_53)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1799, 3))
    st_54 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_54)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Deducoes')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1804, 3))
    st_55 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_55)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(tpNFSe._UseForTag(pyxb.namespace.ExpandedName(None, 'Itens')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1809, 3))
    st_56 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_56)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
         ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
         ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
         ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
         ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
         ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
         ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
         ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
         ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
         ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
         ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
         ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
         ]))
    transitions.append(fac.Transition(st_39, [
         ]))
    transitions.append(fac.Transition(st_40, [
         ]))
    transitions.append(fac.Transition(st_41, [
         ]))
    transitions.append(fac.Transition(st_42, [
         ]))
    transitions.append(fac.Transition(st_43, [
         ]))
    transitions.append(fac.Transition(st_44, [
         ]))
    transitions.append(fac.Transition(st_45, [
         ]))
    transitions.append(fac.Transition(st_46, [
         ]))
    transitions.append(fac.Transition(st_47, [
         ]))
    transitions.append(fac.Transition(st_48, [
         ]))
    transitions.append(fac.Transition(st_49, [
         ]))
    transitions.append(fac.Transition(st_50, [
         ]))
    transitions.append(fac.Transition(st_51, [
         ]))
    transitions.append(fac.Transition(st_52, [
         ]))
    transitions.append(fac.Transition(st_53, [
         ]))
    transitions.append(fac.Transition(st_54, [
         ]))
    transitions.append(fac.Transition(st_55, [
         ]))
    transitions.append(fac.Transition(st_56, [
         ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_47._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_48._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_49._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_50._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_51._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_52._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_53._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_54._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_55, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_55._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_56, [
        fac.UpdateInstruction(cc_31, True) ]))
    st_56._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpNFSe._Automaton = _BuildAutomaton_32()




tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Assinatura'), tpAssinatura, scope=tpRPS, documentation='Assinatura digital do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1821, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), tpInscricaoMunicipal, scope=tpRPS, documentation='Informe a Inscrição Municipal do Prestador', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1826, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador'), tpRazaoSocialPrestador, scope=tpRPS, documentation='Informe a Razao Social do Prestador', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1831, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoRPS'), tpTipoRPS, scope=tpRPS, documentation='Informe o Tipo do RPS emitido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1836, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SerieRPS'), tpSerieRPS, scope=tpRPS, documentation='Informe a Série do RPS emitido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1841, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPS'), tpNumero, scope=tpRPS, documentation='Informe o Número do RPS emitido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1846, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS'), pyxb.binding.datatypes.dateTime, scope=tpRPS, documentation='Informe a Data de emissão do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1851, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SituacaoRPS'), tpSituacaoRPS, scope=tpRPS, documentation='Informe o Status do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1856, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SerieRPSSubstituido'), tpSerieRPSSubstituido, scope=tpRPS, documentation='Informe a Série do RPS substituído.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1861, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroRPSSubstituido'), tpNumeroComZero, scope=tpRPS, documentation='Informe o Número do RPS substituído.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1866, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida'), tpNumeroComZero, scope=tpRPS, documentation='Informe o Número da NFSe substituída.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1871, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida'), tpDataNulo, scope=tpRPS, documentation='Informe a Data de Emissão da NFSe substituída.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1876, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), tpSeriePrestacao, scope=tpRPS, documentation='Informe o Documento de Prestação', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1881, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador'), tpInscricaoMunicipalNulo, scope=tpRPS, documentation='Informe a Inscrição Municipal do Tomador. ATENÇÃO: Este campo só deverá ser preenchido para tomadores estabelecidos no município. Quando este campo for preenchido, seu conteúdo será considerado como prioritário com relação ao campo de CPF/CNPJ do Tomador, sendo utilizado para identificar o Tomador e recuperar seus dados da base de dados da Prefeitura.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1886, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador'), tpCPFCNPJ, scope=tpRPS, documentation='Informe o CPF/CNPJ do tomador do serviço. O conteúdo deste campo será ignorado caso o campo InscricaoMunicipalTomador esteja preenchido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1891, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador'), tpRazaoSocial, scope=tpRPS, documentation='Informe o Nome/Razão Social do tomador. Este campo é obrigatório apenas para tomadores Pessoa Jurídica (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ ou a Inscrição Municipal do tomador pertença ao município.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1896, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DocTomadorEstrangeiro'), tpDocTomadorEstrangeiro, scope=tpRPS, documentation='Informe o Documento de Identificação do tomador. Este campo é obrigatório apenas para tomadores estrageiros, ou seja quando no CidadeTomador que indica o Codigo SIAFI da cidade do tomador for informado 0009999', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1901, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoLogradouroTomador'), tpTipoLogradouro, scope=tpRPS, documentation='Informe o Tipo do Logradouro do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1906, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LogradouroTomador'), tpLogradouro, scope=tpRPS, documentation='Informe o Logradouro do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1911, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroEnderecoTomador'), tpNumeroEndereco, scope=tpRPS, documentation='Informe o Número do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1916, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ComplementoEnderecoTomador'), tpComplementoEndereco, scope=tpRPS, documentation='Informe o Comlpemento do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1921, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoBairroTomador'), tpTipoBairro, scope=tpRPS, documentation='Informe o Tipo do Bairro do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1926, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BairroTomador'), tpBairro, scope=tpRPS, documentation='Informe o Bairro do Endereço do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1931, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CidadeTomador'), tpCodCidade, scope=tpRPS, documentation='Informe a Cidade do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1936, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CidadeTomadorDescricao'), tpCidadeTomadorDescricao, scope=tpRPS, documentation='Informe a Descricao da Cidade do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1941, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CEPTomador'), tpCEP, scope=tpRPS, documentation='Informe o CEP do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1946, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EmailTomador'), tpEmail, scope=tpRPS, documentation='Informe o e-mail do tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1951, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodigoAtividade'), tpCodigoAtividade, scope=tpRPS, documentation='Informe o código da atividade do RPS. Este código deve pertencer à lista CNAE.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1956, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaAtividade'), tpAliquota, scope=tpRPS, documentation='Informe o valor da alíquota.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1961, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento'), tpTipoRecolhimento, scope=tpRPS, documentation='Informe a retenção.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1966, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao'), tpCodCidade, scope=tpRPS, documentation='Informe o Município da Prestação do Serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1971, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacaoDescricao'), tpCidadeDescricao, scope=tpRPS, documentation='Informe o Município da Prestação do Serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1976, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Operacao'), tpOperacao, scope=tpRPS, documentation='Informe a Operação da Prestação do Serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1981, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Tributacao'), tpTributacao, scope=tpRPS, documentation='Informe o tipo de tributação do RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1986, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorPIS'), tpValor, scope=tpRPS, documentation='Informe o valor da retenção do PIS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1991, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCOFINS'), tpValor, scope=tpRPS, documentation='Informe o valor da retenção do COFINS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1996, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorINSS'), tpValor, scope=tpRPS, documentation='Informe o valor da retenção do INSS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2001, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorIR'), tpValor, scope=tpRPS, documentation='Informe o valor da retenção do IR.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2006, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorCSLL'), tpValor, scope=tpRPS, documentation='Informe o valor da retenção do CSLL.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2011, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaPIS'), tpAliquota, scope=tpRPS, documentation='Informe a Alíquota da retenção do PIS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2016, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaCOFINS'), tpAliquota, scope=tpRPS, documentation='Informe a Alíquota da retenção do COFINS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2021, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaINSS'), tpAliquota, scope=tpRPS, documentation='Informe a Alíquota da retenção do INSS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2026, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaIR'), tpAliquota, scope=tpRPS, documentation='Informe a Alíquota da retenção do IR.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2031, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AliquotaCSLL'), tpAliquota, scope=tpRPS, documentation='Informe a Alíquota da retenção do CSLL.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2036, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DescricaoRPS'), tpDescricaoRPS, scope=tpRPS, documentation='Descrição da Nota.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2041, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DDDPrestador'), tpDDDNulo, scope=tpRPS, documentation='DDD do Prestador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2046, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TelefonePrestador'), tpFoneNulo, scope=tpRPS, documentation='Telefone do Prestador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2051, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DDDTomador'), tpDDDNulo, scope=tpRPS, documentation='DDD do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2056, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TelefoneTomador'), tpFoneNulo, scope=tpRPS, documentation='Telefone do Tomador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2061, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MotCancelamento'), tpMotCancelamento, scope=tpRPS, documentation='Informe o Motivo do Cancelamento.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2066, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario'), tpCPFCNPJnulo, scope=tpRPS, documentation='Informe o CPF/CNPJ do intermediário do serviço. Campo não é obrigatório, deve ser informado quando houver um intermediário entre o tomador e o prestador.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2071, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Deducoes'), tpListaDeducoes, scope=tpRPS, documentation='Lista de Deduções.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2076, 3)))

tpRPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Itens'), tpListaItens, scope=tpRPS, documentation='Lista de Itens.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2081, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1861, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1866, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1871, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1876, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1901, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1921, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2066, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2071, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2076, 3))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'Assinatura')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1821, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1826, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1831, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1836, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'SerieRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1841, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1846, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1851, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'SituacaoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1856, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'SerieRPSSubstituido')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1861, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroRPSSubstituido')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1866, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroNFSeSubstituida')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1871, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEmissaoNFSeSubstituida')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1876, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'SeriePrestacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1881, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1886, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1891, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1896, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'DocTomadorEstrangeiro')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1901, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoLogradouroTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1906, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'LogradouroTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1911, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroEnderecoTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1916, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ComplementoEnderecoTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1921, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoBairroTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1926, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'BairroTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1931, 3))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CidadeTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1936, 3))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CidadeTomadorDescricao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1941, 3))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CEPTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1946, 3))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'EmailTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1951, 3))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CodigoAtividade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1956, 3))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaAtividade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1961, 3))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'TipoRecolhimento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1966, 3))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1971, 3))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'MunicipioPrestacaoDescricao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1976, 3))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'Operacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1981, 3))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'Tributacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1986, 3))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorPIS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1991, 3))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCOFINS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 1996, 3))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorINSS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2001, 3))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorIR')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2006, 3))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorCSLL')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2011, 3))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaPIS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2016, 3))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaCOFINS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2021, 3))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaINSS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2026, 3))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaIR')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2031, 3))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'AliquotaCSLL')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2036, 3))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'DescricaoRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2041, 3))
    st_44 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'DDDPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2046, 3))
    st_45 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'TelefonePrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2051, 3))
    st_46 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'DDDTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2056, 3))
    st_47 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_47)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'TelefoneTomador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2061, 3))
    st_48 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_48)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'MotCancelamento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2066, 3))
    st_49 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_49)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJIntermediario')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2071, 3))
    st_50 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_50)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'Deducoes')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2076, 3))
    st_51 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_51)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tpRPS._UseForTag(pyxb.namespace.ExpandedName(None, 'Itens')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/Tipos.xsd', 2081, 3))
    st_52 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_52)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
         ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
         ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
         ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
         ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
         ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
         ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
         ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
         ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
         ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
         ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
         ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
         ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
         ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
         ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
         ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
         ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
         ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
         ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
         ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
         ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
         ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
         ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
         ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
         ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
         ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_47, [
         ]))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, [
         ]))
    st_47._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, [
         ]))
    transitions.append(fac.Transition(st_50, [
         ]))
    transitions.append(fac.Transition(st_51, [
         ]))
    transitions.append(fac.Transition(st_52, [
         ]))
    st_48._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_49._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_50._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_51._set_transitionSet(transitions)
    transitions = []
    st_52._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tpRPS._Automaton = _BuildAutomaton_33()

