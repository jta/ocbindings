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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the global BGP router
  """
  __slots__ = ('_path_helper', '_extmethods', '__as_','__router_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'config']

  def _get_as_(self):
    """
    Getter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/as (oc-inet:as-number)

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    return self.__as_
      
  def _set_as_(self, v, load=False):
    """
    Setter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/as (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_() directly.

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_ must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)""",
        })

    self.__as_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_(self):
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)


  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/router_id (oc-yang:dotted-quad)

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/router_id (oc-yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with oc-yang:dotted-quad""",
          'defined-type': "oc-yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)

  as_ = __builtin__.property(_get_as_, _set_as_)
  router_id = __builtin__.property(_get_router_id, _set_router_id)


  _pyangbind_elements = OrderedDict([('as_', as_), ('router_id', router_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the global BGP router
  """
  __slots__ = ('_path_helper', '_extmethods', '__as_','__router_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'config']

  def _get_as_(self):
    """
    Getter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/as (oc-inet:as-number)

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    return self.__as_
      
  def _set_as_(self, v, load=False):
    """
    Setter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/as (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_() directly.

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_ must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)""",
        })

    self.__as_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_(self):
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)


  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/router_id (oc-yang:dotted-quad)

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/router_id (oc-yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with oc-yang:dotted-quad""",
          'defined-type': "oc-yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)

  as_ = __builtin__.property(_get_as_, _set_as_)
  router_id = __builtin__.property(_get_router_id, _set_router_id)


  _pyangbind_elements = OrderedDict([('as_', as_), ('router_id', router_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the global BGP router
  """
  __slots__ = ('_path_helper', '_extmethods', '__as_','__router_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'config']

  def _get_as_(self):
    """
    Getter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/as (oc-inet:as-number)

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    return self.__as_
      
  def _set_as_(self, v, load=False):
    """
    Setter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/as (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_() directly.

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_ must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)""",
        })

    self.__as_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_(self):
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)


  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/router_id (oc-yang:dotted-quad)

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/router_id (oc-yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with oc-yang:dotted-quad""",
          'defined-type': "oc-yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)

  as_ = __builtin__.property(_get_as_, _set_as_)
  router_id = __builtin__.property(_get_router_id, _set_router_id)


  _pyangbind_elements = OrderedDict([('as_', as_), ('router_id', router_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the global BGP router
  """
  __slots__ = ('_path_helper', '_extmethods', '__as_','__router_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'config']

  def _get_as_(self):
    """
    Getter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/as (oc-inet:as-number)

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    return self.__as_
      
  def _set_as_(self, v, load=False):
    """
    Setter method for as_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/as (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_() directly.

    YANG Description: Local autonomous system number of the router.  Uses
the 32-bit as-number type from the model in RFC 6991.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_ must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)""",
        })

    self.__as_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_(self):
    self.__as_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=True)


  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/router_id (oc-yang:dotted-quad)

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/config/router_id (oc-yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: Router id of the router - an unsigned 32-bit integer
expressed in dotted quad notation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with oc-yang:dotted-quad""",
          'defined-type': "oc-yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:dotted-quad', is_config=True)

  as_ = __builtin__.property(_get_as_, _set_as_)
  router_id = __builtin__.property(_get_router_id, _set_router_id)


  _pyangbind_elements = OrderedDict([('as_', as_), ('router_id', router_id), ])


