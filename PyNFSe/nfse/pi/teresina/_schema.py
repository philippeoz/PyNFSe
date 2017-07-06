# ./_schema.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:599fc53023058a86461294fe9c0afc6727c4a891
# Generated 2017-07-04 11:52:35.944429 by PyXB version 1.2.5 using Python 3.5.3.final.0
# Namespace http://localhost:8080/WsNFe2/lote

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
import _tipos as _ImportedBinding_tipos
import pyxb.binding.datatypes
import _ds as _ImportedBinding_ds

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://localhost:8080/WsNFe2/lote', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding_ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 12, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, None)

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 13, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCid uses Python identifier CodCid
    __CodCid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCid'), 'CodCid', '__httplocalhost8080WsNFe2lote_CTD_ANON__CodCid', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 15, 7), )

    
    CodCid = property(__CodCid.value, __CodCid.set, None, None)

    
    # Element IMPrestador uses Python identifier IMPrestador
    __IMPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IMPrestador'), 'IMPrestador', '__httplocalhost8080WsNFe2lote_CTD_ANON__IMPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 16, 7), )

    
    IMPrestador = property(__IMPrestador.value, __IMPrestador.set, None, None)

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON__CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 17, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, None)

    
    # Element SeriePrestacao uses Python identifier SeriePrestacao
    __SeriePrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), 'SeriePrestacao', '__httplocalhost8080WsNFe2lote_CTD_ANON__SeriePrestacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 18, 7), )

    
    SeriePrestacao = property(__SeriePrestacao.value, __SeriePrestacao.set, None, None)

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON__Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 19, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, None)

    _ElementMap.update({
        __CodCid.name() : __CodCid,
        __IMPrestador.name() : __IMPrestador,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __SeriePrestacao.name() : __SeriePrestacao,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para  Cancelamento de NFSe.Este Schema XML é utilizado pelos Prestadores de serviços cancelarem NFSe emitidas por eles."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_2_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 17, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do pedido.')

    
    # Element Lote uses Python identifier Lote
    __Lote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Lote'), 'Lote', '__httplocalhost8080WsNFe2lote_CTD_ANON_2_Lote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 46, 4), )

    
    Lote = property(__Lote.value, __Lote.set, None, 'Detalhe do pedido de cancelamento de NFSe. Cada detalhe deverá conter a Chave de uma NFSe e sua respectiva assinatura de cancelamento.')

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httplocalhost8080WsNFe2lote_CTD_ANON_2_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __Lote.name() : __Lote,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do pedido."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 21, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_3_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 23, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Informe o Codigo da Cidade.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_3_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 28, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.')

    
    # Element transacao uses Python identifier transacao
    __transacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transacao'), 'transacao', '__httplocalhost8080WsNFe2lote_CTD_ANON_3_transacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 33, 7), )

    
    transacao = property(__transacao.value, __transacao.set, None, 'Informe se as NF-e a serem canceladas farão parte de uma mesma transação. True - As NF-e só serão canceladas se não ocorrer nenhum evento de erro durante o processamento de todo o lote; False - As NF-e aptas a serem canceladas serão canceladas, mesmo que ocorram eventos de erro durante processamento do cancelamento de outras NF-e deste lote.')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_3_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 38, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Informe a Versão do Schema XML utilizado.')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __transacao.name() : __transacao,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para REQUISIçÂO de Consulta de Lote de RPS.Este Schema XML é utilizado pelos Prestadores de serviços para consultarem Lote de RPS emitidos por eles."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_4_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 14, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do pedido.')

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do pedido."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 18, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_5_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 20, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Informe o Codigo da Cidade.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_5_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 25, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_5_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 30, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Informe a Versão do Schema XML utilizado.')

    
    # Element NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroLote'), 'NumeroLote', '__httplocalhost8080WsNFe2lote_CTD_ANON_5_NumeroLote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 35, 7), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, 'Informe o Número do Lote a ser consultado.')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __Versao.name() : __Versao,
        __NumeroLote.name() : __NumeroLote
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para  Consulta de NFSe.Este Schema XML é utilizado pelos Prestadores de serviços consultarem NFSe emitidas por eles."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_6_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 17, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do pedido.')

    
    # Element Lote uses Python identifier Lote
    __Lote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Lote'), 'Lote', '__httplocalhost8080WsNFe2lote_CTD_ANON_6_Lote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 46, 4), )

    
    Lote = property(__Lote.value, __Lote.set, None, 'Detalhe do pedido de consulta de NFSe. Cada detalhe deverá conter a Chave de uma NFSe e sua respectiva assinatura de consulta.')

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httplocalhost8080WsNFe2lote_CTD_ANON_6_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __Lote.name() : __Lote,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do pedido."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 21, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_7_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 23, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Informe o Codigo da Cidade.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_7_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 28, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.')

    
    # Element transacao uses Python identifier transacao
    __transacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transacao'), 'transacao', '__httplocalhost8080WsNFe2lote_CTD_ANON_7_transacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 33, 7), )

    
    transacao = property(__transacao.value, __transacao.set, None, 'Informe se as NF-e a serem consultadas farão parte de uma mesma transação. Informe sempre True.')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_7_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 38, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Informe a Versão do Schema XML utilizado.')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __transacao.name() : __transacao,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para REQUISIÇAO de consultas
				de notas que foram enviadas por lote de RPS.Este Schema XML é utilizado pelos prestadores
				de serviços para consultas de notas que foram enviadas por lote de
				RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_8_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 19, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do pedido.')

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httplocalhost8080WsNFe2lote_CTD_ANON_8_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do pedido."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 23, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_9_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 25, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Informe o Codigo da Cidade.\n\t\t\t\t\t\t\t\t\t')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_9_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 32, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'Informe o CPF/CNPJ do Remetente\n\t\t\t\t\t\t\t\t\t\tautorizado a transmitir a mensagem XML.')

    
    # Element InscricaoMunicipalPrestador uses Python identifier InscricaoMunicipalPrestador
    __InscricaoMunicipalPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), 'InscricaoMunicipalPrestador', '__httplocalhost8080WsNFe2lote_CTD_ANON_9_InscricaoMunicipalPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 39, 7), )

    
    InscricaoMunicipalPrestador = property(__InscricaoMunicipalPrestador.value, __InscricaoMunicipalPrestador.set, None, 'Informe a Inscrição Municipal do\n\t\t\t\t\t\t\t\t\t\tPrestador')

    
    # Element dtInicio uses Python identifier dtInicio
    __dtInicio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dtInicio'), 'dtInicio', '__httplocalhost8080WsNFe2lote_CTD_ANON_9_dtInicio', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 46, 7), )

    
    dtInicio = property(__dtInicio.value, __dtInicio.set, None, 'Informe a data de início do período\n\t\t\t\t\t\t\t\t\t\ttransmitido (AAAA-MM-DD).')

    
    # Element dtFim uses Python identifier dtFim
    __dtFim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dtFim'), 'dtFim', '__httplocalhost8080WsNFe2lote_CTD_ANON_9_dtFim', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 53, 7), )

    
    dtFim = property(__dtFim.value, __dtFim.set, None, 'Informe a data final do período\n\t\t\t\t\t\t\t\t\t\ttransmitido (AAAA-MM-DD).')

    
    # Element NotaInicial uses Python identifier NotaInicial
    __NotaInicial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NotaInicial'), 'NotaInicial', '__httplocalhost8080WsNFe2lote_CTD_ANON_9_NotaInicial', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 60, 7), )

    
    NotaInicial = property(__NotaInicial.value, __NotaInicial.set, None, 'Numero da nota inicial da consulta. Ou\n\t\t\t\t\t\t\t\t\t\tseja a consulta ira retornar as notas no periodo, onde o\n\t\t\t\t\t\t\t\t\t\tnumero da nota seja maior ou igual a esse numero. O retorno\n\t\t\t\t\t\t\t\t\t\tnão pode ultrapassar 500Kb. Caso não tenha o numero da nota,\n\t\t\t\t\t\t\t\t\t\tpassar o valor Zero, será retornado as notas geradas no\n\t\t\t\t\t\t\t\t\t\tperiodo até o limite de 500kb.')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_9_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 71, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Informe a Versão.')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httplocalhost8080WsNFe2lote_CTD_ANON_9_Id', pyxb.binding.datatypes.string)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 79, 6)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 79, 6)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __InscricaoMunicipalPrestador.name() : __InscricaoMunicipalPrestador,
        __dtInicio.name() : __dtInicio,
        __dtFim.name() : __dtFim,
        __NotaInicial.name() : __NotaInicial,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para envio de lote de RPS.Este Schema XML é utilizado pelos prestadores
				de serviços para substituição em lote de RPS por NFS-e.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_10_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 17, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do Lote.')

    
    # Element Lote uses Python identifier Lote
    __Lote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Lote'), 'Lote', '__httplocalhost8080WsNFe2lote_CTD_ANON_10_Lote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 139, 4), )

    
    Lote = property(__Lote.value, __Lote.set, None, 'Informe os RPS a serem substituidos por\n\t\t\t\t\t\t\tNF-e.')

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httplocalhost8080WsNFe2lote_CTD_ANON_10_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __Lote.name() : __Lote,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do Lote."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 21, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 23, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Informe o Codigo da Cidade no Padrão SIAFI.\n\t\t\t\t\t\t\t\t\t')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 29, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, '\n\t\t\t\t\t\t\t\t\t\tCNPJ do contribuinte ou CPF do Responsável Legal autorizado a entregar o lote.\n\t\t\t\t\t\t\t\t\t')

    
    # Element RazaoSocialRemetente uses Python identifier RazaoSocialRemetente
    __RazaoSocialRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialRemetente'), 'RazaoSocialRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_RazaoSocialRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 36, 7), )

    
    RazaoSocialRemetente = property(__RazaoSocialRemetente.value, __RazaoSocialRemetente.set, None, '\n\t\t\t\t\t\t\t\t\t\tInforme o Nome do Contribuinte ou do Responsável Legal\n\t\t\t\t\t\t\t\t\t')

    
    # Element transacao uses Python identifier transacao
    __transacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transacao'), 'transacao', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_transacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 43, 7), )

    
    transacao = property(__transacao.value, __transacao.set, None, '\n\t\t\t\t\t\t\t\t\t\tInforme se os RPS a serem\n\t\t\t\t\t\t\t\t\t\tsubstituídos por\n\t\t\t\t\t\t\t\t\t\tNF-e farão\n\t\t\t\t\t\t\t\t\t\tparte de uma mesma transação.\n\t\t\t\t\t\t\t\t\t\tTrue - Os RPS só serão\n\t\t\t\t\t\t\t\t\t\tsubstituídos por NF-e se não\n\t\t\t\t\t\t\t\t\t\tocorrer nenhum evento de erro\n\t\t\t\t\t\t\t\t\t\tdurante o processamento de todo\n\t\t\t\t\t\t\t\t\t\to lote; False - Os RPS válidos\n\t\t\t\t\t\t\t\t\t\tserão substituídos por NF-e,\n\t\t\t\t\t\t\t\t\t\tmesmo que ocorram eventos de\n\t\t\t\t\t\t\t\t\t\terro durante processamento de\n\t\t\t\t\t\t\t\t\t\toutros RPS deste lote. Por definição\n\t\t\t\t\t\t\t\t\t\testão sendo aceitos apenas lotes com RPS válidos,\n\t\t\t\t\t\t\t\t\t\to lote é\n\t\t\t\t\t\t\t\t\t\trecusado caso haja algum RPS inválido.\n\t\t\t\t\t\t\t\t\t')

    
    # Element dtInicio uses Python identifier dtInicio
    __dtInicio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dtInicio'), 'dtInicio', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_dtInicio', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 66, 7), )

    
    dtInicio = property(__dtInicio.value, __dtInicio.set, None, '\n\t\t\t\t\t\t\t\t\t\tInforme a data de início do\n\t\t\t\t\t\t\t\t\t\tperíodo\n\t\t\t\t\t\t\t\t\t\ttransmitido\n\t\t\t\t\t\t\t\t\t\t(AAAA-MM-DD).\n\t\t\t\t\t\t\t\t\t')

    
    # Element dtFim uses Python identifier dtFim
    __dtFim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dtFim'), 'dtFim', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_dtFim', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 76, 7), )

    
    dtFim = property(__dtFim.value, __dtFim.set, None, '\n\t\t\t\t\t\t\t\t\t\tInforme a data final do período\n\t\t\t\t\t\t\t\t\t\ttransmitido\n\t\t\t\t\t\t\t\t\t\t(AAAA-MM-DD).\n\t\t\t\t\t\t\t\t\t')

    
    # Element QtdRPS uses Python identifier QtdRPS
    __QtdRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'QtdRPS'), 'QtdRPS', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_QtdRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 85, 7), )

    
    QtdRPS = property(__QtdRPS.value, __QtdRPS.set, None, '\n\t\t\t\t\t\t\t\t\t\tInforme o total de RPS contidos\n\t\t\t\t\t\t\t\t\t\tna mensagem\n\t\t\t\t\t\t\t\t\t\tXML. OBS: O xml não pode ultrapassar o tamanho maximo de 500kb.\n\t\t\t\t\t\t\t\t\t')

    
    # Element ValorTotalServicos uses Python identifier ValorTotalServicos
    __ValorTotalServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), 'ValorTotalServicos', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_ValorTotalServicos', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 94, 7), )

    
    ValorTotalServicos = property(__ValorTotalServicos.value, __ValorTotalServicos.set, None, '\n\t\t\t\t\t\t\t\t\t\tInforme o valor total dos\n\t\t\t\t\t\t\t\t\t\tserviços prestados\n\t\t\t\t\t\t\t\t\t\tdos RPS\n\t\t\t\t\t\t\t\t\t\tcontidos na mensagem XML.\n\t\t\t\t\t\t\t\t\t')

    
    # Element ValorTotalDeducoes uses Python identifier ValorTotalDeducoes
    __ValorTotalDeducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), 'ValorTotalDeducoes', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_ValorTotalDeducoes', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 104, 7), )

    
    ValorTotalDeducoes = property(__ValorTotalDeducoes.value, __ValorTotalDeducoes.set, None, '\n\t\t\t\t\t\t\t\t\t\tInforme o valor total das\n\t\t\t\t\t\t\t\t\t\tdeduções dos RPS\n\t\t\t\t\t\t\t\t\t\tcontidos na\n\t\t\t\t\t\t\t\t\t\tmensagem XML.\n\t\t\t\t\t\t\t\t\t')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 114, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, '\n\t\t\t\t\t\t\t\t\t\tInforme a Versão do Schema XML\n\t\t\t\t\t\t\t\t\t\tutilizado.\n\t\t\t\t\t\t\t\t\t')

    
    # Element MetodoEnvio uses Python identifier MetodoEnvio
    __MetodoEnvio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MetodoEnvio'), 'MetodoEnvio', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_MetodoEnvio', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 122, 7), )

    
    MetodoEnvio = property(__MetodoEnvio.value, __MetodoEnvio.set, None, 'Informe o Método de Envio')

    
    # Element VersaoComponente uses Python identifier VersaoComponente
    __VersaoComponente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'VersaoComponente'), 'VersaoComponente', '__httplocalhost8080WsNFe2lote_CTD_ANON_11_VersaoComponente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 128, 7), )

    
    VersaoComponente = property(__VersaoComponente.value, __VersaoComponente.set, None, 'Versão da DLL de envio de lote. Não é necessário informar esse campo caso não utilize a DLL.\n\t\t\t\t\t\t\t\t\t')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __RazaoSocialRemetente.name() : __RazaoSocialRemetente,
        __transacao.name() : __transacao,
        __dtInicio.name() : __dtInicio,
        __dtFim.name() : __dtFim,
        __QtdRPS.name() : __QtdRPS,
        __ValorTotalServicos.name() : __ValorTotalServicos,
        __ValorTotalDeducoes.name() : __ValorTotalDeducoes,
        __Versao.name() : __Versao,
        __MetodoEnvio.name() : __MetodoEnvio,
        __VersaoComponente.name() : __VersaoComponente
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para RETORNO de Pedidos de cancelamento de NFSe.Este Schema XML é utilizado pelo Web Service para informar aos prestadores de serviços qual o resultado do pedido de cancelamento de NFSe."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_12_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 14, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do pedido.')

    
    # Element NotasCanceladas uses Python identifier NotasCanceladas
    __NotasCanceladas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NotasCanceladas'), 'NotasCanceladas', '__httplocalhost8080WsNFe2lote_CTD_ANON_12_NotasCanceladas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 44, 4), )

    
    NotasCanceladas = property(__NotasCanceladas.value, __NotasCanceladas.set, None, 'Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.')

    
    # Element Alertas uses Python identifier Alertas
    __Alertas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Alertas'), 'Alertas', '__httplocalhost8080WsNFe2lote_CTD_ANON_12_Alertas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 49, 4), )

    
    Alertas = property(__Alertas.value, __Alertas.set, None, 'Elemento que representa a ocorrência de eventos de alerta durante o processamento da mensagem XML.')

    
    # Element Erros uses Python identifier Erros
    __Erros = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Erros'), 'Erros', '__httplocalhost8080WsNFe2lote_CTD_ANON_12_Erros', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 54, 4), )

    
    Erros = property(__Erros.value, __Erros.set, None, 'Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.')

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __NotasCanceladas.name() : __NotasCanceladas,
        __Alertas.name() : __Alertas,
        __Erros.name() : __Erros
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do pedido."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 18, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_13_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 20, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Informe o Codigo da Cidade.')

    
    # Element Sucesso uses Python identifier Sucesso
    __Sucesso = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Sucesso'), 'Sucesso', '__httplocalhost8080WsNFe2lote_CTD_ANON_13_Sucesso', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 25, 7), )

    
    Sucesso = property(__Sucesso.value, __Sucesso.set, None, 'Notas Canceladas com Sucesso.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_13_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 30, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_13_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 36, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Informe a Versão do Schema XML utilizado.')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __Sucesso.name() : __Sucesso,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para RETORNO de consulta de lote de RPS.Este Schema XML é utilizado pelo Web Service para informar aos prestadores de serviços o resultado da consulta de lote de RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_14_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 14, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do retorno.')

    
    # Element Alertas uses Python identifier Alertas
    __Alertas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Alertas'), 'Alertas', '__httplocalhost8080WsNFe2lote_CTD_ANON_14_Alertas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 78, 4), )

    
    Alertas = property(__Alertas.value, __Alertas.set, None, 'Elemento que representa a ocorrência de eventos de alerta durante o processamento da mensagem XML.')

    
    # Element Erros uses Python identifier Erros
    __Erros = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Erros'), 'Erros', '__httplocalhost8080WsNFe2lote_CTD_ANON_14_Erros', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 83, 4), )

    
    Erros = property(__Erros.value, __Erros.set, None, 'Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.')

    
    # Element ListaNFSe uses Python identifier ListaNFSe
    __ListaNFSe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ListaNFSe'), 'ListaNFSe', '__httplocalhost8080WsNFe2lote_CTD_ANON_14_ListaNFSe', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 88, 4), )

    
    ListaNFSe = property(__ListaNFSe.value, __ListaNFSe.set, None, 'Lista de retorno para consulta de NFSe.')

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __Alertas.name() : __Alertas,
        __Erros.name() : __Erros,
        __ListaNFSe.name() : __ListaNFSe
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do retorno."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 18, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 20, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Código da Cidade')

    
    # Element Sucesso uses Python identifier Sucesso
    __Sucesso = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Sucesso'), 'Sucesso', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_Sucesso', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 25, 7), )

    
    Sucesso = property(__Sucesso.value, __Sucesso.set, None, 'Campo indicativo do sucesso do pedido do serviço.')

    
    # Element NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroLote'), 'NumeroLote', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_NumeroLote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 30, 7), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, 'Número de lote.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 35, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'CNPJ do remetente autorizado a transmitir a mensagem XML.')

    
    # Element RazaoSocialRemetente uses Python identifier RazaoSocialRemetente
    __RazaoSocialRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RazaoSocialRemetente'), 'RazaoSocialRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_RazaoSocialRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 40, 7), )

    
    RazaoSocialRemetente = property(__RazaoSocialRemetente.value, __RazaoSocialRemetente.set, None, 'Razão Social do remetente autorizado a transmitir a mensagem XML.')

    
    # Element DataEnvioLote uses Python identifier DataEnvioLote
    __DataEnvioLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEnvioLote'), 'DataEnvioLote', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_DataEnvioLote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 45, 7), )

    
    DataEnvioLote = property(__DataEnvioLote.value, __DataEnvioLote.set, None, 'Data/hora de envio do lote.')

    
    # Element QtdNotasProcessadas uses Python identifier QtdNotasProcessadas
    __QtdNotasProcessadas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas'), 'QtdNotasProcessadas', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_QtdNotasProcessadas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 50, 7), )

    
    QtdNotasProcessadas = property(__QtdNotasProcessadas.value, __QtdNotasProcessadas.set, None, 'Quantidade de RPS do lote.')

    
    # Element TempoProcessamento uses Python identifier TempoProcessamento
    __TempoProcessamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TempoProcessamento'), 'TempoProcessamento', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_TempoProcessamento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 55, 7), )

    
    TempoProcessamento = property(__TempoProcessamento.value, __TempoProcessamento.set, None, 'Tempo de processamento do lote.')

    
    # Element ValorTotalServicos uses Python identifier ValorTotalServicos
    __ValorTotalServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), 'ValorTotalServicos', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_ValorTotalServicos', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 60, 7), )

    
    ValorTotalServicos = property(__ValorTotalServicos.value, __ValorTotalServicos.set, None, 'Valor total dos serviços dos RPS contidos na mensagem XML.')

    
    # Element ValorTotalDeducoes uses Python identifier ValorTotalDeducoes
    __ValorTotalDeducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), 'ValorTotalDeducoes', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_ValorTotalDeducoes', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 65, 7), )

    
    ValorTotalDeducoes = property(__ValorTotalDeducoes.value, __ValorTotalDeducoes.set, None, 'Valor total das deduções dos RPS contidos na mensagem XML.')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_15_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 70, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Versão do Schema XML utilizado.')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __Sucesso.name() : __Sucesso,
        __NumeroLote.name() : __NumeroLote,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __RazaoSocialRemetente.name() : __RazaoSocialRemetente,
        __DataEnvioLote.name() : __DataEnvioLote,
        __QtdNotasProcessadas.name() : __QtdNotasProcessadas,
        __TempoProcessamento.name() : __TempoProcessamento,
        __ValorTotalServicos.name() : __ValorTotalServicos,
        __ValorTotalDeducoes.name() : __ValorTotalDeducoes,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para Retrono de consulta de
				notas.Este Schema XML é utilizado pelos prestadores
				de serviços o retorno da consulta de Notas fiscais emitidas por RPS.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_16_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 17, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho da Consulta.\n\t\t\t\t\t\t')

    
    # Element NotasConsultadas uses Python identifier NotasConsultadas
    __NotasConsultadas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NotasConsultadas'), 'NotasConsultadas', '__httplocalhost8080WsNFe2lote_CTD_ANON_16_NotasConsultadas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 57, 4), )

    
    NotasConsultadas = property(__NotasConsultadas.value, __NotasConsultadas.set, None, 'Informe os RPS a serem consultados por\n\t\t\t\t\t\t\tNF-e.')

    
    # Element Alertas uses Python identifier Alertas
    __Alertas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Alertas'), 'Alertas', '__httplocalhost8080WsNFe2lote_CTD_ANON_16_Alertas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 65, 4), )

    
    Alertas = property(__Alertas.value, __Alertas.set, None, 'Elemento que representa a ocorrência de\n\t\t\t\t\t\t\teventos de alertas o durante o processamento da mensagem XML.\n\t\t\t\t\t\t')

    
    # Element Erros uses Python identifier Erros
    __Erros = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Erros'), 'Erros', '__httplocalhost8080WsNFe2lote_CTD_ANON_16_Erros', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 74, 4), )

    
    Erros = property(__Erros.value, __Erros.set, None, 'Elemento que representa a ocorrência de\n\t\t\t\t\t\t\teventos de erro durante o processamento da mensagem XML.\n\t\t\t\t\t\t')

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __NotasConsultadas.name() : __NotasConsultadas,
        __Alertas.name() : __Alertas,
        __Erros.name() : __Erros
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho da Consulta.
						"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 22, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_17_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 24, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Informe o Codigo da Cidade.\n\t\t\t\t\t\t\t\t\t')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_17_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 31, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'Informe o CPF/CNPJ do Remetente\n\t\t\t\t\t\t\t\t\t\tautorizado a transmitir a mensagem XML.')

    
    # Element transacao uses Python identifier transacao
    __transacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transacao'), 'transacao', '__httplocalhost8080WsNFe2lote_CTD_ANON_17_transacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 38, 7), )

    
    transacao = property(__transacao.value, __transacao.set, None, 'Informe se as NF-e a serem consultadas\n\t\t\t\t\t\t\t\t\t\tfarão parte de uma mesma transação. Informe sempre True.\n\t\t\t\t\t\t\t\t\t')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_17_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 46, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Informe a Versão do Schema XML\n\t\t\t\t\t\t\t\t\t\tutilizado.')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __transacao.name() : __transacao,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para Retrono de consulta de notas.Este Schema XML é utilizado pelos prestadores de serviços o retorno da consulta de Notas fiscais emitidas por RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_18_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 14, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho da Consulta.')

    
    # Element Notas uses Python identifier Notas
    __Notas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Notas'), 'Notas', '__httplocalhost8080WsNFe2lote_CTD_ANON_18_Notas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 54, 4), )

    
    Notas = property(__Notas.value, __Notas.set, None, 'Informe os RPS a serem substituidos por NF-e.')

    
    # Element Erros uses Python identifier Erros
    __Erros = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Erros'), 'Erros', '__httplocalhost8080WsNFe2lote_CTD_ANON_18_Erros', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 59, 4), )

    
    Erros = property(__Erros.value, __Erros.set, None, 'Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.')

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __Notas.name() : __Notas,
        __Erros.name() : __Erros
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho da Consulta."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 18, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_19_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 20, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Informe o Codigo da Cidade.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_19_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 25, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.')

    
    # Element InscricaoMunicipalPrestador uses Python identifier InscricaoMunicipalPrestador
    __InscricaoMunicipalPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), 'InscricaoMunicipalPrestador', '__httplocalhost8080WsNFe2lote_CTD_ANON_19_InscricaoMunicipalPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 30, 7), )

    
    InscricaoMunicipalPrestador = property(__InscricaoMunicipalPrestador.value, __InscricaoMunicipalPrestador.set, None, 'Informe a Inscrição Municipal do Prestador')

    
    # Element dtInicio uses Python identifier dtInicio
    __dtInicio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dtInicio'), 'dtInicio', '__httplocalhost8080WsNFe2lote_CTD_ANON_19_dtInicio', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 35, 7), )

    
    dtInicio = property(__dtInicio.value, __dtInicio.set, None, 'Informe a data de início do\tperíodo transmitido\t(AAAA-MM-DD).')

    
    # Element dtFim uses Python identifier dtFim
    __dtFim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dtFim'), 'dtFim', '__httplocalhost8080WsNFe2lote_CTD_ANON_19_dtFim', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 41, 7), )

    
    dtFim = property(__dtFim.value, __dtFim.set, None, 'Informe a data final do período transmitido (AAAA-MM-DD).')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_19_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 46, 10), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Versão do Schema XML utilizado.')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __InscricaoMunicipalPrestador.name() : __InscricaoMunicipalPrestador,
        __dtInicio.name() : __dtInicio,
        __dtFim.name() : __dtFim,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para RETORNO da Consulta
				Sequêncial de RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 13, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_20_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 15, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do retorno.\n\t\t\t\t\t\t')

    
    # Element Alertas uses Python identifier Alertas
    __Alertas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Alertas'), 'Alertas', '__httplocalhost8080WsNFe2lote_CTD_ANON_20_Alertas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 61, 4), )

    
    Alertas = property(__Alertas.value, __Alertas.set, None, 'Elemento que representa a ocorrência de\n\t\t\t\t\t\t\teventos de alerta durante o processamento da mensagem XML.\n\t\t\t\t\t\t')

    
    # Element Erros uses Python identifier Erros
    __Erros = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Erros'), 'Erros', '__httplocalhost8080WsNFe2lote_CTD_ANON_20_Erros', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 69, 4), )

    
    Erros = property(__Erros.value, __Erros.set, None, 'Elemento que representa a ocorrência de\n\t\t\t\t\t\t\teventos de erro durante o processamento da mensagem XML.\n\t\t\t\t\t\t')

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __Alertas.name() : __Alertas,
        __Erros.name() : __Erros
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do retorno.
						"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 20, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCid uses Python identifier CodCid
    __CodCid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCid'), 'CodCid', '__httplocalhost8080WsNFe2lote_CTD_ANON_21_CodCid', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 22, 7), )

    
    CodCid = property(__CodCid.value, __CodCid.set, None, 'Código da Cidade')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_21_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 28, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'CNPJ do remetente autorizado a transmitir\n\t\t\t\t\t\t\t\t\t\ta mensagem XML.')

    
    # Element IMPrestador uses Python identifier IMPrestador
    __IMPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IMPrestador'), 'IMPrestador', '__httplocalhost8080WsNFe2lote_CTD_ANON_21_IMPrestador', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 35, 7), )

    
    IMPrestador = property(__IMPrestador.value, __IMPrestador.set, None, 'Inscrição Municipal do Prestador.\n\t\t\t\t\t\t\t\t\t')

    
    # Element NroUltimoRps uses Python identifier NroUltimoRps
    __NroUltimoRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NroUltimoRps'), 'NroUltimoRps', '__httplocalhost8080WsNFe2lote_CTD_ANON_21_NroUltimoRps', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 42, 7), )

    
    NroUltimoRps = property(__NroUltimoRps.value, __NroUltimoRps.set, None, 'Informe o Número do RPS emitido.\n\t\t\t\t\t\t\t\t\t')

    
    # Element SeriePrestacao uses Python identifier SeriePrestacao
    __SeriePrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), 'SeriePrestacao', '__httplocalhost8080WsNFe2lote_CTD_ANON_21_SeriePrestacao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 49, 7), )

    
    SeriePrestacao = property(__SeriePrestacao.value, __SeriePrestacao.set, None, None)

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_21_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 51, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Versão do Schema XML utilizado.\n\t\t\t\t\t\t\t\t\t')

    _ElementMap.update({
        __CodCid.name() : __CodCid,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __IMPrestador.name() : __IMPrestador,
        __NroUltimoRps.name() : __NroUltimoRps,
        __SeriePrestacao.name() : __SeriePrestacao,
        __Versao.name() : __Versao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Schema utilizado para RETORNO de Requisição de Envio de lote de RPS.Este Schema XML é utilizado pelo Web Service para informar aos prestadores de serviços o resultado do pedido de envio de lote de RPS."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Cabecalho uses Python identifier Cabecalho
    __Cabecalho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cabecalho'), 'Cabecalho', '__httplocalhost8080WsNFe2lote_CTD_ANON_22_Cabecalho', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 14, 4), )

    
    Cabecalho = property(__Cabecalho.value, __Cabecalho.set, None, 'Cabeçalho do retorno.')

    
    # Element Alertas uses Python identifier Alertas
    __Alertas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Alertas'), 'Alertas', '__httplocalhost8080WsNFe2lote_CTD_ANON_22_Alertas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 78, 4), )

    
    Alertas = property(__Alertas.value, __Alertas.set, None, 'Elemento que representa a ocorrência de eventos de alerta durante o processamento da mensagem XML.')

    
    # Element Erros uses Python identifier Erros
    __Erros = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Erros'), 'Erros', '__httplocalhost8080WsNFe2lote_CTD_ANON_22_Erros', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 83, 4), )

    
    Erros = property(__Erros.value, __Erros.set, None, 'Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.')

    
    # Element ChavesNFSeRPS uses Python identifier ChavesNFSeRPS
    __ChavesNFSeRPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChavesNFSeRPS'), 'ChavesNFSeRPS', '__httplocalhost8080WsNFe2lote_CTD_ANON_22_ChavesNFSeRPS', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 88, 4), )

    
    ChavesNFSeRPS = property(__ChavesNFSeRPS.value, __ChavesNFSeRPS.set, None, 'Chave da NF-e e Chave do RPS que esta substitui.')

    _ElementMap.update({
        __Cabecalho.name() : __Cabecalho,
        __Alertas.name() : __Alertas,
        __Erros.name() : __Erros,
        __ChavesNFSeRPS.name() : __ChavesNFSeRPS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Cabeçalho do retorno."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 18, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CodCidade uses Python identifier CodCidade
    __CodCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CodCidade'), 'CodCidade', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_CodCidade', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 20, 7), )

    
    CodCidade = property(__CodCidade.value, __CodCidade.set, None, 'Código da Cidade')

    
    # Element Sucesso uses Python identifier Sucesso
    __Sucesso = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Sucesso'), 'Sucesso', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_Sucesso', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 25, 7), )

    
    Sucesso = property(__Sucesso.value, __Sucesso.set, None, 'Campo indicativo do sucesso do pedido do serviço.')

    
    # Element NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumeroLote'), 'NumeroLote', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_NumeroLote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 30, 7), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, 'Número de lote.')

    
    # Element CPFCNPJRemetente uses Python identifier CPFCNPJRemetente
    __CPFCNPJRemetente = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), 'CPFCNPJRemetente', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_CPFCNPJRemetente', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 35, 7), )

    
    CPFCNPJRemetente = property(__CPFCNPJRemetente.value, __CPFCNPJRemetente.set, None, 'CNPJ do remetente autorizado a transmitir a mensagem XML.')

    
    # Element DataEnvioLote uses Python identifier DataEnvioLote
    __DataEnvioLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DataEnvioLote'), 'DataEnvioLote', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_DataEnvioLote', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 40, 7), )

    
    DataEnvioLote = property(__DataEnvioLote.value, __DataEnvioLote.set, None, 'Data/hora de envio do lote.')

    
    # Element QtdNotasProcessadas uses Python identifier QtdNotasProcessadas
    __QtdNotasProcessadas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas'), 'QtdNotasProcessadas', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_QtdNotasProcessadas', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 45, 7), )

    
    QtdNotasProcessadas = property(__QtdNotasProcessadas.value, __QtdNotasProcessadas.set, None, 'Quantidade de RPS do lote.')

    
    # Element TempoProcessamento uses Python identifier TempoProcessamento
    __TempoProcessamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TempoProcessamento'), 'TempoProcessamento', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_TempoProcessamento', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 50, 7), )

    
    TempoProcessamento = property(__TempoProcessamento.value, __TempoProcessamento.set, None, 'Tempo de processamento do lote.')

    
    # Element ValorTotalServicos uses Python identifier ValorTotalServicos
    __ValorTotalServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), 'ValorTotalServicos', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_ValorTotalServicos', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 55, 7), )

    
    ValorTotalServicos = property(__ValorTotalServicos.value, __ValorTotalServicos.set, None, 'Valor total dos serviços dos RPS contidos na mensagem XML.')

    
    # Element ValorTotalDeducoes uses Python identifier ValorTotalDeducoes
    __ValorTotalDeducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), 'ValorTotalDeducoes', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_ValorTotalDeducoes', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 60, 7), )

    
    ValorTotalDeducoes = property(__ValorTotalDeducoes.value, __ValorTotalDeducoes.set, None, 'Valor total das deduções dos RPS contidos na mensagem XML.')

    
    # Element Versao uses Python identifier Versao
    __Versao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Versao'), 'Versao', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_Versao', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 65, 7), )

    
    Versao = property(__Versao.value, __Versao.set, None, 'Versão do Schema XML utilizado.')

    
    # Element Assincrono uses Python identifier Assincrono
    __Assincrono = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Assincrono'), 'Assincrono', '__httplocalhost8080WsNFe2lote_CTD_ANON_23_Assincrono', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 70, 7), )

    
    Assincrono = property(__Assincrono.value, __Assincrono.set, None, 'Tipo de processamento: N-Processamento Sincrono, S-Processamento Assíncrono')

    _ElementMap.update({
        __CodCidade.name() : __CodCidade,
        __Sucesso.name() : __Sucesso,
        __NumeroLote.name() : __NumeroLote,
        __CPFCNPJRemetente.name() : __CPFCNPJRemetente,
        __DataEnvioLote.name() : __DataEnvioLote,
        __QtdNotasProcessadas.name() : __QtdNotasProcessadas,
        __TempoProcessamento.name() : __TempoProcessamento,
        __ValorTotalServicos.name() : __ValorTotalServicos,
        __ValorTotalDeducoes.name() : __ValorTotalDeducoes,
        __Versao.name() : __Versao,
        __Assincrono.name() : __Assincrono
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


ConsultaSeqRps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultaSeqRps'), CTD_ANON, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 9, 1))
Namespace.addCategoryObject('elementBinding', ConsultaSeqRps.name().localName(), ConsultaSeqRps)

ReqCancelamentoNFSe = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReqCancelamentoNFSe'), CTD_ANON_2, documentation='Schema utilizado para  Cancelamento de NFSe.Este Schema XML é utilizado pelos Prestadores de serviços cancelarem NFSe emitidas por eles.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', ReqCancelamentoNFSe.name().localName(), ReqCancelamentoNFSe)

ReqConsultaLote = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReqConsultaLote'), CTD_ANON_4, documentation='Schema utilizado para REQUISIçÂO de Consulta de Lote de RPS.Este Schema XML é utilizado pelos Prestadores de serviços para consultarem Lote de RPS emitidos por eles.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', ReqConsultaLote.name().localName(), ReqConsultaLote)

ReqConsultaNFSeRPS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReqConsultaNFSeRPS'), CTD_ANON_6, documentation='Schema utilizado para  Consulta de NFSe.Este Schema XML é utilizado pelos Prestadores de serviços consultarem NFSe emitidas por eles.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', ReqConsultaNFSeRPS.name().localName(), ReqConsultaNFSeRPS)

ReqConsultaNotas = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReqConsultaNotas'), CTD_ANON_8, documentation='Schema utilizado para REQUISIÇAO de consultas\n\t\t\t\tde notas que foram enviadas por lote de RPS.Este Schema XML é utilizado pelos prestadores\n\t\t\t\tde serviços para consultas de notas que foram enviadas por lote de\n\t\t\t\tRPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 9, 1))
Namespace.addCategoryObject('elementBinding', ReqConsultaNotas.name().localName(), ReqConsultaNotas)

