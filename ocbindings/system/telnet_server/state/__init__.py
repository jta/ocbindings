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
  from YANG module openconfig-system - based on the path /system/telnet-server/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for telnet
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable','__timeout','__rate_limit','__session_limit',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=False)
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    self.__rate_limit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rate-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    self.__session_limit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="session-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)

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
      return ['system', 'telnet-server', 'state']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /system/telnet_server/state/enable (boolean)

    YANG Description: Enables the telnet server.  Telnet is disabled by
default
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /system/telnet_server/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enables the telnet server.  Telnet is disabled by
default
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=False)


  def _get_timeout(self):
    """
    Getter method for timeout, mapped from YANG variable /system/telnet_server/state/timeout (uint16)

    YANG Description: Set the idle timeout in seconds on terminal connections to
the system for the protocol.
    """
    return self.__timeout
      
  def _set_timeout(self, v, load=False):
    """
    Setter method for timeout, mapped from YANG variable /system/telnet_server/state/timeout (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeout() directly.

    YANG Description: Set the idle timeout in seconds on terminal connections to
the system for the protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeout must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)""",
        })

    self.__timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeout(self):
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)


  def _get_rate_limit(self):
    """
    Getter method for rate_limit, mapped from YANG variable /system/telnet_server/state/rate_limit (uint16)

    YANG Description: Set a limit on the number of connection attempts per
minute to the system for the protocol.
    """
    return self.__rate_limit
      
  def _set_rate_limit(self, v, load=False):
    """
    Setter method for rate_limit, mapped from YANG variable /system/telnet_server/state/rate_limit (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rate_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rate_limit() directly.

    YANG Description: Set a limit on the number of connection attempts per
minute to the system for the protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rate-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rate_limit must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rate-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)""",
        })

    self.__rate_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rate_limit(self):
    self.__rate_limit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rate-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)


  def _get_session_limit(self):
    """
    Getter method for session_limit, mapped from YANG variable /system/telnet_server/state/session_limit (uint16)

    YANG Description: Set a limit on the number of simultaneous active terminal
sessions to the system for the protocol (e.g., ssh,
telnet, ...) 
    """
    return self.__session_limit
      
  def _set_session_limit(self, v, load=False):
    """
    Setter method for session_limit, mapped from YANG variable /system/telnet_server/state/session_limit (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_session_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_session_limit() directly.

    YANG Description: Set a limit on the number of simultaneous active terminal
sessions to the system for the protocol (e.g., ssh,
telnet, ...) 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="session-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """session_limit must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="session-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)""",
        })

    self.__session_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_session_limit(self):
    self.__session_limit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="session-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)

  enable = __builtin__.property(_get_enable)
  timeout = __builtin__.property(_get_timeout)
  rate_limit = __builtin__.property(_get_rate_limit)
  session_limit = __builtin__.property(_get_session_limit)


  _pyangbind_elements = OrderedDict([('enable', enable), ('timeout', timeout), ('rate_limit', rate_limit), ('session_limit', session_limit), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/telnet-server/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for telnet
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable','__timeout','__rate_limit','__session_limit',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=False)
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    self.__rate_limit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rate-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    self.__session_limit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="session-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)

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
      return ['system', 'telnet-server', 'state']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /system/telnet_server/state/enable (boolean)

    YANG Description: Enables the telnet server.  Telnet is disabled by
default
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /system/telnet_server/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enables the telnet server.  Telnet is disabled by
default
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=False)


  def _get_timeout(self):
    """
    Getter method for timeout, mapped from YANG variable /system/telnet_server/state/timeout (uint16)

    YANG Description: Set the idle timeout in seconds on terminal connections to
the system for the protocol.
    """
    return self.__timeout
      
  def _set_timeout(self, v, load=False):
    """
    Setter method for timeout, mapped from YANG variable /system/telnet_server/state/timeout (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeout() directly.

    YANG Description: Set the idle timeout in seconds on terminal connections to
the system for the protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeout must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)""",
        })

    self.__timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeout(self):
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)


  def _get_rate_limit(self):
    """
    Getter method for rate_limit, mapped from YANG variable /system/telnet_server/state/rate_limit (uint16)

    YANG Description: Set a limit on the number of connection attempts per
minute to the system for the protocol.
    """
    return self.__rate_limit
      
  def _set_rate_limit(self, v, load=False):
    """
    Setter method for rate_limit, mapped from YANG variable /system/telnet_server/state/rate_limit (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rate_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rate_limit() directly.

    YANG Description: Set a limit on the number of connection attempts per
minute to the system for the protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rate-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rate_limit must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rate-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)""",
        })

    self.__rate_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rate_limit(self):
    self.__rate_limit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rate-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)


  def _get_session_limit(self):
    """
    Getter method for session_limit, mapped from YANG variable /system/telnet_server/state/session_limit (uint16)

    YANG Description: Set a limit on the number of simultaneous active terminal
sessions to the system for the protocol (e.g., ssh,
telnet, ...) 
    """
    return self.__session_limit
      
  def _set_session_limit(self, v, load=False):
    """
    Setter method for session_limit, mapped from YANG variable /system/telnet_server/state/session_limit (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_session_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_session_limit() directly.

    YANG Description: Set a limit on the number of simultaneous active terminal
sessions to the system for the protocol (e.g., ssh,
telnet, ...) 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="session-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """session_limit must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="session-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)""",
        })

    self.__session_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_session_limit(self):
    self.__session_limit = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="session-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint16', is_config=False)

  enable = __builtin__.property(_get_enable)
  timeout = __builtin__.property(_get_timeout)
  rate_limit = __builtin__.property(_get_rate_limit)
  session_limit = __builtin__.property(_get_session_limit)


  _pyangbind_elements = OrderedDict([('enable', enable), ('timeout', timeout), ('rate_limit', rate_limit), ('session_limit', session_limit), ])


