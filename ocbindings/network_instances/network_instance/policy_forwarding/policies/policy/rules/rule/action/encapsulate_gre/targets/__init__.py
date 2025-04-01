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
from . import target
class targets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the list of GRE tunnel targets that
should be encapsulated towards.
  """
  __slots__ = ('_path_helper', '_extmethods', '__target',)

  _yang_name = 'targets'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target = YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'rules', 'rule', 'action', 'encapsulate-gre', 'targets']

  def _get_target(self):
    """
    Getter method for target, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/encapsulate_gre/targets/target (list)

    YANG Description: Each target specified within this list should be treated as a
endpoint to which packets should be GRE encapsulated. Where the
set of destinations described within a single entry expands to
more than one destination IP address, packets should be load
shared across the destination using the local system's ECMP hashing
mechanisms.
    """
    return self.__target
      
  def _set_target(self, v, load=False):
    """
    Setter method for target, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/encapsulate_gre/targets/target (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target() directly.

    YANG Description: Each target specified within this list should be treated as a
endpoint to which packets should be GRE encapsulated. Where the
set of destinations described within a single entry expands to
more than one destination IP address, packets should be load
shared across the destination using the local system's ECMP hashing
mechanisms.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__target = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target(self):
    self.__target = YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  target = __builtin__.property(_get_target, _set_target)


  _pyangbind_elements = OrderedDict([('target', target), ])


from . import target
class targets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the list of GRE tunnel targets that
should be encapsulated towards.
  """
  __slots__ = ('_path_helper', '_extmethods', '__target',)

  _yang_name = 'targets'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target = YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'rules', 'rule', 'action', 'encapsulate-gre', 'targets']

  def _get_target(self):
    """
    Getter method for target, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/encapsulate_gre/targets/target (list)

    YANG Description: Each target specified within this list should be treated as a
endpoint to which packets should be GRE encapsulated. Where the
set of destinations described within a single entry expands to
more than one destination IP address, packets should be load
shared across the destination using the local system's ECMP hashing
mechanisms.
    """
    return self.__target
      
  def _set_target(self, v, load=False):
    """
    Setter method for target, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/encapsulate_gre/targets/target (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target() directly.

    YANG Description: Each target specified within this list should be treated as a
endpoint to which packets should be GRE encapsulated. Where the
set of destinations described within a single entry expands to
more than one destination IP address, packets should be load
shared across the destination using the local system's ECMP hashing
mechanisms.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__target = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target(self):
    self.__target = YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  target = __builtin__.property(_get_target, _set_target)


  _pyangbind_elements = OrderedDict([('target', target), ])


from . import target
class targets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the list of GRE tunnel targets that
should be encapsulated towards.
  """
  __slots__ = ('_path_helper', '_extmethods', '__target',)

  _yang_name = 'targets'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target = YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'rules', 'rule', 'action', 'encapsulate-gre', 'targets']

  def _get_target(self):
    """
    Getter method for target, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/encapsulate_gre/targets/target (list)

    YANG Description: Each target specified within this list should be treated as a
endpoint to which packets should be GRE encapsulated. Where the
set of destinations described within a single entry expands to
more than one destination IP address, packets should be load
shared across the destination using the local system's ECMP hashing
mechanisms.
    """
    return self.__target
      
  def _set_target(self, v, load=False):
    """
    Setter method for target, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/encapsulate_gre/targets/target (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target() directly.

    YANG Description: Each target specified within this list should be treated as a
endpoint to which packets should be GRE encapsulated. Where the
set of destinations described within a single entry expands to
more than one destination IP address, packets should be load
shared across the destination using the local system's ECMP hashing
mechanisms.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__target = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target(self):
    self.__target = YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  target = __builtin__.property(_get_target, _set_target)


  _pyangbind_elements = OrderedDict([('target', target), ])


from . import target
class targets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the list of GRE tunnel targets that
should be encapsulated towards.
  """
  __slots__ = ('_path_helper', '_extmethods', '__target',)

  _yang_name = 'targets'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target = YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'rules', 'rule', 'action', 'encapsulate-gre', 'targets']

  def _get_target(self):
    """
    Getter method for target, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/encapsulate_gre/targets/target (list)

    YANG Description: Each target specified within this list should be treated as a
endpoint to which packets should be GRE encapsulated. Where the
set of destinations described within a single entry expands to
more than one destination IP address, packets should be load
shared across the destination using the local system's ECMP hashing
mechanisms.
    """
    return self.__target
      
  def _set_target(self, v, load=False):
    """
    Setter method for target, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/action/encapsulate_gre/targets/target (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target() directly.

    YANG Description: Each target specified within this list should be treated as a
endpoint to which packets should be GRE encapsulated. Where the
set of destinations described within a single entry expands to
more than one destination IP address, packets should be load
shared across the destination using the local system's ECMP hashing
mechanisms.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__target = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target(self):
    self.__target = YANGDynClass(base=YANGListType("id",target.target, yang_name="target", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  target = __builtin__.property(_get_target, _set_target)


  _pyangbind_elements = OrderedDict([('target', target), ])


