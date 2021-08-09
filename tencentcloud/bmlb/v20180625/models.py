# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
    """待与四层监听器绑定的物理机主机、虚拟机或半托管主机信息。目前一个四层监听器下面最多允许绑定255个主机端口。

    """

    def __init__(self):
        """
        :param Port: 待绑定的主机端口，可选值1~65535。\n        :type Port: int\n        :param InstanceId: 待绑定的黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        :param Weight: 待绑定的主机权重，可选值0~100。\n        :type Weight: int\n        :param ProbePort: 自定义探测的主机端口，可选值1~65535。（需要监听器开启自定义健康检查）\n        :type ProbePort: int\n        """
        self.Port = None
        self.InstanceId = None
        self.Weight = None
        self.ProbePort = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.ProbePort = params.get("ProbePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindL4BackendsRequest(AbstractModel):
    """BindL4Backends请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 四层监听器实例ID，可通过接口DescribeL4Listeners查询。\n        :type ListenerId: str\n        :param BackendSet: 待绑定的主机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。\n        :type BackendSet: list of BindL4Backend\n        :param BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.BackendSet = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = BindL4Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindL4BackendsResponse(AbstractModel):
    """BindL4Backends返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindL7Backend(AbstractModel):
    """待与七层监听器转发规则绑定的物理机主机、虚拟机或半托管主机信息。目前一个七层转发路径下面最多允许绑定255个主机端口。

    """

    def __init__(self):
        """
        :param Port: 待绑定的主机端口，可选值1~65535。\n        :type Port: int\n        :param InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        :param Weight: 待绑定的主机权重，可选值0~100。\n        :type Weight: int\n        """
        self.Port = None
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindL7BackendsRequest(AbstractModel):
    """BindL7Backends请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。\n        :type DomainId: str\n        :param LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。\n        :type LocationId: str\n        :param BackendSet: 待绑定的主机信息。可以绑定多个主机端口。目前一个七层转发路径下面最多允许绑定255个主机端口。\n        :type BackendSet: list of BindL7Backend\n        :param BindType: 绑定类型。0：物理机，1：虚拟机 2：半托管机器。\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.BackendSet = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = BindL7Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindL7BackendsResponse(AbstractModel):
    """BindL7Backends返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindTrafficMirrorListenersRequest(AbstractModel):
    """BindTrafficMirrorListeners请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID。\n        :type TrafficMirrorId: str\n        :param ListenerIds: 七层监听器实例ID数组，可通过接口DescribeL7Listeners查询。\n        :type ListenerIds: list of str\n        """
        self.TrafficMirrorId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindTrafficMirrorListenersResponse(AbstractModel):
    """BindTrafficMirrorListeners返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindTrafficMirrorReceiver(AbstractModel):
    """待与流量镜像绑定的接收机信息。

    """

    def __init__(self):
        """
        :param Port: 待绑定的主机端口，可选值1~65535。\n        :type Port: int\n        :param InstanceId: 待绑定的主机实例ID。\n        :type InstanceId: str\n        :param Weight: 待绑定的主机权重，可选值0~100。\n        :type Weight: int\n        """
        self.Port = None
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindTrafficMirrorReceiversRequest(AbstractModel):
    """BindTrafficMirrorReceivers请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID。\n        :type TrafficMirrorId: str\n        :param ReceiverSet: 待绑定的黑石物理机信息数组。\n        :type ReceiverSet: list of BindTrafficMirrorReceiver\n        """
        self.TrafficMirrorId = None
        self.ReceiverSet = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self.ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = BindTrafficMirrorReceiver()
                obj._deserialize(item)
                self.ReceiverSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindTrafficMirrorReceiversResponse(AbstractModel):
    """BindTrafficMirrorReceivers返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CertDetailLoadBalancer(AbstractModel):
    """获取证书信息时返回的所用在的负载均衡信息。

    """

    def __init__(self):
        """
        :param LoadBalancerId: 黑石负载均衡实例ID。\n        :type LoadBalancerId: str\n        :param LoadBalancerName: 黑石负载均衡实例名称。\n        :type LoadBalancerName: str\n        :param VpcId: 该黑石负载均衡所在的VpcId。\n        :type VpcId: str\n        :param RegionId: 该黑石负载均衡所在的regionId。\n        :type RegionId: int\n        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.RegionId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4Listener(AbstractModel):
    """用于创建四层监听器的监听器信息。目前一个负载均衡下面最多允许创建50个监听器。

    """

    def __init__(self):
        """
        :param LoadBalancerPort: 监听器监听端口，可选值1~65535。\n        :type LoadBalancerPort: int\n        :param Protocol: 监听器协议类型，可选值tcp，udp。\n        :type Protocol: str\n        :param ListenerName: 监听器名称。\n        :type ListenerName: str\n        :param SessionExpire: 监听器的会话保持时间，单位：秒。可选值：900~3600,不传表示不开启会话保持。\n        :type SessionExpire: int\n        :param HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）。默认值0，表示关闭。\n        :type HealthSwitch: int\n        :param TimeOut: 健康检查的响应超时时间，可选值：2-60，默认值：2，单位:秒。<br><font color="red">响应超时时间要小于检查间隔时间。</font>\n        :type TimeOut: int\n        :param IntervalTime: 健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。\n        :type IntervalTime: int\n        :param HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。\n        :type HealthNum: int\n        :param UnhealthNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。\n        :type UnhealthNum: int\n        :param Bandwidth: 监听器最大带宽值，用于计费模式为固定带宽计费，可选值：0-1000，单位：Mbps。\n        :type Bandwidth: int\n        :param CustomHealthSwitch: 是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）\n        :type CustomHealthSwitch: int\n        :param InputType: 自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。\n        :type InputType: str\n        :param LineSeparatorType: 探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。\n        :type LineSeparatorType: int\n        :param HealthRequest: 自定义探测请求内容。\n        :type HealthRequest: str\n        :param HealthResponse: 自定义探测返回内容。\n        :type HealthResponse: str\n        :param ToaFlag: 是否开启toa。可选值：0（关闭）、1（开启），默认关闭。（该字段在负载均衡为fullnat类型下才生效）\n        :type ToaFlag: int\n        """
        self.LoadBalancerPort = None
        self.Protocol = None
        self.ListenerName = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.Bandwidth = None
        self.CustomHealthSwitch = None
        self.InputType = None
        self.LineSeparatorType = None
        self.HealthRequest = None
        self.HealthResponse = None
        self.ToaFlag = None


    def _deserialize(self, params):
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Protocol = params.get("Protocol")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.Bandwidth = params.get("Bandwidth")
        self.CustomHealthSwitch = params.get("CustomHealthSwitch")
        self.InputType = params.get("InputType")
        self.LineSeparatorType = params.get("LineSeparatorType")
        self.HealthRequest = params.get("HealthRequest")
        self.HealthResponse = params.get("HealthResponse")
        self.ToaFlag = params.get("ToaFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4ListenersRequest(AbstractModel):
    """CreateL4Listeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerSet: 监听器信息数组，可以创建多个监听器。目前一个负载均衡下面最多允许创建50个监听器\n        :type ListenerSet: list of CreateL4Listener\n        """
        self.LoadBalancerId = None
        self.ListenerSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = CreateL4Listener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4ListenersResponse(AbstractModel):
    """CreateL4Listeners返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateL7Listener(AbstractModel):
    """用于创建四层监听器的监听器信息。目前一个负载均衡下面最多允许创建50个七层监听器。

    """

    def __init__(self):
        """
        :param LoadBalancerPort: 七层监听器端口，可选值1~65535。\n        :type LoadBalancerPort: int\n        :param Protocol: 七层监听器协议类型，可选值：http,https。\n        :type Protocol: str\n        :param ListenerName: 七层监听器名称。\n        :type ListenerName: str\n        :param SslMode: 认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。当创建的是https类型的监听器时，此值必选。\n        :type SslMode: int\n        :param CertId: 服务端证书ID。当创建的是https类型的监听器时，此值必选。\n        :type CertId: str\n        :param CertName: 服务端证书名称。\n        :type CertName: str\n        :param CertContent: 服务端证书内容。\n        :type CertContent: str\n        :param CertKey: 服务端证书密钥。\n        :type CertKey: str\n        :param CertCaId: 客户端证书ID。\n        :type CertCaId: str\n        :param CertCaName: 客户端证书名称。\n        :type CertCaName: str\n        :param CertCaContent: 客户端证书内容。\n        :type CertCaContent: str\n        :param Bandwidth: 用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。\n        :type Bandwidth: int\n        :param ForwardProtocol: 转发协议。当Protocol为https时并且SslMode为1或2时，有意义。可选的值为0：https，1：spdy，2：http2，3：spdy+http2。\n        :type ForwardProtocol: int\n        """
        self.LoadBalancerPort = None
        self.Protocol = None
        self.ListenerName = None
        self.SslMode = None
        self.CertId = None
        self.CertName = None
        self.CertContent = None
        self.CertKey = None
        self.CertCaId = None
        self.CertCaName = None
        self.CertCaContent = None
        self.Bandwidth = None
        self.ForwardProtocol = None


    def _deserialize(self, params):
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Protocol = params.get("Protocol")
        self.ListenerName = params.get("ListenerName")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.CertContent = params.get("CertContent")
        self.CertKey = params.get("CertKey")
        self.CertCaId = params.get("CertCaId")
        self.CertCaName = params.get("CertCaName")
        self.CertCaContent = params.get("CertCaContent")
        self.Bandwidth = params.get("Bandwidth")
        self.ForwardProtocol = params.get("ForwardProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7ListenersRequest(AbstractModel):
    """CreateL7Listeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID\n        :type LoadBalancerId: str\n        :param ListenerSet: 七层监听器信息数组，可以创建多个七层监听器。目前一个负载均衡下面最多允许创建50个七层监听器。\n        :type ListenerSet: list of CreateL7Listener\n        """
        self.LoadBalancerId = None
        self.ListenerSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = CreateL7Listener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7ListenersResponse(AbstractModel):
    """CreateL7Listeners返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerIds: 新建的负载均衡七层监听器的唯一ID列表。\n        :type ListenerIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateL7Rule(AbstractModel):
    """用于创建七层监听器的转发规则的信息。目前一个七层监听器下面最多允许创建50个七层转发域名，而每一个转发域名下最多可以创建100个转发规则。

    """

    def __init__(self):
        """
        :param Domain: 七层转发规则的转发域名。\n        :type Domain: str\n        :param Url: 七层转发规则的转发路径。\n        :type Url: str\n        :param SessionExpire: 会话保持时间，单位：秒。可选值：30~3600。默认值0，表示不开启会话保持。\n        :type SessionExpire: int\n        :param HealthSwitch: 健康检查开关：1（开启）、0（关闭）。默认值0，表示关闭。\n        :type HealthSwitch: int\n        :param IntervalTime: 健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。\n        :type IntervalTime: int\n        :param HealthNum: 健康检查健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。\n        :type HealthNum: int\n        :param UnhealthNum: 健康检查不健康阈值，默认值：5，表示当连续探测五次不健康则表示该转发不正常，可选值：2-10，单位：次。\n        :type UnhealthNum: int\n        :param HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。\n        :type HttpCodes: list of int non-negative\n        :param HttpCheckPath: 健康检查检查路径。\n        :type HttpCheckPath: str\n        :param HttpCheckDomain: 健康检查检查域名。如果创建规则的域名使用通配符或正则表达式，则健康检查检查域名可自定义，否则必须跟健康检查检查域名一样。\n        :type HttpCheckDomain: str\n        :param BalanceMode: 均衡方式：ip_hash、wrr。默认值wrr。\n        :type BalanceMode: str\n        """
        self.Domain = None
        self.Url = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpCodes = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.BalanceMode = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpCodes = params.get("HttpCodes")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.BalanceMode = params.get("BalanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesRequest(AbstractModel):
    """CreateL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param RuleSet: 七层转发规则信息数组，可以创建多个七层转发规则。目前一个七层监听器下面最多允许创建50个七层转发域名，而每一个转发域名下最多可以创建100个转发规则。目前只能单条创建，不能批量创建。\n        :type RuleSet: list of CreateL7Rule\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.RuleSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = CreateL7Rule()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesResponse(AbstractModel):
    """CreateL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerBzConf(AbstractModel):
    """用于创建负载均衡的个性化配置。

    """

    def __init__(self):
        """
        :param BzPayMode: 按月/按小时计费。\n        :type BzPayMode: str\n        :param BzL4Metrics: 四层可选按带宽，连接数衡量。\n        :type BzL4Metrics: str\n        :param BzL7Metrics: 七层可选按qps衡量。\n        :type BzL7Metrics: str\n        """
        self.BzPayMode = None
        self.BzL4Metrics = None
        self.BzL7Metrics = None


    def _deserialize(self, params):
        self.BzPayMode = params.get("BzPayMode")
        self.BzL4Metrics = params.get("BzL4Metrics")
        self.BzL7Metrics = params.get("BzL7Metrics")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancersRequest(AbstractModel):
    """CreateLoadBalancers请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 黑石负载均衡实例所属的私有网络ID。\n        :type VpcId: str\n        :param LoadBalancerType: 负载均衡的类型，取值为open或internal。open表示公网(有日租)，internal表示内网。\n        :type LoadBalancerType: str\n        :param SubnetId: 在私有网络内购买内网负载均衡实例的时候需要指定子网ID，内网负载均衡实例的VIP将从这个子网中产生。其他情况不用填写该字段。\n        :type SubnetId: str\n        :param ProjectId: 负载均衡所属项目ID。不填则属于默认项目。\n        :type ProjectId: int\n        :param GoodsNum: 购买黑石负载均衡实例的数量。默认值为1, 最大值为20。\n        :type GoodsNum: int\n        :param PayMode: 黑石负载均衡的计费模式，取值为flow和bandwidth，其中flow模式表示流量模式，bandwidth表示带宽模式。默认值为flow。\n        :type PayMode: str\n        :param TgwSetType: 负载均衡对应的TGW集群类别，取值为tunnel、fullnat或dnat。tunnel表示隧道集群，fullnat表示FULLNAT集群（普通外网负载均衡），dnat表示DNAT集群（增强型外网负载均衡）。默认值为fullnat。如需获取client IP，可以选择 tunnel 模式，fullnat 模式（tcp 通过toa 获取），dnat 模式。\n        :type TgwSetType: str\n        :param Exclusive: 负载均衡的独占类别，取值为0表示非独占，1表示四层独占，2表示七层独占，3表示四层和七层独占，4表示共享容灾。\n        :type Exclusive: int\n        :param SpecifiedVips: 指定的VIP，如果指定，则数量必须与goodsNum一致。如果不指定，则由后台分配随机VIP。\n        :type SpecifiedVips: list of str\n        :param BzConf: （未全地域开放）保障型负载均衡设定参数，如果类别选择保障型则需传入此参数。\n        :type BzConf: :class:`tencentcloud.bmlb.v20180625.models.CreateLoadBalancerBzConf`\n        :param IpProtocolType: IP协议类型。可取的值为“ipv4”或“ipv6”。\n        :type IpProtocolType: str\n        """
        self.VpcId = None
        self.LoadBalancerType = None
        self.SubnetId = None
        self.ProjectId = None
        self.GoodsNum = None
        self.PayMode = None
        self.TgwSetType = None
        self.Exclusive = None
        self.SpecifiedVips = None
        self.BzConf = None
        self.IpProtocolType = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.GoodsNum = params.get("GoodsNum")
        self.PayMode = params.get("PayMode")
        self.TgwSetType = params.get("TgwSetType")
        self.Exclusive = params.get("Exclusive")
        self.SpecifiedVips = params.get("SpecifiedVips")
        if params.get("BzConf") is not None:
            self.BzConf = CreateLoadBalancerBzConf()
            self.BzConf._deserialize(params.get("BzConf"))
        self.IpProtocolType = params.get("IpProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancersResponse(AbstractModel):
    """CreateLoadBalancers返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 创建的黑石负载均衡实例ID。\n        :type LoadBalancerIds: list of str\n        :param TaskId: 创建负载均衡的异步任务ID。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LoadBalancerIds = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateTrafficMirrorRequest(AbstractModel):
    """CreateTrafficMirror请求参数结构体

    """

    def __init__(self):
        """
        :param Alias: 流量镜像实例别名。\n        :type Alias: str\n        :param VpcId: 流量镜像实例所属的私有网络ID，形如：vpc-xxx。\n        :type VpcId: str\n        """
        self.Alias = None
        self.VpcId = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrafficMirrorResponse(AbstractModel):
    """CreateTrafficMirror返回参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID\n        :type TrafficMirrorId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TrafficMirrorId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.RequestId = params.get("RequestId")


class DeleteL7DomainsRequest(AbstractModel):
    """DeleteL7Domains请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param DomainIds: 转发域名实例ID列表，可通过接口DescribeL7Rules查询。\n        :type DomainIds: list of str\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainIds = params.get("DomainIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL7DomainsResponse(AbstractModel):
    """DeleteL7Domains返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteL7RulesRequest(AbstractModel):
    """DeleteL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。\n        :type DomainId: str\n        :param LocationIds: 转发路径实例ID列表，可通过接口DescribeL7Rules查询。\n        :type LocationIds: list of str\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationIds = params.get("LocationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL7RulesResponse(AbstractModel):
    """DeleteL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteListenersRequest(AbstractModel):
    """DeleteListeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerIds: 待删除的负载均衡四层和七层监听器ID列表，可通过接口DescribeL4Listeners和DescribeL7Listeners查询。目前同时只能删除一种类型的监听器，并且删除七层监听器的数量上限为一个。\n        :type ListenerIds: list of str\n        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenersResponse(AbstractModel):
    """DeleteListeners返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        """
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteTrafficMirrorRequest(AbstractModel):
    """DeleteTrafficMirror请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorIds: 流量镜像实例ID数组，可以批量删除，每次删除上限为20\n        :type TrafficMirrorIds: list of str\n        """
        self.TrafficMirrorIds = None


    def _deserialize(self, params):
        self.TrafficMirrorIds = params.get("TrafficMirrorIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTrafficMirrorResponse(AbstractModel):
    """DeleteTrafficMirror返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeCertDetailRequest(AbstractModel):
    """DescribeCertDetail请求参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书ID。\n        :type CertId: str\n        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertDetailResponse(AbstractModel):
    """DescribeCertDetail返回参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书ID。\n        :type CertId: str\n        :param CertName: 证书名称。\n        :type CertName: str\n        :param CertType: 证书类型（SVR=服务器证书，CA=客户端证书）。\n        :type CertType: str\n        :param CertContent: 证书内容。\n        :type CertContent: str\n        :param CertDomain: 证书主域名。\n        :type CertDomain: str\n        :param CertSubjectDomain: 证书子域名列表。\n        :type CertSubjectDomain: list of str\n        :param CertUploadTime: 证书上传时间。\n        :type CertUploadTime: str\n        :param CertBeginTime: 证书生效时间。\n        :type CertBeginTime: str\n        :param CertEndTime: 证书失效时间。\n        :type CertEndTime: str\n        :param CertLoadBalancerSet: 该证书关联的黑石负载均衡对象列表。\n        :type CertLoadBalancerSet: list of CertDetailLoadBalancer\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertId = None
        self.CertName = None
        self.CertType = None
        self.CertContent = None
        self.CertDomain = None
        self.CertSubjectDomain = None
        self.CertUploadTime = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.CertLoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.CertType = params.get("CertType")
        self.CertContent = params.get("CertContent")
        self.CertDomain = params.get("CertDomain")
        self.CertSubjectDomain = params.get("CertSubjectDomain")
        self.CertUploadTime = params.get("CertUploadTime")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        if params.get("CertLoadBalancerSet") is not None:
            self.CertLoadBalancerSet = []
            for item in params.get("CertLoadBalancerSet"):
                obj = CertDetailLoadBalancer()
                obj._deserialize(item)
                self.CertLoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicesBindInfoRequest(AbstractModel):
    """DescribeDevicesBindInfo请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 黑石私有网络唯一ID。\n        :type VpcId: str\n        :param InstanceIds: 主机ID或虚机IP列表，可用于获取绑定了该主机的负载均衡列表。\n        :type InstanceIds: list of str\n        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesBindInfoResponse(AbstractModel):
    """DescribeDevicesBindInfo返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerSet: 返回的负载均衡绑定信息。\n        :type LoadBalancerSet: list of DevicesBindInfoLoadBalancer\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = DevicesBindInfoLoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4Backend(AbstractModel):
    """待查询四层监听器绑定的主机信息。

    """

    def __init__(self):
        """
        :param Port: 待绑定的主机端口，可选值1~65535。\n        :type Port: int\n        :param InstanceId: 黑石物理机的主机ID。\n        :type InstanceId: str\n        """
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4BackendsRequest(AbstractModel):
    """DescribeL4Backends请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。\n        :type ListenerId: str\n        :param BackendSet: 待查询的主机信息。\n        :type BackendSet: list of DescribeL4Backend\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.BackendSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = DescribeL4Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4BackendsResponse(AbstractModel):
    """DescribeL4Backends返回参数结构体

    """

    def __init__(self):
        """
        :param BackendSet: 返回的绑定关系列表。\n        :type BackendSet: list of L4Backend\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BackendSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = L4Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4ListenerInfoRequest(AbstractModel):
    """DescribeL4ListenerInfo请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param SearchKey: 查找的键值，可用于模糊查找该名称的监听器。\n        :type SearchKey: str\n        :param InstanceIds: 主机ID或虚机IP列表，可用于获取绑定了该主机的监听器。\n        :type InstanceIds: list of str\n        """
        self.LoadBalancerId = None
        self.SearchKey = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SearchKey = params.get("SearchKey")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4ListenerInfoResponse(AbstractModel):
    """DescribeL4ListenerInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerSet: 返回的四层监听器列表。\n        :type ListenerSet: list of L4ListenerInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L4ListenerInfo()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4ListenersRequest(AbstractModel):
    """DescribeL4Listeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerIds: 四层监听器实例ID数组，可通过接口DescribeL4Listeners查询。\n        :type ListenerIds: list of str\n        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4ListenersResponse(AbstractModel):
    """DescribeL4Listeners返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerSet: 监听器信息数组。\n        :type ListenerSet: list of L4Listener\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L4Listener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7BackendsRequest(AbstractModel):
    """DescribeL7Backends请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。\n        :type DomainId: str\n        :param LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。\n        :type LocationId: str\n        :param QueryType: 查询条件，传'all'则查询所有与规则绑定的主机信息。如果为all时，DomainId和LocationId参数没有意义不必传入，否则DomainId和LocationId参数必须传入。\n        :type QueryType: str\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.QueryType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        self.QueryType = params.get("QueryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7BackendsResponse(AbstractModel):
    """DescribeL7Backends返回参数结构体

    """

    def __init__(self):
        """
        :param BackendSet: 返回的绑定关系列表。\n        :type BackendSet: list of L7Backend\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BackendSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = L7Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7ListenerInfoRequest(AbstractModel):
    """DescribeL7ListenerInfo请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param SearchKey: 查找的键值，可用于模糊查找有该转发域名的监听器。\n        :type SearchKey: str\n        :param InstanceIds: 主机ID或虚机IP列表，可用于获取绑定了该主机的监听器。\n        :type InstanceIds: list of str\n        :param IfGetBackendInfo: 是否获取转发规则下的主机信息。默认为0，不获取。\n        :type IfGetBackendInfo: int\n        """
        self.LoadBalancerId = None
        self.SearchKey = None
        self.InstanceIds = None
        self.IfGetBackendInfo = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SearchKey = params.get("SearchKey")
        self.InstanceIds = params.get("InstanceIds")
        self.IfGetBackendInfo = params.get("IfGetBackendInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7ListenerInfoResponse(AbstractModel):
    """DescribeL7ListenerInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerSet: 返回的七层监听器列表。\n        :type ListenerSet: list of L7ListenerInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L7ListenerInfo()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7ListenersExRequest(AbstractModel):
    """DescribeL7ListenersEx请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 返回的监听器中标识是否绑定在此流量镜像中。\n        :type TrafficMirrorId: str\n        :param VpcId: 待获取监听器所在的VPC的ID。\n        :type VpcId: str\n        :param Offset: 此VPC中获取负载均衡的偏移。\n        :type Offset: int\n        :param Limit: 此VPC中获取负载均衡的数量。\n        :type Limit: int\n        :param Filters: 过滤条件。
LoadBalancerId - String - （过滤条件）负载均衡ID。
LoadBalancerName - String - （过滤条件）负载均衡名称。
Vip - String - （过滤条件）VIP。
ListenerId - String - （过滤条件）监听器ID。
ListenerName -  String - （过滤条件）监听器名称。
Protocol -  String - （过滤条件）七层协议。
LoadBalancerPort -  String - （过滤条件）监听器端口。\n        :type Filters: list of Filter\n        """
        self.TrafficMirrorId = None
        self.VpcId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.VpcId = params.get("VpcId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7ListenersExResponse(AbstractModel):
    """DescribeL7ListenersEx返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 此指定VPC中负载均衡的总数。\n        :type TotalCount: int\n        :param ListenerSet: 符合条件的监听器。\n        :type ListenerSet: list of L7ExListener\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L7ExListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7ListenersRequest(AbstractModel):
    """DescribeL7Listeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerIds: 七层监听器实例ID列表，可通过接口DescribeL7Listeners查询。\n        :type ListenerIds: list of str\n        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7ListenersResponse(AbstractModel):
    """DescribeL7Listeners返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerSet: 返回的七层监听器列表。\n        :type ListenerSet: list of L7Listener\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L7Listener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7RulesRequest(AbstractModel):
    """DescribeL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param DomainIds: 转发域名ID列表，可通过接口DescribeL7Rules查询。\n        :type DomainIds: list of str\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainIds = params.get("DomainIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7RulesResponse(AbstractModel):
    """DescribeL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param RuleSet: 返回的转发规则列表。\n        :type RuleSet: list of L7Rule\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = L7Rule()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerPortInfoRequest(AbstractModel):
    """DescribeLoadBalancerPortInfo请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        """
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerPortInfoResponse(AbstractModel):
    """DescribeLoadBalancerPortInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerSet: 返回的监听器列表（四层和七层）。\n        :type ListenerSet: list of LoadBalancerPortInfoListener\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = LoadBalancerPortInfoListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerTaskResultRequest(AbstractModel):
    """DescribeLoadBalancerTaskResult请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。由具体的异步操作接口提供。\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerTaskResultResponse(AbstractModel):
    """DescribeLoadBalancerTaskResult返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务当前状态。0：成功，1：失败，2：进行中。\n        :type Status: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 负载均衡器ID数组\n        :type LoadBalancerIds: list of str\n        :param LoadBalancerType: 负载均衡的类型 : open表示公网LB类型，internal表示内网LB类型\n        :type LoadBalancerType: str\n        :param LoadBalancerName: 负载均衡器名称\n        :type LoadBalancerName: str\n        :param Domain: 负载均衡域名。规则：1-60个小写英文字母、数字、点号“.”或连接线“-”。内网类型的负载均衡不能配置该字段\n        :type Domain: str\n        :param LoadBalancerVips: 负载均衡获得的公网IP地址,支持多个\n        :type LoadBalancerVips: list of str\n        :param Offset: 数据偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数据长度，默认为20\n        :type Limit: int\n        :param SearchKey: 模糊查找名称、域名、VIP\n        :type SearchKey: str\n        :param OrderBy: 排序字段，支持：loadBalancerName,createTime,domain,loadBalancerType\n        :type OrderBy: str\n        :param OrderType: 1倒序，0顺序，默认顺序\n        :type OrderType: int\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param Exclusive: 是否筛选独占集群，0表示非独占集群，1表示四层独占集群，2表示七层独占集群，3表示四层和七层独占集群，4表示共享容灾\n        :type Exclusive: int\n        :param TgwSetType: 该负载均衡对应的tgw集群（fullnat,tunnel,dnat）\n        :type TgwSetType: str\n        :param VpcId: 该负载均衡对应的所在的私有网络ID\n        :type VpcId: str\n        :param QueryType: 'CONFLIST' 查询带confId的LB列表，'CONFID' 查询某个confId绑定的LB列表\n        :type QueryType: str\n        :param ConfId: 个性化配置ID\n        :type ConfId: str\n        """
        self.LoadBalancerIds = None
        self.LoadBalancerType = None
        self.LoadBalancerName = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.OrderBy = None
        self.OrderType = None
        self.ProjectId = None
        self.Exclusive = None
        self.TgwSetType = None
        self.VpcId = None
        self.QueryType = None
        self.ConfId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.ProjectId = params.get("ProjectId")
        self.Exclusive = params.get("Exclusive")
        self.TgwSetType = params.get("TgwSetType")
        self.VpcId = params.get("VpcId")
        self.QueryType = params.get("QueryType")
        self.ConfId = params.get("ConfId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerSet: 返回负载均衡信息列表。\n        :type LoadBalancerSet: list of LoadBalancer\n        :param TotalCount: 符合条件的负载均衡总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LoadBalancerSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTrafficMirrorListenersRequest(AbstractModel):
    """DescribeTrafficMirrorListeners请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID。\n        :type TrafficMirrorId: str\n        :param Offset: 分页的偏移量，也即从第几条记录开始查询\n        :type Offset: int\n        :param Limit: 单次查询返回的条目数，默认值：500。\n        :type Limit: int\n        :param SearchLoadBalancerIds: 待搜索的负载均衡Id。\n        :type SearchLoadBalancerIds: list of str\n        :param SearchLoadBalancerNames: 待搜索的负载均衡名称。\n        :type SearchLoadBalancerNames: list of str\n        :param SearchVips: 待搜索的Vip。\n        :type SearchVips: list of str\n        :param SearchListenerIds: 待搜索的监听器ID。\n        :type SearchListenerIds: list of str\n        :param SearchListenerNames: 待搜索的监听器名称。\n        :type SearchListenerNames: list of str\n        :param SearchProtocols: 待搜索的协议名称。\n        :type SearchProtocols: list of str\n        :param SearchLoadBalancerPorts: 待搜索的端口。\n        :type SearchLoadBalancerPorts: list of int non-negative\n        """
        self.TrafficMirrorId = None
        self.Offset = None
        self.Limit = None
        self.SearchLoadBalancerIds = None
        self.SearchLoadBalancerNames = None
        self.SearchVips = None
        self.SearchListenerIds = None
        self.SearchListenerNames = None
        self.SearchProtocols = None
        self.SearchLoadBalancerPorts = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchLoadBalancerIds = params.get("SearchLoadBalancerIds")
        self.SearchLoadBalancerNames = params.get("SearchLoadBalancerNames")
        self.SearchVips = params.get("SearchVips")
        self.SearchListenerIds = params.get("SearchListenerIds")
        self.SearchListenerNames = params.get("SearchListenerNames")
        self.SearchProtocols = params.get("SearchProtocols")
        self.SearchLoadBalancerPorts = params.get("SearchLoadBalancerPorts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorListenersResponse(AbstractModel):
    """DescribeTrafficMirrorListeners返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerSet: 监听器列表。\n        :type ListenerSet: list of TrafficMirrorListener\n        :param TotalCount: 监听器总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListenerSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = TrafficMirrorListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTrafficMirrorReceiver(AbstractModel):
    """流量镜像进行健康检查的接收机信息。

    """

    def __init__(self):
        """
        :param InstanceId: 物理机实例ID。\n        :type InstanceId: str\n        :param Port: 物理机绑定的端口。\n        :type Port: int\n        """
        self.InstanceId = None
        self.Port = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorReceiverHealthStatusRequest(AbstractModel):
    """DescribeTrafficMirrorReceiverHealthStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 查询所在的流量镜像ID。\n        :type TrafficMirrorId: str\n        :param ReceiverSet: 流量镜像接收机实例ID和端口数组。\n        :type ReceiverSet: list of DescribeTrafficMirrorReceiver\n        """
        self.TrafficMirrorId = None
        self.ReceiverSet = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self.ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = DescribeTrafficMirrorReceiver()
                obj._deserialize(item)
                self.ReceiverSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorReceiverHealthStatusResponse(AbstractModel):
    """DescribeTrafficMirrorReceiverHealthStatus返回参数结构体

    """

    def __init__(self):
        """
        :param ReceiversStatusSet: 内网IP和端口对应的状态。\n        :type ReceiversStatusSet: list of TrafficMirrorReciversStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReceiversStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReceiversStatusSet") is not None:
            self.ReceiversStatusSet = []
            for item in params.get("ReceiversStatusSet"):
                obj = TrafficMirrorReciversStatus()
                obj._deserialize(item)
                self.ReceiversStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrafficMirrorReceiversRequest(AbstractModel):
    """DescribeTrafficMirrorReceivers请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID。\n        :type TrafficMirrorId: str\n        :param InstanceIds: 接收机黑石物理机实例ID数组。\n        :type InstanceIds: list of str\n        :param Ports: 接收机接收端口数组。\n        :type Ports: list of int\n        :param Weights: 接收机实例权重数组。\n        :type Weights: list of int\n        :param Offset: 分页的偏移量，也即从第几条记录开始查询\n        :type Offset: int\n        :param Limit: 单次查询返回的条目数，默认值：500。\n        :type Limit: int\n        :param VagueStr: 搜索instance或者alias\n        :type VagueStr: str\n        :param VagueIp: 搜索IP\n        :type VagueIp: str\n        """
        self.TrafficMirrorId = None
        self.InstanceIds = None
        self.Ports = None
        self.Weights = None
        self.Offset = None
        self.Limit = None
        self.VagueStr = None
        self.VagueIp = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.InstanceIds = params.get("InstanceIds")
        self.Ports = params.get("Ports")
        self.Weights = params.get("Weights")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.VagueStr = params.get("VagueStr")
        self.VagueIp = params.get("VagueIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorReceiversResponse(AbstractModel):
    """DescribeTrafficMirrorReceivers返回参数结构体

    """

    def __init__(self):
        """
        :param ReceiverSet: 接收机列表，具体结构描述如data结构所示。\n        :type ReceiverSet: list of TrafficMirrorReceiver\n        :param TotalCount: 接收机总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReceiverSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReceiverSet") is not None:
            self.ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = TrafficMirrorReceiver()
                obj._deserialize(item)
                self.ReceiverSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTrafficMirrorsRequest(AbstractModel):
    """DescribeTrafficMirrors请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorIds: 流量镜像实例ID的数组，支持批量查询\n        :type TrafficMirrorIds: list of str\n        :param Aliases: 流量镜像实例别名数组。\n        :type Aliases: list of str\n        :param VpcIds: 流量镜像实例所属的私有网络ID数组，形如：vpc-xxx。\n        :type VpcIds: list of str\n        :param Offset: 分页的偏移量，也即从第几条记录开始查询\n        :type Offset: int\n        :param Limit: 单次查询返回的条目数，默认值：500。\n        :type Limit: int\n        :param OrderField: 排序字段。trafficMirrorId或者createTime。\n        :type OrderField: str\n        :param Order: 排序方式，取值：0:增序(默认)，1:降序\n        :type Order: int\n        :param SearchKey: 模糊匹配trafficMirrorId或者alias字段。\n        :type SearchKey: str\n        """
        self.TrafficMirrorIds = None
        self.Aliases = None
        self.VpcIds = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.TrafficMirrorIds = params.get("TrafficMirrorIds")
        self.Aliases = params.get("Aliases")
        self.VpcIds = params.get("VpcIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficMirrorsResponse(AbstractModel):
    """DescribeTrafficMirrors返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 流量镜像总数。\n        :type TotalCount: int\n        :param TrafficMirrorSet: 对象数组。数组元素为流量镜像信息，具体结构描述如list结构所示。\n        :type TrafficMirrorSet: list of TrafficMirror\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TrafficMirrorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TrafficMirrorSet") is not None:
            self.TrafficMirrorSet = []
            for item in params.get("TrafficMirrorSet"):
                obj = TrafficMirror()
                obj._deserialize(item)
                self.TrafficMirrorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DevicesBindInfoBackend(AbstractModel):
    """获取设备绑定信息时返回的所绑定的主机信息。

    """

    def __init__(self):
        """
        :param InstanceId: 黑石物理机的主机ID、托管主机ID或虚拟机IP。\n        :type InstanceId: str\n        :param Port: 主机端口。\n        :type Port: int\n        """
        self.InstanceId = None
        self.Port = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoL4Listener(AbstractModel):
    """获取设备绑定信息时返回的四层监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 七层监听器实例ID。\n        :type ListenerId: str\n        :param Protocol: 七层监听器协议类型，可选值：http,https。\n        :type Protocol: str\n        :param LoadBalancerPort: 七层监听器的监听端口。\n        :type LoadBalancerPort: int\n        :param BackendSet: 该转发路径所绑定的主机列表。\n        :type BackendSet: list of DevicesBindInfoBackend\n        """
        self.ListenerId = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.BackendSet = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = DevicesBindInfoBackend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoL7Listener(AbstractModel):
    """获取设备绑定信息时返回的七层监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 七层监听器实例ID。\n        :type ListenerId: str\n        :param Protocol: 七层监听器协议类型，可选值：http,https。\n        :type Protocol: str\n        :param LoadBalancerPort: 七层监听器的监听端口。\n        :type LoadBalancerPort: int\n        :param RuleSet: 返回的转发规则列表。\n        :type RuleSet: list of DevicesBindInfoRule\n        """
        self.ListenerId = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.RuleSet = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = DevicesBindInfoRule()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoLoadBalancer(AbstractModel):
    """获取设备绑定信息时返回的设备被绑定所在的负载均衡信息。

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。\n        :type LoadBalancerId: str\n        :param AppId: 开发商AppId。\n        :type AppId: int\n        :param ProjectId: 负载均衡所属的项目ID。\n        :type ProjectId: int\n        :param VpcId: 黑石私有网络唯一ID。\n        :type VpcId: str\n        :param Vip: 负载均衡的IP地址。\n        :type Vip: str\n        :param TgwSetType: 负载均衡对应的TGW集群类别，取值为tunnel或fullnat。tunnel表示隧道集群，fullnat表示FULLNAT集群。\n        :type TgwSetType: str\n        :param Exclusive: 是否独占TGW集群。\n        :type Exclusive: int\n        :param L4ListenerSet: 具有该绑定关系的四层监听器列表。\n        :type L4ListenerSet: list of DevicesBindInfoL4Listener\n        :param L7ListenerSet: 具有该绑定关系的七层监听器列表。\n        :type L7ListenerSet: list of DevicesBindInfoL7Listener\n        """
        self.LoadBalancerId = None
        self.AppId = None
        self.ProjectId = None
        self.VpcId = None
        self.Vip = None
        self.TgwSetType = None
        self.Exclusive = None
        self.L4ListenerSet = None
        self.L7ListenerSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.Vip = params.get("Vip")
        self.TgwSetType = params.get("TgwSetType")
        self.Exclusive = params.get("Exclusive")
        if params.get("L4ListenerSet") is not None:
            self.L4ListenerSet = []
            for item in params.get("L4ListenerSet"):
                obj = DevicesBindInfoL4Listener()
                obj._deserialize(item)
                self.L4ListenerSet.append(obj)
        if params.get("L7ListenerSet") is not None:
            self.L7ListenerSet = []
            for item in params.get("L7ListenerSet"):
                obj = DevicesBindInfoL7Listener()
                obj._deserialize(item)
                self.L7ListenerSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoLocation(AbstractModel):
    """获取设备绑定信息时返回的设备所绑定的转发路径信息。

    """

    def __init__(self):
        """
        :param Url: 转发路径。\n        :type Url: str\n        :param LocationId: 转发路径实例ID。\n        :type LocationId: str\n        :param BackendSet: 该转发路径所绑定的主机列表。\n        :type BackendSet: list of DevicesBindInfoBackend\n        """
        self.Url = None
        self.LocationId = None
        self.BackendSet = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = DevicesBindInfoBackend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesBindInfoRule(AbstractModel):
    """获取设备绑定信息时返回的设备所绑定的转发规则信息。

    """

    def __init__(self):
        """
        :param Domain: 转发域名。\n        :type Domain: str\n        :param DomainId: 转发域名ID。\n        :type DomainId: str\n        :param LocationSet: 转发路径列表。\n        :type LocationSet: list of DevicesBindInfoLocation\n        """
        self.Domain = None
        self.DomainId = None
        self.LocationSet = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        if params.get("LocationSet") is not None:
            self.LocationSet = []
            for item in params.get("LocationSet"):
                obj = DevicesBindInfoLocation()
                obj._deserialize(item)
                self.LocationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        """
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。\n        :type Name: str\n        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。\n        :type Values: list of str\n        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4Backend(AbstractModel):
    """查询四层监听器返回的与监听器绑定关系的主机信息。

    """

    def __init__(self):
        """
        :param BindType: 绑定类别（0代表黑石物理机，1代表虚拟机IP）。\n        :type BindType: int\n        :param Port: 主机端口。\n        :type Port: int\n        :param Weight: 权重。\n        :type Weight: int\n        :param Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。\n        :type Status: str\n        :param InstanceId: 黑石物理机的主机ID。\n        :type InstanceId: str\n        :param Alias: 黑石物理机的别名。\n        :type Alias: str\n        :param LanIp: 主机IP。\n        :type LanIp: str\n        :param Operates: 黑石物理机当前可以执行的操作。\n        :type Operates: list of str\n        :param ProbePort: 主机探测端口。\n        :type ProbePort: int\n        """
        self.BindType = None
        self.Port = None
        self.Weight = None
        self.Status = None
        self.InstanceId = None
        self.Alias = None
        self.LanIp = None
        self.Operates = None
        self.ProbePort = None


    def _deserialize(self, params):
        self.BindType = params.get("BindType")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.LanIp = params.get("LanIp")
        self.Operates = params.get("Operates")
        self.ProbePort = params.get("ProbePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4Listener(AbstractModel):
    """查询四层监听器时返回的四层监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 监听器ID。\n        :type ListenerId: str\n        :param ListenerName: 用户自定义的监听器名称。\n        :type ListenerName: str\n        :param Protocol: 负载均衡实例监听器协议类型，可选值tcp，udp。\n        :type Protocol: str\n        :param LoadBalancerPort: 负载均衡监听器的监听接口，可选值1~65535。\n        :type LoadBalancerPort: int\n        :param Bandwidth: 用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。\n        :type Bandwidth: int\n        :param ListenerType: 监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。\n        :type ListenerType: str\n        :param SessionExpire: 会话保持时间。单位：秒\n        :type SessionExpire: int\n        :param HealthSwitch: 是否开启了检查：1（开启）、0（关闭）。\n        :type HealthSwitch: int\n        :param TimeOut: 响应超时时间，单位：秒。\n        :type TimeOut: int\n        :param IntervalTime: 检查间隔，单位：秒。\n        :type IntervalTime: int\n        :param HealthNum: 负载均衡监听器健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。\n        :type HealthNum: int\n        :param UnhealthNum: 负载均衡监听器不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。\n        :type UnhealthNum: int\n        :param CustomHealthSwitch: 是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）\n        :type CustomHealthSwitch: int\n        :param InputType: 自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。\n        :type InputType: str\n        :param LineSeparatorType: 探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。\n        :type LineSeparatorType: int\n        :param HealthRequest: 自定义探测请求内容。\n        :type HealthRequest: str\n        :param HealthResponse: 自定义探测返回内容。\n        :type HealthResponse: str\n        :param ToaFlag: 是否开启toa：1（开启）、0（关闭）。\n        :type ToaFlag: int\n        :param Status: 监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。\n        :type Status: int\n        :param AddTimestamp: 创建时间戳。\n        :type AddTimestamp: str\n        :param BalanceMode: 转发后端服务器调度类型。\n        :type BalanceMode: str\n        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.ListenerType = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.CustomHealthSwitch = None
        self.InputType = None
        self.LineSeparatorType = None
        self.HealthRequest = None
        self.HealthResponse = None
        self.ToaFlag = None
        self.Status = None
        self.AddTimestamp = None
        self.BalanceMode = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.CustomHealthSwitch = params.get("CustomHealthSwitch")
        self.InputType = params.get("InputType")
        self.LineSeparatorType = params.get("LineSeparatorType")
        self.HealthRequest = params.get("HealthRequest")
        self.HealthResponse = params.get("HealthResponse")
        self.ToaFlag = params.get("ToaFlag")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        self.BalanceMode = params.get("BalanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4ListenerInfo(AbstractModel):
    """查询绑定了某主机的四层监听器时返回的四层监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 监听器ID。\n        :type ListenerId: str\n        :param ListenerName: 用户自定义的监听器名称。\n        :type ListenerName: str\n        :param Protocol: 负载均衡实例监听器协议类型，可选值tcp，udp。\n        :type Protocol: str\n        :param LoadBalancerPort: 负载均衡监听器的监听接口，可选值1~65535。\n        :type LoadBalancerPort: int\n        :param Bandwidth: 用于计费模式为固定带宽计费，指定监听器最大带宽值，可选值：0-1000，单位：Mbps。\n        :type Bandwidth: int\n        :param ListenerType: 监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。\n        :type ListenerType: str\n        :param SessionExpire: 会话保持时间。单位：秒\n        :type SessionExpire: int\n        :param HealthSwitch: 是否开启了检查：1（开启）、0（关闭）。\n        :type HealthSwitch: int\n        :param TimeOut: 响应超时时间，单位：秒。\n        :type TimeOut: int\n        :param IntervalTime: 检查间隔，单位：秒。\n        :type IntervalTime: int\n        :param HealthNum: 负载均衡监听器健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。\n        :type HealthNum: int\n        :param UnhealthNum: 负载均衡监听器不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。\n        :type UnhealthNum: int\n        :param Status: 监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。\n        :type Status: int\n        :param AddTimestamp: 创建时间戳。\n        :type AddTimestamp: str\n        :param CustomHealthSwitch: 是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）\n        :type CustomHealthSwitch: int\n        :param InputType: 自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。\n        :type InputType: str\n        :param LineSeparatorType: 探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。\n        :type LineSeparatorType: int\n        :param HealthRequest: 自定义探测请求内容。\n        :type HealthRequest: str\n        :param HealthResponse: 自定义探测返回内容。\n        :type HealthResponse: str\n        :param ToaFlag: 是否开启toa：1（开启）、0（关闭）。\n        :type ToaFlag: int\n        :param BalanceMode: 转发后端服务器调度类型。\n        :type BalanceMode: str\n        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.ListenerType = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.Status = None
        self.AddTimestamp = None
        self.CustomHealthSwitch = None
        self.InputType = None
        self.LineSeparatorType = None
        self.HealthRequest = None
        self.HealthResponse = None
        self.ToaFlag = None
        self.BalanceMode = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        self.CustomHealthSwitch = params.get("CustomHealthSwitch")
        self.InputType = params.get("InputType")
        self.LineSeparatorType = params.get("LineSeparatorType")
        self.HealthRequest = params.get("HealthRequest")
        self.HealthResponse = params.get("HealthResponse")
        self.ToaFlag = params.get("ToaFlag")
        self.BalanceMode = params.get("BalanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7Backend(AbstractModel):
    """获取七层转发路径绑定的主机列表时返回的主机信息。

    """

    def __init__(self):
        """
        :param BindType: 绑定类别（0代表黑石物理机，1代表虚拟机IP）。\n        :type BindType: int\n        :param Port: 主机端口。\n        :type Port: int\n        :param Weight: 权重。\n        :type Weight: int\n        :param Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。\n        :type Status: str\n        :param InstanceId: 黑石物理机的主机ID。\n        :type InstanceId: str\n        :param Alias: 黑石物理机的别名。\n        :type Alias: str\n        :param LanIp: 主机IP。\n        :type LanIp: str\n        :param MgtIp: 黑石物理机的管理IP。\n        :type MgtIp: str\n        :param Operates: 黑石物理机当前可以执行的操作。\n        :type Operates: list of str\n        """
        self.BindType = None
        self.Port = None
        self.Weight = None
        self.Status = None
        self.InstanceId = None
        self.Alias = None
        self.LanIp = None
        self.MgtIp = None
        self.Operates = None


    def _deserialize(self, params):
        self.BindType = params.get("BindType")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.LanIp = params.get("LanIp")
        self.MgtIp = params.get("MgtIp")
        self.Operates = params.get("Operates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ExListener(AbstractModel):
    """监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 绑定的监听器唯一ID。\n        :type ListenerId: str\n        :param ListenerName: 监听器名称。\n        :type ListenerName: str\n        :param Protocol: 七层监听器协议类型，可选值：http,https。\n        :type Protocol: str\n        :param LoadBalancerPort: 监听器的监听端口。\n        :type LoadBalancerPort: int\n        :param Bandwidth: 当前带宽。\n        :type Bandwidth: int\n        :param MaxBandwidth: 带宽上限。\n        :type MaxBandwidth: int\n        :param ListenerType: 监听器类型。\n        :type ListenerType: str\n        :param SslMode: 认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。\n        :type SslMode: int\n        :param CertId: 服务端证书ID。\n        :type CertId: str\n        :param CertCaId: 客户端证书ID。\n        :type CertCaId: str\n        :param AddTimestamp: 添加时间。\n        :type AddTimestamp: str\n        :param LoadBalancerId: 负载均衡名ID。\n        :type LoadBalancerId: str\n        :param VpcName: 私有网络名称。\n        :type VpcName: str\n        :param VpcCidrBlock: 私有网络Cidr。\n        :type VpcCidrBlock: str\n        :param LoadBalancerVips: 负载均衡的VIP。\n        :type LoadBalancerVips: list of str\n        :param LoadBalancerName: 负载均衡名称。\n        :type LoadBalancerName: str\n        :param LoadBalancerVipv6s: 负载均衡IPV6的VIP。\n        :type LoadBalancerVipv6s: list of str\n        :param IpProtocolType: 支持的IP协议类型。ipv4或者是ipv6。\n        :type IpProtocolType: str\n        :param BindTrafficMirror: 是否绑定在入参指定的流量镜像中。\n        :type BindTrafficMirror: bool\n        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.MaxBandwidth = None
        self.ListenerType = None
        self.SslMode = None
        self.CertId = None
        self.CertCaId = None
        self.AddTimestamp = None
        self.LoadBalancerId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.LoadBalancerVips = None
        self.LoadBalancerName = None
        self.LoadBalancerVipv6s = None
        self.IpProtocolType = None
        self.BindTrafficMirror = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.AddTimestamp = params.get("AddTimestamp")
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self.IpProtocolType = params.get("IpProtocolType")
        self.BindTrafficMirror = params.get("BindTrafficMirror")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7Listener(AbstractModel):
    """获取黑石负载均衡七层监听器时返回的七层监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 七层监听器实例ID。\n        :type ListenerId: str\n        :param ListenerName: 七层监听器名称。\n        :type ListenerName: str\n        :param Protocol: 七层监听器协议类型，可选值：http,https。\n        :type Protocol: str\n        :param LoadBalancerPort: 七层监听器的监听端口。\n        :type LoadBalancerPort: int\n        :param Bandwidth: 计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。\n        :type Bandwidth: int\n        :param ListenerType: 监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。\n        :type ListenerType: str\n        :param SslMode: 七层监听器的认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。\n        :type SslMode: int\n        :param CertId: 七层监听器关联的服务端证书ID。\n        :type CertId: str\n        :param CertCaId: 七层监听器关联的客户端证书ID。\n        :type CertCaId: str\n        :param Status: 监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。\n        :type Status: int\n        :param AddTimestamp: 创建时间戳。\n        :type AddTimestamp: str\n        :param ForwardProtocol: https转发类型。0：https。1：spdy。2：http2。3：spdy+http2。\n        :type ForwardProtocol: int\n        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.ListenerType = None
        self.SslMode = None
        self.CertId = None
        self.CertCaId = None
        self.Status = None
        self.AddTimestamp = None
        self.ForwardProtocol = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        self.ForwardProtocol = params.get("ForwardProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ListenerInfo(AbstractModel):
    """查询绑定了某主机的七层监听器时返回的七层监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 七层监听器实例ID。\n        :type ListenerId: str\n        :param ListenerName: 七层监听器名称。\n        :type ListenerName: str\n        :param Protocol: 七层监听器协议类型，可选值：http,https。\n        :type Protocol: str\n        :param LoadBalancerPort: 七层监听器的监听端口。\n        :type LoadBalancerPort: int\n        :param Bandwidth: 计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。\n        :type Bandwidth: int\n        :param ListenerType: 监听器的类别：L4Listener（四层监听器），L7Listener（七层监听器）。\n        :type ListenerType: str\n        :param SslMode: 七层监听器的认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。\n        :type SslMode: int\n        :param CertId: 七层监听器关联的服务端证书ID。\n        :type CertId: str\n        :param CertCaId: 七层监听器关联的客户端证书ID。\n        :type CertCaId: str\n        :param Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。\n        :type Status: int\n        :param AddTimestamp: 创建时间戳。\n        :type AddTimestamp: str\n        :param RuleSet: 返回的转发规则列表。\n        :type RuleSet: list of L7ListenerInfoRule\n        :param ForwardProtocol: https转发类型。0：https。1：spdy。2：http2。3：spdy+http2。\n        :type ForwardProtocol: int\n        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.ListenerType = None
        self.SslMode = None
        self.CertId = None
        self.CertCaId = None
        self.Status = None
        self.AddTimestamp = None
        self.RuleSet = None
        self.ForwardProtocol = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = L7ListenerInfoRule()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.ForwardProtocol = params.get("ForwardProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ListenerInfoBackend(AbstractModel):
    """查询绑定了某主机七层监听器时返回的与转发路径所绑定的主机信息。

    """

    def __init__(self):
        """
        :param BindType: 绑定类别（0代表黑石物理机，1代表虚拟机IP）。\n        :type BindType: int\n        :param Port: 主机端口。\n        :type Port: int\n        :param Weight: 权重。\n        :type Weight: int\n        :param Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。\n        :type Status: str\n        :param InstanceId: 黑石物理机的主机ID。\n        :type InstanceId: str\n        :param Alias: 黑石物理机的别名。\n        :type Alias: str\n        :param LanIp: 主机IP。\n        :type LanIp: str\n        """
        self.BindType = None
        self.Port = None
        self.Weight = None
        self.Status = None
        self.InstanceId = None
        self.Alias = None
        self.LanIp = None


    def _deserialize(self, params):
        self.BindType = params.get("BindType")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.LanIp = params.get("LanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ListenerInfoLocation(AbstractModel):
    """查询绑定了某主机的七层监听器时返回的转发路径。

    """

    def __init__(self):
        """
        :param Url: 转发路径。\n        :type Url: str\n        :param LocationId: 转发路径实例ID。\n        :type LocationId: str\n        :param SessionExpire: 会话保持时间。\n        :type SessionExpire: int\n        :param HealthSwitch: 是否开启健康检查。\n        :type HealthSwitch: int\n        :param HttpCheckPath: 健康检查检查路径。\n        :type HttpCheckPath: str\n        :param HttpCheckDomain: 健康检查检查域名。\n        :type HttpCheckDomain: str\n        :param IntervalTime: 健康检查检查间隔时间。\n        :type IntervalTime: int\n        :param HealthNum: 健康检查健康阈值。\n        :type HealthNum: int\n        :param UnhealthNum: 健康检查不健康阈值。\n        :type UnhealthNum: int\n        :param HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。\n        :type HttpCodes: list of int non-negative\n        :param BalanceMode: 均衡方式。\n        :type BalanceMode: str\n        :param Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。\n        :type Status: int\n        :param AddTimestamp: 创建时间戳。\n        :type AddTimestamp: str\n        :param BackendSet: 该转发路径所绑定的主机列表。\n        :type BackendSet: list of L7ListenerInfoBackend\n        """
        self.Url = None
        self.LocationId = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpCodes = None
        self.BalanceMode = None
        self.Status = None
        self.AddTimestamp = None
        self.BackendSet = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.LocationId = params.get("LocationId")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpCodes = params.get("HttpCodes")
        self.BalanceMode = params.get("BalanceMode")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = L7ListenerInfoBackend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7ListenerInfoRule(AbstractModel):
    """查询绑定了某主机的七层监听器时返回的转发规则。

    """

    def __init__(self):
        """
        :param Domain: 转发域名。\n        :type Domain: str\n        :param DomainId: 转发域名实例ID。\n        :type DomainId: str\n        :param Status: 当前绑定关系的健康检查状态（Dead代表不健康，Alive代表健康）。\n        :type Status: int\n        :param AddTimestamp: 创建时间戳。\n        :type AddTimestamp: str\n        :param LocationSet: 该转发域名下面的转发路径列表。\n        :type LocationSet: list of L7ListenerInfoLocation\n        """
        self.Domain = None
        self.DomainId = None
        self.Status = None
        self.AddTimestamp = None
        self.LocationSet = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        if params.get("LocationSet") is not None:
            self.LocationSet = []
            for item in params.get("LocationSet"):
                obj = L7ListenerInfoLocation()
                obj._deserialize(item)
                self.LocationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7Rule(AbstractModel):
    """获取七层监听器转发规则时返回的转发规则。

    """

    def __init__(self):
        """
        :param Domain: 转发域名。\n        :type Domain: str\n        :param DomainId: 转发域名实例ID。\n        :type DomainId: str\n        :param Status: 转发路径当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。\n        :type Status: int\n        :param AddTimestamp: 创建时间戳。\n        :type AddTimestamp: str\n        :param LocationSet: 该转发域名下面的转发路径列表。\n        :type LocationSet: list of L7RulesLocation\n        """
        self.Domain = None
        self.DomainId = None
        self.Status = None
        self.AddTimestamp = None
        self.LocationSet = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        if params.get("LocationSet") is not None:
            self.LocationSet = []
            for item in params.get("LocationSet"):
                obj = L7RulesLocation()
                obj._deserialize(item)
                self.LocationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RulesLocation(AbstractModel):
    """获取七层转发规则时返回的转发域名下面的转发路径。

    """

    def __init__(self):
        """
        :param Url: 转发路径。\n        :type Url: str\n        :param LocationId: 转发路径实例ID。\n        :type LocationId: str\n        :param SessionExpire: 会话保持时间。\n        :type SessionExpire: int\n        :param HealthSwitch: 是否开启健康检查。\n        :type HealthSwitch: int\n        :param HttpCheckPath: 健康检查检查路径。\n        :type HttpCheckPath: str\n        :param HttpCheckDomain: 健康检查检查域名。\n        :type HttpCheckDomain: str\n        :param IntervalTime: 健康检查检查间隔时间。\n        :type IntervalTime: int\n        :param HealthNum: 健康检查健康阈值。\n        :type HealthNum: int\n        :param UnhealthNum: 健康检查不健康阈值。\n        :type UnhealthNum: int\n        :param HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。\n        :type HttpCodes: list of int non-negative\n        :param BalanceMode: 均衡方式。\n        :type BalanceMode: str\n        :param Status: 转发路径当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。\n        :type Status: int\n        :param AddTimestamp: 创建时间戳。\n        :type AddTimestamp: str\n        """
        self.Url = None
        self.LocationId = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpCodes = None
        self.BalanceMode = None
        self.Status = None
        self.AddTimestamp = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.LocationId = params.get("LocationId")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpCodes = params.get("HttpCodes")
        self.BalanceMode = params.get("BalanceMode")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """获取负载均衡实例列表时返回的负载均衡信息。

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡器ID\n        :type LoadBalancerId: str\n        :param ProjectId: 项目ID，通过v2/DescribeProject 接口获得\n        :type ProjectId: int\n        :param LoadBalancerName: 负载均衡器名称\n        :type LoadBalancerName: str\n        :param LoadBalancerType: 负载均衡的类型 : open表示公网负载均衡类型，internal表示内网负载均衡类型\n        :type LoadBalancerType: str\n        :param Exclusive: 是否筛选独占集群，0表示非独占集群，1表示四层独占集群，2表示七层独占集群，3表示四层和七层独占集群，4表示共享容灾\n        :type Exclusive: int\n        :param TgwSetType: 该负载均衡对应的tgw集群（fullnat,tunnel,dnat）\n        :type TgwSetType: str\n        :param Domain: 负载均衡域名。规则：1-60个小写英文字母、数字、点号“.”或连接线“-”。内网类型的负载均衡不能配置该字段\n        :type Domain: str\n        :param VpcId: 该负载均衡对应的所在的VpcId\n        :type VpcId: str\n        :param SubnetId: 该负载均衡对应的所在的SubnetId\n        :type SubnetId: str\n        :param Status: 无\n        :type Status: int\n        :param PayMode: 无\n        :type PayMode: str\n        :param LatestPayMode: 无\n        :type LatestPayMode: str\n        :param CreateTime: 无\n        :type CreateTime: str\n        :param StatusTime: 无\n        :type StatusTime: str\n        :param VpcName: 私有网络名称。\n        :type VpcName: str\n        :param VpcCidrBlock: 私有网络Cidr。\n        :type VpcCidrBlock: str\n        :param LoadBalancerVips: 负载均衡的IPV4的VIP。\n        :type LoadBalancerVips: list of str\n        :param SupportListenerTypes: 无\n        :type SupportListenerTypes: list of str\n        :param Bandwidth: 无\n        :type Bandwidth: int\n        :param ConfId: 负载均衡个性化配置ID\n        :type ConfId: str\n        :param ConfName: 无\n        :type ConfName: str\n        :param LoadBalancerVipv6s: 负载均衡的IPV6的VIP。\n        :type LoadBalancerVipv6s: list of str\n        :param IpProtocolType: 负载均衡IP协议类型。ipv4或者ipv6。\n        :type IpProtocolType: str\n        :param BzPayMode: 保障型网关计费形式\n        :type BzPayMode: str\n        :param BzL4Metrics: 保障型网关四层计费指标\n        :type BzL4Metrics: str\n        :param BzL7Metrics: 保障型网关七层计费指标\n        :type BzL7Metrics: str\n        :param IntVpcId: 该负载均衡对应的所在的整形类型的VpcId\n        :type IntVpcId: int\n        :param CurVips: 负载均衡的IPV6或者IPV4的VIP。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CurVips: list of str\n        """
        self.LoadBalancerId = None
        self.ProjectId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.Exclusive = None
        self.TgwSetType = None
        self.Domain = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.PayMode = None
        self.LatestPayMode = None
        self.CreateTime = None
        self.StatusTime = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.LoadBalancerVips = None
        self.SupportListenerTypes = None
        self.Bandwidth = None
        self.ConfId = None
        self.ConfName = None
        self.LoadBalancerVipv6s = None
        self.IpProtocolType = None
        self.BzPayMode = None
        self.BzL4Metrics = None
        self.BzL7Metrics = None
        self.IntVpcId = None
        self.CurVips = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ProjectId = params.get("ProjectId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Exclusive = params.get("Exclusive")
        self.TgwSetType = params.get("TgwSetType")
        self.Domain = params.get("Domain")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.PayMode = params.get("PayMode")
        self.LatestPayMode = params.get("LatestPayMode")
        self.CreateTime = params.get("CreateTime")
        self.StatusTime = params.get("StatusTime")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.SupportListenerTypes = params.get("SupportListenerTypes")
        self.Bandwidth = params.get("Bandwidth")
        self.ConfId = params.get("ConfId")
        self.ConfName = params.get("ConfName")
        self.LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self.IpProtocolType = params.get("IpProtocolType")
        self.BzPayMode = params.get("BzPayMode")
        self.BzL4Metrics = params.get("BzL4Metrics")
        self.BzL7Metrics = params.get("BzL7Metrics")
        self.IntVpcId = params.get("IntVpcId")
        self.CurVips = params.get("CurVips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerPortInfoListener(AbstractModel):
    """获取黑石负载均衡端口相关信息时返回的监听器信息（四层和七层）。

    """

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器ID。\n        :type ListenerId: str\n        :param ListenerName: 监听器名称。\n        :type ListenerName: str\n        :param Protocol: 监听器协议类型，可选值：http，https，tcp，udp。\n        :type Protocol: str\n        :param LoadBalancerPort: 监听器的监听端口。\n        :type LoadBalancerPort: int\n        :param Bandwidth: 计费模式为按固定带宽方式时监听器的限速值，单位：Mbps。\n        :type Bandwidth: int\n        :param Status: 监听器当前状态（0代表创建中，1代表正常运行，2代表创建失败，3代表删除中，4代表删除失败）。\n        :type Status: int\n        :param Port: 与监听器绑定的主机端口。\n        :type Port: int\n        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.Status = None
        self.Port = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.Status = params.get("Status")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4BackendPortRequest(AbstractModel):
    """ModifyL4BackendPort请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。\n        :type ListenerId: str\n        :param InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        :param Port: 已绑定的主机端口。\n        :type Port: int\n        :param NewPort: 新的主机端口，可选值1~65535。\n        :type NewPort: int\n        :param BindType: 绑定类型。0：物理机  1：虚拟机 2：半托管机器\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.InstanceId = None
        self.Port = None
        self.NewPort = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.NewPort = params.get("NewPort")
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4BackendPortResponse(AbstractModel):
    """ModifyL4BackendPort返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL4BackendProbePortRequest(AbstractModel):
    """ModifyL4BackendProbePort请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        :param Port: 已绑定的主机端口。\n        :type Port: int\n        :param ProbePort: 新的探测端口，可选值1~65535。\n        :type ProbePort: int\n        :param BindType: 绑定类型。0：物理机 1：虚拟机IP 2：半托管机器\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.InstanceId = None
        self.Port = None
        self.ProbePort = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.ProbePort = params.get("ProbePort")
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4BackendProbePortResponse(AbstractModel):
    """ModifyL4BackendProbePort返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL4BackendWeightRequest(AbstractModel):
    """ModifyL4BackendWeight请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。\n        :type ListenerId: str\n        :param InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        :param Weight: 权重信息，可选值0~100。\n        :type Weight: int\n        :param Port: 已绑定的主机端口。\n        :type Port: int\n        :param BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.InstanceId = None
        self.Weight = None
        self.Port = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4BackendWeightResponse(AbstractModel):
    """ModifyL4BackendWeight返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL4ListenerRequest(AbstractModel):
    """ModifyL4Listener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 四层监听器ID。可通过接口DescribeL4Listeners查询。\n        :type ListenerId: str\n        :param ListenerName: 四层监听器名称。\n        :type ListenerName: str\n        :param SessionExpire: 会话保持时间，单位：秒。可选值：900~3600。\n        :type SessionExpire: int\n        :param HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）。默认值0，表示关闭。\n        :type HealthSwitch: int\n        :param TimeOut: 健康检查的响应超时时间，可选值：2-60，默认值：2，单位:秒。<br><font color="red">响应超时时间要小于检查间隔时间。</font>\n        :type TimeOut: int\n        :param IntervalTime: 健康检查间隔，默认值：5，可选值：5-300，单位：秒。\n        :type IntervalTime: int\n        :param HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。\n        :type HealthNum: int\n        :param UnhealthNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。\n        :type UnhealthNum: int\n        :param Bandwidth: 监听器最大带宽值，用于计费模式为固定带宽计费。可选值：0-1000，单位：Mbps。\n        :type Bandwidth: int\n        :param CustomHealthSwitch: 是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）\n        :type CustomHealthSwitch: int\n        :param InputType: 自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。\n        :type InputType: str\n        :param LineSeparatorType: 探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。\n        :type LineSeparatorType: int\n        :param HealthRequest: 自定义探测请求内容。\n        :type HealthRequest: str\n        :param HealthResponse: 自定义探测返回内容。\n        :type HealthResponse: str\n        :param ToaFlag: 是否开启toa。可选值：0（关闭）、1（开启），默认关闭。（该字段在负载均衡为fullnat类型下才生效）\n        :type ToaFlag: int\n        :param BalanceMode: 四层调度方式。wrr，wlc。\n        :type BalanceMode: str\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.Bandwidth = None
        self.CustomHealthSwitch = None
        self.InputType = None
        self.LineSeparatorType = None
        self.HealthRequest = None
        self.HealthResponse = None
        self.ToaFlag = None
        self.BalanceMode = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.Bandwidth = params.get("Bandwidth")
        self.CustomHealthSwitch = params.get("CustomHealthSwitch")
        self.InputType = params.get("InputType")
        self.LineSeparatorType = params.get("LineSeparatorType")
        self.HealthRequest = params.get("HealthRequest")
        self.HealthResponse = params.get("HealthResponse")
        self.ToaFlag = params.get("ToaFlag")
        self.BalanceMode = params.get("BalanceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4ListenerResponse(AbstractModel):
    """ModifyL4Listener返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL7BackendPortRequest(AbstractModel):
    """ModifyL7BackendPort请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。\n        :type DomainId: str\n        :param LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。\n        :type LocationId: str\n        :param InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        :param Port: 已绑定的主机端口。\n        :type Port: int\n        :param NewPort: 新的主机端口，可选值1~65535。\n        :type NewPort: int\n        :param BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.InstanceId = None
        self.Port = None
        self.NewPort = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.NewPort = params.get("NewPort")
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7BackendPortResponse(AbstractModel):
    """ModifyL7BackendPort返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL7BackendWeightRequest(AbstractModel):
    """ModifyL7BackendWeight请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。\n        :type DomainId: str\n        :param LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。\n        :type LocationId: str\n        :param InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        :param Weight: 权重信息，可选值0~100。\n        :type Weight: int\n        :param Port: 已绑定的主机端口。\n        :type Port: int\n        :param BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.InstanceId = None
        self.Weight = None
        self.Port = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7BackendWeightResponse(AbstractModel):
    """ModifyL7BackendWeight返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL7ListenerRequest(AbstractModel):
    """ModifyL7Listener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param ListenerName: 七层监听器名称。\n        :type ListenerName: str\n        :param SslMode: 认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。\n        :type SslMode: int\n        :param CertId: 服务端证书ID。\n        :type CertId: str\n        :param CertName: 服务端证书名称。\n        :type CertName: str\n        :param CertContent: 服务端证书内容。\n        :type CertContent: str\n        :param CertKey: 服务端证书密钥。\n        :type CertKey: str\n        :param CertCaId: 客户端证书ID。\n        :type CertCaId: str\n        :param CertCaName: 客户端证书名称。\n        :type CertCaName: str\n        :param CertCaContent: 客户端证书内容。\n        :type CertCaContent: str\n        :param Bandwidth: 计费模式为按固定带宽方式时监听器的限速值，可选值：0-1000，单位：Mbps。\n        :type Bandwidth: int\n        :param ForwardProtocol: 转发协议。当监听器Protocol为https时并且SslMode为1或2时，有意义。可选的值为0：https，1：spdy，2：http2，3：spdy+http2。\n        :type ForwardProtocol: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SslMode = None
        self.CertId = None
        self.CertName = None
        self.CertContent = None
        self.CertKey = None
        self.CertCaId = None
        self.CertCaName = None
        self.CertCaContent = None
        self.Bandwidth = None
        self.ForwardProtocol = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.CertContent = params.get("CertContent")
        self.CertKey = params.get("CertKey")
        self.CertCaId = params.get("CertCaId")
        self.CertCaName = params.get("CertCaName")
        self.CertCaContent = params.get("CertCaContent")
        self.Bandwidth = params.get("Bandwidth")
        self.ForwardProtocol = params.get("ForwardProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7ListenerResponse(AbstractModel):
    """ModifyL7Listener返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用[DescribeLoadBalancerTaskResult](/document/product/386/9308)接口来查询任务操作结果\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL7LocationRule(AbstractModel):
    """修改黑石负载均衡七层转发路径时待修改的七层转发规则信息。

    """

    def __init__(self):
        """
        :param DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。\n        :type DomainId: str\n        :param LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。\n        :type LocationId: str\n        :param Url: 转发路径。\n        :type Url: str\n        :param SessionExpire: 会话保持时间，单位：秒。可选值：30~3600。默认值0，表示不开启会话保持。\n        :type SessionExpire: int\n        :param HealthSwitch: 健康检查开关：1（开启）、0（关闭）。默认值0，表示关闭。\n        :type HealthSwitch: int\n        :param IntervalTime: 健康检查检查间隔时间，默认值：5，可选值：5-300，单位：秒。\n        :type IntervalTime: int\n        :param HealthNum: 健康检查健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。\n        :type HealthNum: int\n        :param UnhealthNum: 健康检查不健康阈值，默认值：5，表示当连续探测五次不健康则表示该转发不正常，可选值：2-10，单位：次。\n        :type UnhealthNum: int\n        :param HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。\n        :type HttpCodes: list of int non-negative\n        :param HttpCheckPath: 健康检查检查路径。\n        :type HttpCheckPath: str\n        :param HttpCheckDomain: 健康检查检查域名。如果规则的域名使用通配符或正则表达式，则健康检查检查域名可自定义，否则必须跟健康检查检查域名一样。不填表示不修改。\n        :type HttpCheckDomain: str\n        :param BalanceMode: 均衡方式：ip_hash、wrr。默认值wrr。\n        :type BalanceMode: str\n        :param Domain: 转发域名。\n        :type Domain: str\n        """
        self.DomainId = None
        self.LocationId = None
        self.Url = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpCodes = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.BalanceMode = None
        self.Domain = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        self.Url = params.get("Url")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpCodes = params.get("HttpCodes")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.BalanceMode = params.get("BalanceMode")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7LocationsRequest(AbstractModel):
    """ModifyL7Locations请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param RuleSet: 待更新的七层转发规则信息数组。\n        :type RuleSet: list of ModifyL7LocationRule\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.RuleSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = ModifyL7LocationRule()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7LocationsResponse(AbstractModel):
    """ModifyL7Locations返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerChargeModeListener(AbstractModel):
    """修改负载均衡计费方式的监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 监听器ID。\n        :type ListenerId: str\n        :param Protocol: 协议类型。\n        :type Protocol: str\n        :param Bandwidth: 带宽。\n        :type Bandwidth: int\n        """
        self.ListenerId = None
        self.Protocol = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerChargeModeRequest(AbstractModel):
    """ModifyLoadBalancerChargeMode请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。\n        :type LoadBalancerId: str\n        :param PayMode: 计费方式。flow或bandwidth。\n        :type PayMode: str\n        :param ListenerSet: 监听器信息，当计费方式选为 bandwidth 且此负载均衡实例下存在监听器时需填入此字段，可以自定义每个监听器带宽上限。\n        :type ListenerSet: list of ModifyLoadBalancerChargeModeListener\n        """
        self.LoadBalancerId = None
        self.PayMode = None
        self.ListenerSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.PayMode = params.get("PayMode")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = ModifyLoadBalancerChargeModeListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerChargeModeResponse(AbstractModel):
    """ModifyLoadBalancerChargeMode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerRequest(AbstractModel):
    """ModifyLoadBalancer请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param LoadBalancerName: 负载均衡器名称，规则：1-20个英文、汉字、数字、连接线“-”或下划线“_”。\n        :type LoadBalancerName: str\n        :param DomainPrefix: 域名前缀，负载均衡的域名由用户输入的域名前缀与配置文件中的域名后缀一起组合而成，保证是唯一的域名。规则：1-20个小写英文字母、数字或连接线“-”。内网类型的负载均衡不能配置该字段。\n        :type DomainPrefix: str\n        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.DomainPrefix = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.DomainPrefix = params.get("DomainPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerResponse(AbstractModel):
    """ModifyLoadBalancer返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ReplaceCertRequest(AbstractModel):
    """ReplaceCert请求参数结构体

    """

    def __init__(self):
        """
        :param OldCertId: 要被替换的证书ID\n        :type OldCertId: str\n        :param NewCert: 证书内容\n        :type NewCert: str\n        :param NewAlias: 证书名称\n        :type NewAlias: str\n        :param NewKey: 私钥内容，证书类型为SVR时不需要传递\n        :type NewKey: str\n        :param DeleteOld: 是否删除旧证书，0 表示不删除，1 表示删除\n        :type DeleteOld: int\n        """
        self.OldCertId = None
        self.NewCert = None
        self.NewAlias = None
        self.NewKey = None
        self.DeleteOld = None


    def _deserialize(self, params):
        self.OldCertId = params.get("OldCertId")
        self.NewCert = params.get("NewCert")
        self.NewAlias = params.get("NewAlias")
        self.NewKey = params.get("NewKey")
        self.DeleteOld = params.get("DeleteOld")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertResponse(AbstractModel):
    """ReplaceCert返回参数结构体

    """

    def __init__(self):
        """
        :param NewCertId: 新证书ID。\n        :type NewCertId: str\n        :param OldCertId: 旧证书ID。\n        :type OldCertId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NewCertId = None
        self.OldCertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NewCertId = params.get("NewCertId")
        self.OldCertId = params.get("OldCertId")
        self.RequestId = params.get("RequestId")


class SetTrafficMirrorAliasRequest(AbstractModel):
    """SetTrafficMirrorAlias请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID。\n        :type TrafficMirrorId: str\n        :param Alias: 流量镜像实例别名。\n        :type Alias: str\n        """
        self.TrafficMirrorId = None
        self.Alias = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTrafficMirrorAliasResponse(AbstractModel):
    """SetTrafficMirrorAlias返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTrafficMirrorHealthSwitchRequest(AbstractModel):
    """SetTrafficMirrorHealthSwitch请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID。\n        :type TrafficMirrorId: str\n        :param HealthSwitch: 健康检查开关，0：关闭，1：打开\n        :type HealthSwitch: int\n        :param HealthNum: 健康检查判断健康的次数，最小值2，最大值10。\n        :type HealthNum: int\n        :param UnhealthNum: 健康检查判断不健康的次数，最小值2，最大值10。\n        :type UnhealthNum: int\n        :param IntervalTime: 健康检查间隔，单位：秒，最小值5，最大值300。\n        :type IntervalTime: int\n        :param HttpCheckDomain: 检查的域名配置。\n        :type HttpCheckDomain: str\n        :param HttpCheckPath: 检查的路径配置。\n        :type HttpCheckPath: str\n        :param HttpCodes: 健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。\n        :type HttpCodes: list of int\n        """
        self.TrafficMirrorId = None
        self.HealthSwitch = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.IntervalTime = None
        self.HttpCheckDomain = None
        self.HttpCheckPath = None
        self.HttpCodes = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.HealthSwitch = params.get("HealthSwitch")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.IntervalTime = params.get("IntervalTime")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCodes = params.get("HttpCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTrafficMirrorHealthSwitchResponse(AbstractModel):
    """SetTrafficMirrorHealthSwitch返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class TrafficMirror(AbstractModel):
    """获取流量镜像实例的列表信息时返回的流量镜像信息。

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像ID。\n        :type TrafficMirrorId: str\n        :param Alias: 流量镜像名称。\n        :type Alias: str\n        :param VpcId: 流量镜像所在的私有网络ID。\n        :type VpcId: str\n        :param LoadBalancerType: 接收机负载均衡方式。wrr，ip_hash，wlc。\n        :type LoadBalancerType: str\n        :param HealthSwitch: 是否开始对接收机的健康检查。0：关闭，非0：开启。\n        :type HealthSwitch: int\n        :param HealthNum: 健康阈值。\n        :type HealthNum: int\n        :param UnhealthNum: 不健康阈值。\n        :type UnhealthNum: int\n        :param IntervalTime: 检查间隔。\n        :type IntervalTime: int\n        :param HttpCheckDomain: 检查域名。\n        :type HttpCheckDomain: str\n        :param HttpCheckPath: 检查目录。\n        :type HttpCheckPath: str\n        :param HttpCodes: 健康检查返回码。 1：1xx，2：2xx，3：3xx，4：4xx，5：5xx。\n        :type HttpCodes: list of int\n        :param CreateTime: 创建时间。\n        :type CreateTime: str\n        :param VpcCidrBlock: 流量镜像所在私有网络的Cidr。\n        :type VpcCidrBlock: str\n        :param VpcName: 流量镜像所在私有网络的名称。\n        :type VpcName: str\n        """
        self.TrafficMirrorId = None
        self.Alias = None
        self.VpcId = None
        self.LoadBalancerType = None
        self.HealthSwitch = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.IntervalTime = None
        self.HttpCheckDomain = None
        self.HttpCheckPath = None
        self.HttpCodes = None
        self.CreateTime = None
        self.VpcCidrBlock = None
        self.VpcName = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.Alias = params.get("Alias")
        self.VpcId = params.get("VpcId")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.HealthSwitch = params.get("HealthSwitch")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.IntervalTime = params.get("IntervalTime")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCodes = params.get("HttpCodes")
        self.CreateTime = params.get("CreateTime")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficMirrorListener(AbstractModel):
    """获取流量镜像的监听器列表信息时返回的与流量镜像绑定的监听器信息。

    """

    def __init__(self):
        """
        :param ListenerId: 监听器ID。\n        :type ListenerId: str\n        :param ListenerName: 监听器名称。\n        :type ListenerName: str\n        :param Protocol: 七层监听器协议类型，可选值：http,https。\n        :type Protocol: str\n        :param LoadBalancerPort: 监听器的监听端口。\n        :type LoadBalancerPort: int\n        :param Bandwidth: 当前带宽。\n        :type Bandwidth: int\n        :param MaxBandwidth: 带宽上限。\n        :type MaxBandwidth: int\n        :param ListenerType: 监听器类型。\n        :type ListenerType: str\n        :param SslMode: 认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。\n        :type SslMode: int\n        :param CertId: 服务端证书ID。\n        :type CertId: str\n        :param CertCaId: 客户端证书ID。\n        :type CertCaId: str\n        :param AddTimestamp: 添加时间。\n        :type AddTimestamp: str\n        :param LoadBalancerId: 负载均衡ID。\n        :type LoadBalancerId: str\n        :param VpcName: 私有网络名称。\n        :type VpcName: str\n        :param VpcCidrBlock: 私有网络Cidr。\n        :type VpcCidrBlock: str\n        :param LoadBalancerVips: 负载均衡的VIP。\n        :type LoadBalancerVips: list of str\n        :param LoadBalancerName: 负载均衡名称。\n        :type LoadBalancerName: str\n        :param LoadBalancerVipv6s: 负载均衡的IPV6的VIP。\n        :type LoadBalancerVipv6s: list of str\n        :param IpProtocolType: 支持的IP协议类型。ipv4或者是ipv6。\n        :type IpProtocolType: str\n        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.MaxBandwidth = None
        self.ListenerType = None
        self.SslMode = None
        self.CertId = None
        self.CertCaId = None
        self.AddTimestamp = None
        self.LoadBalancerId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.LoadBalancerVips = None
        self.LoadBalancerName = None
        self.LoadBalancerVipv6s = None
        self.IpProtocolType = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.AddTimestamp = params.get("AddTimestamp")
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self.IpProtocolType = params.get("IpProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficMirrorPortStatus(AbstractModel):
    """流量镜像健康检查返回的接收机的端口及状态信息。

    """

    def __init__(self):
        """
        :param Port: 接收机端口。\n        :type Port: int\n        :param Status: 状态。\n        :type Status: str\n        """
        self.Port = None
        self.Status = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficMirrorReceiver(AbstractModel):
    """获取与流量镜像绑定的接收机信息时返回的接收机信息。

    """

    def __init__(self):
        """
        :param InstanceId: 接收机实例ID。\n        :type InstanceId: str\n        :param Port: 接收机接收端口。\n        :type Port: int\n        :param Weight: 接收机权重。\n        :type Weight: int\n        :param TrafficMirrorId: 流量镜像ID。\n        :type TrafficMirrorId: str\n        :param Alias: 接收机别名。\n        :type Alias: str\n        :param LanIp: 接收机内网IP地址。\n        :type LanIp: str\n        :param SubnetId: 接收机所在的子网的ID。\n        :type SubnetId: str\n        :param SubnetName: 接收机所在的子网的名称。\n        :type SubnetName: str\n        :param SubnetCidrBlock: 接收机所在的子网的Cidr。\n        :type SubnetCidrBlock: str\n        :param VpcId: 接收机所在的私有网络的ID。\n        :type VpcId: str\n        :param VpcName: 接收机所在的私有网络的名称。\n        :type VpcName: str\n        :param VpcCidrBlock: 接收机所在的私有网络的Cidr。\n        :type VpcCidrBlock: str\n        :param HealthStatus: 接收机的健康状态。\n        :type HealthStatus: str\n        :param Operates: 接收机的可以执行的操作集合。\n        :type Operates: list of str\n        """
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.TrafficMirrorId = None
        self.Alias = None
        self.LanIp = None
        self.SubnetId = None
        self.SubnetName = None
        self.SubnetCidrBlock = None
        self.VpcId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.HealthStatus = None
        self.Operates = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.Alias = params.get("Alias")
        self.LanIp = params.get("LanIp")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.HealthStatus = params.get("HealthStatus")
        self.Operates = params.get("Operates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficMirrorReciversStatus(AbstractModel):
    """流量镜像健康检查返回的接收机状态信息。

    """

    def __init__(self):
        """
        :param LanIp: 内网IP。\n        :type LanIp: str\n        :param ReceiversPortStatusSet: 端口及对应的状态。\n        :type ReceiversPortStatusSet: list of TrafficMirrorPortStatus\n        """
        self.LanIp = None
        self.ReceiversPortStatusSet = None


    def _deserialize(self, params):
        self.LanIp = params.get("LanIp")
        if params.get("ReceiversPortStatusSet") is not None:
            self.ReceiversPortStatusSet = []
            for item in params.get("ReceiversPortStatusSet"):
                obj = TrafficMirrorPortStatus()
                obj._deserialize(item)
                self.ReceiversPortStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL4Backend(AbstractModel):
    """待与四层监听器解绑的物理机主机、虚拟机或半托管主机信息。

    """

    def __init__(self):
        """
        :param Port: 待解绑的主机端口，可选值1~65535。\n        :type Port: int\n        :param InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        """
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL4BackendsRequest(AbstractModel):
    """UnbindL4Backends请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。\n        :type ListenerId: str\n        :param BackendSet: 待解绑的主机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。\n        :type BackendSet: list of UnbindL4Backend\n        :param BindType: 绑定类型。0：物理机 1：虚拟机 2：半托管机器\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.BackendSet = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = UnbindL4Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL4BackendsResponse(AbstractModel):
    """UnbindL4Backends返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindL7Backend(AbstractModel):
    """待与七层监听器转发规则解绑的物理机主机、虚拟机或半托管主机信息。

    """

    def __init__(self):
        """
        :param Port: 待解绑的主机端口，可选值1~65535。\n        :type Port: int\n        :param InstanceId: 黑石物理机主机ID、虚拟机IP或者是半托管主机ID。\n        :type InstanceId: str\n        """
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL7BackendsRequest(AbstractModel):
    """UnbindL7Backends请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID，可通过接口DescribeLoadBalancers查询。\n        :type LoadBalancerId: str\n        :param ListenerId: 七层监听器实例ID，可通过接口DescribeL7Listeners查询。\n        :type ListenerId: str\n        :param DomainId: 转发域名实例ID，可通过接口DescribeL7Rules查询。\n        :type DomainId: str\n        :param LocationId: 转发路径实例ID，可通过接口DescribeL7Rules查询。\n        :type LocationId: str\n        :param BackendSet: 待绑定的主机信息。\n        :type BackendSet: list of UnbindL7Backend\n        :param BindType: 绑定类型。0：物理机  1：虚拟机 2：半托管机器\n        :type BindType: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.BackendSet = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = UnbindL7Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindL7BackendsResponse(AbstractModel):
    """UnbindL7Backends返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindTrafficMirrorListenersRequest(AbstractModel):
    """UnbindTrafficMirrorListeners请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID。\n        :type TrafficMirrorId: str\n        :param ListenerIds: 七层监听器实例ID数组，可通过接口DescribeL7Listeners查询。\n        :type ListenerIds: list of str\n        """
        self.TrafficMirrorId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindTrafficMirrorListenersResponse(AbstractModel):
    """UnbindTrafficMirrorListeners返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindTrafficMirrorReceiver(AbstractModel):
    """待与流量镜像解绑的接收机信息。

    """

    def __init__(self):
        """
        :param Port: 待解绑的主机端口，可选值1~65535。\n        :type Port: int\n        :param InstanceId: 待解绑的主机实例ID。\n        :type InstanceId: str\n        """
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindTrafficMirrorReceiversRequest(AbstractModel):
    """UnbindTrafficMirrorReceivers请求参数结构体

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量镜像实例ID。\n        :type TrafficMirrorId: str\n        :param ReceiverSet: 待绑定的主机实例ID和端口数组。\n        :type ReceiverSet: list of UnbindTrafficMirrorReceiver\n        """
        self.TrafficMirrorId = None
        self.ReceiverSet = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self.ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = UnbindTrafficMirrorReceiver()
                obj._deserialize(item)
                self.ReceiverSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindTrafficMirrorReceiversResponse(AbstractModel):
    """UnbindTrafficMirrorReceivers返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。该接口为异步任务，可根据本参数调用DescribeLoadBalancerTaskResult接口来查询任务操作结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UploadCertRequest(AbstractModel):
    """UploadCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertType: 证书类型，可选值：CA，SVR。\n        :type CertType: str\n        :param Cert: 证书内容。\n        :type Cert: str\n        :param Alias: 证书别名。\n        :type Alias: str\n        :param Key: 私钥内容，证书类型为SVR时不需要传递。\n        :type Key: str\n        """
        self.CertType = None
        self.Cert = None
        self.Alias = None
        self.Key = None


    def _deserialize(self, params):
        self.CertType = params.get("CertType")
        self.Cert = params.get("Cert")
        self.Alias = params.get("Alias")
        self.Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertResponse(AbstractModel):
    """UploadCert返回参数结构体

    """

    def __init__(self):
        """
        :param CertId: 新建的证书ID。\n        :type CertId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.RequestId = params.get("RequestId")