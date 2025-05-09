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
from . import counters
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-relay-agent - based on the path /relay-agent/dhcp/interfaces/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for relay agent interfaces.
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__enable','__helper_address','__counters',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/relay-agent'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='oc-if:interface-id', is_config=False)
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    self.__helper_address = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="helper-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='inet:ip-address', is_config=False)
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='container', is_config=False)

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
      return ['relay-agent', 'dhcp', 'interfaces', 'interface', 'state']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/id (oc-if:interface-id)

    YANG Description: Name of the interface on which relay agent is active
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: Name of the interface on which relay agent is active
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='oc-if:interface-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='oc-if:interface-id', is_config=False)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='oc-if:interface-id', is_config=False)


  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/enable (boolean)

    YANG Description: Enables the relay agent on the referenced interface.
At least one helper address should also be configured
for forwarding requested.
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enables the relay agent on the referenced interface.
At least one helper address should also be configured
for forwarding requested.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)


  def _get_helper_address(self):
    """
    Getter method for helper_address, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/helper_address (inet:ip-address)

    YANG Description: List of IPv4 or IPv6 addresses of DHCP servers to which the
relay agent should forward DHCPv4 requests.  The relay agent is
expected to forward DHCPv4/BOOTP requests to all listed
server addresses when DHCPv4 relaying is enabled globally, or
on the interface.
    """
    return self.__helper_address
      
  def _set_helper_address(self, v, load=False):
    """
    Setter method for helper_address, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/helper_address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_helper_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_helper_address() directly.

    YANG Description: List of IPv4 or IPv6 addresses of DHCP servers to which the
relay agent should forward DHCPv4 requests.  The relay agent is
expected to forward DHCPv4/BOOTP requests to all listed
server addresses when DHCPv4 relaying is enabled globally, or
on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="helper-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """helper_address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="helper-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='inet:ip-address', is_config=False)""",
        })

    self.__helper_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_helper_address(self):
    self.__helper_address = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="helper-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='inet:ip-address', is_config=False)


  def _get_counters(self):
    """
    Getter method for counters, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/counters (container)

    YANG Description: Counters and statistics for relay agent operation.
    """
    return self.__counters
      
  def _set_counters(self, v, load=False):
    """
    Setter method for counters, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counters() directly.

    YANG Description: Counters and statistics for relay agent operation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """counters must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='container', is_config=False)""",
        })

    self.__counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_counters(self):
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='container', is_config=False)

  id = __builtin__.property(_get_id)
  enable = __builtin__.property(_get_enable)
  helper_address = __builtin__.property(_get_helper_address)
  counters = __builtin__.property(_get_counters)


  _pyangbind_elements = OrderedDict([('id', id), ('enable', enable), ('helper_address', helper_address), ('counters', counters), ])


from . import counters
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-relay-agent - based on the path /relay-agent/dhcp/interfaces/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for relay agent interfaces.
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__enable','__helper_address','__counters',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/relay-agent'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='oc-if:interface-id', is_config=False)
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    self.__helper_address = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="helper-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='inet:ip-address', is_config=False)
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='container', is_config=False)

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
      return ['relay-agent', 'dhcp', 'interfaces', 'interface', 'state']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/id (oc-if:interface-id)

    YANG Description: Name of the interface on which relay agent is active
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: Name of the interface on which relay agent is active
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='oc-if:interface-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='oc-if:interface-id', is_config=False)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='oc-if:interface-id', is_config=False)


  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/enable (boolean)

    YANG Description: Enables the relay agent on the referenced interface.
At least one helper address should also be configured
for forwarding requested.
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enables the relay agent on the referenced interface.
At least one helper address should also be configured
for forwarding requested.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)


  def _get_helper_address(self):
    """
    Getter method for helper_address, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/helper_address (inet:ip-address)

    YANG Description: List of IPv4 or IPv6 addresses of DHCP servers to which the
relay agent should forward DHCPv4 requests.  The relay agent is
expected to forward DHCPv4/BOOTP requests to all listed
server addresses when DHCPv4 relaying is enabled globally, or
on the interface.
    """
    return self.__helper_address
      
  def _set_helper_address(self, v, load=False):
    """
    Setter method for helper_address, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/helper_address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_helper_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_helper_address() directly.

    YANG Description: List of IPv4 or IPv6 addresses of DHCP servers to which the
relay agent should forward DHCPv4 requests.  The relay agent is
expected to forward DHCPv4/BOOTP requests to all listed
server addresses when DHCPv4 relaying is enabled globally, or
on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="helper-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """helper_address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="helper-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='inet:ip-address', is_config=False)""",
        })

    self.__helper_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_helper_address(self):
    self.__helper_address = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="helper-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='inet:ip-address', is_config=False)


  def _get_counters(self):
    """
    Getter method for counters, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/counters (container)

    YANG Description: Counters and statistics for relay agent operation.
    """
    return self.__counters
      
  def _set_counters(self, v, load=False):
    """
    Setter method for counters, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/state/counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counters() directly.

    YANG Description: Counters and statistics for relay agent operation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """counters must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='container', is_config=False)""",
        })

    self.__counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_counters(self):
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='container', is_config=False)

  id = __builtin__.property(_get_id)
  enable = __builtin__.property(_get_enable)
  helper_address = __builtin__.property(_get_helper_address)
  counters = __builtin__.property(_get_counters)


  _pyangbind_elements = OrderedDict([('id', id), ('enable', enable), ('helper_address', helper_address), ('counters', counters), ])


