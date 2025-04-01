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
from . import fabric_block_error
class fabric_block(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/integrated-circuit/pipeline-counters/errors/fabric-block. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IC fabric block subsystem connects the IC to the external
systems fabric subsystem
  """
  __slots__ = ('_path_helper', '_extmethods', '__fabric_block_error',)

  _yang_name = 'fabric-block'
  _yang_namespace = 'http://openconfig.net/yang/platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__fabric_block_error = YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)

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
      return ['components', 'component', 'integrated-circuit', 'pipeline-counters', 'errors', 'fabric-block']

  def _get_fabric_block_error(self):
    """
    Getter method for fabric_block_error, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters/errors/fabric_block/fabric_block_error (list)

    YANG Description: An individual error within the fabric block. Each error counter
is uniquely identified by the name of the error.
    """
    return self.__fabric_block_error
      
  def _set_fabric_block_error(self, v, load=False):
    """
    Setter method for fabric_block_error, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters/errors/fabric_block/fabric_block_error (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_block_error is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_block_error() directly.

    YANG Description: An individual error within the fabric block. Each error counter
is uniquely identified by the name of the error.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_block_error must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)""",
        })

    self.__fabric_block_error = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_block_error(self):
    self.__fabric_block_error = YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)

  fabric_block_error = __builtin__.property(_get_fabric_block_error)


  _pyangbind_elements = OrderedDict([('fabric_block_error', fabric_block_error), ])


from . import fabric_block_error
class fabric_block(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform-common - based on the path /components/component/integrated-circuit/pipeline-counters/errors/fabric-block. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IC fabric block subsystem connects the IC to the external
systems fabric subsystem
  """
  __slots__ = ('_path_helper', '_extmethods', '__fabric_block_error',)

  _yang_name = 'fabric-block'
  _yang_namespace = 'http://openconfig.net/yang/platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__fabric_block_error = YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)

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
      return ['components', 'component', 'integrated-circuit', 'pipeline-counters', 'errors', 'fabric-block']

  def _get_fabric_block_error(self):
    """
    Getter method for fabric_block_error, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters/errors/fabric_block/fabric_block_error (list)

    YANG Description: An individual error within the fabric block. Each error counter
is uniquely identified by the name of the error.
    """
    return self.__fabric_block_error
      
  def _set_fabric_block_error(self, v, load=False):
    """
    Setter method for fabric_block_error, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters/errors/fabric_block/fabric_block_error (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_block_error is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_block_error() directly.

    YANG Description: An individual error within the fabric block. Each error counter
is uniquely identified by the name of the error.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_block_error must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)""",
        })

    self.__fabric_block_error = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_block_error(self):
    self.__fabric_block_error = YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)

  fabric_block_error = __builtin__.property(_get_fabric_block_error)


  _pyangbind_elements = OrderedDict([('fabric_block_error', fabric_block_error), ])


from . import fabric_block_error
class fabric_block(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/integrated-circuit/pipeline-counters/errors/fabric-block. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IC fabric block subsystem connects the IC to the external
systems fabric subsystem
  """
  __slots__ = ('_path_helper', '_extmethods', '__fabric_block_error',)

  _yang_name = 'fabric-block'
  _yang_namespace = 'http://openconfig.net/yang/platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__fabric_block_error = YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)

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
      return ['components', 'component', 'integrated-circuit', 'pipeline-counters', 'errors', 'fabric-block']

  def _get_fabric_block_error(self):
    """
    Getter method for fabric_block_error, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters/errors/fabric_block/fabric_block_error (list)

    YANG Description: An individual error within the fabric block. Each error counter
is uniquely identified by the name of the error.
    """
    return self.__fabric_block_error
      
  def _set_fabric_block_error(self, v, load=False):
    """
    Setter method for fabric_block_error, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters/errors/fabric_block/fabric_block_error (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_block_error is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_block_error() directly.

    YANG Description: An individual error within the fabric block. Each error counter
is uniquely identified by the name of the error.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_block_error must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)""",
        })

    self.__fabric_block_error = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_block_error(self):
    self.__fabric_block_error = YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)

  fabric_block_error = __builtin__.property(_get_fabric_block_error)


  _pyangbind_elements = OrderedDict([('fabric_block_error', fabric_block_error), ])


from . import fabric_block_error
class fabric_block(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform-common - based on the path /components/component/integrated-circuit/pipeline-counters/errors/fabric-block. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IC fabric block subsystem connects the IC to the external
systems fabric subsystem
  """
  __slots__ = ('_path_helper', '_extmethods', '__fabric_block_error',)

  _yang_name = 'fabric-block'
  _yang_namespace = 'http://openconfig.net/yang/platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__fabric_block_error = YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)

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
      return ['components', 'component', 'integrated-circuit', 'pipeline-counters', 'errors', 'fabric-block']

  def _get_fabric_block_error(self):
    """
    Getter method for fabric_block_error, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters/errors/fabric_block/fabric_block_error (list)

    YANG Description: An individual error within the fabric block. Each error counter
is uniquely identified by the name of the error.
    """
    return self.__fabric_block_error
      
  def _set_fabric_block_error(self, v, load=False):
    """
    Setter method for fabric_block_error, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters/errors/fabric_block/fabric_block_error (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_block_error is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_block_error() directly.

    YANG Description: An individual error within the fabric block. Each error counter
is uniquely identified by the name of the error.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_block_error must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)""",
        })

    self.__fabric_block_error = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_block_error(self):
    self.__fabric_block_error = YANGDynClass(base=YANGListType("name",fabric_block_error.fabric_block_error, yang_name="fabric-block-error", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="fabric-block-error", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='list', is_config=False)

  fabric_block_error = __builtin__.property(_get_fabric_block_error)


  _pyangbind_elements = OrderedDict([('fabric_block_error', fabric_block_error), ])


