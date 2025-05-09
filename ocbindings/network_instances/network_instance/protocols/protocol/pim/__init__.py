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
from . import global_
from . import interfaces
class pim(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/pim. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level PIM configuration and operational state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__interfaces',)

  _yang_name = 'pim'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'pim']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/global (container)

    YANG Description: This container defines global PIM configuration and state
information.
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: This container defines global PIM configuration and state
information.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/interfaces (container)

    YANG Description: Configuration and state data for PIM on each interface.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Configuration and state data for PIM on each interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('global_', global_), ('interfaces', interfaces), ])


from . import global_
from . import interfaces
class pim(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/pim. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level PIM configuration and operational state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__interfaces',)

  _yang_name = 'pim'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'pim']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/global (container)

    YANG Description: This container defines global PIM configuration and state
information.
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: This container defines global PIM configuration and state
information.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/interfaces (container)

    YANG Description: Configuration and state data for PIM on each interface.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Configuration and state data for PIM on each interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('global_', global_), ('interfaces', interfaces), ])


from . import global_
from . import interfaces
class pim(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/pim. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level PIM configuration and operational state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__interfaces',)

  _yang_name = 'pim'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'pim']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/global (container)

    YANG Description: This container defines global PIM configuration and state
information.
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: This container defines global PIM configuration and state
information.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/interfaces (container)

    YANG Description: Configuration and state data for PIM on each interface.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Configuration and state data for PIM on each interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('global_', global_), ('interfaces', interfaces), ])


from . import global_
from . import interfaces
class pim(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/pim. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level PIM configuration and operational state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__interfaces',)

  _yang_name = 'pim'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'pim']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/global (container)

    YANG Description: This container defines global PIM configuration and state
information.
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: This container defines global PIM configuration and state
information.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/interfaces (container)

    YANG Description: Configuration and state data for PIM on each interface.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /network_instances/network_instance/protocols/protocol/pim/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Configuration and state data for PIM on each interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('global_', global_), ('interfaces', interfaces), ])


