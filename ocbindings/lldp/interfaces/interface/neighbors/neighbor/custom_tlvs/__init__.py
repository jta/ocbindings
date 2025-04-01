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
from . import tlv
class custom_tlvs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-lldp - based on the path /lldp/interfaces/interface/neighbors/neighbor/custom-tlvs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of custom TLVs from a
neighbor
  """
  __slots__ = ('_path_helper', '_extmethods', '__tlv',)

  _yang_name = 'custom-tlvs'
  _yang_namespace = 'http://openconfig.net/yang/lldp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tlv = YANGDynClass(base=YANGListType("type oui oui_subtype",tlv.tlv, yang_name="tlv", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type oui oui-subtype', extensions=None), is_container='list', yang_name="tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='list', is_config=False)

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
      return ['lldp', 'interfaces', 'interface', 'neighbors', 'neighbor', 'custom-tlvs']

  def _get_tlv(self):
    """
    Getter method for tlv, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv (list)

    YANG Description: List of custom LLDP TLVs from a neighbor
    """
    return self.__tlv
      
  def _set_tlv(self, v, load=False):
    """
    Setter method for tlv, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tlv() directly.

    YANG Description: List of custom LLDP TLVs from a neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type oui oui_subtype",tlv.tlv, yang_name="tlv", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type oui oui-subtype', extensions=None), is_container='list', yang_name="tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tlv must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type oui oui_subtype",tlv.tlv, yang_name="tlv", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type oui oui-subtype', extensions=None), is_container='list', yang_name="tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='list', is_config=False)""",
        })

    self.__tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tlv(self):
    self.__tlv = YANGDynClass(base=YANGListType("type oui oui_subtype",tlv.tlv, yang_name="tlv", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type oui oui-subtype', extensions=None), is_container='list', yang_name="tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='list', is_config=False)

  tlv = __builtin__.property(_get_tlv)


  _pyangbind_elements = OrderedDict([('tlv', tlv), ])


from . import tlv
class custom_tlvs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-lldp - based on the path /lldp/interfaces/interface/neighbors/neighbor/custom-tlvs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of custom TLVs from a
neighbor
  """
  __slots__ = ('_path_helper', '_extmethods', '__tlv',)

  _yang_name = 'custom-tlvs'
  _yang_namespace = 'http://openconfig.net/yang/lldp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tlv = YANGDynClass(base=YANGListType("type oui oui_subtype",tlv.tlv, yang_name="tlv", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type oui oui-subtype', extensions=None), is_container='list', yang_name="tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='list', is_config=False)

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
      return ['lldp', 'interfaces', 'interface', 'neighbors', 'neighbor', 'custom-tlvs']

  def _get_tlv(self):
    """
    Getter method for tlv, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv (list)

    YANG Description: List of custom LLDP TLVs from a neighbor
    """
    return self.__tlv
      
  def _set_tlv(self, v, load=False):
    """
    Setter method for tlv, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/custom_tlvs/tlv (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tlv() directly.

    YANG Description: List of custom LLDP TLVs from a neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type oui oui_subtype",tlv.tlv, yang_name="tlv", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type oui oui-subtype', extensions=None), is_container='list', yang_name="tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tlv must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type oui oui_subtype",tlv.tlv, yang_name="tlv", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type oui oui-subtype', extensions=None), is_container='list', yang_name="tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='list', is_config=False)""",
        })

    self.__tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tlv(self):
    self.__tlv = YANGDynClass(base=YANGListType("type oui oui_subtype",tlv.tlv, yang_name="tlv", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type oui oui-subtype', extensions=None), is_container='list', yang_name="tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='list', is_config=False)

  tlv = __builtin__.property(_get_tlv)


  _pyangbind_elements = OrderedDict([('tlv', tlv), ])


