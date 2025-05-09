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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv3/areas/area/virtual-links/virtual-link/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the OSPF virtual link
  """
  __slots__ = ('_path_helper', '_extmethods', '__remote_router_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__remote_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv3', 'areas', 'area', 'virtual-links', 'virtual-link', 'config']

  def _get_remote_router_id(self):
    """
    Getter method for remote_router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv3/areas/area/virtual_links/virtual_link/config/remote_router_id (inet:ipv4-address-no-zone)

    YANG Description: The router ID of the device which terminates the remote end
of the virtual link
    """
    return self.__remote_router_id
      
  def _set_remote_router_id(self, v, load=False):
    """
    Setter method for remote_router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv3/areas/area/virtual_links/virtual_link/config/remote_router_id (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_router_id() directly.

    YANG Description: The router ID of the device which terminates the remote end
of the virtual link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_router_id must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)""",
        })

    self.__remote_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_router_id(self):
    self.__remote_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)

  remote_router_id = __builtin__.property(_get_remote_router_id, _set_remote_router_id)


  _pyangbind_elements = OrderedDict([('remote_router_id', remote_router_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv3/areas/area/virtual-links/virtual-link/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the OSPF virtual link
  """
  __slots__ = ('_path_helper', '_extmethods', '__remote_router_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__remote_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv3', 'areas', 'area', 'virtual-links', 'virtual-link', 'config']

  def _get_remote_router_id(self):
    """
    Getter method for remote_router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv3/areas/area/virtual_links/virtual_link/config/remote_router_id (inet:ipv4-address-no-zone)

    YANG Description: The router ID of the device which terminates the remote end
of the virtual link
    """
    return self.__remote_router_id
      
  def _set_remote_router_id(self, v, load=False):
    """
    Setter method for remote_router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv3/areas/area/virtual_links/virtual_link/config/remote_router_id (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_router_id() directly.

    YANG Description: The router ID of the device which terminates the remote end
of the virtual link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_router_id must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)""",
        })

    self.__remote_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_router_id(self):
    self.__remote_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)

  remote_router_id = __builtin__.property(_get_remote_router_id, _set_remote_router_id)


  _pyangbind_elements = OrderedDict([('remote_router_id', remote_router_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv3/areas/area/virtual-links/virtual-link/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the OSPF virtual link
  """
  __slots__ = ('_path_helper', '_extmethods', '__remote_router_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__remote_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv3', 'areas', 'area', 'virtual-links', 'virtual-link', 'config']

  def _get_remote_router_id(self):
    """
    Getter method for remote_router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv3/areas/area/virtual_links/virtual_link/config/remote_router_id (inet:ipv4-address-no-zone)

    YANG Description: The router ID of the device which terminates the remote end
of the virtual link
    """
    return self.__remote_router_id
      
  def _set_remote_router_id(self, v, load=False):
    """
    Setter method for remote_router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv3/areas/area/virtual_links/virtual_link/config/remote_router_id (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_router_id() directly.

    YANG Description: The router ID of the device which terminates the remote end
of the virtual link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_router_id must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)""",
        })

    self.__remote_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_router_id(self):
    self.__remote_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)

  remote_router_id = __builtin__.property(_get_remote_router_id, _set_remote_router_id)


  _pyangbind_elements = OrderedDict([('remote_router_id', remote_router_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv3/areas/area/virtual-links/virtual-link/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the OSPF virtual link
  """
  __slots__ = ('_path_helper', '_extmethods', '__remote_router_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__remote_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv3', 'areas', 'area', 'virtual-links', 'virtual-link', 'config']

  def _get_remote_router_id(self):
    """
    Getter method for remote_router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv3/areas/area/virtual_links/virtual_link/config/remote_router_id (inet:ipv4-address-no-zone)

    YANG Description: The router ID of the device which terminates the remote end
of the virtual link
    """
    return self.__remote_router_id
      
  def _set_remote_router_id(self, v, load=False):
    """
    Setter method for remote_router_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv3/areas/area/virtual_links/virtual_link/config/remote_router_id (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_router_id() directly.

    YANG Description: The router ID of the device which terminates the remote end
of the virtual link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_router_id must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)""",
        })

    self.__remote_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_router_id(self):
    self.__remote_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="remote-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=True)

  remote_router_id = __builtin__.property(_get_remote_router_id, _set_remote_router_id)


  _pyangbind_elements = OrderedDict([('remote_router_id', remote_router_id), ])


