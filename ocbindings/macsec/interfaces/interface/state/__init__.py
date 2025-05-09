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
from . import counters
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__enable','__replay_protection','__counters',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/macsec'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-if:base-interface-ref', is_config=False)
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='boolean', is_config=False)
    self.__replay_protection = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="replay-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='uint16', is_config=False)
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='container', is_config=False)

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
      return ['macsec', 'interfaces', 'interface', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /macsec/interfaces/interface/state/name (oc-if:base-interface-ref)

    YANG Description: Reference to the MACsec Ethernet interface
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /macsec/interfaces/interface/state/name (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference to the MACsec Ethernet interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-if:base-interface-ref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-if:base-interface-ref', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-if:base-interface-ref', is_config=False)


  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /macsec/interfaces/interface/state/enable (boolean)

    YANG Description: Enable MACsec on an interface
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /macsec/interfaces/interface/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enable MACsec on an interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='boolean', is_config=False)


  def _get_replay_protection(self):
    """
    Getter method for replay_protection, mapped from YANG variable /macsec/interfaces/interface/state/replay_protection (uint16)

    YANG Description: MACsec window size, as defined by the number of out-of-order frames
that are accepted. A value of 0 means that frames are accepted only in
the correct order.
    """
    return self.__replay_protection
      
  def _set_replay_protection(self, v, load=False):
    """
    Setter method for replay_protection, mapped from YANG variable /macsec/interfaces/interface/state/replay_protection (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_replay_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_replay_protection() directly.

    YANG Description: MACsec window size, as defined by the number of out-of-order frames
that are accepted. A value of 0 means that frames are accepted only in
the correct order.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="replay-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """replay_protection must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="replay-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='uint16', is_config=False)""",
        })

    self.__replay_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_replay_protection(self):
    self.__replay_protection = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="replay-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='uint16', is_config=False)


  def _get_counters(self):
    """
    Getter method for counters, mapped from YANG variable /macsec/interfaces/interface/state/counters (container)

    YANG Description: MACsec interface counters
    """
    return self.__counters
      
  def _set_counters(self, v, load=False):
    """
    Setter method for counters, mapped from YANG variable /macsec/interfaces/interface/state/counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counters() directly.

    YANG Description: MACsec interface counters
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """counters must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='container', is_config=False)""",
        })

    self.__counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_counters(self):
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='container', is_config=False)

  name = __builtin__.property(_get_name)
  enable = __builtin__.property(_get_enable)
  replay_protection = __builtin__.property(_get_replay_protection)
  counters = __builtin__.property(_get_counters)


  _pyangbind_elements = OrderedDict([('name', name), ('enable', enable), ('replay_protection', replay_protection), ('counters', counters), ])


from . import counters
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__enable','__replay_protection','__counters',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/macsec'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-if:base-interface-ref', is_config=False)
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='boolean', is_config=False)
    self.__replay_protection = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="replay-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='uint16', is_config=False)
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='container', is_config=False)

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
      return ['macsec', 'interfaces', 'interface', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /macsec/interfaces/interface/state/name (oc-if:base-interface-ref)

    YANG Description: Reference to the MACsec Ethernet interface
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /macsec/interfaces/interface/state/name (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference to the MACsec Ethernet interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-if:base-interface-ref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-if:base-interface-ref', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-if:base-interface-ref', is_config=False)


  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /macsec/interfaces/interface/state/enable (boolean)

    YANG Description: Enable MACsec on an interface
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /macsec/interfaces/interface/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enable MACsec on an interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='boolean', is_config=False)


  def _get_replay_protection(self):
    """
    Getter method for replay_protection, mapped from YANG variable /macsec/interfaces/interface/state/replay_protection (uint16)

    YANG Description: MACsec window size, as defined by the number of out-of-order frames
that are accepted. A value of 0 means that frames are accepted only in
the correct order.
    """
    return self.__replay_protection
      
  def _set_replay_protection(self, v, load=False):
    """
    Setter method for replay_protection, mapped from YANG variable /macsec/interfaces/interface/state/replay_protection (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_replay_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_replay_protection() directly.

    YANG Description: MACsec window size, as defined by the number of out-of-order frames
that are accepted. A value of 0 means that frames are accepted only in
the correct order.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="replay-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """replay_protection must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="replay-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='uint16', is_config=False)""",
        })

    self.__replay_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_replay_protection(self):
    self.__replay_protection = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="replay-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='uint16', is_config=False)


  def _get_counters(self):
    """
    Getter method for counters, mapped from YANG variable /macsec/interfaces/interface/state/counters (container)

    YANG Description: MACsec interface counters
    """
    return self.__counters
      
  def _set_counters(self, v, load=False):
    """
    Setter method for counters, mapped from YANG variable /macsec/interfaces/interface/state/counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counters() directly.

    YANG Description: MACsec interface counters
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """counters must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='container', is_config=False)""",
        })

    self.__counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_counters(self):
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='container', is_config=False)

  name = __builtin__.property(_get_name)
  enable = __builtin__.property(_get_enable)
  replay_protection = __builtin__.property(_get_replay_protection)
  counters = __builtin__.property(_get_counters)


  _pyangbind_elements = OrderedDict([('name', name), ('enable', enable), ('replay_protection', replay_protection), ('counters', counters), ])


