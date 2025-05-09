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
from . import ha_group
class ha_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-fw-high-availability - based on the path /ha-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for HA groups
  """
  __slots__ = ('_path_helper', '_extmethods', '__ha_group',)

  _yang_name = 'ha-groups'
  _yang_namespace = 'http://openconfig.net/yang/oc-fw-ha'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ha_group = YANGDynClass(base=YANGListType("id",ha_group.ha_group, yang_name="ha-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="ha-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='list', is_config=True)

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
      return ['ha-groups']

  def _get_ha_group(self):
    """
    Getter method for ha_group, mapped from YANG variable /ha_groups/ha_group (list)

    YANG Description: HA group id used to create a logical HA group
    """
    return self.__ha_group
      
  def _set_ha_group(self, v, load=False):
    """
    Setter method for ha_group, mapped from YANG variable /ha_groups/ha_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ha_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ha_group() directly.

    YANG Description: HA group id used to create a logical HA group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",ha_group.ha_group, yang_name="ha-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="ha-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ha_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",ha_group.ha_group, yang_name="ha-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="ha-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='list', is_config=True)""",
        })

    self.__ha_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ha_group(self):
    self.__ha_group = YANGDynClass(base=YANGListType("id",ha_group.ha_group, yang_name="ha-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="ha-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='list', is_config=True)

  ha_group = __builtin__.property(_get_ha_group, _set_ha_group)


  _pyangbind_elements = OrderedDict([('ha_group', ha_group), ])


from . import ha_group
class ha_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-fw-high-availability - based on the path /ha-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for HA groups
  """
  __slots__ = ('_path_helper', '_extmethods', '__ha_group',)

  _yang_name = 'ha-groups'
  _yang_namespace = 'http://openconfig.net/yang/oc-fw-ha'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ha_group = YANGDynClass(base=YANGListType("id",ha_group.ha_group, yang_name="ha-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="ha-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='list', is_config=True)

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
      return ['ha-groups']

  def _get_ha_group(self):
    """
    Getter method for ha_group, mapped from YANG variable /ha_groups/ha_group (list)

    YANG Description: HA group id used to create a logical HA group
    """
    return self.__ha_group
      
  def _set_ha_group(self, v, load=False):
    """
    Setter method for ha_group, mapped from YANG variable /ha_groups/ha_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ha_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ha_group() directly.

    YANG Description: HA group id used to create a logical HA group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",ha_group.ha_group, yang_name="ha-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="ha-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ha_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",ha_group.ha_group, yang_name="ha-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="ha-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='list', is_config=True)""",
        })

    self.__ha_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ha_group(self):
    self.__ha_group = YANGDynClass(base=YANGListType("id",ha_group.ha_group, yang_name="ha-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="ha-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='list', is_config=True)

  ha_group = __builtin__.property(_get_ha_group, _set_ha_group)


  _pyangbind_elements = OrderedDict([('ha_group', ha_group), ])


