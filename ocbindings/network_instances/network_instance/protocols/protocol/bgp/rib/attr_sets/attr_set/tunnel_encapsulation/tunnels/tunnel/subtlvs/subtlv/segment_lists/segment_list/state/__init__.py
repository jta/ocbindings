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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels/tunnel/subtlvs/subtlv/segment-lists/segment-list/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the Segment List within the
Tunnel Encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instance_id','__weight',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels', 'tunnel', 'subtlvs', 'subtlv', 'segment-lists', 'segment-list', 'state']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/instance_id (uint64)

    YANG Description: Instance of the segment list within the sub-TLV
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/instance_id (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: Instance of the segment list within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/weight (uint32)

    YANG Description: The weight given to the path within the set of segment
lists that are included in the tunnel attribute sub-TLV.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: The weight given to the path within the set of segment
lists that are included in the tunnel attribute sub-TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  instance_id = __builtin__.property(_get_instance_id)
  weight = __builtin__.property(_get_weight)


  _pyangbind_elements = OrderedDict([('instance_id', instance_id), ('weight', weight), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels/tunnel/subtlvs/subtlv/segment-lists/segment-list/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the Segment List within the
Tunnel Encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instance_id','__weight',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels', 'tunnel', 'subtlvs', 'subtlv', 'segment-lists', 'segment-list', 'state']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/instance_id (uint64)

    YANG Description: Instance of the segment list within the sub-TLV
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/instance_id (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: Instance of the segment list within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/weight (uint32)

    YANG Description: The weight given to the path within the set of segment
lists that are included in the tunnel attribute sub-TLV.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: The weight given to the path within the set of segment
lists that are included in the tunnel attribute sub-TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  instance_id = __builtin__.property(_get_instance_id)
  weight = __builtin__.property(_get_weight)


  _pyangbind_elements = OrderedDict([('instance_id', instance_id), ('weight', weight), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels/tunnel/subtlvs/subtlv/segment-lists/segment-list/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the Segment List within the
Tunnel Encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instance_id','__weight',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels', 'tunnel', 'subtlvs', 'subtlv', 'segment-lists', 'segment-list', 'state']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/instance_id (uint64)

    YANG Description: Instance of the segment list within the sub-TLV
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/instance_id (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: Instance of the segment list within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/weight (uint32)

    YANG Description: The weight given to the path within the set of segment
lists that are included in the tunnel attribute sub-TLV.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: The weight given to the path within the set of segment
lists that are included in the tunnel attribute sub-TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  instance_id = __builtin__.property(_get_instance_id)
  weight = __builtin__.property(_get_weight)


  _pyangbind_elements = OrderedDict([('instance_id', instance_id), ('weight', weight), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels/tunnel/subtlvs/subtlv/segment-lists/segment-list/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the Segment List within the
Tunnel Encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instance_id','__weight',)

  _yang_name = 'state'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels', 'tunnel', 'subtlvs', 'subtlv', 'segment-lists', 'segment-list', 'state']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/instance_id (uint64)

    YANG Description: Instance of the segment list within the sub-TLV
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/instance_id (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: Instance of the segment list within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/weight (uint32)

    YANG Description: The weight given to the path within the set of segment
lists that are included in the tunnel attribute sub-TLV.
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel/subtlvs/subtlv/segment_lists/segment_list/state/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: The weight given to the path within the set of segment
lists that are included in the tunnel attribute sub-TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  instance_id = __builtin__.property(_get_instance_id)
  weight = __builtin__.property(_get_weight)


  _pyangbind_elements = OrderedDict([('instance_id', instance_id), ('weight', weight), ])


