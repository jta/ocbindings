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
from . import group
class groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/port/breakout-mode/groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for breakout groups data.

When a device has the capability to break a port into
interfaces of different speeds and different number of
physical channels, it can breakout a 400G OSFP port with
8 physical channels (with support for 25G NRZ, 50G PAM4
and 100G PAM4) into  mixed speed interfaces. Particularly, to
break out into two 100G ports with different modulation, and a 200G
port, a user must configure 1 interface with 2 physical channels
1 interface with 4 physical channels and 1 interface with
2 physical channels. With this configuration the interface in
1st breakout group would use 50G PAM4 modulation, interface
in 2nd breakout group would use 25G NRZ modulation and the
interface in 3rd breakout group would use 100G PAM4 modulation
This configuration would result in 3 entries in the breakout
groups list. The example configuration for this case is shown below:

   {
     "groups": {
       "group": [
         {
           "config": {
             "breakout-speed": "SPEED_100GB",
             "index": 0,
             "num-breakouts": 1,
             "num-physical-channels": 2
           },
           "index": 0
         },
         {
           "config": {
             "breakout-speed": "SPEED_100GB",
             "index": 1,
             "num-breakouts": 1,
             "num-physical-channels": 4
           },
           "index": 1
         },
         {
           "config": {
             "breakout-speed": "SPEED_200GB",
             "index": 2,
             "num-breakouts": 1,
             "num-physical-channels": 2
           },
           "index": 2
         }
       ]
     }
   }

When a device does not have the capability to break a port
into interfaces of different speeds and different number of
physical channels, in order to  breakout a 400G OSFP port with
8 physical channels into 50G breakout ports it would use 8 interfaces
with 1 physical channel each. This would result in 1 entry in the
breakout groups list. The example configuration for this case is
shown below:

 {
   "groups": {
     "group": [
       {
         "config": {
           "breakout-speed": "SPEED_50GB",
           "index": 0,
           "num-breakouts": 8,
           "num-physical-channels": 1
         },
         "index": 0
       }
     ]
   }
 }

Similarly, if a 400G-DR4 interface (8 electrical channels at 50Gbps)
is to be broken out into 4 100Gbps ports, the following configuration
is used:

 {
   "groups": {
     "group": [
       {
         "config": {
           "breakout-speed": "SPEED_100GB",
           "index": 0,
           "num-breakouts": 4,
           "num-physical-channels": 2
         },
         "index": 0
       }
     ]
   }
 }
  """
  __slots__ = ('_path_helper', '_extmethods', '__group',)

  _yang_name = 'groups'
  _yang_namespace = 'http://openconfig.net/yang/platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__group = YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)

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
      return ['components', 'component', 'port', 'breakout-mode', 'groups']

  def _get_group(self):
    """
    Getter method for group, mapped from YANG variable /components/component/port/breakout_mode/groups/group (list)

    YANG Description: List of breakout groups.
    """
    return self.__group
      
  def _set_group(self, v, load=False):
    """
    Setter method for group, mapped from YANG variable /components/component/port/breakout_mode/groups/group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group() directly.

    YANG Description: List of breakout groups.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)""",
        })

    self.__group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group(self):
    self.__group = YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)

  group = __builtin__.property(_get_group, _set_group)


  _pyangbind_elements = OrderedDict([('group', group), ])


from . import group
class groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform-common - based on the path /components/component/port/breakout-mode/groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for breakout groups data.

When a device has the capability to break a port into
interfaces of different speeds and different number of
physical channels, it can breakout a 400G OSFP port with
8 physical channels (with support for 25G NRZ, 50G PAM4
and 100G PAM4) into  mixed speed interfaces. Particularly, to
break out into two 100G ports with different modulation, and a 200G
port, a user must configure 1 interface with 2 physical channels
1 interface with 4 physical channels and 1 interface with
2 physical channels. With this configuration the interface in
1st breakout group would use 50G PAM4 modulation, interface
in 2nd breakout group would use 25G NRZ modulation and the
interface in 3rd breakout group would use 100G PAM4 modulation
This configuration would result in 3 entries in the breakout
groups list. The example configuration for this case is shown below:

   {
     "groups": {
       "group": [
         {
           "config": {
             "breakout-speed": "SPEED_100GB",
             "index": 0,
             "num-breakouts": 1,
             "num-physical-channels": 2
           },
           "index": 0
         },
         {
           "config": {
             "breakout-speed": "SPEED_100GB",
             "index": 1,
             "num-breakouts": 1,
             "num-physical-channels": 4
           },
           "index": 1
         },
         {
           "config": {
             "breakout-speed": "SPEED_200GB",
             "index": 2,
             "num-breakouts": 1,
             "num-physical-channels": 2
           },
           "index": 2
         }
       ]
     }
   }

When a device does not have the capability to break a port
into interfaces of different speeds and different number of
physical channels, in order to  breakout a 400G OSFP port with
8 physical channels into 50G breakout ports it would use 8 interfaces
with 1 physical channel each. This would result in 1 entry in the
breakout groups list. The example configuration for this case is
shown below:

 {
   "groups": {
     "group": [
       {
         "config": {
           "breakout-speed": "SPEED_50GB",
           "index": 0,
           "num-breakouts": 8,
           "num-physical-channels": 1
         },
         "index": 0
       }
     ]
   }
 }

Similarly, if a 400G-DR4 interface (8 electrical channels at 50Gbps)
is to be broken out into 4 100Gbps ports, the following configuration
is used:

 {
   "groups": {
     "group": [
       {
         "config": {
           "breakout-speed": "SPEED_100GB",
           "index": 0,
           "num-breakouts": 4,
           "num-physical-channels": 2
         },
         "index": 0
       }
     ]
   }
 }
  """
  __slots__ = ('_path_helper', '_extmethods', '__group',)

  _yang_name = 'groups'
  _yang_namespace = 'http://openconfig.net/yang/platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__group = YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)

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
      return ['components', 'component', 'port', 'breakout-mode', 'groups']

  def _get_group(self):
    """
    Getter method for group, mapped from YANG variable /components/component/port/breakout_mode/groups/group (list)

    YANG Description: List of breakout groups.
    """
    return self.__group
      
  def _set_group(self, v, load=False):
    """
    Setter method for group, mapped from YANG variable /components/component/port/breakout_mode/groups/group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group() directly.

    YANG Description: List of breakout groups.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)""",
        })

    self.__group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group(self):
    self.__group = YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)

  group = __builtin__.property(_get_group, _set_group)


  _pyangbind_elements = OrderedDict([('group', group), ])


