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
from . import keychain
class keychains(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-keychain - based on the path /keychains. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines keychains.
  """
  __slots__ = ('_path_helper', '_extmethods', '__keychain',)

  _yang_name = 'keychains'
  _yang_namespace = 'http://openconfig.net/yang/oc-keychain'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__keychain = YANGDynClass(base=YANGListType("name",keychain.keychain, yang_name="keychain", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="keychain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='list', is_config=True)

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
      return ['keychains']

  def _get_keychain(self):
    """
    Getter method for keychain, mapped from YANG variable /keychains/keychain (list)

    YANG Description: List of defined keychains.
    """
    return self.__keychain
      
  def _set_keychain(self, v, load=False):
    """
    Setter method for keychain, mapped from YANG variable /keychains/keychain (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_keychain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_keychain() directly.

    YANG Description: List of defined keychains.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",keychain.keychain, yang_name="keychain", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="keychain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """keychain must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",keychain.keychain, yang_name="keychain", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="keychain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='list', is_config=True)""",
        })

    self.__keychain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_keychain(self):
    self.__keychain = YANGDynClass(base=YANGListType("name",keychain.keychain, yang_name="keychain", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="keychain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='list', is_config=True)

  keychain = __builtin__.property(_get_keychain, _set_keychain)


  _pyangbind_elements = OrderedDict([('keychain', keychain), ])


from . import keychain
class keychains(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-keychain - based on the path /keychains. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines keychains.
  """
  __slots__ = ('_path_helper', '_extmethods', '__keychain',)

  _yang_name = 'keychains'
  _yang_namespace = 'http://openconfig.net/yang/oc-keychain'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__keychain = YANGDynClass(base=YANGListType("name",keychain.keychain, yang_name="keychain", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="keychain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='list', is_config=True)

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
      return ['keychains']

  def _get_keychain(self):
    """
    Getter method for keychain, mapped from YANG variable /keychains/keychain (list)

    YANG Description: List of defined keychains.
    """
    return self.__keychain
      
  def _set_keychain(self, v, load=False):
    """
    Setter method for keychain, mapped from YANG variable /keychains/keychain (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_keychain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_keychain() directly.

    YANG Description: List of defined keychains.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",keychain.keychain, yang_name="keychain", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="keychain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """keychain must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",keychain.keychain, yang_name="keychain", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="keychain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='list', is_config=True)""",
        })

    self.__keychain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_keychain(self):
    self.__keychain = YANGDynClass(base=YANGListType("name",keychain.keychain, yang_name="keychain", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="keychain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-keychain', defining_module='openconfig-keychain', yang_type='list', is_config=True)

  keychain = __builtin__.property(_get_keychain, _set_keychain)


  _pyangbind_elements = OrderedDict([('keychain', keychain), ])


