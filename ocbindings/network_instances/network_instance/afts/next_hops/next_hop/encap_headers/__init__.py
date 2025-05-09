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
from . import encap_header
class encap_headers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/afts/next-hops/next-hop/encap-headers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for packet encapsulation headers.  When leaves in this
container are populated, it indicates encapsulation of the packet
matching the next-hop is performed using a stack of one or more
headers defined in the list encap-header.

Each entry in the list must indicate an encapsulation type and
populate a container with the parameters for that encapsulation
header.
  """
  __slots__ = ('_path_helper', '_extmethods', '__encap_header',)

  _yang_name = 'encap-headers'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__encap_header = YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'next-hops', 'next-hop', 'encap-headers']

  def _get_encap_header(self):
    """
    Getter method for encap_header, mapped from YANG variable /network_instances/network_instance/afts/next_hops/next_hop/encap_headers/encap_header (list)

    YANG Description: A list of headers added on top of a packet ordered by the
index value.  The inner-most header is the 0th value and is
adjacent to the original packet.  Additional headers may be
added in index order.

For example, in an encapsulation stack for MPLS in UDPv4, the
first index in the list is the MPLS header and the second
index is a UDPv4 header.
    """
    return self.__encap_header
      
  def _set_encap_header(self, v, load=False):
    """
    Setter method for encap_header, mapped from YANG variable /network_instances/network_instance/afts/next_hops/next_hop/encap_headers/encap_header (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encap_header is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encap_header() directly.

    YANG Description: A list of headers added on top of a packet ordered by the
index value.  The inner-most header is the 0th value and is
adjacent to the original packet.  Additional headers may be
added in index order.

For example, in an encapsulation stack for MPLS in UDPv4, the
first index in the list is the MPLS header and the second
index is a UDPv4 header.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encap_header must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__encap_header = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encap_header(self):
    self.__encap_header = YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  encap_header = __builtin__.property(_get_encap_header)


  _pyangbind_elements = OrderedDict([('encap_header', encap_header), ])


from . import encap_header
class encap_headers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/afts/next-hops/next-hop/encap-headers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for packet encapsulation headers.  When leaves in this
container are populated, it indicates encapsulation of the packet
matching the next-hop is performed using a stack of one or more
headers defined in the list encap-header.

Each entry in the list must indicate an encapsulation type and
populate a container with the parameters for that encapsulation
header.
  """
  __slots__ = ('_path_helper', '_extmethods', '__encap_header',)

  _yang_name = 'encap-headers'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__encap_header = YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'next-hops', 'next-hop', 'encap-headers']

  def _get_encap_header(self):
    """
    Getter method for encap_header, mapped from YANG variable /network_instances/network_instance/afts/next_hops/next_hop/encap_headers/encap_header (list)

    YANG Description: A list of headers added on top of a packet ordered by the
index value.  The inner-most header is the 0th value and is
adjacent to the original packet.  Additional headers may be
added in index order.

For example, in an encapsulation stack for MPLS in UDPv4, the
first index in the list is the MPLS header and the second
index is a UDPv4 header.
    """
    return self.__encap_header
      
  def _set_encap_header(self, v, load=False):
    """
    Setter method for encap_header, mapped from YANG variable /network_instances/network_instance/afts/next_hops/next_hop/encap_headers/encap_header (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encap_header is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encap_header() directly.

    YANG Description: A list of headers added on top of a packet ordered by the
index value.  The inner-most header is the 0th value and is
adjacent to the original packet.  Additional headers may be
added in index order.

For example, in an encapsulation stack for MPLS in UDPv4, the
first index in the list is the MPLS header and the second
index is a UDPv4 header.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encap_header must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__encap_header = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encap_header(self):
    self.__encap_header = YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  encap_header = __builtin__.property(_get_encap_header)


  _pyangbind_elements = OrderedDict([('encap_header', encap_header), ])


from . import encap_header
class encap_headers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/afts/next-hops/next-hop/encap-headers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for packet encapsulation headers.  When leaves in this
container are populated, it indicates encapsulation of the packet
matching the next-hop is performed using a stack of one or more
headers defined in the list encap-header.

Each entry in the list must indicate an encapsulation type and
populate a container with the parameters for that encapsulation
header.
  """
  __slots__ = ('_path_helper', '_extmethods', '__encap_header',)

  _yang_name = 'encap-headers'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__encap_header = YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'next-hops', 'next-hop', 'encap-headers']

  def _get_encap_header(self):
    """
    Getter method for encap_header, mapped from YANG variable /network_instances/network_instance/afts/next_hops/next_hop/encap_headers/encap_header (list)

    YANG Description: A list of headers added on top of a packet ordered by the
index value.  The inner-most header is the 0th value and is
adjacent to the original packet.  Additional headers may be
added in index order.

For example, in an encapsulation stack for MPLS in UDPv4, the
first index in the list is the MPLS header and the second
index is a UDPv4 header.
    """
    return self.__encap_header
      
  def _set_encap_header(self, v, load=False):
    """
    Setter method for encap_header, mapped from YANG variable /network_instances/network_instance/afts/next_hops/next_hop/encap_headers/encap_header (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encap_header is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encap_header() directly.

    YANG Description: A list of headers added on top of a packet ordered by the
index value.  The inner-most header is the 0th value and is
adjacent to the original packet.  Additional headers may be
added in index order.

For example, in an encapsulation stack for MPLS in UDPv4, the
first index in the list is the MPLS header and the second
index is a UDPv4 header.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encap_header must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__encap_header = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encap_header(self):
    self.__encap_header = YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  encap_header = __builtin__.property(_get_encap_header)


  _pyangbind_elements = OrderedDict([('encap_header', encap_header), ])


from . import encap_header
class encap_headers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/afts/next-hops/next-hop/encap-headers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for packet encapsulation headers.  When leaves in this
container are populated, it indicates encapsulation of the packet
matching the next-hop is performed using a stack of one or more
headers defined in the list encap-header.

Each entry in the list must indicate an encapsulation type and
populate a container with the parameters for that encapsulation
header.
  """
  __slots__ = ('_path_helper', '_extmethods', '__encap_header',)

  _yang_name = 'encap-headers'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__encap_header = YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'next-hops', 'next-hop', 'encap-headers']

  def _get_encap_header(self):
    """
    Getter method for encap_header, mapped from YANG variable /network_instances/network_instance/afts/next_hops/next_hop/encap_headers/encap_header (list)

    YANG Description: A list of headers added on top of a packet ordered by the
index value.  The inner-most header is the 0th value and is
adjacent to the original packet.  Additional headers may be
added in index order.

For example, in an encapsulation stack for MPLS in UDPv4, the
first index in the list is the MPLS header and the second
index is a UDPv4 header.
    """
    return self.__encap_header
      
  def _set_encap_header(self, v, load=False):
    """
    Setter method for encap_header, mapped from YANG variable /network_instances/network_instance/afts/next_hops/next_hop/encap_headers/encap_header (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encap_header is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encap_header() directly.

    YANG Description: A list of headers added on top of a packet ordered by the
index value.  The inner-most header is the 0th value and is
adjacent to the original packet.  Additional headers may be
added in index order.

For example, in an encapsulation stack for MPLS in UDPv4, the
first index in the list is the MPLS header and the second
index is a UDPv4 header.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encap_header must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__encap_header = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encap_header(self):
    self.__encap_header = YANGDynClass(base=YANGListType("index",encap_header.encap_header, yang_name="encap-header", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="encap-header", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  encap_header = __builtin__.property(_get_encap_header)


  _pyangbind_elements = OrderedDict([('encap_header', encap_header), ])


