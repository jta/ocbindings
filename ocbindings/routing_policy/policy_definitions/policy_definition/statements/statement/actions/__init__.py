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
from . import set_tag
from . import bgp_actions
from . import ospf_actions
from . import isis_actions
class actions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for policy action statements
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__set_tag','__bgp_actions','__ospf_actions','__isis_actions',)

  _yang_name = 'actions'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=False)
    self.__set_tag = YANGDynClass(base=set_tag.set_tag, is_container='container', yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__bgp_actions = YANGDynClass(base=bgp_actions.bgp_actions, is_container='container', yang_name="bgp-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__ospf_actions = YANGDynClass(base=ospf_actions.ospf_actions, is_container='container', yang_name="ospf-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ospf-policy', defining_module='openconfig-ospf-policy', yang_type='container', is_config=True)
    self.__isis_actions = YANGDynClass(base=isis_actions.isis_actions, is_container='container', yang_name="isis-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='container', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/config (container)

    YANG Description: Configuration data for policy actions
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for policy actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/state (container)

    YANG Description: Operational state data for policy actions
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for policy actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=False)


  def _get_set_tag(self):
    """
    Getter method for set_tag, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag (container)

    YANG Description: Policy actions associated with setting tags for a particular
route. A tag is an abstract entity which can be mapped to underlying
protocol attributes where applicable.
    """
    return self.__set_tag
      
  def _set_set_tag(self, v, load=False):
    """
    Setter method for set_tag, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_tag() directly.

    YANG Description: Policy actions associated with setting tags for a particular
route. A tag is an abstract entity which can be mapped to underlying
protocol attributes where applicable.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_tag.set_tag, is_container='container', yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_tag must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_tag.set_tag, is_container='container', yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__set_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_tag(self):
    self.__set_tag = YANGDynClass(base=set_tag.set_tag, is_container='container', yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_bgp_actions(self):
    """
    Getter method for bgp_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions (container)

    YANG Description: Top-level container for BGP-specific actions
    """
    return self.__bgp_actions
      
  def _set_bgp_actions(self, v, load=False):
    """
    Setter method for bgp_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bgp_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bgp_actions() directly.

    YANG Description: Top-level container for BGP-specific actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bgp_actions.bgp_actions, is_container='container', yang_name="bgp-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bgp_actions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bgp_actions.bgp_actions, is_container='container', yang_name="bgp-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__bgp_actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bgp_actions(self):
    self.__bgp_actions = YANGDynClass(base=bgp_actions.bgp_actions, is_container='container', yang_name="bgp-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_ospf_actions(self):
    """
    Getter method for ospf_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/ospf_actions (container)

    YANG Description: Actions specific to OSPF
    """
    return self.__ospf_actions
      
  def _set_ospf_actions(self, v, load=False):
    """
    Setter method for ospf_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/ospf_actions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_actions() directly.

    YANG Description: Actions specific to OSPF
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ospf_actions.ospf_actions, is_container='container', yang_name="ospf-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ospf-policy', defining_module='openconfig-ospf-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_actions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ospf_actions.ospf_actions, is_container='container', yang_name="ospf-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ospf-policy', defining_module='openconfig-ospf-policy', yang_type='container', is_config=True)""",
        })

    self.__ospf_actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_actions(self):
    self.__ospf_actions = YANGDynClass(base=ospf_actions.ospf_actions, is_container='container', yang_name="ospf-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ospf-policy', defining_module='openconfig-ospf-policy', yang_type='container', is_config=True)


  def _get_isis_actions(self):
    """
    Getter method for isis_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions (container)

    YANG Description: Actions that can be performed by IS-IS within a policy
    """
    return self.__isis_actions
      
  def _set_isis_actions(self, v, load=False):
    """
    Setter method for isis_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_actions() directly.

    YANG Description: Actions that can be performed by IS-IS within a policy
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=isis_actions.isis_actions, is_container='container', yang_name="isis-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_actions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=isis_actions.isis_actions, is_container='container', yang_name="isis-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='container', is_config=True)""",
        })

    self.__isis_actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_actions(self):
    self.__isis_actions = YANGDynClass(base=isis_actions.isis_actions, is_container='container', yang_name="isis-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  set_tag = __builtin__.property(_get_set_tag, _set_set_tag)
  bgp_actions = __builtin__.property(_get_bgp_actions, _set_bgp_actions)
  ospf_actions = __builtin__.property(_get_ospf_actions, _set_ospf_actions)
  isis_actions = __builtin__.property(_get_isis_actions, _set_isis_actions)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('set_tag', set_tag), ('bgp_actions', bgp_actions), ('ospf_actions', ospf_actions), ('isis_actions', isis_actions), ])


