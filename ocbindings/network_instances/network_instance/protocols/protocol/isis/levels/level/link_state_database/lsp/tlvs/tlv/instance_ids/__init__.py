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
from . import instance_id
class instance_ids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/instance-ids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS Instance Identifier TLV.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instance_id',)

  _yang_name = 'instance-ids'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instance_id = YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'instance-ids']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/instance_ids/instance_id (list)

    YANG Description: A list of instance IDs received within TLV 7 within an
IS-IS LSP. In the case that more than one instance of
TLV 7 is included in the LSP, the instance IDs specified
within the instances are concatenated within this
list.
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/instance_ids/instance_id (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: A list of instance IDs received within TLV 7 within an
IS-IS LSP. In the case that more than one instance of
TLV 7 is included in the LSP, the instance IDs specified
within the instances are concatenated within this
list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  instance_id = __builtin__.property(_get_instance_id)


  _pyangbind_elements = OrderedDict([('instance_id', instance_id), ])


from . import instance_id
class instance_ids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/instance-ids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS Instance Identifier TLV.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instance_id',)

  _yang_name = 'instance-ids'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instance_id = YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'instance-ids']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/instance_ids/instance_id (list)

    YANG Description: A list of instance IDs received within TLV 7 within an
IS-IS LSP. In the case that more than one instance of
TLV 7 is included in the LSP, the instance IDs specified
within the instances are concatenated within this
list.
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/instance_ids/instance_id (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: A list of instance IDs received within TLV 7 within an
IS-IS LSP. In the case that more than one instance of
TLV 7 is included in the LSP, the instance IDs specified
within the instances are concatenated within this
list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  instance_id = __builtin__.property(_get_instance_id)


  _pyangbind_elements = OrderedDict([('instance_id', instance_id), ])


from . import instance_id
class instance_ids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/instance-ids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS Instance Identifier TLV.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instance_id',)

  _yang_name = 'instance-ids'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instance_id = YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'instance-ids']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/instance_ids/instance_id (list)

    YANG Description: A list of instance IDs received within TLV 7 within an
IS-IS LSP. In the case that more than one instance of
TLV 7 is included in the LSP, the instance IDs specified
within the instances are concatenated within this
list.
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/instance_ids/instance_id (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: A list of instance IDs received within TLV 7 within an
IS-IS LSP. In the case that more than one instance of
TLV 7 is included in the LSP, the instance IDs specified
within the instances are concatenated within this
list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  instance_id = __builtin__.property(_get_instance_id)


  _pyangbind_elements = OrderedDict([('instance_id', instance_id), ])


from . import instance_id
class instance_ids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/instance-ids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS Instance Identifier TLV.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instance_id',)

  _yang_name = 'instance-ids'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instance_id = YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'instance-ids']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/instance_ids/instance_id (list)

    YANG Description: A list of instance IDs received within TLV 7 within an
IS-IS LSP. In the case that more than one instance of
TLV 7 is included in the LSP, the instance IDs specified
within the instances are concatenated within this
list.
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/instance_ids/instance_id (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: A list of instance IDs received within TLV 7 within an
IS-IS LSP. In the case that more than one instance of
TLV 7 is included in the LSP, the instance IDs specified
within the instances are concatenated within this
list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=YANGListType("instance_id",instance_id.instance_id, yang_name="instance-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  instance_id = __builtin__.property(_get_instance_id)


  _pyangbind_elements = OrderedDict([('instance_id', instance_id), ])


