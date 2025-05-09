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
from . import dot1x
from . import authenticated_sessions
from . import switched_vlan
from . import poe
class ethernet(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/ethernet. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for ethernet configuration
and state
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__dot1x','__authenticated_sessions','__switched_vlan','__poe',)

  _yang_name = 'ethernet'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)
    self.__dot1x = YANGDynClass(base=dot1x.dot1x, is_container='container', yang_name="dot1x", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__authenticated_sessions = YANGDynClass(base=authenticated_sessions.authenticated_sessions, is_container='container', yang_name="authenticated-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__switched_vlan = YANGDynClass(base=switched_vlan.switched_vlan, is_container='container', yang_name="switched-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__poe = YANGDynClass(base=poe.poe, is_container='container', yang_name="poe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'ethernet']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/config (container)

    YANG Description: Configuration data for ethernet interfaces
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for ethernet interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/state (container)

    YANG Description: State variables for Ethernet interfaces
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State variables for Ethernet interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)


  def _get_dot1x(self):
    """
    Getter method for dot1x, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/dot1x (container)

    YANG Description: Top level container for 802.1X configuration and
state data.
    """
    return self.__dot1x
      
  def _set_dot1x(self, v, load=False):
    """
    Setter method for dot1x, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/dot1x (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot1x is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot1x() directly.

    YANG Description: Top level container for 802.1X configuration and
state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dot1x.dot1x, is_container='container', yang_name="dot1x", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot1x must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dot1x.dot1x, is_container='container', yang_name="dot1x", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__dot1x = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot1x(self):
    self.__dot1x = YANGDynClass(base=dot1x.dot1x, is_container='container', yang_name="dot1x", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)


  def _get_authenticated_sessions(self):
    """
    Getter method for authenticated_sessions, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/authenticated_sessions (container)

    YANG Description: Top level container for authenticated sessions state data.
    """
    return self.__authenticated_sessions
      
  def _set_authenticated_sessions(self, v, load=False):
    """
    Setter method for authenticated_sessions, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/authenticated_sessions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authenticated_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authenticated_sessions() directly.

    YANG Description: Top level container for authenticated sessions state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authenticated_sessions.authenticated_sessions, is_container='container', yang_name="authenticated-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authenticated_sessions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authenticated_sessions.authenticated_sessions, is_container='container', yang_name="authenticated-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__authenticated_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authenticated_sessions(self):
    self.__authenticated_sessions = YANGDynClass(base=authenticated_sessions.authenticated_sessions, is_container='container', yang_name="authenticated-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)


  def _get_switched_vlan(self):
    """
    Getter method for switched_vlan, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan (container)

    YANG Description: Enclosing container for VLAN interface-specific
data on Ethernet interfaces.  These are for standard
L2, switched-style VLANs.
    """
    return self.__switched_vlan
      
  def _set_switched_vlan(self, v, load=False):
    """
    Setter method for switched_vlan, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switched_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switched_vlan() directly.

    YANG Description: Enclosing container for VLAN interface-specific
data on Ethernet interfaces.  These are for standard
L2, switched-style VLANs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=switched_vlan.switched_vlan, is_container='container', yang_name="switched-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switched_vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=switched_vlan.switched_vlan, is_container='container', yang_name="switched-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__switched_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switched_vlan(self):
    self.__switched_vlan = YANGDynClass(base=switched_vlan.switched_vlan, is_container='container', yang_name="switched-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)


  def _get_poe(self):
    """
    Getter method for poe, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe (container)

    YANG Description: Top-level container for PoE configuration and state data
    """
    return self.__poe
      
  def _set_poe(self, v, load=False):
    """
    Setter method for poe, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_poe is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_poe() directly.

    YANG Description: Top-level container for PoE configuration and state data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=poe.poe, is_container='container', yang_name="poe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """poe must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=poe.poe, is_container='container', yang_name="poe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__poe = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_poe(self):
    self.__poe = YANGDynClass(base=poe.poe, is_container='container', yang_name="poe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  dot1x = __builtin__.property(_get_dot1x, _set_dot1x)
  authenticated_sessions = __builtin__.property(_get_authenticated_sessions, _set_authenticated_sessions)
  switched_vlan = __builtin__.property(_get_switched_vlan, _set_switched_vlan)
  poe = __builtin__.property(_get_poe, _set_poe)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('dot1x', dot1x), ('authenticated_sessions', authenticated_sessions), ('switched_vlan', switched_vlan), ('poe', poe), ])


from . import config
from . import state
from . import dot1x
from . import authenticated_sessions
from . import switched_vlan
from . import poe
class ethernet(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/ethernet. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for ethernet configuration
and state
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__dot1x','__authenticated_sessions','__switched_vlan','__poe',)

  _yang_name = 'ethernet'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)
    self.__dot1x = YANGDynClass(base=dot1x.dot1x, is_container='container', yang_name="dot1x", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__authenticated_sessions = YANGDynClass(base=authenticated_sessions.authenticated_sessions, is_container='container', yang_name="authenticated-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__switched_vlan = YANGDynClass(base=switched_vlan.switched_vlan, is_container='container', yang_name="switched-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__poe = YANGDynClass(base=poe.poe, is_container='container', yang_name="poe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'ethernet']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/config (container)

    YANG Description: Configuration data for ethernet interfaces
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for ethernet interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/state (container)

    YANG Description: State variables for Ethernet interfaces
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State variables for Ethernet interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)


  def _get_dot1x(self):
    """
    Getter method for dot1x, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/dot1x (container)

    YANG Description: Top level container for 802.1X configuration and
state data.
    """
    return self.__dot1x
      
  def _set_dot1x(self, v, load=False):
    """
    Setter method for dot1x, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/dot1x (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot1x is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot1x() directly.

    YANG Description: Top level container for 802.1X configuration and
state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dot1x.dot1x, is_container='container', yang_name="dot1x", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot1x must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dot1x.dot1x, is_container='container', yang_name="dot1x", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__dot1x = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot1x(self):
    self.__dot1x = YANGDynClass(base=dot1x.dot1x, is_container='container', yang_name="dot1x", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)


  def _get_authenticated_sessions(self):
    """
    Getter method for authenticated_sessions, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/authenticated_sessions (container)

    YANG Description: Top level container for authenticated sessions state data.
    """
    return self.__authenticated_sessions
      
  def _set_authenticated_sessions(self, v, load=False):
    """
    Setter method for authenticated_sessions, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/authenticated_sessions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authenticated_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authenticated_sessions() directly.

    YANG Description: Top level container for authenticated sessions state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authenticated_sessions.authenticated_sessions, is_container='container', yang_name="authenticated-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authenticated_sessions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authenticated_sessions.authenticated_sessions, is_container='container', yang_name="authenticated-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__authenticated_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authenticated_sessions(self):
    self.__authenticated_sessions = YANGDynClass(base=authenticated_sessions.authenticated_sessions, is_container='container', yang_name="authenticated-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)


  def _get_switched_vlan(self):
    """
    Getter method for switched_vlan, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan (container)

    YANG Description: Enclosing container for VLAN interface-specific
data on Ethernet interfaces.  These are for standard
L2, switched-style VLANs.
    """
    return self.__switched_vlan
      
  def _set_switched_vlan(self, v, load=False):
    """
    Setter method for switched_vlan, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switched_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switched_vlan() directly.

    YANG Description: Enclosing container for VLAN interface-specific
data on Ethernet interfaces.  These are for standard
L2, switched-style VLANs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=switched_vlan.switched_vlan, is_container='container', yang_name="switched-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switched_vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=switched_vlan.switched_vlan, is_container='container', yang_name="switched-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__switched_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switched_vlan(self):
    self.__switched_vlan = YANGDynClass(base=switched_vlan.switched_vlan, is_container='container', yang_name="switched-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)


  def _get_poe(self):
    """
    Getter method for poe, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe (container)

    YANG Description: Top-level container for PoE configuration and state data
    """
    return self.__poe
      
  def _set_poe(self, v, load=False):
    """
    Setter method for poe, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_poe is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_poe() directly.

    YANG Description: Top-level container for PoE configuration and state data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=poe.poe, is_container='container', yang_name="poe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """poe must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=poe.poe, is_container='container', yang_name="poe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__poe = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_poe(self):
    self.__poe = YANGDynClass(base=poe.poe, is_container='container', yang_name="poe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  dot1x = __builtin__.property(_get_dot1x, _set_dot1x)
  authenticated_sessions = __builtin__.property(_get_authenticated_sessions, _set_authenticated_sessions)
  switched_vlan = __builtin__.property(_get_switched_vlan, _set_switched_vlan)
  poe = __builtin__.property(_get_poe, _set_poe)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('dot1x', dot1x), ('authenticated_sessions', authenticated_sessions), ('switched_vlan', switched_vlan), ('poe', poe), ])


