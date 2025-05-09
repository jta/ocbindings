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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/tunnel/ipv4/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level IPv4 configuration data for the interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__mtu','__gratuitous_arp_accepted','__dhcp_client',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['68..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='uint16', is_config=True)
    self.__gratuitous_arp_accepted = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="gratuitous-arp-accepted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    self.__dhcp_client = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)

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
      return ['interfaces', 'interface', 'tunnel', 'ipv4', 'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/enabled (boolean)

    YANG Description: Controls whether IPv4 is enabled or disabled on this
interface.  When IPv4 is enabled, this interface is
connected to an IPv4 stack, and the interface can send
and receive IPv4 packets.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Controls whether IPv4 is enabled or disabled on this
interface.  When IPv4 is enabled, this interface is
connected to an IPv4 stack, and the interface can send
and receive IPv4 packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)


  def _get_mtu(self):
    """
    Getter method for mtu, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/mtu (uint16)

    YANG Description: The size, in octets, of the largest IPv4 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
    return self.__mtu
      
  def _set_mtu(self, v, load=False):
    """
    Setter method for mtu, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/mtu (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu() directly.

    YANG Description: The size, in octets, of the largest IPv4 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['68..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['68..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='uint16', is_config=True)""",
        })

    self.__mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu(self):
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['68..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='uint16', is_config=True)


  def _get_gratuitous_arp_accepted(self):
    """
    Getter method for gratuitous_arp_accepted, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/gratuitous_arp_accepted (boolean)

    YANG Description: When set to true, gratuitous ARPs will be accepted and
the ARP table will be updated.
    """
    return self.__gratuitous_arp_accepted
      
  def _set_gratuitous_arp_accepted(self, v, load=False):
    """
    Setter method for gratuitous_arp_accepted, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/gratuitous_arp_accepted (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gratuitous_arp_accepted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gratuitous_arp_accepted() directly.

    YANG Description: When set to true, gratuitous ARPs will be accepted and
the ARP table will be updated.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="gratuitous-arp-accepted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gratuitous_arp_accepted must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="gratuitous-arp-accepted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)""",
        })

    self.__gratuitous_arp_accepted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gratuitous_arp_accepted(self):
    self.__gratuitous_arp_accepted = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="gratuitous-arp-accepted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)


  def _get_dhcp_client(self):
    """
    Getter method for dhcp_client, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/dhcp_client (boolean)

    YANG Description: Enables a DHCP client on the interface in order to request
an address
    """
    return self.__dhcp_client
      
  def _set_dhcp_client(self, v, load=False):
    """
    Setter method for dhcp_client, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/dhcp_client (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dhcp_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dhcp_client() directly.

    YANG Description: Enables a DHCP client on the interface in order to request
an address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dhcp_client must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)""",
        })

    self.__dhcp_client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dhcp_client(self):
    self.__dhcp_client = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  mtu = __builtin__.property(_get_mtu, _set_mtu)
  gratuitous_arp_accepted = __builtin__.property(_get_gratuitous_arp_accepted, _set_gratuitous_arp_accepted)
  dhcp_client = __builtin__.property(_get_dhcp_client, _set_dhcp_client)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('mtu', mtu), ('gratuitous_arp_accepted', gratuitous_arp_accepted), ('dhcp_client', dhcp_client), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/tunnel/ipv4/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level IPv4 configuration data for the interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__mtu','__gratuitous_arp_accepted','__dhcp_client',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['68..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='uint16', is_config=True)
    self.__gratuitous_arp_accepted = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="gratuitous-arp-accepted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    self.__dhcp_client = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)

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
      return ['interfaces', 'interface', 'tunnel', 'ipv4', 'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/enabled (boolean)

    YANG Description: Controls whether IPv4 is enabled or disabled on this
interface.  When IPv4 is enabled, this interface is
connected to an IPv4 stack, and the interface can send
and receive IPv4 packets.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Controls whether IPv4 is enabled or disabled on this
interface.  When IPv4 is enabled, this interface is
connected to an IPv4 stack, and the interface can send
and receive IPv4 packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)


  def _get_mtu(self):
    """
    Getter method for mtu, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/mtu (uint16)

    YANG Description: The size, in octets, of the largest IPv4 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
    return self.__mtu
      
  def _set_mtu(self, v, load=False):
    """
    Setter method for mtu, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/mtu (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu() directly.

    YANG Description: The size, in octets, of the largest IPv4 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['68..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['68..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='uint16', is_config=True)""",
        })

    self.__mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu(self):
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['68..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='uint16', is_config=True)


  def _get_gratuitous_arp_accepted(self):
    """
    Getter method for gratuitous_arp_accepted, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/gratuitous_arp_accepted (boolean)

    YANG Description: When set to true, gratuitous ARPs will be accepted and
the ARP table will be updated.
    """
    return self.__gratuitous_arp_accepted
      
  def _set_gratuitous_arp_accepted(self, v, load=False):
    """
    Setter method for gratuitous_arp_accepted, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/gratuitous_arp_accepted (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gratuitous_arp_accepted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gratuitous_arp_accepted() directly.

    YANG Description: When set to true, gratuitous ARPs will be accepted and
the ARP table will be updated.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="gratuitous-arp-accepted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gratuitous_arp_accepted must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="gratuitous-arp-accepted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)""",
        })

    self.__gratuitous_arp_accepted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gratuitous_arp_accepted(self):
    self.__gratuitous_arp_accepted = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="gratuitous-arp-accepted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)


  def _get_dhcp_client(self):
    """
    Getter method for dhcp_client, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/dhcp_client (boolean)

    YANG Description: Enables a DHCP client on the interface in order to request
an address
    """
    return self.__dhcp_client
      
  def _set_dhcp_client(self, v, load=False):
    """
    Setter method for dhcp_client, mapped from YANG variable /interfaces/interface/tunnel/ipv4/config/dhcp_client (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dhcp_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dhcp_client() directly.

    YANG Description: Enables a DHCP client on the interface in order to request
an address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dhcp_client must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)""",
        })

    self.__dhcp_client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dhcp_client(self):
    self.__dhcp_client = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  mtu = __builtin__.property(_get_mtu, _set_mtu)
  gratuitous_arp_accepted = __builtin__.property(_get_gratuitous_arp_accepted, _set_gratuitous_arp_accepted)
  dhcp_client = __builtin__.property(_get_dhcp_client, _set_dhcp_client)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('mtu', mtu), ('gratuitous_arp_accepted', gratuitous_arp_accepted), ('dhcp_client', dhcp_client), ])


