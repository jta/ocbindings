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
from . import state
from . import client_rf
from . import client_capabilities
from . import dot11k_neighbors
from . import client_connection
class client(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-wifi-mac - based on the path /ssids/ssid/clients/client. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of clients per BSS.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mac','__state','__client_rf','__client_capabilities','__dot11k_neighbors','__client_connection',)

  _yang_name = 'client'
  _yang_namespace = 'http://openconfig.net/yang/wifi-mac'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mac = YANGDynClass(base=str, is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    self.__client_rf = YANGDynClass(base=client_rf.client_rf, is_container='container', yang_name="client-rf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    self.__client_capabilities = YANGDynClass(base=client_capabilities.client_capabilities, is_container='container', yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    self.__dot11k_neighbors = YANGDynClass(base=dot11k_neighbors.dot11k_neighbors, is_container='container', yang_name="dot11k-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    self.__client_connection = YANGDynClass(base=client_connection.client_connection, is_container='container', yang_name="client-connection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)

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
      return ['ssids', 'ssid', 'clients', 'client']

  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /ssids/ssid/clients/client/mac (leafref)

    YANG Description: The clients WiFi MAC address.
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /ssids/ssid/clients/client/mac (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.

    YANG Description: The clients WiFi MAC address.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='leafref', is_config=False)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=str, is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /ssids/ssid/clients/client/state (container)

    YANG Description: Client state data.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /ssids/ssid/clients/client/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Client state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)


  def _get_client_rf(self):
    """
    Getter method for client_rf, mapped from YANG variable /ssids/ssid/clients/client/client_rf (container)

    YANG Description: RF radio-data per non-AP STA.
    """
    return self.__client_rf
      
  def _set_client_rf(self, v, load=False):
    """
    Setter method for client_rf, mapped from YANG variable /ssids/ssid/clients/client/client_rf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_rf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_rf() directly.

    YANG Description: RF radio-data per non-AP STA.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=client_rf.client_rf, is_container='container', yang_name="client-rf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_rf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=client_rf.client_rf, is_container='container', yang_name="client-rf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__client_rf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_rf(self):
    self.__client_rf = YANGDynClass(base=client_rf.client_rf, is_container='container', yang_name="client-rf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)


  def _get_client_capabilities(self):
    """
    Getter method for client_capabilities, mapped from YANG variable /ssids/ssid/clients/client/client_capabilities (container)

    YANG Description: Capabilites as advertised by the Client.
    """
    return self.__client_capabilities
      
  def _set_client_capabilities(self, v, load=False):
    """
    Setter method for client_capabilities, mapped from YANG variable /ssids/ssid/clients/client/client_capabilities (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_capabilities is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_capabilities() directly.

    YANG Description: Capabilites as advertised by the Client.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=client_capabilities.client_capabilities, is_container='container', yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_capabilities must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=client_capabilities.client_capabilities, is_container='container', yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__client_capabilities = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_capabilities(self):
    self.__client_capabilities = YANGDynClass(base=client_capabilities.client_capabilities, is_container='container', yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)


  def _get_dot11k_neighbors(self):
    """
    Getter method for dot11k_neighbors, mapped from YANG variable /ssids/ssid/clients/client/dot11k_neighbors (container)

    YANG Description: 80211.k nieghbor information given from the Client to
the infrastructure.
    """
    return self.__dot11k_neighbors
      
  def _set_dot11k_neighbors(self, v, load=False):
    """
    Setter method for dot11k_neighbors, mapped from YANG variable /ssids/ssid/clients/client/dot11k_neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11k_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11k_neighbors() directly.

    YANG Description: 80211.k nieghbor information given from the Client to
the infrastructure.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dot11k_neighbors.dot11k_neighbors, is_container='container', yang_name="dot11k-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11k_neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dot11k_neighbors.dot11k_neighbors, is_container='container', yang_name="dot11k-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__dot11k_neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11k_neighbors(self):
    self.__dot11k_neighbors = YANGDynClass(base=dot11k_neighbors.dot11k_neighbors, is_container='container', yang_name="dot11k-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)


  def _get_client_connection(self):
    """
    Getter method for client_connection, mapped from YANG variable /ssids/ssid/clients/client/client_connection (container)

    YANG Description: Connection-state and meta-data associated with the
Client.
    """
    return self.__client_connection
      
  def _set_client_connection(self, v, load=False):
    """
    Setter method for client_connection, mapped from YANG variable /ssids/ssid/clients/client/client_connection (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_connection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_connection() directly.

    YANG Description: Connection-state and meta-data associated with the
Client.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=client_connection.client_connection, is_container='container', yang_name="client-connection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_connection must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=client_connection.client_connection, is_container='container', yang_name="client-connection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__client_connection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_connection(self):
    self.__client_connection = YANGDynClass(base=client_connection.client_connection, is_container='container', yang_name="client-connection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)

  mac = __builtin__.property(_get_mac)
  state = __builtin__.property(_get_state)
  client_rf = __builtin__.property(_get_client_rf)
  client_capabilities = __builtin__.property(_get_client_capabilities)
  dot11k_neighbors = __builtin__.property(_get_dot11k_neighbors)
  client_connection = __builtin__.property(_get_client_connection)


  _pyangbind_elements = OrderedDict([('mac', mac), ('state', state), ('client_rf', client_rf), ('client_capabilities', client_capabilities), ('dot11k_neighbors', dot11k_neighbors), ('client_connection', client_connection), ])


from . import state
from . import client_rf
from . import client_capabilities
from . import dot11k_neighbors
from . import client_connection
class client(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-wifi-mac - based on the path /ssids/ssid/clients/client. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of clients per BSS.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mac','__state','__client_rf','__client_capabilities','__dot11k_neighbors','__client_connection',)

  _yang_name = 'client'
  _yang_namespace = 'http://openconfig.net/yang/wifi-mac'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mac = YANGDynClass(base=str, is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    self.__client_rf = YANGDynClass(base=client_rf.client_rf, is_container='container', yang_name="client-rf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    self.__client_capabilities = YANGDynClass(base=client_capabilities.client_capabilities, is_container='container', yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    self.__dot11k_neighbors = YANGDynClass(base=dot11k_neighbors.dot11k_neighbors, is_container='container', yang_name="dot11k-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    self.__client_connection = YANGDynClass(base=client_connection.client_connection, is_container='container', yang_name="client-connection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)

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
      return ['ssids', 'ssid', 'clients', 'client']

  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /ssids/ssid/clients/client/mac (leafref)

    YANG Description: The clients WiFi MAC address.
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /ssids/ssid/clients/client/mac (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.

    YANG Description: The clients WiFi MAC address.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='leafref', is_config=False)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=str, is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /ssids/ssid/clients/client/state (container)

    YANG Description: Client state data.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /ssids/ssid/clients/client/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Client state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)


  def _get_client_rf(self):
    """
    Getter method for client_rf, mapped from YANG variable /ssids/ssid/clients/client/client_rf (container)

    YANG Description: RF radio-data per non-AP STA.
    """
    return self.__client_rf
      
  def _set_client_rf(self, v, load=False):
    """
    Setter method for client_rf, mapped from YANG variable /ssids/ssid/clients/client/client_rf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_rf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_rf() directly.

    YANG Description: RF radio-data per non-AP STA.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=client_rf.client_rf, is_container='container', yang_name="client-rf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_rf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=client_rf.client_rf, is_container='container', yang_name="client-rf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__client_rf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_rf(self):
    self.__client_rf = YANGDynClass(base=client_rf.client_rf, is_container='container', yang_name="client-rf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)


  def _get_client_capabilities(self):
    """
    Getter method for client_capabilities, mapped from YANG variable /ssids/ssid/clients/client/client_capabilities (container)

    YANG Description: Capabilites as advertised by the Client.
    """
    return self.__client_capabilities
      
  def _set_client_capabilities(self, v, load=False):
    """
    Setter method for client_capabilities, mapped from YANG variable /ssids/ssid/clients/client/client_capabilities (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_capabilities is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_capabilities() directly.

    YANG Description: Capabilites as advertised by the Client.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=client_capabilities.client_capabilities, is_container='container', yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_capabilities must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=client_capabilities.client_capabilities, is_container='container', yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__client_capabilities = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_capabilities(self):
    self.__client_capabilities = YANGDynClass(base=client_capabilities.client_capabilities, is_container='container', yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)


  def _get_dot11k_neighbors(self):
    """
    Getter method for dot11k_neighbors, mapped from YANG variable /ssids/ssid/clients/client/dot11k_neighbors (container)

    YANG Description: 80211.k nieghbor information given from the Client to
the infrastructure.
    """
    return self.__dot11k_neighbors
      
  def _set_dot11k_neighbors(self, v, load=False):
    """
    Setter method for dot11k_neighbors, mapped from YANG variable /ssids/ssid/clients/client/dot11k_neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11k_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11k_neighbors() directly.

    YANG Description: 80211.k nieghbor information given from the Client to
the infrastructure.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dot11k_neighbors.dot11k_neighbors, is_container='container', yang_name="dot11k-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11k_neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dot11k_neighbors.dot11k_neighbors, is_container='container', yang_name="dot11k-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__dot11k_neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11k_neighbors(self):
    self.__dot11k_neighbors = YANGDynClass(base=dot11k_neighbors.dot11k_neighbors, is_container='container', yang_name="dot11k-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)


  def _get_client_connection(self):
    """
    Getter method for client_connection, mapped from YANG variable /ssids/ssid/clients/client/client_connection (container)

    YANG Description: Connection-state and meta-data associated with the
Client.
    """
    return self.__client_connection
      
  def _set_client_connection(self, v, load=False):
    """
    Setter method for client_connection, mapped from YANG variable /ssids/ssid/clients/client/client_connection (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_connection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_connection() directly.

    YANG Description: Connection-state and meta-data associated with the
Client.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=client_connection.client_connection, is_container='container', yang_name="client-connection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_connection must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=client_connection.client_connection, is_container='container', yang_name="client-connection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)""",
        })

    self.__client_connection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_connection(self):
    self.__client_connection = YANGDynClass(base=client_connection.client_connection, is_container='container', yang_name="client-connection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='container', is_config=False)

  mac = __builtin__.property(_get_mac)
  state = __builtin__.property(_get_state)
  client_rf = __builtin__.property(_get_client_rf)
  client_capabilities = __builtin__.property(_get_client_capabilities)
  dot11k_neighbors = __builtin__.property(_get_dot11k_neighbors)
  client_connection = __builtin__.property(_get_client_connection)


  _pyangbind_elements = OrderedDict([('mac', mac), ('state', state), ('client_rf', client_rf), ('client_capabilities', client_capabilities), ('dot11k_neighbors', dot11k_neighbors), ('client_connection', client_connection), ])


