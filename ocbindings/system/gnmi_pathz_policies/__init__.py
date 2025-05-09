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
from . import policies
class gnmi_pathz_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/gnmi-pathz-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Collection of OpenConfig-path-based authorization policies that
have been installed on the device using the gNSI OpenConfig-
path-based authorization policy management service.
Each policy listed here is identified by its status (either
   ACTIVE or SANDBOX) and has its version and creation date/time
listed.
  """
  __slots__ = ('_path_helper', '_extmethods', '__policies',)

  _yang_name = 'gnmi-pathz-policies'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__policies = YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://github.com/openconfig/yang/gnsi/pathz', defining_module='openconfig-gnsi-pathz', yang_type='container', is_config=False)

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
      return ['system', 'gnmi-pathz-policies']

  def _get_policies(self):
    """
    Getter method for policies, mapped from YANG variable /system/gnmi_pathz_policies/policies (container)

    YANG Description: Information about freshness of an OpenConfig-path-based
authorization policy that have been installed
on the device using the gNSI OpenConfig-path-based
authorization policy management service.
    """
    return self.__policies
      
  def _set_policies(self, v, load=False):
    """
    Setter method for policies, mapped from YANG variable /system/gnmi_pathz_policies/policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policies() directly.

    YANG Description: Information about freshness of an OpenConfig-path-based
authorization policy that have been installed
on the device using the gNSI OpenConfig-path-based
authorization policy management service.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://github.com/openconfig/yang/gnsi/pathz', defining_module='openconfig-gnsi-pathz', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://github.com/openconfig/yang/gnsi/pathz', defining_module='openconfig-gnsi-pathz', yang_type='container', is_config=False)""",
        })

    self.__policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policies(self):
    self.__policies = YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://github.com/openconfig/yang/gnsi/pathz', defining_module='openconfig-gnsi-pathz', yang_type='container', is_config=False)

  policies = __builtin__.property(_get_policies)


  _pyangbind_elements = OrderedDict([('policies', policies), ])


from . import policies
class gnmi_pathz_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/gnmi-pathz-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Collection of OpenConfig-path-based authorization policies that
have been installed on the device using the gNSI OpenConfig-
path-based authorization policy management service.
Each policy listed here is identified by its status (either
   ACTIVE or SANDBOX) and has its version and creation date/time
listed.
  """
  __slots__ = ('_path_helper', '_extmethods', '__policies',)

  _yang_name = 'gnmi-pathz-policies'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__policies = YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://github.com/openconfig/yang/gnsi/pathz', defining_module='openconfig-gnsi-pathz', yang_type='container', is_config=False)

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
      return ['system', 'gnmi-pathz-policies']

  def _get_policies(self):
    """
    Getter method for policies, mapped from YANG variable /system/gnmi_pathz_policies/policies (container)

    YANG Description: Information about freshness of an OpenConfig-path-based
authorization policy that have been installed
on the device using the gNSI OpenConfig-path-based
authorization policy management service.
    """
    return self.__policies
      
  def _set_policies(self, v, load=False):
    """
    Setter method for policies, mapped from YANG variable /system/gnmi_pathz_policies/policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policies() directly.

    YANG Description: Information about freshness of an OpenConfig-path-based
authorization policy that have been installed
on the device using the gNSI OpenConfig-path-based
authorization policy management service.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://github.com/openconfig/yang/gnsi/pathz', defining_module='openconfig-gnsi-pathz', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://github.com/openconfig/yang/gnsi/pathz', defining_module='openconfig-gnsi-pathz', yang_type='container', is_config=False)""",
        })

    self.__policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policies(self):
    self.__policies = YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://github.com/openconfig/yang/gnsi/pathz', defining_module='openconfig-gnsi-pathz', yang_type='container', is_config=False)

  policies = __builtin__.property(_get_policies)


  _pyangbind_elements = OrderedDict([('policies', policies), ])


