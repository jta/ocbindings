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
from . import attenuator
class attenuators(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-optical-attenuator - based on the path /optical-attenuator/attenuators. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of attenuators
  """
  __slots__ = ('_path_helper', '_extmethods', '__attenuator',)

  _yang_name = 'attenuators'
  _yang_namespace = 'http://openconfig.net/yang/optical-attenuator'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attenuator = YANGDynClass(base=YANGListType("name",attenuator.attenuator, yang_name="attenuator", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="attenuator", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='list', is_config=True)

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
      return ['optical-attenuator', 'attenuators']

  def _get_attenuator(self):
    """
    Getter method for attenuator, mapped from YANG variable /optical_attenuator/attenuators/attenuator (list)

    YANG Description: List of variable optical attenuators present in the device
    """
    return self.__attenuator
      
  def _set_attenuator(self, v, load=False):
    """
    Setter method for attenuator, mapped from YANG variable /optical_attenuator/attenuators/attenuator (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attenuator is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attenuator() directly.

    YANG Description: List of variable optical attenuators present in the device
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",attenuator.attenuator, yang_name="attenuator", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="attenuator", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attenuator must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",attenuator.attenuator, yang_name="attenuator", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="attenuator", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='list', is_config=True)""",
        })

    self.__attenuator = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attenuator(self):
    self.__attenuator = YANGDynClass(base=YANGListType("name",attenuator.attenuator, yang_name="attenuator", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="attenuator", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='list', is_config=True)

  attenuator = __builtin__.property(_get_attenuator, _set_attenuator)


  _pyangbind_elements = OrderedDict([('attenuator', attenuator), ])


from . import attenuator
class attenuators(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-optical-attenuator - based on the path /optical-attenuator/attenuators. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of attenuators
  """
  __slots__ = ('_path_helper', '_extmethods', '__attenuator',)

  _yang_name = 'attenuators'
  _yang_namespace = 'http://openconfig.net/yang/optical-attenuator'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attenuator = YANGDynClass(base=YANGListType("name",attenuator.attenuator, yang_name="attenuator", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="attenuator", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='list', is_config=True)

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
      return ['optical-attenuator', 'attenuators']

  def _get_attenuator(self):
    """
    Getter method for attenuator, mapped from YANG variable /optical_attenuator/attenuators/attenuator (list)

    YANG Description: List of variable optical attenuators present in the device
    """
    return self.__attenuator
      
  def _set_attenuator(self, v, load=False):
    """
    Setter method for attenuator, mapped from YANG variable /optical_attenuator/attenuators/attenuator (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attenuator is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attenuator() directly.

    YANG Description: List of variable optical attenuators present in the device
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",attenuator.attenuator, yang_name="attenuator", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="attenuator", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attenuator must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",attenuator.attenuator, yang_name="attenuator", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="attenuator", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='list', is_config=True)""",
        })

    self.__attenuator = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attenuator(self):
    self.__attenuator = YANGDynClass(base=YANGListType("name",attenuator.attenuator, yang_name="attenuator", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="attenuator", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='list', is_config=True)

  attenuator = __builtin__.property(_get_attenuator, _set_attenuator)


  _pyangbind_elements = OrderedDict([('attenuator', attenuator), ])


