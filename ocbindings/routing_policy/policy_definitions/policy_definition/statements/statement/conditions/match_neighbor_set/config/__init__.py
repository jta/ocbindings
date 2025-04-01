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
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__neighbor_set','__match_set_options',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__neighbor_set = YANGDynClass(base=str, is_leaf=True, yang_name="neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)
    self.__match_set_options = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ANY': {}, 'INVERT': {}},), default=str("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'conditions', 'match-neighbor-set', 'config']

  def _get_neighbor_set(self):
    """
    Getter method for neighbor_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set/config/neighbor_set (leafref)

    YANG Description: References a defined neighbor set
    """
    return self.__neighbor_set
      
  def _set_neighbor_set(self, v, load=False):
    """
    Setter method for neighbor_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set/config/neighbor_set (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_set() directly.

    YANG Description: References a defined neighbor set
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_set must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)""",
        })

    self.__neighbor_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_set(self):
    self.__neighbor_set = YANGDynClass(base=str, is_leaf=True, yang_name="neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)


  def _get_match_set_options(self):
    """
    Getter method for match_set_options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set/config/match_set_options (oc-pol-types:match-set-options-restricted-type)

    YANG Description: Optional parameter that governs the behaviour of the
match operation.  This leaf only supports matching on ANY
member of the set or inverting the match.  Matching on ALL is
not supported
    """
    return self.__match_set_options
      
  def _set_match_set_options(self, v, load=False):
    """
    Setter method for match_set_options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set/config/match_set_options (oc-pol-types:match-set-options-restricted-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_set_options is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_set_options() directly.

    YANG Description: Optional parameter that governs the behaviour of the
match operation.  This leaf only supports matching on ANY
member of the set or inverting the match.  Matching on ALL is
not supported
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ANY': {}, 'INVERT': {}},), default=str("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_set_options must be of a type compatible with oc-pol-types:match-set-options-restricted-type""",
          'defined-type': "oc-pol-types:match-set-options-restricted-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ANY': {}, 'INVERT': {}},), default=str("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=True)""",
        })

    self.__match_set_options = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_set_options(self):
    self.__match_set_options = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ANY': {}, 'INVERT': {}},), default=str("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=True)

  neighbor_set = __builtin__.property(_get_neighbor_set, _set_neighbor_set)
  match_set_options = __builtin__.property(_get_match_set_options, _set_match_set_options)


  _pyangbind_elements = OrderedDict([('neighbor_set', neighbor_set), ('match_set_options', match_set_options), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__neighbor_set','__match_set_options',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__neighbor_set = YANGDynClass(base=str, is_leaf=True, yang_name="neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)
    self.__match_set_options = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ANY': {}, 'INVERT': {}},), default=str("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'conditions', 'match-neighbor-set', 'config']

  def _get_neighbor_set(self):
    """
    Getter method for neighbor_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set/config/neighbor_set (leafref)

    YANG Description: References a defined neighbor set
    """
    return self.__neighbor_set
      
  def _set_neighbor_set(self, v, load=False):
    """
    Setter method for neighbor_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set/config/neighbor_set (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_set() directly.

    YANG Description: References a defined neighbor set
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_set must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)""",
        })

    self.__neighbor_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_set(self):
    self.__neighbor_set = YANGDynClass(base=str, is_leaf=True, yang_name="neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)


  def _get_match_set_options(self):
    """
    Getter method for match_set_options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set/config/match_set_options (oc-pol-types:match-set-options-restricted-type)

    YANG Description: Optional parameter that governs the behaviour of the
match operation.  This leaf only supports matching on ANY
member of the set or inverting the match.  Matching on ALL is
not supported
    """
    return self.__match_set_options
      
  def _set_match_set_options(self, v, load=False):
    """
    Setter method for match_set_options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set/config/match_set_options (oc-pol-types:match-set-options-restricted-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_set_options is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_set_options() directly.

    YANG Description: Optional parameter that governs the behaviour of the
match operation.  This leaf only supports matching on ANY
member of the set or inverting the match.  Matching on ALL is
not supported
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ANY': {}, 'INVERT': {}},), default=str("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_set_options must be of a type compatible with oc-pol-types:match-set-options-restricted-type""",
          'defined-type': "oc-pol-types:match-set-options-restricted-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ANY': {}, 'INVERT': {}},), default=str("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=True)""",
        })

    self.__match_set_options = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_set_options(self):
    self.__match_set_options = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ANY': {}, 'INVERT': {}},), default=str("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=True)

  neighbor_set = __builtin__.property(_get_neighbor_set, _set_neighbor_set)
  match_set_options = __builtin__.property(_get_match_set_options, _set_match_set_options)


  _pyangbind_elements = OrderedDict([('neighbor_set', neighbor_set), ('match_set_options', match_set_options), ])


