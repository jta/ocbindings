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
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-relay-agent - based on the path /relay-agent/dhcp/interfaces/interface/agent-information-option/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable','__circuit_id','__remote_id','__sent_circuit_id','__sent_remote_id',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/relay-agent'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    self.__circuit_id = YANGDynClass(base=str, is_leaf=True, yang_name="circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__remote_id = YANGDynClass(base=str, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__sent_circuit_id = YANGDynClass(base=str, is_leaf=True, yang_name="sent-circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__sent_remote_id = YANGDynClass(base=str, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)

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
      return ['relay-agent', 'dhcp', 'interfaces', 'interface', 'agent-information-option', 'state']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/enable (boolean)

    YANG Description: Enable sending the DHCP option for Relay Agent information
-- option 82.
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enable sending the DHCP option for Relay Agent information
-- option 82.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)


  def _get_circuit_id(self):
    """
    Getter method for circuit_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/circuit_id (string)

    YANG Description: Encodes an agent-local identifier of the circuit from which
a DHCP client-to-server packet was received.  It is intended
for use by agents in relaying DHCP responses back to the
proper circuit.  The circuit id is an opaque value
    """
    return self.__circuit_id
      
  def _set_circuit_id(self, v, load=False):
    """
    Setter method for circuit_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/circuit_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_circuit_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_circuit_id() directly.

    YANG Description: Encodes an agent-local identifier of the circuit from which
a DHCP client-to-server packet was received.  It is intended
for use by agents in relaying DHCP responses back to the
proper circuit.  The circuit id is an opaque value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """circuit_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__circuit_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_circuit_id(self):
    self.__circuit_id = YANGDynClass(base=str, is_leaf=True, yang_name="circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_remote_id(self):
    """
    Getter method for remote_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/remote_id (string)

    YANG Description: Provides a mechanism to identify the remote host end of
the circuit.  The remote-id should be thought of as an
opaque value, but must be globally unique.
    """
    return self.__remote_id
      
  def _set_remote_id(self, v, load=False):
    """
    Setter method for remote_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/remote_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_id() directly.

    YANG Description: Provides a mechanism to identify the remote host end of
the circuit.  The remote-id should be thought of as an
opaque value, but must be globally unique.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_id(self):
    self.__remote_id = YANGDynClass(base=str, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_sent_circuit_id(self):
    """
    Getter method for sent_circuit_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/sent_circuit_id (string)

    YANG Description: Reports the circuit-id sent by the system to the DHCP
server.
    """
    return self.__sent_circuit_id
      
  def _set_sent_circuit_id(self, v, load=False):
    """
    Setter method for sent_circuit_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/sent_circuit_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent_circuit_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent_circuit_id() directly.

    YANG Description: Reports the circuit-id sent by the system to the DHCP
server.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="sent-circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent_circuit_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="sent-circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__sent_circuit_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent_circuit_id(self):
    self.__sent_circuit_id = YANGDynClass(base=str, is_leaf=True, yang_name="sent-circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_sent_remote_id(self):
    """
    Getter method for sent_remote_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/sent_remote_id (string)

    YANG Description: Reports the remote-id value sent by the system to the DHCP
server
    """
    return self.__sent_remote_id
      
  def _set_sent_remote_id(self, v, load=False):
    """
    Setter method for sent_remote_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/sent_remote_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent_remote_id() directly.

    YANG Description: Reports the remote-id value sent by the system to the DHCP
server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent_remote_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__sent_remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent_remote_id(self):
    self.__sent_remote_id = YANGDynClass(base=str, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)

  enable = __builtin__.property(_get_enable)
  circuit_id = __builtin__.property(_get_circuit_id)
  remote_id = __builtin__.property(_get_remote_id)
  sent_circuit_id = __builtin__.property(_get_sent_circuit_id)
  sent_remote_id = __builtin__.property(_get_sent_remote_id)


  _pyangbind_elements = OrderedDict([('enable', enable), ('circuit_id', circuit_id), ('remote_id', remote_id), ('sent_circuit_id', sent_circuit_id), ('sent_remote_id', sent_remote_id), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-relay-agent - based on the path /relay-agent/dhcp/interfaces/interface/agent-information-option/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable','__circuit_id','__remote_id','__sent_circuit_id','__sent_remote_id',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/relay-agent'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    self.__circuit_id = YANGDynClass(base=str, is_leaf=True, yang_name="circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__remote_id = YANGDynClass(base=str, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__sent_circuit_id = YANGDynClass(base=str, is_leaf=True, yang_name="sent-circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__sent_remote_id = YANGDynClass(base=str, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)

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
      return ['relay-agent', 'dhcp', 'interfaces', 'interface', 'agent-information-option', 'state']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/enable (boolean)

    YANG Description: Enable sending the DHCP option for Relay Agent information
-- option 82.
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enable sending the DHCP option for Relay Agent information
-- option 82.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)


  def _get_circuit_id(self):
    """
    Getter method for circuit_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/circuit_id (string)

    YANG Description: Encodes an agent-local identifier of the circuit from which
a DHCP client-to-server packet was received.  It is intended
for use by agents in relaying DHCP responses back to the
proper circuit.  The circuit id is an opaque value
    """
    return self.__circuit_id
      
  def _set_circuit_id(self, v, load=False):
    """
    Setter method for circuit_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/circuit_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_circuit_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_circuit_id() directly.

    YANG Description: Encodes an agent-local identifier of the circuit from which
a DHCP client-to-server packet was received.  It is intended
for use by agents in relaying DHCP responses back to the
proper circuit.  The circuit id is an opaque value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """circuit_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__circuit_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_circuit_id(self):
    self.__circuit_id = YANGDynClass(base=str, is_leaf=True, yang_name="circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_remote_id(self):
    """
    Getter method for remote_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/remote_id (string)

    YANG Description: Provides a mechanism to identify the remote host end of
the circuit.  The remote-id should be thought of as an
opaque value, but must be globally unique.
    """
    return self.__remote_id
      
  def _set_remote_id(self, v, load=False):
    """
    Setter method for remote_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/remote_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_id() directly.

    YANG Description: Provides a mechanism to identify the remote host end of
the circuit.  The remote-id should be thought of as an
opaque value, but must be globally unique.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_id(self):
    self.__remote_id = YANGDynClass(base=str, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_sent_circuit_id(self):
    """
    Getter method for sent_circuit_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/sent_circuit_id (string)

    YANG Description: Reports the circuit-id sent by the system to the DHCP
server.
    """
    return self.__sent_circuit_id
      
  def _set_sent_circuit_id(self, v, load=False):
    """
    Setter method for sent_circuit_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/sent_circuit_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent_circuit_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent_circuit_id() directly.

    YANG Description: Reports the circuit-id sent by the system to the DHCP
server.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="sent-circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent_circuit_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="sent-circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__sent_circuit_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent_circuit_id(self):
    self.__sent_circuit_id = YANGDynClass(base=str, is_leaf=True, yang_name="sent-circuit-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_sent_remote_id(self):
    """
    Getter method for sent_remote_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/sent_remote_id (string)

    YANG Description: Reports the remote-id value sent by the system to the DHCP
server
    """
    return self.__sent_remote_id
      
  def _set_sent_remote_id(self, v, load=False):
    """
    Setter method for sent_remote_id, mapped from YANG variable /relay_agent/dhcp/interfaces/interface/agent_information_option/state/sent_remote_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent_remote_id() directly.

    YANG Description: Reports the remote-id value sent by the system to the DHCP
server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent_remote_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__sent_remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent_remote_id(self):
    self.__sent_remote_id = YANGDynClass(base=str, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)

  enable = __builtin__.property(_get_enable)
  circuit_id = __builtin__.property(_get_circuit_id)
  remote_id = __builtin__.property(_get_remote_id)
  sent_circuit_id = __builtin__.property(_get_sent_circuit_id)
  sent_remote_id = __builtin__.property(_get_sent_remote_id)


  _pyangbind_elements = OrderedDict([('enable', enable), ('circuit_id', circuit_id), ('remote_id', remote_id), ('sent_circuit_id', sent_circuit_id), ('sent_remote_id', sent_remote_id), ])


