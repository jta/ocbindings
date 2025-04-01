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
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries/acl-entry/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for per-interface ACL entries
  """
  __slots__ = ('_path_helper', '_extmethods', '__sequence_id','__matched_packets','__matched_octets',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/acl'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sequence_id = YANGDynClass(base=str, is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    self.__matched_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)
    self.__matched_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets', 'ingress-acl-set', 'acl-entries', 'acl-entry', 'state']

  def _get_sequence_id(self):
    """
    Getter method for sequence_id, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/sequence_id (leafref)

    YANG Description: Reference to an entry in the ACL set applied to an
interface
    """
    return self.__sequence_id
      
  def _set_sequence_id(self, v, load=False):
    """
    Setter method for sequence_id, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/sequence_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sequence_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sequence_id() directly.

    YANG Description: Reference to an entry in the ACL set applied to an
interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sequence_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)""",
        })

    self.__sequence_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sequence_id(self):
    self.__sequence_id = YANGDynClass(base=str, is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)


  def _get_matched_packets(self):
    """
    Getter method for matched_packets, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/matched_packets (oc-yang:counter64)

    YANG Description: Count of the number of packets matching the current ACL
entry.

An implementation should provide this counter on a
per-interface per-ACL-entry if possible.

If an implementation only supports ACL counters per entry
(i.e., not broken out per interface), then the value
should be equal to the aggregate count across all interfaces.

An implementation that provides counters per entry per
interface is not required to also provide an aggregate count,
e.g., per entry -- the user is expected to be able implement
the required aggregation if such a count is needed.
    """
    return self.__matched_packets
      
  def _set_matched_packets(self, v, load=False):
    """
    Setter method for matched_packets, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/matched_packets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_matched_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_matched_packets() directly.

    YANG Description: Count of the number of packets matching the current ACL
entry.

An implementation should provide this counter on a
per-interface per-ACL-entry if possible.

If an implementation only supports ACL counters per entry
(i.e., not broken out per interface), then the value
should be equal to the aggregate count across all interfaces.

An implementation that provides counters per entry per
interface is not required to also provide an aggregate count,
e.g., per entry -- the user is expected to be able implement
the required aggregation if such a count is needed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """matched_packets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__matched_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_matched_packets(self):
    self.__matched_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)


  def _get_matched_octets(self):
    """
    Getter method for matched_octets, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/matched_octets (oc-yang:counter64)

    YANG Description: Count of the number of octets (bytes) matching the current
ACL entry.

An implementation should provide this counter on a
per-interface per-ACL-entry if possible.

If an implementation only supports ACL counters per entry
(i.e., not broken out per interface), then the value
should be equal to the aggregate count across all interfaces.

An implementation that provides counters per entry per
interface is not required to also provide an aggregate count,
e.g., per entry -- the user is expected to be able implement
the required aggregation if such a count is needed.
    """
    return self.__matched_octets
      
  def _set_matched_octets(self, v, load=False):
    """
    Setter method for matched_octets, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/matched_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_matched_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_matched_octets() directly.

    YANG Description: Count of the number of octets (bytes) matching the current
ACL entry.

An implementation should provide this counter on a
per-interface per-ACL-entry if possible.

If an implementation only supports ACL counters per entry
(i.e., not broken out per interface), then the value
should be equal to the aggregate count across all interfaces.

