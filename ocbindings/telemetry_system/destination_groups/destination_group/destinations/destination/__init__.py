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
from . import config
from . import state
class destination(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/destination-groups/destination-group/destinations/destination. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of telemetry stream destinations
  """
  __slots__ = ('_path_helper', '_extmethods', '__destination_address','__destination_port','__config','__state',)

  _yang_name = 'destination'
  _yang_namespace = 'http://openconfig.net/yang/telemetry'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__destination_address = YANGDynClass(base=str, is_leaf=True, yang_name="destination-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    self.__destination_port = YANGDynClass(base=str, is_leaf=True, yang_name="destination-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)

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
      return ['telemetry-system', 'destination-groups', 'destination-group', 'destinations', 'destination']

  def _get_destination_address(self):
    """
    Getter method for destination_address, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/destination_address (leafref)

    YANG Description: Reference to the destination address of the
telemetry stream
    """
    return self.__destination_address
      
  def _set_destination_address(self, v, load=False):
    """
    Setter method for destination_address, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/destination_address (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_address() directly.

    YANG Description: Reference to the destination address of the
telemetry stream
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="destination-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_address must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="destination-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)""",
        })

    self.__destination_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_address(self):
    self.__destination_address = YANGDynClass(base=str, is_leaf=True, yang_name="destination-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)


  def _get_destination_port(self):
    """
    Getter method for destination_port, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/destination_port (leafref)

    YANG Description: Reference to the port number of the stream
destination
    """
    return self.__destination_port
      
  def _set_destination_port(self, v, load=False):
    """
    Setter method for destination_port, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/destination_port (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_port() directly.

    YANG Description: Reference to the port number of the stream
destination
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="destination-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_port must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="destination-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)""",
        })

    self.__destination_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_port(self):
    self.__destination_port = YANGDynClass(base=str, is_leaf=True, yang_name="destination-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/config (container)

    YANG Description: Configuration parameters relating to
telemetry destinations
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to
telemetry destinations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/state (container)

    YANG Description: State information associated with
telemetry destinations
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State information associated with
telemetry destinations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)

  destination_address = __builtin__.property(_get_destination_address, _set_destination_address)
  destination_port = __builtin__.property(_get_destination_port, _set_destination_port)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('destination_address', destination_address), ('destination_port', destination_port), ('config', config), ('state', state), ])


from . import config
from . import state
class destination(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/destination-groups/destination-group/destinations/destination. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of telemetry stream destinations
  """
  __slots__ = ('_path_helper', '_extmethods', '__destination_address','__destination_port','__config','__state',)

  _yang_name = 'destination'
  _yang_namespace = 'http://openconfig.net/yang/telemetry'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__destination_address = YANGDynClass(base=str, is_leaf=True, yang_name="destination-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    self.__destination_port = YANGDynClass(base=str, is_leaf=True, yang_name="destination-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)

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
      return ['telemetry-system', 'destination-groups', 'destination-group', 'destinations', 'destination']

  def _get_destination_address(self):
    """
    Getter method for destination_address, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/destination_address (leafref)

    YANG Description: Reference to the destination address of the
telemetry stream
    """
    return self.__destination_address
      
  def _set_destination_address(self, v, load=False):
    """
    Setter method for destination_address, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/destination_address (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_address() directly.

    YANG Description: Reference to the destination address of the
telemetry stream
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="destination-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_address must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="destination-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)""",
        })

    self.__destination_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_address(self):
    self.__destination_address = YANGDynClass(base=str, is_leaf=True, yang_name="destination-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)


  def _get_destination_port(self):
    """
    Getter method for destination_port, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/destination_port (leafref)

    YANG Description: Reference to the port number of the stream
destination
    """
    return self.__destination_port
      
  def _set_destination_port(self, v, load=False):
    """
    Setter method for destination_port, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/destination_port (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_port() directly.

    YANG Description: Reference to the port number of the stream
destination
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="destination-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_port must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="destination-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)""",
        })

    self.__destination_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_port(self):
    self.__destination_port = YANGDynClass(base=str, is_leaf=True, yang_name="destination-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/config (container)

    YANG Description: Configuration parameters relating to
telemetry destinations
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to
telemetry destinations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/state (container)

    YANG Description: State information associated with
telemetry destinations
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations/destination/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State information associated with
telemetry destinations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)

  destination_address = __builtin__.property(_get_destination_address, _set_destination_address)
  destination_port = __builtin__.property(_get_destination_port, _set_destination_port)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('destination_address', destination_address), ('destination_port', destination_port), ('config', config), ('state', state), ])


