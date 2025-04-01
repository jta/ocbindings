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
  from YANG module openconfig-defined-sets - based on the path /defined-sets/ipv4-prefix-sets/ipv4-prefix-set/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for IPv4 prefix sets.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__description','__prefix',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/defined-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)
    self.__description = YANGDynClass(base=str, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)
    self.__prefix = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'})), is_leaf=False, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='oc-inet:ipv4-prefix', is_config=True)

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
      return ['defined-sets', 'ipv4-prefix-sets', 'ipv4-prefix-set', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/name (string)

    YANG Description: A user defined name of the IPv4 prefix set.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: A user defined name of the IPv4 prefix set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/description (string)

    YANG Description: A user defined IPv4 prefix set description.
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: A user defined IPv4 prefix set description.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=str, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)


  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/prefix (oc-inet:ipv4-prefix)

    YANG Description: A user defined list of IPv4 prefixes to be used in match
conditions. Each entry is a IPv4 + mask combination.
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/prefix (oc-inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.

    YANG Description: A user defined list of IPv4 prefixes to be used in match
conditions. Each entry is a IPv4 + mask combination.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'})), is_leaf=False, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='oc-inet:ipv4-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with oc-inet:ipv4-prefix""",
          'defined-type': "oc-inet:ipv4-prefix",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'})), is_leaf=False, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='oc-inet:ipv4-prefix', is_config=True)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'})), is_leaf=False, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='oc-inet:ipv4-prefix', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  description = __builtin__.property(_get_description, _set_description)
  prefix = __builtin__.property(_get_prefix, _set_prefix)


  _pyangbind_elements = OrderedDict([('name', name), ('description', description), ('prefix', prefix), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-defined-sets - based on the path /defined-sets/ipv4-prefix-sets/ipv4-prefix-set/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for IPv4 prefix sets.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__description','__prefix',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/defined-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)
    self.__description = YANGDynClass(base=str, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)
    self.__prefix = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'})), is_leaf=False, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='oc-inet:ipv4-prefix', is_config=True)

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
      return ['defined-sets', 'ipv4-prefix-sets', 'ipv4-prefix-set', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/name (string)

    YANG Description: A user defined name of the IPv4 prefix set.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: A user defined name of the IPv4 prefix set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/description (string)

    YANG Description: A user defined IPv4 prefix set description.
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: A user defined IPv4 prefix set description.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=str, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='string', is_config=True)


  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/prefix (oc-inet:ipv4-prefix)

    YANG Description: A user defined list of IPv4 prefixes to be used in match
conditions. Each entry is a IPv4 + mask combination.
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /defined_sets/ipv4_prefix_sets/ipv4_prefix_set/config/prefix (oc-inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.

    YANG Description: A user defined list of IPv4 prefixes to be used in match
conditions. Each entry is a IPv4 + mask combination.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'})), is_leaf=False, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='oc-inet:ipv4-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with oc-inet:ipv4-prefix""",
          'defined-type': "oc-inet:ipv4-prefix",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'})), is_leaf=False, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='oc-inet:ipv4-prefix', is_config=True)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'})), is_leaf=False, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/defined-sets', defining_module='openconfig-defined-sets', yang_type='oc-inet:ipv4-prefix', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  description = __builtin__.property(_get_description, _set_description)
  prefix = __builtin__.property(_get_prefix, _set_prefix)


  _pyangbind_elements = OrderedDict([('name', name), ('description', description), ('prefix', prefix), ])


