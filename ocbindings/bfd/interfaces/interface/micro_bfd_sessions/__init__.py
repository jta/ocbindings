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
from . import micro_bfd_session
class micro_bfd_sessions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd/interfaces/interface/micro-bfd-sessions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters relating to micro-BFD sessions associated
with the interface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__micro_bfd_session',)

  _yang_name = 'micro-bfd-sessions'
  _yang_namespace = 'http://openconfig.net/yang/bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__micro_bfd_session = YANGDynClass(base=YANGListType("member_interface",micro_bfd_session.micro_bfd_session, yang_name="micro-bfd-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='member-interface', extensions=None), is_container='list', yang_name="micro-bfd-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='list', is_config=True)

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
      return ['bfd', 'interfaces', 'interface', 'micro-bfd-sessions']

  def _get_micro_bfd_session(self):
    """
    Getter method for micro_bfd_session, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session (list)

    YANG Description: This list contains configuration and state parameters
relating to micro-BFD session.
    """
    return self.__micro_bfd_session
      
  def _set_micro_bfd_session(self, v, load=False):
    """
    Setter method for micro_bfd_session, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_micro_bfd_session is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_micro_bfd_session() directly.

    YANG Description: This list contains configuration and state parameters
relating to micro-BFD session.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("member_interface",micro_bfd_session.micro_bfd_session, yang_name="micro-bfd-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='member-interface', extensions=None), is_container='list', yang_name="micro-bfd-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """micro_bfd_session must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("member_interface",micro_bfd_session.micro_bfd_session, yang_name="micro-bfd-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='member-interface', extensions=None), is_container='list', yang_name="micro-bfd-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='list', is_config=True)""",
        })

    self.__micro_bfd_session = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_micro_bfd_session(self):
    self.__micro_bfd_session = YANGDynClass(base=YANGListType("member_interface",micro_bfd_session.micro_bfd_session, yang_name="micro-bfd-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='member-interface', extensions=None), is_container='list', yang_name="micro-bfd-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='list', is_config=True)

  micro_bfd_session = __builtin__.property(_get_micro_bfd_session, _set_micro_bfd_session)


  _pyangbind_elements = OrderedDict([('micro_bfd_session', micro_bfd_session), ])


from . import micro_bfd_session
class micro_bfd_sessions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd/interfaces/interface/micro-bfd-sessions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters relating to micro-BFD sessions associated
with the interface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__micro_bfd_session',)

  _yang_name = 'micro-bfd-sessions'
  _yang_namespace = 'http://openconfig.net/yang/bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__micro_bfd_session = YANGDynClass(base=YANGListType("member_interface",micro_bfd_session.micro_bfd_session, yang_name="micro-bfd-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='member-interface', extensions=None), is_container='list', yang_name="micro-bfd-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='list', is_config=True)

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
      return ['bfd', 'interfaces', 'interface', 'micro-bfd-sessions']

  def _get_micro_bfd_session(self):
    """
    Getter method for micro_bfd_session, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session (list)

    YANG Description: This list contains configuration and state parameters
relating to micro-BFD session.
    """
    return self.__micro_bfd_session
      
  def _set_micro_bfd_session(self, v, load=False):
    """
    Setter method for micro_bfd_session, mapped from YANG variable /bfd/interfaces/interface/micro_bfd_sessions/micro_bfd_session (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_micro_bfd_session is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_micro_bfd_session() directly.

    YANG Description: This list contains configuration and state parameters
relating to micro-BFD session.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("member_interface",micro_bfd_session.micro_bfd_session, yang_name="micro-bfd-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='member-interface', extensions=None), is_container='list', yang_name="micro-bfd-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """micro_bfd_session must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("member_interface",micro_bfd_session.micro_bfd_session, yang_name="micro-bfd-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='member-interface', extensions=None), is_container='list', yang_name="micro-bfd-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='list', is_config=True)""",
        })

    self.__micro_bfd_session = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_micro_bfd_session(self):
    self.__micro_bfd_session = YANGDynClass(base=YANGListType("member_interface",micro_bfd_session.micro_bfd_session, yang_name="micro-bfd-session", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='member-interface', extensions=None), is_container='list', yang_name="micro-bfd-session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='list', is_config=True)

  micro_bfd_session = __builtin__.property(_get_micro_bfd_session, _set_micro_bfd_session)


  _pyangbind_elements = OrderedDict([('micro_bfd_session', micro_bfd_session), ])


