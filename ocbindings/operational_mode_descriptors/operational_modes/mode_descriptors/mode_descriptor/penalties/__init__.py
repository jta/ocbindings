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
from . import penalty
class penalties(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device-properties - based on the path /operational-mode-descriptors/operational-modes/mode-descriptors/mode-descriptor/penalties. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enconsing list's container.
  """
  __slots__ = ('_path_helper', '_extmethods', '__penalty',)

  _yang_name = 'penalties'
  _yang_namespace = 'http://openconfig.net/yang/openconfig-terminal-device-properties'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__penalty = YANGDynClass(base=YANGListType("parameter_and_unit up_to_boundary",penalty.penalty, yang_name="penalty", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='parameter-and-unit up-to-boundary', extensions=None), is_container='list', yang_name="penalty", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)

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
      return ['operational-mode-descriptors', 'operational-modes', 'mode-descriptors', 'mode-descriptor', 'penalties']

  def _get_penalty(self):
    """
    Getter method for penalty, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty (list)

    YANG Description: Penalties includes contributions from different impairments including
cd, pmd, low RX Power, pdl,...
- For parameter values below lowest up-to-boundary value, the penalty is 0.
- For parameter values between lowest and highest up-to-boundary
values, penalty could be linearly interpolated.
- For parameter values above highest up-to-boundary value, the penalty is the one
included within penalty-value attribute associated to the highest up-to-boundary
    """
    return self.__penalty
      
  def _set_penalty(self, v, load=False):
    """
    Setter method for penalty, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_penalty is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_penalty() directly.

    YANG Description: Penalties includes contributions from different impairments including
cd, pmd, low RX Power, pdl,...
- For parameter values below lowest up-to-boundary value, the penalty is 0.
- For parameter values between lowest and highest up-to-boundary
values, penalty could be linearly interpolated.
- For parameter values above highest up-to-boundary value, the penalty is the one
included within penalty-value attribute associated to the highest up-to-boundary
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("parameter_and_unit up_to_boundary",penalty.penalty, yang_name="penalty", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='parameter-and-unit up-to-boundary', extensions=None), is_container='list', yang_name="penalty", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """penalty must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("parameter_and_unit up_to_boundary",penalty.penalty, yang_name="penalty", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='parameter-and-unit up-to-boundary', extensions=None), is_container='list', yang_name="penalty", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)""",
        })

    self.__penalty = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_penalty(self):
    self.__penalty = YANGDynClass(base=YANGListType("parameter_and_unit up_to_boundary",penalty.penalty, yang_name="penalty", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='parameter-and-unit up-to-boundary', extensions=None), is_container='list', yang_name="penalty", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)

  penalty = __builtin__.property(_get_penalty)


  _pyangbind_elements = OrderedDict([('penalty', penalty), ])


from . import penalty
class penalties(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device-properties - based on the path /operational-mode-descriptors/operational-modes/mode-descriptors/mode-descriptor/penalties. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enconsing list's container.
  """
  __slots__ = ('_path_helper', '_extmethods', '__penalty',)

  _yang_name = 'penalties'
  _yang_namespace = 'http://openconfig.net/yang/openconfig-terminal-device-properties'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__penalty = YANGDynClass(base=YANGListType("parameter_and_unit up_to_boundary",penalty.penalty, yang_name="penalty", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='parameter-and-unit up-to-boundary', extensions=None), is_container='list', yang_name="penalty", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)

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
      return ['operational-mode-descriptors', 'operational-modes', 'mode-descriptors', 'mode-descriptor', 'penalties']

  def _get_penalty(self):
    """
    Getter method for penalty, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty (list)

    YANG Description: Penalties includes contributions from different impairments including
cd, pmd, low RX Power, pdl,...
- For parameter values below lowest up-to-boundary value, the penalty is 0.
- For parameter values between lowest and highest up-to-boundary
values, penalty could be linearly interpolated.
- For parameter values above highest up-to-boundary value, the penalty is the one
included within penalty-value attribute associated to the highest up-to-boundary
    """
    return self.__penalty
      
  def _set_penalty(self, v, load=False):
    """
    Setter method for penalty, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor/penalties/penalty (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_penalty is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_penalty() directly.

    YANG Description: Penalties includes contributions from different impairments including
cd, pmd, low RX Power, pdl,...
- For parameter values below lowest up-to-boundary value, the penalty is 0.
- For parameter values between lowest and highest up-to-boundary
values, penalty could be linearly interpolated.
- For parameter values above highest up-to-boundary value, the penalty is the one
included within penalty-value attribute associated to the highest up-to-boundary
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("parameter_and_unit up_to_boundary",penalty.penalty, yang_name="penalty", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='parameter-and-unit up-to-boundary', extensions=None), is_container='list', yang_name="penalty", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """penalty must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("parameter_and_unit up_to_boundary",penalty.penalty, yang_name="penalty", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='parameter-and-unit up-to-boundary', extensions=None), is_container='list', yang_name="penalty", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)""",
        })

    self.__penalty = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_penalty(self):
    self.__penalty = YANGDynClass(base=YANGListType("parameter_and_unit up_to_boundary",penalty.penalty, yang_name="penalty", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='parameter-and-unit up-to-boundary', extensions=None), is_container='list', yang_name="penalty", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)

  penalty = __builtin__.property(_get_penalty)


  _pyangbind_elements = OrderedDict([('penalty', penalty), ])


