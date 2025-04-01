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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/ethernet/switched-vlan/dot1x-vlan-map/vlan-name/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each configured VLAN
name in the VLAN ID to VLAN name mapping
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_name','__id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_name = YANGDynClass(base=str, is_leaf=True, yang_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='string', is_config=True)
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='oc-vlan-types:vlan-id', is_config=True)

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
      return ['interfaces', 'interface', 'ethernet', 'switched-vlan', 'dot1x-vlan-map', 'vlan-name', 'config']

  def _get_vlan_name(self):
    """
    Getter method for vlan_name, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map/vlan_name/config/vlan_name (string)

    YANG Description: The VLAN name to be mapped to the VLAN id.
    """
    return self.__vlan_name
      
  def _set_vlan_name(self, v, load=False):
    """
    Setter method for vlan_name, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map/vlan_name/config/vlan_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_name() directly.

    YANG Description: The VLAN name to be mapped to the VLAN id.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='string', is_config=True)""",
        })

    self.__vlan_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_name(self):
    self.__vlan_name = YANGDynClass(base=str, is_leaf=True, yang_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='string', is_config=True)


  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map/vlan_name/config/id (oc-vlan-types:vlan-id)

    YANG Description: The VLAN id to be mapped to the VLAN name.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map/vlan_name/config/id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: The VLAN id to be mapped to the VLAN name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='oc-vlan-types:vlan-id', is_config=True)

  vlan_name = __builtin__.property(_get_vlan_name, _set_vlan_name)
  id = __builtin__.property(_get_id, _set_id)


  _pyangbind_elements = OrderedDict([('vlan_name', vlan_name), ('id', id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/ethernet/switched-vlan/dot1x-vlan-map/vlan-name/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each configured VLAN
name in the VLAN ID to VLAN name mapping
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_name','__id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_name = YANGDynClass(base=str, is_leaf=True, yang_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='string', is_config=True)
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='oc-vlan-types:vlan-id', is_config=True)

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
      return ['interfaces', 'interface', 'ethernet', 'switched-vlan', 'dot1x-vlan-map', 'vlan-name', 'config']

  def _get_vlan_name(self):
    """
    Getter method for vlan_name, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map/vlan_name/config/vlan_name (string)

    YANG Description: The VLAN name to be mapped to the VLAN id.
    """
    return self.__vlan_name
      
  def _set_vlan_name(self, v, load=False):
    """
    Setter method for vlan_name, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map/vlan_name/config/vlan_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_name() directly.

    YANG Description: The VLAN name to be mapped to the VLAN id.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='string', is_config=True)""",
        })

    self.__vlan_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_name(self):
    self.__vlan_name = YANGDynClass(base=str, is_leaf=True, yang_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='string', is_config=True)


  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map/vlan_name/config/id (oc-vlan-types:vlan-id)

    YANG Description: The VLAN id to be mapped to the VLAN name.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/dot1x_vlan_map/vlan_name/config/id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: The VLAN id to be mapped to the VLAN name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='oc-vlan-types:vlan-id', is_config=True)

  vlan_name = __builtin__.property(_get_vlan_name, _set_vlan_name)
  id = __builtin__.property(_get_id, _set_id)


  _pyangbind_elements = OrderedDict([('vlan_name', vlan_name), ('id', id), ])


