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
from . import ipv4_entry
class ipv4_unicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/afts/ipv4-unicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The abstract forwarding table for IPv4 unicast. Entries
within this table are uniquely keyed on the IPv4 unicast
destination prefix which is matched by ingress packets.

The data set represented by the IPv4 Unicast AFT is the set
of entries from the IPv4 unicast RIB that have been selected
for installation into the FIB of the device exporting the
data structure.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ipv4_entry',)

  _yang_name = 'ipv4-unicast'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ipv4_entry = YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'ipv4-unicast']

  def _get_ipv4_entry(self):
    """
    Getter method for ipv4_entry, mapped from YANG variable /network_instances/network_instance/afts/ipv4_unicast/ipv4_entry (list)

    YANG Description: List of the IPv4 unicast entries within the abstract
forwarding table. This list is keyed by the destination IPv4
prefix.
    """
    return self.__ipv4_entry
      
  def _set_ipv4_entry(self, v, load=False):
    """
    Setter method for ipv4_entry, mapped from YANG variable /network_instances/network_instance/afts/ipv4_unicast/ipv4_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_entry() directly.

    YANG Description: List of the IPv4 unicast entries within the abstract
forwarding table. This list is keyed by the destination IPv4
prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__ipv4_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_entry(self):
    self.__ipv4_entry = YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  ipv4_entry = __builtin__.property(_get_ipv4_entry)


  _pyangbind_elements = OrderedDict([('ipv4_entry', ipv4_entry), ])


from . import ipv4_entry
class ipv4_unicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/afts/ipv4-unicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The abstract forwarding table for IPv4 unicast. Entries
within this table are uniquely keyed on the IPv4 unicast
destination prefix which is matched by ingress packets.

The data set represented by the IPv4 Unicast AFT is the set
of entries from the IPv4 unicast RIB that have been selected
for installation into the FIB of the device exporting the
data structure.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ipv4_entry',)

  _yang_name = 'ipv4-unicast'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ipv4_entry = YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'ipv4-unicast']

  def _get_ipv4_entry(self):
    """
    Getter method for ipv4_entry, mapped from YANG variable /network_instances/network_instance/afts/ipv4_unicast/ipv4_entry (list)

    YANG Description: List of the IPv4 unicast entries within the abstract
forwarding table. This list is keyed by the destination IPv4
prefix.
    """
    return self.__ipv4_entry
      
  def _set_ipv4_entry(self, v, load=False):
    """
    Setter method for ipv4_entry, mapped from YANG variable /network_instances/network_instance/afts/ipv4_unicast/ipv4_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_entry() directly.

    YANG Description: List of the IPv4 unicast entries within the abstract
forwarding table. This list is keyed by the destination IPv4
prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__ipv4_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_entry(self):
    self.__ipv4_entry = YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  ipv4_entry = __builtin__.property(_get_ipv4_entry)


  _pyangbind_elements = OrderedDict([('ipv4_entry', ipv4_entry), ])


from . import ipv4_entry
class ipv4_unicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/afts/ipv4-unicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The abstract forwarding table for IPv4 unicast. Entries
within this table are uniquely keyed on the IPv4 unicast
destination prefix which is matched by ingress packets.

The data set represented by the IPv4 Unicast AFT is the set
of entries from the IPv4 unicast RIB that have been selected
for installation into the FIB of the device exporting the
data structure.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ipv4_entry',)

  _yang_name = 'ipv4-unicast'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ipv4_entry = YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'ipv4-unicast']

  def _get_ipv4_entry(self):
    """
    Getter method for ipv4_entry, mapped from YANG variable /network_instances/network_instance/afts/ipv4_unicast/ipv4_entry (list)

    YANG Description: List of the IPv4 unicast entries within the abstract
forwarding table. This list is keyed by the destination IPv4
prefix.
    """
    return self.__ipv4_entry
      
  def _set_ipv4_entry(self, v, load=False):
    """
    Setter method for ipv4_entry, mapped from YANG variable /network_instances/network_instance/afts/ipv4_unicast/ipv4_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_entry() directly.

    YANG Description: List of the IPv4 unicast entries within the abstract
forwarding table. This list is keyed by the destination IPv4
prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__ipv4_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_entry(self):
    self.__ipv4_entry = YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  ipv4_entry = __builtin__.property(_get_ipv4_entry)


  _pyangbind_elements = OrderedDict([('ipv4_entry', ipv4_entry), ])


from . import ipv4_entry
class ipv4_unicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/afts/ipv4-unicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The abstract forwarding table for IPv4 unicast. Entries
within this table are uniquely keyed on the IPv4 unicast
destination prefix which is matched by ingress packets.

The data set represented by the IPv4 Unicast AFT is the set
of entries from the IPv4 unicast RIB that have been selected
for installation into the FIB of the device exporting the
data structure.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ipv4_entry',)

  _yang_name = 'ipv4-unicast'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ipv4_entry = YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'ipv4-unicast']

  def _get_ipv4_entry(self):
    """
    Getter method for ipv4_entry, mapped from YANG variable /network_instances/network_instance/afts/ipv4_unicast/ipv4_entry (list)

    YANG Description: List of the IPv4 unicast entries within the abstract
forwarding table. This list is keyed by the destination IPv4
prefix.
    """
    return self.__ipv4_entry
      
  def _set_ipv4_entry(self, v, load=False):
    """
    Setter method for ipv4_entry, mapped from YANG variable /network_instances/network_instance/afts/ipv4_unicast/ipv4_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_entry() directly.

    YANG Description: List of the IPv4 unicast entries within the abstract
forwarding table. This list is keyed by the destination IPv4
prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__ipv4_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_entry(self):
    self.__ipv4_entry = YANGDynClass(base=YANGListType("prefix",ipv4_entry.ipv4_entry, yang_name="ipv4-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prefix', extensions=None), is_container='list', yang_name="ipv4-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  ipv4_entry = __builtin__.property(_get_ipv4_entry)


  _pyangbind_elements = OrderedDict([('ipv4_entry', ipv4_entry), ])


