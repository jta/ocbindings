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
  from YANG module openconfig-telemetry - based on the path /telemetry-system/subscriptions/persistent-subscriptions/persistent-subscription/sensor-profiles/sensor-profile/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the sensor profile
for a subscription
  """
  __slots__ = ('_path_helper', '_extmethods', '__sensor_group','__sample_interval','__heartbeat_interval','__suppress_redundant',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/telemetry'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sensor_group = YANGDynClass(base=str, is_leaf=True, yang_name="sensor-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=False)
    self.__sample_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sample-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)
    self.__heartbeat_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="heartbeat-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)
    self.__suppress_redundant = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-redundant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='boolean', is_config=False)

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
      return ['telemetry-system', 'subscriptions', 'persistent-subscriptions', 'persistent-subscription', 'sensor-profiles', 'sensor-profile', 'state']

  def _get_sensor_group(self):
    """
    Getter method for sensor_group, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/sensor_group (leafref)

    YANG Description: Reference to the sensor group which is used in the profile
    """
    return self.__sensor_group
      
  def _set_sensor_group(self, v, load=False):
    """
    Setter method for sensor_group, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/sensor_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sensor_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sensor_group() directly.

    YANG Description: Reference to the sensor group which is used in the profile
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="sensor-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sensor_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="sensor-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=False)""",
        })

    self.__sensor_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sensor_group(self):
    self.__sensor_group = YANGDynClass(base=str, is_leaf=True, yang_name="sensor-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=False)


  def _get_sample_interval(self):
    """
    Getter method for sample_interval, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/sample_interval (uint64)

    YANG Description: Time in milliseconds between the device's sample of a
telemetry data source. For example, setting this to 100
would require the local device to collect the telemetry
data every 100 milliseconds. There can be latency or jitter
in transmitting the data, but the sample must occur at
the specified interval.

The timestamp must reflect the actual time when the data
was sampled, not simply the previous sample timestamp +
sample-interval.

If sample-interval is set to 0, the telemetry sensor
becomes event based. The sensor must then emit data upon
every change of the underlying data source.
    """
    return self.__sample_interval
      
  def _set_sample_interval(self, v, load=False):
    """
    Setter method for sample_interval, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/sample_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sample_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sample_interval() directly.

    YANG Description: Time in milliseconds between the device's sample of a
telemetry data source. For example, setting this to 100
would require the local device to collect the telemetry
data every 100 milliseconds. There can be latency or jitter
in transmitting the data, but the sample must occur at
the specified interval.

The timestamp must reflect the actual time when the data
was sampled, not simply the previous sample timestamp +
sample-interval.

If sample-interval is set to 0, the telemetry sensor
becomes event based. The sensor must then emit data upon
every change of the underlying data source.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sample-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sample_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sample-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)""",
        })

    self.__sample_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sample_interval(self):
    self.__sample_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sample-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)


  def _get_heartbeat_interval(self):
    """
    Getter method for heartbeat_interval, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/heartbeat_interval (uint64)

    YANG Description: Maximum time interval in seconds that may pass
between updates from a device to a telemetry collector.
If this interval expires, but there is no updated data to
send (such as if suppress_updates has been configured), the
device must send a telemetry message to the collector.
    """
    return self.__heartbeat_interval
      
  def _set_heartbeat_interval(self, v, load=False):
    """
    Setter method for heartbeat_interval, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/heartbeat_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_heartbeat_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_heartbeat_interval() directly.

    YANG Description: Maximum time interval in seconds that may pass
