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
from . import optical_channel_config_value_constraints
class constrained_compatible_mode(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device-properties - based on the path /linecard-descriptors/linecard-descriptor/compatible-transceivers/compatible-transceiver/constrained-compatible-modes/constrained-compatible-mode. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of operational modes supported by the target transceiver.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mode_id','__state','__optical_channel_config_value_constraints',)

  _yang_name = 'constrained-compatible-mode'
  _yang_namespace = 'http://openconfig.net/yang/openconfig-terminal-device-properties'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mode_id = YANGDynClass(base=str, is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)
    self.__optical_channel_config_value_constraints = YANGDynClass(base=optical_channel_config_value_constraints.optical_channel_config_value_constraints, is_container='container', yang_name="optical-channel-config-value-constraints", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)

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
      return ['linecard-descriptors', 'linecard-descriptor', 'compatible-transceivers', 'compatible-transceiver', 'constrained-compatible-modes', 'constrained-compatible-mode']

  def _get_mode_id(self):
    """
    Getter method for mode_id, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/mode_id (leafref)

    YANG Description: Reference to linecard-descriptor/constrained-compatible-mode/state/mode-id.
    """
    return self.__mode_id
      
  def _set_mode_id(self, v, load=False):
    """
    Setter method for mode_id, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/mode_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode_id() directly.

    YANG Description: Reference to linecard-descriptor/constrained-compatible-mode/state/mode-id.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='leafref', is_config=False)""",
        })

    self.__mode_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode_id(self):
    self.__mode_id = YANGDynClass(base=str, is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/state (container)

    YANG Description: State container for linecard constrained compatible modes
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State container for linecard constrained compatible modes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)


  def _get_optical_channel_config_value_constraints(self):
    """
    Getter method for optical_channel_config_value_constraints, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/optical_channel_config_value_constraints (container)

    YANG Description: Set of constraints of the configuration attributes
of the optical-channel associated to the selected
operational-mode.
    """
    return self.__optical_channel_config_value_constraints
      
  def _set_optical_channel_config_value_constraints(self, v, load=False):
    """
    Setter method for optical_channel_config_value_constraints, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/optical_channel_config_value_constraints (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_optical_channel_config_value_constraints is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_optical_channel_config_value_constraints() directly.

    YANG Description: Set of constraints of the configuration attributes
of the optical-channel associated to the selected
operational-mode.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=optical_channel_config_value_constraints.optical_channel_config_value_constraints, is_container='container', yang_name="optical-channel-config-value-constraints", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """optical_channel_config_value_constraints must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=optical_channel_config_value_constraints.optical_channel_config_value_constraints, is_container='container', yang_name="optical-channel-config-value-constraints", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)""",
        })

    self.__optical_channel_config_value_constraints = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_optical_channel_config_value_constraints(self):
    self.__optical_channel_config_value_constraints = YANGDynClass(base=optical_channel_config_value_constraints.optical_channel_config_value_constraints, is_container='container', yang_name="optical-channel-config-value-constraints", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)

  mode_id = __builtin__.property(_get_mode_id)
  state = __builtin__.property(_get_state)
  optical_channel_config_value_constraints = __builtin__.property(_get_optical_channel_config_value_constraints)


  _pyangbind_elements = OrderedDict([('mode_id', mode_id), ('state', state), ('optical_channel_config_value_constraints', optical_channel_config_value_constraints), ])


from . import state
from . import optical_channel_config_value_constraints
class constrained_compatible_mode(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device-properties - based on the path /linecard-descriptors/linecard-descriptor/compatible-transceivers/compatible-transceiver/constrained-compatible-modes/constrained-compatible-mode. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of operational modes supported by the target transceiver.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mode_id','__state','__optical_channel_config_value_constraints',)

  _yang_name = 'constrained-compatible-mode'
  _yang_namespace = 'http://openconfig.net/yang/openconfig-terminal-device-properties'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mode_id = YANGDynClass(base=str, is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)
    self.__optical_channel_config_value_constraints = YANGDynClass(base=optical_channel_config_value_constraints.optical_channel_config_value_constraints, is_container='container', yang_name="optical-channel-config-value-constraints", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)

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
      return ['linecard-descriptors', 'linecard-descriptor', 'compatible-transceivers', 'compatible-transceiver', 'constrained-compatible-modes', 'constrained-compatible-mode']

  def _get_mode_id(self):
    """
    Getter method for mode_id, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/mode_id (leafref)

    YANG Description: Reference to linecard-descriptor/constrained-compatible-mode/state/mode-id.
    """
    return self.__mode_id
      
  def _set_mode_id(self, v, load=False):
    """
    Setter method for mode_id, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/mode_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode_id() directly.

    YANG Description: Reference to linecard-descriptor/constrained-compatible-mode/state/mode-id.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='leafref', is_config=False)""",
        })

    self.__mode_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode_id(self):
    self.__mode_id = YANGDynClass(base=str, is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/state (container)

    YANG Description: State container for linecard constrained compatible modes
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State container for linecard constrained compatible modes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)


  def _get_optical_channel_config_value_constraints(self):
    """
    Getter method for optical_channel_config_value_constraints, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/optical_channel_config_value_constraints (container)

    YANG Description: Set of constraints of the configuration attributes
of the optical-channel associated to the selected
operational-mode.
    """
    return self.__optical_channel_config_value_constraints
      
  def _set_optical_channel_config_value_constraints(self, v, load=False):
    """
    Setter method for optical_channel_config_value_constraints, mapped from YANG variable /linecard_descriptors/linecard_descriptor/compatible_transceivers/compatible_transceiver/constrained_compatible_modes/constrained_compatible_mode/optical_channel_config_value_constraints (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_optical_channel_config_value_constraints is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_optical_channel_config_value_constraints() directly.

    YANG Description: Set of constraints of the configuration attributes
of the optical-channel associated to the selected
operational-mode.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=optical_channel_config_value_constraints.optical_channel_config_value_constraints, is_container='container', yang_name="optical-channel-config-value-constraints", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """optical_channel_config_value_constraints must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=optical_channel_config_value_constraints.optical_channel_config_value_constraints, is_container='container', yang_name="optical-channel-config-value-constraints", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)""",
        })

    self.__optical_channel_config_value_constraints = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_optical_channel_config_value_constraints(self):
    self.__optical_channel_config_value_constraints = YANGDynClass(base=optical_channel_config_value_constraints.optical_channel_config_value_constraints, is_container='container', yang_name="optical-channel-config-value-constraints", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='container', is_config=False)

  mode_id = __builtin__.property(_get_mode_id)
  state = __builtin__.property(_get_state)
  optical_channel_config_value_constraints = __builtin__.property(_get_optical_channel_config_value_constraints)


  _pyangbind_elements = OrderedDict([('mode_id', mode_id), ('state', state), ('optical_channel_config_value_constraints', optical_channel_config_value_constraints), ])


