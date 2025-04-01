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
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-oam - based on the path /oam/cfm/domains/maintenance-domain/maintenance-associations/maintenance-association/mep-endpoints/mep-endpoint/link-loss-forwarding/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: link loss forwarding state for a mep.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable','__damping_timer','__action',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/oam'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='boolean', is_config=False)
    self.__damping_timer = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="damping-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='uint64', is_config=False)
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SHUTDOWN': {}, 'ALARM': {}, 'DISABLE_ROUTING': {}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='enumeration', is_config=False)

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
      return ['oam', 'cfm', 'domains', 'maintenance-domain', 'maintenance-associations', 'maintenance-association', 'mep-endpoints', 'mep-endpoint', 'link-loss-forwarding', 'state']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/enable (boolean)

    YANG Description: Enable propagation of the remote
attachment-circuit link state to the
local attachment-circuit link state
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enable propagation of the remote
attachment-circuit link state to the
local attachment-circuit link state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='boolean', is_config=False)


  def _get_damping_timer(self):
    """
    Getter method for damping_timer, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/damping_timer (uint64)

    YANG Description: The damping timer is the amount of time that the local
attachment-circuit link state will be held in the down state
after the remote attachment-circuit link state has been
detected to be up. The damping timer is used to prevent
flapping of the local attachment-circuit link state.
    """
    return self.__damping_timer
      
  def _set_damping_timer(self, v, load=False):
    """
    Setter method for damping_timer, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/damping_timer (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_damping_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_damping_timer() directly.

    YANG Description: The damping timer is the amount of time that the local
attachment-circuit link state will be held in the down state
after the remote attachment-circuit link state has been
detected to be up. The damping timer is used to prevent
flapping of the local attachment-circuit link state.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="damping-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """damping_timer must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="damping-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='uint64', is_config=False)""",
        })

    self.__damping_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_damping_timer(self):
    self.__damping_timer = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="damping-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='uint64', is_config=False)


  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/action (enumeration)

    YANG Description: Action to take on link loss.
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.

    YANG Description: Action to take on link loss.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SHUTDOWN': {}, 'ALARM': {}, 'DISABLE_ROUTING': {}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with enumeration""",
          'defined-type': "openconfig-oam-cfm:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SHUTDOWN': {}, 'ALARM': {}, 'DISABLE_ROUTING': {}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='enumeration', is_config=False)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SHUTDOWN': {}, 'ALARM': {}, 'DISABLE_ROUTING': {}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='enumeration', is_config=False)

  enable = __builtin__.property(_get_enable)
  damping_timer = __builtin__.property(_get_damping_timer)
  action = __builtin__.property(_get_action)


  _pyangbind_elements = OrderedDict([('enable', enable), ('damping_timer', damping_timer), ('action', action), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-oam - based on the path /oam/cfm/domains/maintenance-domain/maintenance-associations/maintenance-association/mep-endpoints/mep-endpoint/link-loss-forwarding/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: link loss forwarding state for a mep.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable','__damping_timer','__action',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/oam'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='boolean', is_config=False)
    self.__damping_timer = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="damping-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='uint64', is_config=False)
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SHUTDOWN': {}, 'ALARM': {}, 'DISABLE_ROUTING': {}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='enumeration', is_config=False)

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
      return ['oam', 'cfm', 'domains', 'maintenance-domain', 'maintenance-associations', 'maintenance-association', 'mep-endpoints', 'mep-endpoint', 'link-loss-forwarding', 'state']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/enable (boolean)

    YANG Description: Enable propagation of the remote
attachment-circuit link state to the
local attachment-circuit link state
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enable propagation of the remote
attachment-circuit link state to the
local attachment-circuit link state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='boolean', is_config=False)


  def _get_damping_timer(self):
    """
    Getter method for damping_timer, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/damping_timer (uint64)

    YANG Description: The damping timer is the amount of time that the local
attachment-circuit link state will be held in the down state
after the remote attachment-circuit link state has been
detected to be up. The damping timer is used to prevent
flapping of the local attachment-circuit link state.
    """
    return self.__damping_timer
      
  def _set_damping_timer(self, v, load=False):
    """
    Setter method for damping_timer, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/damping_timer (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_damping_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_damping_timer() directly.

    YANG Description: The damping timer is the amount of time that the local
attachment-circuit link state will be held in the down state
after the remote attachment-circuit link state has been
detected to be up. The damping timer is used to prevent
flapping of the local attachment-circuit link state.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="damping-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """damping_timer must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="damping-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='uint64', is_config=False)""",
        })

    self.__damping_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_damping_timer(self):
    self.__damping_timer = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="damping-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='uint64', is_config=False)


  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/action (enumeration)

    YANG Description: Action to take on link loss.
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/link_loss_forwarding/state/action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.

    YANG Description: Action to take on link loss.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SHUTDOWN': {}, 'ALARM': {}, 'DISABLE_ROUTING': {}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with enumeration""",
          'defined-type': "openconfig-oam-cfm:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SHUTDOWN': {}, 'ALARM': {}, 'DISABLE_ROUTING': {}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='enumeration', is_config=False)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=str,                                     restriction_type="dict_key",                                     restriction_arg={'SHUTDOWN': {}, 'ALARM': {}, 'DISABLE_ROUTING': {}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='enumeration', is_config=False)

  enable = __builtin__.property(_get_enable)
  damping_timer = __builtin__.property(_get_damping_timer)
  action = __builtin__.property(_get_action)


  _pyangbind_elements = OrderedDict([('enable', enable), ('damping_timer', damping_timer), ('action', action), ])


