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
from . import port_identity
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-ptp - based on the path /ptp/transparent-clock-ports/port/port-ds/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data of transparent clock port data set.
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_min_pdelay_req_interval','__faulty_flag','__network_transport','__port_identity','__peer_mean_path_delay',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/ptp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_min_pdelay_req_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="log-min-pdelay-req-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='int8', is_config=False)
    self.__faulty_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="faulty-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='boolean', is_config=False)
    self.__network_transport = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'L2': {'value': 1}, 'UDPV4': {'value': 2}, 'UDPV6': {'value': 3}},), is_leaf=True, yang_name="network-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:network-transport-enumeration', is_config=False)
    self.__port_identity = YANGDynClass(base=port_identity.port_identity, is_container='container', yang_name="port-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='container', is_config=False)
    self.__peer_mean_path_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="peer-mean-path-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:time-interval', is_config=False)

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
      return ['ptp', 'transparent-clock-ports', 'port', 'port-ds', 'state']

  def _get_log_min_pdelay_req_interval(self):
    """
    Getter method for log_min_pdelay_req_interval, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/log_min_pdelay_req_interval (int8)

    YANG Description: The logarithm to the base 2 of the
minPdelayReqInterval (minimum permitted mean time
interval between successive Pdelay_Req messages).
    """
    return self.__log_min_pdelay_req_interval
      
  def _set_log_min_pdelay_req_interval(self, v, load=False):
    """
    Setter method for log_min_pdelay_req_interval, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/log_min_pdelay_req_interval (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_min_pdelay_req_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_min_pdelay_req_interval() directly.

    YANG Description: The logarithm to the base 2 of the
minPdelayReqInterval (minimum permitted mean time
interval between successive Pdelay_Req messages).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="log-min-pdelay-req-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_min_pdelay_req_interval must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="log-min-pdelay-req-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='int8', is_config=False)""",
        })

    self.__log_min_pdelay_req_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_min_pdelay_req_interval(self):
    self.__log_min_pdelay_req_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="log-min-pdelay-req-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='int8', is_config=False)


  def _get_faulty_flag(self):
    """
    Getter method for faulty_flag, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/faulty_flag (boolean)

    YANG Description: Shall be true if the port is faulty and false
if the port is operating normally.
    """
    return self.__faulty_flag
      
  def _set_faulty_flag(self, v, load=False):
    """
    Setter method for faulty_flag, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/faulty_flag (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_faulty_flag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_faulty_flag() directly.

    YANG Description: Shall be true if the port is faulty and false
if the port is operating normally.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="faulty-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """faulty_flag must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="faulty-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='boolean', is_config=False)""",
        })

    self.__faulty_flag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_faulty_flag(self):
    self.__faulty_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="faulty-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='boolean', is_config=False)


  def _get_network_transport(self):
    """
    Getter method for network_transport, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/network_transport (oc-ptp-types:network-transport-enumeration)

    YANG Description: The network transport used for communication
    """
    return self.__network_transport
      
  def _set_network_transport(self, v, load=False):
    """
    Setter method for network_transport, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/network_transport (oc-ptp-types:network-transport-enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_transport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_transport() directly.

    YANG Description: The network transport used for communication
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'L2': {'value': 1}, 'UDPV4': {'value': 2}, 'UDPV6': {'value': 3}},), is_leaf=True, yang_name="network-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:network-transport-enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_transport must be of a type compatible with oc-ptp-types:network-transport-enumeration""",
          'defined-type': "oc-ptp-types:network-transport-enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'L2': {'value': 1}, 'UDPV4': {'value': 2}, 'UDPV6': {'value': 3}},), is_leaf=True, yang_name="network-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:network-transport-enumeration', is_config=False)""",
        })

    self.__network_transport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_transport(self):
    self.__network_transport = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'L2': {'value': 1}, 'UDPV4': {'value': 2}, 'UDPV6': {'value': 3}},), is_leaf=True, yang_name="network-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:network-transport-enumeration', is_config=False)


  def _get_port_identity(self):
    """
    Getter method for port_identity, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/port_identity (container)

    YANG Description: The IEEE Std 1588 portIdentity of this port.
    """
    return self.__port_identity
      
  def _set_port_identity(self, v, load=False):
    """
    Setter method for port_identity, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/port_identity (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_identity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_identity() directly.

    YANG Description: The IEEE Std 1588 portIdentity of this port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=port_identity.port_identity, is_container='container', yang_name="port-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_identity must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=port_identity.port_identity, is_container='container', yang_name="port-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='container', is_config=False)""",
        })

    self.__port_identity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_identity(self):
    self.__port_identity = YANGDynClass(base=port_identity.port_identity, is_container='container', yang_name="port-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='container', is_config=False)


  def _get_peer_mean_path_delay(self):
    """
    Getter method for peer_mean_path_delay, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/peer_mean_path_delay (oc-ptp-types:time-interval)

    YANG Description: An estimate of the current one-way propagation delay
on the link when the delayMechanism is P2P; otherwise,
it is zero.
    """
    return self.__peer_mean_path_delay
      
  def _set_peer_mean_path_delay(self, v, load=False):
    """
    Setter method for peer_mean_path_delay, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/peer_mean_path_delay (oc-ptp-types:time-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_mean_path_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_mean_path_delay() directly.

    YANG Description: An estimate of the current one-way propagation delay
on the link when the delayMechanism is P2P; otherwise,
it is zero.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="peer-mean-path-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:time-interval', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_mean_path_delay must be of a type compatible with oc-ptp-types:time-interval""",
          'defined-type': "oc-ptp-types:time-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="peer-mean-path-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:time-interval', is_config=False)""",
        })

    self.__peer_mean_path_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_mean_path_delay(self):
    self.__peer_mean_path_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="peer-mean-path-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:time-interval', is_config=False)

  log_min_pdelay_req_interval = __builtin__.property(_get_log_min_pdelay_req_interval)
  faulty_flag = __builtin__.property(_get_faulty_flag)
  network_transport = __builtin__.property(_get_network_transport)
  port_identity = __builtin__.property(_get_port_identity)
  peer_mean_path_delay = __builtin__.property(_get_peer_mean_path_delay)


  _pyangbind_elements = OrderedDict([('log_min_pdelay_req_interval', log_min_pdelay_req_interval), ('faulty_flag', faulty_flag), ('network_transport', network_transport), ('port_identity', port_identity), ('peer_mean_path_delay', peer_mean_path_delay), ])


