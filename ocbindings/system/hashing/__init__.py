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
from . import algorithms
from . import hashing_policies
class hashing(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/hashing. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for Hashing algorithms and hashing policies
  """
  __slots__ = ('_path_helper', '_extmethods', '__algorithms','__hashing_policies',)

  _yang_name = 'hashing'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__algorithms = YANGDynClass(base=algorithms.algorithms, is_container='container', yang_name="algorithms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    self.__hashing_policies = YANGDynClass(base=hashing_policies.hashing_policies, is_container='container', yang_name="hashing-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)

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
      return ['system', 'hashing']

  def _get_algorithms(self):
    """
    Getter method for algorithms, mapped from YANG variable /system/hashing/algorithms (container)

    YANG Description: Container for vendor supported hashing algorithms.
    """
    return self.__algorithms
      
  def _set_algorithms(self, v, load=False):
    """
    Setter method for algorithms, mapped from YANG variable /system/hashing/algorithms (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_algorithms is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_algorithms() directly.

    YANG Description: Container for vendor supported hashing algorithms.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=algorithms.algorithms, is_container='container', yang_name="algorithms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """algorithms must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=algorithms.algorithms, is_container='container', yang_name="algorithms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)""",
        })

    self.__algorithms = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_algorithms(self):
    self.__algorithms = YANGDynClass(base=algorithms.algorithms, is_container='container', yang_name="algorithms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)


  def _get_hashing_policies(self):
    """
    Getter method for hashing_policies, mapped from YANG variable /system/hashing/hashing_policies (container)

    YANG Description: Top level container for hashing, including configuration and
state data.
    """
    return self.__hashing_policies
      
  def _set_hashing_policies(self, v, load=False):
    """
    Setter method for hashing_policies, mapped from YANG variable /system/hashing/hashing_policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hashing_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hashing_policies() directly.

    YANG Description: Top level container for hashing, including configuration and
state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=hashing_policies.hashing_policies, is_container='container', yang_name="hashing-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hashing_policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hashing_policies.hashing_policies, is_container='container', yang_name="hashing-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)""",
        })

    self.__hashing_policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hashing_policies(self):
    self.__hashing_policies = YANGDynClass(base=hashing_policies.hashing_policies, is_container='container', yang_name="hashing-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)

  algorithms = __builtin__.property(_get_algorithms, _set_algorithms)
  hashing_policies = __builtin__.property(_get_hashing_policies, _set_hashing_policies)


  _pyangbind_elements = OrderedDict([('algorithms', algorithms), ('hashing_policies', hashing_policies), ])


from . import algorithms
from . import hashing_policies
class hashing(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/hashing. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for Hashing algorithms and hashing policies
  """
  __slots__ = ('_path_helper', '_extmethods', '__algorithms','__hashing_policies',)

  _yang_name = 'hashing'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__algorithms = YANGDynClass(base=algorithms.algorithms, is_container='container', yang_name="algorithms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    self.__hashing_policies = YANGDynClass(base=hashing_policies.hashing_policies, is_container='container', yang_name="hashing-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)

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
      return ['system', 'hashing']

  def _get_algorithms(self):
    """
    Getter method for algorithms, mapped from YANG variable /system/hashing/algorithms (container)

    YANG Description: Container for vendor supported hashing algorithms.
    """
    return self.__algorithms
      
  def _set_algorithms(self, v, load=False):
    """
    Setter method for algorithms, mapped from YANG variable /system/hashing/algorithms (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_algorithms is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_algorithms() directly.

    YANG Description: Container for vendor supported hashing algorithms.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=algorithms.algorithms, is_container='container', yang_name="algorithms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """algorithms must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=algorithms.algorithms, is_container='container', yang_name="algorithms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)""",
        })

    self.__algorithms = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_algorithms(self):
    self.__algorithms = YANGDynClass(base=algorithms.algorithms, is_container='container', yang_name="algorithms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)


  def _get_hashing_policies(self):
    """
    Getter method for hashing_policies, mapped from YANG variable /system/hashing/hashing_policies (container)

    YANG Description: Top level container for hashing, including configuration and
state data.
    """
    return self.__hashing_policies
      
  def _set_hashing_policies(self, v, load=False):
    """
    Setter method for hashing_policies, mapped from YANG variable /system/hashing/hashing_policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hashing_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hashing_policies() directly.

    YANG Description: Top level container for hashing, including configuration and
state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=hashing_policies.hashing_policies, is_container='container', yang_name="hashing-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hashing_policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hashing_policies.hashing_policies, is_container='container', yang_name="hashing-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)""",
        })

    self.__hashing_policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hashing_policies(self):
    self.__hashing_policies = YANGDynClass(base=hashing_policies.hashing_policies, is_container='container', yang_name="hashing-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='container', is_config=True)

  algorithms = __builtin__.property(_get_algorithms, _set_algorithms)
  hashing_policies = __builtin__.property(_get_hashing_policies, _set_hashing_policies)


  _pyangbind_elements = OrderedDict([('algorithms', algorithms), ('hashing_policies', hashing_policies), ])


