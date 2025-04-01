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
  from YANG module openconfig-relay-agent - based on the path /relay-agent/dhcp/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data global DHCPv4
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable_relay_agent',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/relay-agent'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable_relay_agent = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-relay-agent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)

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
      return ['relay-agent', 'dhcp', 'state']

  def _get_enable_relay_agent(self):
    """
    Getter method for enable_relay_agent, mapped from YANG variable /relay_agent/dhcp/state/enable_relay_agent (boolean)

    YANG Description: Enables DHCP/BOOTP relay agent on all interfaces
    """
    return self.__enable_relay_agent
      
  def _set_enable_relay_agent(self, v, load=False):
    """
    Setter method for enable_relay_agent, mapped from YANG variable /relay_agent/dhcp/state/enable_relay_agent (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_relay_agent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_relay_agent() directly.

    YANG Description: Enables DHCP/BOOTP relay agent on all interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-relay-agent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_relay_agent must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-relay-agent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable_relay_agent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_relay_agent(self):
    self.__enable_relay_agent = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-relay-agent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)

  enable_relay_agent = __builtin__.property(_get_enable_relay_agent)


  _pyangbind_elements = OrderedDict([('enable_relay_agent', enable_relay_agent), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-relay-agent - based on the path /relay-agent/dhcp/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data global DHCPv4
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable_relay_agent',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/relay-agent'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable_relay_agent = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-relay-agent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)

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
      return ['relay-agent', 'dhcp', 'state']

  def _get_enable_relay_agent(self):
    """
    Getter method for enable_relay_agent, mapped from YANG variable /relay_agent/dhcp/state/enable_relay_agent (boolean)

    YANG Description: Enables DHCP/BOOTP relay agent on all interfaces
    """
    return self.__enable_relay_agent
      
  def _set_enable_relay_agent(self, v, load=False):
    """
    Setter method for enable_relay_agent, mapped from YANG variable /relay_agent/dhcp/state/enable_relay_agent (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_relay_agent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_relay_agent() directly.

    YANG Description: Enables DHCP/BOOTP relay agent on all interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-relay-agent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_relay_agent must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-relay-agent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable_relay_agent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_relay_agent(self):
    self.__enable_relay_agent = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-relay-agent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)

  enable_relay_agent = __builtin__.property(_get_enable_relay_agent)


  _pyangbind_elements = OrderedDict([('enable_relay_agent', enable_relay_agent), ])