from . import group
class groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/port/breakout-mode/groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for breakout groups data.

When a device has the capability to break a port into
interfaces of different speeds and different number of
physical channels, it can breakout a 400G OSFP port with
8 physical channels (with support for 25G NRZ, 50G PAM4
and 100G PAM4) into  mixed speed interfaces. Particularly, to
break out into two 100G ports with different modulation, and a 200G
port, a user must configure 1 interface with 2 physical channels
1 interface with 4 physical channels and 1 interface with
2 physical channels. With this configuration the interface in
1st breakout group would use 50G PAM4 modulation, interface
in 2nd breakout group would use 25G NRZ modulation and the
interface in 3rd breakout group would use 100G PAM4 modulation
This configuration would result in 3 entries in the breakout
groups list. The example configuration for this case is shown below:

   {
     "groups": {
       "group": [
         {
           "config": {
             "breakout-speed": "SPEED_100GB",
             "index": 0,
             "num-breakouts": 1,
             "num-physical-channels": 2
           },
           "index": 0
         },
         {
           "config": {
             "breakout-speed": "SPEED_100GB",
             "index": 1,
             "num-breakouts": 1,
             "num-physical-channels": 4
           },
           "index": 1
         },
         {
           "config": {
             "breakout-speed": "SPEED_200GB",
             "index": 2,
             "num-breakouts": 1,
             "num-physical-channels": 2
           },
           "index": 2
         }
       ]
     }
   }

When a device does not have the capability to break a port
into interfaces of different speeds and different number of
physical channels, in order to  breakout a 400G OSFP port with
8 physical channels into 50G breakout ports it would use 8 interfaces
with 1 physical channel each. This would result in 1 entry in the
breakout groups list. The example configuration for this case is
shown below:

 {
   "groups": {
     "group": [
       {
         "config": {
           "breakout-speed": "SPEED_50GB",
           "index": 0,
           "num-breakouts": 8,
           "num-physical-channels": 1
         },
         "index": 0
       }
     ]
   }
 }

