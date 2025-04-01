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
from . import loc_rib
from . import neighbors
class ipv6_srte_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-srte-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Routing tables for the IPv6 Unicast, SR-TE Policy SAFI.
  """
  __slots__ = ('_path_helper', '_extmethods', '__loc_rib','__neighbors',)

  _yang_name = 'ipv6-srte-policy'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__loc_rib = YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv6-srte-policy']

  def _get_loc_rib(self):
    """
    Getter method for loc_rib, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/loc_rib (container)

    YANG Description: The Loc-RIB for the SR-TE Policy SAFI for IPv4 or IPv6 Unicast
AFIs.
    """
    return self.__loc_rib
      
  def _set_loc_rib(self, v, load=False):
    """
    Setter method for loc_rib, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/loc_rib (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loc_rib is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loc_rib() directly.

    YANG Description: The Loc-RIB for the SR-TE Policy SAFI for IPv4 or IPv6 Unicast
AFIs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loc_rib must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__loc_rib = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loc_rib(self):
    self.__loc_rib = YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_neighbors(self):
    """
    Getter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/neighbors (container)

    YANG Description: Surrounding container for the list of neighbours that are
enabled for the IPv4 and IPv6 AFI, SR-TE Policy SAFI address
family.
    """
    return self.__neighbors
      
  def _set_neighbors(self, v, load=False):
    """
    Setter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: Surrounding container for the list of neighbours that are
enabled for the IPv4 and IPv6 AFI, SR-TE Policy SAFI address
family.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbors(self):
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  loc_rib = __builtin__.property(_get_loc_rib)
  neighbors = __builtin__.property(_get_neighbors)


  _pyangbind_elements = OrderedDict([('loc_rib', loc_rib), ('neighbors', neighbors), ])


from . import loc_rib
from . import neighbors
class ipv6_srte_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-srte-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Routing tables for the IPv6 Unicast, SR-TE Policy SAFI.
  """
  __slots__ = ('_path_helper', '_extmethods', '__loc_rib','__neighbors',)

  _yang_name = 'ipv6-srte-policy'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__loc_rib = YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv6-srte-policy']

  def _get_loc_rib(self):
    """
    Getter method for loc_rib, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/loc_rib (container)

    YANG Description: The Loc-RIB for the SR-TE Policy SAFI for IPv4 or IPv6 Unicast
AFIs.
    """
    return self.__loc_rib
      
  def _set_loc_rib(self, v, load=False):
    """
    Setter method for loc_rib, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/loc_rib (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loc_rib is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loc_rib() directly.

    YANG Description: The Loc-RIB for the SR-TE Policy SAFI for IPv4 or IPv6 Unicast
AFIs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loc_rib must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__loc_rib = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loc_rib(self):
    self.__loc_rib = YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_neighbors(self):
    """
    Getter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/neighbors (container)

    YANG Description: Surrounding container for the list of neighbours that are
enabled for the IPv4 and IPv6 AFI, SR-TE Policy SAFI address
family.
    """
    return self.__neighbors
      
  def _set_neighbors(self, v, load=False):
    """
    Setter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: Surrounding container for the list of neighbours that are
enabled for the IPv4 and IPv6 AFI, SR-TE Policy SAFI address
family.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbors(self):
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  loc_rib = __builtin__.property(_get_loc_rib)
  neighbors = __builtin__.property(_get_neighbors)


  _pyangbind_elements = OrderedDict([('loc_rib', loc_rib), ('neighbors', neighbors), ])


from . import loc_rib
from . import neighbors
class ipv6_srte_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-srte-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Routing tables for the IPv6 Unicast, SR-TE Policy SAFI.
  """
  __slots__ = ('_path_helper', '_extmethods', '__loc_rib','__neighbors',)

  _yang_name = 'ipv6-srte-policy'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__loc_rib = YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv6-srte-policy']

  def _get_loc_rib(self):
    """
    Getter method for loc_rib, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/loc_rib (container)

    YANG Description: The Loc-RIB for the SR-TE Policy SAFI for IPv4 or IPv6 Unicast
AFIs.
    """
    return self.__loc_rib
      
  def _set_loc_rib(self, v, load=False):
    """
    Setter method for loc_rib, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/loc_rib (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loc_rib is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loc_rib() directly.

    YANG Description: The Loc-RIB for the SR-TE Policy SAFI for IPv4 or IPv6 Unicast
AFIs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loc_rib must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__loc_rib = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loc_rib(self):
    self.__loc_rib = YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_neighbors(self):
    """
    Getter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/neighbors (container)

    YANG Description: Surrounding container for the list of neighbours that are
enabled for the IPv4 and IPv6 AFI, SR-TE Policy SAFI address
family.
    """
    return self.__neighbors
      
  def _set_neighbors(self, v, load=False):
    """
    Setter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: Surrounding container for the list of neighbours that are
enabled for the IPv4 and IPv6 AFI, SR-TE Policy SAFI address
family.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbors(self):
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  loc_rib = __builtin__.property(_get_loc_rib)
  neighbors = __builtin__.property(_get_neighbors)


  _pyangbind_elements = OrderedDict([('loc_rib', loc_rib), ('neighbors', neighbors), ])


from . import loc_rib
from . import neighbors
class ipv6_srte_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv6-srte-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Routing tables for the IPv6 Unicast, SR-TE Policy SAFI.
  """
  __slots__ = ('_path_helper', '_extmethods', '__loc_rib','__neighbors',)

  _yang_name = 'ipv6-srte-policy'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__loc_rib = YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv6-srte-policy']

  def _get_loc_rib(self):
    """
    Getter method for loc_rib, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/loc_rib (container)

    YANG Description: The Loc-RIB for the SR-TE Policy SAFI for IPv4 or IPv6 Unicast
AFIs.
    """
    return self.__loc_rib
      
  def _set_loc_rib(self, v, load=False):
    """
    Setter method for loc_rib, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/loc_rib (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loc_rib is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loc_rib() directly.

    YANG Description: The Loc-RIB for the SR-TE Policy SAFI for IPv4 or IPv6 Unicast
AFIs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loc_rib must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__loc_rib = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loc_rib(self):
    self.__loc_rib = YANGDynClass(base=loc_rib.loc_rib, is_container='container', yang_name="loc-rib", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_neighbors(self):
    """
    Getter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/neighbors (container)

    YANG Description: Surrounding container for the list of neighbours that are
enabled for the IPv4 and IPv6 AFI, SR-TE Policy SAFI address
family.
    """
    return self.__neighbors
      
  def _set_neighbors(self, v, load=False):
    """
    Setter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv6_srte_policy/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: Surrounding container for the list of neighbours that are
enabled for the IPv4 and IPv6 AFI, SR-TE Policy SAFI address
family.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbors(self):
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  loc_rib = __builtin__.property(_get_loc_rib)
  neighbors = __builtin__.property(_get_neighbors)


  _pyangbind_elements = OrderedDict([('loc_rib', loc_rib), ('neighbors', neighbors), ])


