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
from . import dot1x_vlan_map
class switched_vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/ethernet/switched-vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for VLAN interface-specific
data on Ethernet interfaces.  These are for standard
L2, switched-style VLANs.
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__dot1x_vlan_map',)

  _yang_name = 'switched-vlan'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)
    self.__dot1x_vlan_map = YANGDynClass(base=dot1x_vlan_map.dot1x_vlan_map, is_container='container', yang_name="dot1x-vlan-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'ethernet', 'switched-vlan']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/config (container)

    YANG Description: Configuration parameters for VLANs
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters for VLANs
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
    Getter method for state, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/state (container)

    YANG Description: State variables for VLANs
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State variables for VLANs
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


  def _get_dot1x_vlan_map(self):
    """
    Getter method for dot1x_vlan_map, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map (container)

    YANG Description: Enclosing container for mapping a VLAN name to VLAN id
    """
    return self.__dot1x_vlan_map
      
  def _set_dot1x_vlan_map(self, v, load=False):
    """
    Setter method for dot1x_vlan_map, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot1x_vlan_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot1x_vlan_map() directly.

    YANG Description: Enclosing container for mapping a VLAN name to VLAN id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dot1x_vlan_map.dot1x_vlan_map, is_container='container', yang_name="dot1x-vlan-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot1x_vlan_map must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dot1x_vlan_map.dot1x_vlan_map, is_container='container', yang_name="dot1x-vlan-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__dot1x_vlan_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot1x_vlan_map(self):
    self.__dot1x_vlan_map = YANGDynClass(base=dot1x_vlan_map.dot1x_vlan_map, is_container='container', yang_name="dot1x-vlan-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  dot1x_vlan_map = __builtin__.property(_get_dot1x_vlan_map, _set_dot1x_vlan_map)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('dot1x_vlan_map', dot1x_vlan_map), ])


from . import config
from . import state
from . import dot1x_vlan_map
class switched_vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/ethernet/switched-vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for VLAN interface-specific
data on Ethernet interfaces.  These are for standard
L2, switched-style VLANs.
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__dot1x_vlan_map',)

  _yang_name = 'switched-vlan'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=False)
    self.__dot1x_vlan_map = YANGDynClass(base=dot1x_vlan_map.dot1x_vlan_map, is_container='container', yang_name="dot1x-vlan-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'ethernet', 'switched-vlan']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/config (container)

    YANG Description: Configuration parameters for VLANs
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters for VLANs
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
    Getter method for state, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/state (container)

    YANG Description: State variables for VLANs
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State variables for VLANs
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


  def _get_dot1x_vlan_map(self):
    """
    Getter method for dot1x_vlan_map, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map (container)

    YANG Description: Enclosing container for mapping a VLAN name to VLAN id
    """
    return self.__dot1x_vlan_map
      
  def _set_dot1x_vlan_map(self, v, load=False):
    """
    Setter method for dot1x_vlan_map, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot1x_vlan_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot1x_vlan_map() directly.

    YANG Description: Enclosing container for mapping a VLAN name to VLAN id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dot1x_vlan_map.dot1x_vlan_map, is_container='container', yang_name="dot1x-vlan-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot1x_vlan_map must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dot1x_vlan_map.dot1x_vlan_map, is_container='container', yang_name="dot1x-vlan-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__dot1x_vlan_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot1x_vlan_map(self):
    self.__dot1x_vlan_map = YANGDynClass(base=dot1x_vlan_map.dot1x_vlan_map, is_container='container', yang_name="dot1x-vlan-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  dot1x_vlan_map = __builtin__.property(_get_dot1x_vlan_map, _set_dot1x_vlan_map)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('dot1x_vlan_map', dot1x_vlan_map), ])


