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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/vlan/match/double-tagged-inner-outer-range/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration for matching double-tagged packets against an
inner range and an outer range of VLAN identifiers.
  """
  __slots__ = ('_path_helper', '_extmethods', '__inner_low_vlan_id','__inner_high_vlan_id','__outer_low_vlan_id','__outer_high_vlan_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__inner_low_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__inner_high_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__outer_low_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__outer_high_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)

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
      return ['interfaces', 'interface', 'subinterfaces', 'subinterface', 'vlan', 'match', 'double-tagged-inner-outer-range', 'config']

  def _get_inner_low_vlan_id(self):
    """
    Getter method for inner_low_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/inner_low_vlan_id (oc-vlan-types:vlan-id)

    YANG Description: The low-value inner VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    return self.__inner_low_vlan_id
      
  def _set_inner_low_vlan_id(self, v, load=False):
    """
    Setter method for inner_low_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/inner_low_vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inner_low_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inner_low_vlan_id() directly.

    YANG Description: The low-value inner VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inner_low_vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__inner_low_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inner_low_vlan_id(self):
    self.__inner_low_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_inner_high_vlan_id(self):
    """
    Getter method for inner_high_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/inner_high_vlan_id (oc-vlan-types:vlan-id)

    YANG Description: The high-value inner VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    return self.__inner_high_vlan_id
      
  def _set_inner_high_vlan_id(self, v, load=False):
    """
    Setter method for inner_high_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/inner_high_vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inner_high_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inner_high_vlan_id() directly.

    YANG Description: The high-value inner VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inner_high_vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__inner_high_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inner_high_vlan_id(self):
    self.__inner_high_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_outer_low_vlan_id(self):
    """
    Getter method for outer_low_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/outer_low_vlan_id (oc-vlan-types:vlan-id)

    YANG Description: The low-value outer VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    return self.__outer_low_vlan_id
      
  def _set_outer_low_vlan_id(self, v, load=False):
    """
    Setter method for outer_low_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/outer_low_vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_outer_low_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_outer_low_vlan_id() directly.

    YANG Description: The low-value outer VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """outer_low_vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__outer_low_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_outer_low_vlan_id(self):
    self.__outer_low_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_outer_high_vlan_id(self):
    """
    Getter method for outer_high_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/outer_high_vlan_id (oc-vlan-types:vlan-id)

    YANG Description: The high-value outer VLAN identifier for double-tagged packets.
The range is matched inclusively.
    """
    return self.__outer_high_vlan_id
      
  def _set_outer_high_vlan_id(self, v, load=False):
    """
    Setter method for outer_high_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/outer_high_vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_outer_high_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_outer_high_vlan_id() directly.

    YANG Description: The high-value outer VLAN identifier for double-tagged packets.
The range is matched inclusively.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """outer_high_vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__outer_high_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_outer_high_vlan_id(self):
    self.__outer_high_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)

  inner_low_vlan_id = __builtin__.property(_get_inner_low_vlan_id, _set_inner_low_vlan_id)
  inner_high_vlan_id = __builtin__.property(_get_inner_high_vlan_id, _set_inner_high_vlan_id)
  outer_low_vlan_id = __builtin__.property(_get_outer_low_vlan_id, _set_outer_low_vlan_id)
  outer_high_vlan_id = __builtin__.property(_get_outer_high_vlan_id, _set_outer_high_vlan_id)


  _pyangbind_elements = OrderedDict([('inner_low_vlan_id', inner_low_vlan_id), ('inner_high_vlan_id', inner_high_vlan_id), ('outer_low_vlan_id', outer_low_vlan_id), ('outer_high_vlan_id', outer_high_vlan_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/vlan/match/double-tagged-inner-outer-range/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration for matching double-tagged packets against an
inner range and an outer range of VLAN identifiers.
  """
  __slots__ = ('_path_helper', '_extmethods', '__inner_low_vlan_id','__inner_high_vlan_id','__outer_low_vlan_id','__outer_high_vlan_id',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__inner_low_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__inner_high_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__outer_low_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__outer_high_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)

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
      return ['interfaces', 'interface', 'subinterfaces', 'subinterface', 'vlan', 'match', 'double-tagged-inner-outer-range', 'config']

  def _get_inner_low_vlan_id(self):
    """
    Getter method for inner_low_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/inner_low_vlan_id (oc-vlan-types:vlan-id)

    YANG Description: The low-value inner VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    return self.__inner_low_vlan_id
      
  def _set_inner_low_vlan_id(self, v, load=False):
    """
    Setter method for inner_low_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/inner_low_vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inner_low_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inner_low_vlan_id() directly.

    YANG Description: The low-value inner VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inner_low_vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__inner_low_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inner_low_vlan_id(self):
    self.__inner_low_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_inner_high_vlan_id(self):
    """
    Getter method for inner_high_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/inner_high_vlan_id (oc-vlan-types:vlan-id)

    YANG Description: The high-value inner VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    return self.__inner_high_vlan_id
      
  def _set_inner_high_vlan_id(self, v, load=False):
    """
    Setter method for inner_high_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/inner_high_vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inner_high_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inner_high_vlan_id() directly.

    YANG Description: The high-value inner VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inner_high_vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__inner_high_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inner_high_vlan_id(self):
    self.__inner_high_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="inner-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_outer_low_vlan_id(self):
    """
    Getter method for outer_low_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/outer_low_vlan_id (oc-vlan-types:vlan-id)

    YANG Description: The low-value outer VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    return self.__outer_low_vlan_id
      
  def _set_outer_low_vlan_id(self, v, load=False):
    """
    Setter method for outer_low_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/outer_low_vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_outer_low_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_outer_low_vlan_id() directly.

    YANG Description: The low-value outer VLAN identifier in a range for double-tagged
packets. The range is matched inclusively.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """outer_low_vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__outer_low_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_outer_low_vlan_id(self):
    self.__outer_low_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-low-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_outer_high_vlan_id(self):
    """
    Getter method for outer_high_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/outer_high_vlan_id (oc-vlan-types:vlan-id)

    YANG Description: The high-value outer VLAN identifier for double-tagged packets.
The range is matched inclusively.
    """
    return self.__outer_high_vlan_id
      
  def _set_outer_high_vlan_id(self, v, load=False):
    """
    Setter method for outer_high_vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match/double_tagged_inner_outer_range/config/outer_high_vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_outer_high_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_outer_high_vlan_id() directly.

    YANG Description: The high-value outer VLAN identifier for double-tagged packets.
The range is matched inclusively.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """outer_high_vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__outer_high_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_outer_high_vlan_id(self):
    self.__outer_high_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="outer-high-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)

  inner_low_vlan_id = __builtin__.property(_get_inner_low_vlan_id, _set_inner_low_vlan_id)
  inner_high_vlan_id = __builtin__.property(_get_inner_high_vlan_id, _set_inner_high_vlan_id)
  outer_low_vlan_id = __builtin__.property(_get_outer_low_vlan_id, _set_outer_low_vlan_id)
  outer_high_vlan_id = __builtin__.property(_get_outer_high_vlan_id, _set_outer_high_vlan_id)


  _pyangbind_elements = OrderedDict([('inner_low_vlan_id', inner_low_vlan_id), ('inner_high_vlan_id', inner_high_vlan_id), ('outer_low_vlan_id', outer_low_vlan_id), ('outer_high_vlan_id', outer_high_vlan_id), ])


