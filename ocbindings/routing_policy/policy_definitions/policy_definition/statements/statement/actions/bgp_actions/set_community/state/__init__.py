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
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/bgp-actions/set-community/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for the set-community action
  """
  __slots__ = ('_path_helper', '_extmethods', '__method','__options',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__method = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INLINE': {}, 'REFERENCE': {}},), is_leaf=True, yang_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)
    self.__options = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ADD': {}, 'REMOVE': {}, 'REPLACE': {}},), is_leaf=True, yang_name="options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-community-option-type', is_config=False)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions', 'bgp-actions', 'set-community', 'state']

  def _get_method(self):
    """
    Getter method for method, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community/state/method (enumeration)

    YANG Description: Indicates the method used to specify the extended
communities for the set-ext-community action
    """
    return self.__method
      
  def _set_method(self, v, load=False):
    """
    Setter method for method, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community/state/method (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_method() directly.

    YANG Description: Indicates the method used to specify the extended
communities for the set-ext-community action
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INLINE': {}, 'REFERENCE': {}},), is_leaf=True, yang_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """method must be of a type compatible with enumeration""",
          'defined-type': "openconfig-bgp-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INLINE': {}, 'REFERENCE': {}},), is_leaf=True, yang_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)""",
        })

    self.__method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_method(self):
    self.__method = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INLINE': {}, 'REFERENCE': {}},), is_leaf=True, yang_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)


  def _get_options(self):
    """
    Getter method for options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community/state/options (bgp-set-community-option-type)

    YANG Description: Options for modifying the community attribute with
the specified values.  These options apply to both
methods of setting the community attribute.
    """
    return self.__options
      
  def _set_options(self, v, load=False):
    """
    Setter method for options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community/state/options (bgp-set-community-option-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_options is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_options() directly.

    YANG Description: Options for modifying the community attribute with
the specified values.  These options apply to both
methods of setting the community attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ADD': {}, 'REMOVE': {}, 'REPLACE': {}},), is_leaf=True, yang_name="options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-community-option-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """options must be of a type compatible with bgp-set-community-option-type""",
          'defined-type': "openconfig-bgp-policy:bgp-set-community-option-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ADD': {}, 'REMOVE': {}, 'REPLACE': {}},), is_leaf=True, yang_name="options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-community-option-type', is_config=False)""",
        })

    self.__options = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_options(self):
    self.__options = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ADD': {}, 'REMOVE': {}, 'REPLACE': {}},), is_leaf=True, yang_name="options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-community-option-type', is_config=False)

  method = __builtin__.property(_get_method)
  options = __builtin__.property(_get_options)


  _pyangbind_elements = OrderedDict([('method', method), ('options', options), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/bgp-actions/set-community/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for the set-community action
  """
  __slots__ = ('_path_helper', '_extmethods', '__method','__options',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__method = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INLINE': {}, 'REFERENCE': {}},), is_leaf=True, yang_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)
    self.__options = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ADD': {}, 'REMOVE': {}, 'REPLACE': {}},), is_leaf=True, yang_name="options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-community-option-type', is_config=False)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions', 'bgp-actions', 'set-community', 'state']

  def _get_method(self):
    """
    Getter method for method, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community/state/method (enumeration)

    YANG Description: Indicates the method used to specify the extended
communities for the set-ext-community action
    """
    return self.__method
      
  def _set_method(self, v, load=False):
    """
    Setter method for method, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community/state/method (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_method() directly.

    YANG Description: Indicates the method used to specify the extended
communities for the set-ext-community action
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INLINE': {}, 'REFERENCE': {}},), is_leaf=True, yang_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """method must be of a type compatible with enumeration""",
          'defined-type': "openconfig-bgp-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INLINE': {}, 'REFERENCE': {}},), is_leaf=True, yang_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)""",
        })

    self.__method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_method(self):
    self.__method = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INLINE': {}, 'REFERENCE': {}},), is_leaf=True, yang_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)


  def _get_options(self):
    """
    Getter method for options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community/state/options (bgp-set-community-option-type)

    YANG Description: Options for modifying the community attribute with
the specified values.  These options apply to both
methods of setting the community attribute.
    """
    return self.__options
      
  def _set_options(self, v, load=False):
    """
    Setter method for options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community/state/options (bgp-set-community-option-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_options is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_options() directly.

    YANG Description: Options for modifying the community attribute with
the specified values.  These options apply to both
methods of setting the community attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ADD': {}, 'REMOVE': {}, 'REPLACE': {}},), is_leaf=True, yang_name="options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-community-option-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """options must be of a type compatible with bgp-set-community-option-type""",
          'defined-type': "openconfig-bgp-policy:bgp-set-community-option-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ADD': {}, 'REMOVE': {}, 'REPLACE': {}},), is_leaf=True, yang_name="options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-community-option-type', is_config=False)""",
        })

    self.__options = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_options(self):
    self.__options = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'ADD': {}, 'REMOVE': {}, 'REPLACE': {}},), is_leaf=True, yang_name="options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-community-option-type', is_config=False)

  method = __builtin__.property(_get_method)
  options = __builtin__.property(_get_options)


  _pyangbind_elements = OrderedDict([('method', method), ('options', options), ])


