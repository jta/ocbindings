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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/rates/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for operational state representing
interface rates.
  """
  __slots__ = ('_path_helper', '_extmethods', '__load_interval','__out_bits_rate','__in_bits_rate','__out_pkts_rate','__in_pkts_rate',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__load_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="load-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint16', is_config=False)
    self.__out_bits_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    self.__in_bits_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    self.__out_pkts_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    self.__in_pkts_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)

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
      return ['interfaces', 'interface', 'rates', 'state']

  def _get_load_interval(self):
    """
    Getter method for load_interval, mapped from YANG variable /interfaces/interface/rates/state/load_interval (uint16)

    YANG Description: The interval of interface rates calculation in seconds
    """
    return self.__load_interval
      
  def _set_load_interval(self, v, load=False):
    """
    Setter method for load_interval, mapped from YANG variable /interfaces/interface/rates/state/load_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_interval() directly.

    YANG Description: The interval of interface rates calculation in seconds
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="load-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="load-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint16', is_config=False)""",
        })

    self.__load_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_interval(self):
    self.__load_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="load-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint16', is_config=False)


  def _get_out_bits_rate(self):
    """
    Getter method for out_bits_rate, mapped from YANG variable /interfaces/interface/rates/state/out_bits_rate (uint64)

    YANG Description: The calculated transmitted rate of the interface, measured in bits
per second.
    """
    return self.__out_bits_rate
      
  def _set_out_bits_rate(self, v, load=False):
    """
    Setter method for out_bits_rate, mapped from YANG variable /interfaces/interface/rates/state/out_bits_rate (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_bits_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_bits_rate() directly.

    YANG Description: The calculated transmitted rate of the interface, measured in bits
per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_bits_rate must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)""",
        })

    self.__out_bits_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_bits_rate(self):
    self.__out_bits_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)


  def _get_in_bits_rate(self):
    """
    Getter method for in_bits_rate, mapped from YANG variable /interfaces/interface/rates/state/in_bits_rate (uint64)

    YANG Description: The calculated received rate of the interface, measured in bits
per second.
    """
    return self.__in_bits_rate
      
  def _set_in_bits_rate(self, v, load=False):
    """
    Setter method for in_bits_rate, mapped from YANG variable /interfaces/interface/rates/state/in_bits_rate (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_bits_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_bits_rate() directly.

    YANG Description: The calculated received rate of the interface, measured in bits
per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_bits_rate must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)""",
        })

    self.__in_bits_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_bits_rate(self):
    self.__in_bits_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)


  def _get_out_pkts_rate(self):
    """
    Getter method for out_pkts_rate, mapped from YANG variable /interfaces/interface/rates/state/out_pkts_rate (uint64)

    YANG Description: The calculated transmitted rate of the interface, measured in packets
per second.
    """
    return self.__out_pkts_rate
      
  def _set_out_pkts_rate(self, v, load=False):
    """
    Setter method for out_pkts_rate, mapped from YANG variable /interfaces/interface/rates/state/out_pkts_rate (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_pkts_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_pkts_rate() directly.

    YANG Description: The calculated transmitted rate of the interface, measured in packets
per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_pkts_rate must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)""",
        })

    self.__out_pkts_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_pkts_rate(self):
    self.__out_pkts_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)


  def _get_in_pkts_rate(self):
    """
    Getter method for in_pkts_rate, mapped from YANG variable /interfaces/interface/rates/state/in_pkts_rate (uint64)

    YANG Description: The calculated received rate of the interface, measured in packets
per second.
    """
    return self.__in_pkts_rate
      
  def _set_in_pkts_rate(self, v, load=False):
    """
    Setter method for in_pkts_rate, mapped from YANG variable /interfaces/interface/rates/state/in_pkts_rate (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_pkts_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_pkts_rate() directly.

    YANG Description: The calculated received rate of the interface, measured in packets
per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_pkts_rate must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)""",
        })

    self.__in_pkts_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_pkts_rate(self):
    self.__in_pkts_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)

  load_interval = __builtin__.property(_get_load_interval)
  out_bits_rate = __builtin__.property(_get_out_bits_rate)
  in_bits_rate = __builtin__.property(_get_in_bits_rate)
  out_pkts_rate = __builtin__.property(_get_out_pkts_rate)
  in_pkts_rate = __builtin__.property(_get_in_pkts_rate)


  _pyangbind_elements = OrderedDict([('load_interval', load_interval), ('out_bits_rate', out_bits_rate), ('in_bits_rate', in_bits_rate), ('out_pkts_rate', out_pkts_rate), ('in_pkts_rate', in_pkts_rate), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/rates/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for operational state representing
interface rates.
  """
  __slots__ = ('_path_helper', '_extmethods', '__load_interval','__out_bits_rate','__in_bits_rate','__out_pkts_rate','__in_pkts_rate',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/interfaces'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__load_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="load-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint16', is_config=False)
    self.__out_bits_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    self.__in_bits_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    self.__out_pkts_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    self.__in_pkts_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)

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
      return ['interfaces', 'interface', 'rates', 'state']

  def _get_load_interval(self):
    """
    Getter method for load_interval, mapped from YANG variable /interfaces/interface/rates/state/load_interval (uint16)

    YANG Description: The interval of interface rates calculation in seconds
    """
    return self.__load_interval
      
  def _set_load_interval(self, v, load=False):
    """
    Setter method for load_interval, mapped from YANG variable /interfaces/interface/rates/state/load_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_interval() directly.

    YANG Description: The interval of interface rates calculation in seconds
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="load-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="load-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint16', is_config=False)""",
        })

    self.__load_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_interval(self):
    self.__load_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="load-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint16', is_config=False)


  def _get_out_bits_rate(self):
    """
    Getter method for out_bits_rate, mapped from YANG variable /interfaces/interface/rates/state/out_bits_rate (uint64)

    YANG Description: The calculated transmitted rate of the interface, measured in bits
per second.
    """
    return self.__out_bits_rate
      
  def _set_out_bits_rate(self, v, load=False):
    """
    Setter method for out_bits_rate, mapped from YANG variable /interfaces/interface/rates/state/out_bits_rate (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_bits_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_bits_rate() directly.

    YANG Description: The calculated transmitted rate of the interface, measured in bits
per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_bits_rate must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)""",
        })

    self.__out_bits_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_bits_rate(self):
    self.__out_bits_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)


  def _get_in_bits_rate(self):
    """
    Getter method for in_bits_rate, mapped from YANG variable /interfaces/interface/rates/state/in_bits_rate (uint64)

    YANG Description: The calculated received rate of the interface, measured in bits
per second.
    """
    return self.__in_bits_rate
      
  def _set_in_bits_rate(self, v, load=False):
    """
    Setter method for in_bits_rate, mapped from YANG variable /interfaces/interface/rates/state/in_bits_rate (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_bits_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_bits_rate() directly.

    YANG Description: The calculated received rate of the interface, measured in bits
per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_bits_rate must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)""",
        })

    self.__in_bits_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_bits_rate(self):
    self.__in_bits_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-bits-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)


  def _get_out_pkts_rate(self):
    """
    Getter method for out_pkts_rate, mapped from YANG variable /interfaces/interface/rates/state/out_pkts_rate (uint64)

    YANG Description: The calculated transmitted rate of the interface, measured in packets
per second.
    """
    return self.__out_pkts_rate
      
  def _set_out_pkts_rate(self, v, load=False):
    """
    Setter method for out_pkts_rate, mapped from YANG variable /interfaces/interface/rates/state/out_pkts_rate (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_pkts_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_pkts_rate() directly.

    YANG Description: The calculated transmitted rate of the interface, measured in packets
per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_pkts_rate must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)""",
        })

    self.__out_pkts_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_pkts_rate(self):
    self.__out_pkts_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)


  def _get_in_pkts_rate(self):
    """
    Getter method for in_pkts_rate, mapped from YANG variable /interfaces/interface/rates/state/in_pkts_rate (uint64)

    YANG Description: The calculated received rate of the interface, measured in packets
per second.
    """
    return self.__in_pkts_rate
      
  def _set_in_pkts_rate(self, v, load=False):
    """
    Setter method for in_pkts_rate, mapped from YANG variable /interfaces/interface/rates/state/in_pkts_rate (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_pkts_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_pkts_rate() directly.

    YANG Description: The calculated received rate of the interface, measured in packets
per second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_pkts_rate must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)""",
        })

    self.__in_pkts_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_pkts_rate(self):
    self.__in_pkts_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/rates', defining_module='openconfig-if-rates', yang_type='uint64', is_config=False)

  load_interval = __builtin__.property(_get_load_interval)
  out_bits_rate = __builtin__.property(_get_out_bits_rate)
  in_bits_rate = __builtin__.property(_get_in_bits_rate)
  out_pkts_rate = __builtin__.property(_get_out_pkts_rate)
  in_pkts_rate = __builtin__.property(_get_in_pkts_rate)


  _pyangbind_elements = OrderedDict([('load_interval', load_interval), ('out_bits_rate', out_bits_rate), ('in_bits_rate', in_bits_rate), ('out_pkts_rate', out_pkts_rate), ('in_pkts_rate', in_pkts_rate), ])


