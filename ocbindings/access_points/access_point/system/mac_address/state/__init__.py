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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/mac-address/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for routing MAC address.
  """
  __slots__ = ('_path_helper', '_extmethods', '__routing_mac',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__routing_mac = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="routing-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'mac-address', 'state']

  def _get_routing_mac(self):
    """
    Getter method for routing_mac, mapped from YANG variable /access_points/access_point/system/mac_address/state/routing_mac (oc-yang:mac-address)

    YANG Description: Any packets destined to this MAC address must be sent through the
routing pipeline by the system. This MAC address is used to identify
routed packets in addition to any other MAC addresses that the system
may already have been using to perform routing.

It is not expected that this MAC address will be used as the
source MAC address of any routed packet, as the source MAC address of
any packets generated by the system, or a MAC address used in ARP
response. This MAC address may not be allocated from the block of
MAC address that system owns. For instance, it's allocation could
be managed by an external controller.
    """
    return self.__routing_mac
      
  def _set_routing_mac(self, v, load=False):
    """
    Setter method for routing_mac, mapped from YANG variable /access_points/access_point/system/mac_address/state/routing_mac (oc-yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routing_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routing_mac() directly.

    YANG Description: Any packets destined to this MAC address must be sent through the
routing pipeline by the system. This MAC address is used to identify
routed packets in addition to any other MAC addresses that the system
may already have been using to perform routing.

It is not expected that this MAC address will be used as the
source MAC address of any routed packet, as the source MAC address of
any packets generated by the system, or a MAC address used in ARP
response. This MAC address may not be allocated from the block of
MAC address that system owns. For instance, it's allocation could
be managed by an external controller.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="routing-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routing_mac must be of a type compatible with oc-yang:mac-address""",
          'defined-type': "oc-yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="routing-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)""",
        })

    self.__routing_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routing_mac(self):
    self.__routing_mac = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="routing-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)

  routing_mac = __builtin__.property(_get_routing_mac)


  _pyangbind_elements = OrderedDict([('routing_mac', routing_mac), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/mac-address/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for routing MAC address.
  """
  __slots__ = ('_path_helper', '_extmethods', '__routing_mac',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__routing_mac = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="routing-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'mac-address', 'state']

  def _get_routing_mac(self):
    """
    Getter method for routing_mac, mapped from YANG variable /access_points/access_point/system/mac_address/state/routing_mac (oc-yang:mac-address)

    YANG Description: Any packets destined to this MAC address must be sent through the
routing pipeline by the system. This MAC address is used to identify
routed packets in addition to any other MAC addresses that the system
may already have been using to perform routing.

It is not expected that this MAC address will be used as the
source MAC address of any routed packet, as the source MAC address of
any packets generated by the system, or a MAC address used in ARP
response. This MAC address may not be allocated from the block of
MAC address that system owns. For instance, it's allocation could
be managed by an external controller.
    """
    return self.__routing_mac
      
  def _set_routing_mac(self, v, load=False):
    """
    Setter method for routing_mac, mapped from YANG variable /access_points/access_point/system/mac_address/state/routing_mac (oc-yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routing_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routing_mac() directly.

    YANG Description: Any packets destined to this MAC address must be sent through the
routing pipeline by the system. This MAC address is used to identify
routed packets in addition to any other MAC addresses that the system
may already have been using to perform routing.

It is not expected that this MAC address will be used as the
source MAC address of any routed packet, as the source MAC address of
any packets generated by the system, or a MAC address used in ARP
response. This MAC address may not be allocated from the block of
MAC address that system owns. For instance, it's allocation could
be managed by an external controller.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="routing-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routing_mac must be of a type compatible with oc-yang:mac-address""",
          'defined-type': "oc-yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="routing-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)""",
        })

    self.__routing_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routing_mac(self):
    self.__routing_mac = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="routing-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)

  routing_mac = __builtin__.property(_get_routing_mac)


  _pyangbind_elements = OrderedDict([('routing_mac', routing_mac), ])