ReqEnvioLoteRPS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReqEnvioLoteRPS'), CTD_ANON_10, documentation='Schema utilizado para envio de lote de RPS.Este Schema XML é utilizado pelos prestadores\n\t\t\t\tde serviços para substituição em lote de RPS por NFS-e.\n\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 8, 1))
Namespace.addCategoryObject('elementBinding', ReqEnvioLoteRPS.name().localName(), ReqEnvioLoteRPS)

RetornoCancelamentoNFSe = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RetornoCancelamentoNFSe'), CTD_ANON_12, documentation='Schema utilizado para RETORNO de Pedidos de cancelamento de NFSe.Este Schema XML é utilizado pelo Web Service para informar aos prestadores de serviços qual o resultado do pedido de cancelamento de NFSe.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', RetornoCancelamentoNFSe.name().localName(), RetornoCancelamentoNFSe)

RetornoConsultaLote = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RetornoConsultaLote'), CTD_ANON_14, documentation='Schema utilizado para RETORNO de consulta de lote de RPS.Este Schema XML é utilizado pelo Web Service para informar aos prestadores de serviços o resultado da consulta de lote de RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', RetornoConsultaLote.name().localName(), RetornoConsultaLote)

RetornoConsultaNFSeRPS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RetornoConsultaNFSeRPS'), CTD_ANON_16, documentation='Schema utilizado para Retrono de consulta de\n\t\t\t\tnotas.Este Schema XML é utilizado pelos prestadores\n\t\t\t\tde serviços o retorno da consulta de Notas fiscais emitidas por RPS.\n\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', RetornoConsultaNFSeRPS.name().localName(), RetornoConsultaNFSeRPS)

