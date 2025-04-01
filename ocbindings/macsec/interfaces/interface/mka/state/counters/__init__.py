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
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/mka/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MKA interface counters
  """
  __slots__ = ('_path_helper', '_extmethods', '__in_mkpdu','__in_sak_mkpdu','__in_cak_mkpdu','__out_mkpdu','__out_sak_mkpdu','__out_cak_mkpdu',)

  _yang_name = 'counters'
  _yang_namespace = 'http://openconfig.net/yang/macsec'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__in_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__in_sak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__in_cak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__out_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__out_sak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__out_cak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)

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
      return ['macsec', 'interfaces', 'interface', 'mka', 'state', 'counters']

  def _get_in_mkpdu(self):
    """
    Getter method for in_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_mkpdu (oc-yang:counter64)

    YANG Description: Validated MKPDU received count
    """
    return self.__in_mkpdu
      
  def _set_in_mkpdu(self, v, load=False):
    """
    Setter method for in_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_mkpdu() directly.

    YANG Description: Validated MKPDU received count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_mkpdu(self):
    self.__in_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_sak_mkpdu(self):
    """
    Getter method for in_sak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_sak_mkpdu (oc-yang:counter64)

    YANG Description: Validated MKPDU received SAK count
    """
    return self.__in_sak_mkpdu
      
  def _set_in_sak_mkpdu(self, v, load=False):
    """
    Setter method for in_sak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_sak_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_sak_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_sak_mkpdu() directly.

    YANG Description: Validated MKPDU received SAK count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_sak_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_sak_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_sak_mkpdu(self):
    self.__in_sak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_cak_mkpdu(self):
    """
    Getter method for in_cak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_cak_mkpdu (oc-yang:counter64)

    YANG Description: Count of validated MKPDU  connectivity association key (CAK) pdus
received.  This counter is related to the group-cak feature in the
802.1X-2010 standard.
    """
    return self.__in_cak_mkpdu
      
  def _set_in_cak_mkpdu(self, v, load=False):
    """
    Setter method for in_cak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_cak_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_cak_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_cak_mkpdu() directly.

    YANG Description: Count of validated MKPDU  connectivity association key (CAK) pdus
