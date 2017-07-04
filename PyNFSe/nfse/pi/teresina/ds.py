# ./ds.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f1c343a882e7a65fb879f4ee813309f8231f28c8
# Generated 2017-07-04 11:52:35.943860 by PyXB version 1.2.5 using Python 3.5.3.final.0
# Namespace http://www.w3.org/2000/09/xmldsig# [xmlns:ds]

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/2000/09/xmldsig#', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 59, 3)
    _Documentation = None
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minLength)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://www.w3.org/2000/09/xmldsig#}DigestValueType
class DigestValueType (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DigestValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 89, 1)
    _Documentation = None
DigestValueType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DigestValueType', DigestValueType)
_module_typeBindings.DigestValueType = DigestValueType

# Atomic simple type: {http://www.w3.org/2000/09/xmldsig#}TTransformURI
class TTransformURI (pyxb.binding.datatypes.anyURI, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TTransformURI')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 92, 1)
    _Documentation = None
TTransformURI._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TTransformURI, enum_prefix=None)
TTransformURI.httpwww_w3_org200009xmldsigenveloped_signature = TTransformURI._CF_enumeration.addEnumeration(unicode_value='http://www.w3.org/2000/09/xmldsig#enveloped-signature', tag='httpwww_w3_org200009xmldsigenveloped_signature')
TTransformURI.httpwww_w3_orgTR2001REC_xml_c14n_20010315 = TTransformURI._CF_enumeration.addEnumeration(unicode_value='http://www.w3.org/TR/2001/REC-xml-c14n-20010315', tag='httpwww_w3_orgTR2001REC_xml_c14n_20010315')
TTransformURI.httpwww_w3_orgTR2001REC_xml_c14n_20010315WithComments = TTransformURI._CF_enumeration.addEnumeration(unicode_value='http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments', tag='httpwww_w3_orgTR2001REC_xml_c14n_20010315WithComments')
TTransformURI.httpwww_w3_orgTR1999REC_xpath_19991116 = TTransformURI._CF_enumeration.addEnumeration(unicode_value='http://www.w3.org/TR/1999/REC-xpath-19991116', tag='httpwww_w3_orgTR1999REC_xpath_19991116')
TTransformURI._InitializeFacetMap(TTransformURI._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TTransformURI', TTransformURI)
_module_typeBindings.TTransformURI = TTransformURI

# Complex type {http://www.w3.org/2000/09/xmldsig#}SignatureType with content type ELEMENT_ONLY
class SignatureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2000/09/xmldsig#}SignatureType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignatureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 10, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}SignedInfo uses Python identifier SignedInfo
    __SignedInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignedInfo'), 'SignedInfo', '__httpwww_w3_org200009xmldsig_SignatureType_httpwww_w3_org200009xmldsigSignedInfo', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 12, 3), )

    
    SignedInfo = property(__SignedInfo.value, __SignedInfo.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}SignatureValue uses Python identifier SignatureValue
    __SignatureValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignatureValue'), 'SignatureValue', '__httpwww_w3_org200009xmldsig_SignatureType_httpwww_w3_org200009xmldsigSignatureValue', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 13, 3), )

    
    SignatureValue = property(__SignatureValue.value, __SignatureValue.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}KeyInfo uses Python identifier KeyInfo
    __KeyInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KeyInfo'), 'KeyInfo', '__httpwww_w3_org200009xmldsig_SignatureType_httpwww_w3_org200009xmldsigKeyInfo', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 14, 3), )

    
    KeyInfo = property(__KeyInfo.value, __KeyInfo.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_w3_org200009xmldsig_SignatureType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 16, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 16, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __SignedInfo.name() : __SignedInfo,
        __SignatureValue.name() : __SignatureValue,
        __KeyInfo.name() : __KeyInfo
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.SignatureType = SignatureType
Namespace.addCategoryObject('typeBinding', 'SignatureType', SignatureType)


# Complex type {http://www.w3.org/2000/09/xmldsig#}SignatureValueType with content type SIMPLE
class SignatureValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2000/09/xmldsig#}SignatureValueType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignatureValueType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 18, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary
    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_w3_org200009xmldsig_SignatureValueType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 21, 4)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 21, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.SignatureValueType = SignatureValueType
Namespace.addCategoryObject('typeBinding', 'SignatureValueType', SignatureValueType)


# Complex type {http://www.w3.org/2000/09/xmldsig#}SignedInfoType with content type ELEMENT_ONLY
class SignedInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2000/09/xmldsig#}SignedInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignedInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}CanonicalizationMethod uses Python identifier CanonicalizationMethod
    __CanonicalizationMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CanonicalizationMethod'), 'CanonicalizationMethod', '__httpwww_w3_org200009xmldsig_SignedInfoType_httpwww_w3_org200009xmldsigCanonicalizationMethod', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 27, 3), )

    
    CanonicalizationMethod = property(__CanonicalizationMethod.value, __CanonicalizationMethod.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}SignatureMethod uses Python identifier SignatureMethod
    __SignatureMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignatureMethod'), 'SignatureMethod', '__httpwww_w3_org200009xmldsig_SignedInfoType_httpwww_w3_org200009xmldsigSignatureMethod', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 32, 3), )

    
    SignatureMethod = property(__SignatureMethod.value, __SignatureMethod.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__httpwww_w3_org200009xmldsig_SignedInfoType_httpwww_w3_org200009xmldsigReference', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 37, 3), )

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_w3_org200009xmldsig_SignedInfoType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 39, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 39, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __CanonicalizationMethod.name() : __CanonicalizationMethod,
        __SignatureMethod.name() : __SignatureMethod,
        __Reference.name() : __Reference
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.SignedInfoType = SignedInfoType
Namespace.addCategoryObject('typeBinding', 'SignedInfoType', SignedInfoType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 28, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Algorithm uses Python identifier Algorithm
    __Algorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Algorithm'), 'Algorithm', '__httpwww_w3_org200009xmldsig_CTD_ANON_Algorithm', pyxb.binding.datatypes.anyURI, fixed=True, unicode_default='http://www.w3.org/TR/2001/REC-xml-c14n-20010315', required=True)
    __Algorithm._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 29, 5)
    __Algorithm._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 29, 5)
    
    Algorithm = property(__Algorithm.value, __Algorithm.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Algorithm.name() : __Algorithm
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 33, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Algorithm uses Python identifier Algorithm
    __Algorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Algorithm'), 'Algorithm', '__httpwww_w3_org200009xmldsig_CTD_ANON__Algorithm', pyxb.binding.datatypes.anyURI, fixed=True, unicode_default='http://www.w3.org/2000/09/xmldsig#rsa-sha1', required=True)
    __Algorithm._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 34, 5)
    __Algorithm._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 34, 5)
    
    Algorithm = property(__Algorithm.value, __Algorithm.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Algorithm.name() : __Algorithm
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Algorithm uses Python identifier Algorithm
    __Algorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Algorithm'), 'Algorithm', '__httpwww_w3_org200009xmldsig_CTD_ANON_2_Algorithm', pyxb.binding.datatypes.anyURI, fixed=True, unicode_default='http://www.w3.org/2000/09/xmldsig#sha1', required=True)
    __Algorithm._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 52, 5)
    __Algorithm._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 52, 5)
    
    Algorithm = property(__Algorithm.value, __Algorithm.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Algorithm.name() : __Algorithm
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.w3.org/2000/09/xmldsig#}TransformsType with content type ELEMENT_ONLY
class TransformsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2000/09/xmldsig#}TransformsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransformsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 67, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}Transform uses Python identifier Transform
    __Transform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Transform'), 'Transform', '__httpwww_w3_org200009xmldsig_TransformsType_httpwww_w3_org200009xmldsigTransform', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 69, 3), )

    
    Transform = property(__Transform.value, __Transform.set, None, None)

    _ElementMap.update({
        __Transform.name() : __Transform
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TransformsType = TransformsType
Namespace.addCategoryObject('typeBinding', 'TransformsType', TransformsType)


# Complex type {http://www.w3.org/2000/09/xmldsig#}KeyInfoType with content type ELEMENT_ONLY
class KeyInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2000/09/xmldsig#}KeyInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'KeyInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 78, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}X509Data uses Python identifier X509Data
    __X509Data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'X509Data'), 'X509Data', '__httpwww_w3_org200009xmldsig_KeyInfoType_httpwww_w3_org200009xmldsigX509Data', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 80, 3), )

    
    X509Data = property(__X509Data.value, __X509Data.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_w3_org200009xmldsig_KeyInfoType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 82, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 82, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __X509Data.name() : __X509Data
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.KeyInfoType = KeyInfoType
Namespace.addCategoryObject('typeBinding', 'KeyInfoType', KeyInfoType)


# Complex type {http://www.w3.org/2000/09/xmldsig#}X509DataType with content type ELEMENT_ONLY
class X509DataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2000/09/xmldsig#}X509DataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'X509DataType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 84, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}X509Certificate uses Python identifier X509Certificate
    __X509Certificate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'X509Certificate'), 'X509Certificate', '__httpwww_w3_org200009xmldsig_X509DataType_httpwww_w3_org200009xmldsigX509Certificate', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 86, 3), )

    
    X509Certificate = property(__X509Certificate.value, __X509Certificate.set, None, None)

    _ElementMap.update({
        __X509Certificate.name() : __X509Certificate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.X509DataType = X509DataType
Namespace.addCategoryObject('typeBinding', 'X509DataType', X509DataType)


# Complex type {http://www.w3.org/2000/09/xmldsig#}ReferenceType with content type ELEMENT_ONLY
class ReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2000/09/xmldsig#}ReferenceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 41, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}Transforms uses Python identifier Transforms
    __Transforms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Transforms'), 'Transforms', '__httpwww_w3_org200009xmldsig_ReferenceType_httpwww_w3_org200009xmldsigTransforms', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 43, 3), )

    
    Transforms = property(__Transforms.value, __Transforms.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}DigestMethod uses Python identifier DigestMethod
    __DigestMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DigestMethod'), 'DigestMethod', '__httpwww_w3_org200009xmldsig_ReferenceType_httpwww_w3_org200009xmldsigDigestMethod', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 50, 3), )

    
    DigestMethod = property(__DigestMethod.value, __DigestMethod.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}DigestValue uses Python identifier DigestValue
    __DigestValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DigestValue'), 'DigestValue', '__httpwww_w3_org200009xmldsig_ReferenceType_httpwww_w3_org200009xmldsigDigestValue', False, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 55, 3), )

    
    DigestValue = property(__DigestValue.value, __DigestValue.set, None, None)

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_w3_org200009xmldsig_ReferenceType_Id', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 57, 2)
    __Id._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 57, 2)
    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Attribute URI uses Python identifier URI
    __URI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'URI'), 'URI', '__httpwww_w3_org200009xmldsig_ReferenceType_URI', _module_typeBindings.STD_ANON, required=True)
    __URI._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 58, 2)
    __URI._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 58, 2)
    
    URI = property(__URI.value, __URI.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__httpwww_w3_org200009xmldsig_ReferenceType_Type', pyxb.binding.datatypes.anyURI)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 65, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 65, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        __Transforms.name() : __Transforms,
        __DigestMethod.name() : __DigestMethod,
        __DigestValue.name() : __DigestValue
    })
    _AttributeMap.update({
        __Id.name() : __Id,
        __URI.name() : __URI,
        __Type.name() : __Type
    })
