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
from . import connection_point
class connection_points(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of connection points within a forwarding
instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__connection_point',)

  _yang_name = 'connection-points'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__connection_point = YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points']

  def _get_connection_point(self):
    """
    Getter method for connection_point, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point (list)

    YANG Description: A connection point within a Layer 2 network instance.
Each connection-point consists of a set of interfaces
only one of which is active at any one time. Other than
the specification of whether an interface is local
(i.e., exists within this network-instance), or remote,
all configuration and state parameters are common
    """
    return self.__connection_point
      
  def _set_connection_point(self, v, load=False):
    """
    Setter method for connection_point, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_point is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_point() directly.

    YANG Description: A connection point within a Layer 2 network instance.
Each connection-point consists of a set of interfaces
only one of which is active at any one time. Other than
the specification of whether an interface is local
(i.e., exists within this network-instance), or remote,
all configuration and state parameters are common
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_point must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__connection_point = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_point(self):
    self.__connection_point = YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  connection_point = __builtin__.property(_get_connection_point, _set_connection_point)


  _pyangbind_elements = OrderedDict([('connection_point', connection_point), ])


from . import connection_point
class connection_points(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of connection points within a forwarding
instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__connection_point',)

  _yang_name = 'connection-points'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__connection_point = YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points']

  def _get_connection_point(self):
    """
    Getter method for connection_point, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point (list)

    YANG Description: A connection point within a Layer 2 network instance.
Each connection-point consists of a set of interfaces
only one of which is active at any one time. Other than
the specification of whether an interface is local
(i.e., exists within this network-instance), or remote,
all configuration and state parameters are common
    """
    return self.__connection_point
      
  def _set_connection_point(self, v, load=False):
    """
    Setter method for connection_point, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_point is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_point() directly.

    YANG Description: A connection point within a Layer 2 network instance.
Each connection-point consists of a set of interfaces
only one of which is active at any one time. Other than
the specification of whether an interface is local
(i.e., exists within this network-instance), or remote,
all configuration and state parameters are common
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_point must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__connection_point = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_point(self):
    self.__connection_point = YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  connection_point = __builtin__.property(_get_connection_point, _set_connection_point)


  _pyangbind_elements = OrderedDict([('connection_point', connection_point), ])


from . import connection_point
class connection_points(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of connection points within a forwarding
instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__connection_point',)

  _yang_name = 'connection-points'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__connection_point = YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points']

  def _get_connection_point(self):
    """
    Getter method for connection_point, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point (list)

    YANG Description: A connection point within a Layer 2 network instance.
Each connection-point consists of a set of interfaces
only one of which is active at any one time. Other than
the specification of whether an interface is local
(i.e., exists within this network-instance), or remote,
all configuration and state parameters are common
    """
    return self.__connection_point
      
  def _set_connection_point(self, v, load=False):
    """
    Setter method for connection_point, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_point is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_point() directly.

    YANG Description: A connection point within a Layer 2 network instance.
Each connection-point consists of a set of interfaces
only one of which is active at any one time. Other than
the specification of whether an interface is local
(i.e., exists within this network-instance), or remote,
all configuration and state parameters are common
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_point must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__connection_point = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_point(self):
    self.__connection_point = YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  connection_point = __builtin__.property(_get_connection_point, _set_connection_point)


  _pyangbind_elements = OrderedDict([('connection_point', connection_point), ])


from . import connection_point
class connection_points(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of connection points within a forwarding
instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__connection_point',)

  _yang_name = 'connection-points'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__connection_point = YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points']

  def _get_connection_point(self):
    """
    Getter method for connection_point, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point (list)

    YANG Description: A connection point within a Layer 2 network instance.
Each connection-point consists of a set of interfaces
only one of which is active at any one time. Other than
the specification of whether an interface is local
(i.e., exists within this network-instance), or remote,
all configuration and state parameters are common
    """
    return self.__connection_point
      
  def _set_connection_point(self, v, load=False):
    """
    Setter method for connection_point, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_point is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_point() directly.

    YANG Description: A connection point within a Layer 2 network instance.
Each connection-point consists of a set of interfaces
only one of which is active at any one time. Other than
the specification of whether an interface is local
(i.e., exists within this network-instance), or remote,
all configuration and state parameters are common
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_point must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__connection_point = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_point(self):
    self.__connection_point = YANGDynClass(base=YANGListType("connection_point_id",connection_point.connection_point, yang_name="connection-point", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='connection-point-id', extensions=None), is_container='list', yang_name="connection-point", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  connection_point = __builtin__.property(_get_connection_point, _set_connection_point)


  _pyangbind_elements = OrderedDict([('connection_point', connection_point), ])


