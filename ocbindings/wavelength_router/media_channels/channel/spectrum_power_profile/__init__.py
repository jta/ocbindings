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
from . import distribution
class spectrum_power_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-wavelength-router - based on the path /wavelength-router/media-channels/channel/spectrum-power-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of values describing
the target spectrum powers
  """
  __slots__ = ('_path_helper', '_extmethods', '__distribution',)

  _yang_name = 'spectrum-power-profile'
  _yang_namespace = 'http://openconfig.net/yang/wavelength-router'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__distribution = YANGDynClass(base=YANGListType("lower_frequency upper_frequency",distribution.distribution, yang_name="distribution", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lower-frequency upper-frequency', extensions=None), is_container='list', yang_name="distribution", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='list', is_config=True)

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
      return ['wavelength-router', 'media-channels', 'channel', 'spectrum-power-profile']

  def _get_distribution(self):
    """
    Getter method for distribution, mapped from YANG variable /wavelength_router/media_channels/channel/spectrum_power_profile/distribution (list)

    YANG Description: List of tuples describing the target spectrum power
distribution
    """
    return self.__distribution
      
  def _set_distribution(self, v, load=False):
    """
    Setter method for distribution, mapped from YANG variable /wavelength_router/media_channels/channel/spectrum_power_profile/distribution (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_distribution is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_distribution() directly.

    YANG Description: List of tuples describing the target spectrum power
distribution
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("lower_frequency upper_frequency",distribution.distribution, yang_name="distribution", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lower-frequency upper-frequency', extensions=None), is_container='list', yang_name="distribution", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """distribution must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lower_frequency upper_frequency",distribution.distribution, yang_name="distribution", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lower-frequency upper-frequency', extensions=None), is_container='list', yang_name="distribution", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='list', is_config=True)""",
        })

    self.__distribution = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_distribution(self):
    self.__distribution = YANGDynClass(base=YANGListType("lower_frequency upper_frequency",distribution.distribution, yang_name="distribution", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lower-frequency upper-frequency', extensions=None), is_container='list', yang_name="distribution", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='list', is_config=True)

  distribution = __builtin__.property(_get_distribution, _set_distribution)


  _pyangbind_elements = OrderedDict([('distribution', distribution), ])


from . import distribution
class spectrum_power_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-wavelength-router - based on the path /wavelength-router/media-channels/channel/spectrum-power-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of values describing
the target spectrum powers
  """
  __slots__ = ('_path_helper', '_extmethods', '__distribution',)

  _yang_name = 'spectrum-power-profile'
  _yang_namespace = 'http://openconfig.net/yang/wavelength-router'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__distribution = YANGDynClass(base=YANGListType("lower_frequency upper_frequency",distribution.distribution, yang_name="distribution", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lower-frequency upper-frequency', extensions=None), is_container='list', yang_name="distribution", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='list', is_config=True)

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
      return ['wavelength-router', 'media-channels', 'channel', 'spectrum-power-profile']

  def _get_distribution(self):
    """
    Getter method for distribution, mapped from YANG variable /wavelength_router/media_channels/channel/spectrum_power_profile/distribution (list)

    YANG Description: List of tuples describing the target spectrum power
distribution
    """
    return self.__distribution
      
  def _set_distribution(self, v, load=False):
    """
    Setter method for distribution, mapped from YANG variable /wavelength_router/media_channels/channel/spectrum_power_profile/distribution (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_distribution is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_distribution() directly.

    YANG Description: List of tuples describing the target spectrum power
distribution
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("lower_frequency upper_frequency",distribution.distribution, yang_name="distribution", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lower-frequency upper-frequency', extensions=None), is_container='list', yang_name="distribution", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """distribution must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lower_frequency upper_frequency",distribution.distribution, yang_name="distribution", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lower-frequency upper-frequency', extensions=None), is_container='list', yang_name="distribution", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='list', is_config=True)""",
        })

    self.__distribution = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_distribution(self):
    self.__distribution = YANGDynClass(base=YANGListType("lower_frequency upper_frequency",distribution.distribution, yang_name="distribution", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lower-frequency upper-frequency', extensions=None), is_container='list', yang_name="distribution", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wavelength-router', defining_module='openconfig-wavelength-router', yang_type='list', is_config=True)

  distribution = __builtin__.property(_get_distribution, _set_distribution)


  _pyangbind_elements = OrderedDict([('distribution', distribution), ])


