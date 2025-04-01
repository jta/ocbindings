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
from . import statement
class statements(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for policy statements
  """
  __slots__ = ('_path_helper', '_extmethods', '__statement',)

  _yang_name = 'statements'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__statement = YANGDynClass(base=YANGListType("name",statement.statement, yang_name="statement", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="statement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='list', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements']

  def _get_statement(self):
    """
    Getter method for statement, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement (list)

    YANG Description: Policy statements group conditions and actions
within a policy definition.  They are evaluated in
the order specified (see the description of policy
evaluation at the top of this module.
    """
    return self.__statement
      
  def _set_statement(self, v, load=False):
    """
    Setter method for statement, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_statement is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_statement() directly.

    YANG Description: Policy statements group conditions and actions
within a policy definition.  They are evaluated in
the order specified (see the description of policy
evaluation at the top of this module.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",statement.statement, yang_name="statement", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="statement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """statement must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",statement.statement, yang_name="statement", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="statement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='list', is_config=True)""",
        })

    self.__statement = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_statement(self):
    self.__statement = YANGDynClass(base=YANGListType("name",statement.statement, yang_name="statement", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="statement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='list', is_config=True)

  statement = __builtin__.property(_get_statement, _set_statement)


  _pyangbind_elements = OrderedDict([('statement', statement), ])


from . import statement
class statements(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for policy statements
  """
  __slots__ = ('_path_helper', '_extmethods', '__statement',)

  _yang_name = 'statements'
  _yang_namespace = 'http://openconfig.net/yang/routing-policy'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__statement = YANGDynClass(base=YANGListType("name",statement.statement, yang_name="statement", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="statement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='list', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements']

  def _get_statement(self):
    """
    Getter method for statement, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement (list)

    YANG Description: Policy statements group conditions and actions
within a policy definition.  They are evaluated in
the order specified (see the description of policy
evaluation at the top of this module.
    """
    return self.__statement
      
  def _set_statement(self, v, load=False):
    """
    Setter method for statement, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_statement is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_statement() directly.

    YANG Description: Policy statements group conditions and actions
within a policy definition.  They are evaluated in
the order specified (see the description of policy
evaluation at the top of this module.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",statement.statement, yang_name="statement", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="statement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """statement must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",statement.statement, yang_name="statement", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="statement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='list', is_config=True)""",
        })

    self.__statement = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_statement(self):
    self.__statement = YANGDynClass(base=YANGListType("name",statement.statement, yang_name="statement", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="statement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='list', is_config=True)

  statement = __builtin__.property(_get_statement, _set_statement)


  _pyangbind_elements = OrderedDict([('statement', statement), ])


