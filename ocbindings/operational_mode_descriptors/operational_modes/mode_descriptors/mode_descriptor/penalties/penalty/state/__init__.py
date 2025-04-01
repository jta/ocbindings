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
  from YANG module openconfig-terminal-device-properties - based on the path /operational-mode-descriptors/operational-modes/mode-descriptors/mode-descriptor/penalties/penalty/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Penalties list element's state attributes top container.
  """
  __slots__ = ('_path_helper', '_extmethods', '__parameter_and_unit','__up_to_boundary','__penalty_value',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/openconfig-terminal-device-properties'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__parameter_and_unit = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}},), is_leaf=True, yang_name="parameter-and-unit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='oc-opt-term-prop-types:impairment-type', is_config=False)
    self.__up_to_boundary = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="up-to-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)
    self.__penalty_value = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="penalty-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)

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
      return ['operational-mode-descriptors', 'operational-modes', 'mode-descriptors', 'mode-descriptor', 'penalties', 'penalty', 'state']

  def _get_parameter_and_unit(self):
    """
    Getter method for parameter_and_unit, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/parameter_and_unit (oc-opt-term-prop-types:impairment-type)

    YANG Description: Impairment and unit leading to the penalty (i.e., cd-ps)
    """
    return self.__parameter_and_unit
      
  def _set_parameter_and_unit(self, v, load=False):
    """
    Setter method for parameter_and_unit, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/parameter_and_unit (oc-opt-term-prop-types:impairment-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parameter_and_unit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parameter_and_unit() directly.

    YANG Description: Impairment and unit leading to the penalty (i.e., cd-ps)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}},), is_leaf=True, yang_name="parameter-and-unit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='oc-opt-term-prop-types:impairment-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parameter_and_unit must be of a type compatible with oc-opt-term-prop-types:impairment-type""",
          'defined-type': "oc-opt-term-prop-types:impairment-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}},), is_leaf=True, yang_name="parameter-and-unit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='oc-opt-term-prop-types:impairment-type', is_config=False)""",
        })

    self.__parameter_and_unit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parameter_and_unit(self):
    self.__parameter_and_unit = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}},), is_leaf=True, yang_name="parameter-and-unit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='oc-opt-term-prop-types:impairment-type', is_config=False)


  def _get_up_to_boundary(self):
    """
    Getter method for up_to_boundary, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/up_to_boundary (decimal64)

    YANG Description: defines the upper (for positive values) and lower (for negative values)
