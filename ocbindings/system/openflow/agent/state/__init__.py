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
  from YANG module openconfig-system - based on the path /system/openflow/agent/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for the Openflow agent state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__datapath_id','__failure_mode','__backoff_interval','__max_backoff','__inactivity_probe',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__datapath_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}'}), is_leaf=True, yang_name="datapath-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:datapath-id', is_config=False)
    self.__failure_mode = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SECURE': {}, 'STANDALONE': {}},), is_leaf=True, yang_name="failure-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:failure-mode', is_config=False)
    self.__backoff_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="backoff-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    self.__max_backoff = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-backoff", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    self.__inactivity_probe = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="inactivity-probe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)

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
      return ['system', 'openflow', 'agent', 'state']

  def _get_datapath_id(self):
    """
    Getter method for datapath_id, mapped from YANG variable /system/openflow/agent/state/datapath_id (of-types:datapath-id)

    YANG Description: Datapath unique ID. The lower 48-bits are for
a MAC address, while the upper 16-bits are
implementer-defined.
    """
    return self.__datapath_id
      
  def _set_datapath_id(self, v, load=False):
    """
    Setter method for datapath_id, mapped from YANG variable /system/openflow/agent/state/datapath_id (of-types:datapath-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_datapath_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_datapath_id() directly.

    YANG Description: Datapath unique ID. The lower 48-bits are for
a MAC address, while the upper 16-bits are
implementer-defined.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}'}), is_leaf=True, yang_name="datapath-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:datapath-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """datapath_id must be of a type compatible with of-types:datapath-id""",
          'defined-type': "of-types:datapath-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}'}), is_leaf=True, yang_name="datapath-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:datapath-id', is_config=False)""",
        })

    self.__datapath_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_datapath_id(self):
    self.__datapath_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}'}), is_leaf=True, yang_name="datapath-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:datapath-id', is_config=False)


  def _get_failure_mode(self):
    """
    Getter method for failure_mode, mapped from YANG variable /system/openflow/agent/state/failure_mode (of-types:failure-mode)

    YANG Description: Failure mode for Openflow.
    """
    return self.__failure_mode
      
  def _set_failure_mode(self, v, load=False):
    """
    Setter method for failure_mode, mapped from YANG variable /system/openflow/agent/state/failure_mode (of-types:failure-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_failure_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_failure_mode() directly.

    YANG Description: Failure mode for Openflow.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SECURE': {}, 'STANDALONE': {}},), is_leaf=True, yang_name="failure-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:failure-mode', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """failure_mode must be of a type compatible with of-types:failure-mode""",
          'defined-type': "of-types:failure-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SECURE': {}, 'STANDALONE': {}},), is_leaf=True, yang_name="failure-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:failure-mode', is_config=False)""",
        })

    self.__failure_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_failure_mode(self):
    self.__failure_mode = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SECURE': {}, 'STANDALONE': {}},), is_leaf=True, yang_name="failure-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:failure-mode', is_config=False)


  def _get_backoff_interval(self):
    """
    Getter method for backoff_interval, mapped from YANG variable /system/openflow/agent/state/backoff_interval (uint32)

    YANG Description: Openflow agent connection backoff interval.
    """
    return self.__backoff_interval
      
  def _set_backoff_interval(self, v, load=False):
    """
    Setter method for backoff_interval, mapped from YANG variable /system/openflow/agent/state/backoff_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_backoff_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_backoff_interval() directly.

    YANG Description: Openflow agent connection backoff interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="backoff-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """backoff_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="backoff-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)""",
        })

    self.__backoff_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_backoff_interval(self):
    self.__backoff_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="backoff-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)


  def _get_max_backoff(self):
    """
    Getter method for max_backoff, mapped from YANG variable /system/openflow/agent/state/max_backoff (uint32)

    YANG Description: Openflow agent max backoff time.
    """
    return self.__max_backoff
      
  def _set_max_backoff(self, v, load=False):
    """
    Setter method for max_backoff, mapped from YANG variable /system/openflow/agent/state/max_backoff (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_backoff is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_backoff() directly.

    YANG Description: Openflow agent max backoff time.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-backoff", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_backoff must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-backoff", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)""",
        })

    self.__max_backoff = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_backoff(self):
    self.__max_backoff = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-backoff", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)


  def _get_inactivity_probe(self):
    """
    Getter method for inactivity_probe, mapped from YANG variable /system/openflow/agent/state/inactivity_probe (uint32)

    YANG Description: Openflow agent inactivity probe period.
    """
    return self.__inactivity_probe
      
  def _set_inactivity_probe(self, v, load=False):
    """
    Setter method for inactivity_probe, mapped from YANG variable /system/openflow/agent/state/inactivity_probe (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inactivity_probe is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inactivity_probe() directly.

    YANG Description: Openflow agent inactivity probe period.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="inactivity-probe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inactivity_probe must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="inactivity-probe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)""",
        })

    self.__inactivity_probe = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inactivity_probe(self):
    self.__inactivity_probe = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="inactivity-probe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)

  datapath_id = __builtin__.property(_get_datapath_id)
  failure_mode = __builtin__.property(_get_failure_mode)
  backoff_interval = __builtin__.property(_get_backoff_interval)
  max_backoff = __builtin__.property(_get_max_backoff)
  inactivity_probe = __builtin__.property(_get_inactivity_probe)


  _pyangbind_elements = OrderedDict([('datapath_id', datapath_id), ('failure_mode', failure_mode), ('backoff_interval', backoff_interval), ('max_backoff', max_backoff), ('inactivity_probe', inactivity_probe), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/openflow/agent/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for the Openflow agent state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__datapath_id','__failure_mode','__backoff_interval','__max_backoff','__inactivity_probe',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__datapath_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}'}), is_leaf=True, yang_name="datapath-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:datapath-id', is_config=False)
    self.__failure_mode = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SECURE': {}, 'STANDALONE': {}},), is_leaf=True, yang_name="failure-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:failure-mode', is_config=False)
    self.__backoff_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="backoff-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    self.__max_backoff = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-backoff", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    self.__inactivity_probe = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="inactivity-probe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)

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
      return ['system', 'openflow', 'agent', 'state']

  def _get_datapath_id(self):
    """
    Getter method for datapath_id, mapped from YANG variable /system/openflow/agent/state/datapath_id (of-types:datapath-id)

    YANG Description: Datapath unique ID. The lower 48-bits are for
a MAC address, while the upper 16-bits are
implementer-defined.
    """
    return self.__datapath_id
      
  def _set_datapath_id(self, v, load=False):
    """
    Setter method for datapath_id, mapped from YANG variable /system/openflow/agent/state/datapath_id (of-types:datapath-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_datapath_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_datapath_id() directly.

    YANG Description: Datapath unique ID. The lower 48-bits are for
a MAC address, while the upper 16-bits are
implementer-defined.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}'}), is_leaf=True, yang_name="datapath-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:datapath-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """datapath_id must be of a type compatible with of-types:datapath-id""",
          'defined-type': "of-types:datapath-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}'}), is_leaf=True, yang_name="datapath-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:datapath-id', is_config=False)""",
        })

    self.__datapath_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_datapath_id(self):
    self.__datapath_id = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}'}), is_leaf=True, yang_name="datapath-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:datapath-id', is_config=False)


  def _get_failure_mode(self):
    """
    Getter method for failure_mode, mapped from YANG variable /system/openflow/agent/state/failure_mode (of-types:failure-mode)

    YANG Description: Failure mode for Openflow.
    """
    return self.__failure_mode
      
  def _set_failure_mode(self, v, load=False):
    """
    Setter method for failure_mode, mapped from YANG variable /system/openflow/agent/state/failure_mode (of-types:failure-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_failure_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_failure_mode() directly.

    YANG Description: Failure mode for Openflow.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SECURE': {}, 'STANDALONE': {}},), is_leaf=True, yang_name="failure-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:failure-mode', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """failure_mode must be of a type compatible with of-types:failure-mode""",
          'defined-type': "of-types:failure-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SECURE': {}, 'STANDALONE': {}},), is_leaf=True, yang_name="failure-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:failure-mode', is_config=False)""",
        })

    self.__failure_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_failure_mode(self):
    self.__failure_mode = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SECURE': {}, 'STANDALONE': {}},), is_leaf=True, yang_name="failure-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='of-types:failure-mode', is_config=False)


  def _get_backoff_interval(self):
    """
    Getter method for backoff_interval, mapped from YANG variable /system/openflow/agent/state/backoff_interval (uint32)

    YANG Description: Openflow agent connection backoff interval.
    """
    return self.__backoff_interval
      
  def _set_backoff_interval(self, v, load=False):
    """
    Setter method for backoff_interval, mapped from YANG variable /system/openflow/agent/state/backoff_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_backoff_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_backoff_interval() directly.

    YANG Description: Openflow agent connection backoff interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="backoff-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """backoff_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="backoff-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)""",
        })

    self.__backoff_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_backoff_interval(self):
    self.__backoff_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="backoff-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)


  def _get_max_backoff(self):
    """
    Getter method for max_backoff, mapped from YANG variable /system/openflow/agent/state/max_backoff (uint32)

    YANG Description: Openflow agent max backoff time.
    """
    return self.__max_backoff
      
  def _set_max_backoff(self, v, load=False):
    """
    Setter method for max_backoff, mapped from YANG variable /system/openflow/agent/state/max_backoff (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_backoff is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_backoff() directly.

    YANG Description: Openflow agent max backoff time.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-backoff", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_backoff must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-backoff", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)""",
        })

    self.__max_backoff = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_backoff(self):
    self.__max_backoff = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-backoff", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)


  def _get_inactivity_probe(self):
    """
    Getter method for inactivity_probe, mapped from YANG variable /system/openflow/agent/state/inactivity_probe (uint32)

    YANG Description: Openflow agent inactivity probe period.
    """
    return self.__inactivity_probe
      
  def _set_inactivity_probe(self, v, load=False):
    """
    Setter method for inactivity_probe, mapped from YANG variable /system/openflow/agent/state/inactivity_probe (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inactivity_probe is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inactivity_probe() directly.

    YANG Description: Openflow agent inactivity probe period.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="inactivity-probe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inactivity_probe must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="inactivity-probe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)""",
        })

    self.__inactivity_probe = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inactivity_probe(self):
    self.__inactivity_probe = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="inactivity-probe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openflow', defining_module='openconfig-openflow', yang_type='uint32', is_config=False)

  datapath_id = __builtin__.property(_get_datapath_id)
  failure_mode = __builtin__.property(_get_failure_mode)
  backoff_interval = __builtin__.property(_get_backoff_interval)
  max_backoff = __builtin__.property(_get_max_backoff)
  inactivity_probe = __builtin__.property(_get_inactivity_probe)


  _pyangbind_elements = OrderedDict([('datapath_id', datapath_id), ('failure_mode', failure_mode), ('backoff_interval', backoff_interval), ('max_backoff', max_backoff), ('inactivity_probe', inactivity_probe), ])


