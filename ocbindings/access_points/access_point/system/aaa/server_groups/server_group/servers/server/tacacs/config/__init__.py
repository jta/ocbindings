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
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/aaa/server-groups/server-group/servers/server/tacacs/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for TACACS+ server
  """
  __slots__ = ('_path_helper', '_extmethods', '__port','__secret_key','__secret_key_hashed','__source_address',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:port-number', is_config=True)
    self.__secret_key = YANGDynClass(base=str, is_leaf=True, yang_name="secret-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:routing-password', is_config=True)
    self.__secret_key_hashed = YANGDynClass(base=str, is_leaf=True, yang_name="secret-key-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    self.__source_address = YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'aaa', 'server-groups', 'server-group', 'servers', 'server', 'tacacs', 'config']

  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/port (oc-inet:port-number)

    YANG Description: The port number on which to contact the TACACS server
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/port (oc-inet:port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: The port number on which to contact the TACACS server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:port-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with oc-inet:port-number""",
          'defined-type': "oc-inet:port-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:port-number', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:port-number', is_config=True)


  def _get_secret_key(self):
    """
    Getter method for secret_key, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/secret_key (oc-types:routing-password)

    YANG Description: The unencrypted shared key used between the authentication
server and the device.
    """
    return self.__secret_key
      
  def _set_secret_key(self, v, load=False):
    """
    Setter method for secret_key, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/secret_key (oc-types:routing-password)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secret_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secret_key() directly.

    YANG Description: The unencrypted shared key used between the authentication
server and the device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="secret-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:routing-password', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secret_key must be of a type compatible with oc-types:routing-password""",
          'defined-type': "oc-types:routing-password",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="secret-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:routing-password', is_config=True)""",
        })

    self.__secret_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secret_key(self):
    self.__secret_key = YANGDynClass(base=str, is_leaf=True, yang_name="secret-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:routing-password', is_config=True)


  def _get_secret_key_hashed(self):
    """
    Getter method for secret_key_hashed, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/secret_key_hashed (oc-aaa-types:crypt-password-type)

    YANG Description: The hashed shared key used between the authentication
server and the device.
    """
    return self.__secret_key_hashed
      
  def _set_secret_key_hashed(self, v, load=False):
    """
    Setter method for secret_key_hashed, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/secret_key_hashed (oc-aaa-types:crypt-password-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secret_key_hashed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secret_key_hashed() directly.

    YANG Description: The hashed shared key used between the authentication
server and the device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="secret-key-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secret_key_hashed must be of a type compatible with oc-aaa-types:crypt-password-type""",
          'defined-type': "oc-aaa-types:crypt-password-type",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="secret-key-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-aaa-types:crypt-password-type', is_config=True)""",
        })

    self.__secret_key_hashed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secret_key_hashed(self):
    self.__secret_key_hashed = YANGDynClass(base=str, is_leaf=True, yang_name="secret-key-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-aaa-types:crypt-password-type', is_config=True)


  def _get_source_address(self):
    """
    Getter method for source_address, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/source_address (oc-inet:ip-address)

    YANG Description: Source IP address to use in messages to the TACACS server
    """
    return self.__source_address
      
  def _set_source_address(self, v, load=False):
    """
    Setter method for source_address, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/source_address (oc-inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_address() directly.

    YANG Description: Source IP address to use in messages to the TACACS server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_address must be of a type compatible with oc-inet:ip-address""",
          'defined-type': "oc-inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=True)""",
        })

    self.__source_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_address(self):
    self.__source_address = YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=True)

  port = __builtin__.property(_get_port, _set_port)
  secret_key = __builtin__.property(_get_secret_key, _set_secret_key)
  secret_key_hashed = __builtin__.property(_get_secret_key_hashed, _set_secret_key_hashed)
  source_address = __builtin__.property(_get_source_address, _set_source_address)


  _pyangbind_elements = OrderedDict([('port', port), ('secret_key', secret_key), ('secret_key_hashed', secret_key_hashed), ('source_address', source_address), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/aaa/server-groups/server-group/servers/server/tacacs/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for TACACS+ server
  """
  __slots__ = ('_path_helper', '_extmethods', '__port','__secret_key','__secret_key_hashed','__source_address',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:port-number', is_config=True)
    self.__secret_key = YANGDynClass(base=str, is_leaf=True, yang_name="secret-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:routing-password', is_config=True)
    self.__secret_key_hashed = YANGDynClass(base=str, is_leaf=True, yang_name="secret-key-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    self.__source_address = YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'aaa', 'server-groups', 'server-group', 'servers', 'server', 'tacacs', 'config']

  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/port (oc-inet:port-number)

    YANG Description: The port number on which to contact the TACACS server
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/port (oc-inet:port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: The port number on which to contact the TACACS server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:port-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with oc-inet:port-number""",
          'defined-type': "oc-inet:port-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:port-number', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:port-number', is_config=True)


  def _get_secret_key(self):
    """
    Getter method for secret_key, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/secret_key (oc-types:routing-password)

    YANG Description: The unencrypted shared key used between the authentication
server and the device.
    """
    return self.__secret_key
      
  def _set_secret_key(self, v, load=False):
    """
    Setter method for secret_key, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/secret_key (oc-types:routing-password)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secret_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secret_key() directly.

    YANG Description: The unencrypted shared key used between the authentication
server and the device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="secret-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:routing-password', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secret_key must be of a type compatible with oc-types:routing-password""",
          'defined-type': "oc-types:routing-password",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="secret-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:routing-password', is_config=True)""",
        })

    self.__secret_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secret_key(self):
    self.__secret_key = YANGDynClass(base=str, is_leaf=True, yang_name="secret-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:routing-password', is_config=True)


  def _get_secret_key_hashed(self):
    """
    Getter method for secret_key_hashed, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/secret_key_hashed (oc-aaa-types:crypt-password-type)

    YANG Description: The hashed shared key used between the authentication
server and the device.
    """
    return self.__secret_key_hashed
      
  def _set_secret_key_hashed(self, v, load=False):
    """
    Setter method for secret_key_hashed, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/secret_key_hashed (oc-aaa-types:crypt-password-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secret_key_hashed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secret_key_hashed() directly.

    YANG Description: The hashed shared key used between the authentication
server and the device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="secret-key-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-aaa-types:crypt-password-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secret_key_hashed must be of a type compatible with oc-aaa-types:crypt-password-type""",
          'defined-type': "oc-aaa-types:crypt-password-type",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="secret-key-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-aaa-types:crypt-password-type', is_config=True)""",
        })

    self.__secret_key_hashed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secret_key_hashed(self):
    self.__secret_key_hashed = YANGDynClass(base=str, is_leaf=True, yang_name="secret-key-hashed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-aaa-types:crypt-password-type', is_config=True)


  def _get_source_address(self):
    """
    Getter method for source_address, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/source_address (oc-inet:ip-address)

    YANG Description: Source IP address to use in messages to the TACACS server
    """
    return self.__source_address
      
  def _set_source_address(self, v, load=False):
    """
    Setter method for source_address, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/tacacs/config/source_address (oc-inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_address() directly.

    YANG Description: Source IP address to use in messages to the TACACS server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_address must be of a type compatible with oc-inet:ip-address""",
          'defined-type': "oc-inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=True)""",
        })

    self.__source_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_address(self):
    self.__source_address = YANGDynClass(base=[RestrictedClassType(base_type=str, restriction_dict={'pattern': '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}'}),RestrictedClassType(base_type=str, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=True)

  port = __builtin__.property(_get_port, _set_port)
  secret_key = __builtin__.property(_get_secret_key, _set_secret_key)
  secret_key_hashed = __builtin__.property(_get_secret_key_hashed, _set_secret_key_hashed)
  source_address = __builtin__.property(_get_source_address, _set_source_address)


  _pyangbind_elements = OrderedDict([('port', port), ('secret_key', secret_key), ('secret_key_hashed', secret_key_hashed), ('source_address', source_address), ])


