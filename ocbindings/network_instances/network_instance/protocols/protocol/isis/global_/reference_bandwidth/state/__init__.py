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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/reference-bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state for Reference Bandwidth.
  """
  __slots__ = ('_path_helper', '_extmethods', '__reference_bandwidth',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reference_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'reference-bandwidth', 'state']

  def _get_reference_bandwidth(self):
    """
    Getter method for reference_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/reference_bandwidth/state/reference_bandwidth (uint32)

    YANG Description: ISIS Reference Bandwidth value
    """
    return self.__reference_bandwidth
      
  def _set_reference_bandwidth(self, v, load=False):
    """
    Setter method for reference_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/reference_bandwidth/state/reference_bandwidth (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reference_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reference_bandwidth() directly.

    YANG Description: ISIS Reference Bandwidth value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reference_bandwidth must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__reference_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reference_bandwidth(self):
    self.__reference_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  reference_bandwidth = __builtin__.property(_get_reference_bandwidth)


  _pyangbind_elements = OrderedDict([('reference_bandwidth', reference_bandwidth), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/reference-bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state for Reference Bandwidth.
  """
  __slots__ = ('_path_helper', '_extmethods', '__reference_bandwidth',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reference_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'reference-bandwidth', 'state']

  def _get_reference_bandwidth(self):
    """
    Getter method for reference_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/reference_bandwidth/state/reference_bandwidth (uint32)

    YANG Description: ISIS Reference Bandwidth value
    """
    return self.__reference_bandwidth
      
  def _set_reference_bandwidth(self, v, load=False):
    """
    Setter method for reference_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/reference_bandwidth/state/reference_bandwidth (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reference_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reference_bandwidth() directly.

    YANG Description: ISIS Reference Bandwidth value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reference_bandwidth must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__reference_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reference_bandwidth(self):
    self.__reference_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  reference_bandwidth = __builtin__.property(_get_reference_bandwidth)


  _pyangbind_elements = OrderedDict([('reference_bandwidth', reference_bandwidth), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/reference-bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state for Reference Bandwidth.
  """
  __slots__ = ('_path_helper', '_extmethods', '__reference_bandwidth',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reference_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'reference-bandwidth', 'state']

  def _get_reference_bandwidth(self):
    """
    Getter method for reference_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/reference_bandwidth/state/reference_bandwidth (uint32)

    YANG Description: ISIS Reference Bandwidth value
    """
    return self.__reference_bandwidth
      
  def _set_reference_bandwidth(self, v, load=False):
    """
    Setter method for reference_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/reference_bandwidth/state/reference_bandwidth (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reference_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reference_bandwidth() directly.

    YANG Description: ISIS Reference Bandwidth value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reference_bandwidth must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__reference_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reference_bandwidth(self):
    self.__reference_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  reference_bandwidth = __builtin__.property(_get_reference_bandwidth)


  _pyangbind_elements = OrderedDict([('reference_bandwidth', reference_bandwidth), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/reference-bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state for Reference Bandwidth.
  """
  __slots__ = ('_path_helper', '_extmethods', '__reference_bandwidth',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reference_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'reference-bandwidth', 'state']

  def _get_reference_bandwidth(self):
    """
    Getter method for reference_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/reference_bandwidth/state/reference_bandwidth (uint32)

    YANG Description: ISIS Reference Bandwidth value
    """
    return self.__reference_bandwidth
      
  def _set_reference_bandwidth(self, v, load=False):
    """
    Setter method for reference_bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/reference_bandwidth/state/reference_bandwidth (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reference_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reference_bandwidth() directly.

    YANG Description: ISIS Reference Bandwidth value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reference_bandwidth must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__reference_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reference_bandwidth(self):
    self.__reference_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reference-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  reference_bandwidth = __builtin__.property(_get_reference_bandwidth)


  _pyangbind_elements = OrderedDict([('reference_bandwidth', reference_bandwidth), ])


