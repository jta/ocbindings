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
from . import hash_field_modes
class hashing_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/hashing/hashing-policies/hashing-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of named policies to be used on the device.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__config','__state','__hash_field_modes',)

  _yang_name = 'hashing-policy'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=False)
    self.__hash_field_modes = YANGDynClass(base=hash_field_modes.hash_field_modes, is_container='container', yang_name="hash-field-modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)

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
      return ['system', 'hashing', 'hashing-policies', 'hashing-policy']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/name (leafref)

    YANG Description: References the name of the hashing policy.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: References the name of the hashing policy.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='leafref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config (container)

    YANG Description: Configurable items at the global hash policy level.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configurable items at the global hash policy level.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/state (container)

    YANG Description: Operational state data at the global hash policy
level.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data at the global hash policy
level.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=False)


  def _get_hash_field_modes(self):
    """
    Getter method for hash_field_modes, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/hash_field_modes (container)

    YANG Description: Container for specifying inputs to be used when
calculating the hash.
    """
    return self.__hash_field_modes
      
  def _set_hash_field_modes(self, v, load=False):
    """
    Setter method for hash_field_modes, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/hash_field_modes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hash_field_modes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hash_field_modes() directly.

    YANG Description: Container for specifying inputs to be used when
calculating the hash.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=hash_field_modes.hash_field_modes, is_container='container', yang_name="hash-field-modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hash_field_modes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hash_field_modes.hash_field_modes, is_container='container', yang_name="hash-field-modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)""",
        })

    self.__hash_field_modes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hash_field_modes(self):
    self.__hash_field_modes = YANGDynClass(base=hash_field_modes.hash_field_modes, is_container='container', yang_name="hash-field-modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  hash_field_modes = __builtin__.property(_get_hash_field_modes, _set_hash_field_modes)


  _pyangbind_elements = OrderedDict([('name', name), ('config', config), ('state', state), ('hash_field_modes', hash_field_modes), ])


from . import config
from . import state
from . import hash_field_modes
class hashing_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/hashing/hashing-policies/hashing-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of named policies to be used on the device.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__config','__state','__hash_field_modes',)

  _yang_name = 'hashing-policy'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=False)
    self.__hash_field_modes = YANGDynClass(base=hash_field_modes.hash_field_modes, is_container='container', yang_name="hash-field-modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)

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
      return ['system', 'hashing', 'hashing-policies', 'hashing-policy']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/name (leafref)

    YANG Description: References the name of the hashing policy.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: References the name of the hashing policy.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='leafref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config (container)

    YANG Description: Configurable items at the global hash policy level.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configurable items at the global hash policy level.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/state (container)

    YANG Description: Operational state data at the global hash policy
level.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data at the global hash policy
level.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=False)


  def _get_hash_field_modes(self):
    """
    Getter method for hash_field_modes, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/hash_field_modes (container)

    YANG Description: Container for specifying inputs to be used when
calculating the hash.
    """
    return self.__hash_field_modes
      
  def _set_hash_field_modes(self, v, load=False):
    """
    Setter method for hash_field_modes, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/hash_field_modes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hash_field_modes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hash_field_modes() directly.

    YANG Description: Container for specifying inputs to be used when
calculating the hash.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=hash_field_modes.hash_field_modes, is_container='container', yang_name="hash-field-modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hash_field_modes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hash_field_modes.hash_field_modes, is_container='container', yang_name="hash-field-modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)""",
        })

    self.__hash_field_modes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hash_field_modes(self):
    self.__hash_field_modes = YANGDynClass(base=hash_field_modes.hash_field_modes, is_container='container', yang_name="hash-field-modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  hash_field_modes = __builtin__.property(_get_hash_field_modes, _set_hash_field_modes)


  _pyangbind_elements = OrderedDict([('name', name), ('config', config), ('state', state), ('hash_field_modes', hash_field_modes), ])


