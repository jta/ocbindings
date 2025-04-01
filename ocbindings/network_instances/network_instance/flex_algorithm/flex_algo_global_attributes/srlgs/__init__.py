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
from . import srlg
class srlgs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/flex-algorithm/flex-algo-global-attributes/srlgs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Shared risk link groups attributes
  """
  __slots__ = ('_path_helper', '_extmethods', '__srlg',)

  _yang_name = 'srlgs'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__srlg = YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'flex-algorithm', 'flex-algo-global-attributes', 'srlgs']

  def _get_srlg(self):
    """
    Getter method for srlg, mapped from YANG variable /network_instances/network_instance/flex_algorithm/flex_algo_global_attributes/srlgs/srlg (list)

    YANG Description: List of shared risk link groups
    """
    return self.__srlg
      
  def _set_srlg(self, v, load=False):
    """
    Setter method for srlg, mapped from YANG variable /network_instances/network_instance/flex_algorithm/flex_algo_global_attributes/srlgs/srlg (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srlg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srlg() directly.

    YANG Description: List of shared risk link groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srlg must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)""",
        })

    self.__srlg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srlg(self):
    self.__srlg = YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)

  srlg = __builtin__.property(_get_srlg, _set_srlg)


  _pyangbind_elements = OrderedDict([('srlg', srlg), ])


from . import srlg
class srlgs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/flex-algorithm/flex-algo-global-attributes/srlgs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Shared risk link groups attributes
  """
  __slots__ = ('_path_helper', '_extmethods', '__srlg',)

  _yang_name = 'srlgs'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__srlg = YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'flex-algorithm', 'flex-algo-global-attributes', 'srlgs']

  def _get_srlg(self):
    """
    Getter method for srlg, mapped from YANG variable /network_instances/network_instance/flex_algorithm/flex_algo_global_attributes/srlgs/srlg (list)

    YANG Description: List of shared risk link groups
    """
    return self.__srlg
      
  def _set_srlg(self, v, load=False):
    """
    Setter method for srlg, mapped from YANG variable /network_instances/network_instance/flex_algorithm/flex_algo_global_attributes/srlgs/srlg (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srlg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srlg() directly.

    YANG Description: List of shared risk link groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srlg must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)""",
        })

    self.__srlg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srlg(self):
    self.__srlg = YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)

  srlg = __builtin__.property(_get_srlg, _set_srlg)


  _pyangbind_elements = OrderedDict([('srlg', srlg), ])


from . import srlg
class srlgs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/flex-algorithm/flex-algo-global-attributes/srlgs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Shared risk link groups attributes
  """
  __slots__ = ('_path_helper', '_extmethods', '__srlg',)

  _yang_name = 'srlgs'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__srlg = YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'flex-algorithm', 'flex-algo-global-attributes', 'srlgs']

  def _get_srlg(self):
    """
    Getter method for srlg, mapped from YANG variable /network_instances/network_instance/flex_algorithm/flex_algo_global_attributes/srlgs/srlg (list)

    YANG Description: List of shared risk link groups
    """
    return self.__srlg
      
  def _set_srlg(self, v, load=False):
    """
    Setter method for srlg, mapped from YANG variable /network_instances/network_instance/flex_algorithm/flex_algo_global_attributes/srlgs/srlg (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srlg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srlg() directly.

    YANG Description: List of shared risk link groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srlg must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)""",
        })

    self.__srlg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srlg(self):
    self.__srlg = YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)

  srlg = __builtin__.property(_get_srlg, _set_srlg)


  _pyangbind_elements = OrderedDict([('srlg', srlg), ])


from . import srlg
class srlgs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/flex-algorithm/flex-algo-global-attributes/srlgs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Shared risk link groups attributes
  """
  __slots__ = ('_path_helper', '_extmethods', '__srlg',)

  _yang_name = 'srlgs'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__srlg = YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'flex-algorithm', 'flex-algo-global-attributes', 'srlgs']

  def _get_srlg(self):
    """
    Getter method for srlg, mapped from YANG variable /network_instances/network_instance/flex_algorithm/flex_algo_global_attributes/srlgs/srlg (list)

    YANG Description: List of shared risk link groups
    """
    return self.__srlg
      
  def _set_srlg(self, v, load=False):
    """
    Setter method for srlg, mapped from YANG variable /network_instances/network_instance/flex_algorithm/flex_algo_global_attributes/srlgs/srlg (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srlg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srlg() directly.

    YANG Description: List of shared risk link groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srlg must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)""",
        })

    self.__srlg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srlg(self):
    self.__srlg = YANGDynClass(base=YANGListType("name",srlg.srlg, yang_name="srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/flexalgo', defining_module='openconfig-flexalgo', yang_type='list', is_config=True)

  srlg = __builtin__.property(_get_srlg, _set_srlg)


  _pyangbind_elements = OrderedDict([('srlg', srlg), ])


