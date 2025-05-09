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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/ntp/ntp-keys/ntp-key/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for NTP auth keys
  """
  __slots__ = ('_path_helper', '_extmethods', '__key_id','__key_type','__key_value',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__key_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=True)
    self.__key_type = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}},), is_leaf=True, yang_name="key-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)
    self.__key_value = YANGDynClass(base=str, is_leaf=True, yang_name="key-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'ntp', 'ntp-keys', 'ntp-key', 'config']

  def _get_key_id(self):
    """
    Getter method for key_id, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_id (uint16)

    YANG Description: Integer identifier used by the client and server to
designate a secret key.  The client and server must use
the same key id.
    """
    return self.__key_id
      
  def _set_key_id(self, v, load=False):
    """
    Setter method for key_id, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_id() directly.

    YANG Description: Integer identifier used by the client and server to
designate a secret key.  The client and server must use
the same key id.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=True)""",
        })

    self.__key_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_id(self):
    self.__key_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=True)


  def _get_key_type(self):
    """
    Getter method for key_type, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_type (identityref)

    YANG Description: Encryption type used for the NTP authentication key
    """
    return self.__key_type
      
  def _set_key_type(self, v, load=False):
    """
    Setter method for key_type, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_type() directly.

    YANG Description: Encryption type used for the NTP authentication key
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}},), is_leaf=True, yang_name="key-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_type must be of a type compatible with identityref""",
          'defined-type': "openconfig-access-points:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}},), is_leaf=True, yang_name="key-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)""",
        })

    self.__key_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_type(self):
    self.__key_type = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}},), is_leaf=True, yang_name="key-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)


  def _get_key_value(self):
    """
    Getter method for key_value, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_value (string)

    YANG Description: NTP authentication key value
    """
    return self.__key_value
      
  def _set_key_value(self, v, load=False):
    """
    Setter method for key_value, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_value (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_value() directly.

    YANG Description: NTP authentication key value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="key-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_value must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="key-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)""",
        })

    self.__key_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_value(self):
    self.__key_value = YANGDynClass(base=str, is_leaf=True, yang_name="key-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)

  key_id = __builtin__.property(_get_key_id, _set_key_id)
  key_type = __builtin__.property(_get_key_type, _set_key_type)
  key_value = __builtin__.property(_get_key_value, _set_key_value)


  _pyangbind_elements = OrderedDict([('key_id', key_id), ('key_type', key_type), ('key_value', key_value), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/ntp/ntp-keys/ntp-key/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for NTP auth keys
  """
  __slots__ = ('_path_helper', '_extmethods', '__key_id','__key_type','__key_value',)

  _yang_name = 'config'
  _yang_namespace = 'http://openconfig.net/yang/wifi/access-points'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__key_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=True)
    self.__key_type = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}},), is_leaf=True, yang_name="key-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)
    self.__key_value = YANGDynClass(base=str, is_leaf=True, yang_name="key-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'ntp', 'ntp-keys', 'ntp-key', 'config']

  def _get_key_id(self):
    """
    Getter method for key_id, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_id (uint16)

    YANG Description: Integer identifier used by the client and server to
designate a secret key.  The client and server must use
the same key id.
    """
    return self.__key_id
      
  def _set_key_id(self, v, load=False):
    """
    Setter method for key_id, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_id() directly.

    YANG Description: Integer identifier used by the client and server to
designate a secret key.  The client and server must use
the same key id.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=True)""",
        })

    self.__key_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_id(self):
    self.__key_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=True)


  def _get_key_type(self):
    """
    Getter method for key_type, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_type (identityref)

    YANG Description: Encryption type used for the NTP authentication key
    """
    return self.__key_type
      
  def _set_key_type(self, v, load=False):
    """
    Setter method for key_type, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_type() directly.

    YANG Description: Encryption type used for the NTP authentication key
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}},), is_leaf=True, yang_name="key-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_type must be of a type compatible with identityref""",
          'defined-type': "openconfig-access-points:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}},), is_leaf=True, yang_name="key-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)""",
        })

    self.__key_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_type(self):
    self.__key_type = YANGDynClass(base=RestrictedClassType(base_type=str, restriction_type="dict_key", restriction_arg={'NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_MD5': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA1': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA384': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_SHA512': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_128': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'openconfig-system:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}, 'oc-sys:NTP_AUTH_AES_CBC_256': {'@module': 'openconfig-system', '@namespace': 'http://openconfig.net/yang/system'}},), is_leaf=True, yang_name="key-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)


  def _get_key_value(self):
    """
    Getter method for key_value, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_value (string)

    YANG Description: NTP authentication key value
    """
    return self.__key_value
      
  def _set_key_value(self, v, load=False):
    """
    Setter method for key_value, mapped from YANG variable /access_points/access_point/system/ntp/ntp_keys/ntp_key/config/key_value (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_value() directly.

    YANG Description: NTP authentication key value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="key-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_value must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="key-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)""",
        })

    self.__key_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_value(self):
    self.__key_value = YANGDynClass(base=str, is_leaf=True, yang_name="key-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=True)

  key_id = __builtin__.property(_get_key_id, _set_key_id)
  key_type = __builtin__.property(_get_key_type, _set_key_type)
  key_value = __builtin__.property(_get_key_value, _set_key_value)


  _pyangbind_elements = OrderedDict([('key_id', key_id), ('key_type', key_type), ('key_value', key_value), ])


