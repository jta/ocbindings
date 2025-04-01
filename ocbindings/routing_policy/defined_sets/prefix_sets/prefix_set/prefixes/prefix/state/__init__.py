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
  from YANG module openconfig-routing-policy - based on the path /routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for prefix definition
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip_prefix','__masklength_range',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip_prefix = YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-inet:ip-prefix', is_config=False)
    self.__masklength_range = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]+\\.\\.[0-9]+)|exact)'}), is_leaf=True, yang_name="masklength-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='string', is_config=False)

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
      return ['routing-policy', 'defined-sets', 'prefix-sets', 'prefix-set', 'prefixes', 'prefix', 'state']

  def _get_ip_prefix(self):
    """
    Getter method for ip_prefix, mapped from YANG variable /routing_policy/defined_sets/prefix_sets/prefix_set/prefixes/prefix/state/ip_prefix (oc-inet:ip-prefix)

    YANG Description: The prefix member in CIDR notation -- while the
prefix may be either IPv4 or IPv6, most
implementations require all members of the prefix set
to be the same address family.  Mixing address types in
the same prefix set is likely to cause an error.
    """
    return self.__ip_prefix
      
  def _set_ip_prefix(self, v, load=False):
    """
    Setter method for ip_prefix, mapped from YANG variable /routing_policy/defined_sets/prefix_sets/prefix_set/prefixes/prefix/state/ip_prefix (oc-inet:ip-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_prefix() directly.

    YANG Description: The prefix member in CIDR notation -- while the
prefix may be either IPv4 or IPv6, most
implementations require all members of the prefix set
to be the same address family.  Mixing address types in
the same prefix set is likely to cause an error.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-inet:ip-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_prefix must be of a type compatible with oc-inet:ip-prefix""",
          'defined-type': "oc-inet:ip-prefix",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-inet:ip-prefix', is_config=False)""",
        })

    self.__ip_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_prefix(self):
    self.__ip_prefix = YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-inet:ip-prefix', is_config=False)


  def _get_masklength_range(self):
    """
    Getter method for masklength_range, mapped from YANG variable /routing_policy/defined_sets/prefix_sets/prefix_set/prefixes/prefix/state/masklength_range (string)

    YANG Description: Defines a range for the masklength, or 'exact' if
the prefix has an exact length.

Example: 10.3.192.0/21 through 10.3.192.0/24 would be
expressed as prefix: 10.3.192.0/21,
masklength-range: 21..24.

Example: 10.3.192.0/21 would be expressed as
prefix: 10.3.192.0/21,
masklength-range: exact
    """
    return self.__masklength_range
      
  def _set_masklength_range(self, v, load=False):
    """
    Setter method for masklength_range, mapped from YANG variable /routing_policy/defined_sets/prefix_sets/prefix_set/prefixes/prefix/state/masklength_range (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_masklength_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_masklength_range() directly.

    YANG Description: Defines a range for the masklength, or 'exact' if
the prefix has an exact length.

Example: 10.3.192.0/21 through 10.3.192.0/24 would be
expressed as prefix: 10.3.192.0/21,
masklength-range: 21..24.

Example: 10.3.192.0/21 would be expressed as
prefix: 10.3.192.0/21,
masklength-range: exact
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]+\\.\\.[0-9]+)|exact)'}), is_leaf=True, yang_name="masklength-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """masklength_range must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]+\\.\\.[0-9]+)|exact)'}), is_leaf=True, yang_name="masklength-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='string', is_config=False)""",
        })

    self.__masklength_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_masklength_range(self):
    self.__masklength_range = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]+\\.\\.[0-9]+)|exact)'}), is_leaf=True, yang_name="masklength-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='string', is_config=False)

  ip_prefix = __builtin__.property(_get_ip_prefix)
  masklength_range = __builtin__.property(_get_masklength_range)


  _pyangbind_elements = OrderedDict([('ip_prefix', ip_prefix), ('masklength_range', masklength_range), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for prefix definition
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip_prefix','__masklength_range',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip_prefix = YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-inet:ip-prefix', is_config=False)
    self.__masklength_range = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]+\\.\\.[0-9]+)|exact)'}), is_leaf=True, yang_name="masklength-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='string', is_config=False)

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
      return ['routing-policy', 'defined-sets', 'prefix-sets', 'prefix-set', 'prefixes', 'prefix', 'state']

  def _get_ip_prefix(self):
    """
    Getter method for ip_prefix, mapped from YANG variable /routing_policy/defined_sets/prefix_sets/prefix_set/prefixes/prefix/state/ip_prefix (oc-inet:ip-prefix)

    YANG Description: The prefix member in CIDR notation -- while the
prefix may be either IPv4 or IPv6, most
implementations require all members of the prefix set
to be the same address family.  Mixing address types in
the same prefix set is likely to cause an error.
    """
    return self.__ip_prefix
      
  def _set_ip_prefix(self, v, load=False):
    """
    Setter method for ip_prefix, mapped from YANG variable /routing_policy/defined_sets/prefix_sets/prefix_set/prefixes/prefix/state/ip_prefix (oc-inet:ip-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_prefix() directly.

    YANG Description: The prefix member in CIDR notation -- while the
prefix may be either IPv4 or IPv6, most
implementations require all members of the prefix set
to be the same address family.  Mixing address types in
the same prefix set is likely to cause an error.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-inet:ip-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_prefix must be of a type compatible with oc-inet:ip-prefix""",
          'defined-type': "oc-inet:ip-prefix",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-inet:ip-prefix', is_config=False)""",
        })

    self.__ip_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_prefix(self):
    self.__ip_prefix = YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}/([0-9]|[12][0-9]|3[0-2])'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-inet:ip-prefix', is_config=False)


  def _get_masklength_range(self):
    """
    Getter method for masklength_range, mapped from YANG variable /routing_policy/defined_sets/prefix_sets/prefix_set/prefixes/prefix/state/masklength_range (string)

    YANG Description: Defines a range for the masklength, or 'exact' if
the prefix has an exact length.

Example: 10.3.192.0/21 through 10.3.192.0/24 would be
expressed as prefix: 10.3.192.0/21,
masklength-range: 21..24.

Example: 10.3.192.0/21 would be expressed as
prefix: 10.3.192.0/21,
masklength-range: exact
    """
    return self.__masklength_range
      
  def _set_masklength_range(self, v, load=False):
    """
    Setter method for masklength_range, mapped from YANG variable /routing_policy/defined_sets/prefix_sets/prefix_set/prefixes/prefix/state/masklength_range (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_masklength_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_masklength_range() directly.

    YANG Description: Defines a range for the masklength, or 'exact' if
the prefix has an exact length.

Example: 10.3.192.0/21 through 10.3.192.0/24 would be
expressed as prefix: 10.3.192.0/21,
masklength-range: 21..24.

Example: 10.3.192.0/21 would be expressed as
prefix: 10.3.192.0/21,
masklength-range: exact
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]+\\.\\.[0-9]+)|exact)'}), is_leaf=True, yang_name="masklength-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """masklength_range must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]+\\.\\.[0-9]+)|exact)'}), is_leaf=True, yang_name="masklength-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='string', is_config=False)""",
        })

    self.__masklength_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_masklength_range(self):
    self.__masklength_range = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9]+\\.\\.[0-9]+)|exact)'}), is_leaf=True, yang_name="masklength-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='string', is_config=False)

  ip_prefix = __builtin__.property(_get_ip_prefix)
  masklength_range = __builtin__.property(_get_masklength_range)


  _pyangbind_elements = OrderedDict([('ip_prefix', ip_prefix), ('masklength_range', masklength_range), ])


