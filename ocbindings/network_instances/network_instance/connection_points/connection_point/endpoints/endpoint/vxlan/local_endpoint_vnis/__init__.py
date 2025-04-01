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
from . import local_endpoint_vni
class local_endpoint_vnis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/vxlan/local-endpoint-vnis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for local configuration related to Layer 2 virtual
network identifiers (L2VNIs) and Layer 3 virtual network identifiers
(L3VNIs) in the default network instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__local_endpoint_vni',)

  _yang_name = 'local-endpoint-vnis'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_endpoint_vni = YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints', 'endpoint', 'vxlan', 'local-endpoint-vnis']

  def _get_local_endpoint_vni(self):
    """
    Getter method for local_endpoint_vni, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/local_endpoint_vnis/local_endpoint_vni (list)

    YANG Description: List of L2VNIs and L3VNIs configured on the local VTEP
    """
    return self.__local_endpoint_vni
      
  def _set_local_endpoint_vni(self, v, load=False):
    """
    Setter method for local_endpoint_vni, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/local_endpoint_vnis/local_endpoint_vni (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_endpoint_vni is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_endpoint_vni() directly.

    YANG Description: List of L2VNIs and L3VNIs configured on the local VTEP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_endpoint_vni must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__local_endpoint_vni = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_endpoint_vni(self):
    self.__local_endpoint_vni = YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  local_endpoint_vni = __builtin__.property(_get_local_endpoint_vni, _set_local_endpoint_vni)


  _pyangbind_elements = OrderedDict([('local_endpoint_vni', local_endpoint_vni), ])


from . import local_endpoint_vni
class local_endpoint_vnis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/vxlan/local-endpoint-vnis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for local configuration related to Layer 2 virtual
network identifiers (L2VNIs) and Layer 3 virtual network identifiers
(L3VNIs) in the default network instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__local_endpoint_vni',)

  _yang_name = 'local-endpoint-vnis'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_endpoint_vni = YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints', 'endpoint', 'vxlan', 'local-endpoint-vnis']

  def _get_local_endpoint_vni(self):
    """
    Getter method for local_endpoint_vni, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/local_endpoint_vnis/local_endpoint_vni (list)

    YANG Description: List of L2VNIs and L3VNIs configured on the local VTEP
    """
    return self.__local_endpoint_vni
      
  def _set_local_endpoint_vni(self, v, load=False):
    """
    Setter method for local_endpoint_vni, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/local_endpoint_vnis/local_endpoint_vni (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_endpoint_vni is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_endpoint_vni() directly.

    YANG Description: List of L2VNIs and L3VNIs configured on the local VTEP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_endpoint_vni must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__local_endpoint_vni = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_endpoint_vni(self):
    self.__local_endpoint_vni = YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  local_endpoint_vni = __builtin__.property(_get_local_endpoint_vni, _set_local_endpoint_vni)


  _pyangbind_elements = OrderedDict([('local_endpoint_vni', local_endpoint_vni), ])


from . import local_endpoint_vni
class local_endpoint_vnis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/vxlan/local-endpoint-vnis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for local configuration related to Layer 2 virtual
network identifiers (L2VNIs) and Layer 3 virtual network identifiers
(L3VNIs) in the default network instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__local_endpoint_vni',)

  _yang_name = 'local-endpoint-vnis'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_endpoint_vni = YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints', 'endpoint', 'vxlan', 'local-endpoint-vnis']

  def _get_local_endpoint_vni(self):
    """
    Getter method for local_endpoint_vni, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/local_endpoint_vnis/local_endpoint_vni (list)

    YANG Description: List of L2VNIs and L3VNIs configured on the local VTEP
    """
    return self.__local_endpoint_vni
      
  def _set_local_endpoint_vni(self, v, load=False):
    """
    Setter method for local_endpoint_vni, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/local_endpoint_vnis/local_endpoint_vni (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_endpoint_vni is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_endpoint_vni() directly.

    YANG Description: List of L2VNIs and L3VNIs configured on the local VTEP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_endpoint_vni must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__local_endpoint_vni = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_endpoint_vni(self):
    self.__local_endpoint_vni = YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  local_endpoint_vni = __builtin__.property(_get_local_endpoint_vni, _set_local_endpoint_vni)


  _pyangbind_elements = OrderedDict([('local_endpoint_vni', local_endpoint_vni), ])


from . import local_endpoint_vni
class local_endpoint_vnis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/vxlan/local-endpoint-vnis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for local configuration related to Layer 2 virtual
network identifiers (L2VNIs) and Layer 3 virtual network identifiers
(L3VNIs) in the default network instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__local_endpoint_vni',)

  _yang_name = 'local-endpoint-vnis'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_endpoint_vni = YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints', 'endpoint', 'vxlan', 'local-endpoint-vnis']

  def _get_local_endpoint_vni(self):
    """
    Getter method for local_endpoint_vni, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/local_endpoint_vnis/local_endpoint_vni (list)

    YANG Description: List of L2VNIs and L3VNIs configured on the local VTEP
    """
    return self.__local_endpoint_vni
      
  def _set_local_endpoint_vni(self, v, load=False):
    """
    Setter method for local_endpoint_vni, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/local_endpoint_vnis/local_endpoint_vni (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_endpoint_vni is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_endpoint_vni() directly.

    YANG Description: List of L2VNIs and L3VNIs configured on the local VTEP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_endpoint_vni must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__local_endpoint_vni = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_endpoint_vni(self):
    self.__local_endpoint_vni = YANGDynClass(base=YANGListType("vni",local_endpoint_vni.local_endpoint_vni, yang_name="local-endpoint-vni", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni', extensions=None), is_container='list', yang_name="local-endpoint-vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  local_endpoint_vni = __builtin__.property(_get_local_endpoint_vni, _set_local_endpoint_vni)


  _pyangbind_elements = OrderedDict([('local_endpoint_vni', local_endpoint_vni), ])


