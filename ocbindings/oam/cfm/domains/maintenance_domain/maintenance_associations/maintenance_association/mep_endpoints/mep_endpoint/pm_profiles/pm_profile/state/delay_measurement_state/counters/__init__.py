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
  from YANG module openconfig-oam - based on the path /oam/cfm/domains/maintenance-domain/maintenance-associations/maintenance-association/mep-endpoints/mep-endpoint/pm-profiles/pm-profile/state/delay-measurement-state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A collection of delay-measurement-related statistics objects.
  """
  __slots__ = ('_path_helper', '_extmethods', '__dmm_sent','__dmm_received','__dmr_sent','__dmr_received',)

  _yang_name = 'counters'
  _yang_namespace = 'http://openconfig.net/yang/oam'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__dmm_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    self.__dmm_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    self.__dmr_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    self.__dmr_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)

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
      return ['oam', 'cfm', 'domains', 'maintenance-domain', 'maintenance-associations', 'maintenance-association', 'mep-endpoints', 'mep-endpoint', 'pm-profiles', 'pm-profile', 'state', 'delay-measurement-state', 'counters']

  def _get_dmm_sent(self):
    """
    Getter method for dmm_sent, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmm_sent (oc-yang:counter64)

    YANG Description: slm Probes sent.
    """
    return self.__dmm_sent
      
  def _set_dmm_sent(self, v, load=False):
    """
    Setter method for dmm_sent, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmm_sent (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmm_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmm_sent() directly.

    YANG Description: slm Probes sent.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmm_sent must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__dmm_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmm_sent(self):
    self.__dmm_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)


  def _get_dmm_received(self):
    """
    Getter method for dmm_received, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmm_received (oc-yang:counter64)

    YANG Description: slm Probes sent.
    """
    return self.__dmm_received
      
  def _set_dmm_received(self, v, load=False):
    """
    Setter method for dmm_received, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmm_received (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmm_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmm_received() directly.

    YANG Description: slm Probes sent.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmm_received must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__dmm_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmm_received(self):
    self.__dmm_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)


  def _get_dmr_sent(self):
    """
    Getter method for dmr_sent, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmr_sent (oc-yang:counter64)

    YANG Description: slm Probes sent.
    """
    return self.__dmr_sent
      
  def _set_dmr_sent(self, v, load=False):
    """
    Setter method for dmr_sent, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmr_sent (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmr_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmr_sent() directly.

    YANG Description: slm Probes sent.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmr_sent must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__dmr_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmr_sent(self):
    self.__dmr_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)


  def _get_dmr_received(self):
    """
    Getter method for dmr_received, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmr_received (oc-yang:counter64)

    YANG Description: slm Probes sent.
    """
    return self.__dmr_received
      
  def _set_dmr_received(self, v, load=False):
    """
    Setter method for dmr_received, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmr_received (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmr_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmr_received() directly.

    YANG Description: slm Probes sent.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmr_received must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__dmr_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmr_received(self):
    self.__dmr_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)

  dmm_sent = __builtin__.property(_get_dmm_sent)
  dmm_received = __builtin__.property(_get_dmm_received)
  dmr_sent = __builtin__.property(_get_dmr_sent)
  dmr_received = __builtin__.property(_get_dmr_received)


  _pyangbind_elements = OrderedDict([('dmm_sent', dmm_sent), ('dmm_received', dmm_received), ('dmr_sent', dmr_sent), ('dmr_received', dmr_received), ])


class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-oam - based on the path /oam/cfm/domains/maintenance-domain/maintenance-associations/maintenance-association/mep-endpoints/mep-endpoint/pm-profiles/pm-profile/state/delay-measurement-state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A collection of delay-measurement-related statistics objects.
  """
  __slots__ = ('_path_helper', '_extmethods', '__dmm_sent','__dmm_received','__dmr_sent','__dmr_received',)

  _yang_name = 'counters'
  _yang_namespace = 'http://openconfig.net/yang/oam'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__dmm_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    self.__dmm_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    self.__dmr_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    self.__dmr_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)

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
      return ['oam', 'cfm', 'domains', 'maintenance-domain', 'maintenance-associations', 'maintenance-association', 'mep-endpoints', 'mep-endpoint', 'pm-profiles', 'pm-profile', 'state', 'delay-measurement-state', 'counters']

  def _get_dmm_sent(self):
    """
    Getter method for dmm_sent, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmm_sent (oc-yang:counter64)

    YANG Description: slm Probes sent.
    """
    return self.__dmm_sent
      
  def _set_dmm_sent(self, v, load=False):
    """
    Setter method for dmm_sent, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmm_sent (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmm_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmm_sent() directly.

    YANG Description: slm Probes sent.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmm_sent must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__dmm_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmm_sent(self):
    self.__dmm_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)


  def _get_dmm_received(self):
    """
    Getter method for dmm_received, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmm_received (oc-yang:counter64)

    YANG Description: slm Probes sent.
    """
    return self.__dmm_received
      
  def _set_dmm_received(self, v, load=False):
    """
    Setter method for dmm_received, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmm_received (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmm_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmm_received() directly.

    YANG Description: slm Probes sent.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmm_received must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__dmm_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmm_received(self):
    self.__dmm_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmm-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)


  def _get_dmr_sent(self):
    """
    Getter method for dmr_sent, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmr_sent (oc-yang:counter64)

    YANG Description: slm Probes sent.
    """
    return self.__dmr_sent
      
  def _set_dmr_sent(self, v, load=False):
    """
    Setter method for dmr_sent, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmr_sent (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmr_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmr_sent() directly.

    YANG Description: slm Probes sent.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmr_sent must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__dmr_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmr_sent(self):
    self.__dmr_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)


  def _get_dmr_received(self):
    """
    Getter method for dmr_received, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmr_received (oc-yang:counter64)

    YANG Description: slm Probes sent.
    """
    return self.__dmr_received
      
  def _set_dmr_received(self, v, load=False):
    """
    Setter method for dmr_received, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association/mep_endpoints/mep_endpoint/pm_profiles/pm_profile/state/delay_measurement_state/counters/dmr_received (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmr_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmr_received() directly.

    YANG Description: slm Probes sent.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmr_received must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__dmr_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmr_received(self):
    self.__dmr_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="dmr-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='oc-yang:counter64', is_config=False)

  dmm_sent = __builtin__.property(_get_dmm_sent)
  dmm_received = __builtin__.property(_get_dmm_received)
  dmr_sent = __builtin__.property(_get_dmr_sent)
  dmr_received = __builtin__.property(_get_dmr_received)


  _pyangbind_elements = OrderedDict([('dmm_sent', dmm_sent), ('dmm_received', dmm_received), ('dmr_sent', dmr_sent), ('dmr_received', dmr_received), ])


