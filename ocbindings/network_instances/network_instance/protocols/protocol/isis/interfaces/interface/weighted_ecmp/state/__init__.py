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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/weighted-ecmp/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for weighted ecmp
  """
  __slots__ = ('_path_helper', '_extmethods', '__load_balancing_weight',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__load_balancing_weight = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'weighted-ecmp', 'state']

  def _get_load_balancing_weight(self):
    """
    Getter method for load_balancing_weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/weighted_ecmp/state/load_balancing_weight (union)

    YANG Description: The load-balancing weight of the interface, which applies when
weighted ECMP is enabled and the interface is part of a multipath set.
    """
    return self.__load_balancing_weight
      
  def _set_load_balancing_weight(self, v, load=False):
    """
    Setter method for load_balancing_weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/weighted_ecmp/state/load_balancing_weight (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_balancing_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_balancing_weight() directly.

    YANG Description: The load-balancing weight of the interface, which applies when
weighted ECMP is enabled and the interface is part of a multipath set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_balancing_weight must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__load_balancing_weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_balancing_weight(self):
    self.__load_balancing_weight = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  load_balancing_weight = __builtin__.property(_get_load_balancing_weight)


  _pyangbind_elements = OrderedDict([('load_balancing_weight', load_balancing_weight), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/weighted-ecmp/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for weighted ecmp
  """
  __slots__ = ('_path_helper', '_extmethods', '__load_balancing_weight',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__load_balancing_weight = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'weighted-ecmp', 'state']

  def _get_load_balancing_weight(self):
    """
    Getter method for load_balancing_weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/weighted_ecmp/state/load_balancing_weight (union)

    YANG Description: The load-balancing weight of the interface, which applies when
weighted ECMP is enabled and the interface is part of a multipath set.
    """
    return self.__load_balancing_weight
      
  def _set_load_balancing_weight(self, v, load=False):
    """
    Setter method for load_balancing_weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/weighted_ecmp/state/load_balancing_weight (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_balancing_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_balancing_weight() directly.

    YANG Description: The load-balancing weight of the interface, which applies when
weighted ECMP is enabled and the interface is part of a multipath set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_balancing_weight must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__load_balancing_weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_balancing_weight(self):
    self.__load_balancing_weight = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  load_balancing_weight = __builtin__.property(_get_load_balancing_weight)


  _pyangbind_elements = OrderedDict([('load_balancing_weight', load_balancing_weight), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/weighted-ecmp/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for weighted ecmp
  """
  __slots__ = ('_path_helper', '_extmethods', '__load_balancing_weight',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__load_balancing_weight = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'weighted-ecmp', 'state']

  def _get_load_balancing_weight(self):
    """
    Getter method for load_balancing_weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/weighted_ecmp/state/load_balancing_weight (union)

    YANG Description: The load-balancing weight of the interface, which applies when
weighted ECMP is enabled and the interface is part of a multipath set.
    """
    return self.__load_balancing_weight
      
  def _set_load_balancing_weight(self, v, load=False):
    """
    Setter method for load_balancing_weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/weighted_ecmp/state/load_balancing_weight (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_balancing_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_balancing_weight() directly.

    YANG Description: The load-balancing weight of the interface, which applies when
weighted ECMP is enabled and the interface is part of a multipath set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_balancing_weight must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__load_balancing_weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_balancing_weight(self):
    self.__load_balancing_weight = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  load_balancing_weight = __builtin__.property(_get_load_balancing_weight)


  _pyangbind_elements = OrderedDict([('load_balancing_weight', load_balancing_weight), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/weighted-ecmp/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for weighted ecmp
  """
  __slots__ = ('_path_helper', '_extmethods', '__load_balancing_weight',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__load_balancing_weight = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'weighted-ecmp', 'state']

  def _get_load_balancing_weight(self):
    """
    Getter method for load_balancing_weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/weighted_ecmp/state/load_balancing_weight (union)

    YANG Description: The load-balancing weight of the interface, which applies when
weighted ECMP is enabled and the interface is part of a multipath set.
    """
    return self.__load_balancing_weight
      
  def _set_load_balancing_weight(self, v, load=False):
    """
    Setter method for load_balancing_weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/weighted_ecmp/state/load_balancing_weight (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_balancing_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_balancing_weight() directly.

    YANG Description: The load-balancing weight of the interface, which applies when
weighted ECMP is enabled and the interface is part of a multipath set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_balancing_weight must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__load_balancing_weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_balancing_weight(self):
    self.__load_balancing_weight = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1..4294967295']}),RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'auto': {}, 'none': {}},),], default=str("auto"), is_leaf=True, yang_name="load-balancing-weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  load_balancing_weight = __builtin__.property(_get_load_balancing_weight)


  _pyangbind_elements = OrderedDict([('load_balancing_weight', load_balancing_weight), ])


