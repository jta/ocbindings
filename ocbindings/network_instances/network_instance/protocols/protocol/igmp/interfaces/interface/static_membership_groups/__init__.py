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
from . import static_groups
class static_membership_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/igmp/interfaces/interface/static-membership-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of IGMP Membership information.
  """
  __slots__ = ('_path_helper', '_extmethods', '__static_groups',)

  _yang_name = 'static-membership-groups'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__static_groups = YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'interfaces', 'interface', 'static-membership-groups']

  def _get_static_groups(self):
    """
    Getter method for static_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/static_membership_groups/static_groups (list)

    YANG Description: Multicast group membership.
    """
    return self.__static_groups
      
  def _set_static_groups(self, v, load=False):
    """
    Setter method for static_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/static_membership_groups/static_groups (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_groups() directly.

    YANG Description: Multicast group membership.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_groups must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__static_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_groups(self):
    self.__static_groups = YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  static_groups = __builtin__.property(_get_static_groups, _set_static_groups)


  _pyangbind_elements = OrderedDict([('static_groups', static_groups), ])


from . import static_groups
class static_membership_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/igmp/interfaces/interface/static-membership-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of IGMP Membership information.
  """
  __slots__ = ('_path_helper', '_extmethods', '__static_groups',)

  _yang_name = 'static-membership-groups'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__static_groups = YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'interfaces', 'interface', 'static-membership-groups']

  def _get_static_groups(self):
    """
    Getter method for static_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/static_membership_groups/static_groups (list)

    YANG Description: Multicast group membership.
    """
    return self.__static_groups
      
  def _set_static_groups(self, v, load=False):
    """
    Setter method for static_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/static_membership_groups/static_groups (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_groups() directly.

    YANG Description: Multicast group membership.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_groups must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__static_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_groups(self):
    self.__static_groups = YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  static_groups = __builtin__.property(_get_static_groups, _set_static_groups)


  _pyangbind_elements = OrderedDict([('static_groups', static_groups), ])


from . import static_groups
class static_membership_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/igmp/interfaces/interface/static-membership-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of IGMP Membership information.
  """
  __slots__ = ('_path_helper', '_extmethods', '__static_groups',)

  _yang_name = 'static-membership-groups'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__static_groups = YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'interfaces', 'interface', 'static-membership-groups']

  def _get_static_groups(self):
    """
    Getter method for static_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/static_membership_groups/static_groups (list)

    YANG Description: Multicast group membership.
    """
    return self.__static_groups
      
  def _set_static_groups(self, v, load=False):
    """
    Setter method for static_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/static_membership_groups/static_groups (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_groups() directly.

    YANG Description: Multicast group membership.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_groups must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__static_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_groups(self):
    self.__static_groups = YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  static_groups = __builtin__.property(_get_static_groups, _set_static_groups)


  _pyangbind_elements = OrderedDict([('static_groups', static_groups), ])


from . import static_groups
class static_membership_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/igmp/interfaces/interface/static-membership-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of IGMP Membership information.
  """
  __slots__ = ('_path_helper', '_extmethods', '__static_groups',)

  _yang_name = 'static-membership-groups'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__static_groups = YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'interfaces', 'interface', 'static-membership-groups']

  def _get_static_groups(self):
    """
    Getter method for static_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/static_membership_groups/static_groups (list)

    YANG Description: Multicast group membership.
    """
    return self.__static_groups
      
  def _set_static_groups(self, v, load=False):
    """
    Setter method for static_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/static_membership_groups/static_groups (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_groups() directly.

    YANG Description: Multicast group membership.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_groups must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__static_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_groups(self):
    self.__static_groups = YANGDynClass(base=YANGListType("static_group",static_groups.static_groups, yang_name="static-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-group', extensions=None), is_container='list', yang_name="static-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  static_groups = __builtin__.property(_get_static_groups, _set_static_groups)


  _pyangbind_elements = OrderedDict([('static_groups', static_groups), ])


