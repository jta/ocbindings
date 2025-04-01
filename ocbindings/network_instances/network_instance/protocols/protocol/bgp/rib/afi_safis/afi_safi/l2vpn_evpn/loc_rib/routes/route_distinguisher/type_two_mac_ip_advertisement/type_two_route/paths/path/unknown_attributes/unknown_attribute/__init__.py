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
class unknown_attribute(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/l2vpn-evpn/loc-rib/routes/route-distinguisher/type-two-mac-ip-advertisement/type-two-route/paths/path/unknown-attributes/unknown-attribute. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This list contains received attributes that are unrecognized
or unsupported by the local router.  The list may be empty.
  """
  __slots__ = ('_path_helper', '_extmethods', '__attr_type','__state',)

  _yang_name = 'unknown-attribute'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attr_type = YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'l2vpn-evpn', 'loc-rib', 'routes', 'route-distinguisher', 'type-two-mac-ip-advertisement', 'type-two-route', 'paths', 'path', 'unknown-attributes', 'unknown-attribute']

  def _get_attr_type(self):
    """
    Getter method for attr_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/attr_type (leafref)

    YANG Description: Reference to the list key
    """
    return self.__attr_type
      
  def _set_attr_type(self, v, load=False):
    """
    Setter method for attr_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/attr_type (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr_type() directly.

    YANG Description: Reference to the list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr_type must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__attr_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr_type(self):
    self.__attr_type = YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/state (container)

    YANG Description: Operational state for unknown route attributes
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state for unknown route attributes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  attr_type = __builtin__.property(_get_attr_type)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('attr_type', attr_type), ('state', state), ])


from . import state
class unknown_attribute(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/l2vpn-evpn/loc-rib/routes/route-distinguisher/type-two-mac-ip-advertisement/type-two-route/paths/path/unknown-attributes/unknown-attribute. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This list contains received attributes that are unrecognized
or unsupported by the local router.  The list may be empty.
  """
  __slots__ = ('_path_helper', '_extmethods', '__attr_type','__state',)

  _yang_name = 'unknown-attribute'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attr_type = YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'l2vpn-evpn', 'loc-rib', 'routes', 'route-distinguisher', 'type-two-mac-ip-advertisement', 'type-two-route', 'paths', 'path', 'unknown-attributes', 'unknown-attribute']

  def _get_attr_type(self):
    """
    Getter method for attr_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/attr_type (leafref)

    YANG Description: Reference to the list key
    """
    return self.__attr_type
      
  def _set_attr_type(self, v, load=False):
    """
    Setter method for attr_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/attr_type (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr_type() directly.

    YANG Description: Reference to the list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr_type must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__attr_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr_type(self):
    self.__attr_type = YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/state (container)

    YANG Description: Operational state for unknown route attributes
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state for unknown route attributes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  attr_type = __builtin__.property(_get_attr_type)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('attr_type', attr_type), ('state', state), ])


from . import state
class unknown_attribute(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/l2vpn-evpn/loc-rib/routes/route-distinguisher/type-two-mac-ip-advertisement/type-two-route/paths/path/unknown-attributes/unknown-attribute. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This list contains received attributes that are unrecognized
or unsupported by the local router.  The list may be empty.
  """
  __slots__ = ('_path_helper', '_extmethods', '__attr_type','__state',)

  _yang_name = 'unknown-attribute'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attr_type = YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'l2vpn-evpn', 'loc-rib', 'routes', 'route-distinguisher', 'type-two-mac-ip-advertisement', 'type-two-route', 'paths', 'path', 'unknown-attributes', 'unknown-attribute']

  def _get_attr_type(self):
    """
    Getter method for attr_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/attr_type (leafref)

    YANG Description: Reference to the list key
    """
    return self.__attr_type
      
  def _set_attr_type(self, v, load=False):
    """
    Setter method for attr_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/attr_type (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr_type() directly.

    YANG Description: Reference to the list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr_type must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__attr_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr_type(self):
    self.__attr_type = YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/state (container)

    YANG Description: Operational state for unknown route attributes
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state for unknown route attributes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  attr_type = __builtin__.property(_get_attr_type)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('attr_type', attr_type), ('state', state), ])


from . import state
class unknown_attribute(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/l2vpn-evpn/loc-rib/routes/route-distinguisher/type-two-mac-ip-advertisement/type-two-route/paths/path/unknown-attributes/unknown-attribute. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This list contains received attributes that are unrecognized
or unsupported by the local router.  The list may be empty.
  """
  __slots__ = ('_path_helper', '_extmethods', '__attr_type','__state',)

  _yang_name = 'unknown-attribute'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attr_type = YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'l2vpn-evpn', 'loc-rib', 'routes', 'route-distinguisher', 'type-two-mac-ip-advertisement', 'type-two-route', 'paths', 'path', 'unknown-attributes', 'unknown-attribute']

  def _get_attr_type(self):
    """
    Getter method for attr_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/attr_type (leafref)

    YANG Description: Reference to the list key
    """
    return self.__attr_type
      
  def _set_attr_type(self, v, load=False):
    """
    Setter method for attr_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/attr_type (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr_type() directly.

    YANG Description: Reference to the list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr_type must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__attr_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr_type(self):
    self.__attr_type = YANGDynClass(base=str, is_leaf=True, yang_name="attr-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/state (container)

    YANG Description: Operational state for unknown route attributes
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/l2vpn_evpn/loc_rib/routes/route_distinguisher/type_two_mac_ip_advertisement/type_two_route/paths/path/unknown_attributes/unknown_attribute/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state for unknown route attributes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  attr_type = __builtin__.property(_get_attr_type)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('attr_type', attr_type), ('state', state), ])