from . import config
from . import state
from . import set_tag
from . import bgp_actions
from . import ospf_actions
from . import isis_actions
class actions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for policy action statements
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__set_tag','__bgp_actions','__ospf_actions','__isis_actions',)

  _yang_name = 'actions'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=False)
    self.__set_tag = YANGDynClass(base=set_tag.set_tag, is_container='container', yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__bgp_actions = YANGDynClass(base=bgp_actions.bgp_actions, is_container='container', yang_name="bgp-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__ospf_actions = YANGDynClass(base=ospf_actions.ospf_actions, is_container='container', yang_name="ospf-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ospf-policy', defining_module='openconfig-ospf-policy', yang_type='container', is_config=True)
    self.__isis_actions = YANGDynClass(base=isis_actions.isis_actions, is_container='container', yang_name="isis-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='container', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/config (container)

    YANG Description: Configuration data for policy actions
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for policy actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/state (container)

    YANG Description: Operational state data for policy actions
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for policy actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=False)


  def _get_set_tag(self):
    """
    Getter method for set_tag, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag (container)

    YANG Description: Policy actions associated with setting tags for a particular
route. A tag is an abstract entity which can be mapped to underlying
protocol attributes where applicable.
    """
    return self.__set_tag
      
  def _set_set_tag(self, v, load=False):
    """
    Setter method for set_tag, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_tag() directly.

    YANG Description: Policy actions associated with setting tags for a particular
route. A tag is an abstract entity which can be mapped to underlying
protocol attributes where applicable.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_tag.set_tag, is_container='container', yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_tag must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_tag.set_tag, is_container='container', yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__set_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_tag(self):
    self.__set_tag = YANGDynClass(base=set_tag.set_tag, is_container='container', yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_bgp_actions(self):
    """
    Getter method for bgp_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions (container)

    YANG Description: Top-level container for BGP-specific actions
    """
    return self.__bgp_actions
      
  def _set_bgp_actions(self, v, load=False):
    """
    Setter method for bgp_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bgp_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bgp_actions() directly.

    YANG Description: Top-level container for BGP-specific actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bgp_actions.bgp_actions, is_container='container', yang_name="bgp-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bgp_actions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bgp_actions.bgp_actions, is_container='container', yang_name="bgp-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__bgp_actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bgp_actions(self):
    self.__bgp_actions = YANGDynClass(base=bgp_actions.bgp_actions, is_container='container', yang_name="bgp-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_ospf_actions(self):
    """
    Getter method for ospf_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/ospf_actions (container)

    YANG Description: Actions specific to OSPF
    """
    return self.__ospf_actions
      
  def _set_ospf_actions(self, v, load=False):
    """
    Setter method for ospf_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/ospf_actions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_actions() directly.

    YANG Description: Actions specific to OSPF
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ospf_actions.ospf_actions, is_container='container', yang_name="ospf-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ospf-policy', defining_module='openconfig-ospf-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_actions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ospf_actions.ospf_actions, is_container='container', yang_name="ospf-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ospf-policy', defining_module='openconfig-ospf-policy', yang_type='container', is_config=True)""",
        })

    self.__ospf_actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_actions(self):
    self.__ospf_actions = YANGDynClass(base=ospf_actions.ospf_actions, is_container='container', yang_name="ospf-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ospf-policy', defining_module='openconfig-ospf-policy', yang_type='container', is_config=True)


  def _get_isis_actions(self):
    """
    Getter method for isis_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions (container)

    YANG Description: Actions that can be performed by IS-IS within a policy
    """
    return self.__isis_actions
      
  def _set_isis_actions(self, v, load=False):
    """
    Setter method for isis_actions, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/isis_actions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_actions() directly.

    YANG Description: Actions that can be performed by IS-IS within a policy
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=isis_actions.isis_actions, is_container='container', yang_name="isis-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_actions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=isis_actions.isis_actions, is_container='container', yang_name="isis-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='container', is_config=True)""",
        })

    self.__isis_actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_actions(self):
    self.__isis_actions = YANGDynClass(base=isis_actions.isis_actions, is_container='container', yang_name="isis-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-isis-policy', defining_module='openconfig-isis-policy', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  set_tag = __builtin__.property(_get_set_tag, _set_set_tag)
  bgp_actions = __builtin__.property(_get_bgp_actions, _set_bgp_actions)
  ospf_actions = __builtin__.property(_get_ospf_actions, _set_ospf_actions)
  isis_actions = __builtin__.property(_get_isis_actions, _set_isis_actions)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('set_tag', set_tag), ('bgp_actions', bgp_actions), ('ospf_actions', ospf_actions), ('isis_actions', isis_actions), ])


