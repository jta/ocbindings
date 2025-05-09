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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved-bandwidth/setup-priority/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
11.
  """
  __slots__ = ('_path_helper', '_extmethods', '__priority','__bandwidth',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'unreserved-bandwidth', 'setup-priority', 'state']

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/priority (uint8)

    YANG Description: Setup priority level of 0 through 7 to be used by
Unreserved Bandwidth sub-TLV 11.
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Setup priority level of 0 through 7 to be used by
Unreserved Bandwidth sub-TLV 11.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_bandwidth(self):
    """
    Getter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/bandwidth (oc-types:ieeefloat32)

    YANG Description: The amount of bandwidth reservable in this
direction on this link. Note that for
oversubscription purposes, this can be greater than
the bandwidth of the link. It contains eight 32-bit
IEEE floating point numbers(one for each priority).
The units are bytes (not bits!) per second. The
values correspond to the bandwidth that can be
reserved with a setup priority of 0 through 7,
arranged in increasing order with priority 0
occurring at the start of the sub-TLV, and priority
7 at the end of the sub-TLV.
    """
    return self.__bandwidth
      
  def _set_bandwidth(self, v, load=False):
    """
    Setter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/bandwidth (oc-types:ieeefloat32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth() directly.

    YANG Description: The amount of bandwidth reservable in this
direction on this link. Note that for
oversubscription purposes, this can be greater than
the bandwidth of the link. It contains eight 32-bit
IEEE floating point numbers(one for each priority).
The units are bytes (not bits!) per second. The
values correspond to the bandwidth that can be
reserved with a setup priority of 0 through 7,
arranged in increasing order with priority 0
occurring at the start of the sub-TLV, and priority
7 at the end of the sub-TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth must be of a type compatible with oc-types:ieeefloat32""",
          'defined-type': "oc-types:ieeefloat32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)""",
        })

    self.__bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth(self):
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

  priority = __builtin__.property(_get_priority)
  bandwidth = __builtin__.property(_get_bandwidth)


  _pyangbind_elements = OrderedDict([('priority', priority), ('bandwidth', bandwidth), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved-bandwidth/setup-priority/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
11.
  """
  __slots__ = ('_path_helper', '_extmethods', '__priority','__bandwidth',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'unreserved-bandwidth', 'setup-priority', 'state']

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/priority (uint8)

    YANG Description: Setup priority level of 0 through 7 to be used by
Unreserved Bandwidth sub-TLV 11.
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Setup priority level of 0 through 7 to be used by
Unreserved Bandwidth sub-TLV 11.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_bandwidth(self):
    """
    Getter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/bandwidth (oc-types:ieeefloat32)

    YANG Description: The amount of bandwidth reservable in this
direction on this link. Note that for
oversubscription purposes, this can be greater than
the bandwidth of the link. It contains eight 32-bit
IEEE floating point numbers(one for each priority).
The units are bytes (not bits!) per second. The
values correspond to the bandwidth that can be
reserved with a setup priority of 0 through 7,
arranged in increasing order with priority 0
occurring at the start of the sub-TLV, and priority
7 at the end of the sub-TLV.
    """
    return self.__bandwidth
      
  def _set_bandwidth(self, v, load=False):
    """
    Setter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/bandwidth (oc-types:ieeefloat32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth() directly.

    YANG Description: The amount of bandwidth reservable in this
direction on this link. Note that for
oversubscription purposes, this can be greater than
the bandwidth of the link. It contains eight 32-bit
IEEE floating point numbers(one for each priority).
The units are bytes (not bits!) per second. The
values correspond to the bandwidth that can be
reserved with a setup priority of 0 through 7,
arranged in increasing order with priority 0
occurring at the start of the sub-TLV, and priority
7 at the end of the sub-TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth must be of a type compatible with oc-types:ieeefloat32""",
          'defined-type': "oc-types:ieeefloat32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)""",
        })

    self.__bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth(self):
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

  priority = __builtin__.property(_get_priority)
  bandwidth = __builtin__.property(_get_bandwidth)


  _pyangbind_elements = OrderedDict([('priority', priority), ('bandwidth', bandwidth), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved-bandwidth/setup-priority/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
11.
  """
  __slots__ = ('_path_helper', '_extmethods', '__priority','__bandwidth',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'unreserved-bandwidth', 'setup-priority', 'state']

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/priority (uint8)

    YANG Description: Setup priority level of 0 through 7 to be used by
Unreserved Bandwidth sub-TLV 11.
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Setup priority level of 0 through 7 to be used by
Unreserved Bandwidth sub-TLV 11.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_bandwidth(self):
    """
    Getter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/bandwidth (oc-types:ieeefloat32)

    YANG Description: The amount of bandwidth reservable in this
direction on this link. Note that for
oversubscription purposes, this can be greater than
the bandwidth of the link. It contains eight 32-bit
IEEE floating point numbers(one for each priority).
The units are bytes (not bits!) per second. The
values correspond to the bandwidth that can be
reserved with a setup priority of 0 through 7,
arranged in increasing order with priority 0
occurring at the start of the sub-TLV, and priority
7 at the end of the sub-TLV.
    """
    return self.__bandwidth
      
  def _set_bandwidth(self, v, load=False):
    """
    Setter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/bandwidth (oc-types:ieeefloat32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth() directly.

    YANG Description: The amount of bandwidth reservable in this
direction on this link. Note that for
oversubscription purposes, this can be greater than
the bandwidth of the link. It contains eight 32-bit
IEEE floating point numbers(one for each priority).
The units are bytes (not bits!) per second. The
values correspond to the bandwidth that can be
reserved with a setup priority of 0 through 7,
arranged in increasing order with priority 0
occurring at the start of the sub-TLV, and priority
7 at the end of the sub-TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth must be of a type compatible with oc-types:ieeefloat32""",
          'defined-type': "oc-types:ieeefloat32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)""",
        })

    self.__bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth(self):
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

  priority = __builtin__.property(_get_priority)
  bandwidth = __builtin__.property(_get_bandwidth)


  _pyangbind_elements = OrderedDict([('priority', priority), ('bandwidth', bandwidth), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved-bandwidth/setup-priority/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
11.
  """
  __slots__ = ('_path_helper', '_extmethods', '__priority','__bandwidth',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'unreserved-bandwidth', 'setup-priority', 'state']

  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/priority (uint8)

    YANG Description: Setup priority level of 0 through 7 to be used by
Unreserved Bandwidth sub-TLV 11.
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Setup priority level of 0 through 7 to be used by
Unreserved Bandwidth sub-TLV 11.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_bandwidth(self):
    """
    Getter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/bandwidth (oc-types:ieeefloat32)

    YANG Description: The amount of bandwidth reservable in this
direction on this link. Note that for
oversubscription purposes, this can be greater than
the bandwidth of the link. It contains eight 32-bit
IEEE floating point numbers(one for each priority).
The units are bytes (not bits!) per second. The
values correspond to the bandwidth that can be
reserved with a setup priority of 0 through 7,
arranged in increasing order with priority 0
occurring at the start of the sub-TLV, and priority
7 at the end of the sub-TLV.
    """
    return self.__bandwidth
      
  def _set_bandwidth(self, v, load=False):
    """
    Setter method for bandwidth, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/unreserved_bandwidth/setup_priority/state/bandwidth (oc-types:ieeefloat32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth() directly.

    YANG Description: The amount of bandwidth reservable in this
direction on this link. Note that for
oversubscription purposes, this can be greater than
the bandwidth of the link. It contains eight 32-bit
IEEE floating point numbers(one for each priority).
The units are bytes (not bits!) per second. The
values correspond to the bandwidth that can be
reserved with a setup priority of 0 through 7,
arranged in increasing order with priority 0
occurring at the start of the sub-TLV, and priority
7 at the end of the sub-TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth must be of a type compatible with oc-types:ieeefloat32""",
          'defined-type': "oc-types:ieeefloat32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)""",
        })

    self.__bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth(self):
    self.__bandwidth = YANGDynClass(base=RestrictedClassType(base_type=YANGBinary, restriction_dict={'length': ['4']}), is_leaf=True, yang_name="bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:ieeefloat32', is_config=False)

  priority = __builtin__.property(_get_priority)
  bandwidth = __builtin__.property(_get_bandwidth)


  _pyangbind_elements = OrderedDict([('priority', priority), ('bandwidth', bandwidth), ])


