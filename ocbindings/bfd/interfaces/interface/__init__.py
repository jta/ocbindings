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
from . import interface_ref
from . import micro_bfd_sessions
from . import peers
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd/interfaces/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-interface configuration and state parameters for BFD.
The interface referenced is based on the interface and
subinterface leaves within the interface-ref container -
which reference an entry in the /interfaces/interface list -
and should not rely on the value of the list key.
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__config','__state','__interface_ref','__micro_bfd_sessions','__peers',)

  _yang_name = 'interface'
  _yang_namespace = 'http://openconfig.net/yang/bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=False)
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    self.__micro_bfd_sessions = YANGDynClass(base=micro_bfd_sessions.micro_bfd_sessions, is_container='container', yang_name="micro-bfd-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    self.__peers = YANGDynClass(base=peers.peers, is_container='container', yang_name="peers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

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
      return ['bfd', 'interfaces', 'interface']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /bfd/interfaces/interface/id (leafref)

    YANG Description: A reference to an identifier for the interface on which
BFD is enabled.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /bfd/interfaces/interface/id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: A reference to an identifier for the interface on which
BFD is enabled.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='leafref', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /bfd/interfaces/interface/config (container)

    YANG Description: Configuration parameters for BFD on the specified
interface.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /bfd/interfaces/interface/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters for BFD on the specified
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /bfd/interfaces/interface/state (container)

    YANG Description: Operational state parameters for BFD on the specified
interface.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /bfd/interfaces/interface/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters for BFD on the specified
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=False)


  def _get_interface_ref(self):
    """
    Getter method for interface_ref, mapped from YANG variable /bfd/interfaces/interface/interface_ref (container)

    YANG Description: Reference to an interface or subinterface. The interface
that is being referenced is uniquely referenced based on
the specified interface and subinterface leaves. In contexts
where a Layer 3 interface is to be referenced, both the
interface and subinterface leaves must be populated, as
Layer 3 configuration within the OpenConfig models is
associated with a subinterface. In the case where a
Layer 2 interface is to be referenced, only the
interface is specified.

The interface/subinterface leaf tuple must be used as
the means by which the interface is specified, regardless
of any other context information (e.g., key in a list).
    """
    return self.__interface_ref
      
  def _set_interface_ref(self, v, load=False):
    """
    Setter method for interface_ref, mapped from YANG variable /bfd/interfaces/interface/interface_ref (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ref() directly.

    YANG Description: Reference to an interface or subinterface. The interface
that is being referenced is uniquely referenced based on
the specified interface and subinterface leaves. In contexts
where a Layer 3 interface is to be referenced, both the
interface and subinterface leaves must be populated, as
Layer 3 configuration within the OpenConfig models is
associated with a subinterface. In the case where a
Layer 2 interface is to be referenced, only the
interface is specified.

The interface/subinterface leaf tuple must be used as
the means by which the interface is specified, regardless
of any other context information (e.g., key in a list).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ref must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__interface_ref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ref(self):
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)


  def _get_micro_bfd_sessions(self):
    """
    Getter method for micro_bfd_sessions, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions (container)

    YANG Description: Parameters relating to micro-BFD sessions associated
with the interface.
    """
    return self.__micro_bfd_sessions
      
  def _set_micro_bfd_sessions(self, v, load=False):
    """
    Setter method for micro_bfd_sessions, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_micro_bfd_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_micro_bfd_sessions() directly.

    YANG Description: Parameters relating to micro-BFD sessions associated
