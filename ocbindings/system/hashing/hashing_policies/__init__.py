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
from . import hashing_policy
class hashing_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/hashing/hashing-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for hashing, including configuration and
state data.
  """
  __slots__ = ('_path_helper', '_extmethods', '__hashing_policy',)

  _yang_name = 'hashing-policies'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hashing_policy = YANGDynClass(base=YANGListType("name",hashing_policy.hashing_policy, yang_name="hashing-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="hashing-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='list', is_config=True)

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
      return ['system', 'hashing', 'hashing-policies']

  def _get_hashing_policy(self):
    """
    Getter method for hashing_policy, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy (list)

    YANG Description: The list of named policies to be used on the device.
    """
    return self.__hashing_policy
      
  def _set_hashing_policy(self, v, load=False):
    """
    Setter method for hashing_policy, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hashing_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hashing_policy() directly.

    YANG Description: The list of named policies to be used on the device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",hashing_policy.hashing_policy, yang_name="hashing-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="hashing-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hashing_policy must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",hashing_policy.hashing_policy, yang_name="hashing-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="hashing-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='list', is_config=True)""",
        })

    self.__hashing_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hashing_policy(self):
    self.__hashing_policy = YANGDynClass(base=YANGListType("name",hashing_policy.hashing_policy, yang_name="hashing-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="hashing-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='list', is_config=True)

  hashing_policy = __builtin__.property(_get_hashing_policy, _set_hashing_policy)


  _pyangbind_elements = OrderedDict([('hashing_policy', hashing_policy), ])


from . import hashing_policy
class hashing_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/hashing/hashing-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for hashing, including configuration and
state data.
  """
  __slots__ = ('_path_helper', '_extmethods', '__hashing_policy',)

  _yang_name = 'hashing-policies'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hashing_policy = YANGDynClass(base=YANGListType("name",hashing_policy.hashing_policy, yang_name="hashing-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="hashing-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='list', is_config=True)

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
      return ['system', 'hashing', 'hashing-policies']

  def _get_hashing_policy(self):
    """
    Getter method for hashing_policy, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy (list)

    YANG Description: The list of named policies to be used on the device.
    """
    return self.__hashing_policy
      
  def _set_hashing_policy(self, v, load=False):
    """
    Setter method for hashing_policy, mapped from YANG variable /system/hashing/hashing_policies/hashing_policy (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hashing_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hashing_policy() directly.

    YANG Description: The list of named policies to be used on the device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",hashing_policy.hashing_policy, yang_name="hashing-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="hashing-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hashing_policy must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",hashing_policy.hashing_policy, yang_name="hashing-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="hashing-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='list', is_config=True)""",
        })

    self.__hashing_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hashing_policy(self):
    self.__hashing_policy = YANGDynClass(base=YANGListType("name",hashing_policy.hashing_policy, yang_name="hashing-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="hashing-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/hashing', defining_module='openconfig-hashing', yang_type='list', is_config=True)

  hashing_policy = __builtin__.property(_get_hashing_policy, _set_hashing_policy)


  _pyangbind_elements = OrderedDict([('hashing_policy', hashing_policy), ])


