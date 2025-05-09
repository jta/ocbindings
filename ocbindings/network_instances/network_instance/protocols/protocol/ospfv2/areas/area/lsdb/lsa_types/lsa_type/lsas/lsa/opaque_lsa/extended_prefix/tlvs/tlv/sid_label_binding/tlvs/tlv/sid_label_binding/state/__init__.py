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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/sid-label-binding/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameteres relating to the SID/Label Binding
sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__sid_type','__sid_value',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sid_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    self.__sid_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'extended-prefix', 'tlvs', 'tlv', 'sid-label-binding', 'tlvs', 'tlv', 'sid-label-binding', 'state']

  def _get_sid_type(self):
    """
    Getter method for sid_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_type (oc-ospf-types:sr-sid-type)

    YANG Description: The type of the value contained within the sub-TLV
    """
    return self.__sid_type
      
  def _set_sid_type(self, v, load=False):
    """
    Setter method for sid_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_type (oc-ospf-types:sr-sid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_type() directly.

    YANG Description: The type of the value contained within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_type must be of a type compatible with oc-ospf-types:sr-sid-type""",
          'defined-type': "oc-ospf-types:sr-sid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)""",
        })

    self.__sid_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_type(self):
    self.__sid_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)


  def _get_sid_value(self):
    """
    Getter method for sid_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_value (uint32)

    YANG Description: The value of the binding included within the sub-TLV. The type of
this binding is indicated by the type leaf.
    """
    return self.__sid_value
      
  def _set_sid_value(self, v, load=False):
    """
    Setter method for sid_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_value() directly.

    YANG Description: The value of the binding included within the sub-TLV. The type of
this binding is indicated by the type leaf.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__sid_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_value(self):
    self.__sid_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  sid_type = __builtin__.property(_get_sid_type)
  sid_value = __builtin__.property(_get_sid_value)


  _pyangbind_elements = OrderedDict([('sid_type', sid_type), ('sid_value', sid_value), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/sid-label-binding/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameteres relating to the SID/Label Binding
sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__sid_type','__sid_value',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sid_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    self.__sid_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'extended-prefix', 'tlvs', 'tlv', 'sid-label-binding', 'tlvs', 'tlv', 'sid-label-binding', 'state']

  def _get_sid_type(self):
    """
    Getter method for sid_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_type (oc-ospf-types:sr-sid-type)

    YANG Description: The type of the value contained within the sub-TLV
    """
    return self.__sid_type
      
  def _set_sid_type(self, v, load=False):
    """
    Setter method for sid_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_type (oc-ospf-types:sr-sid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_type() directly.

    YANG Description: The type of the value contained within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_type must be of a type compatible with oc-ospf-types:sr-sid-type""",
          'defined-type': "oc-ospf-types:sr-sid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)""",
        })

    self.__sid_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_type(self):
    self.__sid_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)


  def _get_sid_value(self):
    """
    Getter method for sid_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_value (uint32)

    YANG Description: The value of the binding included within the sub-TLV. The type of
this binding is indicated by the type leaf.
    """
    return self.__sid_value
      
  def _set_sid_value(self, v, load=False):
    """
    Setter method for sid_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_value() directly.

    YANG Description: The value of the binding included within the sub-TLV. The type of
this binding is indicated by the type leaf.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__sid_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_value(self):
    self.__sid_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  sid_type = __builtin__.property(_get_sid_type)
  sid_value = __builtin__.property(_get_sid_value)


  _pyangbind_elements = OrderedDict([('sid_type', sid_type), ('sid_value', sid_value), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/sid-label-binding/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameteres relating to the SID/Label Binding
sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__sid_type','__sid_value',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sid_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    self.__sid_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'extended-prefix', 'tlvs', 'tlv', 'sid-label-binding', 'tlvs', 'tlv', 'sid-label-binding', 'state']

  def _get_sid_type(self):
    """
    Getter method for sid_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_type (oc-ospf-types:sr-sid-type)

    YANG Description: The type of the value contained within the sub-TLV
    """
    return self.__sid_type
      
  def _set_sid_type(self, v, load=False):
    """
    Setter method for sid_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_type (oc-ospf-types:sr-sid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_type() directly.

    YANG Description: The type of the value contained within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_type must be of a type compatible with oc-ospf-types:sr-sid-type""",
          'defined-type': "oc-ospf-types:sr-sid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)""",
        })

    self.__sid_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_type(self):
    self.__sid_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)


  def _get_sid_value(self):
    """
    Getter method for sid_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_value (uint32)

    YANG Description: The value of the binding included within the sub-TLV. The type of
this binding is indicated by the type leaf.
    """
    return self.__sid_value
      
  def _set_sid_value(self, v, load=False):
    """
    Setter method for sid_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_value() directly.

    YANG Description: The value of the binding included within the sub-TLV. The type of
this binding is indicated by the type leaf.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__sid_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_value(self):
    self.__sid_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  sid_type = __builtin__.property(_get_sid_type)
  sid_value = __builtin__.property(_get_sid_value)


  _pyangbind_elements = OrderedDict([('sid_type', sid_type), ('sid_value', sid_value), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/sid-label-binding/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameteres relating to the SID/Label Binding
sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__sid_type','__sid_value',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sid_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    self.__sid_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'extended-prefix', 'tlvs', 'tlv', 'sid-label-binding', 'tlvs', 'tlv', 'sid-label-binding', 'state']

  def _get_sid_type(self):
    """
    Getter method for sid_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_type (oc-ospf-types:sr-sid-type)

    YANG Description: The type of the value contained within the sub-TLV
    """
    return self.__sid_type
      
  def _set_sid_type(self, v, load=False):
    """
    Setter method for sid_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_type (oc-ospf-types:sr-sid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_type() directly.

    YANG Description: The type of the value contained within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_type must be of a type compatible with oc-ospf-types:sr-sid-type""",
          'defined-type': "oc-ospf-types:sr-sid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)""",
        })

    self.__sid_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_type(self):
    self.__sid_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'LABEL': {}, 'SID': {}},), is_leaf=True, yang_name="sid-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:sr-sid-type', is_config=False)


  def _get_sid_value(self):
    """
    Getter method for sid_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_value (uint32)

    YANG Description: The value of the binding included within the sub-TLV. The type of
this binding is indicated by the type leaf.
    """
    return self.__sid_value
      
  def _set_sid_value(self, v, load=False):
    """
    Setter method for sid_value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/sid_label_binding/state/sid_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_value() directly.

    YANG Description: The value of the binding included within the sub-TLV. The type of
this binding is indicated by the type leaf.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sid_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__sid_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sid_value(self):
    self.__sid_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sid-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  sid_type = __builtin__.property(_get_sid_type)
  sid_value = __builtin__.property(_get_sid_value)


  _pyangbind_elements = OrderedDict([('sid_type', sid_type), ('sid_value', sid_value), ])


