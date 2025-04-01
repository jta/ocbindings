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
from . import process
class processes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/processes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters related to all monitored processes
  """
  __slots__ = ('_path_helper', '_extmethods', '__process',)

  _yang_name = 'processes'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__process = YANGDynClass(base=YANGListType("pid",process.process, yang_name="process", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pid', extensions=None), is_container='list', yang_name="process", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'processes']

  def _get_process(self):
    """
    Getter method for process, mapped from YANG variable /access_points/access_point/system/processes/process (list)

    YANG Description: List of monitored processes
    """
    return self.__process
      
  def _set_process(self, v, load=False):
    """
    Setter method for process, mapped from YANG variable /access_points/access_point/system/processes/process (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_process is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_process() directly.

    YANG Description: List of monitored processes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("pid",process.process, yang_name="process", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pid', extensions=None), is_container='list', yang_name="process", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """process must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("pid",process.process, yang_name="process", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pid', extensions=None), is_container='list', yang_name="process", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=False)""",
        })

    self.__process = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_process(self):
    self.__process = YANGDynClass(base=YANGListType("pid",process.process, yang_name="process", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pid', extensions=None), is_container='list', yang_name="process", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=False)

  process = __builtin__.property(_get_process)


  _pyangbind_elements = OrderedDict([('process', process), ])


from . import process
class processes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/processes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters related to all monitored processes
  """
  __slots__ = ('_path_helper', '_extmethods', '__process',)

  _yang_name = 'processes'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__process = YANGDynClass(base=YANGListType("pid",process.process, yang_name="process", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pid', extensions=None), is_container='list', yang_name="process", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'processes']

  def _get_process(self):
    """
    Getter method for process, mapped from YANG variable /access_points/access_point/system/processes/process (list)

    YANG Description: List of monitored processes
    """
    return self.__process
      
  def _set_process(self, v, load=False):
    """
    Setter method for process, mapped from YANG variable /access_points/access_point/system/processes/process (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_process is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_process() directly.

    YANG Description: List of monitored processes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("pid",process.process, yang_name="process", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pid', extensions=None), is_container='list', yang_name="process", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """process must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("pid",process.process, yang_name="process", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pid', extensions=None), is_container='list', yang_name="process", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=False)""",
        })

    self.__process = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_process(self):
    self.__process = YANGDynClass(base=YANGListType("pid",process.process, yang_name="process", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pid', extensions=None), is_container='list', yang_name="process", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=False)

  process = __builtin__.property(_get_process)


  _pyangbind_elements = OrderedDict([('process', process), ])


