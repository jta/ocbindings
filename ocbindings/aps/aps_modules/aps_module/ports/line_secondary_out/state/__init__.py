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
from . import optical_power
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-transport-line-protection - based on the path /aps/aps-modules/aps-module/ports/line-secondary-out/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State data for the line secondary output port
  """
  __slots__ = ('_path_helper', '_extmethods', '__target_attenuation','__attenuation','__optical_power',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/optical-transport-line-protection'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target_attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)
    self.__attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)
    self.__optical_power = YANGDynClass(base=optical_power.optical_power, is_container='container', yang_name="optical-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='container', is_config=False)

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
      return ['aps', 'aps-modules', 'aps-module', 'ports', 'line-secondary-out', 'state']

  def _get_target_attenuation(self):
    """
    Getter method for target_attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/target_attenuation (decimal64)

    YANG Description: Target attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB
    """
    return self.__target_attenuation
      
  def _set_target_attenuation(self, v, load=False):
    """
    Setter method for target_attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/target_attenuation (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_attenuation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_attenuation() directly.

    YANG Description: Target attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_attenuation must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)""",
        })

    self.__target_attenuation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_attenuation(self):
    self.__target_attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)


  def _get_attenuation(self):
    """
    Getter method for attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/attenuation (decimal64)

    YANG Description: The attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB
    """
    return self.__attenuation
      
  def _set_attenuation(self, v, load=False):
    """
    Setter method for attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/attenuation (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attenuation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attenuation() directly.

    YANG Description: The attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attenuation must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)""",
        })

    self.__attenuation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attenuation(self):
    self.__attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)


  def _get_optical_power(self):
    """
    Getter method for optical_power, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/optical_power (container)

    YANG Description: The optical output power of this port in units of
0.01dBm. Optical output power represents the signal
traversing from the module to an external destination. The
power is measured after any attenuation. If avg/min/max
statistics are not supported, the target is expected to
just supply the instant value
    """
    return self.__optical_power
      
  def _set_optical_power(self, v, load=False):
    """
    Setter method for optical_power, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/optical_power (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_optical_power is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_optical_power() directly.

    YANG Description: The optical output power of this port in units of
0.01dBm. Optical output power represents the signal
traversing from the module to an external destination. The
power is measured after any attenuation. If avg/min/max
statistics are not supported, the target is expected to
just supply the instant value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=optical_power.optical_power, is_container='container', yang_name="optical-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """optical_power must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=optical_power.optical_power, is_container='container', yang_name="optical-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='container', is_config=False)""",
        })

    self.__optical_power = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_optical_power(self):
    self.__optical_power = YANGDynClass(base=optical_power.optical_power, is_container='container', yang_name="optical-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='container', is_config=False)

  target_attenuation = __builtin__.property(_get_target_attenuation)
  attenuation = __builtin__.property(_get_attenuation)
  optical_power = __builtin__.property(_get_optical_power)


  _pyangbind_elements = OrderedDict([('target_attenuation', target_attenuation), ('attenuation', attenuation), ('optical_power', optical_power), ])


from . import optical_power
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-transport-line-protection - based on the path /aps/aps-modules/aps-module/ports/line-secondary-out/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State data for the line secondary output port
  """
  __slots__ = ('_path_helper', '_extmethods', '__target_attenuation','__attenuation','__optical_power',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/optical-transport-line-protection'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target_attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)
    self.__attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)
    self.__optical_power = YANGDynClass(base=optical_power.optical_power, is_container='container', yang_name="optical-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='container', is_config=False)

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
      return ['aps', 'aps-modules', 'aps-module', 'ports', 'line-secondary-out', 'state']

  def _get_target_attenuation(self):
    """
    Getter method for target_attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/target_attenuation (decimal64)

    YANG Description: Target attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB
    """
    return self.__target_attenuation
      
  def _set_target_attenuation(self, v, load=False):
    """
    Setter method for target_attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/target_attenuation (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_attenuation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_attenuation() directly.

    YANG Description: Target attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_attenuation must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)""",
        })

    self.__target_attenuation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_attenuation(self):
    self.__target_attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)


  def _get_attenuation(self):
    """
    Getter method for attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/attenuation (decimal64)

    YANG Description: The attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB
    """
    return self.__attenuation
      
  def _set_attenuation(self, v, load=False):
    """
    Setter method for attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/attenuation (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attenuation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attenuation() directly.

    YANG Description: The attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attenuation must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)""",
        })

    self.__attenuation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attenuation(self):
    self.__attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=False)


  def _get_optical_power(self):
    """
    Getter method for optical_power, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/optical_power (container)

    YANG Description: The optical output power of this port in units of
0.01dBm. Optical output power represents the signal
traversing from the module to an external destination. The
power is measured after any attenuation. If avg/min/max
statistics are not supported, the target is expected to
just supply the instant value
    """
    return self.__optical_power
      
  def _set_optical_power(self, v, load=False):
    """
    Setter method for optical_power, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_secondary_out/state/optical_power (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_optical_power is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_optical_power() directly.

    YANG Description: The optical output power of this port in units of
0.01dBm. Optical output power represents the signal
traversing from the module to an external destination. The
power is measured after any attenuation. If avg/min/max
statistics are not supported, the target is expected to
just supply the instant value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=optical_power.optical_power, is_container='container', yang_name="optical-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """optical_power must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=optical_power.optical_power, is_container='container', yang_name="optical-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='container', is_config=False)""",
        })

    self.__optical_power = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_optical_power(self):
    self.__optical_power = YANGDynClass(base=optical_power.optical_power, is_container='container', yang_name="optical-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='container', is_config=False)

  target_attenuation = __builtin__.property(_get_target_attenuation)
  attenuation = __builtin__.property(_get_attenuation)
  optical_power = __builtin__.property(_get_optical_power)


  _pyangbind_elements = OrderedDict([('target_attenuation', target_attenuation), ('attenuation', attenuation), ('optical_power', optical_power), ])


