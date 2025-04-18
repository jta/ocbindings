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
from . import global_
from . import rstp
from . import mstp
from . import rapid_pvst
from . import interfaces
class stp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-spanning-tree - based on the path /stp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for spanning tree configuration and
state data
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__rstp','__mstp','__rapid_pvst','__interfaces',)

  _yang_name = 'stp'
  _yang_namespace = 'http://openconfig.net/yang/spanning-tree'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    self.__rstp = YANGDynClass(base=rstp.rstp, is_container='container', yang_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    self.__mstp = YANGDynClass(base=mstp.mstp, is_container='container', yang_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    self.__rapid_pvst = YANGDynClass(base=rapid_pvst.rapid_pvst, is_container='container', yang_name="rapid-pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)

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
      return ['stp']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /stp/global (container)

    YANG Description: Global configuration and state data
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /stp/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: Global configuration and state data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)


  def _get_rstp(self):
    """
    Getter method for rstp, mapped from YANG variable /stp/rstp (container)

    YANG Description: Rapid Spanning-tree protocol configuration and operation
data
    """
    return self.__rstp
      
  def _set_rstp(self, v, load=False):
    """
    Setter method for rstp, mapped from YANG variable /stp/rstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rstp() directly.

    YANG Description: Rapid Spanning-tree protocol configuration and operation
data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rstp.rstp, is_container='container', yang_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rstp.rstp, is_container='container', yang_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__rstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rstp(self):
    self.__rstp = YANGDynClass(base=rstp.rstp, is_container='container', yang_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)


  def _get_mstp(self):
    """
    Getter method for mstp, mapped from YANG variable /stp/mstp (container)

    YANG Description: Multi Spanning-tree protocol configuration and operation
data
    """
    return self.__mstp
      
  def _set_mstp(self, v, load=False):
    """
    Setter method for mstp, mapped from YANG variable /stp/mstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mstp() directly.

    YANG Description: Multi Spanning-tree protocol configuration and operation
data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mstp.mstp, is_container='container', yang_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mstp.mstp, is_container='container', yang_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__mstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mstp(self):
    self.__mstp = YANGDynClass(base=mstp.mstp, is_container='container', yang_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)


  def _get_rapid_pvst(self):
    """
    Getter method for rapid_pvst, mapped from YANG variable /stp/rapid_pvst (container)

    YANG Description: Rapid per vlan Spanning-tree protocol configuration and
operational data
    """
    return self.__rapid_pvst
      
  def _set_rapid_pvst(self, v, load=False):
    """
    Setter method for rapid_pvst, mapped from YANG variable /stp/rapid_pvst (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rapid_pvst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rapid_pvst() directly.

    YANG Description: Rapid per vlan Spanning-tree protocol configuration and
operational data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rapid_pvst.rapid_pvst, is_container='container', yang_name="rapid-pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rapid_pvst must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rapid_pvst.rapid_pvst, is_container='container', yang_name="rapid-pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__rapid_pvst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rapid_pvst(self):
    self.__rapid_pvst = YANGDynClass(base=rapid_pvst.rapid_pvst, is_container='container', yang_name="rapid-pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /stp/interfaces (container)

    YANG Description: Enclosing container for the list of interface references
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /stp/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Enclosing container for the list of interface references
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  rstp = __builtin__.property(_get_rstp, _set_rstp)
  mstp = __builtin__.property(_get_mstp, _set_mstp)
  rapid_pvst = __builtin__.property(_get_rapid_pvst, _set_rapid_pvst)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('global_', global_), ('rstp', rstp), ('mstp', mstp), ('rapid_pvst', rapid_pvst), ('interfaces', interfaces), ])


from . import global_
from . import rstp
from . import mstp
from . import rapid_pvst
from . import interfaces
class stp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-spanning-tree - based on the path /stp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for spanning tree configuration and
state data
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__rstp','__mstp','__rapid_pvst','__interfaces',)

  _yang_name = 'stp'
  _yang_namespace = 'http://openconfig.net/yang/spanning-tree'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    self.__rstp = YANGDynClass(base=rstp.rstp, is_container='container', yang_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    self.__mstp = YANGDynClass(base=mstp.mstp, is_container='container', yang_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    self.__rapid_pvst = YANGDynClass(base=rapid_pvst.rapid_pvst, is_container='container', yang_name="rapid-pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)

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
      return ['stp']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /stp/global (container)

    YANG Description: Global configuration and state data
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /stp/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: Global configuration and state data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)


  def _get_rstp(self):
    """
    Getter method for rstp, mapped from YANG variable /stp/rstp (container)

    YANG Description: Rapid Spanning-tree protocol configuration and operation
data
    """
    return self.__rstp
      
  def _set_rstp(self, v, load=False):
    """
    Setter method for rstp, mapped from YANG variable /stp/rstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rstp() directly.

    YANG Description: Rapid Spanning-tree protocol configuration and operation
data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rstp.rstp, is_container='container', yang_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rstp.rstp, is_container='container', yang_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__rstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rstp(self):
    self.__rstp = YANGDynClass(base=rstp.rstp, is_container='container', yang_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)


  def _get_mstp(self):
    """
    Getter method for mstp, mapped from YANG variable /stp/mstp (container)

    YANG Description: Multi Spanning-tree protocol configuration and operation
data
    """
    return self.__mstp
      
  def _set_mstp(self, v, load=False):
    """
    Setter method for mstp, mapped from YANG variable /stp/mstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mstp() directly.

    YANG Description: Multi Spanning-tree protocol configuration and operation
data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mstp.mstp, is_container='container', yang_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mstp.mstp, is_container='container', yang_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__mstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mstp(self):
    self.__mstp = YANGDynClass(base=mstp.mstp, is_container='container', yang_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)


  def _get_rapid_pvst(self):
    """
    Getter method for rapid_pvst, mapped from YANG variable /stp/rapid_pvst (container)

    YANG Description: Rapid per vlan Spanning-tree protocol configuration and
operational data
    """
    return self.__rapid_pvst
      
  def _set_rapid_pvst(self, v, load=False):
    """
    Setter method for rapid_pvst, mapped from YANG variable /stp/rapid_pvst (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rapid_pvst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rapid_pvst() directly.

    YANG Description: Rapid per vlan Spanning-tree protocol configuration and
operational data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rapid_pvst.rapid_pvst, is_container='container', yang_name="rapid-pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rapid_pvst must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rapid_pvst.rapid_pvst, is_container='container', yang_name="rapid-pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__rapid_pvst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rapid_pvst(self):
    self.__rapid_pvst = YANGDynClass(base=rapid_pvst.rapid_pvst, is_container='container', yang_name="rapid-pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /stp/interfaces (container)

    YANG Description: Enclosing container for the list of interface references
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /stp/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Enclosing container for the list of interface references
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  rstp = __builtin__.property(_get_rstp, _set_rstp)
  mstp = __builtin__.property(_get_mstp, _set_mstp)
  rapid_pvst = __builtin__.property(_get_rapid_pvst, _set_rapid_pvst)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('global_', global_), ('rstp', rstp), ('mstp', mstp), ('rapid_pvst', rapid_pvst), ('interfaces', interfaces), ])


