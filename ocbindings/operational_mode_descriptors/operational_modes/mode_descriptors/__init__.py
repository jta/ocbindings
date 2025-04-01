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
from . import mode_descriptor
class mode_descriptors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device-properties - based on the path /operational-mode-descriptors/operational-modes/mode-descriptors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Explicit definition of the operational-mode. Typically this is used
for non-standard/proprietary modes defined by the terminal-device
vendor and it is self-described by the capabilities included in
the subtree underneath.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mode_descriptor',)

  _yang_name = 'mode-descriptors'
  _yang_namespace = 'http://openconfig.net/yang/openconfig-terminal-device-properties'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mode_descriptor = YANGDynClass(base=YANGListType("mode_descriptor_id",mode_descriptor.mode_descriptor, yang_name="mode-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mode-descriptor-id', extensions=None), is_container='list', yang_name="mode-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)

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
      return ['operational-mode-descriptors', 'operational-modes', 'mode-descriptors']

  def _get_mode_descriptor(self):
    """
    Getter method for mode_descriptor, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor (list)
    """
    return self.__mode_descriptor
      
  def _set_mode_descriptor(self, v, load=False):
    """
    Setter method for mode_descriptor, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode_descriptor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode_descriptor() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("mode_descriptor_id",mode_descriptor.mode_descriptor, yang_name="mode-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mode-descriptor-id', extensions=None), is_container='list', yang_name="mode-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode_descriptor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mode_descriptor_id",mode_descriptor.mode_descriptor, yang_name="mode-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mode-descriptor-id', extensions=None), is_container='list', yang_name="mode-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)""",
        })

    self.__mode_descriptor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode_descriptor(self):
    self.__mode_descriptor = YANGDynClass(base=YANGListType("mode_descriptor_id",mode_descriptor.mode_descriptor, yang_name="mode-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mode-descriptor-id', extensions=None), is_container='list', yang_name="mode-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)

  mode_descriptor = __builtin__.property(_get_mode_descriptor)


  _pyangbind_elements = OrderedDict([('mode_descriptor', mode_descriptor), ])


from . import mode_descriptor
class mode_descriptors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device-properties - based on the path /operational-mode-descriptors/operational-modes/mode-descriptors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Explicit definition of the operational-mode. Typically this is used
for non-standard/proprietary modes defined by the terminal-device
vendor and it is self-described by the capabilities included in
the subtree underneath.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mode_descriptor',)

  _yang_name = 'mode-descriptors'
  _yang_namespace = 'http://openconfig.net/yang/openconfig-terminal-device-properties'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mode_descriptor = YANGDynClass(base=YANGListType("mode_descriptor_id",mode_descriptor.mode_descriptor, yang_name="mode-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mode-descriptor-id', extensions=None), is_container='list', yang_name="mode-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)

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
      return ['operational-mode-descriptors', 'operational-modes', 'mode-descriptors']

  def _get_mode_descriptor(self):
    """
    Getter method for mode_descriptor, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor (list)
    """
    return self.__mode_descriptor
      
  def _set_mode_descriptor(self, v, load=False):
    """
    Setter method for mode_descriptor, mapped from YANG variable /operational_mode_descriptors/operational_modes/mode_descriptors/mode_descriptor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode_descriptor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode_descriptor() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("mode_descriptor_id",mode_descriptor.mode_descriptor, yang_name="mode-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mode-descriptor-id', extensions=None), is_container='list', yang_name="mode-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode_descriptor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mode_descriptor_id",mode_descriptor.mode_descriptor, yang_name="mode-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mode-descriptor-id', extensions=None), is_container='list', yang_name="mode-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)""",
        })

    self.__mode_descriptor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode_descriptor(self):
    self.__mode_descriptor = YANGDynClass(base=YANGListType("mode_descriptor_id",mode_descriptor.mode_descriptor, yang_name="mode-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mode-descriptor-id', extensions=None), is_container='list', yang_name="mode-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/openconfig-terminal-device-properties', defining_module='openconfig-terminal-device-properties', yang_type='list', is_config=False)

  mode_descriptor = __builtin__.property(_get_mode_descriptor)


  _pyangbind_elements = OrderedDict([('mode_descriptor', mode_descriptor), ])


