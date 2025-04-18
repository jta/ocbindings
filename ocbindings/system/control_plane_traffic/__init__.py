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
from . import ingress
from . import egress
class control_plane_traffic(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/control-plane-traffic. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Policies and configuration relating to the traffic destined towards
 the system control-plane.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress','__egress',)

  _yang_name = 'control-plane-traffic'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress = YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    self.__egress = YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)

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
      return ['system', 'control-plane-traffic']

  def _get_ingress(self):
    """
    Getter method for ingress, mapped from YANG variable /system/control_plane_traffic/ingress (container)

    YANG Description: Control-plane traffic parameters relating to ingress traffic.
This refers to traffic that is being received by the system's
control plane from external-to-the-controlplane sources.
    """
    return self.__ingress
      
  def _set_ingress(self, v, load=False):
    """
    Setter method for ingress, mapped from YANG variable /system/control_plane_traffic/ingress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress() directly.

    YANG Description: Control-plane traffic parameters relating to ingress traffic.
This refers to traffic that is being received by the system's
control plane from external-to-the-controlplane sources.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)""",
        })

    self.__ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress(self):
    self.__ingress = YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)


  def _get_egress(self):
    """
    Getter method for egress, mapped from YANG variable /system/control_plane_traffic/egress (container)

    YANG Description: Control-plane traffic parameters relating to egress traffic.
This refers to traffic that is sent by the system's control
plane to external-to-the-controlplane destinations.
    """
    return self.__egress
      
  def _set_egress(self, v, load=False):
    """
    Setter method for egress, mapped from YANG variable /system/control_plane_traffic/egress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress() directly.

    YANG Description: Control-plane traffic parameters relating to egress traffic.
This refers to traffic that is sent by the system's control
plane to external-to-the-controlplane destinations.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)""",
        })

    self.__egress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress(self):
    self.__egress = YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)

  ingress = __builtin__.property(_get_ingress, _set_ingress)
  egress = __builtin__.property(_get_egress, _set_egress)


  _pyangbind_elements = OrderedDict([('ingress', ingress), ('egress', egress), ])


from . import ingress
from . import egress
class control_plane_traffic(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/control-plane-traffic. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Policies and configuration relating to the traffic destined towards
 the system control-plane.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress','__egress',)

  _yang_name = 'control-plane-traffic'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress = YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    self.__egress = YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)

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
      return ['system', 'control-plane-traffic']

  def _get_ingress(self):
    """
    Getter method for ingress, mapped from YANG variable /system/control_plane_traffic/ingress (container)

    YANG Description: Control-plane traffic parameters relating to ingress traffic.
This refers to traffic that is being received by the system's
control plane from external-to-the-controlplane sources.
    """
    return self.__ingress
      
  def _set_ingress(self, v, load=False):
    """
    Setter method for ingress, mapped from YANG variable /system/control_plane_traffic/ingress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress() directly.

    YANG Description: Control-plane traffic parameters relating to ingress traffic.
This refers to traffic that is being received by the system's
control plane from external-to-the-controlplane sources.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)""",
        })

    self.__ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress(self):
    self.__ingress = YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)


  def _get_egress(self):
    """
    Getter method for egress, mapped from YANG variable /system/control_plane_traffic/egress (container)

    YANG Description: Control-plane traffic parameters relating to egress traffic.
This refers to traffic that is sent by the system's control
plane to external-to-the-controlplane destinations.
    """
    return self.__egress
      
  def _set_egress(self, v, load=False):
    """
    Setter method for egress, mapped from YANG variable /system/control_plane_traffic/egress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress() directly.

    YANG Description: Control-plane traffic parameters relating to egress traffic.
This refers to traffic that is sent by the system's control
plane to external-to-the-controlplane destinations.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)""",
        })

    self.__egress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress(self):
    self.__egress = YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)

  ingress = __builtin__.property(_get_ingress, _set_ingress)
  egress = __builtin__.property(_get_egress, _set_egress)


  _pyangbind_elements = OrderedDict([('ingress', ingress), ('egress', egress), ])