from . import port_identity
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-ptp - based on the path /ptp/transparent-clock-ports/port/port-ds/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data of transparent clock port data set.
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_min_pdelay_req_interval','__faulty_flag','__network_transport','__port_identity','__peer_mean_path_delay',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/ptp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_min_pdelay_req_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="log-min-pdelay-req-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='int8', is_config=False)
    self.__faulty_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="faulty-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='boolean', is_config=False)
    self.__network_transport = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'L2': {'value': 1}, 'UDPV4': {'value': 2}, 'UDPV6': {'value': 3}},), is_leaf=True, yang_name="network-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:network-transport-enumeration', is_config=False)
    self.__port_identity = YANGDynClass(base=port_identity.port_identity, is_container='container', yang_name="port-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='container', is_config=False)
    self.__peer_mean_path_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="peer-mean-path-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:time-interval', is_config=False)

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
      return ['ptp', 'transparent-clock-ports', 'port', 'port-ds', 'state']

  def _get_log_min_pdelay_req_interval(self):
    """
    Getter method for log_min_pdelay_req_interval, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/log_min_pdelay_req_interval (int8)

    YANG Description: The logarithm to the base 2 of the
minPdelayReqInterval (minimum permitted mean time
interval between successive Pdelay_Req messages).
    """
    return self.__log_min_pdelay_req_interval
      
  def _set_log_min_pdelay_req_interval(self, v, load=False):
    """
    Setter method for log_min_pdelay_req_interval, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/log_min_pdelay_req_interval (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_min_pdelay_req_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_min_pdelay_req_interval() directly.

    YANG Description: The logarithm to the base 2 of the
minPdelayReqInterval (minimum permitted mean time
interval between successive Pdelay_Req messages).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="log-min-pdelay-req-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_min_pdelay_req_interval must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="log-min-pdelay-req-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='int8', is_config=False)""",
        })

    self.__log_min_pdelay_req_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_min_pdelay_req_interval(self):
    self.__log_min_pdelay_req_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="log-min-pdelay-req-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='int8', is_config=False)


  def _get_faulty_flag(self):
    """
    Getter method for faulty_flag, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/faulty_flag (boolean)

    YANG Description: Shall be true if the port is faulty and false
if the port is operating normally.
    """
    return self.__faulty_flag
      
  def _set_faulty_flag(self, v, load=False):
    """
    Setter method for faulty_flag, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/faulty_flag (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_faulty_flag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_faulty_flag() directly.

    YANG Description: Shall be true if the port is faulty and false
if the port is operating normally.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="faulty-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """faulty_flag must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="faulty-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='boolean', is_config=False)""",
        })

    self.__faulty_flag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_faulty_flag(self):
    self.__faulty_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="faulty-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='boolean', is_config=False)


  def _get_network_transport(self):
    """
    Getter method for network_transport, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/network_transport (oc-ptp-types:network-transport-enumeration)

    YANG Description: The network transport used for communication
    """
    return self.__network_transport
      
  def _set_network_transport(self, v, load=False):
    """
    Setter method for network_transport, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/network_transport (oc-ptp-types:network-transport-enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_transport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_transport() directly.

    YANG Description: The network transport used for communication
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'L2': {'value': 1}, 'UDPV4': {'value': 2}, 'UDPV6': {'value': 3}},), is_leaf=True, yang_name="network-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:network-transport-enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_transport must be of a type compatible with oc-ptp-types:network-transport-enumeration""",
          'defined-type': "oc-ptp-types:network-transport-enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'L2': {'value': 1}, 'UDPV4': {'value': 2}, 'UDPV6': {'value': 3}},), is_leaf=True, yang_name="network-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:network-transport-enumeration', is_config=False)""",
        })

    self.__network_transport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_transport(self):
    self.__network_transport = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'L2': {'value': 1}, 'UDPV4': {'value': 2}, 'UDPV6': {'value': 3}},), is_leaf=True, yang_name="network-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:network-transport-enumeration', is_config=False)


  def _get_port_identity(self):
    """
    Getter method for port_identity, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/port_identity (container)

    YANG Description: The IEEE Std 1588 portIdentity of this port.
    """
    return self.__port_identity
      
  def _set_port_identity(self, v, load=False):
    """
    Setter method for port_identity, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/port_identity (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_identity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_identity() directly.

    YANG Description: The IEEE Std 1588 portIdentity of this port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=port_identity.port_identity, is_container='container', yang_name="port-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_identity must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=port_identity.port_identity, is_container='container', yang_name="port-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='container', is_config=False)""",
        })

    self.__port_identity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_identity(self):
    self.__port_identity = YANGDynClass(base=port_identity.port_identity, is_container='container', yang_name="port-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='container', is_config=False)


  def _get_peer_mean_path_delay(self):
    """
    Getter method for peer_mean_path_delay, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/peer_mean_path_delay (oc-ptp-types:time-interval)

    YANG Description: An estimate of the current one-way propagation delay
on the link when the delayMechanism is P2P; otherwise,
it is zero.
    """
    return self.__peer_mean_path_delay
      
  def _set_peer_mean_path_delay(self, v, load=False):
    """
    Setter method for peer_mean_path_delay, mapped from YANG variable /ptp/transparent_clock_ports/port/port_ds/state/peer_mean_path_delay (oc-ptp-types:time-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_mean_path_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_mean_path_delay() directly.

    YANG Description: An estimate of the current one-way propagation delay
on the link when the delayMechanism is P2P; otherwise,
it is zero.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="peer-mean-path-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:time-interval', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_mean_path_delay must be of a type compatible with oc-ptp-types:time-interval""",
          'defined-type': "oc-ptp-types:time-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="peer-mean-path-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:time-interval', is_config=False)""",
        })

    self.__peer_mean_path_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_mean_path_delay(self):
    self.__peer_mean_path_delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64), is_leaf=True, yang_name="peer-mean-path-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ptp', defining_module='openconfig-ptp', yang_type='oc-ptp-types:time-interval', is_config=False)

  log_min_pdelay_req_interval = __builtin__.property(_get_log_min_pdelay_req_interval)
  faulty_flag = __builtin__.property(_get_faulty_flag)
  network_transport = __builtin__.property(_get_network_transport)
  port_identity = __builtin__.property(_get_port_identity)
  peer_mean_path_delay = __builtin__.property(_get_peer_mean_path_delay)


  _pyangbind_elements = OrderedDict([('log_min_pdelay_req_interval', log_min_pdelay_req_interval), ('faulty_flag', faulty_flag), ('network_transport', network_transport), ('port_identity', port_identity), ('peer_mean_path_delay', peer_mean_path_delay), ])