_module_typeBindings.ReferenceType = ReferenceType
Namespace.addCategoryObject('typeBinding', 'ReferenceType', ReferenceType)


# Complex type {http://www.w3.org/2000/09/xmldsig#}TransformType with content type ELEMENT_ONLY
class TransformType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2000/09/xmldsig#}TransformType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransformType')
    _XSDLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 72, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}XPath uses Python identifier XPath
    __XPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'XPath'), 'XPath', '__httpwww_w3_org200009xmldsig_TransformType_httpwww_w3_org200009xmldsigXPath', True, pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 74, 3), )

    
    XPath = property(__XPath.value, __XPath.set, None, None)

    
    # Attribute Algorithm uses Python identifier Algorithm
    __Algorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Algorithm'), 'Algorithm', '__httpwww_w3_org200009xmldsig_TransformType_Algorithm', _module_typeBindings.TTransformURI, required=True)
    __Algorithm._DeclarationLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 76, 2)
    __Algorithm._UseLocation = pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 76, 2)
    
    Algorithm = property(__Algorithm.value, __Algorithm.set, None, None)

    _ElementMap.update({
        __XPath.name() : __XPath
    })
    _AttributeMap.update({
        __Algorithm.name() : __Algorithm
    })
_module_typeBindings.TransformType = TransformType
Namespace.addCategoryObject('typeBinding', 'TransformType', TransformType)