with the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=micro_bfd_sessions.micro_bfd_sessions, is_container='container', yang_name="micro-bfd-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """micro_bfd_sessions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=micro_bfd_sessions.micro_bfd_sessions, is_container='container', yang_name="micro-bfd-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__micro_bfd_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_micro_bfd_sessions(self):
    self.__micro_bfd_sessions = YANGDynClass(base=micro_bfd_sessions.micro_bfd_sessions, is_container='container', yang_name="micro-bfd-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)


  def _get_peers(self):
    """
    Getter method for peers, mapped from YANG variable /bfd/interfaces/interface/peers (container)

    YANG Description: Parameters relating to the BFD peers which are seen
over this interface.
    """
    return self.__peers
      
  def _set_peers(self, v, load=False):
    """
    Setter method for peers, mapped from YANG variable /bfd/interfaces/interface/peers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peers() directly.

    YANG Description: Parameters relating to the BFD peers which are seen
over this interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=peers.peers, is_container='container', yang_name="peers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=peers.peers, is_container='container', yang_name="peers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__peers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peers(self):
    self.__peers = YANGDynClass(base=peers.peers, is_container='container', yang_name="peers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  interface_ref = __builtin__.property(_get_interface_ref, _set_interface_ref)
  micro_bfd_sessions = __builtin__.property(_get_micro_bfd_sessions, _set_micro_bfd_sessions)
  peers = __builtin__.property(_get_peers, _set_peers)


  _pyangbind_elements = OrderedDict([('id', id), ('config', config), ('state', state), ('interface_ref', interface_ref), ('micro_bfd_sessions', micro_bfd_sessions), ('peers', peers), ])


from . import config
from . import state
from . import interface_ref
from . import micro_bfd_sessions
from . import peers
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd/interfaces/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-interface configuration and state parameters for BFD.
The interface referenced is based on the interface and
subinterface leaves within the interface-ref container -
which reference an entry in the /interfaces/interface list -
and should not rely on the value of the list key.
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__config','__state','__interface_ref','__micro_bfd_sessions','__peers',)

  _yang_name = 'interface'
  _yang_namespace = 'http://openconfig.net/yang/bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=False)
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    self.__micro_bfd_sessions = YANGDynClass(base=micro_bfd_sessions.micro_bfd_sessions, is_container='container', yang_name="micro-bfd-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    self.__peers = YANGDynClass(base=peers.peers, is_container='container', yang_name="peers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

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
      return ['bfd', 'interfaces', 'interface']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /bfd/interfaces/interface/id (leafref)

    YANG Description: A reference to an identifier for the interface on which
BFD is enabled.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /bfd/interfaces/interface/id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: A reference to an identifier for the interface on which
BFD is enabled.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='leafref', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=str, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /bfd/interfaces/interface/config (container)

    YANG Description: Configuration parameters for BFD on the specified
interface.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /bfd/interfaces/interface/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters for BFD on the specified
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /bfd/interfaces/interface/state (container)

    YANG Description: Operational state parameters for BFD on the specified
interface.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /bfd/interfaces/interface/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters for BFD on the specified
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=False)


  def _get_interface_ref(self):
    """
    Getter method for interface_ref, mapped from YANG variable /bfd/interfaces/interface/interface_ref (container)

    YANG Description: Reference to an interface or subinterface. The interface
that is being referenced is uniquely referenced based on
the specified interface and subinterface leaves. In contexts
where a Layer 3 interface is to be referenced, both the
interface and subinterface leaves must be populated, as
Layer 3 configuration within the OpenConfig models is
associated with a subinterface. In the case where a
Layer 2 interface is to be referenced, only the
interface is specified.

The interface/subinterface leaf tuple must be used as
the means by which the interface is specified, regardless
of any other context information (e.g., key in a list).
    """
    return self.__interface_ref
      
  def _set_interface_ref(self, v, load=False):
    """
    Setter method for interface_ref, mapped from YANG variable /bfd/interfaces/interface/interface_ref (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ref() directly.

    YANG Description: Reference to an interface or subinterface. The interface
that is being referenced is uniquely referenced based on
the specified interface and subinterface leaves. In contexts
where a Layer 3 interface is to be referenced, both the
interface and subinterface leaves must be populated, as
Layer 3 configuration within the OpenConfig models is
associated with a subinterface. In the case where a
Layer 2 interface is to be referenced, only the
interface is specified.

The interface/subinterface leaf tuple must be used as
the means by which the interface is specified, regardless
of any other context information (e.g., key in a list).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ref must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__interface_ref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ref(self):
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)


  def _get_micro_bfd_sessions(self):
    """
    Getter method for micro_bfd_sessions, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions (container)

    YANG Description: Parameters relating to micro-BFD sessions associated
with the interface.
    """
    return self.__micro_bfd_sessions
      
  def _set_micro_bfd_sessions(self, v, load=False):
    """
    Setter method for micro_bfd_sessions, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_micro_bfd_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_micro_bfd_sessions() directly.

    YANG Description: Parameters relating to micro-BFD sessions associated
with the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=micro_bfd_sessions.micro_bfd_sessions, is_container='container', yang_name="micro-bfd-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """micro_bfd_sessions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=micro_bfd_sessions.micro_bfd_sessions, is_container='container', yang_name="micro-bfd-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__micro_bfd_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_micro_bfd_sessions(self):
    self.__micro_bfd_sessions = YANGDynClass(base=micro_bfd_sessions.micro_bfd_sessions, is_container='container', yang_name="micro-bfd-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)


  def _get_peers(self):
    """
    Getter method for peers, mapped from YANG variable /bfd/interfaces/interface/peers (container)

    YANG Description: Parameters relating to the BFD peers which are seen
over this interface.
    """
    return self.__peers
      
  def _set_peers(self, v, load=False):
    """
    Setter method for peers, mapped from YANG variable /bfd/interfaces/interface/peers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peers() directly.

    YANG Description: Parameters relating to the BFD peers which are seen
over this interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=peers.peers, is_container='container', yang_name="peers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=peers.peers, is_container='container', yang_name="peers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__peers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peers(self):
    self.__peers = YANGDynClass(base=peers.peers, is_container='container', yang_name="peers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state)
  interface_ref = __builtin__.property(_get_interface_ref, _set_interface_ref)
  micro_bfd_sessions = __builtin__.property(_get_micro_bfd_sessions, _set_micro_bfd_sessions)
  peers = __builtin__.property(_get_peers, _set_peers)


  _pyangbind_elements = OrderedDict([('id', id), ('config', config), ('state', state), ('interface_ref', interface_ref), ('micro_bfd_sessions', micro_bfd_sessions), ('peers', peers), ])


