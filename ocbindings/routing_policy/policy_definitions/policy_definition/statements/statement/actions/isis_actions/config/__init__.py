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
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/isis-actions/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to IS-IS actions
  """
  __slots__ = ('_path_helper', '_extmethods', '__set_level','__set_metric_type','__set_metric_style_type','__set_metric',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__set_level = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..2']}), is_leaf=True, yang_name="set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:level-number', is_config=True)
    self.__set_metric_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}, 'EXTERNAL': {}},), is_leaf=True, yang_name="set-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-type', is_config=True)
    self.__set_metric_style_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NARROW_METRIC': {}, 'WIDE_METRIC': {}},), is_leaf=True, yang_name="set-metric-style-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-style', is_config=True)
    self.__set_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..16777215']}), is_leaf=True, yang_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:wide-metric', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions', 'isis-actions', 'config']

  def _get_set_level(self):
    """
    Getter method for set_level, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_level (isis-types:level-number)

    YANG Description: Set the level that a prefix is to be imported into.
    """
    return self.__set_level
      
  def _set_set_level(self, v, load=False):
    """
    Setter method for set_level, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_level (isis-types:level-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_level() directly.

    YANG Description: Set the level that a prefix is to be imported into.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..2']}), is_leaf=True, yang_name="set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:level-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_level must be of a type compatible with isis-types:level-number""",
          'defined-type': "isis-types:level-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..2']}), is_leaf=True, yang_name="set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:level-number', is_config=True)""",
        })

    self.__set_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_level(self):
    self.__set_level = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..2']}), is_leaf=True, yang_name="set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:level-number', is_config=True)


  def _get_set_metric_type(self):
    """
    Getter method for set_metric_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric_type (isis-types:metric-type)

    YANG Description: This leaf sets the type of metric that is to be specified
when the set-metric leaf is specified
    """
    return self.__set_metric_type
      
  def _set_set_metric_type(self, v, load=False):
    """
    Setter method for set_metric_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric_type (isis-types:metric-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_metric_type() directly.

    YANG Description: This leaf sets the type of metric that is to be specified
when the set-metric leaf is specified
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}, 'EXTERNAL': {}},), is_leaf=True, yang_name="set-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_metric_type must be of a type compatible with isis-types:metric-type""",
          'defined-type': "isis-types:metric-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}, 'EXTERNAL': {}},), is_leaf=True, yang_name="set-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-type', is_config=True)""",
        })

    self.__set_metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_metric_type(self):
    self.__set_metric_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}, 'EXTERNAL': {}},), is_leaf=True, yang_name="set-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-type', is_config=True)


  def _get_set_metric_style_type(self):
    """
    Getter method for set_metric_style_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric_style_type (isis-types:metric-style)

    YANG Description: Set the style of the metric
    """
    return self.__set_metric_style_type
      
  def _set_set_metric_style_type(self, v, load=False):
    """
    Setter method for set_metric_style_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric_style_type (isis-types:metric-style)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_metric_style_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_metric_style_type() directly.

    YANG Description: Set the style of the metric
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NARROW_METRIC': {}, 'WIDE_METRIC': {}},), is_leaf=True, yang_name="set-metric-style-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-style', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_metric_style_type must be of a type compatible with isis-types:metric-style""",
          'defined-type': "isis-types:metric-style",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NARROW_METRIC': {}, 'WIDE_METRIC': {}},), is_leaf=True, yang_name="set-metric-style-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-style', is_config=True)""",
        })

    self.__set_metric_style_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_metric_style_type(self):
    self.__set_metric_style_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NARROW_METRIC': {}, 'WIDE_METRIC': {}},), is_leaf=True, yang_name="set-metric-style-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-style', is_config=True)


  def _get_set_metric(self):
    """
    Getter method for set_metric, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric (isis-types:wide-metric)

    YANG Description: Set the metric of the IS-IS prefix
    """
    return self.__set_metric
      
  def _set_set_metric(self, v, load=False):
    """
    Setter method for set_metric, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric (isis-types:wide-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_metric() directly.

    YANG Description: Set the metric of the IS-IS prefix
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..16777215']}), is_leaf=True, yang_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:wide-metric', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_metric must be of a type compatible with isis-types:wide-metric""",
          'defined-type': "isis-types:wide-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..16777215']}), is_leaf=True, yang_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:wide-metric', is_config=True)""",
        })

    self.__set_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_metric(self):
    self.__set_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..16777215']}), is_leaf=True, yang_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:wide-metric', is_config=True)

  set_level = __builtin__.property(_get_set_level, _set_set_level)
  set_metric_type = __builtin__.property(_get_set_metric_type, _set_set_metric_type)
  set_metric_style_type = __builtin__.property(_get_set_metric_style_type, _set_set_metric_style_type)
  set_metric = __builtin__.property(_get_set_metric, _set_set_metric)


  _pyangbind_elements = OrderedDict([('set_level', set_level), ('set_metric_type', set_metric_type), ('set_metric_style_type', set_metric_style_type), ('set_metric', set_metric), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/isis-actions/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to IS-IS actions
  """
  __slots__ = ('_path_helper', '_extmethods', '__set_level','__set_metric_type','__set_metric_style_type','__set_metric',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__set_level = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..2']}), is_leaf=True, yang_name="set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:level-number', is_config=True)
    self.__set_metric_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}, 'EXTERNAL': {}},), is_leaf=True, yang_name="set-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-type', is_config=True)
    self.__set_metric_style_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NARROW_METRIC': {}, 'WIDE_METRIC': {}},), is_leaf=True, yang_name="set-metric-style-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-style', is_config=True)
    self.__set_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..16777215']}), is_leaf=True, yang_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:wide-metric', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions', 'isis-actions', 'config']

  def _get_set_level(self):
    """
    Getter method for set_level, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_level (isis-types:level-number)

    YANG Description: Set the level that a prefix is to be imported into.
    """
    return self.__set_level
      
  def _set_set_level(self, v, load=False):
    """
    Setter method for set_level, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_level (isis-types:level-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_level() directly.

    YANG Description: Set the level that a prefix is to be imported into.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..2']}), is_leaf=True, yang_name="set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:level-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_level must be of a type compatible with isis-types:level-number""",
          'defined-type': "isis-types:level-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..2']}), is_leaf=True, yang_name="set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:level-number', is_config=True)""",
        })

    self.__set_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_level(self):
    self.__set_level = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..2']}), is_leaf=True, yang_name="set-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:level-number', is_config=True)


  def _get_set_metric_type(self):
    """
    Getter method for set_metric_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric_type (isis-types:metric-type)

    YANG Description: This leaf sets the type of metric that is to be specified
when the set-metric leaf is specified
    """
    return self.__set_metric_type
      
  def _set_set_metric_type(self, v, load=False):
    """
    Setter method for set_metric_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric_type (isis-types:metric-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_metric_type() directly.

    YANG Description: This leaf sets the type of metric that is to be specified
when the set-metric leaf is specified
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}, 'EXTERNAL': {}},), is_leaf=True, yang_name="set-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_metric_type must be of a type compatible with isis-types:metric-type""",
          'defined-type': "isis-types:metric-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}, 'EXTERNAL': {}},), is_leaf=True, yang_name="set-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-type', is_config=True)""",
        })

    self.__set_metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_metric_type(self):
    self.__set_metric_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}, 'EXTERNAL': {}},), is_leaf=True, yang_name="set-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-type', is_config=True)


  def _get_set_metric_style_type(self):
    """
    Getter method for set_metric_style_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric_style_type (isis-types:metric-style)

    YANG Description: Set the style of the metric
    """
    return self.__set_metric_style_type
      
  def _set_set_metric_style_type(self, v, load=False):
    """
    Setter method for set_metric_style_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric_style_type (isis-types:metric-style)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_metric_style_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_metric_style_type() directly.

    YANG Description: Set the style of the metric
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NARROW_METRIC': {}, 'WIDE_METRIC': {}},), is_leaf=True, yang_name="set-metric-style-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-style', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_metric_style_type must be of a type compatible with isis-types:metric-style""",
          'defined-type': "isis-types:metric-style",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NARROW_METRIC': {}, 'WIDE_METRIC': {}},), is_leaf=True, yang_name="set-metric-style-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-style', is_config=True)""",
        })

    self.__set_metric_style_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_metric_style_type(self):
    self.__set_metric_style_type = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NARROW_METRIC': {}, 'WIDE_METRIC': {}},), is_leaf=True, yang_name="set-metric-style-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:metric-style', is_config=True)


  def _get_set_metric(self):
    """
    Getter method for set_metric, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric (isis-types:wide-metric)

    YANG Description: Set the metric of the IS-IS prefix
    """
    return self.__set_metric
      
  def _set_set_metric(self, v, load=False):
    """
    Setter method for set_metric, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions/config/set_metric (isis-types:wide-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_metric() directly.

    YANG Description: Set the metric of the IS-IS prefix
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..16777215']}), is_leaf=True, yang_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:wide-metric', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_metric must be of a type compatible with isis-types:wide-metric""",
          'defined-type': "isis-types:wide-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..16777215']}), is_leaf=True, yang_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:wide-metric', is_config=True)""",
        })

    self.__set_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_metric(self):
    self.__set_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..16777215']}), is_leaf=True, yang_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='isis-types:wide-metric', is_config=True)

  set_level = __builtin__.property(_get_set_level, _set_set_level)
  set_metric_type = __builtin__.property(_get_set_metric_type, _set_set_metric_type)
  set_metric_style_type = __builtin__.property(_get_set_metric_style_type, _set_set_metric_style_type)
  set_metric = __builtin__.property(_get_set_metric, _set_set_metric)


  _pyangbind_elements = OrderedDict([('set_level', set_level), ('set_metric_type', set_metric_type), ('set_metric_style_type', set_metric_style_type), ('set_metric', set_metric), ])