An implementation that provides counters per entry per
interface is not required to also provide an aggregate count,
e.g., per entry -- the user is expected to be able implement
the required aggregation if such a count is needed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """matched_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__matched_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_matched_octets(self):
    self.__matched_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)

  sequence_id = __builtin__.property(_get_sequence_id)
  matched_packets = __builtin__.property(_get_matched_packets)
  matched_octets = __builtin__.property(_get_matched_octets)


  _pyangbind_elements = OrderedDict([('sequence_id', sequence_id), ('matched_packets', matched_packets), ('matched_octets', matched_octets), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries/acl-entry/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for per-interface ACL entries
  """
  __slots__ = ('_path_helper', '_extmethods', '__sequence_id','__matched_packets','__matched_octets',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/acl'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sequence_id = YANGDynClass(base=str, is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    self.__matched_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)
    self.__matched_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets', 'ingress-acl-set', 'acl-entries', 'acl-entry', 'state']

  def _get_sequence_id(self):
    """
    Getter method for sequence_id, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/sequence_id (leafref)

    YANG Description: Reference to an entry in the ACL set applied to an
interface
    """
    return self.__sequence_id
      
  def _set_sequence_id(self, v, load=False):
    """
    Setter method for sequence_id, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/sequence_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sequence_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sequence_id() directly.

    YANG Description: Reference to an entry in the ACL set applied to an
interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sequence_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)""",
        })

    self.__sequence_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sequence_id(self):
    self.__sequence_id = YANGDynClass(base=str, is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)


  def _get_matched_packets(self):
    """
    Getter method for matched_packets, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/matched_packets (oc-yang:counter64)

    YANG Description: Count of the number of packets matching the current ACL
entry.

An implementation should provide this counter on a
per-interface per-ACL-entry if possible.

If an implementation only supports ACL counters per entry
(i.e., not broken out per interface), then the value
should be equal to the aggregate count across all interfaces.

An implementation that provides counters per entry per
interface is not required to also provide an aggregate count,
e.g., per entry -- the user is expected to be able implement
the required aggregation if such a count is needed.
    """
    return self.__matched_packets
      
  def _set_matched_packets(self, v, load=False):
    """
    Setter method for matched_packets, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/matched_packets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_matched_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_matched_packets() directly.

    YANG Description: Count of the number of packets matching the current ACL
entry.

An implementation should provide this counter on a
per-interface per-ACL-entry if possible.

If an implementation only supports ACL counters per entry
(i.e., not broken out per interface), then the value
should be equal to the aggregate count across all interfaces.

An implementation that provides counters per entry per
interface is not required to also provide an aggregate count,
e.g., per entry -- the user is expected to be able implement
the required aggregation if such a count is needed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """matched_packets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__matched_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_matched_packets(self):
    self.__matched_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)


  def _get_matched_octets(self):
    """
    Getter method for matched_octets, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/matched_octets (oc-yang:counter64)

    YANG Description: Count of the number of octets (bytes) matching the current
ACL entry.

An implementation should provide this counter on a
per-interface per-ACL-entry if possible.

If an implementation only supports ACL counters per entry
(i.e., not broken out per interface), then the value
should be equal to the aggregate count across all interfaces.

An implementation that provides counters per entry per
interface is not required to also provide an aggregate count,
e.g., per entry -- the user is expected to be able implement
the required aggregation if such a count is needed.
    """
    return self.__matched_octets
      
  def _set_matched_octets(self, v, load=False):
    """
    Setter method for matched_octets, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set/acl_entries/acl_entry/state/matched_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_matched_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_matched_octets() directly.

    YANG Description: Count of the number of octets (bytes) matching the current
ACL entry.

An implementation should provide this counter on a
per-interface per-ACL-entry if possible.

If an implementation only supports ACL counters per entry
(i.e., not broken out per interface), then the value
should be equal to the aggregate count across all interfaces.

An implementation that provides counters per entry per
interface is not required to also provide an aggregate count,
e.g., per entry -- the user is expected to be able implement
the required aggregation if such a count is needed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """matched_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__matched_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_matched_octets(self):
    self.__matched_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-yang:counter64', is_config=False)

  sequence_id = __builtin__.property(_get_sequence_id)
  matched_packets = __builtin__.property(_get_matched_packets)
  matched_octets = __builtin__.property(_get_matched_octets)


  _pyangbind_elements = OrderedDict([('sequence_id', sequence_id), ('matched_packets', matched_packets), ('matched_octets', matched_octets), ])


