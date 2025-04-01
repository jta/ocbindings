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
from . import record_route_object
class record_route_objects(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/sessions/session/record-route-objects. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for MPLS RRO objects associated with the
traffic engineered tunnel.
  """
  __slots__ = ('_path_helper', '_extmethods', '__record_route_object',)

  _yang_name = 'record-route-objects'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__record_route_object = YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'sessions', 'session', 'record-route-objects']

  def _get_record_route_object(self):
    """
    Getter method for record_route_object, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object (list)

    YANG Description: Read-only list of record route objects associated with the
traffic engineered tunnel. Each entry in the list
may contain a hop IP address, MPLS label allocated
at the hop, and the flags associated with the entry.
    """
    return self.__record_route_object
      
  def _set_record_route_object(self, v, load=False):
    """
    Setter method for record_route_object, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_record_route_object is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_record_route_object() directly.

    YANG Description: Read-only list of record route objects associated with the
traffic engineered tunnel. Each entry in the list
may contain a hop IP address, MPLS label allocated
at the hop, and the flags associated with the entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """record_route_object must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__record_route_object = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_record_route_object(self):
    self.__record_route_object = YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  record_route_object = __builtin__.property(_get_record_route_object)


  _pyangbind_elements = OrderedDict([('record_route_object', record_route_object), ])


from . import record_route_object
class record_route_objects(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/sessions/session/record-route-objects. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for MPLS RRO objects associated with the
traffic engineered tunnel.
  """
  __slots__ = ('_path_helper', '_extmethods', '__record_route_object',)

  _yang_name = 'record-route-objects'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__record_route_object = YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'sessions', 'session', 'record-route-objects']

  def _get_record_route_object(self):
    """
    Getter method for record_route_object, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object (list)

    YANG Description: Read-only list of record route objects associated with the
traffic engineered tunnel. Each entry in the list
may contain a hop IP address, MPLS label allocated
at the hop, and the flags associated with the entry.
    """
    return self.__record_route_object
      
  def _set_record_route_object(self, v, load=False):
    """
    Setter method for record_route_object, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_record_route_object is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_record_route_object() directly.

    YANG Description: Read-only list of record route objects associated with the
traffic engineered tunnel. Each entry in the list
may contain a hop IP address, MPLS label allocated
at the hop, and the flags associated with the entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """record_route_object must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__record_route_object = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_record_route_object(self):
    self.__record_route_object = YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  record_route_object = __builtin__.property(_get_record_route_object)


  _pyangbind_elements = OrderedDict([('record_route_object', record_route_object), ])


from . import record_route_object
class record_route_objects(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/sessions/session/record-route-objects. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for MPLS RRO objects associated with the
traffic engineered tunnel.
  """
  __slots__ = ('_path_helper', '_extmethods', '__record_route_object',)

  _yang_name = 'record-route-objects'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__record_route_object = YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'sessions', 'session', 'record-route-objects']

  def _get_record_route_object(self):
    """
    Getter method for record_route_object, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object (list)

    YANG Description: Read-only list of record route objects associated with the
traffic engineered tunnel. Each entry in the list
may contain a hop IP address, MPLS label allocated
at the hop, and the flags associated with the entry.
    """
    return self.__record_route_object
      
  def _set_record_route_object(self, v, load=False):
    """
    Setter method for record_route_object, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_record_route_object is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_record_route_object() directly.

    YANG Description: Read-only list of record route objects associated with the
traffic engineered tunnel. Each entry in the list
may contain a hop IP address, MPLS label allocated
at the hop, and the flags associated with the entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """record_route_object must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__record_route_object = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_record_route_object(self):
    self.__record_route_object = YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  record_route_object = __builtin__.property(_get_record_route_object)


  _pyangbind_elements = OrderedDict([('record_route_object', record_route_object), ])


from . import record_route_object
class record_route_objects(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/sessions/session/record-route-objects. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for MPLS RRO objects associated with the
traffic engineered tunnel.
  """
  __slots__ = ('_path_helper', '_extmethods', '__record_route_object',)

  _yang_name = 'record-route-objects'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__record_route_object = YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'sessions', 'session', 'record-route-objects']

  def _get_record_route_object(self):
    """
    Getter method for record_route_object, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object (list)

    YANG Description: Read-only list of record route objects associated with the
traffic engineered tunnel. Each entry in the list
may contain a hop IP address, MPLS label allocated
at the hop, and the flags associated with the entry.
    """
    return self.__record_route_object
      
  def _set_record_route_object(self, v, load=False):
    """
    Setter method for record_route_object, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects/record_route_object (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_record_route_object is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_record_route_object() directly.

    YANG Description: Read-only list of record route objects associated with the
traffic engineered tunnel. Each entry in the list
may contain a hop IP address, MPLS label allocated
at the hop, and the flags associated with the entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """record_route_object must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__record_route_object = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_record_route_object(self):
    self.__record_route_object = YANGDynClass(base=YANGListType("index",record_route_object.record_route_object, yang_name="record-route-object", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="record-route-object", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  record_route_object = __builtin__.property(_get_record_route_object)


  _pyangbind_elements = OrderedDict([('record_route_object', record_route_object), ])