received.  This counter is related to the group-cak feature in the
802.1X-2010 standard.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_cak_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_cak_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_cak_mkpdu(self):
    self.__in_cak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_mkpdu(self):
    """
    Getter method for out_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_mkpdu (oc-yang:counter64)

    YANG Description: MKPDU sent count
    """
    return self.__out_mkpdu
      
  def _set_out_mkpdu(self, v, load=False):
    """
    Setter method for out_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_mkpdu() directly.

    YANG Description: MKPDU sent count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_mkpdu(self):
    self.__out_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_sak_mkpdu(self):
    """
    Getter method for out_sak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_sak_mkpdu (oc-yang:counter64)

    YANG Description: MKPDU SAK sent count
    """
    return self.__out_sak_mkpdu
      
  def _set_out_sak_mkpdu(self, v, load=False):
    """
    Setter method for out_sak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_sak_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_sak_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_sak_mkpdu() directly.

    YANG Description: MKPDU SAK sent count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_sak_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_sak_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_sak_mkpdu(self):
    self.__out_sak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_cak_mkpdu(self):
    """
    Getter method for out_cak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_cak_mkpdu (oc-yang:counter64)

    YANG Description: Count of MKPDU connectivity association key (CAK) pdu's sent.
This counter is related to the group-cak feature in the
802.1X-2010 standard.
    """
    return self.__out_cak_mkpdu
      
  def _set_out_cak_mkpdu(self, v, load=False):
    """
    Setter method for out_cak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_cak_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_cak_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_cak_mkpdu() directly.

    YANG Description: Count of MKPDU connectivity association key (CAK) pdu's sent.
This counter is related to the group-cak feature in the
802.1X-2010 standard.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_cak_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_cak_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_cak_mkpdu(self):
    self.__out_cak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)

  in_mkpdu = __builtin__.property(_get_in_mkpdu)
  in_sak_mkpdu = __builtin__.property(_get_in_sak_mkpdu)
  in_cak_mkpdu = __builtin__.property(_get_in_cak_mkpdu)
  out_mkpdu = __builtin__.property(_get_out_mkpdu)
  out_sak_mkpdu = __builtin__.property(_get_out_sak_mkpdu)
  out_cak_mkpdu = __builtin__.property(_get_out_cak_mkpdu)


  _pyangbind_elements = OrderedDict([('in_mkpdu', in_mkpdu), ('in_sak_mkpdu', in_sak_mkpdu), ('in_cak_mkpdu', in_cak_mkpdu), ('out_mkpdu', out_mkpdu), ('out_sak_mkpdu', out_sak_mkpdu), ('out_cak_mkpdu', out_cak_mkpdu), ])


class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/mka/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MKA interface counters
  """
  __slots__ = ('_path_helper', '_extmethods', '__in_mkpdu','__in_sak_mkpdu','__in_cak_mkpdu','__out_mkpdu','__out_sak_mkpdu','__out_cak_mkpdu',)

  _yang_name = 'counters'
  _yang_namespace = 'http://openconfig.net/yang/macsec'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__in_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__in_sak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__in_cak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__out_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__out_sak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    self.__out_cak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)

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
      return ['macsec', 'interfaces', 'interface', 'mka', 'state', 'counters']

  def _get_in_mkpdu(self):
    """
    Getter method for in_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_mkpdu (oc-yang:counter64)

    YANG Description: Validated MKPDU received count
    """
    return self.__in_mkpdu
      
  def _set_in_mkpdu(self, v, load=False):
    """
    Setter method for in_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_mkpdu() directly.

    YANG Description: Validated MKPDU received count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_mkpdu(self):
    self.__in_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_sak_mkpdu(self):
    """
    Getter method for in_sak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_sak_mkpdu (oc-yang:counter64)

    YANG Description: Validated MKPDU received SAK count
    """
    return self.__in_sak_mkpdu
      
  def _set_in_sak_mkpdu(self, v, load=False):
    """
    Setter method for in_sak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_sak_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_sak_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_sak_mkpdu() directly.

    YANG Description: Validated MKPDU received SAK count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_sak_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_sak_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_sak_mkpdu(self):
    self.__in_sak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_cak_mkpdu(self):
    """
    Getter method for in_cak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_cak_mkpdu (oc-yang:counter64)

    YANG Description: Count of validated MKPDU  connectivity association key (CAK) pdus
received.  This counter is related to the group-cak feature in the
802.1X-2010 standard.
    """
    return self.__in_cak_mkpdu
      
  def _set_in_cak_mkpdu(self, v, load=False):
    """
    Setter method for in_cak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/in_cak_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_cak_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_cak_mkpdu() directly.

    YANG Description: Count of validated MKPDU  connectivity association key (CAK) pdus
received.  This counter is related to the group-cak feature in the
802.1X-2010 standard.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_cak_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_cak_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_cak_mkpdu(self):
    self.__in_cak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_mkpdu(self):
    """
    Getter method for out_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_mkpdu (oc-yang:counter64)

    YANG Description: MKPDU sent count
    """
    return self.__out_mkpdu
      
  def _set_out_mkpdu(self, v, load=False):
    """
    Setter method for out_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_mkpdu() directly.

    YANG Description: MKPDU sent count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_mkpdu(self):
    self.__out_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_sak_mkpdu(self):
    """
    Getter method for out_sak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_sak_mkpdu (oc-yang:counter64)

    YANG Description: MKPDU SAK sent count
    """
    return self.__out_sak_mkpdu
      
  def _set_out_sak_mkpdu(self, v, load=False):
    """
    Setter method for out_sak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_sak_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_sak_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_sak_mkpdu() directly.

    YANG Description: MKPDU SAK sent count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_sak_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_sak_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_sak_mkpdu(self):
    self.__out_sak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-sak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_cak_mkpdu(self):
    """
    Getter method for out_cak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_cak_mkpdu (oc-yang:counter64)

    YANG Description: Count of MKPDU connectivity association key (CAK) pdu's sent.
This counter is related to the group-cak feature in the
802.1X-2010 standard.
    """
    return self.__out_cak_mkpdu
      
  def _set_out_cak_mkpdu(self, v, load=False):
    """
    Setter method for out_cak_mkpdu, mapped from YANG variable /macsec/interfaces/interface/mka/state/counters/out_cak_mkpdu (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_cak_mkpdu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_cak_mkpdu() directly.

    YANG Description: Count of MKPDU connectivity association key (CAK) pdu's sent.
This counter is related to the group-cak feature in the
802.1X-2010 standard.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_cak_mkpdu must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_cak_mkpdu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_cak_mkpdu(self):
    self.__out_cak_mkpdu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-cak-mkpdu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='oc-yang:counter64', is_config=False)

  in_mkpdu = __builtin__.property(_get_in_mkpdu)
  in_sak_mkpdu = __builtin__.property(_get_in_sak_mkpdu)
  in_cak_mkpdu = __builtin__.property(_get_in_cak_mkpdu)
  out_mkpdu = __builtin__.property(_get_out_mkpdu)
  out_sak_mkpdu = __builtin__.property(_get_out_sak_mkpdu)
  out_cak_mkpdu = __builtin__.property(_get_out_cak_mkpdu)


  _pyangbind_elements = OrderedDict([('in_mkpdu', in_mkpdu), ('in_sak_mkpdu', in_sak_mkpdu), ('in_cak_mkpdu', in_cak_mkpdu), ('out_mkpdu', out_mkpdu), ('out_sak_mkpdu', out_sak_mkpdu), ('out_cak_mkpdu', out_cak_mkpdu), ])


