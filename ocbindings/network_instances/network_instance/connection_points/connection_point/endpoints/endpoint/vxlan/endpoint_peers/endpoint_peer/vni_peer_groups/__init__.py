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
from . import vni_peer_group
class vni_peer_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/vxlan/endpoint-peers/endpoint-peer/vni-peer-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for associating ingress and egress VNIs to router MACs
  """
  __slots__ = ('_path_helper', '_extmethods', '__vni_peer_group',)

  _yang_name = 'vni-peer-groups'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vni_peer_group = YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints', 'endpoint', 'vxlan', 'endpoint-peers', 'endpoint-peer', 'vni-peer-groups']

  def _get_vni_peer_group(self):
    """
    Getter method for vni_peer_group, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/endpoint_peers/endpoint_peer/vni_peer_groups/vni_peer_group (list)

    YANG Description: List of VNI peer groups
    """
    return self.__vni_peer_group
      
  def _set_vni_peer_group(self, v, load=False):
    """
    Setter method for vni_peer_group, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/endpoint_peers/endpoint_peer/vni_peer_groups/vni_peer_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vni_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vni_peer_group() directly.

    YANG Description: List of VNI peer groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vni_peer_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__vni_peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vni_peer_group(self):
    self.__vni_peer_group = YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  vni_peer_group = __builtin__.property(_get_vni_peer_group)


  _pyangbind_elements = OrderedDict([('vni_peer_group', vni_peer_group), ])


from . import vni_peer_group
class vni_peer_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/vxlan/endpoint-peers/endpoint-peer/vni-peer-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for associating ingress and egress VNIs to router MACs
  """
  __slots__ = ('_path_helper', '_extmethods', '__vni_peer_group',)

  _yang_name = 'vni-peer-groups'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vni_peer_group = YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints', 'endpoint', 'vxlan', 'endpoint-peers', 'endpoint-peer', 'vni-peer-groups']

  def _get_vni_peer_group(self):
    """
    Getter method for vni_peer_group, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/endpoint_peers/endpoint_peer/vni_peer_groups/vni_peer_group (list)

    YANG Description: List of VNI peer groups
    """
    return self.__vni_peer_group
      
  def _set_vni_peer_group(self, v, load=False):
    """
    Setter method for vni_peer_group, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/endpoint_peers/endpoint_peer/vni_peer_groups/vni_peer_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vni_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vni_peer_group() directly.

    YANG Description: List of VNI peer groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vni_peer_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__vni_peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vni_peer_group(self):
    self.__vni_peer_group = YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  vni_peer_group = __builtin__.property(_get_vni_peer_group)


  _pyangbind_elements = OrderedDict([('vni_peer_group', vni_peer_group), ])


from . import vni_peer_group
class vni_peer_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/vxlan/endpoint-peers/endpoint-peer/vni-peer-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for associating ingress and egress VNIs to router MACs
  """
  __slots__ = ('_path_helper', '_extmethods', '__vni_peer_group',)

  _yang_name = 'vni-peer-groups'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vni_peer_group = YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints', 'endpoint', 'vxlan', 'endpoint-peers', 'endpoint-peer', 'vni-peer-groups']

  def _get_vni_peer_group(self):
    """
    Getter method for vni_peer_group, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/endpoint_peers/endpoint_peer/vni_peer_groups/vni_peer_group (list)

    YANG Description: List of VNI peer groups
    """
    return self.__vni_peer_group
      
  def _set_vni_peer_group(self, v, load=False):
    """
    Setter method for vni_peer_group, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/endpoint_peers/endpoint_peer/vni_peer_groups/vni_peer_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vni_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vni_peer_group() directly.

    YANG Description: List of VNI peer groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vni_peer_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__vni_peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vni_peer_group(self):
    self.__vni_peer_group = YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  vni_peer_group = __builtin__.property(_get_vni_peer_group)


  _pyangbind_elements = OrderedDict([('vni_peer_group', vni_peer_group), ])


from . import vni_peer_group
class vni_peer_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/vxlan/endpoint-peers/endpoint-peer/vni-peer-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for associating ingress and egress VNIs to router MACs
  """
  __slots__ = ('_path_helper', '_extmethods', '__vni_peer_group',)

  _yang_name = 'vni-peer-groups'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vni_peer_group = YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints', 'endpoint', 'vxlan', 'endpoint-peers', 'endpoint-peer', 'vni-peer-groups']

  def _get_vni_peer_group(self):
    """
    Getter method for vni_peer_group, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/endpoint_peers/endpoint_peer/vni_peer_groups/vni_peer_group (list)

    YANG Description: List of VNI peer groups
    """
    return self.__vni_peer_group
      
  def _set_vni_peer_group(self, v, load=False):
    """
    Setter method for vni_peer_group, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/vxlan/endpoint_peers/endpoint_peer/vni_peer_groups/vni_peer_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vni_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vni_peer_group() directly.

    YANG Description: List of VNI peer groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vni_peer_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__vni_peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vni_peer_group(self):
    self.__vni_peer_group = YANGDynClass(base=YANGListType("cp_vni egress_vni",vni_peer_group.vni_peer_group, yang_name="vni-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cp-vni egress-vni', extensions=None), is_container='list', yang_name="vni-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  vni_peer_group = __builtin__.property(_get_vni_peer_group)


  _pyangbind_elements = OrderedDict([('vni_peer_group', vni_peer_group), ])


