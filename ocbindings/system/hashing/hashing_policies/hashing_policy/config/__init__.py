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
  from YANG module openconfig-system - based on the path /system/hashing/hashing-policies/hashing-policy/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configurable items at the global hash policy level.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__seed','__algorithm',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)
    self.__seed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="seed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='uint64', is_config=True)
    self.__algorithm = YANGDynClass(base=str, is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)

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
      return ['system', 'hashing', 'hashing-policies', 'hashing-policy', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/name (string)

    YANG Description: The name of the hashing policy.
When a configured user-controlled policy is created by the
system, it is instantiated with the same name in the
/system/hashing-policies/hashing-policy/name list.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: The name of the hashing policy.
When a configured user-controlled policy is created by the
system, it is instantiated with the same name in the
/system/hashing-policies/hashing-policy/name list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)


  def _get_seed(self):
    """
    Getter method for seed, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/seed (uint64)

    YANG Description: The seed used to initialize the hash algorithm
    """
    return self.__seed
      
  def _set_seed(self, v, load=False):
    """
    Setter method for seed, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/seed (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_seed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_seed() directly.

    YANG Description: The seed used to initialize the hash algorithm
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="seed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """seed must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="seed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='uint64', is_config=True)""",
        })

    self.__seed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_seed(self):
    self.__seed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="seed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='uint64', is_config=True)


  def _get_algorithm(self):
    """
    Getter method for algorithm, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/algorithm (string)

    YANG Description: The name of hash algorithm. This algorithm MUST
be a supported algorithm
    """
    return self.__algorithm
      
  def _set_algorithm(self, v, load=False):
    """
    Setter method for algorithm, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/algorithm (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_algorithm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_algorithm() directly.

    YANG Description: The name of hash algorithm. This algorithm MUST
be a supported algorithm
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """algorithm must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)""",
        })

    self.__algorithm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_algorithm(self):
    self.__algorithm = YANGDynClass(base=str, is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  seed = __builtin__.property(_get_seed, _set_seed)
  algorithm = __builtin__.property(_get_algorithm, _set_algorithm)


  _pyangbind_elements = OrderedDict([('name', name), ('seed', seed), ('algorithm', algorithm), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/hashing/hashing-policies/hashing-policy/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configurable items at the global hash policy level.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__seed','__algorithm',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)
    self.__seed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="seed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='uint64', is_config=True)
    self.__algorithm = YANGDynClass(base=str, is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)

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
      return ['system', 'hashing', 'hashing-policies', 'hashing-policy', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/name (string)

    YANG Description: The name of the hashing policy.
When a configured user-controlled policy is created by the
system, it is instantiated with the same name in the
/system/hashing-policies/hashing-policy/name list.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: The name of the hashing policy.
When a configured user-controlled policy is created by the
system, it is instantiated with the same name in the
/system/hashing-policies/hashing-policy/name list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)


  def _get_seed(self):
    """
    Getter method for seed, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/seed (uint64)

    YANG Description: The seed used to initialize the hash algorithm
    """
    return self.__seed
      
  def _set_seed(self, v, load=False):
    """
    Setter method for seed, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/seed (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_seed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_seed() directly.

    YANG Description: The seed used to initialize the hash algorithm
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="seed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """seed must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="seed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='uint64', is_config=True)""",
        })

    self.__seed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_seed(self):
    self.__seed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="seed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='uint64', is_config=True)


  def _get_algorithm(self):
    """
    Getter method for algorithm, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/algorithm (string)

    YANG Description: The name of hash algorithm. This algorithm MUST
be a supported algorithm
    """
    return self.__algorithm
      
  def _set_algorithm(self, v, load=False):
    """
    Setter method for algorithm, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy/config/algorithm (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_algorithm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_algorithm() directly.

    YANG Description: The name of hash algorithm. This algorithm MUST
be a supported algorithm
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """algorithm must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)""",
        })

    self.__algorithm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_algorithm(self):
    self.__algorithm = YANGDynClass(base=str, is_leaf=True, yang_name="algorithm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  seed = __builtin__.property(_get_seed, _set_seed)
  algorithm = __builtin__.property(_get_algorithm, _set_algorithm)


  _pyangbind_elements = OrderedDict([('name', name), ('seed', seed), ('algorithm', algorithm), ])


