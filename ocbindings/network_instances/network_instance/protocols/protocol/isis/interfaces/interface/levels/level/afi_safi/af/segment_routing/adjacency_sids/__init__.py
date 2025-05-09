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
from . import adjacency_sid
class adjacency_sids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/afi-safi/af/segment-routing/adjacency-sids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing adjacency SID for this
interface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__adjacency_sid',)

  _yang_name = 'adjacency-sids'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__adjacency_sid = YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'levels', 'level', 'afi-safi', 'af', 'segment-routing', 'adjacency-sids']

  def _get_adjacency_sid(self):
    """
    Getter method for adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid (list)

    YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
    """
    return self.__adjacency_sid
      
  def _set_adjacency_sid(self, v, load=False):
    """
    Setter method for adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjacency_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjacency_sid() directly.

    YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjacency_sid must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__adjacency_sid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjacency_sid(self):
    self.__adjacency_sid = YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  adjacency_sid = __builtin__.property(_get_adjacency_sid, _set_adjacency_sid)


  _pyangbind_elements = OrderedDict([('adjacency_sid', adjacency_sid), ])


from . import adjacency_sid
class adjacency_sids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/afi-safi/af/segment-routing/adjacency-sids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing adjacency SID for this
interface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__adjacency_sid',)

  _yang_name = 'adjacency-sids'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__adjacency_sid = YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'levels', 'level', 'afi-safi', 'af', 'segment-routing', 'adjacency-sids']

  def _get_adjacency_sid(self):
    """
    Getter method for adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid (list)

    YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
    """
    return self.__adjacency_sid
      
  def _set_adjacency_sid(self, v, load=False):
    """
    Setter method for adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjacency_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjacency_sid() directly.

    YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjacency_sid must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__adjacency_sid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjacency_sid(self):
    self.__adjacency_sid = YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  adjacency_sid = __builtin__.property(_get_adjacency_sid, _set_adjacency_sid)


  _pyangbind_elements = OrderedDict([('adjacency_sid', adjacency_sid), ])


from . import adjacency_sid
class adjacency_sids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/afi-safi/af/segment-routing/adjacency-sids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing adjacency SID for this
interface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__adjacency_sid',)

  _yang_name = 'adjacency-sids'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__adjacency_sid = YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'levels', 'level', 'afi-safi', 'af', 'segment-routing', 'adjacency-sids']

  def _get_adjacency_sid(self):
    """
    Getter method for adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid (list)

    YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
    """
    return self.__adjacency_sid
      
  def _set_adjacency_sid(self, v, load=False):
    """
    Setter method for adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjacency_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjacency_sid() directly.

    YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjacency_sid must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__adjacency_sid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjacency_sid(self):
    self.__adjacency_sid = YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  adjacency_sid = __builtin__.property(_get_adjacency_sid, _set_adjacency_sid)


  _pyangbind_elements = OrderedDict([('adjacency_sid', adjacency_sid), ])


from . import adjacency_sid
class adjacency_sids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/afi-safi/af/segment-routing/adjacency-sids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing adjacency SID for this
interface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__adjacency_sid',)

  _yang_name = 'adjacency-sids'
  _yang_namespace = 'http://openconfig.net/yang/network-instance'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__adjacency_sid = YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'levels', 'level', 'afi-safi', 'af', 'segment-routing', 'adjacency-sids']

  def _get_adjacency_sid(self):
    """
    Getter method for adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid (list)

    YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
    """
    return self.__adjacency_sid
      
  def _set_adjacency_sid(self, v, load=False):
    """
    Setter method for adjacency_sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids/adjacency_sid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjacency_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjacency_sid() directly.

    YANG Description: An Adjacency SID to be advertised for the specified interface.
The Adj-SID's identifier (the SID ID) must be unique, with flags
specified indicating the parameters that should be set for the SID.
Where a SID value is specified that is allocated from the SRGB, the
global flag must be set by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjacency_sid must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__adjacency_sid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjacency_sid(self):
    self.__adjacency_sid = YANGDynClass(base=YANGListType("neighbor sid_id",adjacency_sid.adjacency_sid, yang_name="adjacency-sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor sid-id', extensions=None), is_container='list', yang_name="adjacency-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  adjacency_sid = __builtin__.property(_get_adjacency_sid, _set_adjacency_sid)


  _pyangbind_elements = OrderedDict([('adjacency_sid', adjacency_sid), ])


