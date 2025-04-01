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
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/logging/files/file/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for logfile
  """
  __slots__ = ('_path_helper', '_extmethods', '__filename_prefix','__path','__rotate','__max_size','__max_open_time',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__filename_prefix = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="filename-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    self.__path = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    self.__rotate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    self.__max_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="max-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    self.__max_open_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1440), is_leaf=True, yang_name="max-open-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'logging', 'files', 'file', 'config']

  def _get_filename_prefix(self):
    """
    Getter method for filename_prefix, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/filename_prefix (string)

    YANG Description: A name used for the file.  It is expected that an
implementation may append timestamp, serial-number or
other identifier to the filename.
    """
    return self.__filename_prefix
      
  def _set_filename_prefix(self, v, load=False):
    """
    Setter method for filename_prefix, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/filename_prefix (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filename_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filename_prefix() directly.

    YANG Description: A name used for the file.  It is expected that an
implementation may append timestamp, serial-number or
other identifier to the filename.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="filename-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filename_prefix must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="filename-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)""",
        })

    self.__filename_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filename_prefix(self):
    self.__filename_prefix = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="filename-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)


  def _get_path(self):
    """
    Getter method for path, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/path (string)

    YANG Description: The fully specified path of the folder where the
logfile is stored.  The path is implementation specific
and may include attributes such as a drive identifier.
    """
    return self.__path
      
  def _set_path(self, v, load=False):
    """
    Setter method for path, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/path (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path() directly.

    YANG Description: The fully specified path of the folder where the
logfile is stored.  The path is implementation specific
and may include attributes such as a drive identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)""",
        })

    self.__path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path(self):
    self.__path = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)


  def _get_rotate(self):
    """
    Getter method for rotate, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/rotate (uint32)

    YANG Description: Used for logfile rotation.
Log files are rotated the number of times defined by
this leaf.
The default value of 1 indicates that there will be one
rotation file and one active file.  A 0 value indicates
old versions are removed rather than rotated.
    """
    return self.__rotate
      
  def _set_rotate(self, v, load=False):
    """
    Setter method for rotate, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/rotate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rotate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rotate() directly.

    YANG Description: Used for logfile rotation.
Log files are rotated the number of times defined by
this leaf.
The default value of 1 indicates that there will be one
rotation file and one active file.  A 0 value indicates
old versions are removed rather than rotated.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rotate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)""",
        })

    self.__rotate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rotate(self):
    self.__rotate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)


  def _get_max_size(self):
    """
    Getter method for max_size, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/max_size (uint32)

    YANG Description: Used for logfile rotation.
Maximum size in Bytes, logfile may grow to. When logfile
reach this size it triggers log rotation. The log file need to
be save, closed, and new file open or future log storage.
If needed oldest logfile of same prefix shall be deleted to
    """
    return self.__max_size
      
  def _set_max_size(self, v, load=False):
    """
    Setter method for max_size, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/max_size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_size() directly.

    YANG Description: Used for logfile rotation.
Maximum size in Bytes, logfile may grow to. When logfile
reach this size it triggers log rotation. The log file need to
be save, closed, and new file open or future log storage.
If needed oldest logfile of same prefix shall be deleted to
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="max-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="max-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)""",
        })

    self.__max_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_size(self):
    self.__max_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="max-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)


  def _get_max_open_time(self):
    """
    Getter method for max_open_time, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/max_open_time (uint32)

    YANG Description: Used for logfile rotation.
Maximum time, in minutes, the logfile can be open. When expires,
it triggers log rotation.
Actions are same ans when log file reaches its max-size.
it need to be closed, save, and new file open or future log
storage. If needed oldest logfile of same prefix shall be
deleted to 
    """
    return self.__max_open_time
      
  def _set_max_open_time(self, v, load=False):
    """
    Setter method for max_open_time, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/max_open_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_open_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_open_time() directly.

    YANG Description: Used for logfile rotation.
