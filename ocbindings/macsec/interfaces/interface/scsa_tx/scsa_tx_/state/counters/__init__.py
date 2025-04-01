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
class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/scsa-tx/scsa-tx/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Counters container for macsec-scsa-tx-interface-stats
  """
  __slots__ = ('_path_helper', '_extmethods', '__sc_auth_only','__sc_encrypted','__sa_auth_only','__sa_encrypted',)

  _yang_name = 'counters'
  _yang_namespace = 'http://openconfig.net/yang/macsec'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sc_auth_only = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__sc_encrypted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__sa_auth_only = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__sa_encrypted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)

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
      return ['macsec', 'interfaces', 'interface', 'scsa-tx', 'scsa-tx', 'state', 'counters']

  def _get_sc_auth_only(self):
    """
    Getter method for sc_auth_only, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sc_auth_only (oc-yang:counter64)

    YANG Description: Secure Channel Authenticated only TX Packets counter.
This counter reflects the number of authenticated only transmitted
packets in a secure channel.
    """
    return self.__sc_auth_only
      
  def _set_sc_auth_only(self, v, load=False):
    """
    Setter method for sc_auth_only, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sc_auth_only (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sc_auth_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sc_auth_only() directly.

    YANG Description: Secure Channel Authenticated only TX Packets counter.
This counter reflects the number of authenticated only transmitted
packets in a secure channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sc_auth_only must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__sc_auth_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sc_auth_only(self):
    self.__sc_auth_only = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_sc_encrypted(self):
    """
    Getter method for sc_encrypted, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sc_encrypted (oc-yang:counter64)

    YANG Description: Secure Channel Encrypted TX Packets counter.
This counter reflects the number of encrypted and authenticated
transmitted packets in a secure channel.
    """
    return self.__sc_encrypted
      
  def _set_sc_encrypted(self, v, load=False):
    """
    Setter method for sc_encrypted, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sc_encrypted (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sc_encrypted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sc_encrypted() directly.

    YANG Description: Secure Channel Encrypted TX Packets counter.
This counter reflects the number of encrypted and authenticated
transmitted packets in a secure channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sc_encrypted must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__sc_encrypted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sc_encrypted(self):
    self.__sc_encrypted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_sa_auth_only(self):
    """
    Getter method for sa_auth_only, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sa_auth_only (oc-yang:counter64)

    YANG Description: Secure Association Authenticated only TX Packets counter.
This counter reflects the number of authenticated only, transmitted
packets in a secure association.
    """
    return self.__sa_auth_only
      
  def _set_sa_auth_only(self, v, load=False):
    """
    Setter method for sa_auth_only, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sa_auth_only (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sa_auth_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sa_auth_only() directly.

    YANG Description: Secure Association Authenticated only TX Packets counter.
This counter reflects the number of authenticated only, transmitted
packets in a secure association.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sa_auth_only must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__sa_auth_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sa_auth_only(self):
    self.__sa_auth_only = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_sa_encrypted(self):
    """
    Getter method for sa_encrypted, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sa_encrypted (oc-yang:counter64)

    YANG Description: Secure Association Encrypted TX Packets counter.
This counter reflects the number of encrypted and authenticated
transmitted packets in a secure association.
    """
    return self.__sa_encrypted
      
  def _set_sa_encrypted(self, v, load=False):
    """
    Setter method for sa_encrypted, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sa_encrypted (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sa_encrypted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sa_encrypted() directly.

    YANG Description: Secure Association Encrypted TX Packets counter.
This counter reflects the number of encrypted and authenticated
transmitted packets in a secure association.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sa_encrypted must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__sa_encrypted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sa_encrypted(self):
    self.__sa_encrypted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)

  sc_auth_only = __builtin__.property(_get_sc_auth_only)
  sc_encrypted = __builtin__.property(_get_sc_encrypted)
  sa_auth_only = __builtin__.property(_get_sa_auth_only)
  sa_encrypted = __builtin__.property(_get_sa_encrypted)


  _pyangbind_elements = OrderedDict([('sc_auth_only', sc_auth_only), ('sc_encrypted', sc_encrypted), ('sa_auth_only', sa_auth_only), ('sa_encrypted', sa_encrypted), ])


class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/scsa-tx/scsa-tx/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Counters container for macsec-scsa-tx-interface-stats
  """
  __slots__ = ('_path_helper', '_extmethods', '__sc_auth_only','__sc_encrypted','__sa_auth_only','__sa_encrypted',)

  _yang_name = 'counters'
  _yang_namespace = 'http://openconfig.net/yang/macsec'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sc_auth_only = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__sc_encrypted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__sa_auth_only = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__sa_encrypted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)

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
      return ['macsec', 'interfaces', 'interface', 'scsa-tx', 'scsa-tx', 'state', 'counters']

  def _get_sc_auth_only(self):
    """
    Getter method for sc_auth_only, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sc_auth_only (oc-yang:counter64)

    YANG Description: Secure Channel Authenticated only TX Packets counter.
This counter reflects the number of authenticated only transmitted
packets in a secure channel.
    """
    return self.__sc_auth_only
      
  def _set_sc_auth_only(self, v, load=False):
    """
    Setter method for sc_auth_only, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sc_auth_only (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sc_auth_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sc_auth_only() directly.

    YANG Description: Secure Channel Authenticated only TX Packets counter.
This counter reflects the number of authenticated only transmitted
packets in a secure channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sc_auth_only must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__sc_auth_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sc_auth_only(self):
    self.__sc_auth_only = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_sc_encrypted(self):
    """
    Getter method for sc_encrypted, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sc_encrypted (oc-yang:counter64)

    YANG Description: Secure Channel Encrypted TX Packets counter.
This counter reflects the number of encrypted and authenticated
transmitted packets in a secure channel.
    """
    return self.__sc_encrypted
      
  def _set_sc_encrypted(self, v, load=False):
    """
    Setter method for sc_encrypted, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sc_encrypted (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sc_encrypted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sc_encrypted() directly.

    YANG Description: Secure Channel Encrypted TX Packets counter.
This counter reflects the number of encrypted and authenticated
transmitted packets in a secure channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sc_encrypted must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__sc_encrypted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sc_encrypted(self):
    self.__sc_encrypted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sc-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_sa_auth_only(self):
    """
    Getter method for sa_auth_only, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sa_auth_only (oc-yang:counter64)

    YANG Description: Secure Association Authenticated only TX Packets counter.
This counter reflects the number of authenticated only, transmitted
packets in a secure association.
    """
    return self.__sa_auth_only
      
  def _set_sa_auth_only(self, v, load=False):
    """
    Setter method for sa_auth_only, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sa_auth_only (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sa_auth_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sa_auth_only() directly.

    YANG Description: Secure Association Authenticated only TX Packets counter.
This counter reflects the number of authenticated only, transmitted
packets in a secure association.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sa_auth_only must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__sa_auth_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sa_auth_only(self):
    self.__sa_auth_only = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-auth-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_sa_encrypted(self):
    """
    Getter method for sa_encrypted, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sa_encrypted (oc-yang:counter64)

    YANG Description: Secure Association Encrypted TX Packets counter.
This counter reflects the number of encrypted and authenticated
transmitted packets in a secure association.
    """
    return self.__sa_encrypted
      
  def _set_sa_encrypted(self, v, load=False):
    """
    Setter method for sa_encrypted, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx/state/counters/sa_encrypted (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sa_encrypted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sa_encrypted() directly.

    YANG Description: Secure Association Encrypted TX Packets counter.
This counter reflects the number of encrypted and authenticated
transmitted packets in a secure association.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sa_encrypted must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__sa_encrypted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sa_encrypted(self):
    self.__sa_encrypted = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="sa-encrypted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)

  sc_auth_only = __builtin__.property(_get_sc_auth_only)
  sc_encrypted = __builtin__.property(_get_sc_encrypted)
  sa_auth_only = __builtin__.property(_get_sa_auth_only)
  sa_encrypted = __builtin__.property(_get_sa_encrypted)


  _pyangbind_elements = OrderedDict([('sc_auth_only', sc_auth_only), ('sc_encrypted', sc_encrypted), ('sa_auth_only', sa_auth_only), ('sa_encrypted', sa_encrypted), ])


