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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/ssids/ssid/dot1x-timers/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for dot1x state elements.
  """
  __slots__ = ('_path_helper', '_extmethods', '__max_auth_failures','__blacklist_time',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__max_auth_failures = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="max-auth-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint8', is_config=False)
    self.__blacklist_time = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="blacklist-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)

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
      return ['access-points', 'access-point', 'ssids', 'ssid', 'dot1x-timers', 'state']

  def _get_max_auth_failures(self):
    """
    Getter method for max_auth_failures, mapped from YANG variable /access_points/access_point/ssids/ssid/dot1x_timers/state/max_auth_failures (uint8)

    YANG Description: Number of consecutive authentication failures,
via RADIUS Access-Reject, before Station
is blacklisted.
    """
    return self.__max_auth_failures
      
  def _set_max_auth_failures(self, v, load=False):
    """
    Setter method for max_auth_failures, mapped from YANG variable /access_points/access_point/ssids/ssid/dot1x_timers/state/max_auth_failures (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_auth_failures is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_auth_failures() directly.

    YANG Description: Number of consecutive authentication failures,
via RADIUS Access-Reject, before Station
is blacklisted.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="max-auth-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_auth_failures must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="max-auth-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint8', is_config=False)""",
        })

    self.__max_auth_failures = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_auth_failures(self):
    self.__max_auth_failures = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="max-auth-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint8', is_config=False)


  def _get_blacklist_time(self):
    """
    Getter method for blacklist_time, mapped from YANG variable /access_points/access_point/ssids/ssid/dot1x_timers/state/blacklist_time (uint16)

    YANG Description: Length of time, in seconds, a Station will be
blacklisted as a result of max-auth-failures.
    """
    return self.__blacklist_time
      
  def _set_blacklist_time(self, v, load=False):
    """
    Setter method for blacklist_time, mapped from YANG variable /access_points/access_point/ssids/ssid/dot1x_timers/state/blacklist_time (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blacklist_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blacklist_time() directly.

    YANG Description: Length of time, in seconds, a Station will be
blacklisted as a result of max-auth-failures.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="blacklist-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blacklist_time must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="blacklist-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)""",
        })

    self.__blacklist_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blacklist_time(self):
    self.__blacklist_time = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="blacklist-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)

  max_auth_failures = __builtin__.property(_get_max_auth_failures)
  blacklist_time = __builtin__.property(_get_blacklist_time)


  _pyangbind_elements = OrderedDict([('max_auth_failures', max_auth_failures), ('blacklist_time', blacklist_time), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/ssids/ssid/dot1x-timers/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for dot1x state elements.
  """
  __slots__ = ('_path_helper', '_extmethods', '__max_auth_failures','__blacklist_time',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__max_auth_failures = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="max-auth-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint8', is_config=False)
    self.__blacklist_time = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="blacklist-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)

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
      return ['access-points', 'access-point', 'ssids', 'ssid', 'dot1x-timers', 'state']

  def _get_max_auth_failures(self):
    """
    Getter method for max_auth_failures, mapped from YANG variable /access_points/access_point/ssids/ssid/dot1x_timers/state/max_auth_failures (uint8)

    YANG Description: Number of consecutive authentication failures,
via RADIUS Access-Reject, before Station
is blacklisted.
    """
    return self.__max_auth_failures
      
  def _set_max_auth_failures(self, v, load=False):
    """
    Setter method for max_auth_failures, mapped from YANG variable /access_points/access_point/ssids/ssid/dot1x_timers/state/max_auth_failures (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_auth_failures is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_auth_failures() directly.

    YANG Description: Number of consecutive authentication failures,
via RADIUS Access-Reject, before Station
is blacklisted.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="max-auth-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_auth_failures must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="max-auth-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint8', is_config=False)""",
        })

    self.__max_auth_failures = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_auth_failures(self):
    self.__max_auth_failures = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="max-auth-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint8', is_config=False)


  def _get_blacklist_time(self):
    """
    Getter method for blacklist_time, mapped from YANG variable /access_points/access_point/ssids/ssid/dot1x_timers/state/blacklist_time (uint16)

    YANG Description: Length of time, in seconds, a Station will be
blacklisted as a result of max-auth-failures.
    """
    return self.__blacklist_time
      
  def _set_blacklist_time(self, v, load=False):
    """
    Setter method for blacklist_time, mapped from YANG variable /access_points/access_point/ssids/ssid/dot1x_timers/state/blacklist_time (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blacklist_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blacklist_time() directly.

    YANG Description: Length of time, in seconds, a Station will be
blacklisted as a result of max-auth-failures.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="blacklist-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blacklist_time must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="blacklist-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)""",
        })

    self.__blacklist_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blacklist_time(self):
    self.__blacklist_time = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="blacklist-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)

  max_auth_failures = __builtin__.property(_get_max_auth_failures)
  blacklist_time = __builtin__.property(_get_blacklist_time)


  _pyangbind_elements = OrderedDict([('max_auth_failures', max_auth_failures), ('blacklist_time', blacklist_time), ])


