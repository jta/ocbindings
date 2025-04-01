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
from . import sflow
class sampling(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-sampling - based on the path /sampling. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for sampling-related configuration and
operational state data
  """
  __slots__ = ('_path_helper', '_extmethods', '__sflow',)

  _yang_name = 'sampling'
  _yang_namespace = 'http://openconfig.net/yang/sampling'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sflow = YANGDynClass(base=sflow.sflow, is_container='container', yang_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='container', is_config=True)

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
      return ['sampling']

  def _get_sflow(self):
    """
    Getter method for sflow, mapped from YANG variable /sampling/sflow (container)

    YANG Description: Top-level container for sFlow data.
    """
    return self.__sflow
      
  def _set_sflow(self, v, load=False):
    """
    Setter method for sflow, mapped from YANG variable /sampling/sflow (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sflow is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sflow() directly.

    YANG Description: Top-level container for sFlow data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sflow.sflow, is_container='container', yang_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sflow must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sflow.sflow, is_container='container', yang_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='container', is_config=True)""",
        })

    self.__sflow = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sflow(self):
    self.__sflow = YANGDynClass(base=sflow.sflow, is_container='container', yang_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='container', is_config=True)

  sflow = __builtin__.property(_get_sflow, _set_sflow)


  _pyangbind_elements = OrderedDict([('sflow', sflow), ])


from . import sflow
class sampling(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-sampling - based on the path /sampling. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for sampling-related configuration and
operational state data
  """
  __slots__ = ('_path_helper', '_extmethods', '__sflow',)

  _yang_name = 'sampling'
  _yang_namespace = 'http://openconfig.net/yang/sampling'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sflow = YANGDynClass(base=sflow.sflow, is_container='container', yang_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='container', is_config=True)

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
      return ['sampling']

  def _get_sflow(self):
    """
    Getter method for sflow, mapped from YANG variable /sampling/sflow (container)

    YANG Description: Top-level container for sFlow data.
    """
    return self.__sflow
      
  def _set_sflow(self, v, load=False):
    """
    Setter method for sflow, mapped from YANG variable /sampling/sflow (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sflow is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sflow() directly.

    YANG Description: Top-level container for sFlow data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sflow.sflow, is_container='container', yang_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sflow must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sflow.sflow, is_container='container', yang_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='container', is_config=True)""",
        })

    self.__sflow = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sflow(self):
    self.__sflow = YANGDynClass(base=sflow.sflow, is_container='container', yang_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='container', is_config=True)

  sflow = __builtin__.property(_get_sflow, _set_sflow)


  _pyangbind_elements = OrderedDict([('sflow', sflow), ])


