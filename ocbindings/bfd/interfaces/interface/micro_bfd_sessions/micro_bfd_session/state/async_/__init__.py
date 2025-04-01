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
class async_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd/interfaces/interface/micro-bfd-sessions/micro-bfd-session/state/async. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters specifically relating to
asynchronous mode of BFD.
  """
  __slots__ = ('_path_helper', '_extmethods', '__last_packet_transmitted','__last_packet_received','__transmitted_packets','__received_packets','__up_transitions',)

  _yang_name = 'async'
  _yang_namespace = 'http://openconfig.net/yang/bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__last_packet_transmitted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-transmitted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    self.__last_packet_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    self.__transmitted_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="transmitted-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    self.__received_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="received-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    self.__up_transitions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="up-transitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)

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
      return ['bfd', 'interfaces', 'interface', 'micro-bfd-sessions', 'micro-bfd-session', 'state', 'async']

  def _get_last_packet_transmitted(self):
    """
    Getter method for last_packet_transmitted, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/last_packet_transmitted (uint64)

    YANG Description: The date and time at which the last BFD packet
was transmitted for this session, expressed as the number
of nanoseconds since the Unix Epoch (January 1, 1970,
00:00 UTC).
    """
    return self.__last_packet_transmitted
      
  def _set_last_packet_transmitted(self, v, load=False):
    """
    Setter method for last_packet_transmitted, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/last_packet_transmitted (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_packet_transmitted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_packet_transmitted() directly.

    YANG Description: The date and time at which the last BFD packet
was transmitted for this session, expressed as the number
of nanoseconds since the Unix Epoch (January 1, 1970,
00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-transmitted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_packet_transmitted must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-transmitted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__last_packet_transmitted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_packet_transmitted(self):
    self.__last_packet_transmitted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-transmitted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)


  def _get_last_packet_received(self):
    """
    Getter method for last_packet_received, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/last_packet_received (uint64)

    YANG Description: The date and time at which the last BFD packet
was received for this session, expressed as the number
of nanoseconds since the Unix Epoch (January 1, 1970,
00:00 UTC).
    """
    return self.__last_packet_received
      
  def _set_last_packet_received(self, v, load=False):
    """
    Setter method for last_packet_received, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/last_packet_received (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_packet_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_packet_received() directly.

    YANG Description: The date and time at which the last BFD packet
was received for this session, expressed as the number
of nanoseconds since the Unix Epoch (January 1, 1970,
00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_packet_received must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__last_packet_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_packet_received(self):
    self.__last_packet_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)


  def _get_transmitted_packets(self):
    """
    Getter method for transmitted_packets, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/transmitted_packets (uint64)

    YANG Description: The number of packets that have been transmitted
by the local system.
    """
    return self.__transmitted_packets
      
  def _set_transmitted_packets(self, v, load=False):
    """
    Setter method for transmitted_packets, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/transmitted_packets (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transmitted_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transmitted_packets() directly.

    YANG Description: The number of packets that have been transmitted
by the local system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="transmitted-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transmitted_packets must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="transmitted-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__transmitted_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transmitted_packets(self):
    self.__transmitted_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="transmitted-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)


  def _get_received_packets(self):
    """
    Getter method for received_packets, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/received_packets (uint64)

    YANG Description: The number of packets that have been received by the
local system from the remote neighbour.
    """
    return self.__received_packets
      
  def _set_received_packets(self, v, load=False):
    """
    Setter method for received_packets, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/received_packets (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_received_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_received_packets() directly.

    YANG Description: The number of packets that have been received by the
local system from the remote neighbour.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="received-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """received_packets must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="received-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__received_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_received_packets(self):
    self.__received_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="received-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)


  def _get_up_transitions(self):
    """
    Getter method for up_transitions, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/up_transitions (uint64)

    YANG Description: The number of times that the adjacency with the neighbor
has transitioned into the up state.

This leaf is deprecated and will be replaced by a single
up-transitions leaf in state container. New path:
/bfd/interfaces/interface/peers/peer/state/up-transitions.
    """
    return self.__up_transitions
      
  def _set_up_transitions(self, v, load=False):
    """
    Setter method for up_transitions, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/up_transitions (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_up_transitions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_up_transitions() directly.

    YANG Description: The number of times that the adjacency with the neighbor
has transitioned into the up state.

This leaf is deprecated and will be replaced by a single
up-transitions leaf in state container. New path:
/bfd/interfaces/interface/peers/peer/state/up-transitions.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="up-transitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """up_transitions must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="up-transitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__up_transitions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_up_transitions(self):
    self.__up_transitions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="up-transitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)

  last_packet_transmitted = __builtin__.property(_get_last_packet_transmitted)
  last_packet_received = __builtin__.property(_get_last_packet_received)
  transmitted_packets = __builtin__.property(_get_transmitted_packets)
  received_packets = __builtin__.property(_get_received_packets)
  up_transitions = __builtin__.property(_get_up_transitions)


  _pyangbind_elements = OrderedDict([('last_packet_transmitted', last_packet_transmitted), ('last_packet_received', last_packet_received), ('transmitted_packets', transmitted_packets), ('received_packets', received_packets), ('up_transitions', up_transitions), ])


class async_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd/interfaces/interface/micro-bfd-sessions/micro-bfd-session/state/async. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters specifically relating to
asynchronous mode of BFD.
  """
  __slots__ = ('_path_helper', '_extmethods', '__last_packet_transmitted','__last_packet_received','__transmitted_packets','__received_packets','__up_transitions',)

  _yang_name = 'async'
  _yang_namespace = 'http://openconfig.net/yang/bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__last_packet_transmitted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-transmitted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    self.__last_packet_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    self.__transmitted_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="transmitted-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    self.__received_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="received-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    self.__up_transitions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="up-transitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)

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
      return ['bfd', 'interfaces', 'interface', 'micro-bfd-sessions', 'micro-bfd-session', 'state', 'async']

  def _get_last_packet_transmitted(self):
    """
    Getter method for last_packet_transmitted, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/last_packet_transmitted (uint64)

    YANG Description: The date and time at which the last BFD packet
was transmitted for this session, expressed as the number
of nanoseconds since the Unix Epoch (January 1, 1970,
00:00 UTC).
    """
    return self.__last_packet_transmitted
      
  def _set_last_packet_transmitted(self, v, load=False):
    """
    Setter method for last_packet_transmitted, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/last_packet_transmitted (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_packet_transmitted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_packet_transmitted() directly.

    YANG Description: The date and time at which the last BFD packet
was transmitted for this session, expressed as the number
of nanoseconds since the Unix Epoch (January 1, 1970,
00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-transmitted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_packet_transmitted must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-transmitted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__last_packet_transmitted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_packet_transmitted(self):
    self.__last_packet_transmitted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-transmitted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)


  def _get_last_packet_received(self):
    """
    Getter method for last_packet_received, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/last_packet_received (uint64)

    YANG Description: The date and time at which the last BFD packet
was received for this session, expressed as the number
of nanoseconds since the Unix Epoch (January 1, 1970,
00:00 UTC).
    """
    return self.__last_packet_received
      
  def _set_last_packet_received(self, v, load=False):
    """
    Setter method for last_packet_received, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/last_packet_received (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_packet_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_packet_received() directly.

    YANG Description: The date and time at which the last BFD packet
was received for this session, expressed as the number
of nanoseconds since the Unix Epoch (January 1, 1970,
00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_packet_received must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__last_packet_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_packet_received(self):
    self.__last_packet_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-packet-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)


  def _get_transmitted_packets(self):
    """
    Getter method for transmitted_packets, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/transmitted_packets (uint64)

    YANG Description: The number of packets that have been transmitted
by the local system.
    """
    return self.__transmitted_packets
      
  def _set_transmitted_packets(self, v, load=False):
    """
    Setter method for transmitted_packets, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/transmitted_packets (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transmitted_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transmitted_packets() directly.

    YANG Description: The number of packets that have been transmitted
by the local system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="transmitted-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transmitted_packets must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="transmitted-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__transmitted_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transmitted_packets(self):
    self.__transmitted_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="transmitted-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)


  def _get_received_packets(self):
    """
    Getter method for received_packets, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/received_packets (uint64)

    YANG Description: The number of packets that have been received by the
local system from the remote neighbour.
    """
    return self.__received_packets
      
  def _set_received_packets(self, v, load=False):
    """
    Setter method for received_packets, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/received_packets (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_received_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_received_packets() directly.

    YANG Description: The number of packets that have been received by the
local system from the remote neighbour.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="received-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """received_packets must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="received-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__received_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_received_packets(self):
    self.__received_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="received-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)


  def _get_up_transitions(self):
    """
    Getter method for up_transitions, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/up_transitions (uint64)

    YANG Description: The number of times that the adjacency with the neighbor
has transitioned into the up state.

This leaf is deprecated and will be replaced by a single
up-transitions leaf in state container. New path:
/bfd/interfaces/interface/peers/peer/state/up-transitions.
    """
    return self.__up_transitions
      
  def _set_up_transitions(self, v, load=False):
    """
    Setter method for up_transitions, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session/state/async/up_transitions (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_up_transitions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_up_transitions() directly.

    YANG Description: The number of times that the adjacency with the neighbor
has transitioned into the up state.

This leaf is deprecated and will be replaced by a single
up-transitions leaf in state container. New path:
/bfd/interfaces/interface/peers/peer/state/up-transitions.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="up-transitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """up_transitions must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="up-transitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)""",
        })

    self.__up_transitions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_up_transitions(self):
    self.__up_transitions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="up-transitions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='uint64', is_config=False)

  last_packet_transmitted = __builtin__.property(_get_last_packet_transmitted)
  last_packet_received = __builtin__.property(_get_last_packet_received)
  transmitted_packets = __builtin__.property(_get_transmitted_packets)
  received_packets = __builtin__.property(_get_received_packets)
  up_transitions = __builtin__.property(_get_up_transitions)


  _pyangbind_elements = OrderedDict([('last_packet_transmitted', last_packet_transmitted), ('last_packet_received', last_packet_received), ('transmitted_packets', transmitted_packets), ('received_packets', received_packets), ('up_transitions', up_transitions), ])