Similarly, if a 400G-DR4 interface (8 electrical channels at 50Gbps)
is to be broken out into 4 100Gbps ports, the following configuration
is used:

 {
   "groups": {
     "group": [
       {
         "config": {
           "breakout-speed": "SPEED_100GB",
           "index": 0,
           "num-breakouts": 4,
           "num-physical-channels": 2
         },
         "index": 0
       }
     ]
   }
 }
  """
  __slots__ = ('_path_helper', '_extmethods', '__group',)

  _yang_name = 'groups'
  _yang_namespace = 'http://openconfig.net/yang/platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__group = YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)

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
      return ['components', 'component', 'port', 'breakout-mode', 'groups']

  def _get_group(self):
    """
    Getter method for group, mapped from YANG variable /components/component/port/breakout_mode/groups/group (list)

    YANG Description: List of breakout groups.
    """
    return self.__group
      
  def _set_group(self, v, load=False):
    """
    Setter method for group, mapped from YANG variable /components/component/port/breakout_mode/groups/group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group() directly.

    YANG Description: List of breakout groups.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)""",
        })

    self.__group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group(self):
    self.__group = YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)

  group = __builtin__.property(_get_group, _set_group)


  _pyangbind_elements = OrderedDict([('group', group), ])


from . import group
class groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform-common - based on the path /components/component/port/breakout-mode/groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container for breakout groups data.

When a device has the capability to break a port into
interfaces of different speeds and different number of
physical channels, it can breakout a 400G OSFP port with
8 physical channels (with support for 25G NRZ, 50G PAM4
and 100G PAM4) into  mixed speed interfaces. Particularly, to
break out into two 100G ports with different modulation, and a 200G
port, a user must configure 1 interface with 2 physical channels
1 interface with 4 physical channels and 1 interface with
2 physical channels. With this configuration the interface in
1st breakout group would use 50G PAM4 modulation, interface
in 2nd breakout group would use 25G NRZ modulation and the
interface in 3rd breakout group would use 100G PAM4 modulation
This configuration would result in 3 entries in the breakout
groups list. The example configuration for this case is shown below:

   {
     "groups": {
       "group": [
         {
           "config": {
             "breakout-speed": "SPEED_100GB",
             "index": 0,
             "num-breakouts": 1,
             "num-physical-channels": 2
           },
           "index": 0
         },
         {
           "config": {
             "breakout-speed": "SPEED_100GB",
             "index": 1,
             "num-breakouts": 1,
             "num-physical-channels": 4
           },
           "index": 1
         },
         {
           "config": {
             "breakout-speed": "SPEED_200GB",
             "index": 2,
             "num-breakouts": 1,
             "num-physical-channels": 2
           },
           "index": 2
         }
       ]
     }
   }

When a device does not have the capability to break a port
into interfaces of different speeds and different number of
physical channels, in order to  breakout a 400G OSFP port with
8 physical channels into 50G breakout ports it would use 8 interfaces
with 1 physical channel each. This would result in 1 entry in the
breakout groups list. The example configuration for this case is
shown below:

 {
   "groups": {
     "group": [
       {
         "config": {
           "breakout-speed": "SPEED_50GB",
           "index": 0,
           "num-breakouts": 8,
           "num-physical-channels": 1
         },
         "index": 0
       }
     ]
   }
 }

Similarly, if a 400G-DR4 interface (8 electrical channels at 50Gbps)
is to be broken out into 4 100Gbps ports, the following configuration
is used:

 {
   "groups": {
     "group": [
       {
         "config": {
           "breakout-speed": "SPEED_100GB",
           "index": 0,
           "num-breakouts": 4,
           "num-physical-channels": 2
         },
         "index": 0
       }
     ]
   }
 }
  """
  __slots__ = ('_path_helper', '_extmethods', '__group',)

  _yang_name = 'groups'
  _yang_namespace = 'http://openconfig.net/yang/platform'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__group = YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)

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
      return ['components', 'component', 'port', 'breakout-mode', 'groups']

  def _get_group(self):
    """
    Getter method for group, mapped from YANG variable /components/component/port/breakout_mode/groups/group (list)

    YANG Description: List of breakout groups.
    """
    return self.__group
      
  def _set_group(self, v, load=False):
    """
    Setter method for group, mapped from YANG variable /components/component/port/breakout_mode/groups/group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group() directly.

    YANG Description: List of breakout groups.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)""",
        })

    self.__group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group(self):
    self.__group = YANGDynClass(base=YANGListType("index",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='list', is_config=True)

  group = __builtin__.property(_get_group, _set_group)


  _pyangbind_elements = OrderedDict([('group', group), ])


