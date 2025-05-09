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
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/interface-ref/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state for interface-ref
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface','__subinterface',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/acl'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface = YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    self.__subinterface = YANGDynClass(base=str, is_leaf=True, yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)

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
      return ['acl', 'interfaces', 'interface', 'interface-ref', 'state']

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /acl/interfaces/interface/interface_ref/state/interface (leafref)

    YANG Description: Reference to a base interface.  If a reference to a
subinterface is required, this leaf must be specified
to indicate the base interface.
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /acl/interfaces/interface/interface_ref/state/interface (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Reference to a base interface.  If a reference to a
subinterface is required, this leaf must be specified
to indicate the base interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)


  def _get_subinterface(self):
    """
    Getter method for subinterface, mapped from YANG variable /acl/interfaces/interface/interface_ref/state/subinterface (leafref)

    YANG Description: Reference to a subinterface -- this requires the base
interface to be specified using the interface leaf in
this container.  If only a reference to a base interface
is required, this leaf should not be set.
    """
    return self.__subinterface
      
  def _set_subinterface(self, v, load=False):
    """
    Setter method for subinterface, mapped from YANG variable /acl/interfaces/interface/interface_ref/state/subinterface (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subinterface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subinterface() directly.

    YANG Description: Reference to a subinterface -- this requires the base
interface to be specified using the interface leaf in
this container.  If only a reference to a base interface
is required, this leaf should not be set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subinterface must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)""",
        })

    self.__subinterface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subinterface(self):
    self.__subinterface = YANGDynClass(base=str, is_leaf=True, yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)

  interface = __builtin__.property(_get_interface)
  subinterface = __builtin__.property(_get_subinterface)


  _pyangbind_elements = OrderedDict([('interface', interface), ('subinterface', subinterface), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/interface-ref/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state for interface-ref
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface','__subinterface',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/acl'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface = YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    self.__subinterface = YANGDynClass(base=str, is_leaf=True, yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)

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
      return ['acl', 'interfaces', 'interface', 'interface-ref', 'state']

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /acl/interfaces/interface/interface_ref/state/interface (leafref)

    YANG Description: Reference to a base interface.  If a reference to a
subinterface is required, this leaf must be specified
to indicate the base interface.
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /acl/interfaces/interface/interface_ref/state/interface (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Reference to a base interface.  If a reference to a
subinterface is required, this leaf must be specified
to indicate the base interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=str, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)


  def _get_subinterface(self):
    """
    Getter method for subinterface, mapped from YANG variable /acl/interfaces/interface/interface_ref/state/subinterface (leafref)

    YANG Description: Reference to a subinterface -- this requires the base
interface to be specified using the interface leaf in
this container.  If only a reference to a base interface
is required, this leaf should not be set.
    """
    return self.__subinterface
      
  def _set_subinterface(self, v, load=False):
    """
    Setter method for subinterface, mapped from YANG variable /acl/interfaces/interface/interface_ref/state/subinterface (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subinterface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subinterface() directly.

    YANG Description: Reference to a subinterface -- this requires the base
interface to be specified using the interface leaf in
this container.  If only a reference to a base interface
is required, this leaf should not be set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subinterface must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)""",
        })

    self.__subinterface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subinterface(self):
    self.__subinterface = YANGDynClass(base=str, is_leaf=True, yang_name="subinterface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='leafref', is_config=False)

  interface = __builtin__.property(_get_interface)
  subinterface = __builtin__.property(_get_subinterface)


  _pyangbind_elements = OrderedDict([('interface', interface), ('subinterface', subinterface), ])