RetornoConsultaNotas = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RetornoConsultaNotas'), CTD_ANON_18, documentation='Schema utilizado para Retrono de consulta de notas.Este Schema XML é utilizado pelos prestadores de serviços o retorno da consulta de Notas fiscais emitidas por RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', RetornoConsultaNotas.name().localName(), RetornoConsultaNotas)

RetornoConsultaSeqRps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RetornoConsultaSeqRps'), CTD_ANON_20, documentation='Schema utilizado para RETORNO da Consulta\n\t\t\t\tSequêncial de RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', RetornoConsultaSeqRps.name().localName(), RetornoConsultaSeqRps)

RetornoEnvioLoteRPS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RetornoEnvioLoteRPS'), CTD_ANON_22, documentation='Schema utilizado para RETORNO de Requisição de Envio de lote de RPS.Este Schema XML é utilizado pelo Web Service para informar aos prestadores de serviços o resultado do pedido de envio de lote de RPS.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', RetornoEnvioLoteRPS.name().localName(), RetornoEnvioLoteRPS)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 12, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 12, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCid'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 15, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IMPrestador'), _ImportedBinding_tipos.tpInscricaoMunicipal, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 16, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 17, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), _ImportedBinding_tipos.tpSeriePrestacao, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 18, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 19, 7), fixed=True, unicode_default='1'))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 18, 7))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCid')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 15, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'IMPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 16, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 17, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'SeriePrestacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 18, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ConsultaSeqRps.xsd', 19, 7))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_3, scope=CTD_ANON_2, documentation='Cabeçalho do pedido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 17, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Lote'), _ImportedBinding_tipos.tpLoteCancelamentoNFSe, scope=CTD_ANON_2, documentation='Detalhe do pedido de cancelamento de NFSe. Cada detalhe deverá conter a Chave de uma NFSe e sua respectiva assinatura de cancelamento.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 46, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding_ds.SignatureType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 51, 16))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'Lote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 46, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 51, 16))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_3, documentation='Informe o Codigo da Cidade.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 23, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_3, documentation='Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 28, 7)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transacao'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_3, documentation='Informe se as NF-e a serem canceladas farão parte de uma mesma transação. True - As NF-e só serão canceladas se não ocorrer nenhum evento de erro durante o processamento de todo o lote; False - As NF-e aptas a serem canceladas serão canceladas, mesmo que ocorram eventos de erro durante processamento do cancelamento de outras NF-e deste lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 33, 7), unicode_default='true'))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_3, documentation='Informe a Versão do Schema XML utilizado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 38, 7), fixed=True, unicode_default='1'))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 23, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 28, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'transacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 33, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqCancelamentoNFSe.xsd', 38, 7))
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
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_5, scope=CTD_ANON_4, documentation='Cabeçalho do pedido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 14, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 14, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_5, documentation='Informe o Codigo da Cidade.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 20, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_5, documentation='Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 25, 7)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_5, documentation='Informe a Versão do Schema XML utilizado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 30, 7), fixed=True, unicode_default='1'))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroLote'), _ImportedBinding_tipos.tpNumero, scope=CTD_ANON_5, documentation='Informe o Número do Lote a ser consultado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 35, 7)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 20, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 25, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 30, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroLote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaLote.xsd', 35, 7))
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
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_7, scope=CTD_ANON_6, documentation='Cabeçalho do pedido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 17, 4)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Lote'), _ImportedBinding_tipos.tpLoteConsultaNFSe, scope=CTD_ANON_6, documentation='Detalhe do pedido de consulta de NFSe. Cada detalhe deverá conter a Chave de uma NFSe e sua respectiva assinatura de consulta.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 46, 4)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding_ds.SignatureType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 51, 16))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'Lote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 46, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 51, 16))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_7, documentation='Informe o Codigo da Cidade.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 23, 7)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_7, documentation='Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 28, 7)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transacao'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_7, documentation='Informe se as NF-e a serem consultadas farão parte de uma mesma transação. Informe sempre True.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 33, 7), unicode_default='true'))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_7, documentation='Informe a Versão do Schema XML utilizado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 38, 7), fixed=True, unicode_default='1'))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 23, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 28, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'transacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 33, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNFSeRPS.xsd', 38, 7))
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
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_9, scope=CTD_ANON_8, documentation='Cabeçalho do pedido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 19, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding_ds.SignatureType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 83, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 19, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 83, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_9, documentation='Informe o Codigo da Cidade.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 25, 7)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_9, documentation='Informe o CPF/CNPJ do Remetente\n\t\t\t\t\t\t\t\t\t\tautorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 32, 7)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), _ImportedBinding_tipos.tpInscricaoMunicipal, scope=CTD_ANON_9, documentation='Informe a Inscrição Municipal do\n\t\t\t\t\t\t\t\t\t\tPrestador', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 39, 7)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dtInicio'), pyxb.binding.datatypes.date, scope=CTD_ANON_9, documentation='Informe a data de início do período\n\t\t\t\t\t\t\t\t\t\ttransmitido (AAAA-MM-DD).', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 46, 7)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dtFim'), pyxb.binding.datatypes.date, scope=CTD_ANON_9, documentation='Informe a data final do período\n\t\t\t\t\t\t\t\t\t\ttransmitido (AAAA-MM-DD).', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 53, 7)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NotaInicial'), _ImportedBinding_tipos.tpNumero, scope=CTD_ANON_9, documentation='Numero da nota inicial da consulta. Ou\n\t\t\t\t\t\t\t\t\t\tseja a consulta ira retornar as notas no periodo, onde o\n\t\t\t\t\t\t\t\t\t\tnumero da nota seja maior ou igual a esse numero. O retorno\n\t\t\t\t\t\t\t\t\t\tnão pode ultrapassar 500Kb. Caso não tenha o numero da nota,\n\t\t\t\t\t\t\t\t\t\tpassar o valor Zero, será retornado as notas geradas no\n\t\t\t\t\t\t\t\t\t\tperiodo até o limite de 500kb.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 60, 7)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_9, documentation='Informe a Versão.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 71, 7)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 60, 7))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 25, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 32, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 39, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'dtInicio')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 46, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'dtFim')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 53, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'NotaInicial')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 60, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqConsultaNotas.xsd', 71, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_11, scope=CTD_ANON_10, documentation='Cabeçalho do Lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 17, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Lote'), _ImportedBinding_tipos.tpLote, scope=CTD_ANON_10, documentation='Informe os RPS a serem substituidos por\n\t\t\t\t\t\t\tNF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 139, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding_ds.SignatureType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 145, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'Lote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 139, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 145, 4))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_11, documentation='Informe o Codigo da Cidade no Padrão SIAFI.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 23, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tCNPJ do contribuinte ou CPF do Responsável Legal autorizado a entregar o lote.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 29, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialRemetente'), _ImportedBinding_tipos.tpRazaoSocial, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tInforme o Nome do Contribuinte ou do Responsável Legal\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 36, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transacao'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tInforme se os RPS a serem\n\t\t\t\t\t\t\t\t\t\tsubstituídos por\n\t\t\t\t\t\t\t\t\t\tNF-e farão\n\t\t\t\t\t\t\t\t\t\tparte de uma mesma transação.\n\t\t\t\t\t\t\t\t\t\tTrue - Os RPS só serão\n\t\t\t\t\t\t\t\t\t\tsubstituídos por NF-e se não\n\t\t\t\t\t\t\t\t\t\tocorrer nenhum evento de erro\n\t\t\t\t\t\t\t\t\t\tdurante o processamento de todo\n\t\t\t\t\t\t\t\t\t\to lote; False - Os RPS válidos\n\t\t\t\t\t\t\t\t\t\tserão substituídos por NF-e,\n\t\t\t\t\t\t\t\t\t\tmesmo que ocorram eventos de\n\t\t\t\t\t\t\t\t\t\terro durante processamento de\n\t\t\t\t\t\t\t\t\t\toutros RPS deste lote. Por definição\n\t\t\t\t\t\t\t\t\t\testão sendo aceitos apenas lotes com RPS válidos,\n\t\t\t\t\t\t\t\t\t\to lote é\n\t\t\t\t\t\t\t\t\t\trecusado caso haja algum RPS inválido.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 43, 7), unicode_default='true'))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dtInicio'), pyxb.binding.datatypes.date, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tInforme a data de início do\n\t\t\t\t\t\t\t\t\t\tperíodo\n\t\t\t\t\t\t\t\t\t\ttransmitido\n\t\t\t\t\t\t\t\t\t\t(AAAA-MM-DD).\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 66, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dtFim'), pyxb.binding.datatypes.date, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tInforme a data final do período\n\t\t\t\t\t\t\t\t\t\ttransmitido\n\t\t\t\t\t\t\t\t\t\t(AAAA-MM-DD).\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 76, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'QtdRPS'), _ImportedBinding_tipos.tpQtdRpsLote, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tInforme o total de RPS contidos\n\t\t\t\t\t\t\t\t\t\tna mensagem\n\t\t\t\t\t\t\t\t\t\tXML. OBS: O xml não pode ultrapassar o tamanho maximo de 500kb.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 85, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), _ImportedBinding_tipos.tpValor, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tInforme o valor total dos\n\t\t\t\t\t\t\t\t\t\tserviços prestados\n\t\t\t\t\t\t\t\t\t\tdos RPS\n\t\t\t\t\t\t\t\t\t\tcontidos na mensagem XML.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 94, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), _ImportedBinding_tipos.tpValor, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tInforme o valor total das\n\t\t\t\t\t\t\t\t\t\tdeduções dos RPS\n\t\t\t\t\t\t\t\t\t\tcontidos na\n\t\t\t\t\t\t\t\t\t\tmensagem XML.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 104, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_11, documentation='\n\t\t\t\t\t\t\t\t\t\tInforme a Versão do Schema XML\n\t\t\t\t\t\t\t\t\t\tutilizado.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 114, 7), fixed=True, unicode_default='1'))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MetodoEnvio'), _ImportedBinding_tipos.tpMetodoEnvio, scope=CTD_ANON_11, documentation='Informe o Método de Envio', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 122, 7)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'VersaoComponente'), _ImportedBinding_tipos.tpVersaoComponente, scope=CTD_ANON_11, documentation='Versão da DLL de envio de lote. Não é necessário informar esse campo caso não utilize a DLL.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 128, 7)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 128, 7))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 23, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 29, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 36, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'transacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 43, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'dtInicio')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 66, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'dtFim')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 76, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'QtdRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 85, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 94, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 104, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 114, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'MetodoEnvio')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 122, 7))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'VersaoComponente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/ReqEnvioLoteRPS.xsd', 128, 7))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_13, scope=CTD_ANON_12, documentation='Cabeçalho do pedido.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 14, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NotasCanceladas'), _ImportedBinding_tipos.tpRetornoNotasCancelamentoNFSe, scope=CTD_ANON_12, documentation='Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 44, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Alertas'), _ImportedBinding_tipos.tpListaAlertas, scope=CTD_ANON_12, documentation='Elemento que representa a ocorrência de eventos de alerta durante o processamento da mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 49, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Erros'), _ImportedBinding_tipos.tpListaErros, scope=CTD_ANON_12, documentation='Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 54, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 44, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 49, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 54, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 14, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'NotasCanceladas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 44, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'Alertas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 49, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'Erros')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 54, 4))
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
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_13, documentation='Informe o Codigo da Cidade.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 20, 7)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Sucesso'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_13, documentation='Notas Canceladas com Sucesso.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 25, 7), unicode_default='true'))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_13, documentation='Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 30, 7)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_13, documentation='Informe a Versão do Schema XML utilizado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 36, 7), fixed=True, unicode_default='1'))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 20, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'Sucesso')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 25, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 30, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoCancelamentoNFSe.xsd', 36, 7))
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
CTD_ANON_13._Automaton = _BuildAutomaton_13()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_15, scope=CTD_ANON_14, documentation='Cabeçalho do retorno.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 14, 4)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Alertas'), _ImportedBinding_tipos.tpListaAlertas, scope=CTD_ANON_14, documentation='Elemento que representa a ocorrência de eventos de alerta durante o processamento da mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 78, 4)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Erros'), _ImportedBinding_tipos.tpListaErros, scope=CTD_ANON_14, documentation='Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 83, 4)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ListaNFSe'), _ImportedBinding_tipos.tpListaNFSe, scope=CTD_ANON_14, documentation='Lista de retorno para consulta de NFSe.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 88, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 78, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 83, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 88, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 14, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'Alertas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 78, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'Erros')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 83, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'ListaNFSe')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 88, 4))
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
CTD_ANON_14._Automaton = _BuildAutomaton_14()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_15, documentation='Código da Cidade', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 20, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Sucesso'), _ImportedBinding_tipos.tpSucesso, scope=CTD_ANON_15, documentation='Campo indicativo do sucesso do pedido do serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 25, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroLote'), _ImportedBinding_tipos.tpNumero, scope=CTD_ANON_15, documentation='Número de lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 30, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_15, documentation='CNPJ do remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 35, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RazaoSocialRemetente'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, documentation='Razão Social do remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 40, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEnvioLote'), _ImportedBinding_tipos.tpDataHoraNulo, scope=CTD_ANON_15, documentation='Data/hora de envio do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 45, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas'), _ImportedBinding_tipos.tpQtdRpsLote, scope=CTD_ANON_15, documentation='Quantidade de RPS do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 50, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TempoProcessamento'), _ImportedBinding_tipos.tpTempoProcessamento, scope=CTD_ANON_15, documentation='Tempo de processamento do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 55, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), _ImportedBinding_tipos.tpValor, scope=CTD_ANON_15, documentation='Valor total dos serviços dos RPS contidos na mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 60, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), _ImportedBinding_tipos.tpValor, scope=CTD_ANON_15, documentation='Valor total das deduções dos RPS contidos na mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 65, 7)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_15, documentation='Versão do Schema XML utilizado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 70, 7), fixed=True, unicode_default='1'))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 20, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'Sucesso')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 25, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroLote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 30, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 35, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'RazaoSocialRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 40, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEnvioLote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 45, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 50, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'TempoProcessamento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 55, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 60, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 65, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaLote.xsd', 70, 7))
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
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_15()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_17, scope=CTD_ANON_16, documentation='Cabeçalho da Consulta.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 17, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NotasConsultadas'), _ImportedBinding_tipos.tpListaNFSeConsultaNota, scope=CTD_ANON_16, documentation='Informe os RPS a serem consultados por\n\t\t\t\t\t\t\tNF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 57, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Alertas'), _ImportedBinding_tipos.tpListaAlertas, scope=CTD_ANON_16, documentation='Elemento que representa a ocorrência de\n\t\t\t\t\t\t\teventos de alertas o durante o processamento da mensagem XML.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 65, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Erros'), _ImportedBinding_tipos.tpListaErros, scope=CTD_ANON_16, documentation='Elemento que representa a ocorrência de\n\t\t\t\t\t\t\teventos de erro durante o processamento da mensagem XML.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 74, 4)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 57, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 65, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 74, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'NotasConsultadas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 57, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'Alertas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 65, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'Erros')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 74, 4))
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
CTD_ANON_16._Automaton = _BuildAutomaton_16()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_17, documentation='Informe o Codigo da Cidade.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 24, 7)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_17, documentation='Informe o CPF/CNPJ do Remetente\n\t\t\t\t\t\t\t\t\t\tautorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 31, 7)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transacao'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_17, documentation='Informe se as NF-e a serem consultadas\n\t\t\t\t\t\t\t\t\t\tfarão parte de uma mesma transação. Informe sempre True.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 38, 7), unicode_default='true'))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_17, documentation='Informe a Versão do Schema XML\n\t\t\t\t\t\t\t\t\t\tutilizado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 46, 7), fixed=True, unicode_default='1'))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 24, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 31, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'transacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 38, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNFSeRPS.xsd', 46, 7))
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
CTD_ANON_17._Automaton = _BuildAutomaton_17()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_19, scope=CTD_ANON_18, documentation='Cabeçalho da Consulta.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 14, 4)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Notas'), _ImportedBinding_tipos.tpListaNFSeConsultaNota, scope=CTD_ANON_18, documentation='Informe os RPS a serem substituidos por NF-e.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 54, 4)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Erros'), _ImportedBinding_tipos.tpListaErros, scope=CTD_ANON_18, documentation='Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 59, 4)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 54, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 59, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 14, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'Notas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 54, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'Erros')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 59, 4))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_18()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_19, documentation='Informe o Codigo da Cidade.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 20, 7)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_19, documentation='Informe o CPF/CNPJ do Remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 25, 7)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador'), _ImportedBinding_tipos.tpInscricaoMunicipal, scope=CTD_ANON_19, documentation='Informe a Inscrição Municipal do Prestador', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 30, 7)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dtInicio'), pyxb.binding.datatypes.date, scope=CTD_ANON_19, documentation='Informe a data de início do\tperíodo transmitido\t(AAAA-MM-DD).', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 35, 7)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dtFim'), pyxb.binding.datatypes.date, scope=CTD_ANON_19, documentation='Informe a data final do período transmitido (AAAA-MM-DD).', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 41, 7)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_19, documentation='Versão do Schema XML utilizado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 46, 10), fixed=True, unicode_default='1'))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 20, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 25, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'InscricaoMunicipalPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 30, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'dtInicio')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 35, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'dtFim')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 41, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaNotas.xsd', 46, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_19()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_21, scope=CTD_ANON_20, documentation='Cabeçalho do retorno.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 15, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Alertas'), _ImportedBinding_tipos.tpListaAlertas, scope=CTD_ANON_20, documentation='Elemento que representa a ocorrência de\n\t\t\t\t\t\t\teventos de alerta durante o processamento da mensagem XML.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 61, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Erros'), _ImportedBinding_tipos.tpListaErros, scope=CTD_ANON_20, documentation='Elemento que representa a ocorrência de\n\t\t\t\t\t\t\teventos de erro durante o processamento da mensagem XML.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 69, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 61, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 69, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 15, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, 'Alertas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 61, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, 'Erros')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 69, 4))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_20()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCid'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_21, documentation='Código da Cidade', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 22, 7)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_21, documentation='CNPJ do remetente autorizado a transmitir\n\t\t\t\t\t\t\t\t\t\ta mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 28, 7)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IMPrestador'), _ImportedBinding_tipos.tpInscricaoMunicipal, scope=CTD_ANON_21, documentation='Inscrição Municipal do Prestador.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 35, 7)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NroUltimoRps'), _ImportedBinding_tipos.tpNumero, scope=CTD_ANON_21, documentation='Informe o Número do RPS emitido.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 42, 7)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SeriePrestacao'), _ImportedBinding_tipos.tpSeriePrestacao, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 49, 7)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_21, documentation='Versão do Schema XML utilizado.\n\t\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 51, 7), fixed=True, unicode_default='1'))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 49, 7))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCid')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 22, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 28, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'IMPrestador')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 35, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'NroUltimoRps')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 42, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'SeriePrestacao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 49, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoConsultaSeqRps.xsd', 51, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_21()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cabecalho'), CTD_ANON_23, scope=CTD_ANON_22, documentation='Cabeçalho do retorno.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 14, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Alertas'), _ImportedBinding_tipos.tpListaAlertas, scope=CTD_ANON_22, documentation='Elemento que representa a ocorrência de eventos de alerta durante o processamento da mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 78, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Erros'), _ImportedBinding_tipos.tpListaErros, scope=CTD_ANON_22, documentation='Elemento que representa a ocorrência de eventos de erro durante o processamento da mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 83, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChavesNFSeRPS'), _ImportedBinding_tipos.tpListaNFSeRPS, scope=CTD_ANON_22, documentation='Chave da NF-e e Chave do RPS que esta substitui.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 88, 4)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 78, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 83, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 88, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'Cabecalho')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 14, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'Alertas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 78, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'Erros')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 83, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'ChavesNFSeRPS')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 88, 4))
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
CTD_ANON_22._Automaton = _BuildAutomaton_22()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CodCidade'), _ImportedBinding_tipos.tpCodCidade, scope=CTD_ANON_23, documentation='Código da Cidade', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 20, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Sucesso'), _ImportedBinding_tipos.tpSucesso, scope=CTD_ANON_23, documentation='Campo indicativo do sucesso do pedido do serviço.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 25, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumeroLote'), _ImportedBinding_tipos.tpNumero, scope=CTD_ANON_23, documentation='Número de lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 30, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente'), _ImportedBinding_tipos.tpCPFCNPJ, scope=CTD_ANON_23, documentation='CNPJ do remetente autorizado a transmitir a mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 35, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DataEnvioLote'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_23, documentation='Data/hora de envio do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 40, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas'), _ImportedBinding_tipos.tpQtdRpsLote, scope=CTD_ANON_23, documentation='Quantidade de RPS do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 45, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TempoProcessamento'), _ImportedBinding_tipos.tpTempoProcessamento, scope=CTD_ANON_23, documentation='Tempo de processamento do lote.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 50, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos'), _ImportedBinding_tipos.tpValor, scope=CTD_ANON_23, documentation='Valor total dos serviços dos RPS contidos na mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 55, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes'), _ImportedBinding_tipos.tpValor, scope=CTD_ANON_23, documentation='Valor total das deduções dos RPS contidos na mensagem XML.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 60, 7)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Versao'), _ImportedBinding_tipos.tpVersao, scope=CTD_ANON_23, documentation='Versão do Schema XML utilizado.', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 65, 7), fixed=True, unicode_default='1'))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Assincrono'), _ImportedBinding_tipos.tpAssincrono, scope=CTD_ANON_23, documentation='Tipo de processamento: N-Processamento Sincrono, S-Processamento Assíncrono', location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 70, 7)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'CodCidade')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 20, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'Sucesso')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 25, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'NumeroLote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 30, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'CPFCNPJRemetente')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 35, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'DataEnvioLote')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 40, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'QtdNotasProcessadas')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 45, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'TempoProcessamento')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 50, 7))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalServicos')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 55, 7))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'ValorTotalDeducoes')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 60, 7))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'Versao')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 65, 7))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'Assincrono')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/RetornoEnvioLoteRPS.xsd', 70, 7))
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
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_23()

