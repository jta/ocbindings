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
  from YANG module openconfig-system - based on the path /system/mount-points/mount-point/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State of system mount point.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__storage_component','__size','__available','__utilized','__type',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    self.__storage_component = YANGDynClass(base=str, is_leaf=True, yang_name="storage-component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)
    self.__size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    self.__available = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="available", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    self.__utilized = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    self.__type = YANGDynClass(base=str, is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)

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
      return ['system', 'mount-points', 'mount-point', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/mount_points/mount_point/state/name (string)

    YANG Description: Mount point name.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/mount_points/mount_point/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Mount point name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)


  def _get_storage_component(self):
    """
    Getter method for storage_component, mapped from YANG variable /system/mount_points/mount_point/state/storage_component (leafref)

    YANG Description: In the case that the filesystem that is mounted corresponds to a
physical or logical component within the system, this leaf provides
a reference to the hosting component within the /components
hierarchy.

The reference should be to the most specific component (e.g., if an
entry for /dev/sda1 exists, then this should be referred to,
otherwise a reference to /dev/sda may be provided.
    """
    return self.__storage_component
      
  def _set_storage_component(self, v, load=False):
    """
    Setter method for storage_component, mapped from YANG variable /system/mount_points/mount_point/state/storage_component (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_storage_component is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_storage_component() directly.

    YANG Description: In the case that the filesystem that is mounted corresponds to a
physical or logical component within the system, this leaf provides
a reference to the hosting component within the /components
hierarchy.

The reference should be to the most specific component (e.g., if an
entry for /dev/sda1 exists, then this should be referred to,
otherwise a reference to /dev/sda may be provided.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="storage-component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """storage_component must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="storage-component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)""",
        })

    self.__storage_component = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_storage_component(self):
    self.__storage_component = YANGDynClass(base=str, is_leaf=True, yang_name="storage-component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)


  def _get_size(self):
    """
    Getter method for size, mapped from YANG variable /system/mount_points/mount_point/state/size (uint64)

    YANG Description: The total size of the initialised filesystem.
    """
    return self.__size
      
  def _set_size(self, v, load=False):
    """
    Setter method for size, mapped from YANG variable /system/mount_points/mount_point/state/size (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_size() directly.

    YANG Description: The total size of the initialised filesystem.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """size must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_size(self):
    self.__size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_available(self):
    """
    Getter method for available, mapped from YANG variable /system/mount_points/mount_point/state/available (uint64)

    YANG Description: The amount of unused space on the filesystem.
    """
    return self.__available
      
  def _set_available(self, v, load=False):
    """
    Setter method for available, mapped from YANG variable /system/mount_points/mount_point/state/available (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_available is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_available() directly.

    YANG Description: The amount of unused space on the filesystem.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="available", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """available must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="available", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__available = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_available(self):
    self.__available = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="available", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_utilized(self):
    """
    Getter method for utilized, mapped from YANG variable /system/mount_points/mount_point/state/utilized (uint64)

    YANG Description: The amount of space currently in use on the filesystem.
    """
    return self.__utilized
      
  def _set_utilized(self, v, load=False):
    """
    Setter method for utilized, mapped from YANG variable /system/mount_points/mount_point/state/utilized (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_utilized is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_utilized() directly.

    YANG Description: The amount of space currently in use on the filesystem.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """utilized must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__utilized = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_utilized(self):
    self.__utilized = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /system/mount_points/mount_point/state/type (string)

    YANG Description: A human readable string indicating the filesystem type used
for storage.  Examples might include flash, hard disk, tmpfs/ramdisk
or remote/network based storage.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /system/mount_points/mount_point/state/type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: A human readable string indicating the filesystem type used
for storage.  Examples might include flash, hard disk, tmpfs/ramdisk
or remote/network based storage.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=str, is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)

  name = __builtin__.property(_get_name)
  storage_component = __builtin__.property(_get_storage_component)
  size = __builtin__.property(_get_size)
  available = __builtin__.property(_get_available)
  utilized = __builtin__.property(_get_utilized)
  type = __builtin__.property(_get_type)


  _pyangbind_elements = OrderedDict([('name', name), ('storage_component', storage_component), ('size', size), ('available', available), ('utilized', utilized), ('type', type), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/mount-points/mount-point/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State of system mount point.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__storage_component','__size','__available','__utilized','__type',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    self.__storage_component = YANGDynClass(base=str, is_leaf=True, yang_name="storage-component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)
    self.__size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    self.__available = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="available", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    self.__utilized = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    self.__type = YANGDynClass(base=str, is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)

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
      return ['system', 'mount-points', 'mount-point', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/mount_points/mount_point/state/name (string)

    YANG Description: Mount point name.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/mount_points/mount_point/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Mount point name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)


  def _get_storage_component(self):
    """
    Getter method for storage_component, mapped from YANG variable /system/mount_points/mount_point/state/storage_component (leafref)

    YANG Description: In the case that the filesystem that is mounted corresponds to a
physical or logical component within the system, this leaf provides
a reference to the hosting component within the /components
hierarchy.

The reference should be to the most specific component (e.g., if an
entry for /dev/sda1 exists, then this should be referred to,
otherwise a reference to /dev/sda may be provided.
    """
    return self.__storage_component
      
  def _set_storage_component(self, v, load=False):
    """
    Setter method for storage_component, mapped from YANG variable /system/mount_points/mount_point/state/storage_component (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_storage_component is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_storage_component() directly.

    YANG Description: In the case that the filesystem that is mounted corresponds to a
physical or logical component within the system, this leaf provides
a reference to the hosting component within the /components
hierarchy.

The reference should be to the most specific component (e.g., if an
entry for /dev/sda1 exists, then this should be referred to,
otherwise a reference to /dev/sda may be provided.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="storage-component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """storage_component must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="storage-component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)""",
        })

    self.__storage_component = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_storage_component(self):
    self.__storage_component = YANGDynClass(base=str, is_leaf=True, yang_name="storage-component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)


  def _get_size(self):
    """
    Getter method for size, mapped from YANG variable /system/mount_points/mount_point/state/size (uint64)

    YANG Description: The total size of the initialised filesystem.
    """
    return self.__size
      
  def _set_size(self, v, load=False):
    """
    Setter method for size, mapped from YANG variable /system/mount_points/mount_point/state/size (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_size() directly.

    YANG Description: The total size of the initialised filesystem.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """size must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_size(self):
    self.__size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_available(self):
    """
    Getter method for available, mapped from YANG variable /system/mount_points/mount_point/state/available (uint64)

    YANG Description: The amount of unused space on the filesystem.
    """
    return self.__available
      
  def _set_available(self, v, load=False):
    """
    Setter method for available, mapped from YANG variable /system/mount_points/mount_point/state/available (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_available is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_available() directly.

    YANG Description: The amount of unused space on the filesystem.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="available", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """available must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="available", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__available = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_available(self):
    self.__available = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="available", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_utilized(self):
    """
    Getter method for utilized, mapped from YANG variable /system/mount_points/mount_point/state/utilized (uint64)

    YANG Description: The amount of space currently in use on the filesystem.
    """
    return self.__utilized
      
  def _set_utilized(self, v, load=False):
    """
    Setter method for utilized, mapped from YANG variable /system/mount_points/mount_point/state/utilized (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_utilized is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_utilized() directly.

    YANG Description: The amount of space currently in use on the filesystem.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """utilized must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)""",
        })

    self.__utilized = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_utilized(self):
    self.__utilized = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint64', is_config=False)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /system/mount_points/mount_point/state/type (string)

    YANG Description: A human readable string indicating the filesystem type used
for storage.  Examples might include flash, hard disk, tmpfs/ramdisk
or remote/network based storage.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /system/mount_points/mount_point/state/type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: A human readable string indicating the filesystem type used
for storage.  Examples might include flash, hard disk, tmpfs/ramdisk
or remote/network based storage.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=str, is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)

  name = __builtin__.property(_get_name)
  storage_component = __builtin__.property(_get_storage_component)
  size = __builtin__.property(_get_size)
  available = __builtin__.property(_get_available)
  utilized = __builtin__.property(_get_utilized)
  type = __builtin__.property(_get_type)


  _pyangbind_elements = OrderedDict([('name', name), ('storage_component', storage_component), ('size', size), ('available', available), ('utilized', utilized), ('type', type), ])


