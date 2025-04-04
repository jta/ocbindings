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
from . import bandwidth_reservation
class bandwidth_reservations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/bandwidth-reservations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for bandwidth reservation
  """
  __slots__ = ('_path_helper', '_extmethods', '__bandwidth_reservation',)

  _yang_name = 'bandwidth-reservations'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth_reservation = YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'interface-attributes', 'interface', 'bandwidth-reservations']

  def _get_bandwidth_reservation(self):
    """
    Getter method for bandwidth_reservation, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/bandwidth_reservations/bandwidth_reservation (list)

    YANG Description: Available and reserved bandwidth by priority on
the interface.
    """
    return self.__bandwidth_reservation
      
  def _set_bandwidth_reservation(self, v, load=False):
    """
    Setter method for bandwidth_reservation, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/bandwidth_reservations/bandwidth_reservation (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_reservation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_reservation() directly.

    YANG Description: Available and reserved bandwidth by priority on
the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_reservation must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__bandwidth_reservation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_reservation(self):
    self.__bandwidth_reservation = YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  bandwidth_reservation = __builtin__.property(_get_bandwidth_reservation)


  _pyangbind_elements = OrderedDict([('bandwidth_reservation', bandwidth_reservation), ])


from . import bandwidth_reservation
class bandwidth_reservations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/bandwidth-reservations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for bandwidth reservation
  """
  __slots__ = ('_path_helper', '_extmethods', '__bandwidth_reservation',)

  _yang_name = 'bandwidth-reservations'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth_reservation = YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'interface-attributes', 'interface', 'bandwidth-reservations']

  def _get_bandwidth_reservation(self):
    """
    Getter method for bandwidth_reservation, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/bandwidth_reservations/bandwidth_reservation (list)

    YANG Description: Available and reserved bandwidth by priority on
the interface.
    """
    return self.__bandwidth_reservation
      
  def _set_bandwidth_reservation(self, v, load=False):
    """
    Setter method for bandwidth_reservation, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/bandwidth_reservations/bandwidth_reservation (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_reservation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_reservation() directly.

    YANG Description: Available and reserved bandwidth by priority on
the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_reservation must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__bandwidth_reservation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_reservation(self):
    self.__bandwidth_reservation = YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  bandwidth_reservation = __builtin__.property(_get_bandwidth_reservation)


  _pyangbind_elements = OrderedDict([('bandwidth_reservation', bandwidth_reservation), ])


from . import bandwidth_reservation
class bandwidth_reservations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/bandwidth-reservations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for bandwidth reservation
  """
  __slots__ = ('_path_helper', '_extmethods', '__bandwidth_reservation',)

  _yang_name = 'bandwidth-reservations'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth_reservation = YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'interface-attributes', 'interface', 'bandwidth-reservations']

  def _get_bandwidth_reservation(self):
    """
    Getter method for bandwidth_reservation, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/bandwidth_reservations/bandwidth_reservation (list)

    YANG Description: Available and reserved bandwidth by priority on
the interface.
    """
    return self.__bandwidth_reservation
      
  def _set_bandwidth_reservation(self, v, load=False):
    """
    Setter method for bandwidth_reservation, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/bandwidth_reservations/bandwidth_reservation (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_reservation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_reservation() directly.

    YANG Description: Available and reserved bandwidth by priority on
the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_reservation must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__bandwidth_reservation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_reservation(self):
    self.__bandwidth_reservation = YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  bandwidth_reservation = __builtin__.property(_get_bandwidth_reservation)


  _pyangbind_elements = OrderedDict([('bandwidth_reservation', bandwidth_reservation), ])


from . import bandwidth_reservation
class bandwidth_reservations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/bandwidth-reservations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for bandwidth reservation
  """
  __slots__ = ('_path_helper', '_extmethods', '__bandwidth_reservation',)

  _yang_name = 'bandwidth-reservations'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth_reservation = YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'interface-attributes', 'interface', 'bandwidth-reservations']

  def _get_bandwidth_reservation(self):
    """
    Getter method for bandwidth_reservation, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/bandwidth_reservations/bandwidth_reservation (list)

    YANG Description: Available and reserved bandwidth by priority on
the interface.
    """
    return self.__bandwidth_reservation
      
  def _set_bandwidth_reservation(self, v, load=False):
    """
    Setter method for bandwidth_reservation, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/bandwidth_reservations/bandwidth_reservation (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_reservation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_reservation() directly.

    YANG Description: Available and reserved bandwidth by priority on
the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_reservation must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__bandwidth_reservation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_reservation(self):
    self.__bandwidth_reservation = YANGDynClass(base=YANGListType("priority",bandwidth_reservation.bandwidth_reservation, yang_name="bandwidth-reservation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='priority', extensions=None), is_container='list', yang_name="bandwidth-reservation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  bandwidth_reservation = __builtin__.property(_get_bandwidth_reservation)


  _pyangbind_elements = OrderedDict([('bandwidth_reservation', bandwidth_reservation), ])


