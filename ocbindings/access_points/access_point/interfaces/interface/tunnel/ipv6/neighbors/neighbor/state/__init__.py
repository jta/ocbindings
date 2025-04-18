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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State data for each IPv6 address on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip','__link_layer_address','__origin','__is_router','__neighbor_state',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv6-address', is_config=False)
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=False)
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DYNAMIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='neighbor-origin', is_config=False)
    self.__is_router = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)
    self.__neighbor_state = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INCOMPLETE': {}, 'REACHABLE': {}, 'STALE': {}, 'DELAY': {}, 'PROBE': {}},), is_leaf=True, yang_name="neighbor-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=False)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'tunnel', 'ipv6', 'neighbors', 'neighbor', 'state']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/ip (oc-inet:ipv6-address)

    YANG Description: The IPv6 address of the neighbor node.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/ip (oc-inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IPv6 address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv6-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with oc-inet:ipv6-address""",
          'defined-type': "oc-inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv6-address', is_config=False)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv6-address', is_config=False)


  def _get_link_layer_address(self):
    """
    Getter method for link_layer_address, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/link_layer_address (oc-yang:phys-address)

    YANG Description: The link-layer address of the neighbor node.
    """
    return self.__link_layer_address
      
  def _set_link_layer_address(self, v, load=False):
    """
    Setter method for link_layer_address, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/link_layer_address (oc-yang:phys-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_layer_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_layer_address() directly.

    YANG Description: The link-layer address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_layer_address must be of a type compatible with oc-yang:phys-address""",
          'defined-type': "oc-yang:phys-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=False)""",
        })

    self.__link_layer_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_layer_address(self):
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=False)


  def _get_origin(self):
    """
    Getter method for origin, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/origin (neighbor-origin)

    YANG Description: The origin of this neighbor entry.
    """
    return self.__origin
      
  def _set_origin(self, v, load=False):
    """
    Setter method for origin, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/origin (neighbor-origin)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin() directly.

    YANG Description: The origin of this neighbor entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DYNAMIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='neighbor-origin', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin must be of a type compatible with neighbor-origin""",
          'defined-type': "openconfig-ap-interfaces:neighbor-origin",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DYNAMIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='neighbor-origin', is_config=False)""",
        })

    self.__origin = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin(self):
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DYNAMIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='neighbor-origin', is_config=False)


  def _get_is_router(self):
    """
    Getter method for is_router, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/is_router (boolean)

    YANG Description: Indicates that the neighbor node acts as a router.
    """
    return self.__is_router
      
  def _set_is_router(self, v, load=False):
    """
    Setter method for is_router, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/is_router (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_router is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_router() directly.

    YANG Description: Indicates that the neighbor node acts as a router.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="is-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_router must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)""",
        })

    self.__is_router = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_router(self):
    self.__is_router = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)


  def _get_neighbor_state(self):
    """
    Getter method for neighbor_state, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/neighbor_state (enumeration)

    YANG Description: The Neighbor Unreachability Detection state of this
entry.
    """
    return self.__neighbor_state
      
  def _set_neighbor_state(self, v, load=False):
    """
    Setter method for neighbor_state, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/neighbor_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_state() directly.

    YANG Description: The Neighbor Unreachability Detection state of this
entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INCOMPLETE': {}, 'REACHABLE': {}, 'STALE': {}, 'DELAY': {}, 'PROBE': {}},), is_leaf=True, yang_name="neighbor-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_state must be of a type compatible with enumeration""",
          'defined-type': "openconfig-ap-interfaces:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INCOMPLETE': {}, 'REACHABLE': {}, 'STALE': {}, 'DELAY': {}, 'PROBE': {}},), is_leaf=True, yang_name="neighbor-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=False)""",
        })

    self.__neighbor_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_state(self):
    self.__neighbor_state = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INCOMPLETE': {}, 'REACHABLE': {}, 'STALE': {}, 'DELAY': {}, 'PROBE': {}},), is_leaf=True, yang_name="neighbor-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=False)

  ip = __builtin__.property(_get_ip)
  link_layer_address = __builtin__.property(_get_link_layer_address)
  origin = __builtin__.property(_get_origin)
  is_router = __builtin__.property(_get_is_router)
  neighbor_state = __builtin__.property(_get_neighbor_state)


  _pyangbind_elements = OrderedDict([('ip', ip), ('link_layer_address', link_layer_address), ('origin', origin), ('is_router', is_router), ('neighbor_state', neighbor_state), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State data for each IPv6 address on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip','__link_layer_address','__origin','__is_router','__neighbor_state',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv6-address', is_config=False)
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=False)
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DYNAMIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='neighbor-origin', is_config=False)
    self.__is_router = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)
    self.__neighbor_state = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INCOMPLETE': {}, 'REACHABLE': {}, 'STALE': {}, 'DELAY': {}, 'PROBE': {}},), is_leaf=True, yang_name="neighbor-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=False)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'tunnel', 'ipv6', 'neighbors', 'neighbor', 'state']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/ip (oc-inet:ipv6-address)

    YANG Description: The IPv6 address of the neighbor node.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/ip (oc-inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IPv6 address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv6-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with oc-inet:ipv6-address""",
          'defined-type': "oc-inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv6-address', is_config=False)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-inet:ipv6-address', is_config=False)


  def _get_link_layer_address(self):
    """
    Getter method for link_layer_address, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/link_layer_address (oc-yang:phys-address)

    YANG Description: The link-layer address of the neighbor node.
    """
    return self.__link_layer_address
      
  def _set_link_layer_address(self, v, load=False):
    """
    Setter method for link_layer_address, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/link_layer_address (oc-yang:phys-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_layer_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_layer_address() directly.

    YANG Description: The link-layer address of the neighbor node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_layer_address must be of a type compatible with oc-yang:phys-address""",
          'defined-type': "oc-yang:phys-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=False)""",
        })

    self.__link_layer_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_layer_address(self):
    self.__link_layer_address = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}), is_leaf=True, yang_name="link-layer-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='oc-yang:phys-address', is_config=False)


  def _get_origin(self):
    """
    Getter method for origin, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/origin (neighbor-origin)

    YANG Description: The origin of this neighbor entry.
    """
    return self.__origin
      
  def _set_origin(self, v, load=False):
    """
    Setter method for origin, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/origin (neighbor-origin)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin() directly.

    YANG Description: The origin of this neighbor entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DYNAMIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='neighbor-origin', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin must be of a type compatible with neighbor-origin""",
          'defined-type': "openconfig-ap-interfaces:neighbor-origin",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DYNAMIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='neighbor-origin', is_config=False)""",
        })

    self.__origin = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin(self):
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'OTHER': {}, 'STATIC': {}, 'DYNAMIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='neighbor-origin', is_config=False)


  def _get_is_router(self):
    """
    Getter method for is_router, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/is_router (boolean)

    YANG Description: Indicates that the neighbor node acts as a router.
    """
    return self.__is_router
      
  def _set_is_router(self, v, load=False):
    """
    Setter method for is_router, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/is_router (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_router is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_router() directly.

    YANG Description: Indicates that the neighbor node acts as a router.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="is-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_router must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)""",
        })

    self.__is_router = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_router(self):
    self.__is_router = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)


  def _get_neighbor_state(self):
    """
    Getter method for neighbor_state, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/neighbor_state (enumeration)

    YANG Description: The Neighbor Unreachability Detection state of this
entry.
    """
    return self.__neighbor_state
      
  def _set_neighbor_state(self, v, load=False):
    """
    Setter method for neighbor_state, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/neighbors/neighbor/state/neighbor_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_state() directly.

    YANG Description: The Neighbor Unreachability Detection state of this
entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INCOMPLETE': {}, 'REACHABLE': {}, 'STALE': {}, 'DELAY': {}, 'PROBE': {}},), is_leaf=True, yang_name="neighbor-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_state must be of a type compatible with enumeration""",
          'defined-type': "openconfig-ap-interfaces:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INCOMPLETE': {}, 'REACHABLE': {}, 'STALE': {}, 'DELAY': {}, 'PROBE': {}},), is_leaf=True, yang_name="neighbor-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=False)""",
        })

    self.__neighbor_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_state(self):
    self.__neighbor_state = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INCOMPLETE': {}, 'REACHABLE': {}, 'STALE': {}, 'DELAY': {}, 'PROBE': {}},), is_leaf=True, yang_name="neighbor-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=False)

  ip = __builtin__.property(_get_ip)
  link_layer_address = __builtin__.property(_get_link_layer_address)
  origin = __builtin__.property(_get_origin)
  is_router = __builtin__.property(_get_is_router)
  neighbor_state = __builtin__.property(_get_neighbor_state)


  _pyangbind_elements = OrderedDict([('ip', ip), ('link_layer_address', link_layer_address), ('origin', origin), ('is_router', is_router), ('neighbor_state', neighbor_state), ])


