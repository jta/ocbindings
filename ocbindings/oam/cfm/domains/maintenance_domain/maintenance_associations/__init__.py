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
from . import maintenance_association
class maintenance_associations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-oam - based on the path /oam/cfm/domains/maintenance-domain/maintenance-associations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Collection of maintenance associations within a
maintenance domain.Provides configuration and operational data
for the Maintenance Associations. A Maintenance Association is a set
of MEPs, each configured with the same MAID and MD level,
established to verify the integrity of a single service
instance. A Maintenance Association can be thought of as a
full mesh of Maintenance Entities among a set of MEPs so
configured.
  """
  __slots__ = ('_path_helper', '_extmethods', '__maintenance_association',)

  _yang_name = 'maintenance-associations'
  _yang_namespace = 'http://openconfig.net/yang/oam'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__maintenance_association = YANGDynClass(base=YANGListType("ma_id",maintenance_association.maintenance_association, yang_name="maintenance-association", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-id', extensions=None), is_container='list', yang_name="maintenance-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='list', is_config=True)

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
      return ['oam', 'cfm', 'domains', 'maintenance-domain', 'maintenance-associations']

  def _get_maintenance_association(self):
    """
    Getter method for maintenance_association, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association (list)

    YANG Description: Collection of maintenance associations within a maintenance domain.
    """
    return self.__maintenance_association
      
  def _set_maintenance_association(self, v, load=False):
    """
    Setter method for maintenance_association, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maintenance_association is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maintenance_association() directly.

    YANG Description: Collection of maintenance associations within a maintenance domain.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ma_id",maintenance_association.maintenance_association, yang_name="maintenance-association", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-id', extensions=None), is_container='list', yang_name="maintenance-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maintenance_association must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ma_id",maintenance_association.maintenance_association, yang_name="maintenance-association", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-id', extensions=None), is_container='list', yang_name="maintenance-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='list', is_config=True)""",
        })

    self.__maintenance_association = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maintenance_association(self):
    self.__maintenance_association = YANGDynClass(base=YANGListType("ma_id",maintenance_association.maintenance_association, yang_name="maintenance-association", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-id', extensions=None), is_container='list', yang_name="maintenance-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='list', is_config=True)

  maintenance_association = __builtin__.property(_get_maintenance_association, _set_maintenance_association)


  _pyangbind_elements = OrderedDict([('maintenance_association', maintenance_association), ])


from . import maintenance_association
class maintenance_associations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-oam - based on the path /oam/cfm/domains/maintenance-domain/maintenance-associations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Collection of maintenance associations within a
maintenance domain.Provides configuration and operational data
for the Maintenance Associations. A Maintenance Association is a set
of MEPs, each configured with the same MAID and MD level,
established to verify the integrity of a single service
instance. A Maintenance Association can be thought of as a
full mesh of Maintenance Entities among a set of MEPs so
configured.
  """
  __slots__ = ('_path_helper', '_extmethods', '__maintenance_association',)

  _yang_name = 'maintenance-associations'
  _yang_namespace = 'http://openconfig.net/yang/oam'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__maintenance_association = YANGDynClass(base=YANGListType("ma_id",maintenance_association.maintenance_association, yang_name="maintenance-association", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-id', extensions=None), is_container='list', yang_name="maintenance-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='list', is_config=True)

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
      return ['oam', 'cfm', 'domains', 'maintenance-domain', 'maintenance-associations']

  def _get_maintenance_association(self):
    """
    Getter method for maintenance_association, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association (list)

    YANG Description: Collection of maintenance associations within a maintenance domain.
    """
    return self.__maintenance_association
      
  def _set_maintenance_association(self, v, load=False):
    """
    Setter method for maintenance_association, mapped from YANG variable /oam/cfm/domains/maintenance_domain/maintenance_associations/maintenance_association (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maintenance_association is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maintenance_association() directly.

    YANG Description: Collection of maintenance associations within a maintenance domain.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ma_id",maintenance_association.maintenance_association, yang_name="maintenance-association", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-id', extensions=None), is_container='list', yang_name="maintenance-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maintenance_association must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ma_id",maintenance_association.maintenance_association, yang_name="maintenance-association", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-id', extensions=None), is_container='list', yang_name="maintenance-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='list', is_config=True)""",
        })

    self.__maintenance_association = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maintenance_association(self):
    self.__maintenance_association = YANGDynClass(base=YANGListType("ma_id",maintenance_association.maintenance_association, yang_name="maintenance-association", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-id', extensions=None), is_container='list', yang_name="maintenance-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oam/cfm', defining_module='openconfig-oam-cfm', yang_type='list', is_config=True)

  maintenance_association = __builtin__.property(_get_maintenance_association, _set_maintenance_association)


  _pyangbind_elements = OrderedDict([('maintenance_association', maintenance_association), ])


