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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv4/addresses/address/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for each IPv4 address
configured on the interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip','__prefix_length','__type','__origin',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ipv4-address', is_config=False)
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'PRIMARY': {}, 'SECONDARY': {}},), default=str("PRIMARY"), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ipv4-address-type', is_config=False)
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DHCP': {}, 'LINK_LAYER': {}, 'RANDOM': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)

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
      return ['interfaces', 'interface', 'routed-vlan', 'ipv4', 'addresses', 'address', 'state']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/ip (oc-inet:ipv4-address)

    YANG Description: The IPv4 address on the interface.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/ip (oc-inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IPv4 address on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with oc-inet:ipv4-address""",
          'defined-type': "oc-inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ipv4-address', is_config=False)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ipv4-address', is_config=False)


  def _get_prefix_length(self):
    """
    Getter method for prefix_length, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/prefix_length (uint8)

    YANG Description: The length of the subnet prefix.
    """
    return self.__prefix_length
      
  def _set_prefix_length(self, v, load=False):
    """
    Setter method for prefix_length, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/prefix_length (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_length() directly.

    YANG Description: The length of the subnet prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_length must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)""",
        })

    self.__prefix_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_length(self):
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/type (ipv4-address-type)

    YANG Description: Specifies the explicit type of the IPv4 address being assigned
to the interface. By default, addresses are assumed to be a primary address.
Where secondary addresses is to be configured, this leaf should be set
to SECONDARY.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/type (ipv4-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: Specifies the explicit type of the IPv4 address being assigned
to the interface. By default, addresses are assumed to be a primary address.
Where secondary addresses is to be configured, this leaf should be set
to SECONDARY.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'PRIMARY': {}, 'SECONDARY': {}},), default=str("PRIMARY"), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ipv4-address-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with ipv4-address-type""",
          'defined-type': "openconfig-if-ip:ipv4-address-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'PRIMARY': {}, 'SECONDARY': {}},), default=str("PRIMARY"), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ipv4-address-type', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'PRIMARY': {}, 'SECONDARY': {}},), default=str("PRIMARY"), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ipv4-address-type', is_config=False)


  def _get_origin(self):
    """
    Getter method for origin, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/origin (ip-address-origin)

    YANG Description: The origin of this address, e.g., statically configured,
assigned by DHCP, etc..
    """
    return self.__origin
      
  def _set_origin(self, v, load=False):
    """
    Setter method for origin, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/origin (ip-address-origin)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin() directly.

    YANG Description: The origin of this address, e.g., statically configured,
assigned by DHCP, etc..
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DHCP': {}, 'LINK_LAYER': {}, 'RANDOM': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin must be of a type compatible with ip-address-origin""",
          'defined-type': "openconfig-if-ip:ip-address-origin",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DHCP': {}, 'LINK_LAYER': {}, 'RANDOM': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)""",
        })

    self.__origin = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin(self):
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DHCP': {}, 'LINK_LAYER': {}, 'RANDOM': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)

  ip = __builtin__.property(_get_ip)
  prefix_length = __builtin__.property(_get_prefix_length)
  type = __builtin__.property(_get_type)
  origin = __builtin__.property(_get_origin)


  _pyangbind_elements = OrderedDict([('ip', ip), ('prefix_length', prefix_length), ('type', type), ('origin', origin), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv4/addresses/address/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for each IPv4 address
configured on the interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip','__prefix_length','__type','__origin',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ipv4-address', is_config=False)
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'PRIMARY': {}, 'SECONDARY': {}},), default=str("PRIMARY"), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ipv4-address-type', is_config=False)
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DHCP': {}, 'LINK_LAYER': {}, 'RANDOM': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)

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
      return ['interfaces', 'interface', 'routed-vlan', 'ipv4', 'addresses', 'address', 'state']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/ip (oc-inet:ipv4-address)

    YANG Description: The IPv4 address on the interface.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/ip (oc-inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IPv4 address on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with oc-inet:ipv4-address""",
          'defined-type': "oc-inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ipv4-address', is_config=False)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ipv4-address', is_config=False)


  def _get_prefix_length(self):
    """
    Getter method for prefix_length, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/prefix_length (uint8)

    YANG Description: The length of the subnet prefix.
    """
    return self.__prefix_length
      
  def _set_prefix_length(self, v, load=False):
    """
    Setter method for prefix_length, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/prefix_length (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_length() directly.

    YANG Description: The length of the subnet prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_length must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)""",
        })

    self.__prefix_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_length(self):
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/type (ipv4-address-type)

    YANG Description: Specifies the explicit type of the IPv4 address being assigned
to the interface. By default, addresses are assumed to be a primary address.
Where secondary addresses is to be configured, this leaf should be set
to SECONDARY.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/type (ipv4-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: Specifies the explicit type of the IPv4 address being assigned
to the interface. By default, addresses are assumed to be a primary address.
Where secondary addresses is to be configured, this leaf should be set
to SECONDARY.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'PRIMARY': {}, 'SECONDARY': {}},), default=str("PRIMARY"), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ipv4-address-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with ipv4-address-type""",
          'defined-type': "openconfig-if-ip:ipv4-address-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'PRIMARY': {}, 'SECONDARY': {}},), default=str("PRIMARY"), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ipv4-address-type', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'PRIMARY': {}, 'SECONDARY': {}},), default=str("PRIMARY"), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ipv4-address-type', is_config=False)


  def _get_origin(self):
    """
    Getter method for origin, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/origin (ip-address-origin)

    YANG Description: The origin of this address, e.g., statically configured,
assigned by DHCP, etc..
    """
    return self.__origin
      
  def _set_origin(self, v, load=False):
    """
    Setter method for origin, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/state/origin (ip-address-origin)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin() directly.

    YANG Description: The origin of this address, e.g., statically configured,
assigned by DHCP, etc..
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DHCP': {}, 'LINK_LAYER': {}, 'RANDOM': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin must be of a type compatible with ip-address-origin""",
          'defined-type': "openconfig-if-ip:ip-address-origin",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DHCP': {}, 'LINK_LAYER': {}, 'RANDOM': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)""",
        })

    self.__origin = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin(self):
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DHCP': {}, 'LINK_LAYER': {}, 'RANDOM': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)

  ip = __builtin__.property(_get_ip)
  prefix_length = __builtin__.property(_get_prefix_length)
  type = __builtin__.property(_get_type)
  origin = __builtin__.property(_get_origin)


  _pyangbind_elements = OrderedDict([('ip', ip), ('prefix_length', prefix_length), ('type', type), ('origin', origin), ])


