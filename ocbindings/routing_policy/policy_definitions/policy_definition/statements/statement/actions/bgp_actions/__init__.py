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
from . import config
from . import state
from . import set_as_path_prepend
from . import set_community
from . import set_ext_community
class bgp_actions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/bgp-actions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for BGP-specific actions
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__set_as_path_prepend','__set_community','__set_ext_community',)

  _yang_name = 'bgp-actions'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=False)
    self.__set_as_path_prepend = YANGDynClass(base=set_as_path_prepend.set_as_path_prepend, is_container='container', yang_name="set-as-path-prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__set_community = YANGDynClass(base=set_community.set_community, is_container='container', yang_name="set-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__set_ext_community = YANGDynClass(base=set_ext_community.set_ext_community, is_container='container', yang_name="set-ext-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions', 'bgp-actions']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config (container)

    YANG Description: Configuration data for BGP-specific actions
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for BGP-specific actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/state (container)

    YANG Description: Operational state data for BGP-specific actions
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for BGP-specific actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=False)


  def _get_set_as_path_prepend(self):
    """
    Getter method for set_as_path_prepend, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_as_path_prepend (container)

    YANG Description: Action to prepend the specified AS number to the AS-path a
specified number of times
    """
    return self.__set_as_path_prepend
      
  def _set_set_as_path_prepend(self, v, load=False):
    """
    Setter method for set_as_path_prepend, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_as_path_prepend (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_as_path_prepend is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_as_path_prepend() directly.

    YANG Description: Action to prepend the specified AS number to the AS-path a
specified number of times
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_as_path_prepend.set_as_path_prepend, is_container='container', yang_name="set-as-path-prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_as_path_prepend must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_as_path_prepend.set_as_path_prepend, is_container='container', yang_name="set-as-path-prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__set_as_path_prepend = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_as_path_prepend(self):
    self.__set_as_path_prepend = YANGDynClass(base=set_as_path_prepend.set_as_path_prepend, is_container='container', yang_name="set-as-path-prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_set_community(self):
    """
    Getter method for set_community, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community (container)

    YANG Description: Action to set the community attributes of the route, along
with options to modify how the community is modified.
Communities may be set using an inline list OR
reference to an existing defined set (not both).
    """
    return self.__set_community
      
  def _set_set_community(self, v, load=False):
    """
    Setter method for set_community, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_community() directly.

    YANG Description: Action to set the community attributes of the route, along
with options to modify how the community is modified.
Communities may be set using an inline list OR
reference to an existing defined set (not both).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_community.set_community, is_container='container', yang_name="set-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_community must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_community.set_community, is_container='container', yang_name="set-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__set_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_community(self):
    self.__set_community = YANGDynClass(base=set_community.set_community, is_container='container', yang_name="set-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_set_ext_community(self):
    """
    Getter method for set_ext_community, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_ext_community (container)

    YANG Description: Action to set the extended community attributes of the
route, along with options to modify how the community is
modified. Extended communities may be set using an inline
list OR a reference to an existing defined set (but not
both).
    """
    return self.__set_ext_community
      
  def _set_set_ext_community(self, v, load=False):
    """
    Setter method for set_ext_community, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_ext_community (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_ext_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_ext_community() directly.

    YANG Description: Action to set the extended community attributes of the
route, along with options to modify how the community is
modified. Extended communities may be set using an inline
list OR a reference to an existing defined set (but not
both).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_ext_community.set_ext_community, is_container='container', yang_name="set-ext-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_ext_community must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_ext_community.set_ext_community, is_container='container', yang_name="set-ext-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__set_ext_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_ext_community(self):
    self.__set_ext_community = YANGDynClass(base=set_ext_community.set_ext_community, is_container='container', yang_name="set-ext-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  set_as_path_prepend = __builtin__.property(_get_set_as_path_prepend, _set_set_as_path_prepend)
  set_community = __builtin__.property(_get_set_community, _set_set_community)
  set_ext_community = __builtin__.property(_get_set_ext_community, _set_set_ext_community)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('set_as_path_prepend', set_as_path_prepend), ('set_community', set_community), ('set_ext_community', set_ext_community), ])


from . import config
from . import state
from . import set_as_path_prepend
from . import set_community
from . import set_ext_community
class bgp_actions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/bgp-actions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for BGP-specific actions
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__set_as_path_prepend','__set_community','__set_ext_community',)

  _yang_name = 'bgp-actions'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=False)
    self.__set_as_path_prepend = YANGDynClass(base=set_as_path_prepend.set_as_path_prepend, is_container='container', yang_name="set-as-path-prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__set_community = YANGDynClass(base=set_community.set_community, is_container='container', yang_name="set-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__set_ext_community = YANGDynClass(base=set_ext_community.set_ext_community, is_container='container', yang_name="set-ext-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions', 'bgp-actions']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config (container)

    YANG Description: Configuration data for BGP-specific actions
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for BGP-specific actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/state (container)

    YANG Description: Operational state data for BGP-specific actions
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for BGP-specific actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=False)


  def _get_set_as_path_prepend(self):
    """
    Getter method for set_as_path_prepend, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_as_path_prepend (container)

    YANG Description: Action to prepend the specified AS number to the AS-path a
specified number of times
    """
    return self.__set_as_path_prepend
      
  def _set_set_as_path_prepend(self, v, load=False):
    """
    Setter method for set_as_path_prepend, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_as_path_prepend (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_as_path_prepend is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_as_path_prepend() directly.

    YANG Description: Action to prepend the specified AS number to the AS-path a
specified number of times
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_as_path_prepend.set_as_path_prepend, is_container='container', yang_name="set-as-path-prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_as_path_prepend must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_as_path_prepend.set_as_path_prepend, is_container='container', yang_name="set-as-path-prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__set_as_path_prepend = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_as_path_prepend(self):
    self.__set_as_path_prepend = YANGDynClass(base=set_as_path_prepend.set_as_path_prepend, is_container='container', yang_name="set-as-path-prepend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_set_community(self):
    """
    Getter method for set_community, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community (container)

    YANG Description: Action to set the community attributes of the route, along
with options to modify how the community is modified.
Communities may be set using an inline list OR
reference to an existing defined set (not both).
    """
    return self.__set_community
      
  def _set_set_community(self, v, load=False):
    """
    Setter method for set_community, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_community (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_community() directly.

    YANG Description: Action to set the community attributes of the route, along
with options to modify how the community is modified.
Communities may be set using an inline list OR
reference to an existing defined set (not both).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_community.set_community, is_container='container', yang_name="set-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_community must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_community.set_community, is_container='container', yang_name="set-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__set_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_community(self):
    self.__set_community = YANGDynClass(base=set_community.set_community, is_container='container', yang_name="set-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_set_ext_community(self):
    """
    Getter method for set_ext_community, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_ext_community (container)

    YANG Description: Action to set the extended community attributes of the
route, along with options to modify how the community is
modified. Extended communities may be set using an inline
list OR a reference to an existing defined set (but not
both).
    """
    return self.__set_ext_community
      
  def _set_set_ext_community(self, v, load=False):
    """
    Setter method for set_ext_community, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/set_ext_community (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_ext_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_ext_community() directly.

    YANG Description: Action to set the extended community attributes of the
route, along with options to modify how the community is
modified. Extended communities may be set using an inline
list OR a reference to an existing defined set (but not
both).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_ext_community.set_ext_community, is_container='container', yang_name="set-ext-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_ext_community must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_ext_community.set_ext_community, is_container='container', yang_name="set-ext-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__set_ext_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_ext_community(self):
    self.__set_ext_community = YANGDynClass(base=set_ext_community.set_ext_community, is_container='container', yang_name="set-ext-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  set_as_path_prepend = __builtin__.property(_get_set_as_path_prepend, _set_set_as_path_prepend)
  set_community = __builtin__.property(_get_set_community, _set_set_community)
  set_ext_community = __builtin__.property(_get_set_ext_community, _set_set_ext_community)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('set_as_path_prepend', set_as_path_prepend), ('set_community', set_community), ('set_ext_community', set_ext_community), ])


