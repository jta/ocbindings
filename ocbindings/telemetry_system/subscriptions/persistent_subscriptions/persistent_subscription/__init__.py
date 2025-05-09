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
from . import sensor_profiles
from . import destination_groups
class persistent_subscription(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/subscriptions/persistent-subscriptions/persistent-subscription. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of telemetry subscriptions. A telemetry
subscription consists of a set of collection
destinations, stream attributes, and associated paths to
state information in the model (sensor data)
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__config','__state','__sensor_profiles','__destination_groups',)

  _yang_name = 'persistent-subscription'
  _yang_namespace = 'http://openconfig.net/yang/telemetry'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)
    self.__sensor_profiles = YANGDynClass(base=sensor_profiles.sensor_profiles, is_container='container', yang_name="sensor-profiles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__destination_groups = YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

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
      return ['telemetry-system', 'subscriptions', 'persistent-subscriptions', 'persistent-subscription']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/name (leafref)

    YANG Description: Reference to the identifier of the subscription
itself. The id will be the handle to refer to the
subscription once created
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference to the identifier of the subscription
itself. The id will be the handle to refer to the
subscription once created
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/config (container)

    YANG Description: Config parameters relating to the telemetry
subscriptions on the local device
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Config parameters relating to the telemetry
subscriptions on the local device
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
    Getter method for state, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/state (container)

    YANG Description: State parameters relating to the telemetry
subscriptions on the local device
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters relating to the telemetry
subscriptions on the local device
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


  def _get_sensor_profiles(self):
    """
    Getter method for sensor_profiles, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles (container)

    YANG Description: A sensor profile is a set of sensor groups or
individual sensor paths which are associated with a
telemetry subscription. This is the source of the
telemetry data for the subscription to send to the
defined collectors.
    """
    return self.__sensor_profiles
      
  def _set_sensor_profiles(self, v, load=False):
    """
    Setter method for sensor_profiles, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sensor_profiles is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sensor_profiles() directly.

    YANG Description: A sensor profile is a set of sensor groups or
individual sensor paths which are associated with a
telemetry subscription. This is the source of the
telemetry data for the subscription to send to the
defined collectors.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sensor_profiles.sensor_profiles, is_container='container', yang_name="sensor-profiles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sensor_profiles must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sensor_profiles.sensor_profiles, is_container='container', yang_name="sensor-profiles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__sensor_profiles = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sensor_profiles(self):
    self.__sensor_profiles = YANGDynClass(base=sensor_profiles.sensor_profiles, is_container='container', yang_name="sensor-profiles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_destination_groups(self):
    """
    Getter method for destination_groups, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/destination_groups (container)

    YANG Description: A subscription may specify destination addresses.
If the subscription supplies destination addresses,
the network element will be the initiator of the
telemetry streaming, sending it to the destination(s)
specified.

If the destination set is omitted, the subscription
preconfigures certain elements such as paths and
sample intervals under a specified subscription ID.
In this case, the network element will NOT initiate an
outbound connection for telemetry, but will wait for
an inbound connection from a network management
system.

It is expected that the network management system
connecting to the network element will reference
the preconfigured subscription ID when initiating
a subscription.
    """
    return self.__destination_groups
      
  def _set_destination_groups(self, v, load=False):
    """
    Setter method for destination_groups, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/destination_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_groups() directly.

    YANG Description: A subscription may specify destination addresses.
If the subscription supplies destination addresses,
the network element will be the initiator of the
telemetry streaming, sending it to the destination(s)
specified.

If the destination set is omitted, the subscription
preconfigures certain elements such as paths and
sample intervals under a specified subscription ID.
In this case, the network element will NOT initiate an
outbound connection for telemetry, but will wait for
an inbound connection from a network management
system.

It is expected that the network management system
connecting to the network element will reference
the preconfigured subscription ID when initiating
a subscription.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__destination_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_groups(self):
    self.__destination_groups = YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  sensor_profiles = __builtin__.property(_get_sensor_profiles, _set_sensor_profiles)
  destination_groups = __builtin__.property(_get_destination_groups, _set_destination_groups)


  _pyangbind_elements = OrderedDict([('name', name), ('config', config), ('state', state), ('sensor_profiles', sensor_profiles), ('destination_groups', destination_groups), ])


from . import config
from . import state
from . import sensor_profiles
from . import destination_groups
class persistent_subscription(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/subscriptions/persistent-subscriptions/persistent-subscription. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of telemetry subscriptions. A telemetry
subscription consists of a set of collection
destinations, stream attributes, and associated paths to
state information in the model (sensor data)
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__config','__state','__sensor_profiles','__destination_groups',)

  _yang_name = 'persistent-subscription'
  _yang_namespace = 'http://openconfig.net/yang/telemetry'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=False)
    self.__sensor_profiles = YANGDynClass(base=sensor_profiles.sensor_profiles, is_container='container', yang_name="sensor-profiles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__destination_groups = YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

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
      return ['telemetry-system', 'subscriptions', 'persistent-subscriptions', 'persistent-subscription']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/name (leafref)

    YANG Description: Reference to the identifier of the subscription
itself. The id will be the handle to refer to the
subscription once created
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference to the identifier of the subscription
itself. The id will be the handle to refer to the
subscription once created
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/config (container)

    YANG Description: Config parameters relating to the telemetry
subscriptions on the local device
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Config parameters relating to the telemetry
subscriptions on the local device
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
    Getter method for state, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/state (container)

    YANG Description: State parameters relating to the telemetry
subscriptions on the local device
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters relating to the telemetry
subscriptions on the local device
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


  def _get_sensor_profiles(self):
    """
    Getter method for sensor_profiles, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles (container)

    YANG Description: A sensor profile is a set of sensor groups or
individual sensor paths which are associated with a
telemetry subscription. This is the source of the
telemetry data for the subscription to send to the
defined collectors.
    """
    return self.__sensor_profiles
      
  def _set_sensor_profiles(self, v, load=False):
    """
    Setter method for sensor_profiles, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sensor_profiles is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sensor_profiles() directly.

    YANG Description: A sensor profile is a set of sensor groups or
individual sensor paths which are associated with a
telemetry subscription. This is the source of the
telemetry data for the subscription to send to the
defined collectors.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sensor_profiles.sensor_profiles, is_container='container', yang_name="sensor-profiles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sensor_profiles must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sensor_profiles.sensor_profiles, is_container='container', yang_name="sensor-profiles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__sensor_profiles = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sensor_profiles(self):
    self.__sensor_profiles = YANGDynClass(base=sensor_profiles.sensor_profiles, is_container='container', yang_name="sensor-profiles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_destination_groups(self):
    """
    Getter method for destination_groups, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/destination_groups (container)

    YANG Description: A subscription may specify destination addresses.
If the subscription supplies destination addresses,
the network element will be the initiator of the
telemetry streaming, sending it to the destination(s)
specified.

If the destination set is omitted, the subscription
preconfigures certain elements such as paths and
sample intervals under a specified subscription ID.
In this case, the network element will NOT initiate an
outbound connection for telemetry, but will wait for
an inbound connection from a network management
system.

It is expected that the network management system
connecting to the network element will reference
the preconfigured subscription ID when initiating
a subscription.
    """
    return self.__destination_groups
      
  def _set_destination_groups(self, v, load=False):
    """
    Setter method for destination_groups, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/destination_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_groups() directly.

    YANG Description: A subscription may specify destination addresses.
If the subscription supplies destination addresses,
the network element will be the initiator of the
telemetry streaming, sending it to the destination(s)
specified.

If the destination set is omitted, the subscription
preconfigures certain elements such as paths and
sample intervals under a specified subscription ID.
In this case, the network element will NOT initiate an
outbound connection for telemetry, but will wait for
an inbound connection from a network management
system.

It is expected that the network management system
connecting to the network element will reference
the preconfigured subscription ID when initiating
a subscription.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__destination_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_groups(self):
    self.__destination_groups = YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  sensor_profiles = __builtin__.property(_get_sensor_profiles, _set_sensor_profiles)
  destination_groups = __builtin__.property(_get_destination_groups, _set_destination_groups)


  _pyangbind_elements = OrderedDict([('name', name), ('config', config), ('state', state), ('sensor_profiles', sensor_profiles), ('destination_groups', destination_groups), ])


