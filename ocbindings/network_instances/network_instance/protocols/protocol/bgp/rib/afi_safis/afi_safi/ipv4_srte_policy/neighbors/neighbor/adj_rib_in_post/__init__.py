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
from . import routes
class adj_rib_in_post(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-srte-policy/neighbors/neighbor/adj-rib-in-post. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Adj-RIB-In for the SR-TE Policy SAFI for the neighbour,
following any inbound policy constraints or modifications
being made.
  """
  __slots__ = ('_path_helper', '_extmethods', '__routes',)

  _yang_name = 'adj-rib-in-post'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__routes = YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv4-srte-policy', 'neighbors', 'neighbor', 'adj-rib-in-post']

  def _get_routes(self):
    """
    Getter method for routes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/neighbors/neighbor/adj_rib_in_post/routes (container)

    YANG Description: The set of routes that are within the Adj-RIB-Out for the
neighbour.
    """
    return self.__routes
      
  def _set_routes(self, v, load=False):
    """
    Setter method for routes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/neighbors/neighbor/adj_rib_in_post/routes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routes() directly.

    YANG Description: The set of routes that are within the Adj-RIB-Out for the
neighbour.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__routes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routes(self):
    self.__routes = YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  routes = __builtin__.property(_get_routes)


  _pyangbind_elements = OrderedDict([('routes', routes), ])


from . import routes
class adj_rib_in_post(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-srte-policy/neighbors/neighbor/adj-rib-in-post. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Adj-RIB-In for the SR-TE Policy SAFI for the neighbour,
following any inbound policy constraints or modifications
being made.
  """
  __slots__ = ('_path_helper', '_extmethods', '__routes',)

  _yang_name = 'adj-rib-in-post'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__routes = YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv4-srte-policy', 'neighbors', 'neighbor', 'adj-rib-in-post']

  def _get_routes(self):
    """
    Getter method for routes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/neighbors/neighbor/adj_rib_in_post/routes (container)

    YANG Description: The set of routes that are within the Adj-RIB-Out for the
neighbour.
    """
    return self.__routes
      
  def _set_routes(self, v, load=False):
    """
    Setter method for routes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/neighbors/neighbor/adj_rib_in_post/routes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routes() directly.

    YANG Description: The set of routes that are within the Adj-RIB-Out for the
neighbour.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__routes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routes(self):
    self.__routes = YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  routes = __builtin__.property(_get_routes)


  _pyangbind_elements = OrderedDict([('routes', routes), ])


from . import routes
class adj_rib_in_post(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-srte-policy/neighbors/neighbor/adj-rib-in-post. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Adj-RIB-In for the SR-TE Policy SAFI for the neighbour,
following any inbound policy constraints or modifications
being made.
  """
  __slots__ = ('_path_helper', '_extmethods', '__routes',)

  _yang_name = 'adj-rib-in-post'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__routes = YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv4-srte-policy', 'neighbors', 'neighbor', 'adj-rib-in-post']

  def _get_routes(self):
    """
    Getter method for routes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/neighbors/neighbor/adj_rib_in_post/routes (container)

    YANG Description: The set of routes that are within the Adj-RIB-Out for the
neighbour.
    """
    return self.__routes
      
  def _set_routes(self, v, load=False):
    """
    Setter method for routes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/neighbors/neighbor/adj_rib_in_post/routes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routes() directly.

    YANG Description: The set of routes that are within the Adj-RIB-Out for the
neighbour.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__routes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routes(self):
    self.__routes = YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  routes = __builtin__.property(_get_routes)


  _pyangbind_elements = OrderedDict([('routes', routes), ])


from . import routes
class adj_rib_in_post(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-srte-policy/neighbors/neighbor/adj-rib-in-post. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Adj-RIB-In for the SR-TE Policy SAFI for the neighbour,
following any inbound policy constraints or modifications
being made.
  """
  __slots__ = ('_path_helper', '_extmethods', '__routes',)

  _yang_name = 'adj-rib-in-post'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__routes = YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv4-srte-policy', 'neighbors', 'neighbor', 'adj-rib-in-post']

  def _get_routes(self):
    """
    Getter method for routes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/neighbors/neighbor/adj_rib_in_post/routes (container)

    YANG Description: The set of routes that are within the Adj-RIB-Out for the
neighbour.
    """
    return self.__routes
      
  def _set_routes(self, v, load=False):
    """
    Setter method for routes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/neighbors/neighbor/adj_rib_in_post/routes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routes() directly.

    YANG Description: The set of routes that are within the Adj-RIB-Out for the
neighbour.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__routes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routes(self):
    self.__routes = YANGDynClass(base=routes.routes, is_container='container', yang_name="routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  routes = __builtin__.property(_get_routes)


  _pyangbind_elements = OrderedDict([('routes', routes), ])


