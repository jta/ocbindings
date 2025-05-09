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
  from YANG module openconfig-spanning-tree - based on the path /stp/rstp/interfaces/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for STP on each interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__cost','__port_priority',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/spanning-tree'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-if:base-interface-ref', is_config=True)
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..200000000']}), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=True)
    self.__port_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..240']}), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-port-priority-type', is_config=True)

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
      return ['stp', 'rstp', 'interfaces', 'interface', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /stp/rstp/interfaces/interface/config/name (oc-if:base-interface-ref)

    YANG Description: Reference to the STP ethernet interface
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /stp/rstp/interfaces/interface/config/name (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference to the STP ethernet interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-if:base-interface-ref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-if:base-interface-ref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-if:base-interface-ref', is_config=True)


  def _get_cost(self):
    """
    Getter method for cost, mapped from YANG variable /stp/rstp/interfaces/interface/config/cost (uint32)

    YANG Description: The port's contribution, when it is the Root Port,
to the Root Path Cost for the Bridge
    """
    return self.__cost
      
  def _set_cost(self, v, load=False):
    """
    Setter method for cost, mapped from YANG variable /stp/rstp/interfaces/interface/config/cost (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cost is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cost() directly.

    YANG Description: The port's contribution, when it is the Root Port,
to the Root Path Cost for the Bridge
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..200000000']}), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cost must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..200000000']}), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=True)""",
        })

    self.__cost = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cost(self):
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..200000000']}), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=True)


  def _get_port_priority(self):
    """
    Getter method for port_priority, mapped from YANG variable /stp/rstp/interfaces/interface/config/port_priority (oc-stp-types:stp-port-priority-type)

    YANG Description: The manageable component of the Port Identifier,
also known as the Port Priority
    """
    return self.__port_priority
      
  def _set_port_priority(self, v, load=False):
    """
    Setter method for port_priority, mapped from YANG variable /stp/rstp/interfaces/interface/config/port_priority (oc-stp-types:stp-port-priority-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_priority() directly.

    YANG Description: The manageable component of the Port Identifier,
also known as the Port Priority
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..240']}), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-port-priority-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_priority must be of a type compatible with oc-stp-types:stp-port-priority-type""",
          'defined-type': "oc-stp-types:stp-port-priority-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..240']}), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-port-priority-type', is_config=True)""",
        })

    self.__port_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_priority(self):
    self.__port_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..240']}), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-port-priority-type', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  cost = __builtin__.property(_get_cost, _set_cost)
  port_priority = __builtin__.property(_get_port_priority, _set_port_priority)


  _pyangbind_elements = OrderedDict([('name', name), ('cost', cost), ('port_priority', port_priority), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-spanning-tree - based on the path /stp/rstp/interfaces/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for STP on each interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__cost','__port_priority',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/spanning-tree'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-if:base-interface-ref', is_config=True)
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..200000000']}), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=True)
    self.__port_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..240']}), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-port-priority-type', is_config=True)

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
      return ['stp', 'rstp', 'interfaces', 'interface', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /stp/rstp/interfaces/interface/config/name (oc-if:base-interface-ref)

    YANG Description: Reference to the STP ethernet interface
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /stp/rstp/interfaces/interface/config/name (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference to the STP ethernet interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-if:base-interface-ref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-if:base-interface-ref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-if:base-interface-ref', is_config=True)


  def _get_cost(self):
    """
    Getter method for cost, mapped from YANG variable /stp/rstp/interfaces/interface/config/cost (uint32)

    YANG Description: The port's contribution, when it is the Root Port,
to the Root Path Cost for the Bridge
    """
    return self.__cost
      
  def _set_cost(self, v, load=False):
    """
    Setter method for cost, mapped from YANG variable /stp/rstp/interfaces/interface/config/cost (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cost is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cost() directly.

    YANG Description: The port's contribution, when it is the Root Port,
to the Root Path Cost for the Bridge
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..200000000']}), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cost must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..200000000']}), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=True)""",
        })

    self.__cost = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cost(self):
    self.__cost = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..200000000']}), is_leaf=True, yang_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=True)


  def _get_port_priority(self):
    """
    Getter method for port_priority, mapped from YANG variable /stp/rstp/interfaces/interface/config/port_priority (oc-stp-types:stp-port-priority-type)

    YANG Description: The manageable component of the Port Identifier,
also known as the Port Priority
    """
    return self.__port_priority
      
  def _set_port_priority(self, v, load=False):
    """
    Setter method for port_priority, mapped from YANG variable /stp/rstp/interfaces/interface/config/port_priority (oc-stp-types:stp-port-priority-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_priority() directly.

    YANG Description: The manageable component of the Port Identifier,
also known as the Port Priority
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..240']}), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-port-priority-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_priority must be of a type compatible with oc-stp-types:stp-port-priority-type""",
          'defined-type': "oc-stp-types:stp-port-priority-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..240']}), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-port-priority-type', is_config=True)""",
        })

    self.__port_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_priority(self):
    self.__port_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..240']}), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-port-priority-type', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  cost = __builtin__.property(_get_cost, _set_cost)
  port_priority = __builtin__.property(_get_port_priority, _set_port_priority)


  _pyangbind_elements = OrderedDict([('name', name), ('cost', cost), ('port_priority', port_priority), ])


