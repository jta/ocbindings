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
from . import classifier
from . import scheduler_policy
class qos(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/control-plane-traffic/ingress/qos. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state relating to QoS policies
that are applied to control-plane traffic.
  """
  __slots__ = ('_path_helper', '_extmethods', '__classifier','__scheduler_policy',)

  _yang_name = 'qos'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__classifier = YANGDynClass(base=classifier.classifier, is_container='container', yang_name="classifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)

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
      return ['system', 'control-plane-traffic', 'ingress', 'qos']

  def _get_classifier(self):
    """
    Getter method for classifier, mapped from YANG variable /system/control_plane_traffic/ingress/qos/classifier (container)

    YANG Description: Configuration and state parameters relating to the QoS
classifier that is applied to control plane traffic. A QoS
classifier - defined in /qos/classifiers specifies how traffic
is mapped to QoS queues. The classifier specified in this
container and corresponding state allows for traffic towards
the control-plane to be classified.
    """
    return self.__classifier
      
  def _set_classifier(self, v, load=False):
    """
    Setter method for classifier, mapped from YANG variable /system/control_plane_traffic/ingress/qos/classifier (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_classifier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_classifier() directly.

    YANG Description: Configuration and state parameters relating to the QoS
classifier that is applied to control plane traffic. A QoS
classifier - defined in /qos/classifiers specifies how traffic
is mapped to QoS queues. The classifier specified in this
container and corresponding state allows for traffic towards
the control-plane to be classified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=classifier.classifier, is_container='container', yang_name="classifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """classifier must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=classifier.classifier, is_container='container', yang_name="classifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)""",
        })

    self.__classifier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_classifier(self):
    self.__classifier = YANGDynClass(base=classifier.classifier, is_container='container', yang_name="classifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)


  def _get_scheduler_policy(self):
    """
    Getter method for scheduler_policy, mapped from YANG variable /system/control_plane_traffic/ingress/qos/scheduler_policy (container)

    YANG Description: Configuration and operational state relating to the QoS
scheduler policy that is applied to control-plane traffic.
The scheduler policy determines how traffic, classified by
the specified control-plane classifier is rate-limited towards
the control-plane. The scheduler policy is defined in
/qos/scheduler-policies.
    """
    return self.__scheduler_policy
      
  def _set_scheduler_policy(self, v, load=False):
    """
    Setter method for scheduler_policy, mapped from YANG variable /system/control_plane_traffic/ingress/qos/scheduler_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler_policy() directly.

    YANG Description: Configuration and operational state relating to the QoS
scheduler policy that is applied to control-plane traffic.
The scheduler policy determines how traffic, classified by
the specified control-plane classifier is rate-limited towards
the control-plane. The scheduler policy is defined in
/qos/scheduler-policies.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)""",
        })

    self.__scheduler_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler_policy(self):
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)

  classifier = __builtin__.property(_get_classifier, _set_classifier)
  scheduler_policy = __builtin__.property(_get_scheduler_policy, _set_scheduler_policy)


  _pyangbind_elements = OrderedDict([('classifier', classifier), ('scheduler_policy', scheduler_policy), ])


from . import classifier
from . import scheduler_policy
class qos(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/control-plane-traffic/ingress/qos. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state relating to QoS policies
that are applied to control-plane traffic.
  """
  __slots__ = ('_path_helper', '_extmethods', '__classifier','__scheduler_policy',)

  _yang_name = 'qos'
  _yang_namespace = 'http://openconfig.net/yang/system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__classifier = YANGDynClass(base=classifier.classifier, is_container='container', yang_name="classifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)

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
      return ['system', 'control-plane-traffic', 'ingress', 'qos']

  def _get_classifier(self):
    """
    Getter method for classifier, mapped from YANG variable /system/control_plane_traffic/ingress/qos/classifier (container)

    YANG Description: Configuration and state parameters relating to the QoS
classifier that is applied to control plane traffic. A QoS
classifier - defined in /qos/classifiers specifies how traffic
is mapped to QoS queues. The classifier specified in this
container and corresponding state allows for traffic towards
the control-plane to be classified.
    """
    return self.__classifier
      
  def _set_classifier(self, v, load=False):
    """
    Setter method for classifier, mapped from YANG variable /system/control_plane_traffic/ingress/qos/classifier (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_classifier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_classifier() directly.

    YANG Description: Configuration and state parameters relating to the QoS
classifier that is applied to control plane traffic. A QoS
classifier - defined in /qos/classifiers specifies how traffic
is mapped to QoS queues. The classifier specified in this
container and corresponding state allows for traffic towards
the control-plane to be classified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=classifier.classifier, is_container='container', yang_name="classifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """classifier must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=classifier.classifier, is_container='container', yang_name="classifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)""",
        })

    self.__classifier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_classifier(self):
    self.__classifier = YANGDynClass(base=classifier.classifier, is_container='container', yang_name="classifier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)


  def _get_scheduler_policy(self):
    """
    Getter method for scheduler_policy, mapped from YANG variable /system/control_plane_traffic/ingress/qos/scheduler_policy (container)

    YANG Description: Configuration and operational state relating to the QoS
scheduler policy that is applied to control-plane traffic.
The scheduler policy determines how traffic, classified by
the specified control-plane classifier is rate-limited towards
the control-plane. The scheduler policy is defined in
/qos/scheduler-policies.
    """
    return self.__scheduler_policy
      
  def _set_scheduler_policy(self, v, load=False):
    """
    Setter method for scheduler_policy, mapped from YANG variable /system/control_plane_traffic/ingress/qos/scheduler_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler_policy() directly.

    YANG Description: Configuration and operational state relating to the QoS
scheduler policy that is applied to control-plane traffic.
The scheduler policy determines how traffic, classified by
the specified control-plane classifier is rate-limited towards
the control-plane. The scheduler policy is defined in
/qos/scheduler-policies.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)""",
        })

    self.__scheduler_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler_policy(self):
    self.__scheduler_policy = YANGDynClass(base=scheduler_policy.scheduler_policy, is_container='container', yang_name="scheduler-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system-controlplane', defining_module='openconfig-system-controlplane', yang_type='container', is_config=True)

  classifier = __builtin__.property(_get_classifier, _set_classifier)
  scheduler_policy = __builtin__.property(_get_scheduler_policy, _set_scheduler_policy)


  _pyangbind_elements = OrderedDict([('classifier', classifier), ('scheduler_policy', scheduler_policy), ])


