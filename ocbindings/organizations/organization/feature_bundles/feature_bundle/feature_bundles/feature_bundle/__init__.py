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
class feature_bundle(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-module-catalog - based on the path /organizations/organization/feature-bundles/feature-bundle/feature-bundles/feature-bundle. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of feature bundles included in the current
feature bundle.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__publisher','__version',)

  _yang_name = 'feature-bundle'
  _yang_namespace = 'http://openconfig.net/yang/module-catalog'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    self.__publisher = YANGDynClass(base=str, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    self.__version = YANGDynClass(base=str, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)

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
      return ['organizations', 'organization', 'feature-bundles', 'feature-bundle', 'feature-bundles', 'feature-bundle']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/name (leafref)

    YANG Description: Name of the referenced feature bundle
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the referenced feature bundle
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)


  def _get_publisher(self):
    """
    Getter method for publisher, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/publisher (leafref)

    YANG Description: Publisher of the referenced feature bundle
    """
    return self.__publisher
      
  def _set_publisher(self, v, load=False):
    """
    Setter method for publisher, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/publisher (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_publisher is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_publisher() directly.

    YANG Description: Publisher of the referenced feature bundle
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """publisher must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)""",
        })

    self.__publisher = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_publisher(self):
    self.__publisher = YANGDynClass(base=str, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)


  def _get_version(self):
    """
    Getter method for version, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/version (oc-cat-types:module-version-type)

    YANG Description: Version of the referenced feature bundle
    """
    return self.__version
      
  def _set_version(self, v, load=False):
    """
    Setter method for version, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/version (oc-cat-types:module-version-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_version() directly.

    YANG Description: Version of the referenced feature bundle
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """version must be of a type compatible with oc-cat-types:module-version-type""",
          'defined-type': "oc-cat-types:module-version-type",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)""",
        })

    self.__version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_version(self):
    self.__version = YANGDynClass(base=str, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  publisher = __builtin__.property(_get_publisher, _set_publisher)
  version = __builtin__.property(_get_version, _set_version)


  _pyangbind_elements = OrderedDict([('name', name), ('publisher', publisher), ('version', version), ])


class feature_bundle(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-module-catalog - based on the path /organizations/organization/feature-bundles/feature-bundle/feature-bundles/feature-bundle. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of feature bundles included in the current
feature bundle.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__publisher','__version',)

  _yang_name = 'feature-bundle'
  _yang_namespace = 'http://openconfig.net/yang/module-catalog'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    self.__publisher = YANGDynClass(base=str, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    self.__version = YANGDynClass(base=str, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)

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
      return ['organizations', 'organization', 'feature-bundles', 'feature-bundle', 'feature-bundles', 'feature-bundle']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/name (leafref)

    YANG Description: Name of the referenced feature bundle
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the referenced feature bundle
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=str, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)


  def _get_publisher(self):
    """
    Getter method for publisher, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/publisher (leafref)

    YANG Description: Publisher of the referenced feature bundle
    """
    return self.__publisher
      
  def _set_publisher(self, v, load=False):
    """
    Setter method for publisher, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/publisher (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_publisher is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_publisher() directly.

    YANG Description: Publisher of the referenced feature bundle
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """publisher must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)""",
        })

    self.__publisher = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_publisher(self):
    self.__publisher = YANGDynClass(base=str, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)


  def _get_version(self):
    """
    Getter method for version, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/version (oc-cat-types:module-version-type)

    YANG Description: Version of the referenced feature bundle
    """
    return self.__version
      
  def _set_version(self, v, load=False):
    """
    Setter method for version, mapped from YANG variable /organizations/organization/feature_bundles/feature_bundle/feature_bundles/feature_bundle/version (oc-cat-types:module-version-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_version() directly.

    YANG Description: Version of the referenced feature bundle
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """version must be of a type compatible with oc-cat-types:module-version-type""",
          'defined-type': "oc-cat-types:module-version-type",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)""",
        })

    self.__version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_version(self):
    self.__version = YANGDynClass(base=str, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  publisher = __builtin__.property(_get_publisher, _set_publisher)
  version = __builtin__.property(_get_version, _set_version)


  _pyangbind_elements = OrderedDict([('name', name), ('publisher', publisher), ('version', version), ])


