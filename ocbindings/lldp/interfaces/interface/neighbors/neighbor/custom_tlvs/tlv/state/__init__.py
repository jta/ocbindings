# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.yangtypes import YANGBinary
from pyangbind.lib.yangtypes import YANGBitsType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal

import builtins as __builtin__
long = int
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-lldp - based on the path /lldp/interfaces/interface/neighbors/neighbor/custom-tlvs/tlv/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__type','__oui','__oui_subtype','__value',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/lldp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='int32', is_config=False)
    self.__oui = YANGDynClass(base=str, is_leaf=True, yang_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)
    self.__oui_subtype = YANGDynClass(base=str, is_leaf=True, yang_name="oui-subtype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)
    self.__value = YANGDynClass(base=YANGBinary, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='binary', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['lldp', 'interfaces', 'interface', 'neighbors', 'neighbor', 'custom-tlvs', 'tlv', 'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/type (int32)

    YANG Description: The integer value identifying the type of information
contained in the value field.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/type (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The integer value identifying the type of information
contained in the value field.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='int32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='int32', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='int32', is_config=False)


  def _get_oui(self):
    """
    Getter method for oui, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/oui (string)

    YANG Description: The organizationally unique identifier field shall contain
the organization's OUI as defined in Clause 9 of IEEE Std
802. The high-order octet is 0 and the low-order 3 octets
are the SMI Network Management Private Enterprise Code of
the Vendor in network byte order, as defined in the
'Assigned Numbers' RFC [RFC3232].
    """
    return self.__oui
      
  def _set_oui(self, v, load=False):
    """
    Setter method for oui, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/oui (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oui is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oui() directly.

    YANG Description: The organizationally unique identifier field shall contain
the organization's OUI as defined in Clause 9 of IEEE Std
802. The high-order octet is 0 and the low-order 3 octets
are the SMI Network Management Private Enterprise Code of
the Vendor in network byte order, as defined in the
'Assigned Numbers' RFC [RFC3232].
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oui must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)""",
        })

    self.__oui = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oui(self):
    self.__oui = YANGDynClass(base=str, is_leaf=True, yang_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)


  def _get_oui_subtype(self):
    """
    Getter method for oui_subtype, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/oui_subtype (string)

    YANG Description: The organizationally defined subtype field shall contain a
unique subtype value assigned by the defining organization.
    """
    return self.__oui_subtype
      
  def _set_oui_subtype(self, v, load=False):
    """
    Setter method for oui_subtype, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/oui_subtype (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oui_subtype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oui_subtype() directly.

    YANG Description: The organizationally defined subtype field shall contain a
unique subtype value assigned by the defining organization.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="oui-subtype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oui_subtype must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="oui-subtype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)""",
        })

    self.__oui_subtype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oui_subtype(self):
    self.__oui_subtype = YANGDynClass(base=str, is_leaf=True, yang_name="oui-subtype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/value (binary)

    YANG Description: A variable-length octet-string containing the
instance-specific information for this TLV.
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/value (binary)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: A variable-length octet-string containing the
instance-specific information for this TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBinary, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='binary', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with binary""",
          'defined-type': "binary",
          'generated-type': """YANGDynClass(base=YANGBinary, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='binary', is_config=False)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=YANGBinary, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='binary', is_config=False)

  type = __builtin__.property(_get_type)
  oui = __builtin__.property(_get_oui)
  oui_subtype = __builtin__.property(_get_oui_subtype)
  value = __builtin__.property(_get_value)


  _pyangbind_elements = OrderedDict([('type', type), ('oui', oui), ('oui_subtype', oui_subtype), ('value', value), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-lldp - based on the path /lldp/interfaces/interface/neighbors/neighbor/custom-tlvs/tlv/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__type','__oui','__oui_subtype','__value',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/lldp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='int32', is_config=False)
    self.__oui = YANGDynClass(base=str, is_leaf=True, yang_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)
    self.__oui_subtype = YANGDynClass(base=str, is_leaf=True, yang_name="oui-subtype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)
    self.__value = YANGDynClass(base=YANGBinary, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='binary', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['lldp', 'interfaces', 'interface', 'neighbors', 'neighbor', 'custom-tlvs', 'tlv', 'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/type (int32)

    YANG Description: The integer value identifying the type of information
contained in the value field.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/type (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The integer value identifying the type of information
contained in the value field.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='int32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='int32', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='int32', is_config=False)


  def _get_oui(self):
    """
    Getter method for oui, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/oui (string)

    YANG Description: The organizationally unique identifier field shall contain
the organization's OUI as defined in Clause 9 of IEEE Std
802. The high-order octet is 0 and the low-order 3 octets
are the SMI Network Management Private Enterprise Code of
the Vendor in network byte order, as defined in the
'Assigned Numbers' RFC [RFC3232].
    """
    return self.__oui
      
  def _set_oui(self, v, load=False):
    """
    Setter method for oui, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/oui (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oui is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oui() directly.

    YANG Description: The organizationally unique identifier field shall contain
the organization's OUI as defined in Clause 9 of IEEE Std
802. The high-order octet is 0 and the low-order 3 octets
are the SMI Network Management Private Enterprise Code of
the Vendor in network byte order, as defined in the
'Assigned Numbers' RFC [RFC3232].
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oui must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)""",
        })

    self.__oui = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oui(self):
    self.__oui = YANGDynClass(base=str, is_leaf=True, yang_name="oui", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)


  def _get_oui_subtype(self):
    """
    Getter method for oui_subtype, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/oui_subtype (string)

    YANG Description: The organizationally defined subtype field shall contain a
unique subtype value assigned by the defining organization.
    """
    return self.__oui_subtype
      
  def _set_oui_subtype(self, v, load=False):
    """
    Setter method for oui_subtype, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/oui_subtype (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oui_subtype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oui_subtype() directly.

    YANG Description: The organizationally defined subtype field shall contain a
unique subtype value assigned by the defining organization.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="oui-subtype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oui_subtype must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="oui-subtype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)""",
        })

    self.__oui_subtype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oui_subtype(self):
    self.__oui_subtype = YANGDynClass(base=str, is_leaf=True, yang_name="oui-subtype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='string', is_config=False)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/value (binary)

    YANG Description: A variable-length octet-string containing the
instance-specific information for this TLV.
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv/state/value (binary)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: A variable-length octet-string containing the
instance-specific information for this TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBinary, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='binary', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with binary""",
          'defined-type': "binary",
          'generated-type': """YANGDynClass(base=YANGBinary, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='binary', is_config=False)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=YANGBinary, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='binary', is_config=False)

  type = __builtin__.property(_get_type)
  oui = __builtin__.property(_get_oui)
  oui_subtype = __builtin__.property(_get_oui_subtype)
  value = __builtin__.property(_get_value)


  _pyangbind_elements = OrderedDict([('type', type), ('oui', oui), ('oui_subtype', oui_subtype), ('value', value), ])