limit for which the penalty value is valid.
    """
    return self.__up_to_boundary
      
  def _set_up_to_boundary(self, v, load=False):
    """
    Setter method for up_to_boundary, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/up_to_boundary (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_up_to_boundary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_up_to_boundary() directly.

    YANG Description: defines the upper (for positive values) and lower (for negative values)
limit for which the penalty value is valid.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="up-to-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """up_to_boundary must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="up-to-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)""",
        })

    self.__up_to_boundary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_up_to_boundary(self):
    self.__up_to_boundary = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="up-to-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)


  def _get_penalty_value(self):
    """
    Getter method for penalty_value, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/penalty_value (decimal64)

    YANG Description: OSNR penalty associated to the given values, expressed in dB.
    """
    return self.__penalty_value
      
  def _set_penalty_value(self, v, load=False):
    """
    Setter method for penalty_value, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/penalty_value (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_penalty_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_penalty_value() directly.

    YANG Description: OSNR penalty associated to the given values, expressed in dB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="penalty-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """penalty_value must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="penalty-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)""",
        })

    self.__penalty_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_penalty_value(self):
    self.__penalty_value = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="penalty-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)

  parameter_and_unit = __builtin__.property(_get_parameter_and_unit)
  up_to_boundary = __builtin__.property(_get_up_to_boundary)
  penalty_value = __builtin__.property(_get_penalty_value)


  _pyangbind_elements = OrderedDict([('parameter_and_unit', parameter_and_unit), ('up_to_boundary', up_to_boundary), ('penalty_value', penalty_value), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device-properties - based on the path /operational-mode-descriptors/operational-modes/mode-descriptors/mode-descriptor/penalties/penalty/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Penalties list element's state attributes top container.
  """
  __slots__ = ('_path_helper', '_extmethods', '__parameter_and_unit','__up_to_boundary','__penalty_value',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/openconfig-terminal-device-properties'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__parameter_and_unit = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}},), is_leaf=True, yang_name="parameter-and-unit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='oc-opt-term-prop-types:impairment-type', is_config=False)
    self.__up_to_boundary = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="up-to-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)
    self.__penalty_value = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="penalty-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)

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
      return ['operational-mode-descriptors', 'operational-modes', 'mode-descriptors', 'mode-descriptor', 'penalties', 'penalty', 'state']

  def _get_parameter_and_unit(self):
    """
    Getter method for parameter_and_unit, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/parameter_and_unit (oc-opt-term-prop-types:impairment-type)

    YANG Description: Impairment and unit leading to the penalty (i.e., cd-ps)
    """
    return self.__parameter_and_unit
      
  def _set_parameter_and_unit(self, v, load=False):
    """
    Setter method for parameter_and_unit, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/parameter_and_unit (oc-opt-term-prop-types:impairment-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parameter_and_unit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parameter_and_unit() directly.

    YANG Description: Impairment and unit leading to the penalty (i.e., cd-ps)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}},), is_leaf=True, yang_name="parameter-and-unit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='oc-opt-term-prop-types:impairment-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parameter_and_unit must be of a type compatible with oc-opt-term-prop-types:impairment-type""",
          'defined-type': "oc-opt-term-prop-types:impairment-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}},), is_leaf=True, yang_name="parameter-and-unit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='oc-opt-term-prop-types:impairment-type', is_config=False)""",
        })

    self.__parameter_and_unit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parameter_and_unit(self):
    self.__parameter_and_unit = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:CD_PS_NM': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PMD_PS': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'openconfig-terminal-device-property-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}, 'oc-opt-term-prop-types:PDL_DB': {'@module': 'openconfig-terminal-device-property-types', '@namespace': 'http://openconfig.net/yang/openconfig-terminal-device-property-types'}},), is_leaf=True, yang_name="parameter-and-unit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='oc-opt-term-prop-types:impairment-type', is_config=False)


  def _get_up_to_boundary(self):
    """
    Getter method for up_to_boundary, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/up_to_boundary (decimal64)

    YANG Description: defines the upper (for positive values) and lower (for negative values)
limit for which the penalty value is valid.
    """
    return self.__up_to_boundary
      
  def _set_up_to_boundary(self, v, load=False):
    """
    Setter method for up_to_boundary, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/up_to_boundary (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_up_to_boundary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_up_to_boundary() directly.

    YANG Description: defines the upper (for positive values) and lower (for negative values)
limit for which the penalty value is valid.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="up-to-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """up_to_boundary must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="up-to-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)""",
        })

    self.__up_to_boundary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_up_to_boundary(self):
    self.__up_to_boundary = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="up-to-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)


  def _get_penalty_value(self):
    """
    Getter method for penalty_value, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/penalty_value (decimal64)

    YANG Description: OSNR penalty associated to the given values, expressed in dB.
    """
    return self.__penalty_value
      
  def _set_penalty_value(self, v, load=False):
    """
    Setter method for penalty_value, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty/state/penalty_value (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_penalty_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_penalty_value() directly.

    YANG Description: OSNR penalty associated to the given values, expressed in dB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="penalty-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """penalty_value must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="penalty-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)""",
        })

    self.__penalty_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_penalty_value(self):
    self.__penalty_value = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="penalty-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='decimal64', is_config=False)

  parameter_and_unit = __builtin__.property(_get_parameter_and_unit)
  up_to_boundary = __builtin__.property(_get_up_to_boundary)
  penalty_value = __builtin__.property(_get_penalty_value)


  _pyangbind_elements = OrderedDict([('parameter_and_unit', parameter_and_unit), ('up_to_boundary', up_to_boundary), ('penalty_value', penalty_value), ])


