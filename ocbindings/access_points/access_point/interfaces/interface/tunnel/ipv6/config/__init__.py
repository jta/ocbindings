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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/tunnel/ipv6/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level config data for the IPv6 interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__mtu','__dup_addr_detect_transmits','__learn_unsolicited','__dhcp_client',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    self.__dup_addr_detect_transmits = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    self.__learn_unsolicited = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NONE': {'value': 0}, 'GLOBAL': {'value': 1}, 'LINK_LOCAL': {'value': 2}, 'BOTH': {'value': 3}},), default=str("NONE"), is_leaf=True, yang_name="learn-unsolicited", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)
    self.__dhcp_client = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'tunnel', 'ipv6', 'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/enabled (boolean)

    YANG Description: Controls whether IPv6 is enabled or disabled on this
interface.  When IPv6 is enabled, this interface is
connected to an IPv6 stack, and the interface can send
and receive IPv6 packets.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Controls whether IPv6 is enabled or disabled on this
interface.  When IPv6 is enabled, this interface is
connected to an IPv6 stack, and the interface can send
and receive IPv6 packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)


  def _get_mtu(self):
    """
    Getter method for mtu, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/mtu (uint32)

    YANG Description: The size, in octets, of the largest IPv6 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
    return self.__mtu
      
  def _set_mtu(self, v, load=False):
    """
    Setter method for mtu, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/mtu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu() directly.

    YANG Description: The size, in octets, of the largest IPv6 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu(self):
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)


  def _get_dup_addr_detect_transmits(self):
    """
    Getter method for dup_addr_detect_transmits, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/dup_addr_detect_transmits (uint32)

    YANG Description: The number of consecutive Neighbor Solicitation messages
sent while performing Duplicate Address Detection on a
tentative address.  A value of zero indicates that
Duplicate Address Detection is not performed on
tentative addresses.  A value of one indicates a single
transmission with no follow-up retransmissions.
    """
    return self.__dup_addr_detect_transmits
      
  def _set_dup_addr_detect_transmits(self, v, load=False):
    """
    Setter method for dup_addr_detect_transmits, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/dup_addr_detect_transmits (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dup_addr_detect_transmits is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dup_addr_detect_transmits() directly.

    YANG Description: The number of consecutive Neighbor Solicitation messages
sent while performing Duplicate Address Detection on a
tentative address.  A value of zero indicates that
Duplicate Address Detection is not performed on
tentative addresses.  A value of one indicates a single
transmission with no follow-up retransmissions.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dup_addr_detect_transmits must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__dup_addr_detect_transmits = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dup_addr_detect_transmits(self):
    self.__dup_addr_detect_transmits = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)


  def _get_learn_unsolicited(self):
    """
    Getter method for learn_unsolicited, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/learn_unsolicited (enumeration)

    YANG Description: Sets if neighbors should be learned from unsolicited neighbor
advertisements for global or link local addresses or both.
    """
    return self.__learn_unsolicited
      
  def _set_learn_unsolicited(self, v, load=False):
    """
    Setter method for learn_unsolicited, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/learn_unsolicited (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_learn_unsolicited is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_learn_unsolicited() directly.

    YANG Description: Sets if neighbors should be learned from unsolicited neighbor
advertisements for global or link local addresses or both.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NONE': {'value': 0}, 'GLOBAL': {'value': 1}, 'LINK_LOCAL': {'value': 2}, 'BOTH': {'value': 3}},), default=str("NONE"), is_leaf=True, yang_name="learn-unsolicited", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """learn_unsolicited must be of a type compatible with enumeration""",
          'defined-type': "openconfig-ap-interfaces:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NONE': {'value': 0}, 'GLOBAL': {'value': 1}, 'LINK_LOCAL': {'value': 2}, 'BOTH': {'value': 3}},), default=str("NONE"), is_leaf=True, yang_name="learn-unsolicited", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)""",
        })

    self.__learn_unsolicited = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_learn_unsolicited(self):
    self.__learn_unsolicited = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NONE': {'value': 0}, 'GLOBAL': {'value': 1}, 'LINK_LOCAL': {'value': 2}, 'BOTH': {'value': 3}},), default=str("NONE"), is_leaf=True, yang_name="learn-unsolicited", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)


  def _get_dhcp_client(self):
    """
    Getter method for dhcp_client, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/dhcp_client (boolean)

    YANG Description: Enables a DHCP client on the interface in order to request
an address
    """
    return self.__dhcp_client
      
  def _set_dhcp_client(self, v, load=False):
    """
    Setter method for dhcp_client, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/dhcp_client (boolean)
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
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dhcp_client must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)""",
        })

    self.__dhcp_client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dhcp_client(self):
    self.__dhcp_client = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  mtu = __builtin__.property(_get_mtu, _set_mtu)
  dup_addr_detect_transmits = __builtin__.property(_get_dup_addr_detect_transmits, _set_dup_addr_detect_transmits)
  learn_unsolicited = __builtin__.property(_get_learn_unsolicited, _set_learn_unsolicited)
  dhcp_client = __builtin__.property(_get_dhcp_client, _set_dhcp_client)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('mtu', mtu), ('dup_addr_detect_transmits', dup_addr_detect_transmits), ('learn_unsolicited', learn_unsolicited), ('dhcp_client', dhcp_client), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/tunnel/ipv6/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level config data for the IPv6 interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__mtu','__dup_addr_detect_transmits','__learn_unsolicited','__dhcp_client',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    self.__dup_addr_detect_transmits = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    self.__learn_unsolicited = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NONE': {'value': 0}, 'GLOBAL': {'value': 1}, 'LINK_LOCAL': {'value': 2}, 'BOTH': {'value': 3}},), default=str("NONE"), is_leaf=True, yang_name="learn-unsolicited", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)
    self.__dhcp_client = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'tunnel', 'ipv6', 'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/enabled (boolean)

    YANG Description: Controls whether IPv6 is enabled or disabled on this
