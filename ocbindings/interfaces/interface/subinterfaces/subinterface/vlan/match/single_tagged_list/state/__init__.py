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
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/vlan/match/single-tagged-list/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State for matching single-tagged packets with a list of VLAN
identifiers.
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_ids',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_ids = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']})), is_leaf=False, yang_name="vlan-ids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=False)

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
      return ['interfaces', 'interface', 'subinterfaces', 'subinterface', 'vlan', 'match', 'single-tagged-list', 'state']

  def _get_vlan_ids(self):
    """
    Getter method for vlan_ids, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/single_tagged_list/state/vlan_ids (oc-vlan-types:vlan-id)

    YANG Description: VLAN identifiers for single-tagged packets.
    """
    return self.__vlan_ids
      
  def _set_vlan_ids(self, v, load=False):
    """
    Setter method for vlan_ids, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/single_tagged_list/state/vlan_ids (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_ids is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_ids() directly.

    YANG Description: VLAN identifiers for single-tagged packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']})), is_leaf=False, yang_name="vlan-ids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_ids must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']})), is_leaf=False, yang_name="vlan-ids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=False)""",
        })

    self.__vlan_ids = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_ids(self):
    self.__vlan_ids = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']})), is_leaf=False, yang_name="vlan-ids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=False)

  vlan_ids = __builtin__.property(_get_vlan_ids)


  _pyangbind_elements = OrderedDict([('vlan_ids', vlan_ids), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/vlan/match/single-tagged-list/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State for matching single-tagged packets with a list of VLAN
identifiers.
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_ids',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_ids = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']})), is_leaf=False, yang_name="vlan-ids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=False)

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
      return ['interfaces', 'interface', 'subinterfaces', 'subinterface', 'vlan', 'match', 'single-tagged-list', 'state']

  def _get_vlan_ids(self):
    """
    Getter method for vlan_ids, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/single_tagged_list/state/vlan_ids (oc-vlan-types:vlan-id)

    YANG Description: VLAN identifiers for single-tagged packets.
    """
    return self.__vlan_ids
      
  def _set_vlan_ids(self, v, load=False):
    """
    Setter method for vlan_ids, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/single_tagged_list/state/vlan_ids (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_ids is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_ids() directly.

    YANG Description: VLAN identifiers for single-tagged packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']})), is_leaf=False, yang_name="vlan-ids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_ids must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']})), is_leaf=False, yang_name="vlan-ids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=False)""",
        })

    self.__vlan_ids = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_ids(self):
    self.__vlan_ids = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']})), is_leaf=False, yang_name="vlan-ids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=False)

  vlan_ids = __builtin__.property(_get_vlan_ids)


  _pyangbind_elements = OrderedDict([('vlan_ids', vlan_ids), ])


