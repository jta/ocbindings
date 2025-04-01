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
from . import forwarding_class
class forwarding_classes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/interfaces/interface/sid-counters/sid-counter/forwarding-classes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-SID per-forwarding class counters for Segment Routing.
  """
  __slots__ = ('_path_helper', '_extmethods', '__forwarding_class',)

  _yang_name = 'forwarding-classes'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__forwarding_class = YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'segment-routing', 'interfaces', 'interface', 'sid-counters', 'sid-counter', 'forwarding-classes']

  def _get_forwarding_class(self):
    """
    Getter method for forwarding_class, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes/forwarding_class (list)

    YANG Description: SID entries for the forwarding class associated with the
referenced MPLS EXP.
    """
    return self.__forwarding_class
      
  def _set_forwarding_class(self, v, load=False):
    """
    Setter method for forwarding_class, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes/forwarding_class (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_class() directly.

    YANG Description: SID entries for the forwarding class associated with the
referenced MPLS EXP.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_class must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__forwarding_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_class(self):
    self.__forwarding_class = YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  forwarding_class = __builtin__.property(_get_forwarding_class)


  _pyangbind_elements = OrderedDict([('forwarding_class', forwarding_class), ])


from . import forwarding_class
class forwarding_classes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/interfaces/interface/sid-counters/sid-counter/forwarding-classes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-SID per-forwarding class counters for Segment Routing.
  """
  __slots__ = ('_path_helper', '_extmethods', '__forwarding_class',)

  _yang_name = 'forwarding-classes'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__forwarding_class = YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'segment-routing', 'interfaces', 'interface', 'sid-counters', 'sid-counter', 'forwarding-classes']

  def _get_forwarding_class(self):
    """
    Getter method for forwarding_class, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes/forwarding_class (list)

    YANG Description: SID entries for the forwarding class associated with the
referenced MPLS EXP.
    """
    return self.__forwarding_class
      
  def _set_forwarding_class(self, v, load=False):
    """
    Setter method for forwarding_class, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes/forwarding_class (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_class() directly.

    YANG Description: SID entries for the forwarding class associated with the
referenced MPLS EXP.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_class must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__forwarding_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_class(self):
    self.__forwarding_class = YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  forwarding_class = __builtin__.property(_get_forwarding_class)


  _pyangbind_elements = OrderedDict([('forwarding_class', forwarding_class), ])


from . import forwarding_class
class forwarding_classes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/interfaces/interface/sid-counters/sid-counter/forwarding-classes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-SID per-forwarding class counters for Segment Routing.
  """
  __slots__ = ('_path_helper', '_extmethods', '__forwarding_class',)

  _yang_name = 'forwarding-classes'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__forwarding_class = YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'segment-routing', 'interfaces', 'interface', 'sid-counters', 'sid-counter', 'forwarding-classes']

  def _get_forwarding_class(self):
    """
    Getter method for forwarding_class, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes/forwarding_class (list)

    YANG Description: SID entries for the forwarding class associated with the
referenced MPLS EXP.
    """
    return self.__forwarding_class
      
  def _set_forwarding_class(self, v, load=False):
    """
    Setter method for forwarding_class, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes/forwarding_class (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_class() directly.

    YANG Description: SID entries for the forwarding class associated with the
referenced MPLS EXP.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_class must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__forwarding_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_class(self):
    self.__forwarding_class = YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  forwarding_class = __builtin__.property(_get_forwarding_class)


  _pyangbind_elements = OrderedDict([('forwarding_class', forwarding_class), ])


from . import forwarding_class
class forwarding_classes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/interfaces/interface/sid-counters/sid-counter/forwarding-classes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-SID per-forwarding class counters for Segment Routing.
  """
  __slots__ = ('_path_helper', '_extmethods', '__forwarding_class',)

  _yang_name = 'forwarding-classes'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__forwarding_class = YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'segment-routing', 'interfaces', 'interface', 'sid-counters', 'sid-counter', 'forwarding-classes']

  def _get_forwarding_class(self):
    """
    Getter method for forwarding_class, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes/forwarding_class (list)

    YANG Description: SID entries for the forwarding class associated with the
referenced MPLS EXP.
    """
    return self.__forwarding_class
      
  def _set_forwarding_class(self, v, load=False):
    """
    Setter method for forwarding_class, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/sid_counters/sid_counter/forwarding_classes/forwarding_class (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_class() directly.

    YANG Description: SID entries for the forwarding class associated with the
referenced MPLS EXP.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_class must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__forwarding_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_class(self):
    self.__forwarding_class = YANGDynClass(base=YANGListType("exp",forwarding_class.forwarding_class, yang_name="forwarding-class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='exp', extensions=None), is_container='list', yang_name="forwarding-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  forwarding_class = __builtin__.property(_get_forwarding_class)


  _pyangbind_elements = OrderedDict([('forwarding_class', forwarding_class), ])


