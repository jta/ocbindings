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
  from YANG module openconfig-keychain - based on the path /keychains/keychain/keys/key/send-lifetime/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for key send lifetime.
  """
  __slots__ = ('_path_helper', '_extmethods', '__start_time','__end_time','__send_and_receive',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/oc-keychain'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__start_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)
    self.__end_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="end-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)
    self.__send_and_receive = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="send-and-receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='boolean', is_config=True)

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
      return ['keychains', 'keychain', 'keys', 'key', 'send-lifetime', 'config']

  def _get_start_time(self):
    """
    Getter method for start_time, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/start_time (oc-types:timeticks64)

    YANG Description: The time at which the key becomes valid for use.
The value is the timestamp in nanoseconds relative to
the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    return self.__start_time
      
  def _set_start_time(self, v, load=False):
    """
    Setter method for start_time, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/start_time (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_time() directly.

    YANG Description: The time at which the key becomes valid for use.
The value is the timestamp in nanoseconds relative to
the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_time must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)""",
        })

    self.__start_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_time(self):
    self.__start_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)


  def _get_end_time(self):
    """
    Getter method for end_time, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/end_time (oc-types:timeticks64)

    YANG Description: The time at which the key becomes invalid for use.
The value is the timestamp in nanoseconds relative to
the Unix Epoch (Jan 1, 1970 00:00:00 UTC).

Leaving this value unset, or setting it to 0, indicates that
the key remains valid forever (no end time).
    """
    return self.__end_time
      
  def _set_end_time(self, v, load=False):
    """
    Setter method for end_time, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/end_time (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_end_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_end_time() directly.

    YANG Description: The time at which the key becomes invalid for use.
The value is the timestamp in nanoseconds relative to
the Unix Epoch (Jan 1, 1970 00:00:00 UTC).

Leaving this value unset, or setting it to 0, indicates that
the key remains valid forever (no end time).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="end-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """end_time must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="end-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)""",
        })

    self.__end_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_end_time(self):
    self.__end_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="end-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)


  def _get_send_and_receive(self):
    """
    Getter method for send_and_receive, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/send_and_receive (boolean)

    YANG Description: When this is set to true (the default value), the specified
send lifetime is also used in the receive direction.  When set
to false, the device should use the specified receive-lifetime
for the receive direction (asymmetric mode).  If send-and-receive
is false, and the device does not support asymmetric configuration,
the config should be rejected as unsupported.
    """
    return self.__send_and_receive
      
  def _set_send_and_receive(self, v, load=False):
    """
    Setter method for send_and_receive, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/send_and_receive (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_and_receive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_and_receive() directly.

    YANG Description: When this is set to true (the default value), the specified
send lifetime is also used in the receive direction.  When set
to false, the device should use the specified receive-lifetime
for the receive direction (asymmetric mode).  If send-and-receive
is false, and the device does not support asymmetric configuration,
the config should be rejected as unsupported.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="send-and-receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_and_receive must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="send-and-receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='boolean', is_config=True)""",
        })

    self.__send_and_receive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_and_receive(self):
    self.__send_and_receive = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="send-and-receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='boolean', is_config=True)

  start_time = __builtin__.property(_get_start_time, _set_start_time)
  end_time = __builtin__.property(_get_end_time, _set_end_time)
  send_and_receive = __builtin__.property(_get_send_and_receive, _set_send_and_receive)


  _pyangbind_elements = OrderedDict([('start_time', start_time), ('end_time', end_time), ('send_and_receive', send_and_receive), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-keychain - based on the path /keychains/keychain/keys/key/send-lifetime/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for key send lifetime.
  """
  __slots__ = ('_path_helper', '_extmethods', '__start_time','__end_time','__send_and_receive',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/oc-keychain'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__start_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)
    self.__end_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="end-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)
    self.__send_and_receive = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="send-and-receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='boolean', is_config=True)

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
      return ['keychains', 'keychain', 'keys', 'key', 'send-lifetime', 'config']

  def _get_start_time(self):
    """
    Getter method for start_time, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/start_time (oc-types:timeticks64)

    YANG Description: The time at which the key becomes valid for use.
The value is the timestamp in nanoseconds relative to
the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    return self.__start_time
      
  def _set_start_time(self, v, load=False):
    """
    Setter method for start_time, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/start_time (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_time() directly.

    YANG Description: The time at which the key becomes valid for use.
The value is the timestamp in nanoseconds relative to
the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_time must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)""",
        })

    self.__start_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_time(self):
    self.__start_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="start-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)


  def _get_end_time(self):
    """
    Getter method for end_time, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/end_time (oc-types:timeticks64)

    YANG Description: The time at which the key becomes invalid for use.
The value is the timestamp in nanoseconds relative to
the Unix Epoch (Jan 1, 1970 00:00:00 UTC).

Leaving this value unset, or setting it to 0, indicates that
the key remains valid forever (no end time).
    """
    return self.__end_time
      
  def _set_end_time(self, v, load=False):
    """
    Setter method for end_time, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/end_time (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_end_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_end_time() directly.

    YANG Description: The time at which the key becomes invalid for use.
The value is the timestamp in nanoseconds relative to
the Unix Epoch (Jan 1, 1970 00:00:00 UTC).

Leaving this value unset, or setting it to 0, indicates that
the key remains valid forever (no end time).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="end-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """end_time must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="end-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)""",
        })

    self.__end_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_end_time(self):
    self.__end_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="end-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='oc-types:timeticks64', is_config=True)


  def _get_send_and_receive(self):
    """
    Getter method for send_and_receive, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/send_and_receive (boolean)

    YANG Description: When this is set to true (the default value), the specified
send lifetime is also used in the receive direction.  When set
to false, the device should use the specified receive-lifetime
for the receive direction (asymmetric mode).  If send-and-receive
is false, and the device does not support asymmetric configuration,
the config should be rejected as unsupported.
    """
    return self.__send_and_receive
      
  def _set_send_and_receive(self, v, load=False):
    """
    Setter method for send_and_receive, mapped from YANG variable /keychains/keychain/keys/key/send_lifetime/config/send_and_receive (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_and_receive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_and_receive() directly.

    YANG Description: When this is set to true (the default value), the specified
send lifetime is also used in the receive direction.  When set
to false, the device should use the specified receive-lifetime
for the receive direction (asymmetric mode).  If send-and-receive
is false, and the device does not support asymmetric configuration,
the config should be rejected as unsupported.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="send-and-receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_and_receive must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="send-and-receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='boolean', is_config=True)""",
        })

    self.__send_and_receive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_and_receive(self):
    self.__send_and_receive = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="send-and-receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='boolean', is_config=True)

  start_time = __builtin__.property(_get_start_time, _set_start_time)
  end_time = __builtin__.property(_get_end_time, _set_end_time)
  send_and_receive = __builtin__.property(_get_send_and_receive, _set_send_and_receive)


  _pyangbind_elements = OrderedDict([('start_time', start_time), ('end_time', end_time), ('send_and_receive', send_and_receive), ])


