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
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each configured IPv4
address on the interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip','__link_layer_address',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv4-address', is_config=True)
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'subinterfaces', 'subinterface', 'ipv4', 'neighbors', 'neighbor', 'config']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /access_points/access_point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config/ip (oc-inet:ipv4-address)

    YANG Description: The IPv4 address of the neighbor node.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /access_points/access_point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config/ip (oc-inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IPv4 address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with oc-inet:ipv4-address""",
          'defined-type': "oc-inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv4-address', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv4-address', is_config=True)


  def _get_link_layer_address(self):
    """
    Getter method for link_layer_address, mapped from YANG variable /access_points/access_point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config/link_layer_address (oc-yang:phys-address)

    YANG Description: The link-layer address of the neighbor node.
    """
    return self.__link_layer_address
      
  def _set_link_layer_address(self, v, load=False):
    """
    Setter method for link_layer_address, mapped from YANG variable /access_points/access_point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config/link_layer_address (oc-yang:phys-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_layer_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_layer_address() directly.

    YANG Description: The link-layer address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_layer_address must be of a type compatible with oc-yang:phys-address""",
          'defined-type': "oc-yang:phys-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=True)""",
        })

    self.__link_layer_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_layer_address(self):
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=True)

  ip = __builtin__.property(_get_ip, _set_ip)
  link_layer_address = __builtin__.property(_get_link_layer_address, _set_link_layer_address)


  _pyangbind_elements = OrderedDict([('ip', ip), ('link_layer_address', link_layer_address), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each configured IPv4
address on the interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip','__link_layer_address',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv4-address', is_config=True)
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'subinterfaces', 'subinterface', 'ipv4', 'neighbors', 'neighbor', 'config']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /access_points/access_point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config/ip (oc-inet:ipv4-address)

    YANG Description: The IPv4 address of the neighbor node.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /access_points/access_point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config/ip (oc-inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IPv4 address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with oc-inet:ipv4-address""",
          'defined-type': "oc-inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv4-address', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv4-address', is_config=True)


  def _get_link_layer_address(self):
    """
    Getter method for link_layer_address, mapped from YANG variable /access_points/access_point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config/link_layer_address (oc-yang:phys-address)

    YANG Description: The link-layer address of the neighbor node.
    """
    return self.__link_layer_address
      
  def _set_link_layer_address(self, v, load=False):
    """
    Setter method for link_layer_address, mapped from YANG variable /access_points/access_point/interfaces/interface/subinterfaces/subinterface/ipv4/neighbors/neighbor/config/link_layer_address (oc-yang:phys-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_layer_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_layer_address() directly.

    YANG Description: The link-layer address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_layer_address must be of a type compatible with oc-yang:phys-address""",
          'defined-type': "oc-yang:phys-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=True)""",
        })

    self.__link_layer_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_layer_address(self):
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=True)

  ip = __builtin__.property(_get_ip, _set_ip)
  link_layer_address = __builtin__.property(_get_link_layer_address, _set_link_layer_address)


  _pyangbind_elements = OrderedDict([('ip', ip), ('link_layer_address', link_layer_address), ])


