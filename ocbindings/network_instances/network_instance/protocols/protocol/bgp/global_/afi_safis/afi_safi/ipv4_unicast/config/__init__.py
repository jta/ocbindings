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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for IPv4 unicast AFI-SAFI options
  """
  __slots__ = ('_path_helper', '_extmethods', '__send_default_route','__extended_next_hop_encoding',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__extended_next_hop_encoding = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'afi-safis', 'afi-safi', 'ipv4-unicast', 'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbor(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbor(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_extended_next_hop_encoding(self):
    """
    Getter method for extended_next_hop_encoding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/extended_next_hop_encoding (boolean)

    YANG Description: This leaf indicates whether extended next-hop encoding is enabled for
this AFI-SAFI
    """
    return self.__extended_next_hop_encoding
      
  def _set_extended_next_hop_encoding(self, v, load=False):
    """
    Setter method for extended_next_hop_encoding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/extended_next_hop_encoding (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended_next_hop_encoding is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended_next_hop_encoding() directly.

    YANG Description: This leaf indicates whether extended next-hop encoding is enabled for
this AFI-SAFI
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended_next_hop_encoding must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__extended_next_hop_encoding = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended_next_hop_encoding(self):
    self.__extended_next_hop_encoding = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)
  extended_next_hop_encoding = __builtin__.property(_get_extended_next_hop_encoding, _set_extended_next_hop_encoding)


  _pyangbind_elements = OrderedDict([('send_default_route', send_default_route), ('extended_next_hop_encoding', extended_next_hop_encoding), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for IPv4 unicast AFI-SAFI options
  """
  __slots__ = ('_path_helper', '_extmethods', '__send_default_route','__extended_next_hop_encoding',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__extended_next_hop_encoding = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'afi-safis', 'afi-safi', 'ipv4-unicast', 'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbor(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbor(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_extended_next_hop_encoding(self):
    """
    Getter method for extended_next_hop_encoding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/extended_next_hop_encoding (boolean)

    YANG Description: This leaf indicates whether extended next-hop encoding is enabled for
this AFI-SAFI
    """
    return self.__extended_next_hop_encoding
      
  def _set_extended_next_hop_encoding(self, v, load=False):
    """
    Setter method for extended_next_hop_encoding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/extended_next_hop_encoding (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended_next_hop_encoding is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended_next_hop_encoding() directly.

    YANG Description: This leaf indicates whether extended next-hop encoding is enabled for
this AFI-SAFI
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended_next_hop_encoding must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__extended_next_hop_encoding = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended_next_hop_encoding(self):
    self.__extended_next_hop_encoding = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)
  extended_next_hop_encoding = __builtin__.property(_get_extended_next_hop_encoding, _set_extended_next_hop_encoding)


  _pyangbind_elements = OrderedDict([('send_default_route', send_default_route), ('extended_next_hop_encoding', extended_next_hop_encoding), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for IPv4 unicast AFI-SAFI options
  """
  __slots__ = ('_path_helper', '_extmethods', '__send_default_route','__extended_next_hop_encoding',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__extended_next_hop_encoding = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'afi-safis', 'afi-safi', 'ipv4-unicast', 'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbor(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbor(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_extended_next_hop_encoding(self):
    """
    Getter method for extended_next_hop_encoding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/extended_next_hop_encoding (boolean)

    YANG Description: This leaf indicates whether extended next-hop encoding is enabled for
this AFI-SAFI
    """
    return self.__extended_next_hop_encoding
      
  def _set_extended_next_hop_encoding(self, v, load=False):
    """
    Setter method for extended_next_hop_encoding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/extended_next_hop_encoding (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended_next_hop_encoding is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended_next_hop_encoding() directly.

    YANG Description: This leaf indicates whether extended next-hop encoding is enabled for
this AFI-SAFI
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended_next_hop_encoding must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__extended_next_hop_encoding = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended_next_hop_encoding(self):
    self.__extended_next_hop_encoding = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)
  extended_next_hop_encoding = __builtin__.property(_get_extended_next_hop_encoding, _set_extended_next_hop_encoding)


  _pyangbind_elements = OrderedDict([('send_default_route', send_default_route), ('extended_next_hop_encoding', extended_next_hop_encoding), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for IPv4 unicast AFI-SAFI options
  """
  __slots__ = ('_path_helper', '_extmethods', '__send_default_route','__extended_next_hop_encoding',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__extended_next_hop_encoding = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'afi-safis', 'afi-safi', 'ipv4-unicast', 'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbor(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbor(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_extended_next_hop_encoding(self):
    """
    Getter method for extended_next_hop_encoding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/extended_next_hop_encoding (boolean)

    YANG Description: This leaf indicates whether extended next-hop encoding is enabled for
this AFI-SAFI
    """
    return self.__extended_next_hop_encoding
      
  def _set_extended_next_hop_encoding(self, v, load=False):
    """
    Setter method for extended_next_hop_encoding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_unicast/config/extended_next_hop_encoding (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended_next_hop_encoding is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended_next_hop_encoding() directly.

    YANG Description: This leaf indicates whether extended next-hop encoding is enabled for
this AFI-SAFI
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended_next_hop_encoding must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__extended_next_hop_encoding = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended_next_hop_encoding(self):
    self.__extended_next_hop_encoding = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="extended-next-hop-encoding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)
  extended_next_hop_encoding = __builtin__.property(_get_extended_next_hop_encoding, _set_extended_next_hop_encoding)


  _pyangbind_elements = OrderedDict([('send_default_route', send_default_route), ('extended_next_hop_encoding', extended_next_hop_encoding), ])


