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
from . import lsp_next_hop
class lsp_next_hops(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/static-lsps/static-lsp/ingress/lsp-next-hops. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and state parameters relating to the
next-hops that are to be utilised for the MPLS static
route being specified
  """
  __slots__ = ('_path_helper', '_extmethods', '__lsp_next_hop',)

  _yang_name = 'lsp-next-hops'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsp_next_hop = YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'lsps', 'static-lsps', 'static-lsp', 'ingress', 'lsp-next-hops']

  def _get_lsp_next_hop(self):
    """
    Getter method for lsp_next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/lsp_next_hops/lsp_next_hop (list)

    YANG Description: A list of next-hops to be utilised for the MPLS
static route being specified.
    """
    return self.__lsp_next_hop
      
  def _set_lsp_next_hop(self, v, load=False):
    """
    Setter method for lsp_next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/lsp_next_hops/lsp_next_hop (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_next_hop() directly.

    YANG Description: A list of next-hops to be utilised for the MPLS
static route being specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_next_hop must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__lsp_next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_next_hop(self):
    self.__lsp_next_hop = YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  lsp_next_hop = __builtin__.property(_get_lsp_next_hop, _set_lsp_next_hop)


  _pyangbind_elements = OrderedDict([('lsp_next_hop', lsp_next_hop), ])


from . import lsp_next_hop
class lsp_next_hops(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/static-lsps/static-lsp/ingress/lsp-next-hops. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and state parameters relating to the
next-hops that are to be utilised for the MPLS static
route being specified
  """
  __slots__ = ('_path_helper', '_extmethods', '__lsp_next_hop',)

  _yang_name = 'lsp-next-hops'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsp_next_hop = YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'lsps', 'static-lsps', 'static-lsp', 'ingress', 'lsp-next-hops']

  def _get_lsp_next_hop(self):
    """
    Getter method for lsp_next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/lsp_next_hops/lsp_next_hop (list)

    YANG Description: A list of next-hops to be utilised for the MPLS
static route being specified.
    """
    return self.__lsp_next_hop
      
  def _set_lsp_next_hop(self, v, load=False):
    """
    Setter method for lsp_next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/lsp_next_hops/lsp_next_hop (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_next_hop() directly.

    YANG Description: A list of next-hops to be utilised for the MPLS
static route being specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_next_hop must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__lsp_next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_next_hop(self):
    self.__lsp_next_hop = YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  lsp_next_hop = __builtin__.property(_get_lsp_next_hop, _set_lsp_next_hop)


  _pyangbind_elements = OrderedDict([('lsp_next_hop', lsp_next_hop), ])


from . import lsp_next_hop
class lsp_next_hops(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/static-lsps/static-lsp/ingress/lsp-next-hops. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and state parameters relating to the
next-hops that are to be utilised for the MPLS static
route being specified
  """
  __slots__ = ('_path_helper', '_extmethods', '__lsp_next_hop',)

  _yang_name = 'lsp-next-hops'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsp_next_hop = YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'lsps', 'static-lsps', 'static-lsp', 'ingress', 'lsp-next-hops']

  def _get_lsp_next_hop(self):
    """
    Getter method for lsp_next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/lsp_next_hops/lsp_next_hop (list)

    YANG Description: A list of next-hops to be utilised for the MPLS
static route being specified.
    """
    return self.__lsp_next_hop
      
  def _set_lsp_next_hop(self, v, load=False):
    """
    Setter method for lsp_next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/lsp_next_hops/lsp_next_hop (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_next_hop() directly.

    YANG Description: A list of next-hops to be utilised for the MPLS
static route being specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_next_hop must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__lsp_next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_next_hop(self):
    self.__lsp_next_hop = YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  lsp_next_hop = __builtin__.property(_get_lsp_next_hop, _set_lsp_next_hop)


  _pyangbind_elements = OrderedDict([('lsp_next_hop', lsp_next_hop), ])


from . import lsp_next_hop
class lsp_next_hops(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/static-lsps/static-lsp/ingress/lsp-next-hops. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and state parameters relating to the
next-hops that are to be utilised for the MPLS static
route being specified
  """
  __slots__ = ('_path_helper', '_extmethods', '__lsp_next_hop',)

  _yang_name = 'lsp-next-hops'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsp_next_hop = YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'lsps', 'static-lsps', 'static-lsp', 'ingress', 'lsp-next-hops']

  def _get_lsp_next_hop(self):
    """
    Getter method for lsp_next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/lsp_next_hops/lsp_next_hop (list)

    YANG Description: A list of next-hops to be utilised for the MPLS
static route being specified.
    """
    return self.__lsp_next_hop
      
  def _set_lsp_next_hop(self, v, load=False):
    """
    Setter method for lsp_next_hop, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress/lsp_next_hops/lsp_next_hop (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_next_hop() directly.

    YANG Description: A list of next-hops to be utilised for the MPLS
static route being specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_next_hop must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__lsp_next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_next_hop(self):
    self.__lsp_next_hop = YANGDynClass(base=YANGListType("index",lsp_next_hop.lsp_next_hop, yang_name="lsp-next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="lsp-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  lsp_next_hop = __builtin__.property(_get_lsp_next_hop, _set_lsp_next_hop)


  _pyangbind_elements = OrderedDict([('lsp_next_hop', lsp_next_hop), ])


