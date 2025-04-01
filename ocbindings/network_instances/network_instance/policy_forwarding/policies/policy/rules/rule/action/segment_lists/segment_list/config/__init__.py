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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/segment-lists/segment-list/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for the SR-TE segment list.
  """
  __slots__ = ('_path_helper', '_extmethods', '__index','__weight',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'rules', 'rule', 'action', 'segment-lists', 'segment-list', 'config']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/index (uint64)

    YANG Description: Unique integer identifying the segment list within the set
of segment lists used for the SR-TE policy action.
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/index (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Unique integer identifying the segment list within the set
of segment lists used for the SR-TE policy action.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/weight (uint32)

    YANG Description: The weight of the segment list within the set of segment lists
specified for the policy. The traffic that is forwarded according
to the policy is distributed across the set of paths such that
each list receives weight/(sum of all weights) traffic.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: The weight of the segment list within the set of segment lists
specified for the policy. The traffic that is forwarded according
to the policy is distributed across the set of paths such that
each list receives weight/(sum of all weights) traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  weight = __builtin__.property(_get_weight, _set_weight)


  _pyangbind_elements = OrderedDict([('index', index), ('weight', weight), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/segment-lists/segment-list/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for the SR-TE segment list.
  """
  __slots__ = ('_path_helper', '_extmethods', '__index','__weight',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'rules', 'rule', 'action', 'segment-lists', 'segment-list', 'config']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/index (uint64)

    YANG Description: Unique integer identifying the segment list within the set
of segment lists used for the SR-TE policy action.
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/index (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Unique integer identifying the segment list within the set
of segment lists used for the SR-TE policy action.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/weight (uint32)

    YANG Description: The weight of the segment list within the set of segment lists
specified for the policy. The traffic that is forwarded according
to the policy is distributed across the set of paths such that
each list receives weight/(sum of all weights) traffic.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: The weight of the segment list within the set of segment lists
specified for the policy. The traffic that is forwarded according
to the policy is distributed across the set of paths such that
each list receives weight/(sum of all weights) traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  weight = __builtin__.property(_get_weight, _set_weight)


  _pyangbind_elements = OrderedDict([('index', index), ('weight', weight), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/segment-lists/segment-list/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for the SR-TE segment list.
  """
  __slots__ = ('_path_helper', '_extmethods', '__index','__weight',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'rules', 'rule', 'action', 'segment-lists', 'segment-list', 'config']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/index (uint64)

    YANG Description: Unique integer identifying the segment list within the set
of segment lists used for the SR-TE policy action.
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/index (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Unique integer identifying the segment list within the set
of segment lists used for the SR-TE policy action.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/weight (uint32)

    YANG Description: The weight of the segment list within the set of segment lists
specified for the policy. The traffic that is forwarded according
to the policy is distributed across the set of paths such that
each list receives weight/(sum of all weights) traffic.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: The weight of the segment list within the set of segment lists
specified for the policy. The traffic that is forwarded according
to the policy is distributed across the set of paths such that
each list receives weight/(sum of all weights) traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  weight = __builtin__.property(_get_weight, _set_weight)


  _pyangbind_elements = OrderedDict([('index', index), ('weight', weight), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/segment-lists/segment-list/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for the SR-TE segment list.
  """
  __slots__ = ('_path_helper', '_extmethods', '__index','__weight',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'rules', 'rule', 'action', 'segment-lists', 'segment-list', 'config']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/index (uint64)

    YANG Description: Unique integer identifying the segment list within the set
of segment lists used for the SR-TE policy action.
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/index (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Unique integer identifying the segment list within the set
of segment lists used for the SR-TE policy action.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint64', is_config=True)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/weight (uint32)

    YANG Description: The weight of the segment list within the set of segment lists
specified for the policy. The traffic that is forwarded according
to the policy is distributed across the set of paths such that
each list receives weight/(sum of all weights) traffic.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/segment_lists/segment_list/config/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: The weight of the segment list within the set of segment lists
specified for the policy. The traffic that is forwarded according
to the policy is distributed across the set of paths such that
each list receives weight/(sum of all weights) traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/policy-forwarding/sr-te', defining_module='openconfig-pf-srte', yang_type='uint32', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  weight = __builtin__.property(_get_weight, _set_weight)


  _pyangbind_elements = OrderedDict([('index', index), ('weight', weight), ])


