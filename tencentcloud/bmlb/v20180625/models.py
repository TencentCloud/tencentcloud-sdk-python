# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class BindL4Backend(AbstractModel):
    r"""待与四层监听器绑定的物理机主机、虚拟机或半托管主机信息。目前一个四层监听器下面最多允许绑定255个主机端口。

    """

    def __init__(self):
        r"""
        :param _Port: 待绑定的主机端口，可选值1~65535。
        :type Port: int
        :param _InstanceId: 待绑定的黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        :param _Weight: 待绑定的主机权重，可选值0~100。
        :type Weight: int
        :param _ProbePort: 自定义探测的主机端口，可选值1~65535。（需要监听器开启自定义健康检查）
        :type ProbePort: int
        """
        self._Port = None
        self._InstanceId = None
        self._Weight = None
        self._ProbePort = None

    @property
    def Port(self):
        r"""待绑定的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        r"""待绑定的黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        r"""待绑定的主机权重，可选值0~100。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def ProbePort(self):
        r"""自定义探测的主机端口，可选值1~65535。（需要监听器开启自定义健康检查）
        :rtype: int
        """
        return self._ProbePort

    @ProbePort.setter
    def ProbePort(self, ProbePort):
        self._ProbePort = ProbePort


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        self._ProbePort = params.get("ProbePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindL4BackendsRequest(AbstractModel):
    r"""BindL4Backends请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 四层监听器实例ID，可通过接口DescribeL4Listeners查询。
        :type ListenerId: str
        :param _BackendSet: 待绑定的主机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。
        :type BackendSet: list of BindL4Backend
        :param _BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._BackendSet = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""四层监听器实例ID，可通过接口DescribeL4Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def BackendSet(self):
        r"""待绑定的主机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。
        :rtype: list of BindL4Backend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet

    @property
    def BindType(self):
        r"""绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = BindL4Backend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindL4BackendsResponse(AbstractModel):
    r"""BindL4Backends返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BindL7Backend(AbstractModel):
    r"""待与七层监听器转发规则绑定的物理机主机、虚拟机或半托管主机信息。目前一个七层转发路径下面最多允许绑定255个主机端口。

    """

    def __init__(self):
        r"""
        :param _Port: 待绑定的主机端口，可选值1~65535。
        :type Port: int
        :param _InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        :param _Weight: 待绑定的主机权重，可选值0~100。
        :type Weight: int
        """
        self._Port = None
        self._InstanceId = None
        self._Weight = None

    @property
    def Port(self):
        r"""待绑定的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        r"""黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        r"""待绑定的主机权重，可选值0~100。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindL7BackendsRequest(AbstractModel):
    r"""BindL7Backends请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。
        :type DomainId: str
        :param _LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。
        :type LocationId: str
        :param _BackendSet: 待绑定的主机信息。可以绑定多个主机端口。目前一个七层转发路径下面最多允许绑定255个主机端口。
        :type BackendSet: list of BindL7Backend
        :param _BindType: 绑定类型。0：物理机，1：虚拟机 2：半托管机器。
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainId = None
        self._LocationId = None
        self._BackendSet = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainId(self):
        r"""转发域名实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LocationId(self):
        r"""转发路径实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def BackendSet(self):
        r"""待绑定的主机信息。可以绑定多个主机端口。目前一个七层转发路径下面最多允许绑定255个主机端口。
        :rtype: list of BindL7Backend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet

    @property
    def BindType(self):
        r"""绑定类型。0：物理机，1：虚拟机 2：半托管机器。
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainId = params.get("DomainId")
        self._LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = BindL7Backend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindL7BackendsResponse(AbstractModel):
    r"""BindL7Backends返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BindTrafficMirrorListenersRequest(AbstractModel):
    r"""BindTrafficMirrorListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID。
        :type TrafficMirrorId: str
        :param _ListenerIds: 七层监听器实例ID数组，可通过接口DescribeL7Listeners查询。
        :type ListenerIds: list of str
        """
        self._TrafficMirrorId = None
        self._ListenerIds = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def ListenerIds(self):
        r"""七层监听器实例ID数组，可通过接口DescribeL7Listeners查询。
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindTrafficMirrorListenersResponse(AbstractModel):
    r"""BindTrafficMirrorListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BindTrafficMirrorReceiver(AbstractModel):
    r"""待与流量镜像绑定的接收机信息。

    """

    def __init__(self):
        r"""
        :param _Port: 待绑定的主机端口，可选值1~65535。
        :type Port: int
        :param _InstanceId: 待绑定的主机实例ID。
        :type InstanceId: str
        :param _Weight: 待绑定的主机权重，可选值0~100。
        :type Weight: int
        """
        self._Port = None
        self._InstanceId = None
        self._Weight = None

    @property
    def Port(self):
        r"""待绑定的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        r"""待绑定的主机实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        r"""待绑定的主机权重，可选值0~100。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindTrafficMirrorReceiversRequest(AbstractModel):
    r"""BindTrafficMirrorReceivers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID。
        :type TrafficMirrorId: str
        :param _ReceiverSet: 待绑定的黑石物理机信息数组。
        :type ReceiverSet: list of BindTrafficMirrorReceiver
        """
        self._TrafficMirrorId = None
        self._ReceiverSet = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def ReceiverSet(self):
        r"""待绑定的黑石物理机信息数组。
        :rtype: list of BindTrafficMirrorReceiver
        """
        return self._ReceiverSet

    @ReceiverSet.setter
    def ReceiverSet(self, ReceiverSet):
        self._ReceiverSet = ReceiverSet


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self._ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = BindTrafficMirrorReceiver()
                obj._deserialize(item)
                self._ReceiverSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindTrafficMirrorReceiversResponse(AbstractModel):
    r"""BindTrafficMirrorReceivers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CertDetailLoadBalancer(AbstractModel):
    r"""获取证书信息时返回的所用在的负载均衡信息。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 黑石负载均衡实例ID。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 黑石负载均衡实例名称。
        :type LoadBalancerName: str
        :param _VpcId: 该黑石负载均衡所在的VpcId。
        :type VpcId: str
        :param _RegionId: 该黑石负载均衡所在的regionId。
        :type RegionId: int
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._VpcId = None
        self._RegionId = None

    @property
    def LoadBalancerId(self):
        r"""黑石负载均衡实例ID。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""黑石负载均衡实例名称。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def VpcId(self):
        r"""该黑石负载均衡所在的VpcId。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def RegionId(self):
        r"""该黑石负载均衡所在的regionId。
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._VpcId = params.get("VpcId")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4Listener(AbstractModel):
    r"""用于创建四层监听器的监听器信息。目前一个负载均衡下面最多允许创建50个监听器。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerPort: 监听器监听端口，可选值1~65535。
        :type LoadBalancerPort: int
        :param _Protocol: 监听器协议类型，可选值tcp，udp。
        :type Protocol: str
        :param _ListenerName: 监听器名称。
        :type ListenerName: str
        :param _SessionExpire: 监听器的会话保持时间，单位：秒。可选值：900~3600,不传表示不开启会话保持。
        :type SessionExpire: int
        :param _HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）。默认值0，表示关闭。
        :type HealthSwitch: int
        :param _TimeOut: 健康检查的响应超时时间，可选值：2-60，默认值：2，单位:秒。<br><font color="red">响应超时时间要小于检查间隔时间。</font>
        :type TimeOut: int
        :param _IntervalTime: 健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。
        :type IntervalTime: int
        :param _HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :type HealthNum: int
        :param _UnhealthNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :type UnhealthNum: int
        :param _Bandwidth: 监听器最大带宽值，用于计费模式为固定带宽计费，可选值：0-1000，单位：Mbps。
        :type Bandwidth: int
        :param _CustomHealthSwitch: 是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）
        :type CustomHealthSwitch: int
        :param _InputType: 自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。
        :type InputType: str
        :param _LineSeparatorType: 探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。
        :type LineSeparatorType: int
        :param _HealthRequest: 自定义探测请求内容。
        :type HealthRequest: str
        :param _HealthResponse: 自定义探测返回内容。
        :type HealthResponse: str
        :param _ToaFlag: 是否开启toa。可选值：0（关闭）、1（开启），默认关闭。（该字段在负载均衡为fullnat类型下才生效）
        :type ToaFlag: int
        """
        self._LoadBalancerPort = None
        self._Protocol = None
        self._ListenerName = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._Bandwidth = None
        self._CustomHealthSwitch = None
        self._InputType = None
        self._LineSeparatorType = None
        self._HealthRequest = None
        self._HealthResponse = None
        self._ToaFlag = None

    @property
    def LoadBalancerPort(self):
        r"""监听器监听端口，可选值1~65535。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Protocol(self):
        r"""监听器协议类型，可选值tcp，udp。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerName(self):
        r"""监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SessionExpire(self):
        r"""监听器的会话保持时间，单位：秒。可选值：900~3600,不传表示不开启会话保持。
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""是否开启健康检查：1（开启）、0（关闭）。默认值0，表示关闭。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        r"""健康检查的响应超时时间，可选值：2-60，默认值：2，单位:秒。<br><font color="red">响应超时时间要小于检查间隔时间。</font>
        :rtype: int
        """
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        r"""健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def Bandwidth(self):
        r"""监听器最大带宽值，用于计费模式为固定带宽计费，可选值：0-1000，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def CustomHealthSwitch(self):
        r"""是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）
        :rtype: int
        """
        return self._CustomHealthSwitch

    @CustomHealthSwitch.setter
    def CustomHealthSwitch(self, CustomHealthSwitch):
        self._CustomHealthSwitch = CustomHealthSwitch

    @property
    def InputType(self):
        r"""自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def LineSeparatorType(self):
        r"""探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。
        :rtype: int
        """
        return self._LineSeparatorType

    @LineSeparatorType.setter
    def LineSeparatorType(self, LineSeparatorType):
        self._LineSeparatorType = LineSeparatorType

    @property
    def HealthRequest(self):
        r"""自定义探测请求内容。
        :rtype: str
        """
        return self._HealthRequest

    @HealthRequest.setter
    def HealthRequest(self, HealthRequest):
        self._HealthRequest = HealthRequest

    @property
    def HealthResponse(self):
        r"""自定义探测返回内容。
        :rtype: str
        """
        return self._HealthResponse

    @HealthResponse.setter
    def HealthResponse(self, HealthResponse):
        self._HealthResponse = HealthResponse

    @property
    def ToaFlag(self):
        r"""是否开启toa。可选值：0（关闭）、1（开启），默认关闭。（该字段在负载均衡为fullnat类型下才生效）
        :rtype: int
        """
        return self._ToaFlag

    @ToaFlag.setter
    def ToaFlag(self, ToaFlag):
        self._ToaFlag = ToaFlag


    def _deserialize(self, params):
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Protocol = params.get("Protocol")
        self._ListenerName = params.get("ListenerName")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._Bandwidth = params.get("Bandwidth")
        self._CustomHealthSwitch = params.get("CustomHealthSwitch")
        self._InputType = params.get("InputType")
        self._LineSeparatorType = params.get("LineSeparatorType")
        self._HealthRequest = params.get("HealthRequest")
        self._HealthResponse = params.get("HealthResponse")
        self._ToaFlag = params.get("ToaFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4ListenersRequest(AbstractModel):
    r"""CreateL4Listeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerSet: 监听器信息数组，可以创建多个监听器。目前一个负载均衡下面最多允许创建50个监听器
        :type ListenerSet: list of CreateL4Listener
        """
        self._LoadBalancerId = None
        self._ListenerSet = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerSet(self):
        r"""监听器信息数组，可以创建多个监听器。目前一个负载均衡下面最多允许创建50个监听器
        :rtype: list of CreateL4Listener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = CreateL4Listener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4ListenersResponse(AbstractModel):
    r"""CreateL4Listeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateL7Listener(AbstractModel):
    r"""用于创建四层监听器的监听器信息。目前一个负载均衡下面最多允许创建50个七层监听器。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerPort: 七层监听器端口，可选值1~65535。
        :type LoadBalancerPort: int
        :param _Protocol: 七层监听器协议类型，可选值：http,https。
        :type Protocol: str
        :param _ListenerName: 七层监听器名称。
        :type ListenerName: str
        :param _SslMode: 认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。当创建的是https类型的监听器时，此值必选。
        :type SslMode: int
        :param _CertId: 服务端证书ID。当创建的是https类型的监听器时，此值必选。
        :type CertId: str
        :param _CertName: 服务端证书名称。
        :type CertName: str
        :param _CertContent: 服务端证书内容。
        :type CertContent: str
        :param _CertKey: 服务端证书密钥。
        :type CertKey: str
        :param _CertCaId: 客户端证书ID。
        :type CertCaId: str
        :param _CertCaName: 客户端证书名称。
        :type CertCaName: str
        :param _CertCaContent: 客户端证书内容。
        :type CertCaContent: str
        :param _Bandwidth: 用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。
        :type Bandwidth: int
        :param _ForwardProtocol: 转发协议。当Protocol为https时并且SslMode为1或2时，有意义。可选的值为0：https，1：spdy，2：http2，3：spdy+http2。
        :type ForwardProtocol: int
        """
        self._LoadBalancerPort = None
        self._Protocol = None
        self._ListenerName = None
        self._SslMode = None
        self._CertId = None
        self._CertName = None
        self._CertContent = None
        self._CertKey = None
        self._CertCaId = None
        self._CertCaName = None
        self._CertCaContent = None
        self._Bandwidth = None
        self._ForwardProtocol = None

    @property
    def LoadBalancerPort(self):
        r"""七层监听器端口，可选值1~65535。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Protocol(self):
        r"""七层监听器协议类型，可选值：http,https。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerName(self):
        r"""七层监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SslMode(self):
        r"""认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。当创建的是https类型的监听器时，此值必选。
        :rtype: int
        """
        return self._SslMode

    @SslMode.setter
    def SslMode(self, SslMode):
        self._SslMode = SslMode

    @property
    def CertId(self):
        r"""服务端证书ID。当创建的是https类型的监听器时，此值必选。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        r"""服务端证书名称。
        :rtype: str
        """
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertContent(self):
        r"""服务端证书内容。
        :rtype: str
        """
        return self._CertContent

    @CertContent.setter
    def CertContent(self, CertContent):
        self._CertContent = CertContent

    @property
    def CertKey(self):
        r"""服务端证书密钥。
        :rtype: str
        """
        return self._CertKey

    @CertKey.setter
    def CertKey(self, CertKey):
        self._CertKey = CertKey

    @property
    def CertCaId(self):
        r"""客户端证书ID。
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def CertCaName(self):
        r"""客户端证书名称。
        :rtype: str
        """
        return self._CertCaName

    @CertCaName.setter
    def CertCaName(self, CertCaName):
        self._CertCaName = CertCaName

    @property
    def CertCaContent(self):
        r"""客户端证书内容。
        :rtype: str
        """
        return self._CertCaContent

    @CertCaContent.setter
    def CertCaContent(self, CertCaContent):
        self._CertCaContent = CertCaContent

    @property
    def Bandwidth(self):
        r"""用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ForwardProtocol(self):
        r"""转发协议。当Protocol为https时并且SslMode为1或2时，有意义。可选的值为0：https，1：spdy，2：http2，3：spdy+http2。
        :rtype: int
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol


    def _deserialize(self, params):
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Protocol = params.get("Protocol")
        self._ListenerName = params.get("ListenerName")
        self._SslMode = params.get("SslMode")
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._CertContent = params.get("CertContent")
        self._CertKey = params.get("CertKey")
        self._CertCaId = params.get("CertCaId")
        self._CertCaName = params.get("CertCaName")
        self._CertCaContent = params.get("CertCaContent")
        self._Bandwidth = params.get("Bandwidth")
        self._ForwardProtocol = params.get("ForwardProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7ListenersRequest(AbstractModel):
    r"""CreateL7Listeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param _ListenerSet: 七层监听器信息数组，可以创建多个七层监听器。目前一个负载均衡下面最多允许创建50个七层监听器。
        :type ListenerSet: list of CreateL7Listener
        """
        self._LoadBalancerId = None
        self._ListenerSet = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerSet(self):
        r"""七层监听器信息数组，可以创建多个七层监听器。目前一个负载均衡下面最多允许创建50个七层监听器。
        :rtype: list of CreateL7Listener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = CreateL7Listener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7ListenersResponse(AbstractModel):
    r"""CreateL7Listeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerIds: 新建的负载均衡七层监听器的唯一ID列表。
        :type ListenerIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerIds = None
        self._RequestId = None

    @property
    def ListenerIds(self):
        r"""新建的负载均衡七层监听器的唯一ID列表。
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListenerIds = params.get("ListenerIds")
        self._RequestId = params.get("RequestId")


class CreateL7Rule(AbstractModel):
    r"""用于创建七层监听器的转发规则的信息。目前一个七层监听器下面最多允许创建50个七层转发域名，而每一个转发域名下最多可以创建100个转发规则。

    """

    def __init__(self):
        r"""
        :param _Domain: 七层转发规则的转发域名。
        :type Domain: str
        :param _Url: 七层转发规则的转发路径。
        :type Url: str
        :param _SessionExpire: 会话保持时间，单位：秒。可选值：30~3600。默认值0，表示不开启会话保持。
        :type SessionExpire: int
        :param _HealthSwitch: 健康检查开关：1（开启）、0（关闭）。默认值0，表示关闭。
        :type HealthSwitch: int
        :param _IntervalTime: 健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。
        :type IntervalTime: int
        :param _HealthNum: 健康检查健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :type HealthNum: int
        :param _UnhealthNum: 健康检查不健康阈值，默认值：5，表示当连续探测五次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :type UnhealthNum: int
        :param _HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :type HttpCodes: list of int non-negative
        :param _HttpCheckPath: 健康检查检查路径。
        :type HttpCheckPath: str
        :param _HttpCheckDomain: 健康检查检查域名。如果创建规则的域名使用通配符或正则表达式，则健康检查检查域名可自定义，否则必须跟健康检查检查域名一样。
        :type HttpCheckDomain: str
        :param _BalanceMode: 均衡方式：ip_hash、wrr。默认值wrr。
        :type BalanceMode: str
        """
        self._Domain = None
        self._Url = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._HttpCodes = None
        self._HttpCheckPath = None
        self._HttpCheckDomain = None
        self._BalanceMode = None

    @property
    def Domain(self):
        r"""七层转发规则的转发域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        r"""七层转发规则的转发路径。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def SessionExpire(self):
        r"""会话保持时间，单位：秒。可选值：30~3600。默认值0，表示不开启会话保持。
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""健康检查开关：1（开启）、0（关闭）。默认值0，表示关闭。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def IntervalTime(self):
        r"""健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""健康检查健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""健康检查不健康阈值，默认值：5，表示当连续探测五次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def HttpCodes(self):
        r"""健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :rtype: list of int non-negative
        """
        return self._HttpCodes

    @HttpCodes.setter
    def HttpCodes(self, HttpCodes):
        self._HttpCodes = HttpCodes

    @property
    def HttpCheckPath(self):
        r"""健康检查检查路径。
        :rtype: str
        """
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def HttpCheckDomain(self):
        r"""健康检查检查域名。如果创建规则的域名使用通配符或正则表达式，则健康检查检查域名可自定义，否则必须跟健康检查检查域名一样。
        :rtype: str
        """
        return self._HttpCheckDomain

    @HttpCheckDomain.setter
    def HttpCheckDomain(self, HttpCheckDomain):
        self._HttpCheckDomain = HttpCheckDomain

    @property
    def BalanceMode(self):
        r"""均衡方式：ip_hash、wrr。默认值wrr。
        :rtype: str
        """
        return self._BalanceMode

    @BalanceMode.setter
    def BalanceMode(self, BalanceMode):
        self._BalanceMode = BalanceMode


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._HttpCodes = params.get("HttpCodes")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._HttpCheckDomain = params.get("HttpCheckDomain")
        self._BalanceMode = params.get("BalanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesRequest(AbstractModel):
    r"""CreateL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _RuleSet: 七层转发规则信息数组，可以创建多个七层转发规则。目前一个七层监听器下面最多允许创建50个七层转发域名，而每一个转发域名下最多可以创建100个转发规则。目前只能单条创建，不能批量创建。
        :type RuleSet: list of CreateL7Rule
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._RuleSet = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RuleSet(self):
        r"""七层转发规则信息数组，可以创建多个七层转发规则。目前一个七层监听器下面最多允许创建50个七层转发域名，而每一个转发域名下最多可以创建100个转发规则。目前只能单条创建，不能批量创建。
        :rtype: list of CreateL7Rule
        """
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = CreateL7Rule()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesResponse(AbstractModel):
    r"""CreateL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancerBzConf(AbstractModel):
    r"""用于创建负载均衡的个性化配置。

    """

    def __init__(self):
        r"""
        :param _BzPayMode: 按月/按小时计费。
        :type BzPayMode: str
        :param _BzL4Metrics: 四层可选按带宽，连接数衡量。
        :type BzL4Metrics: str
        :param _BzL7Metrics: 七层可选按qps衡量。
        :type BzL7Metrics: str
        """
        self._BzPayMode = None
        self._BzL4Metrics = None
        self._BzL7Metrics = None

    @property
    def BzPayMode(self):
        r"""按月/按小时计费。
        :rtype: str
        """
        return self._BzPayMode

    @BzPayMode.setter
    def BzPayMode(self, BzPayMode):
        self._BzPayMode = BzPayMode

    @property
    def BzL4Metrics(self):
        r"""四层可选按带宽，连接数衡量。
        :rtype: str
        """
        return self._BzL4Metrics

    @BzL4Metrics.setter
    def BzL4Metrics(self, BzL4Metrics):
        self._BzL4Metrics = BzL4Metrics

    @property
    def BzL7Metrics(self):
        r"""七层可选按qps衡量。
        :rtype: str
        """
        return self._BzL7Metrics

    @BzL7Metrics.setter
    def BzL7Metrics(self, BzL7Metrics):
        self._BzL7Metrics = BzL7Metrics


    def _deserialize(self, params):
        self._BzPayMode = params.get("BzPayMode")
        self._BzL4Metrics = params.get("BzL4Metrics")
        self._BzL7Metrics = params.get("BzL7Metrics")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancersRequest(AbstractModel):
    r"""CreateLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 黑石负载均衡实例所属的私有网络ID。
        :type VpcId: str
        :param _LoadBalancerType: 负载均衡的类型，取值为open或internal。open表示公网(有日租)，internal表示内网。
        :type LoadBalancerType: str
        :param _SubnetId: 在私有网络内购买内网负载均衡实例的时候需要指定子网ID，内网负载均衡实例的VIP将从这个子网中产生。其他情况不用填写该字段。
        :type SubnetId: str
        :param _ProjectId: 负载均衡所属项目ID。不填则属于默认项目。
        :type ProjectId: int
        :param _GoodsNum: 购买黑石负载均衡实例的数量。默认值为1, 最大值为20。
        :type GoodsNum: int
        :param _PayMode: 黑石负载均衡的计费模式，取值为flow和bandwidth，其中flow模式表示流量模式，bandwidth表示带宽模式。默认值为flow。
        :type PayMode: str
        :param _TgwSetType: 负载均衡对应的TGW集群类别，取值为tunnel、fullnat或dnat。tunnel表示隧道集群，fullnat表示FULLNAT集群（普通外网负载均衡），dnat表示DNAT集群（增强型外网负载均衡）。默认值为fullnat。如需获取client IP，可以选择 tunnel 模式，fullnat 模式（tcp 通过toa 获取），dnat 模式。
        :type TgwSetType: str
        :param _Exclusive: 负载均衡的独占类别，取值为0表示非独占，1表示四层独占，2表示七层独占，3表示四层和七层独占，4表示共享容灾。
        :type Exclusive: int
        :param _SpecifiedVips: 指定的VIP，如果指定，则数量必须与goodsNum一致。如果不指定，则由后台分配随机VIP。
        :type SpecifiedVips: list of str
        :param _BzConf: （未全地域开放）保障型负载均衡设定参数，如果类别选择保障型则需传入此参数。
        :type BzConf: :class:`tencentcloud.bmlb.v20180625.models.CreateLoadBalancerBzConf`
        :param _IpProtocolType: IP协议类型。可取的值为“ipv4”或“ipv6”。
        :type IpProtocolType: str
        """
        self._VpcId = None
        self._LoadBalancerType = None
        self._SubnetId = None
        self._ProjectId = None
        self._GoodsNum = None
        self._PayMode = None
        self._TgwSetType = None
        self._Exclusive = None
        self._SpecifiedVips = None
        self._BzConf = None
        self._IpProtocolType = None

    @property
    def VpcId(self):
        r"""黑石负载均衡实例所属的私有网络ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def LoadBalancerType(self):
        r"""负载均衡的类型，取值为open或internal。open表示公网(有日租)，internal表示内网。
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def SubnetId(self):
        r"""在私有网络内购买内网负载均衡实例的时候需要指定子网ID，内网负载均衡实例的VIP将从这个子网中产生。其他情况不用填写该字段。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        r"""负载均衡所属项目ID。不填则属于默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        r"""购买黑石负载均衡实例的数量。默认值为1, 最大值为20。
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def PayMode(self):
        r"""黑石负载均衡的计费模式，取值为flow和bandwidth，其中flow模式表示流量模式，bandwidth表示带宽模式。默认值为flow。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TgwSetType(self):
        r"""负载均衡对应的TGW集群类别，取值为tunnel、fullnat或dnat。tunnel表示隧道集群，fullnat表示FULLNAT集群（普通外网负载均衡），dnat表示DNAT集群（增强型外网负载均衡）。默认值为fullnat。如需获取client IP，可以选择 tunnel 模式，fullnat 模式（tcp 通过toa 获取），dnat 模式。
        :rtype: str
        """
        return self._TgwSetType

    @TgwSetType.setter
    def TgwSetType(self, TgwSetType):
        self._TgwSetType = TgwSetType

    @property
    def Exclusive(self):
        r"""负载均衡的独占类别，取值为0表示非独占，1表示四层独占，2表示七层独占，3表示四层和七层独占，4表示共享容灾。
        :rtype: int
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def SpecifiedVips(self):
        r"""指定的VIP，如果指定，则数量必须与goodsNum一致。如果不指定，则由后台分配随机VIP。
        :rtype: list of str
        """
        return self._SpecifiedVips

    @SpecifiedVips.setter
    def SpecifiedVips(self, SpecifiedVips):
        self._SpecifiedVips = SpecifiedVips

    @property
    def BzConf(self):
        r"""（未全地域开放）保障型负载均衡设定参数，如果类别选择保障型则需传入此参数。
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateLoadBalancerBzConf`
        """
        return self._BzConf

    @BzConf.setter
    def BzConf(self, BzConf):
        self._BzConf = BzConf

    @property
    def IpProtocolType(self):
        r"""IP协议类型。可取的值为“ipv4”或“ipv6”。
        :rtype: str
        """
        return self._IpProtocolType

    @IpProtocolType.setter
    def IpProtocolType(self, IpProtocolType):
        self._IpProtocolType = IpProtocolType


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._PayMode = params.get("PayMode")
        self._TgwSetType = params.get("TgwSetType")
        self._Exclusive = params.get("Exclusive")
        self._SpecifiedVips = params.get("SpecifiedVips")
        if params.get("BzConf") is not None:
            self._BzConf = CreateLoadBalancerBzConf()
            self._BzConf._deserialize(params.get("BzConf"))
        self._IpProtocolType = params.get("IpProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancersResponse(AbstractModel):
    r"""CreateLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 创建的黑石负载均衡实例ID。
        :type LoadBalancerIds: list of str
        :param _TaskId: 创建负载均衡的异步任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerIds = None
        self._TaskId = None
        self._RequestId = None

    @property
    def LoadBalancerIds(self):
        r"""创建的黑石负载均衡实例ID。
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def TaskId(self):
        r"""创建负载均衡的异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateTrafficMirrorRequest(AbstractModel):
    r"""CreateTrafficMirror请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 流量镜像实例别名。
        :type Alias: str
        :param _VpcId: 流量镜像实例所属的私有网络ID，形如：vpc-xxx。
        :type VpcId: str
        """
        self._Alias = None
        self._VpcId = None

    @property
    def Alias(self):
        r"""流量镜像实例别名。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def VpcId(self):
        r"""流量镜像实例所属的私有网络ID，形如：vpc-xxx。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrafficMirrorResponse(AbstractModel):
    r"""CreateTrafficMirror返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID
        :type TrafficMirrorId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrafficMirrorId = None
        self._RequestId = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._RequestId = params.get("RequestId")


class DeleteL7DomainsRequest(AbstractModel):
    r"""DeleteL7Domains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _DomainIds: 转发域名实例ID列表，可通过接口DescribeL7Rules查询。
        :type DomainIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainIds = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainIds(self):
        r"""转发域名实例ID列表，可通过接口DescribeL7Rules查询。
        :rtype: list of str
        """
        return self._DomainIds

    @DomainIds.setter
    def DomainIds(self, DomainIds):
        self._DomainIds = DomainIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainIds = params.get("DomainIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL7DomainsResponse(AbstractModel):
    r"""DeleteL7Domains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteL7RulesRequest(AbstractModel):
    r"""DeleteL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。
        :type DomainId: str
        :param _LocationIds: 转发路径实例ID列表，可通过接口DescribeL7Rules查询。
        :type LocationIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainId = None
        self._LocationIds = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainId(self):
        r"""转发域名实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LocationIds(self):
        r"""转发路径实例ID列表，可通过接口DescribeL7Rules查询。
        :rtype: list of str
        """
        return self._LocationIds

    @LocationIds.setter
    def LocationIds(self, LocationIds):
        self._LocationIds = LocationIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainId = params.get("DomainId")
        self._LocationIds = params.get("LocationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL7RulesResponse(AbstractModel):
    r"""DeleteL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteListenersRequest(AbstractModel):
    r"""DeleteListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerIds: 待删除的负载均衡四层和七层监听器ID列表，可通过接口DescribeL4Listeners和DescribeL7Listeners查询。目前同时只能删除一种类型的监听器，并且删除七层监听器的数量上限为一个。
        :type ListenerIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerIds = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        r"""待删除的负载均衡四层和七层监听器ID列表，可通过接口DescribeL4Listeners和DescribeL7Listeners查询。目前同时只能删除一种类型的监听器，并且删除七层监听器的数量上限为一个。
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenersResponse(AbstractModel):
    r"""DeleteListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    r"""DeleteLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        """
        self._LoadBalancerId = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    r"""DeleteLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteTrafficMirrorRequest(AbstractModel):
    r"""DeleteTrafficMirror请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorIds: 流量镜像实例ID数组，可以批量删除，每次删除上限为20
        :type TrafficMirrorIds: list of str
        """
        self._TrafficMirrorIds = None

    @property
    def TrafficMirrorIds(self):
        r"""流量镜像实例ID数组，可以批量删除，每次删除上限为20
        :rtype: list of str
        """
        return self._TrafficMirrorIds

    @TrafficMirrorIds.setter
    def TrafficMirrorIds(self, TrafficMirrorIds):
        self._TrafficMirrorIds = TrafficMirrorIds


    def _deserialize(self, params):
        self._TrafficMirrorIds = params.get("TrafficMirrorIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTrafficMirrorResponse(AbstractModel):
    r"""DeleteTrafficMirror返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeCertDetailRequest(AbstractModel):
    r"""DescribeCertDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: 证书ID。
        :type CertId: str
        """
        self._CertId = None

    @property
    def CertId(self):
        r"""证书ID。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertDetailResponse(AbstractModel):
    r"""DescribeCertDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: 证书ID。
        :type CertId: str
        :param _CertName: 证书名称。
        :type CertName: str
        :param _CertType: 证书类型（SVR=服务器证书，CA=客户端证书）。
        :type CertType: str
        :param _CertContent: 证书内容。
        :type CertContent: str
        :param _CertDomain: 证书主域名。
        :type CertDomain: str
        :param _CertSubjectDomain: 证书子域名列表。
        :type CertSubjectDomain: list of str
        :param _CertUploadTime: 证书上传时间。
        :type CertUploadTime: str
        :param _CertBeginTime: 证书生效时间。
        :type CertBeginTime: str
        :param _CertEndTime: 证书失效时间。
        :type CertEndTime: str
        :param _CertLoadBalancerSet: 该证书关联的黑石负载均衡对象列表。
        :type CertLoadBalancerSet: list of CertDetailLoadBalancer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertId = None
        self._CertName = None
        self._CertType = None
        self._CertContent = None
        self._CertDomain = None
        self._CertSubjectDomain = None
        self._CertUploadTime = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._CertLoadBalancerSet = None
        self._RequestId = None

    @property
    def CertId(self):
        r"""证书ID。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        r"""证书名称。
        :rtype: str
        """
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertType(self):
        r"""证书类型（SVR=服务器证书，CA=客户端证书）。
        :rtype: str
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def CertContent(self):
        r"""证书内容。
        :rtype: str
        """
        return self._CertContent

    @CertContent.setter
    def CertContent(self, CertContent):
        self._CertContent = CertContent

    @property
    def CertDomain(self):
        r"""证书主域名。
        :rtype: str
        """
        return self._CertDomain

    @CertDomain.setter
    def CertDomain(self, CertDomain):
        self._CertDomain = CertDomain

    @property
    def CertSubjectDomain(self):
        r"""证书子域名列表。
        :rtype: list of str
        """
        return self._CertSubjectDomain

    @CertSubjectDomain.setter
    def CertSubjectDomain(self, CertSubjectDomain):
        self._CertSubjectDomain = CertSubjectDomain

    @property
    def CertUploadTime(self):
        r"""证书上传时间。
        :rtype: str
        """
        return self._CertUploadTime

    @CertUploadTime.setter
    def CertUploadTime(self, CertUploadTime):
        self._CertUploadTime = CertUploadTime

    @property
    def CertBeginTime(self):
        r"""证书生效时间。
        :rtype: str
        """
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        r"""证书失效时间。
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def CertLoadBalancerSet(self):
        r"""该证书关联的黑石负载均衡对象列表。
        :rtype: list of CertDetailLoadBalancer
        """
        return self._CertLoadBalancerSet

    @CertLoadBalancerSet.setter
    def CertLoadBalancerSet(self, CertLoadBalancerSet):
        self._CertLoadBalancerSet = CertLoadBalancerSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._CertType = params.get("CertType")
        self._CertContent = params.get("CertContent")
        self._CertDomain = params.get("CertDomain")
        self._CertSubjectDomain = params.get("CertSubjectDomain")
        self._CertUploadTime = params.get("CertUploadTime")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        if params.get("CertLoadBalancerSet") is not None:
            self._CertLoadBalancerSet = []
            for item in params.get("CertLoadBalancerSet"):
                obj = CertDetailLoadBalancer()
                obj._deserialize(item)
                self._CertLoadBalancerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDevicesBindInfoRequest(AbstractModel):
    r"""DescribeDevicesBindInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 黑石私有网络唯一ID。
        :type VpcId: str
        :param _InstanceIds: 主机ID或虚机IP列表，可用于获取绑定了该主机的负载均衡列表。
        :type InstanceIds: list of str
        """
        self._VpcId = None
        self._InstanceIds = None

    @property
    def VpcId(self):
        r"""黑石私有网络唯一ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def InstanceIds(self):
        r"""主机ID或虚机IP列表，可用于获取绑定了该主机的负载均衡列表。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesBindInfoResponse(AbstractModel):
    r"""DescribeDevicesBindInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerSet: 返回的负载均衡绑定信息。
        :type LoadBalancerSet: list of DevicesBindInfoLoadBalancer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerSet = None
        self._RequestId = None

    @property
    def LoadBalancerSet(self):
        r"""返回的负载均衡绑定信息。
        :rtype: list of DevicesBindInfoLoadBalancer
        """
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = DevicesBindInfoLoadBalancer()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL4Backend(AbstractModel):
    r"""待查询四层监听器绑定的主机信息。

    """

    def __init__(self):
        r"""
        :param _Port: 待绑定的主机端口，可选值1~65535。
        :type Port: int
        :param _InstanceId: 黑石物理机的主机ID。
        :type InstanceId: str
        """
        self._Port = None
        self._InstanceId = None

    @property
    def Port(self):
        r"""待绑定的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        r"""黑石物理机的主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4BackendsRequest(AbstractModel):
    r"""DescribeL4Backends请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。
        :type ListenerId: str
        :param _BackendSet: 待查询的主机信息。
        :type BackendSet: list of DescribeL4Backend
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._BackendSet = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def BackendSet(self):
        r"""待查询的主机信息。
        :rtype: list of DescribeL4Backend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = DescribeL4Backend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4BackendsResponse(AbstractModel):
    r"""DescribeL4Backends返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackendSet: 返回的绑定关系列表。
        :type BackendSet: list of L4Backend
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackendSet = None
        self._RequestId = None

    @property
    def BackendSet(self):
        r"""返回的绑定关系列表。
        :rtype: list of L4Backend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = L4Backend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL4ListenerInfoRequest(AbstractModel):
    r"""DescribeL4ListenerInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _SearchKey: 查找的键值，可用于模糊查找该名称的监听器。
        :type SearchKey: str
        :param _InstanceIds: 主机ID或虚机IP列表，可用于获取绑定了该主机的监听器。
        :type InstanceIds: list of str
        """
        self._LoadBalancerId = None
        self._SearchKey = None
        self._InstanceIds = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SearchKey(self):
        r"""查找的键值，可用于模糊查找该名称的监听器。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def InstanceIds(self):
        r"""主机ID或虚机IP列表，可用于获取绑定了该主机的监听器。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SearchKey = params.get("SearchKey")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4ListenerInfoResponse(AbstractModel):
    r"""DescribeL4ListenerInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerSet: 返回的四层监听器列表。
        :type ListenerSet: list of L4ListenerInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerSet = None
        self._RequestId = None

    @property
    def ListenerSet(self):
        r"""返回的四层监听器列表。
        :rtype: list of L4ListenerInfo
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L4ListenerInfo()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL4ListenersRequest(AbstractModel):
    r"""DescribeL4Listeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerIds: 四层监听器实例ID数组，可通过接口DescribeL4Listeners查询。
        :type ListenerIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerIds = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        r"""四层监听器实例ID数组，可通过接口DescribeL4Listeners查询。
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4ListenersResponse(AbstractModel):
    r"""DescribeL4Listeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerSet: 监听器信息数组。
        :type ListenerSet: list of L4Listener
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerSet = None
        self._RequestId = None

    @property
    def ListenerSet(self):
        r"""监听器信息数组。
        :rtype: list of L4Listener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L4Listener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL7BackendsRequest(AbstractModel):
    r"""DescribeL7Backends请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。
        :type DomainId: str
        :param _LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。
        :type LocationId: str
        :param _QueryType: 查询条件，传'all'则查询所有与规则绑定的主机信息。如果为all时，DomainId和LocationId参数没有意义不必传入，否则DomainId和LocationId参数必须传入。
        :type QueryType: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainId = None
        self._LocationId = None
        self._QueryType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainId(self):
        r"""转发域名实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LocationId(self):
        r"""转发路径实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def QueryType(self):
        r"""查询条件，传'all'则查询所有与规则绑定的主机信息。如果为all时，DomainId和LocationId参数没有意义不必传入，否则DomainId和LocationId参数必须传入。
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainId = params.get("DomainId")
        self._LocationId = params.get("LocationId")
        self._QueryType = params.get("QueryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7BackendsResponse(AbstractModel):
    r"""DescribeL7Backends返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackendSet: 返回的绑定关系列表。
        :type BackendSet: list of L7Backend
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackendSet = None
        self._RequestId = None

    @property
    def BackendSet(self):
        r"""返回的绑定关系列表。
        :rtype: list of L7Backend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = L7Backend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL7ListenerInfoRequest(AbstractModel):
    r"""DescribeL7ListenerInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _SearchKey: 查找的键值，可用于模糊查找有该转发域名的监听器。
        :type SearchKey: str
        :param _InstanceIds: 主机ID或虚机IP列表，可用于获取绑定了该主机的监听器。
        :type InstanceIds: list of str
        :param _IfGetBackendInfo: 是否获取转发规则下的主机信息。默认为0，不获取。
        :type IfGetBackendInfo: int
        """
        self._LoadBalancerId = None
        self._SearchKey = None
        self._InstanceIds = None
        self._IfGetBackendInfo = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SearchKey(self):
        r"""查找的键值，可用于模糊查找有该转发域名的监听器。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def InstanceIds(self):
        r"""主机ID或虚机IP列表，可用于获取绑定了该主机的监听器。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def IfGetBackendInfo(self):
        r"""是否获取转发规则下的主机信息。默认为0，不获取。
        :rtype: int
        """
        return self._IfGetBackendInfo

    @IfGetBackendInfo.setter
    def IfGetBackendInfo(self, IfGetBackendInfo):
        self._IfGetBackendInfo = IfGetBackendInfo


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SearchKey = params.get("SearchKey")
        self._InstanceIds = params.get("InstanceIds")
        self._IfGetBackendInfo = params.get("IfGetBackendInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7ListenerInfoResponse(AbstractModel):
    r"""DescribeL7ListenerInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerSet: 返回的七层监听器列表。
        :type ListenerSet: list of L7ListenerInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerSet = None
        self._RequestId = None

    @property
    def ListenerSet(self):
        r"""返回的七层监听器列表。
        :rtype: list of L7ListenerInfo
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L7ListenerInfo()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL7ListenersExRequest(AbstractModel):
    r"""DescribeL7ListenersEx请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 返回的监听器中标识是否绑定在此流量镜像中。
        :type TrafficMirrorId: str
        :param _VpcId: 待获取监听器所在的VPC的ID。
        :type VpcId: str
        :param _Offset: 此VPC中获取负载均衡的偏移。
        :type Offset: int
        :param _Limit: 此VPC中获取负载均衡的数量。
        :type Limit: int
        :param _Filters: 过滤条件。
LoadBalancerId - String - （过滤条件）负载均衡ID。
LoadBalancerName - String - （过滤条件）负载均衡名称。
Vip - String - （过滤条件）VIP。
ListenerId - String - （过滤条件）监听器ID。
ListenerName -  String - （过滤条件）监听器名称。
Protocol -  String - （过滤条件）七层协议。
LoadBalancerPort -  String - （过滤条件）监听器端口。
        :type Filters: list of Filter
        """
        self._TrafficMirrorId = None
        self._VpcId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def TrafficMirrorId(self):
        r"""返回的监听器中标识是否绑定在此流量镜像中。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def VpcId(self):
        r"""待获取监听器所在的VPC的ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Offset(self):
        r"""此VPC中获取负载均衡的偏移。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""此VPC中获取负载均衡的数量。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件。
LoadBalancerId - String - （过滤条件）负载均衡ID。
LoadBalancerName - String - （过滤条件）负载均衡名称。
Vip - String - （过滤条件）VIP。
ListenerId - String - （过滤条件）监听器ID。
ListenerName -  String - （过滤条件）监听器名称。
Protocol -  String - （过滤条件）七层协议。
LoadBalancerPort -  String - （过滤条件）监听器端口。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._VpcId = params.get("VpcId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7ListenersExResponse(AbstractModel):
    r"""DescribeL7ListenersEx返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 此指定VPC中负载均衡的总数。
        :type TotalCount: int
        :param _ListenerSet: 符合条件的监听器。
        :type ListenerSet: list of L7ExListener
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""此指定VPC中负载均衡的总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        r"""符合条件的监听器。
        :rtype: list of L7ExListener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L7ExListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL7ListenersRequest(AbstractModel):
    r"""DescribeL7Listeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerIds: 七层监听器实例ID列表，可通过接口DescribeL7Listeners查询。
        :type ListenerIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerIds = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        r"""七层监听器实例ID列表，可通过接口DescribeL7Listeners查询。
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7ListenersResponse(AbstractModel):
    r"""DescribeL7Listeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerSet: 返回的七层监听器列表。
        :type ListenerSet: list of L7Listener
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerSet = None
        self._RequestId = None

    @property
    def ListenerSet(self):
        r"""返回的七层监听器列表。
        :rtype: list of L7Listener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L7Listener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL7RulesRequest(AbstractModel):
    r"""DescribeL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _DomainIds: 转发域名ID列表，可通过接口DescribeL7Rules查询。
        :type DomainIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainIds = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainIds(self):
        r"""转发域名ID列表，可通过接口DescribeL7Rules查询。
        :rtype: list of str
        """
        return self._DomainIds

    @DomainIds.setter
    def DomainIds(self, DomainIds):
        self._DomainIds = DomainIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainIds = params.get("DomainIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7RulesResponse(AbstractModel):
    r"""DescribeL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleSet: 返回的转发规则列表。
        :type RuleSet: list of L7Rule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleSet = None
        self._RequestId = None

    @property
    def RuleSet(self):
        r"""返回的转发规则列表。
        :rtype: list of L7Rule
        """
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = L7Rule()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerPortInfoRequest(AbstractModel):
    r"""DescribeLoadBalancerPortInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        """
        self._LoadBalancerId = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerPortInfoResponse(AbstractModel):
    r"""DescribeLoadBalancerPortInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerSet: 返回的监听器列表（四层和七层）。
        :type ListenerSet: list of LoadBalancerPortInfoListener
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerSet = None
        self._RequestId = None

    @property
    def ListenerSet(self):
        r"""返回的监听器列表（四层和七层）。
        :rtype: list of LoadBalancerPortInfoListener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = LoadBalancerPortInfoListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerTaskResultRequest(AbstractModel):
    r"""DescribeLoadBalancerTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。由具体的异步操作接口提供。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID。由具体的异步操作接口提供。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerTaskResultResponse(AbstractModel):
    r"""DescribeLoadBalancerTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务当前状态。0：成功，1：失败，2：进行中。
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务当前状态。0：成功，1：失败，2：进行中。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    r"""DescribeLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 负载均衡器ID数组
        :type LoadBalancerIds: list of str
        :param _LoadBalancerType: 负载均衡的类型 : open表示公网LB类型，internal表示内网LB类型
        :type LoadBalancerType: str
        :param _LoadBalancerName: 负载均衡器名称
        :type LoadBalancerName: str
        :param _Domain: 负载均衡域名。规则：1-60个小写英文字母、数字、点号“.”或连接线“-”。内网类型的负载均衡不能配置该字段
        :type Domain: str
        :param _LoadBalancerVips: 负载均衡获得的公网IP地址,支持多个
        :type LoadBalancerVips: list of str
        :param _Offset: 数据偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数据长度，默认为20
        :type Limit: int
        :param _SearchKey: 模糊查找名称、域名、VIP
        :type SearchKey: str
        :param _OrderBy: 排序字段，支持：loadBalancerName,createTime,domain,loadBalancerType
        :type OrderBy: str
        :param _OrderType: 1倒序，0顺序，默认顺序
        :type OrderType: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Exclusive: 是否筛选独占集群，0表示非独占集群，1表示四层独占集群，2表示七层独占集群，3表示四层和七层独占集群，4表示共享容灾
        :type Exclusive: int
        :param _TgwSetType: 该负载均衡对应的tgw集群（fullnat,tunnel,dnat）
        :type TgwSetType: str
        :param _VpcId: 该负载均衡对应的所在的私有网络ID
        :type VpcId: str
        :param _QueryType: 'CONFLIST' 查询带confId的LB列表，'CONFID' 查询某个confId绑定的LB列表
        :type QueryType: str
        :param _ConfId: 个性化配置ID
        :type ConfId: str
        """
        self._LoadBalancerIds = None
        self._LoadBalancerType = None
        self._LoadBalancerName = None
        self._Domain = None
        self._LoadBalancerVips = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._OrderBy = None
        self._OrderType = None
        self._ProjectId = None
        self._Exclusive = None
        self._TgwSetType = None
        self._VpcId = None
        self._QueryType = None
        self._ConfId = None

    @property
    def LoadBalancerIds(self):
        r"""负载均衡器ID数组
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def LoadBalancerType(self):
        r"""负载均衡的类型 : open表示公网LB类型，internal表示内网LB类型
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def LoadBalancerName(self):
        r"""负载均衡器名称
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Domain(self):
        r"""负载均衡域名。规则：1-60个小写英文字母、数字、点号“.”或连接线“-”。内网类型的负载均衡不能配置该字段
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerVips(self):
        r"""负载均衡获得的公网IP地址,支持多个
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def Offset(self):
        r"""数据偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数据长度，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        r"""模糊查找名称、域名、VIP
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def OrderBy(self):
        r"""排序字段，支持：loadBalancerName,createTime,domain,loadBalancerType
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""1倒序，0顺序，默认顺序
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Exclusive(self):
        r"""是否筛选独占集群，0表示非独占集群，1表示四层独占集群，2表示七层独占集群，3表示四层和七层独占集群，4表示共享容灾
        :rtype: int
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def TgwSetType(self):
        r"""该负载均衡对应的tgw集群（fullnat,tunnel,dnat）
        :rtype: str
        """
        return self._TgwSetType

    @TgwSetType.setter
    def TgwSetType(self, TgwSetType):
        self._TgwSetType = TgwSetType

    @property
    def VpcId(self):
        r"""该负载均衡对应的所在的私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def QueryType(self):
        r"""'CONFLIST' 查询带confId的LB列表，'CONFID' 查询某个confId绑定的LB列表
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def ConfId(self):
        r"""个性化配置ID
        :rtype: str
        """
        return self._ConfId

    @ConfId.setter
    def ConfId(self, ConfId):
        self._ConfId = ConfId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Domain = params.get("Domain")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._ProjectId = params.get("ProjectId")
        self._Exclusive = params.get("Exclusive")
        self._TgwSetType = params.get("TgwSetType")
        self._VpcId = params.get("VpcId")
        self._QueryType = params.get("QueryType")
        self._ConfId = params.get("ConfId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    r"""DescribeLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerSet: 返回负载均衡信息列表。
        :type LoadBalancerSet: list of LoadBalancer
        :param _TotalCount: 符合条件的负载均衡总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LoadBalancerSet(self):
        r"""返回负载均衡信息列表。
        :rtype: list of LoadBalancer
        """
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def TotalCount(self):
        r"""符合条件的负载均衡总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTrafficMirrorListenersRequest(AbstractModel):
    r"""DescribeTrafficMirrorListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID。
        :type TrafficMirrorId: str
        :param _Offset: 分页的偏移量，也即从第几条记录开始查询
        :type Offset: int
        :param _Limit: 单次查询返回的条目数，默认值：500。
        :type Limit: int
        :param _SearchLoadBalancerIds: 待搜索的负载均衡Id。
        :type SearchLoadBalancerIds: list of str
        :param _SearchLoadBalancerNames: 待搜索的负载均衡名称。
        :type SearchLoadBalancerNames: list of str
        :param _SearchVips: 待搜索的Vip。
        :type SearchVips: list of str
        :param _SearchListenerIds: 待搜索的监听器ID。
        :type SearchListenerIds: list of str
        :param _SearchListenerNames: 待搜索的监听器名称。
        :type SearchListenerNames: list of str
        :param _SearchProtocols: 待搜索的协议名称。
        :type SearchProtocols: list of str
        :param _SearchLoadBalancerPorts: 待搜索的端口。
        :type SearchLoadBalancerPorts: list of int non-negative
        """
        self._TrafficMirrorId = None
        self._Offset = None
        self._Limit = None
        self._SearchLoadBalancerIds = None
        self._SearchLoadBalancerNames = None
        self._SearchVips = None
        self._SearchListenerIds = None
        self._SearchListenerNames = None
        self._SearchProtocols = None
        self._SearchLoadBalancerPorts = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def Offset(self):
        r"""分页的偏移量，也即从第几条记录开始查询
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""单次查询返回的条目数，默认值：500。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchLoadBalancerIds(self):
        r"""待搜索的负载均衡Id。
        :rtype: list of str
        """
        return self._SearchLoadBalancerIds

    @SearchLoadBalancerIds.setter
    def SearchLoadBalancerIds(self, SearchLoadBalancerIds):
        self._SearchLoadBalancerIds = SearchLoadBalancerIds

    @property
    def SearchLoadBalancerNames(self):
        r"""待搜索的负载均衡名称。
        :rtype: list of str
        """
        return self._SearchLoadBalancerNames

    @SearchLoadBalancerNames.setter
    def SearchLoadBalancerNames(self, SearchLoadBalancerNames):
        self._SearchLoadBalancerNames = SearchLoadBalancerNames

    @property
    def SearchVips(self):
        r"""待搜索的Vip。
        :rtype: list of str
        """
        return self._SearchVips

    @SearchVips.setter
    def SearchVips(self, SearchVips):
        self._SearchVips = SearchVips

    @property
    def SearchListenerIds(self):
        r"""待搜索的监听器ID。
        :rtype: list of str
        """
        return self._SearchListenerIds

    @SearchListenerIds.setter
    def SearchListenerIds(self, SearchListenerIds):
        self._SearchListenerIds = SearchListenerIds

    @property
    def SearchListenerNames(self):
        r"""待搜索的监听器名称。
        :rtype: list of str
        """
        return self._SearchListenerNames

    @SearchListenerNames.setter
    def SearchListenerNames(self, SearchListenerNames):
        self._SearchListenerNames = SearchListenerNames

    @property
    def SearchProtocols(self):
        r"""待搜索的协议名称。
        :rtype: list of str
        """
        return self._SearchProtocols

    @SearchProtocols.setter
    def SearchProtocols(self, SearchProtocols):
        self._SearchProtocols = SearchProtocols

    @property
    def SearchLoadBalancerPorts(self):
        r"""待搜索的端口。
        :rtype: list of int non-negative
        """
        return self._SearchLoadBalancerPorts

    @SearchLoadBalancerPorts.setter
    def SearchLoadBalancerPorts(self, SearchLoadBalancerPorts):
        self._SearchLoadBalancerPorts = SearchLoadBalancerPorts


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchLoadBalancerIds = params.get("SearchLoadBalancerIds")
        self._SearchLoadBalancerNames = params.get("SearchLoadBalancerNames")
        self._SearchVips = params.get("SearchVips")
        self._SearchListenerIds = params.get("SearchListenerIds")
        self._SearchListenerNames = params.get("SearchListenerNames")
        self._SearchProtocols = params.get("SearchProtocols")
        self._SearchLoadBalancerPorts = params.get("SearchLoadBalancerPorts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorListenersResponse(AbstractModel):
    r"""DescribeTrafficMirrorListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerSet: 监听器列表。
        :type ListenerSet: list of TrafficMirrorListener
        :param _TotalCount: 监听器总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ListenerSet(self):
        r"""监听器列表。
        :rtype: list of TrafficMirrorListener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def TotalCount(self):
        r"""监听器总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = TrafficMirrorListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTrafficMirrorReceiver(AbstractModel):
    r"""流量镜像进行健康检查的接收机信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 物理机实例ID。
        :type InstanceId: str
        :param _Port: 物理机绑定的端口。
        :type Port: int
        """
        self._InstanceId = None
        self._Port = None

    @property
    def InstanceId(self):
        r"""物理机实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        r"""物理机绑定的端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorReceiverHealthStatusRequest(AbstractModel):
    r"""DescribeTrafficMirrorReceiverHealthStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 查询所在的流量镜像ID。
        :type TrafficMirrorId: str
        :param _ReceiverSet: 流量镜像接收机实例ID和端口数组。
        :type ReceiverSet: list of DescribeTrafficMirrorReceiver
        """
        self._TrafficMirrorId = None
        self._ReceiverSet = None

    @property
    def TrafficMirrorId(self):
        r"""查询所在的流量镜像ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def ReceiverSet(self):
        r"""流量镜像接收机实例ID和端口数组。
        :rtype: list of DescribeTrafficMirrorReceiver
        """
        return self._ReceiverSet

    @ReceiverSet.setter
    def ReceiverSet(self, ReceiverSet):
        self._ReceiverSet = ReceiverSet


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self._ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = DescribeTrafficMirrorReceiver()
                obj._deserialize(item)
                self._ReceiverSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorReceiverHealthStatusResponse(AbstractModel):
    r"""DescribeTrafficMirrorReceiverHealthStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReceiversStatusSet: 内网IP和端口对应的状态。
        :type ReceiversStatusSet: list of TrafficMirrorReciversStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReceiversStatusSet = None
        self._RequestId = None

    @property
    def ReceiversStatusSet(self):
        r"""内网IP和端口对应的状态。
        :rtype: list of TrafficMirrorReciversStatus
        """
        return self._ReceiversStatusSet

    @ReceiversStatusSet.setter
    def ReceiversStatusSet(self, ReceiversStatusSet):
        self._ReceiversStatusSet = ReceiversStatusSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReceiversStatusSet") is not None:
            self._ReceiversStatusSet = []
            for item in params.get("ReceiversStatusSet"):
                obj = TrafficMirrorReciversStatus()
                obj._deserialize(item)
                self._ReceiversStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrafficMirrorReceiversRequest(AbstractModel):
    r"""DescribeTrafficMirrorReceivers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID。
        :type TrafficMirrorId: str
        :param _InstanceIds: 接收机黑石物理机实例ID数组。
        :type InstanceIds: list of str
        :param _Ports: 接收机接收端口数组。
        :type Ports: list of int
        :param _Weights: 接收机实例权重数组。
        :type Weights: list of int
        :param _Offset: 分页的偏移量，也即从第几条记录开始查询
        :type Offset: int
        :param _Limit: 单次查询返回的条目数，默认值：500。
        :type Limit: int
        :param _VagueStr: 搜索instance或者alias
        :type VagueStr: str
        :param _VagueIp: 搜索IP
        :type VagueIp: str
        """
        self._TrafficMirrorId = None
        self._InstanceIds = None
        self._Ports = None
        self._Weights = None
        self._Offset = None
        self._Limit = None
        self._VagueStr = None
        self._VagueIp = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def InstanceIds(self):
        r"""接收机黑石物理机实例ID数组。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Ports(self):
        r"""接收机接收端口数组。
        :rtype: list of int
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Weights(self):
        r"""接收机实例权重数组。
        :rtype: list of int
        """
        return self._Weights

    @Weights.setter
    def Weights(self, Weights):
        self._Weights = Weights

    @property
    def Offset(self):
        r"""分页的偏移量，也即从第几条记录开始查询
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""单次查询返回的条目数，默认值：500。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def VagueStr(self):
        r"""搜索instance或者alias
        :rtype: str
        """
        return self._VagueStr

    @VagueStr.setter
    def VagueStr(self, VagueStr):
        self._VagueStr = VagueStr

    @property
    def VagueIp(self):
        r"""搜索IP
        :rtype: str
        """
        return self._VagueIp

    @VagueIp.setter
    def VagueIp(self, VagueIp):
        self._VagueIp = VagueIp


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._InstanceIds = params.get("InstanceIds")
        self._Ports = params.get("Ports")
        self._Weights = params.get("Weights")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._VagueStr = params.get("VagueStr")
        self._VagueIp = params.get("VagueIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorReceiversResponse(AbstractModel):
    r"""DescribeTrafficMirrorReceivers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReceiverSet: 接收机列表，具体结构描述如data结构所示。
        :type ReceiverSet: list of TrafficMirrorReceiver
        :param _TotalCount: 接收机总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReceiverSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ReceiverSet(self):
        r"""接收机列表，具体结构描述如data结构所示。
        :rtype: list of TrafficMirrorReceiver
        """
        return self._ReceiverSet

    @ReceiverSet.setter
    def ReceiverSet(self, ReceiverSet):
        self._ReceiverSet = ReceiverSet

    @property
    def TotalCount(self):
        r"""接收机总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReceiverSet") is not None:
            self._ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = TrafficMirrorReceiver()
                obj._deserialize(item)
                self._ReceiverSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTrafficMirrorsRequest(AbstractModel):
    r"""DescribeTrafficMirrors请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorIds: 流量镜像实例ID的数组，支持批量查询
        :type TrafficMirrorIds: list of str
        :param _Aliases: 流量镜像实例别名数组。
        :type Aliases: list of str
        :param _VpcIds: 流量镜像实例所属的私有网络ID数组，形如：vpc-xxx。
        :type VpcIds: list of str
        :param _Offset: 分页的偏移量，也即从第几条记录开始查询
        :type Offset: int
        :param _Limit: 单次查询返回的条目数，默认值：500。
        :type Limit: int
        :param _OrderField: 排序字段。trafficMirrorId或者createTime。
        :type OrderField: str
        :param _Order: 排序方式，取值：0:增序(默认)，1:降序
        :type Order: int
        :param _SearchKey: 模糊匹配trafficMirrorId或者alias字段。
        :type SearchKey: str
        """
        self._TrafficMirrorIds = None
        self._Aliases = None
        self._VpcIds = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None
        self._SearchKey = None

    @property
    def TrafficMirrorIds(self):
        r"""流量镜像实例ID的数组，支持批量查询
        :rtype: list of str
        """
        return self._TrafficMirrorIds

    @TrafficMirrorIds.setter
    def TrafficMirrorIds(self, TrafficMirrorIds):
        self._TrafficMirrorIds = TrafficMirrorIds

    @property
    def Aliases(self):
        r"""流量镜像实例别名数组。
        :rtype: list of str
        """
        return self._Aliases

    @Aliases.setter
    def Aliases(self, Aliases):
        self._Aliases = Aliases

    @property
    def VpcIds(self):
        r"""流量镜像实例所属的私有网络ID数组，形如：vpc-xxx。
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def Offset(self):
        r"""分页的偏移量，也即从第几条记录开始查询
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""单次查询返回的条目数，默认值：500。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        r"""排序字段。trafficMirrorId或者createTime。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""排序方式，取值：0:增序(默认)，1:降序
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SearchKey(self):
        r"""模糊匹配trafficMirrorId或者alias字段。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._TrafficMirrorIds = params.get("TrafficMirrorIds")
        self._Aliases = params.get("Aliases")
        self._VpcIds = params.get("VpcIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorsResponse(AbstractModel):
    r"""DescribeTrafficMirrors返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 流量镜像总数。
        :type TotalCount: int
        :param _TrafficMirrorSet: 对象数组。数组元素为流量镜像信息，具体结构描述如list结构所示。
        :type TrafficMirrorSet: list of TrafficMirror
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TrafficMirrorSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""流量镜像总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TrafficMirrorSet(self):
        r"""对象数组。数组元素为流量镜像信息，具体结构描述如list结构所示。
        :rtype: list of TrafficMirror
        """
        return self._TrafficMirrorSet

    @TrafficMirrorSet.setter
    def TrafficMirrorSet(self, TrafficMirrorSet):
        self._TrafficMirrorSet = TrafficMirrorSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TrafficMirrorSet") is not None:
            self._TrafficMirrorSet = []
            for item in params.get("TrafficMirrorSet"):
                obj = TrafficMirror()
                obj._deserialize(item)
                self._TrafficMirrorSet.append(obj)
        self._RequestId = params.get("RequestId")


class DevicesBindInfoBackend(AbstractModel):
    r"""获取设备绑定信息时返回的所绑定的主机信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 黑石物理机的主机ID、托管主机ID或虚拟机IP。
        :type InstanceId: str
        :param _Port: 主机端口。
        :type Port: int
        """
        self._InstanceId = None
        self._Port = None

    @property
    def InstanceId(self):
        r"""黑石物理机的主机ID、托管主机ID或虚拟机IP。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        r"""主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoL4Listener(AbstractModel):
    r"""获取设备绑定信息时返回的四层监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 七层监听器实例ID。
        :type ListenerId: str
        :param _Protocol: 七层监听器协议类型，可选值：http,https。
        :type Protocol: str
        :param _LoadBalancerPort: 七层监听器的监听端口。
        :type LoadBalancerPort: int
        :param _BackendSet: 该转发路径所绑定的主机列表。
        :type BackendSet: list of DevicesBindInfoBackend
        """
        self._ListenerId = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._BackendSet = None

    @property
    def ListenerId(self):
        r"""七层监听器实例ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        r"""七层监听器协议类型，可选值：http,https。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""七层监听器的监听端口。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def BackendSet(self):
        r"""该转发路径所绑定的主机列表。
        :rtype: list of DevicesBindInfoBackend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = DevicesBindInfoBackend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoL7Listener(AbstractModel):
    r"""获取设备绑定信息时返回的七层监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 七层监听器实例ID。
        :type ListenerId: str
        :param _Protocol: 七层监听器协议类型，可选值：http,https。
        :type Protocol: str
        :param _LoadBalancerPort: 七层监听器的监听端口。
        :type LoadBalancerPort: int
        :param _RuleSet: 返回的转发规则列表。
        :type RuleSet: list of DevicesBindInfoRule
        """
        self._ListenerId = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._RuleSet = None

    @property
    def ListenerId(self):
        r"""七层监听器实例ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        r"""七层监听器协议类型，可选值：http,https。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""七层监听器的监听端口。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def RuleSet(self):
        r"""返回的转发规则列表。
        :rtype: list of DevicesBindInfoRule
        """
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = DevicesBindInfoRule()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoLoadBalancer(AbstractModel):
    r"""获取设备绑定信息时返回的设备被绑定所在的负载均衡信息。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _AppId: 开发商AppId。
        :type AppId: int
        :param _ProjectId: 负载均衡所属的项目ID。
        :type ProjectId: int
        :param _VpcId: 黑石私有网络唯一ID。
        :type VpcId: str
        :param _Vip: 负载均衡的IP地址。
        :type Vip: str
        :param _TgwSetType: 负载均衡对应的TGW集群类别，取值为tunnel或fullnat。tunnel表示隧道集群，fullnat表示FULLNAT集群。
        :type TgwSetType: str
        :param _Exclusive: 是否独占TGW集群。
        :type Exclusive: int
        :param _L4ListenerSet: 具有该绑定关系的四层监听器列表。
        :type L4ListenerSet: list of DevicesBindInfoL4Listener
        :param _L7ListenerSet: 具有该绑定关系的七层监听器列表。
        :type L7ListenerSet: list of DevicesBindInfoL7Listener
        """
        self._LoadBalancerId = None
        self._AppId = None
        self._ProjectId = None
        self._VpcId = None
        self._Vip = None
        self._TgwSetType = None
        self._Exclusive = None
        self._L4ListenerSet = None
        self._L7ListenerSet = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def AppId(self):
        r"""开发商AppId。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProjectId(self):
        r"""负载均衡所属的项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        r"""黑石私有网络唯一ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        r"""负载均衡的IP地址。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def TgwSetType(self):
        r"""负载均衡对应的TGW集群类别，取值为tunnel或fullnat。tunnel表示隧道集群，fullnat表示FULLNAT集群。
        :rtype: str
        """
        return self._TgwSetType

    @TgwSetType.setter
    def TgwSetType(self, TgwSetType):
        self._TgwSetType = TgwSetType

    @property
    def Exclusive(self):
        r"""是否独占TGW集群。
        :rtype: int
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def L4ListenerSet(self):
        r"""具有该绑定关系的四层监听器列表。
        :rtype: list of DevicesBindInfoL4Listener
        """
        return self._L4ListenerSet

    @L4ListenerSet.setter
    def L4ListenerSet(self, L4ListenerSet):
        self._L4ListenerSet = L4ListenerSet

    @property
    def L7ListenerSet(self):
        r"""具有该绑定关系的七层监听器列表。
        :rtype: list of DevicesBindInfoL7Listener
        """
        return self._L7ListenerSet

    @L7ListenerSet.setter
    def L7ListenerSet(self, L7ListenerSet):
        self._L7ListenerSet = L7ListenerSet


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._AppId = params.get("AppId")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._Vip = params.get("Vip")
        self._TgwSetType = params.get("TgwSetType")
        self._Exclusive = params.get("Exclusive")
        if params.get("L4ListenerSet") is not None:
            self._L4ListenerSet = []
            for item in params.get("L4ListenerSet"):
                obj = DevicesBindInfoL4Listener()
                obj._deserialize(item)
                self._L4ListenerSet.append(obj)
        if params.get("L7ListenerSet") is not None:
            self._L7ListenerSet = []
            for item in params.get("L7ListenerSet"):
                obj = DevicesBindInfoL7Listener()
                obj._deserialize(item)
                self._L7ListenerSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoLocation(AbstractModel):
    r"""获取设备绑定信息时返回的设备所绑定的转发路径信息。

    """

    def __init__(self):
        r"""
        :param _Url: 转发路径。
        :type Url: str
        :param _LocationId: 转发路径实例ID。
        :type LocationId: str
        :param _BackendSet: 该转发路径所绑定的主机列表。
        :type BackendSet: list of DevicesBindInfoBackend
        """
        self._Url = None
        self._LocationId = None
        self._BackendSet = None

    @property
    def Url(self):
        r"""转发路径。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LocationId(self):
        r"""转发路径实例ID。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def BackendSet(self):
        r"""该转发路径所绑定的主机列表。
        :rtype: list of DevicesBindInfoBackend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = DevicesBindInfoBackend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoRule(AbstractModel):
    r"""获取设备绑定信息时返回的设备所绑定的转发规则信息。

    """

    def __init__(self):
        r"""
        :param _Domain: 转发域名。
        :type Domain: str
        :param _DomainId: 转发域名ID。
        :type DomainId: str
        :param _LocationSet: 转发路径列表。
        :type LocationSet: list of DevicesBindInfoLocation
        """
        self._Domain = None
        self._DomainId = None
        self._LocationSet = None

    @property
    def Domain(self):
        r"""转发域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        r"""转发域名ID。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LocationSet(self):
        r"""转发路径列表。
        :rtype: list of DevicesBindInfoLocation
        """
        return self._LocationSet

    @LocationSet.setter
    def LocationSet(self, LocationSet):
        self._LocationSet = LocationSet


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        if params.get("LocationSet") is not None:
            self._LocationSet = []
            for item in params.get("LocationSet"):
                obj = DevicesBindInfoLocation()
                obj._deserialize(item)
                self._LocationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param _Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4Backend(AbstractModel):
    r"""查询四层监听器返回的与监听器绑定关系的主机信息。

    """

    def __init__(self):
        r"""
        :param _BindType: 绑定类别（0代表黑石物理机，1代表虚拟机IP）。
        :type BindType: int
        :param _Port: 主机端口。
        :type Port: int
        :param _Weight: 权重。
        :type Weight: int
        :param _Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :type Status: str
        :param _InstanceId: 黑石物理机的主机ID。
        :type InstanceId: str
        :param _Alias: 黑石物理机的别名。
        :type Alias: str
        :param _LanIp: 主机IP。
        :type LanIp: str
        :param _Operates: 黑石物理机当前可以执行的操作。
        :type Operates: list of str
        :param _ProbePort: 主机探测端口。
        :type ProbePort: int
        """
        self._BindType = None
        self._Port = None
        self._Weight = None
        self._Status = None
        self._InstanceId = None
        self._Alias = None
        self._LanIp = None
        self._Operates = None
        self._ProbePort = None

    @property
    def BindType(self):
        r"""绑定类别（0代表黑石物理机，1代表虚拟机IP）。
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def Port(self):
        r"""主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        r"""权重。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Status(self):
        r"""当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        r"""黑石物理机的主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alias(self):
        r"""黑石物理机的别名。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def LanIp(self):
        r"""主机IP。
        :rtype: str
        """
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def Operates(self):
        r"""黑石物理机当前可以执行的操作。
        :rtype: list of str
        """
        return self._Operates

    @Operates.setter
    def Operates(self, Operates):
        self._Operates = Operates

    @property
    def ProbePort(self):
        r"""主机探测端口。
        :rtype: int
        """
        return self._ProbePort

    @ProbePort.setter
    def ProbePort(self, ProbePort):
        self._ProbePort = ProbePort


    def _deserialize(self, params):
        self._BindType = params.get("BindType")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        self._LanIp = params.get("LanIp")
        self._Operates = params.get("Operates")
        self._ProbePort = params.get("ProbePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4Listener(AbstractModel):
    r"""查询四层监听器时返回的四层监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ListenerName: 用户自定义的监听器名称。
        :type ListenerName: str
        :param _Protocol: 负载均衡实例监听器协议类型，可选值tcp，udp。
        :type Protocol: str
        :param _LoadBalancerPort: 负载均衡监听器的监听接口，可选值1~65535。
        :type LoadBalancerPort: int
        :param _Bandwidth: 用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。
        :type Bandwidth: int
        :param _ListenerType: 监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。
        :type ListenerType: str
        :param _SessionExpire: 会话保持时间。单位：秒
        :type SessionExpire: int
        :param _HealthSwitch: 是否开启了检查：1（开启）、0（关闭）。
        :type HealthSwitch: int
        :param _TimeOut: 响应超时时间，单位：秒。
        :type TimeOut: int
        :param _IntervalTime: 检查间隔，单位：秒。
        :type IntervalTime: int
        :param _HealthNum: 负载均衡监听器健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :type HealthNum: int
        :param _UnhealthNum: 负载均衡监听器不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :type UnhealthNum: int
        :param _CustomHealthSwitch: 是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）
        :type CustomHealthSwitch: int
        :param _InputType: 自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。
        :type InputType: str
        :param _LineSeparatorType: 探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。
        :type LineSeparatorType: int
        :param _HealthRequest: 自定义探测请求内容。
        :type HealthRequest: str
        :param _HealthResponse: 自定义探测返回内容。
        :type HealthResponse: str
        :param _ToaFlag: 是否开启toa：1（开启）、0（关闭）。
        :type ToaFlag: int
        :param _Status: 监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :type Status: int
        :param _AddTimestamp: 创建时间戳。
        :type AddTimestamp: str
        :param _BalanceMode: 转发后端服务器调度类型。
        :type BalanceMode: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._Bandwidth = None
        self._ListenerType = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._CustomHealthSwitch = None
        self._InputType = None
        self._LineSeparatorType = None
        self._HealthRequest = None
        self._HealthResponse = None
        self._ToaFlag = None
        self._Status = None
        self._AddTimestamp = None
        self._BalanceMode = None

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""用户自定义的监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""负载均衡实例监听器协议类型，可选值tcp，udp。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""负载均衡监听器的监听接口，可选值1~65535。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Bandwidth(self):
        r"""用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ListenerType(self):
        r"""监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def SessionExpire(self):
        r"""会话保持时间。单位：秒
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""是否开启了检查：1（开启）、0（关闭）。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        r"""响应超时时间，单位：秒。
        :rtype: int
        """
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        r"""检查间隔，单位：秒。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""负载均衡监听器健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""负载均衡监听器不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def CustomHealthSwitch(self):
        r"""是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）
        :rtype: int
        """
        return self._CustomHealthSwitch

    @CustomHealthSwitch.setter
    def CustomHealthSwitch(self, CustomHealthSwitch):
        self._CustomHealthSwitch = CustomHealthSwitch

    @property
    def InputType(self):
        r"""自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def LineSeparatorType(self):
        r"""探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。
        :rtype: int
        """
        return self._LineSeparatorType

    @LineSeparatorType.setter
    def LineSeparatorType(self, LineSeparatorType):
        self._LineSeparatorType = LineSeparatorType

    @property
    def HealthRequest(self):
        r"""自定义探测请求内容。
        :rtype: str
        """
        return self._HealthRequest

    @HealthRequest.setter
    def HealthRequest(self, HealthRequest):
        self._HealthRequest = HealthRequest

    @property
    def HealthResponse(self):
        r"""自定义探测返回内容。
        :rtype: str
        """
        return self._HealthResponse

    @HealthResponse.setter
    def HealthResponse(self, HealthResponse):
        self._HealthResponse = HealthResponse

    @property
    def ToaFlag(self):
        r"""是否开启toa：1（开启）、0（关闭）。
        :rtype: int
        """
        return self._ToaFlag

    @ToaFlag.setter
    def ToaFlag(self, ToaFlag):
        self._ToaFlag = ToaFlag

    @property
    def Status(self):
        r"""监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTimestamp(self):
        r"""创建时间戳。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def BalanceMode(self):
        r"""转发后端服务器调度类型。
        :rtype: str
        """
        return self._BalanceMode

    @BalanceMode.setter
    def BalanceMode(self, BalanceMode):
        self._BalanceMode = BalanceMode


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Bandwidth = params.get("Bandwidth")
        self._ListenerType = params.get("ListenerType")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._CustomHealthSwitch = params.get("CustomHealthSwitch")
        self._InputType = params.get("InputType")
        self._LineSeparatorType = params.get("LineSeparatorType")
        self._HealthRequest = params.get("HealthRequest")
        self._HealthResponse = params.get("HealthResponse")
        self._ToaFlag = params.get("ToaFlag")
        self._Status = params.get("Status")
        self._AddTimestamp = params.get("AddTimestamp")
        self._BalanceMode = params.get("BalanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4ListenerInfo(AbstractModel):
    r"""查询绑定了某主机的四层监听器时返回的四层监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ListenerName: 用户自定义的监听器名称。
        :type ListenerName: str
        :param _Protocol: 负载均衡实例监听器协议类型，可选值tcp，udp。
        :type Protocol: str
        :param _LoadBalancerPort: 负载均衡监听器的监听接口，可选值1~65535。
        :type LoadBalancerPort: int
        :param _Bandwidth: 用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。
        :type Bandwidth: int
        :param _ListenerType: 监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。
        :type ListenerType: str
        :param _SessionExpire: 会话保持时间。单位：秒
        :type SessionExpire: int
        :param _HealthSwitch: 是否开启了检查：1（开启）、0（关闭）。
        :type HealthSwitch: int
        :param _TimeOut: 响应超时时间，单位：秒。
        :type TimeOut: int
        :param _IntervalTime: 检查间隔，单位：秒。
        :type IntervalTime: int
        :param _HealthNum: 负载均衡监听器健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :type HealthNum: int
        :param _UnhealthNum: 负载均衡监听器不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :type UnhealthNum: int
        :param _Status: 监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :type Status: int
        :param _AddTimestamp: 创建时间戳。
        :type AddTimestamp: str
        :param _CustomHealthSwitch: 是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）
        :type CustomHealthSwitch: int
        :param _InputType: 自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。
        :type InputType: str
        :param _LineSeparatorType: 探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。
        :type LineSeparatorType: int
        :param _HealthRequest: 自定义探测请求内容。
        :type HealthRequest: str
        :param _HealthResponse: 自定义探测返回内容。
        :type HealthResponse: str
        :param _ToaFlag: 是否开启toa：1（开启）、0（关闭）。
        :type ToaFlag: int
        :param _BalanceMode: 转发后端服务器调度类型。
        :type BalanceMode: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._Bandwidth = None
        self._ListenerType = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._Status = None
        self._AddTimestamp = None
        self._CustomHealthSwitch = None
        self._InputType = None
        self._LineSeparatorType = None
        self._HealthRequest = None
        self._HealthResponse = None
        self._ToaFlag = None
        self._BalanceMode = None

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""用户自定义的监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""负载均衡实例监听器协议类型，可选值tcp，udp。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""负载均衡监听器的监听接口，可选值1~65535。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Bandwidth(self):
        r"""用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ListenerType(self):
        r"""监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def SessionExpire(self):
        r"""会话保持时间。单位：秒
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""是否开启了检查：1（开启）、0（关闭）。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        r"""响应超时时间，单位：秒。
        :rtype: int
        """
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        r"""检查间隔，单位：秒。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""负载均衡监听器健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""负载均衡监听器不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def Status(self):
        r"""监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTimestamp(self):
        r"""创建时间戳。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def CustomHealthSwitch(self):
        r"""是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）
        :rtype: int
        """
        return self._CustomHealthSwitch

    @CustomHealthSwitch.setter
    def CustomHealthSwitch(self, CustomHealthSwitch):
        self._CustomHealthSwitch = CustomHealthSwitch

    @property
    def InputType(self):
        r"""自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def LineSeparatorType(self):
        r"""探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。
        :rtype: int
        """
        return self._LineSeparatorType

    @LineSeparatorType.setter
    def LineSeparatorType(self, LineSeparatorType):
        self._LineSeparatorType = LineSeparatorType

    @property
    def HealthRequest(self):
        r"""自定义探测请求内容。
        :rtype: str
        """
        return self._HealthRequest

    @HealthRequest.setter
    def HealthRequest(self, HealthRequest):
        self._HealthRequest = HealthRequest

    @property
    def HealthResponse(self):
        r"""自定义探测返回内容。
        :rtype: str
        """
        return self._HealthResponse

    @HealthResponse.setter
    def HealthResponse(self, HealthResponse):
        self._HealthResponse = HealthResponse

    @property
    def ToaFlag(self):
        r"""是否开启toa：1（开启）、0（关闭）。
        :rtype: int
        """
        return self._ToaFlag

    @ToaFlag.setter
    def ToaFlag(self, ToaFlag):
        self._ToaFlag = ToaFlag

    @property
    def BalanceMode(self):
        r"""转发后端服务器调度类型。
        :rtype: str
        """
        return self._BalanceMode

    @BalanceMode.setter
    def BalanceMode(self, BalanceMode):
        self._BalanceMode = BalanceMode


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Bandwidth = params.get("Bandwidth")
        self._ListenerType = params.get("ListenerType")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._Status = params.get("Status")
        self._AddTimestamp = params.get("AddTimestamp")
        self._CustomHealthSwitch = params.get("CustomHealthSwitch")
        self._InputType = params.get("InputType")
        self._LineSeparatorType = params.get("LineSeparatorType")
        self._HealthRequest = params.get("HealthRequest")
        self._HealthResponse = params.get("HealthResponse")
        self._ToaFlag = params.get("ToaFlag")
        self._BalanceMode = params.get("BalanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7Backend(AbstractModel):
    r"""获取七层转发路径绑定的主机列表时返回的主机信息。

    """

    def __init__(self):
        r"""
        :param _BindType: 绑定类别（0代表黑石物理机，1代表虚拟机IP）。
        :type BindType: int
        :param _Port: 主机端口。
        :type Port: int
        :param _Weight: 权重。
        :type Weight: int
        :param _Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :type Status: str
        :param _InstanceId: 黑石物理机的主机ID。
        :type InstanceId: str
        :param _Alias: 黑石物理机的别名。
        :type Alias: str
        :param _LanIp: 主机IP。
        :type LanIp: str
        :param _MgtIp: 黑石物理机的管理IP。
        :type MgtIp: str
        :param _Operates: 黑石物理机当前可以执行的操作。
        :type Operates: list of str
        """
        self._BindType = None
        self._Port = None
        self._Weight = None
        self._Status = None
        self._InstanceId = None
        self._Alias = None
        self._LanIp = None
        self._MgtIp = None
        self._Operates = None

    @property
    def BindType(self):
        r"""绑定类别（0代表黑石物理机，1代表虚拟机IP）。
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def Port(self):
        r"""主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        r"""权重。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Status(self):
        r"""当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        r"""黑石物理机的主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alias(self):
        r"""黑石物理机的别名。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def LanIp(self):
        r"""主机IP。
        :rtype: str
        """
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def MgtIp(self):
        r"""黑石物理机的管理IP。
        :rtype: str
        """
        return self._MgtIp

    @MgtIp.setter
    def MgtIp(self, MgtIp):
        self._MgtIp = MgtIp

    @property
    def Operates(self):
        r"""黑石物理机当前可以执行的操作。
        :rtype: list of str
        """
        return self._Operates

    @Operates.setter
    def Operates(self, Operates):
        self._Operates = Operates


    def _deserialize(self, params):
        self._BindType = params.get("BindType")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        self._LanIp = params.get("LanIp")
        self._MgtIp = params.get("MgtIp")
        self._Operates = params.get("Operates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ExListener(AbstractModel):
    r"""监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 绑定的监听器唯一ID。
        :type ListenerId: str
        :param _ListenerName: 监听器名称。
        :type ListenerName: str
        :param _Protocol: 七层监听器协议类型，可选值：http,https。
        :type Protocol: str
        :param _LoadBalancerPort: 监听器的监听端口。
        :type LoadBalancerPort: int
        :param _Bandwidth: 当前带宽。
        :type Bandwidth: int
        :param _MaxBandwidth: 带宽上限。
        :type MaxBandwidth: int
        :param _ListenerType: 监听器类型。
        :type ListenerType: str
        :param _SslMode: 认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :type SslMode: int
        :param _CertId: 服务端证书ID。
        :type CertId: str
        :param _CertCaId: 客户端证书ID。
        :type CertCaId: str
        :param _AddTimestamp: 添加时间。
        :type AddTimestamp: str
        :param _LoadBalancerId: 负载均衡名ID。
        :type LoadBalancerId: str
        :param _VpcName: 私有网络名称。
        :type VpcName: str
        :param _VpcCidrBlock: 私有网络Cidr。
        :type VpcCidrBlock: str
        :param _LoadBalancerVips: 负载均衡的VIP。
        :type LoadBalancerVips: list of str
        :param _LoadBalancerName: 负载均衡名称。
        :type LoadBalancerName: str
        :param _LoadBalancerVipv6s: 负载均衡IPV6的VIP。
        :type LoadBalancerVipv6s: list of str
        :param _IpProtocolType: 支持的IP协议类型。ipv4或者是ipv6。
        :type IpProtocolType: str
        :param _BindTrafficMirror: 是否绑定在入参指定的流量镜像中。
        :type BindTrafficMirror: bool
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._Bandwidth = None
        self._MaxBandwidth = None
        self._ListenerType = None
        self._SslMode = None
        self._CertId = None
        self._CertCaId = None
        self._AddTimestamp = None
        self._LoadBalancerId = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._LoadBalancerVips = None
        self._LoadBalancerName = None
        self._LoadBalancerVipv6s = None
        self._IpProtocolType = None
        self._BindTrafficMirror = None

    @property
    def ListenerId(self):
        r"""绑定的监听器唯一ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""七层监听器协议类型，可选值：http,https。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""监听器的监听端口。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Bandwidth(self):
        r"""当前带宽。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def MaxBandwidth(self):
        r"""带宽上限。
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def ListenerType(self):
        r"""监听器类型。
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def SslMode(self):
        r"""认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :rtype: int
        """
        return self._SslMode

    @SslMode.setter
    def SslMode(self, SslMode):
        self._SslMode = SslMode

    @property
    def CertId(self):
        r"""服务端证书ID。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        r"""客户端证书ID。
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def AddTimestamp(self):
        r"""添加时间。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def LoadBalancerId(self):
        r"""负载均衡名ID。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def VpcName(self):
        r"""私有网络名称。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        r"""私有网络Cidr。
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def LoadBalancerVips(self):
        r"""负载均衡的VIP。
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def LoadBalancerName(self):
        r"""负载均衡名称。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerVipv6s(self):
        r"""负载均衡IPV6的VIP。
        :rtype: list of str
        """
        return self._LoadBalancerVipv6s

    @LoadBalancerVipv6s.setter
    def LoadBalancerVipv6s(self, LoadBalancerVipv6s):
        self._LoadBalancerVipv6s = LoadBalancerVipv6s

    @property
    def IpProtocolType(self):
        r"""支持的IP协议类型。ipv4或者是ipv6。
        :rtype: str
        """
        return self._IpProtocolType

    @IpProtocolType.setter
    def IpProtocolType(self, IpProtocolType):
        self._IpProtocolType = IpProtocolType

    @property
    def BindTrafficMirror(self):
        r"""是否绑定在入参指定的流量镜像中。
        :rtype: bool
        """
        return self._BindTrafficMirror

    @BindTrafficMirror.setter
    def BindTrafficMirror(self, BindTrafficMirror):
        self._BindTrafficMirror = BindTrafficMirror


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Bandwidth = params.get("Bandwidth")
        self._MaxBandwidth = params.get("MaxBandwidth")
        self._ListenerType = params.get("ListenerType")
        self._SslMode = params.get("SslMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._AddTimestamp = params.get("AddTimestamp")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self._IpProtocolType = params.get("IpProtocolType")
        self._BindTrafficMirror = params.get("BindTrafficMirror")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7Listener(AbstractModel):
    r"""获取黑石负载均衡七层监听器时返回的七层监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 七层监听器实例ID。
        :type ListenerId: str
        :param _ListenerName: 七层监听器名称。
        :type ListenerName: str
        :param _Protocol: 七层监听器协议类型，可选值：http,https。
        :type Protocol: str
        :param _LoadBalancerPort: 七层监听器的监听端口。
        :type LoadBalancerPort: int
        :param _Bandwidth: 计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。
        :type Bandwidth: int
        :param _ListenerType: 监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。
        :type ListenerType: str
        :param _SslMode: 七层监听器的认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :type SslMode: int
        :param _CertId: 七层监听器关联的服务端证书ID。
        :type CertId: str
        :param _CertCaId: 七层监听器关联的客户端证书ID。
        :type CertCaId: str
        :param _Status: 监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :type Status: int
        :param _AddTimestamp: 创建时间戳。
        :type AddTimestamp: str
        :param _ForwardProtocol: https转发类型。0：https。1：spdy。2：http2。3：spdy+http2。
        :type ForwardProtocol: int
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._Bandwidth = None
        self._ListenerType = None
        self._SslMode = None
        self._CertId = None
        self._CertCaId = None
        self._Status = None
        self._AddTimestamp = None
        self._ForwardProtocol = None

    @property
    def ListenerId(self):
        r"""七层监听器实例ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""七层监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""七层监听器协议类型，可选值：http,https。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""七层监听器的监听端口。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Bandwidth(self):
        r"""计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ListenerType(self):
        r"""监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def SslMode(self):
        r"""七层监听器的认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :rtype: int
        """
        return self._SslMode

    @SslMode.setter
    def SslMode(self, SslMode):
        self._SslMode = SslMode

    @property
    def CertId(self):
        r"""七层监听器关联的服务端证书ID。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        r"""七层监听器关联的客户端证书ID。
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def Status(self):
        r"""监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTimestamp(self):
        r"""创建时间戳。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def ForwardProtocol(self):
        r"""https转发类型。0：https。1：spdy。2：http2。3：spdy+http2。
        :rtype: int
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Bandwidth = params.get("Bandwidth")
        self._ListenerType = params.get("ListenerType")
        self._SslMode = params.get("SslMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._Status = params.get("Status")
        self._AddTimestamp = params.get("AddTimestamp")
        self._ForwardProtocol = params.get("ForwardProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ListenerInfo(AbstractModel):
    r"""查询绑定了某主机的七层监听器时返回的七层监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 七层监听器实例ID。
        :type ListenerId: str
        :param _ListenerName: 七层监听器名称。
        :type ListenerName: str
        :param _Protocol: 七层监听器协议类型，可选值：http,https。
        :type Protocol: str
        :param _LoadBalancerPort: 七层监听器的监听端口。
        :type LoadBalancerPort: int
        :param _Bandwidth: 计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。
        :type Bandwidth: int
        :param _ListenerType: 监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。
        :type ListenerType: str
        :param _SslMode: 七层监听器的认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :type SslMode: int
        :param _CertId: 七层监听器关联的服务端证书ID。
        :type CertId: str
        :param _CertCaId: 七层监听器关联的客户端证书ID。
        :type CertCaId: str
        :param _Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :type Status: int
        :param _AddTimestamp: 创建时间戳。
        :type AddTimestamp: str
        :param _RuleSet: 返回的转发规则列表。
        :type RuleSet: list of L7ListenerInfoRule
        :param _ForwardProtocol: https转发类型。0：https。1：spdy。2：http2。3：spdy+http2。
        :type ForwardProtocol: int
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._Bandwidth = None
        self._ListenerType = None
        self._SslMode = None
        self._CertId = None
        self._CertCaId = None
        self._Status = None
        self._AddTimestamp = None
        self._RuleSet = None
        self._ForwardProtocol = None

    @property
    def ListenerId(self):
        r"""七层监听器实例ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""七层监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""七层监听器协议类型，可选值：http,https。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""七层监听器的监听端口。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Bandwidth(self):
        r"""计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ListenerType(self):
        r"""监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def SslMode(self):
        r"""七层监听器的认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :rtype: int
        """
        return self._SslMode

    @SslMode.setter
    def SslMode(self, SslMode):
        self._SslMode = SslMode

    @property
    def CertId(self):
        r"""七层监听器关联的服务端证书ID。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        r"""七层监听器关联的客户端证书ID。
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def Status(self):
        r"""当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTimestamp(self):
        r"""创建时间戳。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def RuleSet(self):
        r"""返回的转发规则列表。
        :rtype: list of L7ListenerInfoRule
        """
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet

    @property
    def ForwardProtocol(self):
        r"""https转发类型。0：https。1：spdy。2：http2。3：spdy+http2。
        :rtype: int
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Bandwidth = params.get("Bandwidth")
        self._ListenerType = params.get("ListenerType")
        self._SslMode = params.get("SslMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._Status = params.get("Status")
        self._AddTimestamp = params.get("AddTimestamp")
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = L7ListenerInfoRule()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        self._ForwardProtocol = params.get("ForwardProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ListenerInfoBackend(AbstractModel):
    r"""查询绑定了某主机七层监听器时返回的与转发路径所绑定的主机信息。

    """

    def __init__(self):
        r"""
        :param _BindType: 绑定类别（0代表黑石物理机，1代表虚拟机IP）。
        :type BindType: int
        :param _Port: 主机端口。
        :type Port: int
        :param _Weight: 权重。
        :type Weight: int
        :param _Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :type Status: str
        :param _InstanceId: 黑石物理机的主机ID。
        :type InstanceId: str
        :param _Alias: 黑石物理机的别名。
        :type Alias: str
        :param _LanIp: 主机IP。
        :type LanIp: str
        """
        self._BindType = None
        self._Port = None
        self._Weight = None
        self._Status = None
        self._InstanceId = None
        self._Alias = None
        self._LanIp = None

    @property
    def BindType(self):
        r"""绑定类别（0代表黑石物理机，1代表虚拟机IP）。
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def Port(self):
        r"""主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        r"""权重。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Status(self):
        r"""当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        r"""黑石物理机的主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alias(self):
        r"""黑石物理机的别名。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def LanIp(self):
        r"""主机IP。
        :rtype: str
        """
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp


    def _deserialize(self, params):
        self._BindType = params.get("BindType")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        self._LanIp = params.get("LanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ListenerInfoLocation(AbstractModel):
    r"""查询绑定了某主机的七层监听器时返回的转发路径。

    """

    def __init__(self):
        r"""
        :param _Url: 转发路径。
        :type Url: str
        :param _LocationId: 转发路径实例ID。
        :type LocationId: str
        :param _SessionExpire: 会话保持时间。
        :type SessionExpire: int
        :param _HealthSwitch: 是否开启健康检查。
        :type HealthSwitch: int
        :param _HttpCheckPath: 健康检查检查路径。
        :type HttpCheckPath: str
        :param _HttpCheckDomain: 健康检查检查域名。
        :type HttpCheckDomain: str
        :param _IntervalTime: 健康检查检查间隔时间。
        :type IntervalTime: int
        :param _HealthNum: 健康检查健康阈值。
        :type HealthNum: int
        :param _UnhealthNum: 健康检查不健康阈值。
        :type UnhealthNum: int
        :param _HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :type HttpCodes: list of int non-negative
        :param _BalanceMode: 均衡方式。
        :type BalanceMode: str
        :param _Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :type Status: int
        :param _AddTimestamp: 创建时间戳。
        :type AddTimestamp: str
        :param _BackendSet: 该转发路径所绑定的主机列表。
        :type BackendSet: list of L7ListenerInfoBackend
        """
        self._Url = None
        self._LocationId = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._HttpCheckPath = None
        self._HttpCheckDomain = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._HttpCodes = None
        self._BalanceMode = None
        self._Status = None
        self._AddTimestamp = None
        self._BackendSet = None

    @property
    def Url(self):
        r"""转发路径。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LocationId(self):
        r"""转发路径实例ID。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def SessionExpire(self):
        r"""会话保持时间。
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""是否开启健康检查。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def HttpCheckPath(self):
        r"""健康检查检查路径。
        :rtype: str
        """
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def HttpCheckDomain(self):
        r"""健康检查检查域名。
        :rtype: str
        """
        return self._HttpCheckDomain

    @HttpCheckDomain.setter
    def HttpCheckDomain(self, HttpCheckDomain):
        self._HttpCheckDomain = HttpCheckDomain

    @property
    def IntervalTime(self):
        r"""健康检查检查间隔时间。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""健康检查健康阈值。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""健康检查不健康阈值。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def HttpCodes(self):
        r"""健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :rtype: list of int non-negative
        """
        return self._HttpCodes

    @HttpCodes.setter
    def HttpCodes(self, HttpCodes):
        self._HttpCodes = HttpCodes

    @property
    def BalanceMode(self):
        r"""均衡方式。
        :rtype: str
        """
        return self._BalanceMode

    @BalanceMode.setter
    def BalanceMode(self, BalanceMode):
        self._BalanceMode = BalanceMode

    @property
    def Status(self):
        r"""当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTimestamp(self):
        r"""创建时间戳。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def BackendSet(self):
        r"""该转发路径所绑定的主机列表。
        :rtype: list of L7ListenerInfoBackend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._LocationId = params.get("LocationId")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._HttpCheckDomain = params.get("HttpCheckDomain")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._HttpCodes = params.get("HttpCodes")
        self._BalanceMode = params.get("BalanceMode")
        self._Status = params.get("Status")
        self._AddTimestamp = params.get("AddTimestamp")
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = L7ListenerInfoBackend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ListenerInfoRule(AbstractModel):
    r"""查询绑定了某主机的七层监听器时返回的转发规则。

    """

    def __init__(self):
        r"""
        :param _Domain: 转发域名。
        :type Domain: str
        :param _DomainId: 转发域名实例ID。
        :type DomainId: str
        :param _Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :type Status: int
        :param _AddTimestamp: 创建时间戳。
        :type AddTimestamp: str
        :param _LocationSet: 该转发域名下面的转发路径列表。
        :type LocationSet: list of L7ListenerInfoLocation
        """
        self._Domain = None
        self._DomainId = None
        self._Status = None
        self._AddTimestamp = None
        self._LocationSet = None

    @property
    def Domain(self):
        r"""转发域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        r"""转发域名实例ID。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Status(self):
        r"""当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTimestamp(self):
        r"""创建时间戳。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def LocationSet(self):
        r"""该转发域名下面的转发路径列表。
        :rtype: list of L7ListenerInfoLocation
        """
        return self._LocationSet

    @LocationSet.setter
    def LocationSet(self, LocationSet):
        self._LocationSet = LocationSet


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Status = params.get("Status")
        self._AddTimestamp = params.get("AddTimestamp")
        if params.get("LocationSet") is not None:
            self._LocationSet = []
            for item in params.get("LocationSet"):
                obj = L7ListenerInfoLocation()
                obj._deserialize(item)
                self._LocationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7Rule(AbstractModel):
    r"""获取七层监听器转发规则时返回的转发规则。

    """

    def __init__(self):
        r"""
        :param _Domain: 转发域名。
        :type Domain: str
        :param _DomainId: 转发域名实例ID。
        :type DomainId: str
        :param _Status: 转发路径当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :type Status: int
        :param _AddTimestamp: 创建时间戳。
        :type AddTimestamp: str
        :param _LocationSet: 该转发域名下面的转发路径列表。
        :type LocationSet: list of L7RulesLocation
        """
        self._Domain = None
        self._DomainId = None
        self._Status = None
        self._AddTimestamp = None
        self._LocationSet = None

    @property
    def Domain(self):
        r"""转发域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        r"""转发域名实例ID。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Status(self):
        r"""转发路径当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTimestamp(self):
        r"""创建时间戳。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def LocationSet(self):
        r"""该转发域名下面的转发路径列表。
        :rtype: list of L7RulesLocation
        """
        return self._LocationSet

    @LocationSet.setter
    def LocationSet(self, LocationSet):
        self._LocationSet = LocationSet


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Status = params.get("Status")
        self._AddTimestamp = params.get("AddTimestamp")
        if params.get("LocationSet") is not None:
            self._LocationSet = []
            for item in params.get("LocationSet"):
                obj = L7RulesLocation()
                obj._deserialize(item)
                self._LocationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RulesLocation(AbstractModel):
    r"""获取七层转发规则时返回的转发域名下面的转发路径。

    """

    def __init__(self):
        r"""
        :param _Url: 转发路径。
        :type Url: str
        :param _LocationId: 转发路径实例ID。
        :type LocationId: str
        :param _SessionExpire: 会话保持时间。
        :type SessionExpire: int
        :param _HealthSwitch: 是否开启健康检查。
        :type HealthSwitch: int
        :param _HttpCheckPath: 健康检查检查路径。
        :type HttpCheckPath: str
        :param _HttpCheckDomain: 健康检查检查域名。
        :type HttpCheckDomain: str
        :param _IntervalTime: 健康检查检查间隔时间。
        :type IntervalTime: int
        :param _HealthNum: 健康检查健康阈值。
        :type HealthNum: int
        :param _UnhealthNum: 健康检查不健康阈值。
        :type UnhealthNum: int
        :param _HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :type HttpCodes: list of int non-negative
        :param _BalanceMode: 均衡方式。
        :type BalanceMode: str
        :param _Status: 转发路径当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :type Status: int
        :param _AddTimestamp: 创建时间戳。
        :type AddTimestamp: str
        """
        self._Url = None
        self._LocationId = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._HttpCheckPath = None
        self._HttpCheckDomain = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._HttpCodes = None
        self._BalanceMode = None
        self._Status = None
        self._AddTimestamp = None

    @property
    def Url(self):
        r"""转发路径。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LocationId(self):
        r"""转发路径实例ID。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def SessionExpire(self):
        r"""会话保持时间。
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""是否开启健康检查。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def HttpCheckPath(self):
        r"""健康检查检查路径。
        :rtype: str
        """
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def HttpCheckDomain(self):
        r"""健康检查检查域名。
        :rtype: str
        """
        return self._HttpCheckDomain

    @HttpCheckDomain.setter
    def HttpCheckDomain(self, HttpCheckDomain):
        self._HttpCheckDomain = HttpCheckDomain

    @property
    def IntervalTime(self):
        r"""健康检查检查间隔时间。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""健康检查健康阈值。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""健康检查不健康阈值。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def HttpCodes(self):
        r"""健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :rtype: list of int non-negative
        """
        return self._HttpCodes

    @HttpCodes.setter
    def HttpCodes(self, HttpCodes):
        self._HttpCodes = HttpCodes

    @property
    def BalanceMode(self):
        r"""均衡方式。
        :rtype: str
        """
        return self._BalanceMode

    @BalanceMode.setter
    def BalanceMode(self, BalanceMode):
        self._BalanceMode = BalanceMode

    @property
    def Status(self):
        r"""转发路径当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTimestamp(self):
        r"""创建时间戳。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._LocationId = params.get("LocationId")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._HttpCheckDomain = params.get("HttpCheckDomain")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._HttpCodes = params.get("HttpCodes")
        self._BalanceMode = params.get("BalanceMode")
        self._Status = params.get("Status")
        self._AddTimestamp = params.get("AddTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    r"""获取负载均衡实例列表时返回的负载均衡信息。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡器ID
        :type LoadBalancerId: str
        :param _ProjectId: 项目ID，通过v2/DescribeProject 接口获得
        :type ProjectId: int
        :param _LoadBalancerName: 负载均衡器名称
        :type LoadBalancerName: str
        :param _LoadBalancerType: 负载均衡的类型 : open表示公网负载均衡类型，internal表示内网负载均衡类型
        :type LoadBalancerType: str
        :param _Exclusive: 是否筛选独占集群，0表示非独占集群，1表示四层独占集群，2表示七层独占集群，3表示四层和七层独占集群，4表示共享容灾
        :type Exclusive: int
        :param _TgwSetType: 该负载均衡对应的tgw集群（fullnat,tunnel,dnat）
        :type TgwSetType: str
        :param _Domain: 负载均衡域名。规则：1-60个小写英文字母、数字、点号“.”或连接线“-”。内网类型的负载均衡不能配置该字段
        :type Domain: str
        :param _VpcId: 该负载均衡对应的所在的VpcId
        :type VpcId: str
        :param _SubnetId: 该负载均衡对应的所在的SubnetId
        :type SubnetId: str
        :param _Status: 无
        :type Status: int
        :param _PayMode: 无
        :type PayMode: str
        :param _LatestPayMode: 无
        :type LatestPayMode: str
        :param _CreateTime: 无
        :type CreateTime: str
        :param _StatusTime: 无
        :type StatusTime: str
        :param _VpcName: 私有网络名称。
        :type VpcName: str
        :param _VpcCidrBlock: 私有网络Cidr。
        :type VpcCidrBlock: str
        :param _LoadBalancerVips: 负载均衡的IPV4的VIP。
        :type LoadBalancerVips: list of str
        :param _SupportListenerTypes: 无
        :type SupportListenerTypes: list of str
        :param _Bandwidth: 无
        :type Bandwidth: int
        :param _ConfId: 负载均衡个性化配置ID
        :type ConfId: str
        :param _ConfName: 无
        :type ConfName: str
        :param _LoadBalancerVipv6s: 负载均衡的IPV6的VIP。
        :type LoadBalancerVipv6s: list of str
        :param _IpProtocolType: 负载均衡IP协议类型。ipv4或者ipv6。
        :type IpProtocolType: str
        :param _BzPayMode: 保障型网关计费形式
        :type BzPayMode: str
        :param _BzL4Metrics: 保障型网关四层计费指标
        :type BzL4Metrics: str
        :param _BzL7Metrics: 保障型网关七层计费指标
        :type BzL7Metrics: str
        :param _IntVpcId: 该负载均衡对应的所在的整形类型的VpcId
        :type IntVpcId: int
        :param _CurVips: 负载均衡的IPV6或者IPV4的VIP。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurVips: list of str
        """
        self._LoadBalancerId = None
        self._ProjectId = None
        self._LoadBalancerName = None
        self._LoadBalancerType = None
        self._Exclusive = None
        self._TgwSetType = None
        self._Domain = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._PayMode = None
        self._LatestPayMode = None
        self._CreateTime = None
        self._StatusTime = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._LoadBalancerVips = None
        self._SupportListenerTypes = None
        self._Bandwidth = None
        self._ConfId = None
        self._ConfName = None
        self._LoadBalancerVipv6s = None
        self._IpProtocolType = None
        self._BzPayMode = None
        self._BzL4Metrics = None
        self._BzL7Metrics = None
        self._IntVpcId = None
        self._CurVips = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡器ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ProjectId(self):
        r"""项目ID，通过v2/DescribeProject 接口获得
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def LoadBalancerName(self):
        r"""负载均衡器名称
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        r"""负载均衡的类型 : open表示公网负载均衡类型，internal表示内网负载均衡类型
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Exclusive(self):
        r"""是否筛选独占集群，0表示非独占集群，1表示四层独占集群，2表示七层独占集群，3表示四层和七层独占集群，4表示共享容灾
        :rtype: int
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def TgwSetType(self):
        r"""该负载均衡对应的tgw集群（fullnat,tunnel,dnat）
        :rtype: str
        """
        return self._TgwSetType

    @TgwSetType.setter
    def TgwSetType(self, TgwSetType):
        self._TgwSetType = TgwSetType

    @property
    def Domain(self):
        r"""负载均衡域名。规则：1-60个小写英文字母、数字、点号“.”或连接线“-”。内网类型的负载均衡不能配置该字段
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def VpcId(self):
        r"""该负载均衡对应的所在的VpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""该负载均衡对应的所在的SubnetId
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        r"""无
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PayMode(self):
        r"""无
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def LatestPayMode(self):
        r"""无
        :rtype: str
        """
        return self._LatestPayMode

    @LatestPayMode.setter
    def LatestPayMode(self, LatestPayMode):
        self._LatestPayMode = LatestPayMode

    @property
    def CreateTime(self):
        r"""无
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StatusTime(self):
        r"""无
        :rtype: str
        """
        return self._StatusTime

    @StatusTime.setter
    def StatusTime(self, StatusTime):
        self._StatusTime = StatusTime

    @property
    def VpcName(self):
        r"""私有网络名称。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        r"""私有网络Cidr。
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def LoadBalancerVips(self):
        r"""负载均衡的IPV4的VIP。
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def SupportListenerTypes(self):
        r"""无
        :rtype: list of str
        """
        return self._SupportListenerTypes

    @SupportListenerTypes.setter
    def SupportListenerTypes(self, SupportListenerTypes):
        self._SupportListenerTypes = SupportListenerTypes

    @property
    def Bandwidth(self):
        r"""无
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ConfId(self):
        r"""负载均衡个性化配置ID
        :rtype: str
        """
        return self._ConfId

    @ConfId.setter
    def ConfId(self, ConfId):
        self._ConfId = ConfId

    @property
    def ConfName(self):
        r"""无
        :rtype: str
        """
        return self._ConfName

    @ConfName.setter
    def ConfName(self, ConfName):
        self._ConfName = ConfName

    @property
    def LoadBalancerVipv6s(self):
        r"""负载均衡的IPV6的VIP。
        :rtype: list of str
        """
        return self._LoadBalancerVipv6s

    @LoadBalancerVipv6s.setter
    def LoadBalancerVipv6s(self, LoadBalancerVipv6s):
        self._LoadBalancerVipv6s = LoadBalancerVipv6s

    @property
    def IpProtocolType(self):
        r"""负载均衡IP协议类型。ipv4或者ipv6。
        :rtype: str
        """
        return self._IpProtocolType

    @IpProtocolType.setter
    def IpProtocolType(self, IpProtocolType):
        self._IpProtocolType = IpProtocolType

    @property
    def BzPayMode(self):
        r"""保障型网关计费形式
        :rtype: str
        """
        return self._BzPayMode

    @BzPayMode.setter
    def BzPayMode(self, BzPayMode):
        self._BzPayMode = BzPayMode

    @property
    def BzL4Metrics(self):
        r"""保障型网关四层计费指标
        :rtype: str
        """
        return self._BzL4Metrics

    @BzL4Metrics.setter
    def BzL4Metrics(self, BzL4Metrics):
        self._BzL4Metrics = BzL4Metrics

    @property
    def BzL7Metrics(self):
        r"""保障型网关七层计费指标
        :rtype: str
        """
        return self._BzL7Metrics

    @BzL7Metrics.setter
    def BzL7Metrics(self, BzL7Metrics):
        self._BzL7Metrics = BzL7Metrics

    @property
    def IntVpcId(self):
        r"""该负载均衡对应的所在的整形类型的VpcId
        :rtype: int
        """
        return self._IntVpcId

    @IntVpcId.setter
    def IntVpcId(self, IntVpcId):
        self._IntVpcId = IntVpcId

    @property
    def CurVips(self):
        r"""负载均衡的IPV6或者IPV4的VIP。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CurVips

    @CurVips.setter
    def CurVips(self, CurVips):
        self._CurVips = CurVips


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ProjectId = params.get("ProjectId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Exclusive = params.get("Exclusive")
        self._TgwSetType = params.get("TgwSetType")
        self._Domain = params.get("Domain")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._PayMode = params.get("PayMode")
        self._LatestPayMode = params.get("LatestPayMode")
        self._CreateTime = params.get("CreateTime")
        self._StatusTime = params.get("StatusTime")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._SupportListenerTypes = params.get("SupportListenerTypes")
        self._Bandwidth = params.get("Bandwidth")
        self._ConfId = params.get("ConfId")
        self._ConfName = params.get("ConfName")
        self._LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self._IpProtocolType = params.get("IpProtocolType")
        self._BzPayMode = params.get("BzPayMode")
        self._BzL4Metrics = params.get("BzL4Metrics")
        self._BzL7Metrics = params.get("BzL7Metrics")
        self._IntVpcId = params.get("IntVpcId")
        self._CurVips = params.get("CurVips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerPortInfoListener(AbstractModel):
    r"""获取黑石负载均衡端口相关信息时返回的监听器信息（四层和七层）。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param _ListenerName: 监听器名称。
        :type ListenerName: str
        :param _Protocol: 监听器协议类型，可选值：http，https，tcp，udp。
        :type Protocol: str
        :param _LoadBalancerPort: 监听器的监听端口。
        :type LoadBalancerPort: int
        :param _Bandwidth: 计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。
        :type Bandwidth: int
        :param _Status: 监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :type Status: int
        :param _Port: 与监听器绑定的主机端口。
        :type Port: int
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._Bandwidth = None
        self._Status = None
        self._Port = None

    @property
    def ListenerId(self):
        r"""负载均衡监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""监听器协议类型，可选值：http，https，tcp，udp。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""监听器的监听端口。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Bandwidth(self):
        r"""计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Status(self):
        r"""监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Port(self):
        r"""与监听器绑定的主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Bandwidth = params.get("Bandwidth")
        self._Status = params.get("Status")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4BackendPortRequest(AbstractModel):
    r"""ModifyL4BackendPort请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。
        :type ListenerId: str
        :param _InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        :param _Port: 已绑定的主机端口。
        :type Port: int
        :param _NewPort: 新的主机端口，可选值1~65535。
        :type NewPort: int
        :param _BindType: 绑定类型。0：物理机  1：虚拟机 2：半托管机器
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._InstanceId = None
        self._Port = None
        self._NewPort = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def InstanceId(self):
        r"""黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        r"""已绑定的主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NewPort(self):
        r"""新的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._NewPort

    @NewPort.setter
    def NewPort(self, NewPort):
        self._NewPort = NewPort

    @property
    def BindType(self):
        r"""绑定类型。0：物理机  1：虚拟机 2：半托管机器
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._NewPort = params.get("NewPort")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4BackendPortResponse(AbstractModel):
    r"""ModifyL4BackendPort返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyL4BackendProbePortRequest(AbstractModel):
    r"""ModifyL4BackendProbePort请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        :param _Port: 已绑定的主机端口。
        :type Port: int
        :param _ProbePort: 新的探测端口，可选值1~65535。
        :type ProbePort: int
        :param _BindType: 绑定类型。0：物理机 1：虚拟机IP 2：半托管机器
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._InstanceId = None
        self._Port = None
        self._ProbePort = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""负载均衡四层监听器ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def InstanceId(self):
        r"""黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        r"""已绑定的主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ProbePort(self):
        r"""新的探测端口，可选值1~65535。
        :rtype: int
        """
        return self._ProbePort

    @ProbePort.setter
    def ProbePort(self, ProbePort):
        self._ProbePort = ProbePort

    @property
    def BindType(self):
        r"""绑定类型。0：物理机 1：虚拟机IP 2：半托管机器
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._ProbePort = params.get("ProbePort")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4BackendProbePortResponse(AbstractModel):
    r"""ModifyL4BackendProbePort返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyL4BackendWeightRequest(AbstractModel):
    r"""ModifyL4BackendWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。
        :type ListenerId: str
        :param _InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        :param _Weight: 权重信息，可选值0~100。
        :type Weight: int
        :param _Port: 已绑定的主机端口。
        :type Port: int
        :param _BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._InstanceId = None
        self._Weight = None
        self._Port = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def InstanceId(self):
        r"""黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        r"""权重信息，可选值0~100。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Port(self):
        r"""已绑定的主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def BindType(self):
        r"""绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        self._Port = params.get("Port")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4BackendWeightResponse(AbstractModel):
    r"""ModifyL4BackendWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyL4ListenerRequest(AbstractModel):
    r"""ModifyL4Listener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 四层监听器ID。可通过接口DescribeL4Listeners查询。
        :type ListenerId: str
        :param _ListenerName: 四层监听器名称。
        :type ListenerName: str
        :param _SessionExpire: 会话保持时间，单位：秒。可选值：900~3600。
        :type SessionExpire: int
        :param _HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）。默认值0，表示关闭。
        :type HealthSwitch: int
        :param _TimeOut: 健康检查的响应超时时间，可选值：2-60，默认值：2，单位:秒。<br><font color="red">响应超时时间要小于检查间隔时间。</font>
        :type TimeOut: int
        :param _IntervalTime: 健康检查间隔，默认值：5，可选值：5-300，单位：秒。
        :type IntervalTime: int
        :param _HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :type HealthNum: int
        :param _UnhealthNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :type UnhealthNum: int
        :param _Bandwidth: 监听器最大带宽值，用于计费模式为固定带宽计费。可选值：0-1000，单位：Mbps。
        :type Bandwidth: int
        :param _CustomHealthSwitch: 是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）
        :type CustomHealthSwitch: int
        :param _InputType: 自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。
        :type InputType: str
        :param _LineSeparatorType: 探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。
        :type LineSeparatorType: int
        :param _HealthRequest: 自定义探测请求内容。
        :type HealthRequest: str
        :param _HealthResponse: 自定义探测返回内容。
        :type HealthResponse: str
        :param _ToaFlag: 是否开启toa。可选值：0（关闭）、1（开启），默认关闭。（该字段在负载均衡为fullnat类型下才生效）
        :type ToaFlag: int
        :param _BalanceMode: 四层调度方式。wrr，wlc。
        :type BalanceMode: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._ListenerName = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._Bandwidth = None
        self._CustomHealthSwitch = None
        self._InputType = None
        self._LineSeparatorType = None
        self._HealthRequest = None
        self._HealthResponse = None
        self._ToaFlag = None
        self._BalanceMode = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""四层监听器ID。可通过接口DescribeL4Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""四层监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SessionExpire(self):
        r"""会话保持时间，单位：秒。可选值：900~3600。
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""是否开启健康检查：1（开启）、0（关闭）。默认值0，表示关闭。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        r"""健康检查的响应超时时间，可选值：2-60，默认值：2，单位:秒。<br><font color="red">响应超时时间要小于检查间隔时间。</font>
        :rtype: int
        """
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        r"""健康检查间隔，默认值：5，可选值：5-300，单位：秒。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def Bandwidth(self):
        r"""监听器最大带宽值，用于计费模式为固定带宽计费。可选值：0-1000，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def CustomHealthSwitch(self):
        r"""是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）
        :rtype: int
        """
        return self._CustomHealthSwitch

    @CustomHealthSwitch.setter
    def CustomHealthSwitch(self, CustomHealthSwitch):
        self._CustomHealthSwitch = CustomHealthSwitch

    @property
    def InputType(self):
        r"""自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def LineSeparatorType(self):
        r"""探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。
        :rtype: int
        """
        return self._LineSeparatorType

    @LineSeparatorType.setter
    def LineSeparatorType(self, LineSeparatorType):
        self._LineSeparatorType = LineSeparatorType

    @property
    def HealthRequest(self):
        r"""自定义探测请求内容。
        :rtype: str
        """
        return self._HealthRequest

    @HealthRequest.setter
    def HealthRequest(self, HealthRequest):
        self._HealthRequest = HealthRequest

    @property
    def HealthResponse(self):
        r"""自定义探测返回内容。
        :rtype: str
        """
        return self._HealthResponse

    @HealthResponse.setter
    def HealthResponse(self, HealthResponse):
        self._HealthResponse = HealthResponse

    @property
    def ToaFlag(self):
        r"""是否开启toa。可选值：0（关闭）、1（开启），默认关闭。（该字段在负载均衡为fullnat类型下才生效）
        :rtype: int
        """
        return self._ToaFlag

    @ToaFlag.setter
    def ToaFlag(self, ToaFlag):
        self._ToaFlag = ToaFlag

    @property
    def BalanceMode(self):
        r"""四层调度方式。wrr，wlc。
        :rtype: str
        """
        return self._BalanceMode

    @BalanceMode.setter
    def BalanceMode(self, BalanceMode):
        self._BalanceMode = BalanceMode


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._Bandwidth = params.get("Bandwidth")
        self._CustomHealthSwitch = params.get("CustomHealthSwitch")
        self._InputType = params.get("InputType")
        self._LineSeparatorType = params.get("LineSeparatorType")
        self._HealthRequest = params.get("HealthRequest")
        self._HealthResponse = params.get("HealthResponse")
        self._ToaFlag = params.get("ToaFlag")
        self._BalanceMode = params.get("BalanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4ListenerResponse(AbstractModel):
    r"""ModifyL4Listener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyL7BackendPortRequest(AbstractModel):
    r"""ModifyL7BackendPort请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。
        :type DomainId: str
        :param _LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。
        :type LocationId: str
        :param _InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        :param _Port: 已绑定的主机端口。
        :type Port: int
        :param _NewPort: 新的主机端口，可选值1~65535。
        :type NewPort: int
        :param _BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainId = None
        self._LocationId = None
        self._InstanceId = None
        self._Port = None
        self._NewPort = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainId(self):
        r"""转发域名实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LocationId(self):
        r"""转发路径实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def InstanceId(self):
        r"""黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        r"""已绑定的主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NewPort(self):
        r"""新的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._NewPort

    @NewPort.setter
    def NewPort(self, NewPort):
        self._NewPort = NewPort

    @property
    def BindType(self):
        r"""绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainId = params.get("DomainId")
        self._LocationId = params.get("LocationId")
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._NewPort = params.get("NewPort")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7BackendPortResponse(AbstractModel):
    r"""ModifyL7BackendPort返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyL7BackendWeightRequest(AbstractModel):
    r"""ModifyL7BackendWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。
        :type DomainId: str
        :param _LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。
        :type LocationId: str
        :param _InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        :param _Weight: 权重信息，可选值0~100。
        :type Weight: int
        :param _Port: 已绑定的主机端口。
        :type Port: int
        :param _BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainId = None
        self._LocationId = None
        self._InstanceId = None
        self._Weight = None
        self._Port = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainId(self):
        r"""转发域名实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LocationId(self):
        r"""转发路径实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def InstanceId(self):
        r"""黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        r"""权重信息，可选值0~100。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Port(self):
        r"""已绑定的主机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def BindType(self):
        r"""绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainId = params.get("DomainId")
        self._LocationId = params.get("LocationId")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        self._Port = params.get("Port")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7BackendWeightResponse(AbstractModel):
    r"""ModifyL7BackendWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyL7ListenerRequest(AbstractModel):
    r"""ModifyL7Listener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _ListenerName: 七层监听器名称。
        :type ListenerName: str
        :param _SslMode: 认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :type SslMode: int
        :param _CertId: 服务端证书ID。
        :type CertId: str
        :param _CertName: 服务端证书名称。
        :type CertName: str
        :param _CertContent: 服务端证书内容。
        :type CertContent: str
        :param _CertKey: 服务端证书密钥。
        :type CertKey: str
        :param _CertCaId: 客户端证书ID。
        :type CertCaId: str
        :param _CertCaName: 客户端证书名称。
        :type CertCaName: str
        :param _CertCaContent: 客户端证书内容。
        :type CertCaContent: str
        :param _Bandwidth: 计费模式为按固定带宽方式时监听器的限速值，可选值：0-1000，单位：Mbps。
        :type Bandwidth: int
        :param _ForwardProtocol: 转发协议。当监听器Protocol为https时并且SslMode为1或2时，有意义。可选的值为0：https，1：spdy，2：http2，3：spdy+http2。
        :type ForwardProtocol: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._ListenerName = None
        self._SslMode = None
        self._CertId = None
        self._CertName = None
        self._CertContent = None
        self._CertKey = None
        self._CertCaId = None
        self._CertCaName = None
        self._CertCaContent = None
        self._Bandwidth = None
        self._ForwardProtocol = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""七层监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SslMode(self):
        r"""认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :rtype: int
        """
        return self._SslMode

    @SslMode.setter
    def SslMode(self, SslMode):
        self._SslMode = SslMode

    @property
    def CertId(self):
        r"""服务端证书ID。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        r"""服务端证书名称。
        :rtype: str
        """
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertContent(self):
        r"""服务端证书内容。
        :rtype: str
        """
        return self._CertContent

    @CertContent.setter
    def CertContent(self, CertContent):
        self._CertContent = CertContent

    @property
    def CertKey(self):
        r"""服务端证书密钥。
        :rtype: str
        """
        return self._CertKey

    @CertKey.setter
    def CertKey(self, CertKey):
        self._CertKey = CertKey

    @property
    def CertCaId(self):
        r"""客户端证书ID。
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def CertCaName(self):
        r"""客户端证书名称。
        :rtype: str
        """
        return self._CertCaName

    @CertCaName.setter
    def CertCaName(self, CertCaName):
        self._CertCaName = CertCaName

    @property
    def CertCaContent(self):
        r"""客户端证书内容。
        :rtype: str
        """
        return self._CertCaContent

    @CertCaContent.setter
    def CertCaContent(self, CertCaContent):
        self._CertCaContent = CertCaContent

    @property
    def Bandwidth(self):
        r"""计费模式为按固定带宽方式时监听器的限速值，可选值：0-1000，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ForwardProtocol(self):
        r"""转发协议。当监听器Protocol为https时并且SslMode为1或2时，有意义。可选的值为0：https，1：spdy，2：http2，3：spdy+http2。
        :rtype: int
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SslMode = params.get("SslMode")
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._CertContent = params.get("CertContent")
        self._CertKey = params.get("CertKey")
        self._CertCaId = params.get("CertCaId")
        self._CertCaName = params.get("CertCaName")
        self._CertCaContent = params.get("CertCaContent")
        self._Bandwidth = params.get("Bandwidth")
        self._ForwardProtocol = params.get("ForwardProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7ListenerResponse(AbstractModel):
    r"""ModifyL7Listener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用[DescribeLoadBalancerTaskResult](/document/product/386/9308)接口来查询任务操作结果
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用[DescribeLoadBalancerTaskResult](/document/product/386/9308)接口来查询任务操作结果
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyL7LocationRule(AbstractModel):
    r"""修改黑石负载均衡七层转发路径时待修改的七层转发规则信息。

    """

    def __init__(self):
        r"""
        :param _DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。
        :type DomainId: str
        :param _LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。
        :type LocationId: str
        :param _Url: 转发路径。
        :type Url: str
        :param _SessionExpire: 会话保持时间，单位：秒。可选值：30~3600。默认值0，表示不开启会话保持。
        :type SessionExpire: int
        :param _HealthSwitch: 健康检查开关：1（开启）、0（关闭）。默认值0，表示关闭。
        :type HealthSwitch: int
        :param _IntervalTime: 健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。
        :type IntervalTime: int
        :param _HealthNum: 健康检查健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :type HealthNum: int
        :param _UnhealthNum: 健康检查不健康阈值，默认值：5，表示当连续探测五次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :type UnhealthNum: int
        :param _HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :type HttpCodes: list of int non-negative
        :param _HttpCheckPath: 健康检查检查路径。
        :type HttpCheckPath: str
        :param _HttpCheckDomain: 健康检查检查域名。如果规则的域名使用通配符或正则表达式，则健康检查检查域名可自定义，否则必须跟健康检查检查域名一样。不填表示不修改。
        :type HttpCheckDomain: str
        :param _BalanceMode: 均衡方式：ip_hash、wrr。默认值wrr。
        :type BalanceMode: str
        :param _Domain: 转发域名。
        :type Domain: str
        """
        self._DomainId = None
        self._LocationId = None
        self._Url = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._HttpCodes = None
        self._HttpCheckPath = None
        self._HttpCheckDomain = None
        self._BalanceMode = None
        self._Domain = None

    @property
    def DomainId(self):
        r"""转发域名实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LocationId(self):
        r"""转发路径实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Url(self):
        r"""转发路径。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def SessionExpire(self):
        r"""会话保持时间，单位：秒。可选值：30~3600。默认值0，表示不开启会话保持。
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""健康检查开关：1（开启）、0（关闭）。默认值0，表示关闭。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def IntervalTime(self):
        r"""健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""健康检查健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""健康检查不健康阈值，默认值：5，表示当连续探测五次不健康则表示该转发不正常，可选值：2-10，单位：次。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def HttpCodes(self):
        r"""健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :rtype: list of int non-negative
        """
        return self._HttpCodes

    @HttpCodes.setter
    def HttpCodes(self, HttpCodes):
        self._HttpCodes = HttpCodes

    @property
    def HttpCheckPath(self):
        r"""健康检查检查路径。
        :rtype: str
        """
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def HttpCheckDomain(self):
        r"""健康检查检查域名。如果规则的域名使用通配符或正则表达式，则健康检查检查域名可自定义，否则必须跟健康检查检查域名一样。不填表示不修改。
        :rtype: str
        """
        return self._HttpCheckDomain

    @HttpCheckDomain.setter
    def HttpCheckDomain(self, HttpCheckDomain):
        self._HttpCheckDomain = HttpCheckDomain

    @property
    def BalanceMode(self):
        r"""均衡方式：ip_hash、wrr。默认值wrr。
        :rtype: str
        """
        return self._BalanceMode

    @BalanceMode.setter
    def BalanceMode(self, BalanceMode):
        self._BalanceMode = BalanceMode

    @property
    def Domain(self):
        r"""转发域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._LocationId = params.get("LocationId")
        self._Url = params.get("Url")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._HttpCodes = params.get("HttpCodes")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._HttpCheckDomain = params.get("HttpCheckDomain")
        self._BalanceMode = params.get("BalanceMode")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7LocationsRequest(AbstractModel):
    r"""ModifyL7Locations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _RuleSet: 待更新的七层转发规则信息数组。
        :type RuleSet: list of ModifyL7LocationRule
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._RuleSet = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RuleSet(self):
        r"""待更新的七层转发规则信息数组。
        :rtype: list of ModifyL7LocationRule
        """
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = ModifyL7LocationRule()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7LocationsResponse(AbstractModel):
    r"""ModifyL7Locations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerChargeModeListener(AbstractModel):
    r"""修改负载均衡计费方式的监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _Protocol: 协议类型。
        :type Protocol: str
        :param _Bandwidth: 带宽。
        :type Bandwidth: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Bandwidth = None

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        r"""协议类型。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Bandwidth(self):
        r"""带宽。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerChargeModeRequest(AbstractModel):
    r"""ModifyLoadBalancerChargeMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _PayMode: 计费方式。flow或bandwidth。
        :type PayMode: str
        :param _ListenerSet: 监听器信息，当计费方式选为 bandwidth 且此负载均衡实例下存在监听器时需填入此字段，可以自定义每个监听器带宽上限。
        :type ListenerSet: list of ModifyLoadBalancerChargeModeListener
        """
        self._LoadBalancerId = None
        self._PayMode = None
        self._ListenerSet = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def PayMode(self):
        r"""计费方式。flow或bandwidth。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ListenerSet(self):
        r"""监听器信息，当计费方式选为 bandwidth 且此负载均衡实例下存在监听器时需填入此字段，可以自定义每个监听器带宽上限。
        :rtype: list of ModifyLoadBalancerChargeModeListener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._PayMode = params.get("PayMode")
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = ModifyLoadBalancerChargeModeListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerChargeModeResponse(AbstractModel):
    r"""ModifyLoadBalancerChargeMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerRequest(AbstractModel):
    r"""ModifyLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡器名称，规则：1-20个英文、汉字、数字、连接线“-”或下划线“_”。
        :type LoadBalancerName: str
        :param _DomainPrefix: 域名前缀，负载均衡的域名由用户输入的域名前缀与配置文件中的域名后缀一起组合而成，保证是唯一的域名。规则：1-20个小写英文字母、数字或连接线“-”。内网类型的负载均衡不能配置该字段。
        :type DomainPrefix: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._DomainPrefix = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""负载均衡器名称，规则：1-20个英文、汉字、数字、连接线“-”或下划线“_”。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def DomainPrefix(self):
        r"""域名前缀，负载均衡的域名由用户输入的域名前缀与配置文件中的域名后缀一起组合而成，保证是唯一的域名。规则：1-20个小写英文字母、数字或连接线“-”。内网类型的负载均衡不能配置该字段。
        :rtype: str
        """
        return self._DomainPrefix

    @DomainPrefix.setter
    def DomainPrefix(self, DomainPrefix):
        self._DomainPrefix = DomainPrefix


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._DomainPrefix = params.get("DomainPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerResponse(AbstractModel):
    r"""ModifyLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ReplaceCertRequest(AbstractModel):
    r"""ReplaceCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OldCertId: 要被替换的证书ID
        :type OldCertId: str
        :param _NewCert: 证书内容
        :type NewCert: str
        :param _NewAlias: 证书名称
        :type NewAlias: str
        :param _NewKey: 私钥内容，证书类型为SVR时不需要传递
        :type NewKey: str
        :param _DeleteOld: 是否删除旧证书，0 表示不删除，1 表示删除
        :type DeleteOld: int
        """
        self._OldCertId = None
        self._NewCert = None
        self._NewAlias = None
        self._NewKey = None
        self._DeleteOld = None

    @property
    def OldCertId(self):
        r"""要被替换的证书ID
        :rtype: str
        """
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def NewCert(self):
        r"""证书内容
        :rtype: str
        """
        return self._NewCert

    @NewCert.setter
    def NewCert(self, NewCert):
        self._NewCert = NewCert

    @property
    def NewAlias(self):
        r"""证书名称
        :rtype: str
        """
        return self._NewAlias

    @NewAlias.setter
    def NewAlias(self, NewAlias):
        self._NewAlias = NewAlias

    @property
    def NewKey(self):
        r"""私钥内容，证书类型为SVR时不需要传递
        :rtype: str
        """
        return self._NewKey

    @NewKey.setter
    def NewKey(self, NewKey):
        self._NewKey = NewKey

    @property
    def DeleteOld(self):
        r"""是否删除旧证书，0 表示不删除，1 表示删除
        :rtype: int
        """
        return self._DeleteOld

    @DeleteOld.setter
    def DeleteOld(self, DeleteOld):
        self._DeleteOld = DeleteOld


    def _deserialize(self, params):
        self._OldCertId = params.get("OldCertId")
        self._NewCert = params.get("NewCert")
        self._NewAlias = params.get("NewAlias")
        self._NewKey = params.get("NewKey")
        self._DeleteOld = params.get("DeleteOld")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertResponse(AbstractModel):
    r"""ReplaceCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NewCertId: 新证书ID。
        :type NewCertId: str
        :param _OldCertId: 旧证书ID。
        :type OldCertId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NewCertId = None
        self._OldCertId = None
        self._RequestId = None

    @property
    def NewCertId(self):
        r"""新证书ID。
        :rtype: str
        """
        return self._NewCertId

    @NewCertId.setter
    def NewCertId(self, NewCertId):
        self._NewCertId = NewCertId

    @property
    def OldCertId(self):
        r"""旧证书ID。
        :rtype: str
        """
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NewCertId = params.get("NewCertId")
        self._OldCertId = params.get("OldCertId")
        self._RequestId = params.get("RequestId")


class SetTrafficMirrorAliasRequest(AbstractModel):
    r"""SetTrafficMirrorAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID。
        :type TrafficMirrorId: str
        :param _Alias: 流量镜像实例别名。
        :type Alias: str
        """
        self._TrafficMirrorId = None
        self._Alias = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def Alias(self):
        r"""流量镜像实例别名。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTrafficMirrorAliasResponse(AbstractModel):
    r"""SetTrafficMirrorAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetTrafficMirrorHealthSwitchRequest(AbstractModel):
    r"""SetTrafficMirrorHealthSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID。
        :type TrafficMirrorId: str
        :param _HealthSwitch: 健康检查开关，0：关闭，1：打开
        :type HealthSwitch: int
        :param _HealthNum: 健康检查判断健康的次数，最小值2，最大值10。
        :type HealthNum: int
        :param _UnhealthNum: 健康检查判断不健康的次数，最小值2，最大值10。
        :type UnhealthNum: int
        :param _IntervalTime: 健康检查间隔，单位：秒，最小值5，最大值300。
        :type IntervalTime: int
        :param _HttpCheckDomain: 检查的域名配置。
        :type HttpCheckDomain: str
        :param _HttpCheckPath: 检查的路径配置。
        :type HttpCheckPath: str
        :param _HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :type HttpCodes: list of int
        """
        self._TrafficMirrorId = None
        self._HealthSwitch = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._IntervalTime = None
        self._HttpCheckDomain = None
        self._HttpCheckPath = None
        self._HttpCodes = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def HealthSwitch(self):
        r"""健康检查开关，0：关闭，1：打开
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def HealthNum(self):
        r"""健康检查判断健康的次数，最小值2，最大值10。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""健康检查判断不健康的次数，最小值2，最大值10。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def IntervalTime(self):
        r"""健康检查间隔，单位：秒，最小值5，最大值300。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HttpCheckDomain(self):
        r"""检查的域名配置。
        :rtype: str
        """
        return self._HttpCheckDomain

    @HttpCheckDomain.setter
    def HttpCheckDomain(self, HttpCheckDomain):
        self._HttpCheckDomain = HttpCheckDomain

    @property
    def HttpCheckPath(self):
        r"""检查的路径配置。
        :rtype: str
        """
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def HttpCodes(self):
        r"""健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。
        :rtype: list of int
        """
        return self._HttpCodes

    @HttpCodes.setter
    def HttpCodes(self, HttpCodes):
        self._HttpCodes = HttpCodes


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._HealthSwitch = params.get("HealthSwitch")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._IntervalTime = params.get("IntervalTime")
        self._HttpCheckDomain = params.get("HttpCheckDomain")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._HttpCodes = params.get("HttpCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTrafficMirrorHealthSwitchResponse(AbstractModel):
    r"""SetTrafficMirrorHealthSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class TrafficMirror(AbstractModel):
    r"""获取流量镜像实例的列表信息时返回的流量镜像信息。

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像ID。
        :type TrafficMirrorId: str
        :param _Alias: 流量镜像名称。
        :type Alias: str
        :param _VpcId: 流量镜像所在的私有网络ID。
        :type VpcId: str
        :param _LoadBalancerType: 接收机负载均衡方式。wrr，ip_hash，wlc。
        :type LoadBalancerType: str
        :param _HealthSwitch: 是否开始对接收机的健康检查。0：关闭，非0：开启。
        :type HealthSwitch: int
        :param _HealthNum: 健康阈值。
        :type HealthNum: int
        :param _UnhealthNum: 不健康阈值。
        :type UnhealthNum: int
        :param _IntervalTime: 检查间隔。
        :type IntervalTime: int
        :param _HttpCheckDomain: 检查域名。
        :type HttpCheckDomain: str
        :param _HttpCheckPath: 检查目录。
        :type HttpCheckPath: str
        :param _HttpCodes: 健康检查返回码。 1：1xx，2：2xx，3：3xx，4：4xx，5：5xx。
        :type HttpCodes: list of int
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _VpcCidrBlock: 流量镜像所在私有网络的Cidr。
        :type VpcCidrBlock: str
        :param _VpcName: 流量镜像所在私有网络的名称。
        :type VpcName: str
        """
        self._TrafficMirrorId = None
        self._Alias = None
        self._VpcId = None
        self._LoadBalancerType = None
        self._HealthSwitch = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._IntervalTime = None
        self._HttpCheckDomain = None
        self._HttpCheckPath = None
        self._HttpCodes = None
        self._CreateTime = None
        self._VpcCidrBlock = None
        self._VpcName = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def Alias(self):
        r"""流量镜像名称。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def VpcId(self):
        r"""流量镜像所在的私有网络ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def LoadBalancerType(self):
        r"""接收机负载均衡方式。wrr，ip_hash，wlc。
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def HealthSwitch(self):
        r"""是否开始对接收机的健康检查。0：关闭，非0：开启。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def HealthNum(self):
        r"""健康阈值。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        r"""不健康阈值。
        :rtype: int
        """
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def IntervalTime(self):
        r"""检查间隔。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HttpCheckDomain(self):
        r"""检查域名。
        :rtype: str
        """
        return self._HttpCheckDomain

    @HttpCheckDomain.setter
    def HttpCheckDomain(self, HttpCheckDomain):
        self._HttpCheckDomain = HttpCheckDomain

    @property
    def HttpCheckPath(self):
        r"""检查目录。
        :rtype: str
        """
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def HttpCodes(self):
        r"""健康检查返回码。 1：1xx，2：2xx，3：3xx，4：4xx，5：5xx。
        :rtype: list of int
        """
        return self._HttpCodes

    @HttpCodes.setter
    def HttpCodes(self, HttpCodes):
        self._HttpCodes = HttpCodes

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VpcCidrBlock(self):
        r"""流量镜像所在私有网络的Cidr。
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def VpcName(self):
        r"""流量镜像所在私有网络的名称。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._Alias = params.get("Alias")
        self._VpcId = params.get("VpcId")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._HealthSwitch = params.get("HealthSwitch")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._IntervalTime = params.get("IntervalTime")
        self._HttpCheckDomain = params.get("HttpCheckDomain")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._HttpCodes = params.get("HttpCodes")
        self._CreateTime = params.get("CreateTime")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficMirrorListener(AbstractModel):
    r"""获取流量镜像的监听器列表信息时返回的与流量镜像绑定的监听器信息。

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ListenerName: 监听器名称。
        :type ListenerName: str
        :param _Protocol: 七层监听器协议类型，可选值：http,https。
        :type Protocol: str
        :param _LoadBalancerPort: 监听器的监听端口。
        :type LoadBalancerPort: int
        :param _Bandwidth: 当前带宽。
        :type Bandwidth: int
        :param _MaxBandwidth: 带宽上限。
        :type MaxBandwidth: int
        :param _ListenerType: 监听器类型。
        :type ListenerType: str
        :param _SslMode: 认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :type SslMode: int
        :param _CertId: 服务端证书ID。
        :type CertId: str
        :param _CertCaId: 客户端证书ID。
        :type CertCaId: str
        :param _AddTimestamp: 添加时间。
        :type AddTimestamp: str
        :param _LoadBalancerId: 负载均衡ID。
        :type LoadBalancerId: str
        :param _VpcName: 私有网络名称。
        :type VpcName: str
        :param _VpcCidrBlock: 私有网络Cidr。
        :type VpcCidrBlock: str
        :param _LoadBalancerVips: 负载均衡的VIP。
        :type LoadBalancerVips: list of str
        :param _LoadBalancerName: 负载均衡名称。
        :type LoadBalancerName: str
        :param _LoadBalancerVipv6s: 负载均衡的IPV6的VIP。
        :type LoadBalancerVipv6s: list of str
        :param _IpProtocolType: 支持的IP协议类型。ipv4或者是ipv6。
        :type IpProtocolType: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._LoadBalancerPort = None
        self._Bandwidth = None
        self._MaxBandwidth = None
        self._ListenerType = None
        self._SslMode = None
        self._CertId = None
        self._CertCaId = None
        self._AddTimestamp = None
        self._LoadBalancerId = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._LoadBalancerVips = None
        self._LoadBalancerName = None
        self._LoadBalancerVipv6s = None
        self._IpProtocolType = None

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""七层监听器协议类型，可选值：http,https。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def LoadBalancerPort(self):
        r"""监听器的监听端口。
        :rtype: int
        """
        return self._LoadBalancerPort

    @LoadBalancerPort.setter
    def LoadBalancerPort(self, LoadBalancerPort):
        self._LoadBalancerPort = LoadBalancerPort

    @property
    def Bandwidth(self):
        r"""当前带宽。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def MaxBandwidth(self):
        r"""带宽上限。
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def ListenerType(self):
        r"""监听器类型。
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def SslMode(self):
        r"""认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。
        :rtype: int
        """
        return self._SslMode

    @SslMode.setter
    def SslMode(self, SslMode):
        self._SslMode = SslMode

    @property
    def CertId(self):
        r"""服务端证书ID。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        r"""客户端证书ID。
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def AddTimestamp(self):
        r"""添加时间。
        :rtype: str
        """
        return self._AddTimestamp

    @AddTimestamp.setter
    def AddTimestamp(self, AddTimestamp):
        self._AddTimestamp = AddTimestamp

    @property
    def LoadBalancerId(self):
        r"""负载均衡ID。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def VpcName(self):
        r"""私有网络名称。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        r"""私有网络Cidr。
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def LoadBalancerVips(self):
        r"""负载均衡的VIP。
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def LoadBalancerName(self):
        r"""负载均衡名称。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerVipv6s(self):
        r"""负载均衡的IPV6的VIP。
        :rtype: list of str
        """
        return self._LoadBalancerVipv6s

    @LoadBalancerVipv6s.setter
    def LoadBalancerVipv6s(self, LoadBalancerVipv6s):
        self._LoadBalancerVipv6s = LoadBalancerVipv6s

    @property
    def IpProtocolType(self):
        r"""支持的IP协议类型。ipv4或者是ipv6。
        :rtype: str
        """
        return self._IpProtocolType

    @IpProtocolType.setter
    def IpProtocolType(self, IpProtocolType):
        self._IpProtocolType = IpProtocolType


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._LoadBalancerPort = params.get("LoadBalancerPort")
        self._Bandwidth = params.get("Bandwidth")
        self._MaxBandwidth = params.get("MaxBandwidth")
        self._ListenerType = params.get("ListenerType")
        self._SslMode = params.get("SslMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._AddTimestamp = params.get("AddTimestamp")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self._IpProtocolType = params.get("IpProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficMirrorPortStatus(AbstractModel):
    r"""流量镜像健康检查返回的接收机的端口及状态信息。

    """

    def __init__(self):
        r"""
        :param _Port: 接收机端口。
        :type Port: int
        :param _Status: 状态。
        :type Status: str
        """
        self._Port = None
        self._Status = None

    @property
    def Port(self):
        r"""接收机端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        r"""状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficMirrorReceiver(AbstractModel):
    r"""获取与流量镜像绑定的接收机信息时返回的接收机信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 接收机实例ID。
        :type InstanceId: str
        :param _Port: 接收机接收端口。
        :type Port: int
        :param _Weight: 接收机权重。
        :type Weight: int
        :param _TrafficMirrorId: 流量镜像ID。
        :type TrafficMirrorId: str
        :param _Alias: 接收机别名。
        :type Alias: str
        :param _LanIp: 接收机内网IP地址。
        :type LanIp: str
        :param _SubnetId: 接收机所在的子网的ID。
        :type SubnetId: str
        :param _SubnetName: 接收机所在的子网的名称。
        :type SubnetName: str
        :param _SubnetCidrBlock: 接收机所在的子网的Cidr。
        :type SubnetCidrBlock: str
        :param _VpcId: 接收机所在的私有网络的ID。
        :type VpcId: str
        :param _VpcName: 接收机所在的私有网络的名称。
        :type VpcName: str
        :param _VpcCidrBlock: 接收机所在的私有网络的Cidr。
        :type VpcCidrBlock: str
        :param _HealthStatus: 接收机的健康状态。
        :type HealthStatus: str
        :param _Operates: 接收机的可以执行的操作集合。
        :type Operates: list of str
        """
        self._InstanceId = None
        self._Port = None
        self._Weight = None
        self._TrafficMirrorId = None
        self._Alias = None
        self._LanIp = None
        self._SubnetId = None
        self._SubnetName = None
        self._SubnetCidrBlock = None
        self._VpcId = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._HealthStatus = None
        self._Operates = None

    @property
    def InstanceId(self):
        r"""接收机实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        r"""接收机接收端口。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        r"""接收机权重。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def TrafficMirrorId(self):
        r"""流量镜像ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def Alias(self):
        r"""接收机别名。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def LanIp(self):
        r"""接收机内网IP地址。
        :rtype: str
        """
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def SubnetId(self):
        r"""接收机所在的子网的ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        r"""接收机所在的子网的名称。
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetCidrBlock(self):
        r"""接收机所在的子网的Cidr。
        :rtype: str
        """
        return self._SubnetCidrBlock

    @SubnetCidrBlock.setter
    def SubnetCidrBlock(self, SubnetCidrBlock):
        self._SubnetCidrBlock = SubnetCidrBlock

    @property
    def VpcId(self):
        r"""接收机所在的私有网络的ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""接收机所在的私有网络的名称。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        r"""接收机所在的私有网络的Cidr。
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def HealthStatus(self):
        r"""接收机的健康状态。
        :rtype: str
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def Operates(self):
        r"""接收机的可以执行的操作集合。
        :rtype: list of str
        """
        return self._Operates

    @Operates.setter
    def Operates(self, Operates):
        self._Operates = Operates


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._Alias = params.get("Alias")
        self._LanIp = params.get("LanIp")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._SubnetCidrBlock = params.get("SubnetCidrBlock")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._HealthStatus = params.get("HealthStatus")
        self._Operates = params.get("Operates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficMirrorReciversStatus(AbstractModel):
    r"""流量镜像健康检查返回的接收机状态信息。

    """

    def __init__(self):
        r"""
        :param _LanIp: 内网IP。
        :type LanIp: str
        :param _ReceiversPortStatusSet: 端口及对应的状态。
        :type ReceiversPortStatusSet: list of TrafficMirrorPortStatus
        """
        self._LanIp = None
        self._ReceiversPortStatusSet = None

    @property
    def LanIp(self):
        r"""内网IP。
        :rtype: str
        """
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def ReceiversPortStatusSet(self):
        r"""端口及对应的状态。
        :rtype: list of TrafficMirrorPortStatus
        """
        return self._ReceiversPortStatusSet

    @ReceiversPortStatusSet.setter
    def ReceiversPortStatusSet(self, ReceiversPortStatusSet):
        self._ReceiversPortStatusSet = ReceiversPortStatusSet


    def _deserialize(self, params):
        self._LanIp = params.get("LanIp")
        if params.get("ReceiversPortStatusSet") is not None:
            self._ReceiversPortStatusSet = []
            for item in params.get("ReceiversPortStatusSet"):
                obj = TrafficMirrorPortStatus()
                obj._deserialize(item)
                self._ReceiversPortStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL4Backend(AbstractModel):
    r"""待与四层监听器解绑的物理机主机、虚拟机或半托管主机信息。

    """

    def __init__(self):
        r"""
        :param _Port: 待解绑的主机端口，可选值1~65535。
        :type Port: int
        :param _InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        """
        self._Port = None
        self._InstanceId = None

    @property
    def Port(self):
        r"""待解绑的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        r"""黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL4BackendsRequest(AbstractModel):
    r"""UnbindL4Backends请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。
        :type ListenerId: str
        :param _BackendSet: 待解绑的主机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。
        :type BackendSet: list of UnbindL4Backend
        :param _BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._BackendSet = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def BackendSet(self):
        r"""待解绑的主机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。
        :rtype: list of UnbindL4Backend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet

    @property
    def BindType(self):
        r"""绑定类型。0：物理机 1：虚拟机 2：半托管机器
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = UnbindL4Backend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL4BackendsResponse(AbstractModel):
    r"""UnbindL4Backends返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UnbindL7Backend(AbstractModel):
    r"""待与七层监听器转发规则解绑的物理机主机、虚拟机或半托管主机信息。

    """

    def __init__(self):
        r"""
        :param _Port: 待解绑的主机端口，可选值1~65535。
        :type Port: int
        :param _InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :type InstanceId: str
        """
        self._Port = None
        self._InstanceId = None

    @property
    def Port(self):
        r"""待解绑的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        r"""黑石物理机主机ID、虚拟机IP或者是半托管主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL7BackendsRequest(AbstractModel):
    r"""UnbindL7Backends请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :type LoadBalancerId: str
        :param _ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :type ListenerId: str
        :param _DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。
        :type DomainId: str
        :param _LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。
        :type LocationId: str
        :param _BackendSet: 待绑定的主机信息。
        :type BackendSet: list of UnbindL7Backend
        :param _BindType: 绑定类型。0：物理机  1：虚拟机 2：半托管机器
        :type BindType: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainId = None
        self._LocationId = None
        self._BackendSet = None
        self._BindType = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例ID，可通过接口DescribeLoadBalancers查询。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""七层监听器实例ID，可通过接口DescribeL7Listeners查询。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainId(self):
        r"""转发域名实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LocationId(self):
        r"""转发路径实例ID，可通过接口DescribeL7Rules查询。
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def BackendSet(self):
        r"""待绑定的主机信息。
        :rtype: list of UnbindL7Backend
        """
        return self._BackendSet

    @BackendSet.setter
    def BackendSet(self, BackendSet):
        self._BackendSet = BackendSet

    @property
    def BindType(self):
        r"""绑定类型。0：物理机  1：虚拟机 2：半托管机器
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainId = params.get("DomainId")
        self._LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self._BackendSet = []
            for item in params.get("BackendSet"):
                obj = UnbindL7Backend()
                obj._deserialize(item)
                self._BackendSet.append(obj)
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL7BackendsResponse(AbstractModel):
    r"""UnbindL7Backends返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UnbindTrafficMirrorListenersRequest(AbstractModel):
    r"""UnbindTrafficMirrorListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID。
        :type TrafficMirrorId: str
        :param _ListenerIds: 七层监听器实例ID数组，可通过接口DescribeL7Listeners查询。
        :type ListenerIds: list of str
        """
        self._TrafficMirrorId = None
        self._ListenerIds = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def ListenerIds(self):
        r"""七层监听器实例ID数组，可通过接口DescribeL7Listeners查询。
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        self._ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindTrafficMirrorListenersResponse(AbstractModel):
    r"""UnbindTrafficMirrorListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UnbindTrafficMirrorReceiver(AbstractModel):
    r"""待与流量镜像解绑的接收机信息。

    """

    def __init__(self):
        r"""
        :param _Port: 待解绑的主机端口，可选值1~65535。
        :type Port: int
        :param _InstanceId: 待解绑的主机实例ID。
        :type InstanceId: str
        """
        self._Port = None
        self._InstanceId = None

    @property
    def Port(self):
        r"""待解绑的主机端口，可选值1~65535。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        r"""待解绑的主机实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindTrafficMirrorReceiversRequest(AbstractModel):
    r"""UnbindTrafficMirrorReceivers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrafficMirrorId: 流量镜像实例ID。
        :type TrafficMirrorId: str
        :param _ReceiverSet: 待绑定的主机实例ID和端口数组。
        :type ReceiverSet: list of UnbindTrafficMirrorReceiver
        """
        self._TrafficMirrorId = None
        self._ReceiverSet = None

    @property
    def TrafficMirrorId(self):
        r"""流量镜像实例ID。
        :rtype: str
        """
        return self._TrafficMirrorId

    @TrafficMirrorId.setter
    def TrafficMirrorId(self, TrafficMirrorId):
        self._TrafficMirrorId = TrafficMirrorId

    @property
    def ReceiverSet(self):
        r"""待绑定的主机实例ID和端口数组。
        :rtype: list of UnbindTrafficMirrorReceiver
        """
        return self._ReceiverSet

    @ReceiverSet.setter
    def ReceiverSet(self, ReceiverSet):
        self._ReceiverSet = ReceiverSet


    def _deserialize(self, params):
        self._TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self._ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = UnbindTrafficMirrorReceiver()
                obj._deserialize(item)
                self._ReceiverSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindTrafficMirrorReceiversResponse(AbstractModel):
    r"""UnbindTrafficMirrorReceivers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UploadCertRequest(AbstractModel):
    r"""UploadCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertType: 证书类型，可选值：CA，SVR。
        :type CertType: str
        :param _Cert: 证书内容。
        :type Cert: str
        :param _Alias: 证书别名。
        :type Alias: str
        :param _Key: 私钥内容，证书类型为SVR时不需要传递。
        :type Key: str
        """
        self._CertType = None
        self._Cert = None
        self._Alias = None
        self._Key = None

    @property
    def CertType(self):
        r"""证书类型，可选值：CA，SVR。
        :rtype: str
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Cert(self):
        r"""证书内容。
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def Alias(self):
        r"""证书别名。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Key(self):
        r"""私钥内容，证书类型为SVR时不需要传递。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._CertType = params.get("CertType")
        self._Cert = params.get("Cert")
        self._Alias = params.get("Alias")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertResponse(AbstractModel):
    r"""UploadCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: 新建的证书ID。
        :type CertId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertId = None
        self._RequestId = None

    @property
    def CertId(self):
        r"""新建的证书ID。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._RequestId = params.get("RequestId")