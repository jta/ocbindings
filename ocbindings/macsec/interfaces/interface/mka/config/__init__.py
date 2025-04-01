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
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/mka/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for MKA interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__mka_policy','__key_chain',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/macsec'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mka_policy = YANGDynClass(base=str, is_leaf=True, yang_name="mka-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)
    self.__key_chain = YANGDynClass(base=str, is_leaf=True, yang_name="key-chain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)

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
      return ['macsec', 'interfaces', 'interface', 'mka', 'config']

  def _get_mka_policy(self):
    """
    Getter method for mka_policy, mapped from YANG variable /macsec/interfaces/interface/mka/config/mka_policy (leafref)

    YANG Description: Apply MKA policy on the interface
    """
    return self.__mka_policy
      
  def _set_mka_policy(self, v, load=False):
    """
    Setter method for mka_policy, mapped from YANG variable /macsec/interfaces/interface/mka/config/mka_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mka_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mka_policy() directly.

    YANG Description: Apply MKA policy on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="mka-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mka_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="mka-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)""",
        })

    self.__mka_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mka_policy(self):
    self.__mka_policy = YANGDynClass(base=str, is_leaf=True, yang_name="mka-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)


  def _get_key_chain(self):
    """
    Getter method for key_chain, mapped from YANG variable /macsec/interfaces/interface/mka/config/key_chain (leafref)

    YANG Description: Configure Key Chain name
    """
    return self.__key_chain
      
  def _set_key_chain(self, v, load=False):
    """
    Setter method for key_chain, mapped from YANG variable /macsec/interfaces/interface/mka/config/key_chain (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_chain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_chain() directly.

    YANG Description: Configure Key Chain name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="key-chain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_chain must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="key-chain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)""",
        })

    self.__key_chain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_chain(self):
    self.__key_chain = YANGDynClass(base=str, is_leaf=True, yang_name="key-chain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)

  mka_policy = __builtin__.property(_get_mka_policy, _set_mka_policy)
  key_chain = __builtin__.property(_get_key_chain, _set_key_chain)


  _pyangbind_elements = OrderedDict([('mka_policy', mka_policy), ('key_chain', key_chain), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/mka/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for MKA interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__mka_policy','__key_chain',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/macsec'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mka_policy = YANGDynClass(base=str, is_leaf=True, yang_name="mka-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)
    self.__key_chain = YANGDynClass(base=str, is_leaf=True, yang_name="key-chain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)

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
      return ['macsec', 'interfaces', 'interface', 'mka', 'config']

  def _get_mka_policy(self):
    """
    Getter method for mka_policy, mapped from YANG variable /macsec/interfaces/interface/mka/config/mka_policy (leafref)

    YANG Description: Apply MKA policy on the interface
    """
    return self.__mka_policy
      
  def _set_mka_policy(self, v, load=False):
    """
    Setter method for mka_policy, mapped from YANG variable /macsec/interfaces/interface/mka/config/mka_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mka_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mka_policy() directly.

    YANG Description: Apply MKA policy on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="mka-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mka_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="mka-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)""",
        })

    self.__mka_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mka_policy(self):
    self.__mka_policy = YANGDynClass(base=str, is_leaf=True, yang_name="mka-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)


  def _get_key_chain(self):
    """
    Getter method for key_chain, mapped from YANG variable /macsec/interfaces/interface/mka/config/key_chain (leafref)

    YANG Description: Configure Key Chain name
    """
    return self.__key_chain
      
  def _set_key_chain(self, v, load=False):
    """
    Setter method for key_chain, mapped from YANG variable /macsec/interfaces/interface/mka/config/key_chain (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_chain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_chain() directly.

    YANG Description: Configure Key Chain name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="key-chain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_chain must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="key-chain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)""",
        })

    self.__key_chain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_chain(self):
    self.__key_chain = YANGDynClass(base=str, is_leaf=True, yang_name="key-chain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='leafref', is_config=True)

  mka_policy = __builtin__.property(_get_mka_policy, _set_mka_policy)
  key_chain = __builtin__.property(_get_key_chain, _set_key_chain)


  _pyangbind_elements = OrderedDict([('mka_policy', mka_policy), ('key_chain', key_chain), ])


