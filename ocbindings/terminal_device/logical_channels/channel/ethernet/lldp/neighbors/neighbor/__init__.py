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
from . import state
from . import custom_tlvs
class neighbor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device - based on the path /terminal-device/logical-channels/channel/ethernet/lldp/neighbors/neighbor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of LLDP neighbors. If the implementation only
supports one neighbor, this would always be a list with
one item. If the device and neighbor supported multiple
neighbors, which can be achieved via LLDP forwarding, then
this would be supported
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__state','__custom_tlvs',)

  _yang_name = 'neighbor'
  _yang_namespace = 'http://openconfig.net/yang/terminal-device'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)
    self.__custom_tlvs = YANGDynClass(base=custom_tlvs.custom_tlvs, is_container='container', yang_name="custom-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)

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
      return ['terminal-device', 'logical-channels', 'channel', 'ethernet', 'lldp', 'neighbors', 'neighbor']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/id (leafref)

    YANG Description: System generated identifier for the neighbor on
the logical channel.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: System generated identifier for the neighbor on
the logical channel.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/state (container)

    YANG Description: Operational state data 
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)


  def _get_custom_tlvs(self):
    """
    Getter method for custom_tlvs, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/custom_tlvs (container)

    YANG Description: Enclosing container for list of custom TLVs from a
neighbor
    """
    return self.__custom_tlvs
      
  def _set_custom_tlvs(self, v, load=False):
    """
    Setter method for custom_tlvs, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/custom_tlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_custom_tlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_custom_tlvs() directly.

    YANG Description: Enclosing container for list of custom TLVs from a
neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=custom_tlvs.custom_tlvs, is_container='container', yang_name="custom-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """custom_tlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=custom_tlvs.custom_tlvs, is_container='container', yang_name="custom-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)""",
        })

    self.__custom_tlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_custom_tlvs(self):
    self.__custom_tlvs = YANGDynClass(base=custom_tlvs.custom_tlvs, is_container='container', yang_name="custom-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)

  id = __builtin__.property(_get_id)
  state = __builtin__.property(_get_state)
  custom_tlvs = __builtin__.property(_get_custom_tlvs)


  _pyangbind_elements = OrderedDict([('id', id), ('state', state), ('custom_tlvs', custom_tlvs), ])


from . import state
from . import custom_tlvs
class neighbor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device - based on the path /terminal-device/logical-channels/channel/ethernet/lldp/neighbors/neighbor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of LLDP neighbors. If the implementation only
supports one neighbor, this would always be a list with
one item. If the device and neighbor supported multiple
neighbors, which can be achieved via LLDP forwarding, then
this would be supported
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__state','__custom_tlvs',)

  _yang_name = 'neighbor'
  _yang_namespace = 'http://openconfig.net/yang/terminal-device'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)
    self.__custom_tlvs = YANGDynClass(base=custom_tlvs.custom_tlvs, is_container='container', yang_name="custom-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)

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
      return ['terminal-device', 'logical-channels', 'channel', 'ethernet', 'lldp', 'neighbors', 'neighbor']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/id (leafref)

    YANG Description: System generated identifier for the neighbor on
the logical channel.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: System generated identifier for the neighbor on
the logical channel.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/state (container)

    YANG Description: Operational state data 
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)


  def _get_custom_tlvs(self):
    """
    Getter method for custom_tlvs, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/custom_tlvs (container)

    YANG Description: Enclosing container for list of custom TLVs from a
neighbor
    """
    return self.__custom_tlvs
      
  def _set_custom_tlvs(self, v, load=False):
    """
    Setter method for custom_tlvs, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor/custom_tlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_custom_tlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_custom_tlvs() directly.

    YANG Description: Enclosing container for list of custom TLVs from a
neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=custom_tlvs.custom_tlvs, is_container='container', yang_name="custom-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """custom_tlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=custom_tlvs.custom_tlvs, is_container='container', yang_name="custom-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)""",
        })

    self.__custom_tlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_custom_tlvs(self):
    self.__custom_tlvs = YANGDynClass(base=custom_tlvs.custom_tlvs, is_container='container', yang_name="custom-tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='container', is_config=False)

  id = __builtin__.property(_get_id)
  state = __builtin__.property(_get_state)
  custom_tlvs = __builtin__.property(_get_custom_tlvs)


  _pyangbind_elements = OrderedDict([('id', id), ('state', state), ('custom_tlvs', custom_tlvs), ])


