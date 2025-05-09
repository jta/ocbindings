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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/aaa/accounting/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for user activity accounting.
  """
  __slots__ = ('_path_helper', '_extmethods', '__accounting_method',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__accounting_method = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),str,]), is_leaf=False, yang_name="accounting-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'aaa', 'accounting', 'config']

  def _get_accounting_method(self):
    """
    Getter method for accounting_method, mapped from YANG variable /access_points/access_point/system/aaa/accounting/config/accounting_method (union)

    YANG Description: An ordered list of methods used for AAA accounting for this
event type.  The method is defined by the destination for
accounting data, which may be specified as the group of
all TACACS+/RADIUS servers, a defined server group, or
the local system.
    """
    return self.__accounting_method
      
  def _set_accounting_method(self, v, load=False):
    """
    Setter method for accounting_method, mapped from YANG variable /access_points/access_point/system/aaa/accounting/config/accounting_method (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accounting_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accounting_method() directly.

    YANG Description: An ordered list of methods used for AAA accounting for this
event type.  The method is defined by the destination for
accounting data, which may be specified as the group of
all TACACS+/RADIUS servers, a defined server group, or
the local system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),str,]), is_leaf=False, yang_name="accounting-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accounting_method must be of a type compatible with union""",
          'defined-type': "openconfig-access-points:union",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),str,]), is_leaf=False, yang_name="accounting-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=True)""",
        })

    self.__accounting_method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accounting_method(self):
    self.__accounting_method = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),str,]), is_leaf=False, yang_name="accounting-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=True)

  accounting_method = __builtin__.property(_get_accounting_method, _set_accounting_method)


  _pyangbind_elements = OrderedDict([('accounting_method', accounting_method), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/aaa/accounting/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for user activity accounting.
  """
  __slots__ = ('_path_helper', '_extmethods', '__accounting_method',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__accounting_method = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),str,]), is_leaf=False, yang_name="accounting-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'aaa', 'accounting', 'config']

  def _get_accounting_method(self):
    """
    Getter method for accounting_method, mapped from YANG variable /access_points/access_point/system/aaa/accounting/config/accounting_method (union)

    YANG Description: An ordered list of methods used for AAA accounting for this
event type.  The method is defined by the destination for
accounting data, which may be specified as the group of
all TACACS+/RADIUS servers, a defined server group, or
the local system.
    """
    return self.__accounting_method
      
  def _set_accounting_method(self, v, load=False):
    """
    Setter method for accounting_method, mapped from YANG variable /access_points/access_point/system/aaa/accounting/config/accounting_method (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accounting_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accounting_method() directly.

    YANG Description: An ordered list of methods used for AAA accounting for this
event type.  The method is defined by the destination for
accounting data, which may be specified as the group of
all TACACS+/RADIUS servers, a defined server group, or
the local system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),str,]), is_leaf=False, yang_name="accounting-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accounting_method must be of a type compatible with union""",
          'defined-type': "openconfig-access-points:union",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),str,]), is_leaf=False, yang_name="accounting-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=True)""",
        })

    self.__accounting_method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accounting_method(self):
    self.__accounting_method = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'openconfig-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),str,]), is_leaf=False, yang_name="accounting-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=True)

  accounting_method = __builtin__.property(_get_accounting_method, _set_accounting_method)


  _pyangbind_elements = OrderedDict([('accounting_method', accounting_method), ])


