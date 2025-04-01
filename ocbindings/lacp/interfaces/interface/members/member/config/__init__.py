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
  from YANG module openconfig-lacp - based on the path /lacp/interfaces/interface/members/member/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for aggregate members
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface','__port_priority',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/lacp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface = YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='oc-if:base-interface-ref', is_config=True)
    self.__port_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='uint16', is_config=True)

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
      return ['lacp', 'interfaces', 'interface', 'members', 'member', 'config']

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /lacp/interfaces/interface/members/member/config/interface (oc-if:base-interface-ref)

    YANG Description: Reference to interface member of the LACP aggregate
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /lacp/interfaces/interface/members/member/config/interface (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Reference to interface member of the LACP aggregate
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='oc-if:base-interface-ref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='oc-if:base-interface-ref', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='oc-if:base-interface-ref', is_config=True)


  def _get_port_priority(self):
    """
    Getter method for port_priority, mapped from YANG variable /lacp/interfaces/interface/members/member/config/port_priority (uint16)

    YANG Description: Member interface's priority in its aggregate interface.
    """
    return self.__port_priority
      
  def _set_port_priority(self, v, load=False):
    """
    Setter method for port_priority, mapped from YANG variable /lacp/interfaces/interface/members/member/config/port_priority (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_priority() directly.

    YANG Description: Member interface's priority in its aggregate interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_priority must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='uint16', is_config=True)""",
        })

    self.__port_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_priority(self):
    self.__port_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='uint16', is_config=True)

  interface = __builtin__.property(_get_interface, _set_interface)
  port_priority = __builtin__.property(_get_port_priority, _set_port_priority)


  _pyangbind_elements = OrderedDict([('interface', interface), ('port_priority', port_priority), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-lacp - based on the path /lacp/interfaces/interface/members/member/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for aggregate members
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface','__port_priority',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/lacp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface = YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='oc-if:base-interface-ref', is_config=True)
    self.__port_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='uint16', is_config=True)

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
      return ['lacp', 'interfaces', 'interface', 'members', 'member', 'config']

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /lacp/interfaces/interface/members/member/config/interface (oc-if:base-interface-ref)

    YANG Description: Reference to interface member of the LACP aggregate
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /lacp/interfaces/interface/members/member/config/interface (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Reference to interface member of the LACP aggregate
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='oc-if:base-interface-ref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='oc-if:base-interface-ref', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='oc-if:base-interface-ref', is_config=True)


  def _get_port_priority(self):
    """
    Getter method for port_priority, mapped from YANG variable /lacp/interfaces/interface/members/member/config/port_priority (uint16)

    YANG Description: Member interface's priority in its aggregate interface.
    """
    return self.__port_priority
      
  def _set_port_priority(self, v, load=False):
    """
    Setter method for port_priority, mapped from YANG variable /lacp/interfaces/interface/members/member/config/port_priority (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_priority() directly.

    YANG Description: Member interface's priority in its aggregate interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_priority must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='uint16', is_config=True)""",
        })

    self.__port_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_priority(self):
    self.__port_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lacp', defining_module='openconfig-lacp', yang_type='uint16', is_config=True)

  interface = __builtin__.property(_get_interface, _set_interface)
  port_priority = __builtin__.property(_get_port_priority, _set_port_priority)


  _pyangbind_elements = OrderedDict([('interface', interface), ('port_priority', port_priority), ])


