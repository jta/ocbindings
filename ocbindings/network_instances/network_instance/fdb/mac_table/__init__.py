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
from . import entries
class mac_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/fdb/mac-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Table of learned or statically configured MAC addresses and
corresponding VLANs in the bridge domain
  """
  __slots__ = ('_path_helper', '_extmethods', '__entries',)

  _yang_name = 'mac-table'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__entries = YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'fdb', 'mac-table']

  def _get_entries(self):
    """
    Getter method for entries, mapped from YANG variable /network_instances/network_instance/fdb/mac_table/entries (container)

    YANG Description: Enclosing container for list of MAC table entries
    """
    return self.__entries
      
  def _set_entries(self, v, load=False):
    """
    Setter method for entries, mapped from YANG variable /network_instances/network_instance/fdb/mac_table/entries (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entries() directly.

    YANG Description: Enclosing container for list of MAC table entries
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entries must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entries(self):
    self.__entries = YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  entries = __builtin__.property(_get_entries, _set_entries)


  _pyangbind_elements = OrderedDict([('entries', entries), ])


from . import entries
class mac_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/fdb/mac-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Table of learned or statically configured MAC addresses and
corresponding VLANs in the bridge domain
  """
  __slots__ = ('_path_helper', '_extmethods', '__entries',)

  _yang_name = 'mac-table'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__entries = YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'fdb', 'mac-table']

  def _get_entries(self):
    """
    Getter method for entries, mapped from YANG variable /network_instances/network_instance/fdb/mac_table/entries (container)

    YANG Description: Enclosing container for list of MAC table entries
    """
    return self.__entries
      
  def _set_entries(self, v, load=False):
    """
    Setter method for entries, mapped from YANG variable /network_instances/network_instance/fdb/mac_table/entries (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entries() directly.

    YANG Description: Enclosing container for list of MAC table entries
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entries must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entries(self):
    self.__entries = YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  entries = __builtin__.property(_get_entries, _set_entries)


  _pyangbind_elements = OrderedDict([('entries', entries), ])


from . import entries
class mac_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/fdb/mac-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Table of learned or statically configured MAC addresses and
corresponding VLANs in the bridge domain
  """
  __slots__ = ('_path_helper', '_extmethods', '__entries',)

  _yang_name = 'mac-table'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__entries = YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'fdb', 'mac-table']

  def _get_entries(self):
    """
    Getter method for entries, mapped from YANG variable /network_instances/network_instance/fdb/mac_table/entries (container)

    YANG Description: Enclosing container for list of MAC table entries
    """
    return self.__entries
      
  def _set_entries(self, v, load=False):
    """
    Setter method for entries, mapped from YANG variable /network_instances/network_instance/fdb/mac_table/entries (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entries() directly.

    YANG Description: Enclosing container for list of MAC table entries
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entries must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entries(self):
    self.__entries = YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  entries = __builtin__.property(_get_entries, _set_entries)


  _pyangbind_elements = OrderedDict([('entries', entries), ])


from . import entries
class mac_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/fdb/mac-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Table of learned or statically configured MAC addresses and
corresponding VLANs in the bridge domain
  """
  __slots__ = ('_path_helper', '_extmethods', '__entries',)

  _yang_name = 'mac-table'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__entries = YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'fdb', 'mac-table']

  def _get_entries(self):
    """
    Getter method for entries, mapped from YANG variable /network_instances/network_instance/fdb/mac_table/entries (container)

    YANG Description: Enclosing container for list of MAC table entries
    """
    return self.__entries
      
  def _set_entries(self, v, load=False):
    """
    Setter method for entries, mapped from YANG variable /network_instances/network_instance/fdb/mac_table/entries (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entries() directly.

    YANG Description: Enclosing container for list of MAC table entries
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entries must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entries(self):
    self.__entries = YANGDynClass(base=entries.entries, is_container='container', yang_name="entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  entries = __builtin__.property(_get_entries, _set_entries)


  _pyangbind_elements = OrderedDict([('entries', entries), ])