Signature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Signature'), SignatureType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 9, 1))
Namespace.addCategoryObject('elementBinding', Signature.name().localName(), Signature)



SignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedInfo'), SignedInfoType, scope=SignatureType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 12, 3)))

SignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignatureValue'), SignatureValueType, scope=SignatureType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 13, 3)))

SignatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KeyInfo'), KeyInfoType, scope=SignatureType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 14, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignedInfo')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 12, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignatureValue')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 13, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SignatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KeyInfo')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 14, 3))
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
SignatureType._Automaton = _BuildAutomaton()




SignedInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CanonicalizationMethod'), CTD_ANON, scope=SignedInfoType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 27, 3)))

SignedInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignatureMethod'), CTD_ANON_, scope=SignedInfoType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 32, 3)))

SignedInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), ReferenceType, scope=SignedInfoType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 37, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignedInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CanonicalizationMethod')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignedInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignatureMethod')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 32, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SignedInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 37, 3))
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
SignedInfoType._Automaton = _BuildAutomaton_()




TransformsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Transform'), TransformType, scope=TransformsType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 69, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 69, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransformsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Transform')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 69, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TransformsType._Automaton = _BuildAutomaton_2()




KeyInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'X509Data'), X509DataType, scope=KeyInfoType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 80, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(KeyInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'X509Data')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 80, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
KeyInfoType._Automaton = _BuildAutomaton_3()




X509DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'X509Certificate'), pyxb.binding.datatypes.base64Binary, scope=X509DataType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 86, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(X509DataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'X509Certificate')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
X509DataType._Automaton = _BuildAutomaton_4()




ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Transforms'), TransformsType, scope=ReferenceType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 43, 3)))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DigestMethod'), CTD_ANON_2, scope=ReferenceType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 50, 3)))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DigestValue'), DigestValueType, scope=ReferenceType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 55, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Transforms')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 43, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DigestMethod')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 50, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DigestValue')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 55, 3))
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
ReferenceType._Automaton = _BuildAutomaton_5()




TransformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XPath'), pyxb.binding.datatypes.string, scope=TransformType, location=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 74, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 73, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransformType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XPath')), pyxb.utils.utility.Location('/home/philippeoz/Downloads/NotaFiscal/exemplosws/SchemaXSD/xmldsig-core-schema_v1.01.xsd', 74, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TransformType._Automaton = _BuildAutomaton_6()