interface.  When IPv6 is enabled, this interface is
connected to an IPv6 stack, and the interface can send
and receive IPv6 packets.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Controls whether IPv6 is enabled or disabled on this
interface.  When IPv6 is enabled, this interface is
connected to an IPv6 stack, and the interface can send
and receive IPv6 packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)


  def _get_mtu(self):
    """
    Getter method for mtu, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/mtu (uint32)

    YANG Description: The size, in octets, of the largest IPv6 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
    return self.__mtu
      
  def _set_mtu(self, v, load=False):
    """
    Setter method for mtu, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/mtu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu() directly.

    YANG Description: The size, in octets, of the largest IPv6 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu(self):
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)


  def _get_dup_addr_detect_transmits(self):
    """
    Getter method for dup_addr_detect_transmits, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/dup_addr_detect_transmits (uint32)

    YANG Description: The number of consecutive Neighbor Solicitation messages
sent while performing Duplicate Address Detection on a
tentative address.  A value of zero indicates that
Duplicate Address Detection is not performed on
tentative addresses.  A value of one indicates a single
transmission with no follow-up retransmissions.
    """
    return self.__dup_addr_detect_transmits
      
  def _set_dup_addr_detect_transmits(self, v, load=False):
    """
    Setter method for dup_addr_detect_transmits, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/dup_addr_detect_transmits (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dup_addr_detect_transmits is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dup_addr_detect_transmits() directly.

    YANG Description: The number of consecutive Neighbor Solicitation messages
sent while performing Duplicate Address Detection on a
tentative address.  A value of zero indicates that
Duplicate Address Detection is not performed on
tentative addresses.  A value of one indicates a single
transmission with no follow-up retransmissions.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dup_addr_detect_transmits must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__dup_addr_detect_transmits = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dup_addr_detect_transmits(self):
    self.__dup_addr_detect_transmits = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)


  def _get_learn_unsolicited(self):
    """
    Getter method for learn_unsolicited, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/learn_unsolicited (enumeration)

    YANG Description: Sets if neighbors should be learned from unsolicited neighbor
advertisements for global or link local addresses or both.
    """
    return self.__learn_unsolicited
      
  def _set_learn_unsolicited(self, v, load=False):
    """
    Setter method for learn_unsolicited, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/learn_unsolicited (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_learn_unsolicited is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_learn_unsolicited() directly.

    YANG Description: Sets if neighbors should be learned from unsolicited neighbor
advertisements for global or link local addresses or both.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NONE': {'value': 0}, 'GLOBAL': {'value': 1}, 'LINK_LOCAL': {'value': 2}, 'BOTH': {'value': 3}},), default=str("NONE"), is_leaf=True, yang_name="learn-unsolicited", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """learn_unsolicited must be of a type compatible with enumeration""",
          'defined-type': "openconfig-ap-interfaces:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NONE': {'value': 0}, 'GLOBAL': {'value': 1}, 'LINK_LOCAL': {'value': 2}, 'BOTH': {'value': 3}},), default=str("NONE"), is_leaf=True, yang_name="learn-unsolicited", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)""",
        })

    self.__learn_unsolicited = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_learn_unsolicited(self):
    self.__learn_unsolicited = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'NONE': {'value': 0}, 'GLOBAL': {'value': 1}, 'LINK_LOCAL': {'value': 2}, 'BOTH': {'value': 3}},), default=str("NONE"), is_leaf=True, yang_name="learn-unsolicited", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)


  def _get_dhcp_client(self):
    """
    Getter method for dhcp_client, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/dhcp_client (boolean)

    YANG Description: Enables a DHCP client on the interface in order to request
an address
    """
    return self.__dhcp_client
      
  def _set_dhcp_client(self, v, load=False):
    """
    Setter method for dhcp_client, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/config/dhcp_client (boolean)
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
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dhcp_client must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)""",
        })

    self.__dhcp_client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dhcp_client(self):
    self.__dhcp_client = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="dhcp-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  mtu = __builtin__.property(_get_mtu, _set_mtu)
  dup_addr_detect_transmits = __builtin__.property(_get_dup_addr_detect_transmits, _set_dup_addr_detect_transmits)
  learn_unsolicited = __builtin__.property(_get_learn_unsolicited, _set_learn_unsolicited)
  dhcp_client = __builtin__.property(_get_dhcp_client, _set_dhcp_client)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('mtu', mtu), ('dup_addr_detect_transmits', dup_addr_detect_transmits), ('learn_unsolicited', learn_unsolicited), ('dhcp_client', dhcp_client), ])


