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
  from YANG module openconfig-wavelength-router - based on the path /wavelength-router/media-channels/channel/dest/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for the media channel destination
  """
  __slots__ = ('_path_helper', '_extmethods', '__port_name',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wavelength-router'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port_name = YANGDynClass(base=str, is_leaf=True, yang_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='leafref', is_config=True)

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
      return ['wavelength-router', 'media-channels', 'channel', 'dest', 'config']

  def _get_port_name(self):
    """
    Getter method for port_name, mapped from YANG variable /wavelength_router/media_channels/channel/dest/config/port_name (leafref)

    YANG Description: Reference to the corresponding node port
    """
    return self.__port_name
      
  def _set_port_name(self, v, load=False):
    """
    Setter method for port_name, mapped from YANG variable /wavelength_router/media_channels/channel/dest/config/port_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_name() directly.

    YANG Description: Reference to the corresponding node port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='leafref', is_config=True)""",
        })

    self.__port_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_name(self):
    self.__port_name = YANGDynClass(base=str, is_leaf=True, yang_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='leafref', is_config=True)

  port_name = __builtin__.property(_get_port_name, _set_port_name)


  _pyangbind_elements = OrderedDict([('port_name', port_name), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-wavelength-router - based on the path /wavelength-router/media-channels/channel/dest/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for the media channel destination
  """
  __slots__ = ('_path_helper', '_extmethods', '__port_name',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wavelength-router'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port_name = YANGDynClass(base=str, is_leaf=True, yang_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='leafref', is_config=True)

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
      return ['wavelength-router', 'media-channels', 'channel', 'dest', 'config']

  def _get_port_name(self):
    """
    Getter method for port_name, mapped from YANG variable /wavelength_router/media_channels/channel/dest/config/port_name (leafref)

    YANG Description: Reference to the corresponding node port
    """
    return self.__port_name
      
  def _set_port_name(self, v, load=False):
    """
    Setter method for port_name, mapped from YANG variable /wavelength_router/media_channels/channel/dest/config/port_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_name() directly.

    YANG Description: Reference to the corresponding node port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='leafref', is_config=True)""",
        })

    self.__port_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_name(self):
    self.__port_name = YANGDynClass(base=str, is_leaf=True, yang_name="port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='leafref', is_config=True)

  port_name = __builtin__.property(_get_port_name, _set_port_name)


  _pyangbind_elements = OrderedDict([('port_name', port_name), ])


