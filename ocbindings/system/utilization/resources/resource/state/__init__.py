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
  from YANG module openconfig-system - based on the path /system/utilization/resources/resource/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for resource utilization.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__used_threshold_upper','__used_threshold_upper_clear','__active_component_list',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='string', is_config=False)
    self.__used_threshold_upper = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)
    self.__used_threshold_upper_clear = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)
    self.__active_component_list = YANGDynClass(unique=True, base=TypedListType(allowed_type=str), is_leaf=False, yang_name="active-component-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='leafref', is_config=False)

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
      return ['system', 'utilization', 'resources', 'resource', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/utilization/resources/resource/state/name (string)

    YANG Description: Resource name within the system.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/utilization/resources/resource/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Resource name within the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='string', is_config=False)


  def _get_used_threshold_upper(self):
    """
    Getter method for used_threshold_upper, mapped from YANG variable /system/utilization/resources/resource/state/used_threshold_upper (oc-types:percentage)

    YANG Description: The used percentage value (used / (used + free) * 100) that
when crossed will set utilization-threshold-exceeded to 'true'.
    """
    return self.__used_threshold_upper
      
  def _set_used_threshold_upper(self, v, load=False):
    """
    Setter method for used_threshold_upper, mapped from YANG variable /system/utilization/resources/resource/state/used_threshold_upper (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_used_threshold_upper is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_used_threshold_upper() directly.

    YANG Description: The used percentage value (used / (used + free) * 100) that
when crossed will set utilization-threshold-exceeded to 'true'.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """used_threshold_upper must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__used_threshold_upper = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_used_threshold_upper(self):
    self.__used_threshold_upper = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)


  def _get_used_threshold_upper_clear(self):
    """
    Getter method for used_threshold_upper_clear, mapped from YANG variable /system/utilization/resources/resource/state/used_threshold_upper_clear (oc-types:percentage)

    YANG Description: The used percentage value (used / (used + free) * 100) that when
crossed will set utilization-threshold-exceeded to 'false'.
    """
    return self.__used_threshold_upper_clear
      
  def _set_used_threshold_upper_clear(self, v, load=False):
    """
    Setter method for used_threshold_upper_clear, mapped from YANG variable /system/utilization/resources/resource/state/used_threshold_upper_clear (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_used_threshold_upper_clear is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_used_threshold_upper_clear() directly.

    YANG Description: The used percentage value (used / (used + free) * 100) that when
crossed will set utilization-threshold-exceeded to 'false'.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """used_threshold_upper_clear must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__used_threshold_upper_clear = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_used_threshold_upper_clear(self):
    self.__used_threshold_upper_clear = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)


  def _get_active_component_list(self):
    """
    Getter method for active_component_list, mapped from YANG variable /system/utilization/resources/resource/state/active_component_list (leafref)

    YANG Description: List of references to each component which has this resource.
    """
    return self.__active_component_list
      
  def _set_active_component_list(self, v, load=False):
    """
    Setter method for active_component_list, mapped from YANG variable /system/utilization/resources/resource/state/active_component_list (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_active_component_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_active_component_list() directly.

    YANG Description: List of references to each component which has this resource.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=str), is_leaf=False, yang_name="active-component-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """active_component_list must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=str), is_leaf=False, yang_name="active-component-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='leafref', is_config=False)""",
        })

    self.__active_component_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_active_component_list(self):
    self.__active_component_list = YANGDynClass(unique=True, base=TypedListType(allowed_type=str), is_leaf=False, yang_name="active-component-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='leafref', is_config=False)

  name = __builtin__.property(_get_name)
  used_threshold_upper = __builtin__.property(_get_used_threshold_upper)
  used_threshold_upper_clear = __builtin__.property(_get_used_threshold_upper_clear)
  active_component_list = __builtin__.property(_get_active_component_list)


  _pyangbind_elements = OrderedDict([('name', name), ('used_threshold_upper', used_threshold_upper), ('used_threshold_upper_clear', used_threshold_upper_clear), ('active_component_list', active_component_list), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/utilization/resources/resource/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for resource utilization.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__used_threshold_upper','__used_threshold_upper_clear','__active_component_list',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='string', is_config=False)
    self.__used_threshold_upper = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)
    self.__used_threshold_upper_clear = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)
    self.__active_component_list = YANGDynClass(unique=True, base=TypedListType(allowed_type=str), is_leaf=False, yang_name="active-component-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='leafref', is_config=False)

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
      return ['system', 'utilization', 'resources', 'resource', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/utilization/resources/resource/state/name (string)

    YANG Description: Resource name within the system.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/utilization/resources/resource/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Resource name within the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='string', is_config=False)


  def _get_used_threshold_upper(self):
    """
    Getter method for used_threshold_upper, mapped from YANG variable /system/utilization/resources/resource/state/used_threshold_upper (oc-types:percentage)

    YANG Description: The used percentage value (used / (used + free) * 100) that
when crossed will set utilization-threshold-exceeded to 'true'.
    """
    return self.__used_threshold_upper
      
  def _set_used_threshold_upper(self, v, load=False):
    """
    Setter method for used_threshold_upper, mapped from YANG variable /system/utilization/resources/resource/state/used_threshold_upper (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_used_threshold_upper is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_used_threshold_upper() directly.

    YANG Description: The used percentage value (used / (used + free) * 100) that
when crossed will set utilization-threshold-exceeded to 'true'.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """used_threshold_upper must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__used_threshold_upper = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_used_threshold_upper(self):
    self.__used_threshold_upper = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)


  def _get_used_threshold_upper_clear(self):
    """
    Getter method for used_threshold_upper_clear, mapped from YANG variable /system/utilization/resources/resource/state/used_threshold_upper_clear (oc-types:percentage)

    YANG Description: The used percentage value (used / (used + free) * 100) that when
crossed will set utilization-threshold-exceeded to 'false'.
    """
    return self.__used_threshold_upper_clear
      
  def _set_used_threshold_upper_clear(self, v, load=False):
    """
    Setter method for used_threshold_upper_clear, mapped from YANG variable /system/utilization/resources/resource/state/used_threshold_upper_clear (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_used_threshold_upper_clear is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_used_threshold_upper_clear() directly.

    YANG Description: The used percentage value (used / (used + free) * 100) that when
crossed will set utilization-threshold-exceeded to 'false'.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """used_threshold_upper_clear must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__used_threshold_upper_clear = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_used_threshold_upper_clear(self):
    self.__used_threshold_upper_clear = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="used-threshold-upper-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='oc-types:percentage', is_config=False)


  def _get_active_component_list(self):
    """
    Getter method for active_component_list, mapped from YANG variable /system/utilization/resources/resource/state/active_component_list (leafref)

    YANG Description: List of references to each component which has this resource.
    """
    return self.__active_component_list
      
  def _set_active_component_list(self, v, load=False):
    """
    Setter method for active_component_list, mapped from YANG variable /system/utilization/resources/resource/state/active_component_list (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_active_component_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_active_component_list() directly.

    YANG Description: List of references to each component which has this resource.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=str), is_leaf=False, yang_name="active-component-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """active_component_list must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=str), is_leaf=False, yang_name="active-component-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='leafref', is_config=False)""",
        })

    self.__active_component_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_active_component_list(self):
    self.__active_component_list = YANGDynClass(unique=True, base=TypedListType(allowed_type=str), is_leaf=False, yang_name="active-component-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system-utilization', defining_module='openconfig-system-utilization', yang_type='leafref', is_config=False)

  name = __builtin__.property(_get_name)
  used_threshold_upper = __builtin__.property(_get_used_threshold_upper)
  used_threshold_upper_clear = __builtin__.property(_get_used_threshold_upper_clear)
  active_component_list = __builtin__.property(_get_active_component_list)


  _pyangbind_elements = OrderedDict([('name', name), ('used_threshold_upper', used_threshold_upper), ('used_threshold_upper_clear', used_threshold_upper_clear), ('active_component_list', active_component_list), ])


