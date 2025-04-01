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
  from YANG module openconfig-system - based on the path /system/messages/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for Syslog messages.
  """
  __slots__ = ('_path_helper', '_extmethods', '__severity',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-log:syslog-severity', is_config=True)

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
      return ['system', 'messages', 'config']

  def _get_severity(self):
    """
    Getter method for severity, mapped from YANG variable /system/messages/config/severity (oc-log:syslog-severity)

    YANG Description: Specifies that only messages of the given severity (or
greater severity) are sent over the RPC.

This is analogous to differentiating which severity is to be
sent to legacy Syslog servers, as opposed to local buffer or
files.
    """
    return self.__severity
      
  def _set_severity(self, v, load=False):
    """
    Setter method for severity, mapped from YANG variable /system/messages/config/severity (oc-log:syslog-severity)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity() directly.

    YANG Description: Specifies that only messages of the given severity (or
greater severity) are sent over the RPC.

This is analogous to differentiating which severity is to be
sent to legacy Syslog servers, as opposed to local buffer or
files.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-log:syslog-severity', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity must be of a type compatible with oc-log:syslog-severity""",
          'defined-type': "oc-log:syslog-severity",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-log:syslog-severity', is_config=True)""",
        })

    self.__severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity(self):
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-log:syslog-severity', is_config=True)

  severity = __builtin__.property(_get_severity, _set_severity)


  _pyangbind_elements = OrderedDict([('severity', severity), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/messages/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for Syslog messages.
  """
  __slots__ = ('_path_helper', '_extmethods', '__severity',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-log:syslog-severity', is_config=True)

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
      return ['system', 'messages', 'config']

  def _get_severity(self):
    """
    Getter method for severity, mapped from YANG variable /system/messages/config/severity (oc-log:syslog-severity)

    YANG Description: Specifies that only messages of the given severity (or
greater severity) are sent over the RPC.

This is analogous to differentiating which severity is to be
sent to legacy Syslog servers, as opposed to local buffer or
files.
    """
    return self.__severity
      
  def _set_severity(self, v, load=False):
    """
    Setter method for severity, mapped from YANG variable /system/messages/config/severity (oc-log:syslog-severity)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity() directly.

    YANG Description: Specifies that only messages of the given severity (or
greater severity) are sent over the RPC.

This is analogous to differentiating which severity is to be
sent to legacy Syslog servers, as opposed to local buffer or
files.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-log:syslog-severity', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity must be of a type compatible with oc-log:syslog-severity""",
          'defined-type': "oc-log:syslog-severity",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-log:syslog-severity', is_config=True)""",
        })

    self.__severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity(self):
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-log:syslog-severity', is_config=True)

  severity = __builtin__.property(_get_severity, _set_severity)


  _pyangbind_elements = OrderedDict([('severity', severity), ])