between updates from a device to a telemetry collector.
If this interval expires, but there is no updated data to
send (such as if suppress_updates has been configured), the
device must send a telemetry message to the collector.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="heartbeat-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """heartbeat_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="heartbeat-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)""",
        })

    self.__heartbeat_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_heartbeat_interval(self):
    self.__heartbeat_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="heartbeat-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)


  def _get_suppress_redundant(self):
    """
    Getter method for suppress_redundant, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/suppress_redundant (boolean)

    YANG Description: Boolean flag to control suppression of redundant
telemetry updates to the collector platform. If this flag is
set to TRUE, then the collector will only send an update at
the configured interval if a subscribed data value has
changed. Otherwise, the device will not send an update to
the collector until expiration of the heartbeat interval.
    """
    return self.__suppress_redundant
      
  def _set_suppress_redundant(self, v, load=False):
    """
    Setter method for suppress_redundant, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/suppress_redundant (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_redundant is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_redundant() directly.

    YANG Description: Boolean flag to control suppression of redundant
telemetry updates to the collector platform. If this flag is
set to TRUE, then the collector will only send an update at
the configured interval if a subscribed data value has
changed. Otherwise, the device will not send an update to
the collector until expiration of the heartbeat interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="suppress-redundant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_redundant must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-redundant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='boolean', is_config=False)""",
        })

    self.__suppress_redundant = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_redundant(self):
    self.__suppress_redundant = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-redundant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='boolean', is_config=False)

  sensor_group = __builtin__.property(_get_sensor_group)
  sample_interval = __builtin__.property(_get_sample_interval)
  heartbeat_interval = __builtin__.property(_get_heartbeat_interval)
  suppress_redundant = __builtin__.property(_get_suppress_redundant)


  _pyangbind_elements = OrderedDict([('sensor_group', sensor_group), ('sample_interval', sample_interval), ('heartbeat_interval', heartbeat_interval), ('suppress_redundant', suppress_redundant), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/subscriptions/persistent-subscriptions/persistent-subscription/sensor-profiles/sensor-profile/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to the sensor profile
for a subscription
  """
  __slots__ = ('_path_helper', '_extmethods', '__sensor_group','__sample_interval','__heartbeat_interval','__suppress_redundant',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/telemetry'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sensor_group = YANGDynClass(base=str, is_leaf=True, yang_name="sensor-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=False)
    self.__sample_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sample-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)
    self.__heartbeat_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="heartbeat-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)
    self.__suppress_redundant = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-redundant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='boolean', is_config=False)

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
      return ['telemetry-system', 'subscriptions', 'persistent-subscriptions', 'persistent-subscription', 'sensor-profiles', 'sensor-profile', 'state']

  def _get_sensor_group(self):
    """
    Getter method for sensor_group, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/sensor_group (leafref)

    YANG Description: Reference to the sensor group which is used in the profile
    """
    return self.__sensor_group
      
  def _set_sensor_group(self, v, load=False):
    """
    Setter method for sensor_group, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/sensor_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sensor_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sensor_group() directly.

    YANG Description: Reference to the sensor group which is used in the profile
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="sensor-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sensor_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="sensor-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=False)""",
        })

    self.__sensor_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sensor_group(self):
    self.__sensor_group = YANGDynClass(base=str, is_leaf=True, yang_name="sensor-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=False)


  def _get_sample_interval(self):
    """
    Getter method for sample_interval, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/sample_interval (uint64)

    YANG Description: Time in milliseconds between the device's sample of a
telemetry data source. For example, setting this to 100
would require the local device to collect the telemetry
data every 100 milliseconds. There can be latency or jitter
in transmitting the data, but the sample must occur at
the specified interval.

The timestamp must reflect the actual time when the data
was sampled, not simply the previous sample timestamp +
sample-interval.

If sample-interval is set to 0, the telemetry sensor
becomes event based. The sensor must then emit data upon
every change of the underlying data source.
    """
    return self.__sample_interval
      
  def _set_sample_interval(self, v, load=False):
    """
    Setter method for sample_interval, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/sample_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sample_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sample_interval() directly.

    YANG Description: Time in milliseconds between the device's sample of a
telemetry data source. For example, setting this to 100
would require the local device to collect the telemetry
data every 100 milliseconds. There can be latency or jitter
in transmitting the data, but the sample must occur at
the specified interval.

The timestamp must reflect the actual time when the data
was sampled, not simply the previous sample timestamp +
sample-interval.

If sample-interval is set to 0, the telemetry sensor
becomes event based. The sensor must then emit data upon
every change of the underlying data source.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sample-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sample_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sample-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)""",
        })

    self.__sample_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sample_interval(self):
    self.__sample_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sample-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)


  def _get_heartbeat_interval(self):
    """
    Getter method for heartbeat_interval, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/heartbeat_interval (uint64)

    YANG Description: Maximum time interval in seconds that may pass
between updates from a device to a telemetry collector.
If this interval expires, but there is no updated data to
send (such as if suppress_updates has been configured), the
device must send a telemetry message to the collector.
    """
    return self.__heartbeat_interval
      
  def _set_heartbeat_interval(self, v, load=False):
    """
    Setter method for heartbeat_interval, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/heartbeat_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_heartbeat_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_heartbeat_interval() directly.

    YANG Description: Maximum time interval in seconds that may pass
between updates from a device to a telemetry collector.
If this interval expires, but there is no updated data to
send (such as if suppress_updates has been configured), the
device must send a telemetry message to the collector.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="heartbeat-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """heartbeat_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="heartbeat-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)""",
        })

    self.__heartbeat_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_heartbeat_interval(self):
    self.__heartbeat_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="heartbeat-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='uint64', is_config=False)


  def _get_suppress_redundant(self):
    """
    Getter method for suppress_redundant, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/suppress_redundant (boolean)

    YANG Description: Boolean flag to control suppression of redundant
telemetry updates to the collector platform. If this flag is
set to TRUE, then the collector will only send an update at
the configured interval if a subscribed data value has
changed. Otherwise, the device will not send an update to
the collector until expiration of the heartbeat interval.
    """
    return self.__suppress_redundant
      
  def _set_suppress_redundant(self, v, load=False):
    """
    Setter method for suppress_redundant, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile/state/suppress_redundant (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_redundant is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_redundant() directly.

    YANG Description: Boolean flag to control suppression of redundant
telemetry updates to the collector platform. If this flag is
set to TRUE, then the collector will only send an update at
the configured interval if a subscribed data value has
changed. Otherwise, the device will not send an update to
the collector until expiration of the heartbeat interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="suppress-redundant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_redundant must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-redundant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='boolean', is_config=False)""",
        })

    self.__suppress_redundant = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_redundant(self):
    self.__suppress_redundant = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-redundant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='boolean', is_config=False)

  sensor_group = __builtin__.property(_get_sensor_group)
  sample_interval = __builtin__.property(_get_sample_interval)
  heartbeat_interval = __builtin__.property(_get_heartbeat_interval)
  suppress_redundant = __builtin__.property(_get_suppress_redundant)


  _pyangbind_elements = OrderedDict([('sensor_group', sensor_group), ('sample_interval', sample_interval), ('heartbeat_interval', heartbeat_interval), ('suppress_redundant', suppress_redundant), ])


