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
from . import state
from . import unknown_subtlv
class sub_tlv(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/node-attribute/sub-tlvs/sub-tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of the Sub-TLVs contained within the Node Attribute
TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__state','__unknown_subtlv',)

  _yang_name = 'sub-tlv'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'traffic-engineering', 'tlvs', 'tlv', 'node-attribute', 'sub-tlvs', 'sub-tlv']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state (container)

    YANG Description: State parameters of the Node Attribute TLV sub-TLV
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of the Node Attribute TLV sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unknown_subtlv(self):
    """
    Getter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/unknown_subtlv (container)

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    return self.__unknown_subtlv
      
  def _set_unknown_subtlv(self, v, load=False):
    """
    Setter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/unknown_subtlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_subtlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_subtlv() directly.

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_subtlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unknown_subtlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_subtlv(self):
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  unknown_subtlv = __builtin__.property(_get_unknown_subtlv)


  _pyangbind_elements = OrderedDict([('state', state), ('unknown_subtlv', unknown_subtlv), ])


from . import state
from . import unknown_subtlv
class sub_tlv(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/node-attribute/sub-tlvs/sub-tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of the Sub-TLVs contained within the Node Attribute
TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__state','__unknown_subtlv',)

  _yang_name = 'sub-tlv'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'traffic-engineering', 'tlvs', 'tlv', 'node-attribute', 'sub-tlvs', 'sub-tlv']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state (container)

    YANG Description: State parameters of the Node Attribute TLV sub-TLV
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of the Node Attribute TLV sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unknown_subtlv(self):
    """
    Getter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/unknown_subtlv (container)

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    return self.__unknown_subtlv
      
  def _set_unknown_subtlv(self, v, load=False):
    """
    Setter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/unknown_subtlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_subtlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_subtlv() directly.

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_subtlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unknown_subtlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_subtlv(self):
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  unknown_subtlv = __builtin__.property(_get_unknown_subtlv)


  _pyangbind_elements = OrderedDict([('state', state), ('unknown_subtlv', unknown_subtlv), ])


from . import state
from . import unknown_subtlv
class sub_tlv(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/node-attribute/sub-tlvs/sub-tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of the Sub-TLVs contained within the Node Attribute
TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__state','__unknown_subtlv',)

  _yang_name = 'sub-tlv'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'traffic-engineering', 'tlvs', 'tlv', 'node-attribute', 'sub-tlvs', 'sub-tlv']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state (container)

    YANG Description: State parameters of the Node Attribute TLV sub-TLV
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of the Node Attribute TLV sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unknown_subtlv(self):
    """
    Getter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/unknown_subtlv (container)

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    return self.__unknown_subtlv
      
  def _set_unknown_subtlv(self, v, load=False):
    """
    Setter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/unknown_subtlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_subtlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_subtlv() directly.

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_subtlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unknown_subtlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_subtlv(self):
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  unknown_subtlv = __builtin__.property(_get_unknown_subtlv)


  _pyangbind_elements = OrderedDict([('state', state), ('unknown_subtlv', unknown_subtlv), ])


from . import state
from . import unknown_subtlv
class sub_tlv(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/node-attribute/sub-tlvs/sub-tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of the Sub-TLVs contained within the Node Attribute
TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__state','__unknown_subtlv',)

  _yang_name = 'sub-tlv'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'traffic-engineering', 'tlvs', 'tlv', 'node-attribute', 'sub-tlvs', 'sub-tlv']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state (container)

    YANG Description: State parameters of the Node Attribute TLV sub-TLV
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of the Node Attribute TLV sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unknown_subtlv(self):
    """
    Getter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/unknown_subtlv (container)

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    return self.__unknown_subtlv
      
  def _set_unknown_subtlv(self, v, load=False):
    """
    Setter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/node_attribute/sub_tlvs/sub_tlv/unknown_subtlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_subtlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_subtlv() directly.

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_subtlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unknown_subtlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_subtlv(self):
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  unknown_subtlv = __builtin__.property(_get_unknown_subtlv)


  _pyangbind_elements = OrderedDict([('state', state), ('unknown_subtlv', unknown_subtlv), ])


