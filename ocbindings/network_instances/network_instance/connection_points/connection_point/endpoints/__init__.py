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
from . import endpoint
class endpoints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of endpoints which are grouped within the
connection point
  """
  __slots__ = ('_path_helper', '_extmethods', '__endpoint',)

  _yang_name = 'endpoints'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__endpoint = YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints']

  def _get_endpoint(self):
    """
    Getter method for endpoint, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint (list)

    YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with.
    """
    return self.__endpoint
      
  def _set_endpoint(self, v, load=False):
    """
    Setter method for endpoint, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint() directly.

    YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__endpoint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint(self):
    self.__endpoint = YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  endpoint = __builtin__.property(_get_endpoint, _set_endpoint)


  _pyangbind_elements = OrderedDict([('endpoint', endpoint), ])


from . import endpoint
class endpoints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of endpoints which are grouped within the
connection point
  """
  __slots__ = ('_path_helper', '_extmethods', '__endpoint',)

  _yang_name = 'endpoints'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__endpoint = YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints']

  def _get_endpoint(self):
    """
    Getter method for endpoint, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint (list)

    YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with.
    """
    return self.__endpoint
      
  def _set_endpoint(self, v, load=False):
    """
    Setter method for endpoint, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint() directly.

    YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__endpoint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint(self):
    self.__endpoint = YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  endpoint = __builtin__.property(_get_endpoint, _set_endpoint)


  _pyangbind_elements = OrderedDict([('endpoint', endpoint), ])


from . import endpoint
class endpoints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of endpoints which are grouped within the
connection point
  """
  __slots__ = ('_path_helper', '_extmethods', '__endpoint',)

  _yang_name = 'endpoints'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__endpoint = YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints']

  def _get_endpoint(self):
    """
    Getter method for endpoint, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint (list)

    YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with.
    """
    return self.__endpoint
      
  def _set_endpoint(self, v, load=False):
    """
    Setter method for endpoint, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint() directly.

    YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__endpoint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint(self):
    self.__endpoint = YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  endpoint = __builtin__.property(_get_endpoint, _set_endpoint)


  _pyangbind_elements = OrderedDict([('endpoint', endpoint), ])


from . import endpoint
class endpoints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of endpoints which are grouped within the
connection point
  """
  __slots__ = ('_path_helper', '_extmethods', '__endpoint',)

  _yang_name = 'endpoints'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__endpoint = YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'connection-points', 'connection-point', 'endpoints']

  def _get_endpoint(self):
    """
    Getter method for endpoint, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint (list)

    YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with.
    """
    return self.__endpoint
      
  def _set_endpoint(self, v, load=False):
    """
    Setter method for endpoint, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint() directly.

    YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__endpoint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint(self):
    self.__endpoint = YANGDynClass(base=YANGListType("endpoint_id",endpoint.endpoint, yang_name="endpoint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='endpoint-id', extensions=None), is_container='list', yang_name="endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  endpoint = __builtin__.property(_get_endpoint, _set_endpoint)


  _pyangbind_elements = OrderedDict([('endpoint', endpoint), ])