Maximum time, in minutes, the logfile can be open. When expires,
it triggers log rotation.
Actions are same ans when log file reaches its max-size.
it need to be closed, save, and new file open or future log
storage. If needed oldest logfile of same prefix shall be
deleted to 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1440), is_leaf=True, yang_name="max-open-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_open_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1440), is_leaf=True, yang_name="max-open-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)""",
        })

    self.__max_open_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_open_time(self):
    self.__max_open_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1440), is_leaf=True, yang_name="max-open-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)

  filename_prefix = __builtin__.property(_get_filename_prefix, _set_filename_prefix)
  path = __builtin__.property(_get_path, _set_path)
  rotate = __builtin__.property(_get_rotate, _set_rotate)
  max_size = __builtin__.property(_get_max_size, _set_max_size)
  max_open_time = __builtin__.property(_get_max_open_time, _set_max_open_time)


  _pyangbind_elements = OrderedDict([('filename_prefix', filename_prefix), ('path', path), ('rotate', rotate), ('max_size', max_size), ('max_open_time', max_open_time), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/logging/files/file/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for logfile
  """
  __slots__ = ('_path_helper', '_extmethods', '__filename_prefix','__path','__rotate','__max_size','__max_open_time',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__filename_prefix = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="filename-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    self.__path = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    self.__rotate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    self.__max_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="max-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    self.__max_open_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1440), is_leaf=True, yang_name="max-open-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'logging', 'files', 'file', 'config']

  def _get_filename_prefix(self):
    """
    Getter method for filename_prefix, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/filename_prefix (string)

    YANG Description: A name used for the file.  It is expected that an
implementation may append timestamp, serial-number or
other identifier to the filename.
    """
    return self.__filename_prefix
      
  def _set_filename_prefix(self, v, load=False):
    """
    Setter method for filename_prefix, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/filename_prefix (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filename_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filename_prefix() directly.

    YANG Description: A name used for the file.  It is expected that an
implementation may append timestamp, serial-number or
other identifier to the filename.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="filename-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filename_prefix must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="filename-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)""",
        })

    self.__filename_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filename_prefix(self):
    self.__filename_prefix = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="filename-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)


  def _get_path(self):
    """
    Getter method for path, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/path (string)

    YANG Description: The fully specified path of the folder where the
logfile is stored.  The path is implementation specific
and may include attributes such as a drive identifier.
    """
    return self.__path
      
  def _set_path(self, v, load=False):
    """
    Setter method for path, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/path (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path() directly.

    YANG Description: The fully specified path of the folder where the
logfile is stored.  The path is implementation specific
and may include attributes such as a drive identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)""",
        })

    self.__path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path(self):
    self.__path = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_dict={'length': ['0..255']}), is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)


  def _get_rotate(self):
    """
    Getter method for rotate, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/rotate (uint32)

    YANG Description: Used for logfile rotation.
Log files are rotated the number of times defined by
this leaf.
The default value of 1 indicates that there will be one
rotation file and one active file.  A 0 value indicates
old versions are removed rather than rotated.
    """
    return self.__rotate
      
  def _set_rotate(self, v, load=False):
    """
    Setter method for rotate, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/rotate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rotate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rotate() directly.

    YANG Description: Used for logfile rotation.
Log files are rotated the number of times defined by
this leaf.
The default value of 1 indicates that there will be one
rotation file and one active file.  A 0 value indicates
old versions are removed rather than rotated.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rotate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)""",
        })

    self.__rotate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rotate(self):
    self.__rotate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)


  def _get_max_size(self):
    """
    Getter method for max_size, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/max_size (uint32)

    YANG Description: Used for logfile rotation.
Maximum size in Bytes, logfile may grow to. When logfile
reach this size it triggers log rotation. The log file need to
be save, closed, and new file open or future log storage.
If needed oldest logfile of same prefix shall be deleted to
    """
    return self.__max_size
      
  def _set_max_size(self, v, load=False):
    """
    Setter method for max_size, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/max_size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_size() directly.

    YANG Description: Used for logfile rotation.
Maximum size in Bytes, logfile may grow to. When logfile
reach this size it triggers log rotation. The log file need to
be save, closed, and new file open or future log storage.
If needed oldest logfile of same prefix shall be deleted to
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="max-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="max-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)""",
        })

    self.__max_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_size(self):
    self.__max_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="max-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)


  def _get_max_open_time(self):
    """
    Getter method for max_open_time, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/max_open_time (uint32)

    YANG Description: Used for logfile rotation.
Maximum time, in minutes, the logfile can be open. When expires,
it triggers log rotation.
Actions are same ans when log file reaches its max-size.
it need to be closed, save, and new file open or future log
storage. If needed oldest logfile of same prefix shall be
deleted to 
    """
    return self.__max_open_time
      
  def _set_max_open_time(self, v, load=False):
    """
    Setter method for max_open_time, mapped from YANG variable /access_points/access_point/system/logging/files/file/config/max_open_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_open_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_open_time() directly.

    YANG Description: Used for logfile rotation.
Maximum time, in minutes, the logfile can be open. When expires,
it triggers log rotation.
Actions are same ans when log file reaches its max-size.
it need to be closed, save, and new file open or future log
storage. If needed oldest logfile of same prefix shall be
deleted to 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1440), is_leaf=True, yang_name="max-open-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_open_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1440), is_leaf=True, yang_name="max-open-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)""",
        })

    self.__max_open_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_open_time(self):
    self.__max_open_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1440), is_leaf=True, yang_name="max-open-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint32', is_config=True)

  filename_prefix = __builtin__.property(_get_filename_prefix, _set_filename_prefix)
  path = __builtin__.property(_get_path, _set_path)
  rotate = __builtin__.property(_get_rotate, _set_rotate)
  max_size = __builtin__.property(_get_max_size, _set_max_size)
  max_open_time = __builtin__.property(_get_max_open_time, _set_max_open_time)


  _pyangbind_elements = OrderedDict([('filename_prefix', filename_prefix), ('path', path), ('rotate', rotate), ('max_size', max_size), ('max_open_time', max_open_time), ])


