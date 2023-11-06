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


class AssociateTargetGroupsRequest(AbstractModel):
    """AssociateTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Associations: 绑定的关系数组。
        :type Associations: list of TargetGroupAssociation
        """
        self._Associations = None

    @property
    def Associations(self):
        return self._Associations

    @Associations.setter
    def Associations(self, Associations):
        self._Associations = Associations


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self._Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self._Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateTargetGroupsResponse(AbstractModel):
    """AssociateTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AssociationItem(AbstractModel):
    """目标组关联到的规则

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 关联到的负载均衡ID
        :type LoadBalancerId: str
        :param _ListenerId: 关联到的监听器ID
        :type ListenerId: str
        :param _LocationId: 关联到的转发规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationId: str
        :param _Protocol: 关联到的监听器协议类型，如HTTP,TCP,
        :type Protocol: str
        :param _Port: 关联到的监听器端口
        :type Port: int
        :param _Domain: 关联到的转发规则域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Url: 关联到的转发规则URL
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _LoadBalancerName: 负载均衡名称
        :type LoadBalancerName: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationId = None
        self._Protocol = None
        self._Port = None
        self._Domain = None
        self._Url = None
        self._LoadBalancerName = None
        self._ListenerName = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._ListenerName = params.get("ListenerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoRewriteRequest(AbstractModel):
    """AutoRewrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: HTTPS:443监听器的ID。
        :type ListenerId: str
        :param _Domains: HTTPS:443监听器下需要重定向的域名，若不填，则对HTTPS:443监听器下的所有域名都设置重定向。
        :type Domains: list of str
        :param _RewriteCodes: 重定向状态码，可取值301,302,307。
        :type RewriteCodes: list of int
        :param _TakeUrls: 重定向是否携带匹配的URL。
        :type TakeUrls: list of bool
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domains = None
        self._RewriteCodes = None
        self._TakeUrls = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def RewriteCodes(self):
        return self._RewriteCodes

    @RewriteCodes.setter
    def RewriteCodes(self, RewriteCodes):
        self._RewriteCodes = RewriteCodes

    @property
    def TakeUrls(self):
        return self._TakeUrls

    @TakeUrls.setter
    def TakeUrls(self, TakeUrls):
        self._TakeUrls = TakeUrls


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domains = params.get("Domains")
        self._RewriteCodes = params.get("RewriteCodes")
        self._TakeUrls = params.get("TakeUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoRewriteResponse(AbstractModel):
    """AutoRewrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Backend(AbstractModel):
    """监听器绑定的后端服务的详细信息

    """

    def __init__(self):
        r"""
        :param _Type: 后端服务的类型，可取：CVM、ENI、CCN
        :type Type: str
        :param _InstanceId: 后端服务的唯一 ID，如 ins-abcd1234
        :type InstanceId: str
        :param _Port: 后端服务的监听端口
        :type Port: int
        :param _Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param _PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param _PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param _InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _RegisteredTime: 后端服务被绑定的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        :param _EniId: 弹性网卡唯一ID，如 eni-1234abcd
注意：此字段可能返回 null，表示取不到有效值。
        :type EniId: str
        :param _Tag: 标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        """
        self._Type = None
        self._InstanceId = None
        self._Port = None
        self._Weight = None
        self._PublicIpAddresses = None
        self._PrivateIpAddresses = None
        self._InstanceName = None
        self._RegisteredTime = None
        self._EniId = None
        self._Tag = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegisteredTime(self):
        return self._RegisteredTime

    @RegisteredTime.setter
    def RegisteredTime(self, RegisteredTime):
        self._RegisteredTime = RegisteredTime

    @property
    def EniId(self):
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._InstanceName = params.get("InstanceName")
        self._RegisteredTime = params.get("RegisteredTime")
        self._EniId = params.get("EniId")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BasicTargetGroupInfo(AbstractModel):
    """监听器或者转发规则绑定的目标组基本信息

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param _TargetGroupName: 目标组名称
        :type TargetGroupName: str
        """
        self._TargetGroupId = None
        self._TargetGroupName = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡ID。
        :type LoadBalancerId: str
        :param _Targets: 解绑目标。
        :type Targets: list of BatchTarget
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailListenerIdSet: 解绑失败的监听器ID。
        :type FailListenerIdSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailListenerIdSet = None
        self._RequestId = None

    @property
    def FailListenerIdSet(self):
        return self._FailListenerIdSet

    @FailListenerIdSet.setter
    def FailListenerIdSet(self, FailListenerIdSet):
        self._FailListenerIdSet = FailListenerIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailListenerIdSet = params.get("FailListenerIdSet")
        self._RequestId = params.get("RequestId")


class BatchModifyTargetTagRequest(AbstractModel):
    """BatchModifyTargetTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ModifyList: 要批量修改标签的列表。
        :type ModifyList: list of RsTagRule
        """
        self._LoadBalancerId = None
        self._ModifyList = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModifyList(self):
        return self._ModifyList

    @ModifyList.setter
    def ModifyList(self, ModifyList):
        self._ModifyList = ModifyList


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self._ModifyList = []
            for item in params.get("ModifyList"):
                obj = RsTagRule()
                obj._deserialize(item)
                self._ModifyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTargetTagResponse(AbstractModel):
    """BatchModifyTargetTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ModifyList: 要批量修改权重的列表。
        :type ModifyList: list of RsWeightRule
        """
        self._LoadBalancerId = None
        self._ModifyList = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModifyList(self):
        return self._ModifyList

    @ModifyList.setter
    def ModifyList(self, ModifyList):
        self._ModifyList = ModifyList


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self._ModifyList = []
            for item in params.get("ModifyList"):
                obj = RsWeightRule()
                obj._deserialize(item)
                self._ModifyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡ID。
        :type LoadBalancerId: str
        :param _Targets: 绑定目标。
        :type Targets: list of BatchTarget
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailListenerIdSet: 绑定失败的监听器ID，如为空表示全部绑定成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailListenerIdSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailListenerIdSet = None
        self._RequestId = None

    @property
    def FailListenerIdSet(self):
        return self._FailListenerIdSet

    @FailListenerIdSet.setter
    def FailListenerIdSet(self, FailListenerIdSet):
        self._FailListenerIdSet = FailListenerIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailListenerIdSet = params.get("FailListenerIdSet")
        self._RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """批量绑定类型

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID。
        :type ListenerId: str
        :param _Port: 绑定端口。
        :type Port: int
        :param _InstanceId: 子机 ID。表示绑定主网卡主 IP。
        :type InstanceId: str
        :param _EniIp: 绑定 IP 时需要传入此参数，支持弹性网卡的 IP 和其他内网 IP，如果是弹性网卡则必须先绑定至CVM，然后才能绑定到负载均衡实例。
注意：参数 InstanceId、EniIp 只能传入一个且必须传入一个。如果绑定双栈IPV6子机，必须传该参数。
        :type EniIp: str
        :param _Weight: 子机权重，范围[0, 100]。绑定时如果不存在，则默认为10。
        :type Weight: int
        :param _LocationId: 七层规则 ID。
        :type LocationId: str
        :param _Tag: 标签。
        :type Tag: str
        """
        self._ListenerId = None
        self._Port = None
        self._InstanceId = None
        self._EniIp = None
        self._Weight = None
        self._LocationId = None
        self._Tag = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EniIp(self):
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._EniIp = params.get("EniIp")
        self._Weight = params.get("Weight")
        self._LocationId = params.get("LocationId")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDetailItem(AbstractModel):
    """绑定关系，包含监听器名字、协议、url、vport。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 配置绑定的CLB ID
        :type LoadBalancerId: str
        :param _ListenerId: 配置绑定的监听器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _Domain: 配置绑定的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _LocationId: 配置绑定的规则
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationId: str
        :param _ListenerName: 监听器名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _Protocol: 监听器协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Vport: 监听器端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param _Url: location的url
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _UconfigId: 配置ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UconfigId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domain = None
        self._LocationId = None
        self._ListenerName = None
        self._Protocol = None
        self._Vport = None
        self._Url = None
        self._UconfigId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def UconfigId(self):
        return self._UconfigId

    @UconfigId.setter
    def UconfigId(self, UconfigId):
        self._UconfigId = UconfigId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._LocationId = params.get("LocationId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._Vport = params.get("Vport")
        self._Url = params.get("Url")
        self._UconfigId = params.get("UconfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockedIP(AbstractModel):
    """加入了12306黑名单的IP

    """

    def __init__(self):
        r"""
        :param _IP: 黑名单IP
        :type IP: str
        :param _CreateTime: 加入黑名单的时间
        :type CreateTime: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        """
        self._IP = None
        self._CreateTime = None
        self._ExpireTime = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertIdRelatedWithLoadBalancers(AbstractModel):
    """证书ID，以及与该证书ID关联的负载均衡实例列表

    """

    def __init__(self):
        r"""
        :param _CertId: 证书ID
        :type CertId: str
        :param _LoadBalancers: 与证书关联的负载均衡实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancers: list of LoadBalancer
        """
        self._CertId = None
        self._LoadBalancers = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def LoadBalancers(self):
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertInfo(AbstractModel):
    """证书信息

    """

    def __init__(self):
        r"""
        :param _CertId: 证书 ID，如果不填写此项则必须上传证书内容，包括CertName, CertContent，若为服务端证书必须包含CertKey。
        :type CertId: str
        :param _CertName: 上传证书的名称，如果没有 CertId，则此项必传。
        :type CertName: str
        :param _CertContent: 上传证书的公钥；如果没有 CertId，则此项必传。
        :type CertContent: str
        :param _CertKey: 上传服务端证书的私钥；如果没有 CertId，则此项必传。
        :type CertKey: str
        """
        self._CertId = None
        self._CertName = None
        self._CertContent = None
        self._CertKey = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertContent(self):
        return self._CertContent

    @CertContent.setter
    def CertContent(self, CertContent):
        self._CertContent = CertContent

    @property
    def CertKey(self):
        return self._CertKey

    @CertKey.setter
    def CertKey(self, CertKey):
        self._CertKey = CertKey


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._CertContent = params.get("CertContent")
        self._CertKey = params.get("CertKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInput(AbstractModel):
    """证书信息

    """

    def __init__(self):
        r"""
        :param _SSLMode: 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证
        :type SSLMode: str
        :param _CertId: 服务端证书的 ID，如果不填写此项则必须上传证书，包括 CertContent，CertKey，CertName。
        :type CertId: str
        :param _CertCaId: 客户端证书的 ID，当监听器采用双向认证，即 SSLMode=MUTUAL 时，如果不填写此项则必须上传客户端证书，包括 CertCaContent，CertCaName。
        :type CertCaId: str
        :param _CertName: 上传服务端证书的名称，如果没有 CertId，则此项必传。
        :type CertName: str
        :param _CertKey: 上传服务端证书的 key，如果没有 CertId，则此项必传。
        :type CertKey: str
        :param _CertContent: 上传服务端证书的内容，如果没有 CertId，则此项必传。
        :type CertContent: str
        :param _CertCaName: 上传客户端 CA 证书的名称，如果 SSLMode=mutual，如果没有 CertCaId，则此项必传。
        :type CertCaName: str
        :param _CertCaContent: 上传客户端证书的内容，如果 SSLMode=mutual，如果没有 CertCaId，则此项必传。
        :type CertCaContent: str
        """
        self._SSLMode = None
        self._CertId = None
        self._CertCaId = None
        self._CertName = None
        self._CertKey = None
        self._CertContent = None
        self._CertCaName = None
        self._CertCaContent = None

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertKey(self):
        return self._CertKey

    @CertKey.setter
    def CertKey(self, CertKey):
        self._CertKey = CertKey

    @property
    def CertContent(self):
        return self._CertContent

    @CertContent.setter
    def CertContent(self, CertContent):
        self._CertContent = CertContent

    @property
    def CertCaName(self):
        return self._CertCaName

    @CertCaName.setter
    def CertCaName(self, CertCaName):
        self._CertCaName = CertCaName

    @property
    def CertCaContent(self):
        return self._CertCaContent

    @CertCaContent.setter
    def CertCaContent(self, CertCaContent):
        self._CertCaContent = CertCaContent


    def _deserialize(self, params):
        self._SSLMode = params.get("SSLMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._CertName = params.get("CertName")
        self._CertKey = params.get("CertKey")
        self._CertContent = params.get("CertContent")
        self._CertCaName = params.get("CertCaName")
        self._CertCaContent = params.get("CertCaContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateOutput(AbstractModel):
    """证书相关信息

    """

    def __init__(self):
        r"""
        :param _SSLMode: 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证
        :type SSLMode: str
        :param _CertId: 服务端证书的ID。
        :type CertId: str
        :param _CertCaId: 客户端证书的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertCaId: str
        :param _ExtCertIds: 多本服务器证书场景扩展的服务器证书ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtCertIds: list of str
        """
        self._SSLMode = None
        self._CertId = None
        self._CertCaId = None
        self._ExtCertIds = None

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def ExtCertIds(self):
        return self._ExtCertIds

    @ExtCertIds.setter
    def ExtCertIds(self, ExtCertIds):
        self._ExtCertIds = ExtCertIds


    def _deserialize(self, params):
        self._SSLMode = params.get("SSLMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._ExtCertIds = params.get("ExtCertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalHealth(AbstractModel):
    """传统型负载均衡后端服务的健康状态

    """

    def __init__(self):
        r"""
        :param _IP: 后端服务的内网 IP
        :type IP: str
        :param _Port: 后端服务的端口
        :type Port: int
        :param _ListenerPort: 负载均衡的监听端口
        :type ListenerPort: int
        :param _Protocol: 转发协议
        :type Protocol: str
        :param _HealthStatus: 健康检查结果，1 表示健康，0 表示不健康
        :type HealthStatus: int
        """
        self._IP = None
        self._Port = None
        self._ListenerPort = None
        self._Protocol = None
        self._HealthStatus = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ListenerPort(self):
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        self._ListenerPort = params.get("ListenerPort")
        self._Protocol = params.get("Protocol")
        self._HealthStatus = params.get("HealthStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalListener(AbstractModel):
    """传统型负载均衡监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 负载均衡监听器ID
        :type ListenerId: str
        :param _ListenerPort: 负载均衡监听器端口
        :type ListenerPort: int
        :param _InstancePort: 监听器后端转发端口
        :type InstancePort: int
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Protocol: 监听器协议类型
        :type Protocol: str
        :param _SessionExpire: 会话保持时间
        :type SessionExpire: int
        :param _HealthSwitch: 是否开启了健康检查：1（开启）、0（关闭）
        :type HealthSwitch: int
        :param _TimeOut: 响应超时时间
        :type TimeOut: int
        :param _IntervalTime: 检查间隔
        :type IntervalTime: int
        :param _HealthNum: 健康阈值
        :type HealthNum: int
        :param _UnhealthNum: 不健康阈值
        :type UnhealthNum: int
        :param _HttpHash: 传统型公网负载均衡的 HTTP、HTTPS 监听器的请求均衡方法。wrr 表示按权重轮询，ip_hash 表示根据访问的源 IP 进行一致性哈希方式来分发
        :type HttpHash: str
        :param _HttpCode: 传统型公网负载均衡的 HTTP、HTTPS 监听器的健康检查返回码。具体可参考创建监听器中对该字段的解释
        :type HttpCode: int
        :param _HttpCheckPath: 传统型公网负载均衡的 HTTP、HTTPS 监听器的健康检查路径
        :type HttpCheckPath: str
        :param _SSLMode: 传统型公网负载均衡的 HTTPS 监听器的认证方式
        :type SSLMode: str
        :param _CertId: 传统型公网负载均衡的 HTTPS 监听器的服务端证书 ID
        :type CertId: str
        :param _CertCaId: 传统型公网负载均衡的 HTTPS 监听器的客户端证书 ID
        :type CertCaId: str
        :param _Status: 监听器的状态，0 表示创建中，1 表示运行中
        :type Status: int
        """
        self._ListenerId = None
        self._ListenerPort = None
        self._InstancePort = None
        self._ListenerName = None
        self._Protocol = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._HttpHash = None
        self._HttpCode = None
        self._HttpCheckPath = None
        self._SSLMode = None
        self._CertId = None
        self._CertCaId = None
        self._Status = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerPort(self):
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def InstancePort(self):
        return self._InstancePort

    @InstancePort.setter
    def InstancePort(self, InstancePort):
        self._InstancePort = InstancePort

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SessionExpire(self):
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def HttpHash(self):
        return self._HttpHash

    @HttpHash.setter
    def HttpHash(self, HttpHash):
        self._HttpHash = HttpHash

    @property
    def HttpCode(self):
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def HttpCheckPath(self):
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerPort = params.get("ListenerPort")
        self._InstancePort = params.get("InstancePort")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._HttpHash = params.get("HttpHash")
        self._HttpCode = params.get("HttpCode")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._SSLMode = params.get("SSLMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalLoadBalancerInfo(AbstractModel):
    """负载均衡信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 后端实例ID
        :type InstanceId: str
        :param _LoadBalancerIds: 负载均衡实例ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerIds: list of str
        """
        self._InstanceId = None
        self._LoadBalancerIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalTarget(AbstractModel):
    """传统型负载均衡的后端服务相关信息

    """

    def __init__(self):
        r"""
        :param _Type: 后端服务的类型，可取值：CVM、ENI（即将支持）
        :type Type: str
        :param _InstanceId: 后端服务的唯一 ID，可通过 DescribeInstances 接口返回字段中的 unInstanceId 字段获取
        :type InstanceId: str
        :param _Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param _PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param _PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param _InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _RunFlag: 后端服务的状态
1：故障，2：运行中，3：创建中，4：已关机，5：已退还，6：退还中， 7：重启中，8：开机中，9：关机中，10：密码重置中，11：格式化中，12：镜像制作中，13：带宽设置中，14：重装系统中，19：升级中，21：热迁移中
注意：此字段可能返回 null，表示取不到有效值。
        :type RunFlag: int
        """
        self._Type = None
        self._InstanceId = None
        self._Weight = None
        self._PublicIpAddresses = None
        self._PrivateIpAddresses = None
        self._InstanceName = None
        self._RunFlag = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RunFlag(self):
        return self._RunFlag

    @RunFlag.setter
    def RunFlag(self, RunFlag):
        self._RunFlag = RunFlag


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._InstanceName = params.get("InstanceName")
        self._RunFlag = params.get("RunFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalTargetInfo(AbstractModel):
    """传统型负载均衡的后端信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 后端实例ID
        :type InstanceId: str
        :param _Weight: 权重，取值范围 [0, 100]
        :type Weight: int
        """
        self._InstanceId = None
        self._Weight = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneLoadBalancerRequest(AbstractModel):
    """CloneLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡ID。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 克隆出负载均衡实例的名称，规则：1-60 个英文、汉字、数字、连接线“-”或下划线“_”。
注意：如果名称与系统中已有负载均衡实例的名称相同，则系统将会自动生成此次创建的负载均衡实例的名称。
        :type LoadBalancerName: str
        :param _ProjectId: 负载均衡实例所属的项目 ID，可以通过 [DescribeProject](https://cloud.tencent.com/document/product/378/4400) 接口获取。不传此参数则视为默认项目。
        :type ProjectId: int
        :param _MasterZoneId: 仅适用于公网负载均衡。设置跨可用区容灾时的主可用区ID，例如 100001 或 ap-guangzhou-1
注：主可用区是需要承载流量的可用区，备可用区默认不承载流量，主可用区不可用时才使用备可用区，平台将为您自动选择最佳备可用区。可通过 [DescribeResources](https://cloud.tencent.com/document/api/214/70213) 接口查询一个地域的主可用区的列表。
        :type MasterZoneId: str
        :param _SlaveZoneId: 仅适用于公网负载均衡。设置跨可用区容灾时的备可用区ID，例如 100001 或 ap-guangzhou-1
注：备可用区是主可用区故障后，需要承载流量的可用区。可通过 [DescribeResources](https://cloud.tencent.com/document/api/214/70213) 接口查询一个地域的主/备可用区的列表。
        :type SlaveZoneId: str
        :param _ZoneId: 仅适用于公网负载均衡。可用区ID，指定可用区以创建负载均衡实例。如：ap-guangzhou-1。
        :type ZoneId: str
        :param _InternetAccessible: 仅适用于公网负载均衡。负载均衡的网络计费模式。
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _VipIsp: 仅适用于公网负载均衡。目前仅广州、上海、南京、济南、杭州、福州、北京、石家庄、武汉、长沙、成都、重庆地域支持静态单线 IP 线路类型，如需体验，请联系商务经理申请。申请通过后，即可选择中国移动（CMCC）、中国联通（CUCC）或中国电信（CTCC）的运营商类型，网络计费模式只能使用按带宽包计费(BANDWIDTH_PACKAGE)。 如果不指定本参数，则默认使用BGP。可通过 DescribeResources 接口查询一个地域所支持的Isp。
示例值：CMCC
        :type VipIsp: str
        :param _Vip: 指定Vip申请负载均衡。
        :type Vip: str
        :param _Tags: 购买负载均衡同时，给负载均衡打上标签。
        :type Tags: list of TagInfo
        :param _ExclusiveCluster: 独占集群信息。
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param _BandwidthPackageId: 带宽包ID，指定此参数时，网络计费方式（InternetAccessible.InternetChargeType）只支持按带宽包计费（BANDWIDTH_PACKAGE）。
        :type BandwidthPackageId: str
        :param _SnatPro: 是否支持绑定跨地域/跨Vpc绑定IP的功能。
        :type SnatPro: bool
        :param _SnatIps: 开启绑定跨地域/跨Vpc绑定IP的功能后，创建SnatIp。
        :type SnatIps: list of SnatIp
        :param _ClusterIds: 公网独占集群ID或者CDCId。
        :type ClusterIds: list of str
        :param _SlaType: 性能容量型规格。
        :type SlaType: str
        :param _ClusterTag: Stgw独占集群的标签。
        :type ClusterTag: str
        :param _Zones: 仅适用于私有网络内网负载均衡。内网就近接入时，选择可用区下发。
        :type Zones: list of str
        :param _EipAddressId: EIP 的唯一 ID，形如：eip-11112222，仅适用于内网负载均衡绑定EIP。
        :type EipAddressId: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._ProjectId = None
        self._MasterZoneId = None
        self._SlaveZoneId = None
        self._ZoneId = None
        self._InternetAccessible = None
        self._VipIsp = None
        self._Vip = None
        self._Tags = None
        self._ExclusiveCluster = None
        self._BandwidthPackageId = None
        self._SnatPro = None
        self._SnatIps = None
        self._ClusterIds = None
        self._SlaType = None
        self._ClusterTag = None
        self._Zones = None
        self._EipAddressId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def MasterZoneId(self):
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def SlaveZoneId(self):
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VipIsp(self):
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ExclusiveCluster(self):
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def SnatPro(self):
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def ClusterTag(self):
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def EipAddressId(self):
        return self._EipAddressId

    @EipAddressId.setter
    def EipAddressId(self, EipAddressId):
        self._EipAddressId = EipAddressId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._ProjectId = params.get("ProjectId")
        self._MasterZoneId = params.get("MasterZoneId")
        self._SlaveZoneId = params.get("SlaveZoneId")
        self._ZoneId = params.get("ZoneId")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._VipIsp = params.get("VipIsp")
        self._Vip = params.get("Vip")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ExclusiveCluster") is not None:
            self._ExclusiveCluster = ExclusiveCluster()
            self._ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        self._SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self._SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self._SnatIps.append(obj)
        self._ClusterIds = params.get("ClusterIds")
        self._SlaType = params.get("SlaType")
        self._ClusterTag = params.get("ClusterTag")
        self._Zones = params.get("Zones")
        self._EipAddressId = params.get("EipAddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneLoadBalancerResponse(AbstractModel):
    """CloneLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """集群的详细信息，如集群ID，名称，类型，可用区，标签等

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群唯一ID
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _ClusterType: 集群类型，如TGW，STGW，VPCGW
        :type ClusterType: str
        :param _ClusterTag: 集群标签，只有STGW集群有标签
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterTag: str
        :param _Zone: 集群所在可用区，如ap-guangzhou-1
        :type Zone: str
        :param _Network: 集群网络类型，如Public，Private
        :type Network: str
        :param _MaxConn: 最大连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConn: int
        :param _MaxInFlow: 最大入带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxInFlow: int
        :param _MaxInPkg: 最大入包量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxInPkg: int
        :param _MaxOutFlow: 最大出带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxOutFlow: int
        :param _MaxOutPkg: 最大出包量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxOutPkg: int
        :param _MaxNewConn: 最大新建连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNewConn: int
        :param _HTTPMaxNewConn: http最大新建连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPMaxNewConn: int
        :param _HTTPSMaxNewConn: https最大新建连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPSMaxNewConn: int
        :param _HTTPQps: http QPS
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPQps: int
        :param _HTTPSQps: https QPS
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPSQps: int
        :param _ResourceCount: 集群内资源总数目
        :type ResourceCount: int
        :param _IdleResourceCount: 集群内空闲资源数目
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleResourceCount: int
        :param _LoadBalanceDirectorCount: 集群内转发机的数目
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalanceDirectorCount: int
        :param _Isp: 集群的Isp属性，如："BGP","CMCC","CUCC","CTCC","INTERNAL"。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isp: str
        :param _ClustersZone: 集群所在的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ClustersZone: :class:`tencentcloud.clb.v20180317.models.ClustersZone`
        :param _ClustersVersion: 集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ClustersVersion: str
        :param _DisasterRecoveryType: 集群容灾类型，如SINGLE-ZONE，DISASTER-RECOVERY，MUTUAL-DISASTER-RECOVERY
注意：此字段可能返回 null，表示取不到有效值。
        :type DisasterRecoveryType: str
        :param _Egress: 网络出口
注意：此字段可能返回 null，表示取不到有效值。
        :type Egress: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._ClusterType = None
        self._ClusterTag = None
        self._Zone = None
        self._Network = None
        self._MaxConn = None
        self._MaxInFlow = None
        self._MaxInPkg = None
        self._MaxOutFlow = None
        self._MaxOutPkg = None
        self._MaxNewConn = None
        self._HTTPMaxNewConn = None
        self._HTTPSMaxNewConn = None
        self._HTTPQps = None
        self._HTTPSQps = None
        self._ResourceCount = None
        self._IdleResourceCount = None
        self._LoadBalanceDirectorCount = None
        self._Isp = None
        self._ClustersZone = None
        self._ClustersVersion = None
        self._DisasterRecoveryType = None
        self._Egress = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterTag(self):
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Network(self):
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def MaxConn(self):
        return self._MaxConn

    @MaxConn.setter
    def MaxConn(self, MaxConn):
        self._MaxConn = MaxConn

    @property
    def MaxInFlow(self):
        return self._MaxInFlow

    @MaxInFlow.setter
    def MaxInFlow(self, MaxInFlow):
        self._MaxInFlow = MaxInFlow

    @property
    def MaxInPkg(self):
        return self._MaxInPkg

    @MaxInPkg.setter
    def MaxInPkg(self, MaxInPkg):
        self._MaxInPkg = MaxInPkg

    @property
    def MaxOutFlow(self):
        return self._MaxOutFlow

    @MaxOutFlow.setter
    def MaxOutFlow(self, MaxOutFlow):
        self._MaxOutFlow = MaxOutFlow

    @property
    def MaxOutPkg(self):
        return self._MaxOutPkg

    @MaxOutPkg.setter
    def MaxOutPkg(self, MaxOutPkg):
        self._MaxOutPkg = MaxOutPkg

    @property
    def MaxNewConn(self):
        return self._MaxNewConn

    @MaxNewConn.setter
    def MaxNewConn(self, MaxNewConn):
        self._MaxNewConn = MaxNewConn

    @property
    def HTTPMaxNewConn(self):
        return self._HTTPMaxNewConn

    @HTTPMaxNewConn.setter
    def HTTPMaxNewConn(self, HTTPMaxNewConn):
        self._HTTPMaxNewConn = HTTPMaxNewConn

    @property
    def HTTPSMaxNewConn(self):
        return self._HTTPSMaxNewConn

    @HTTPSMaxNewConn.setter
    def HTTPSMaxNewConn(self, HTTPSMaxNewConn):
        self._HTTPSMaxNewConn = HTTPSMaxNewConn

    @property
    def HTTPQps(self):
        return self._HTTPQps

    @HTTPQps.setter
    def HTTPQps(self, HTTPQps):
        self._HTTPQps = HTTPQps

    @property
    def HTTPSQps(self):
        return self._HTTPSQps

    @HTTPSQps.setter
    def HTTPSQps(self, HTTPSQps):
        self._HTTPSQps = HTTPSQps

    @property
    def ResourceCount(self):
        return self._ResourceCount

    @ResourceCount.setter
    def ResourceCount(self, ResourceCount):
        self._ResourceCount = ResourceCount

    @property
    def IdleResourceCount(self):
        return self._IdleResourceCount

    @IdleResourceCount.setter
    def IdleResourceCount(self, IdleResourceCount):
        self._IdleResourceCount = IdleResourceCount

    @property
    def LoadBalanceDirectorCount(self):
        return self._LoadBalanceDirectorCount

    @LoadBalanceDirectorCount.setter
    def LoadBalanceDirectorCount(self, LoadBalanceDirectorCount):
        self._LoadBalanceDirectorCount = LoadBalanceDirectorCount

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def ClustersZone(self):
        return self._ClustersZone

    @ClustersZone.setter
    def ClustersZone(self, ClustersZone):
        self._ClustersZone = ClustersZone

    @property
    def ClustersVersion(self):
        return self._ClustersVersion

    @ClustersVersion.setter
    def ClustersVersion(self, ClustersVersion):
        self._ClustersVersion = ClustersVersion

    @property
    def DisasterRecoveryType(self):
        return self._DisasterRecoveryType

    @DisasterRecoveryType.setter
    def DisasterRecoveryType(self, DisasterRecoveryType):
        self._DisasterRecoveryType = DisasterRecoveryType

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._ClusterType = params.get("ClusterType")
        self._ClusterTag = params.get("ClusterTag")
        self._Zone = params.get("Zone")
        self._Network = params.get("Network")
        self._MaxConn = params.get("MaxConn")
        self._MaxInFlow = params.get("MaxInFlow")
        self._MaxInPkg = params.get("MaxInPkg")
        self._MaxOutFlow = params.get("MaxOutFlow")
        self._MaxOutPkg = params.get("MaxOutPkg")
        self._MaxNewConn = params.get("MaxNewConn")
        self._HTTPMaxNewConn = params.get("HTTPMaxNewConn")
        self._HTTPSMaxNewConn = params.get("HTTPSMaxNewConn")
        self._HTTPQps = params.get("HTTPQps")
        self._HTTPSQps = params.get("HTTPSQps")
        self._ResourceCount = params.get("ResourceCount")
        self._IdleResourceCount = params.get("IdleResourceCount")
        self._LoadBalanceDirectorCount = params.get("LoadBalanceDirectorCount")
        self._Isp = params.get("Isp")
        if params.get("ClustersZone") is not None:
            self._ClustersZone = ClustersZone()
            self._ClustersZone._deserialize(params.get("ClustersZone"))
        self._ClustersVersion = params.get("ClustersVersion")
        self._DisasterRecoveryType = params.get("DisasterRecoveryType")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterItem(AbstractModel):
    """独占集群信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群唯一ID
        :type ClusterId: str
        :param _ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _Zone: 集群所在可用区，如ap-guangzhou-1
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Zone = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterResource(AbstractModel):
    """集群内资源类型

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群唯一ID，如tgw-12345678。
        :type ClusterId: str
        :param _Vip: ip地址。
        :type Vip: str
        :param _LoadBalancerId: 负载均衡唯一ID，如lb-12345678。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerId: str
        :param _Idle: 资源是否闲置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Idle: str
        :param _ClusterName: 集群名称。
        :type ClusterName: str
        :param _Isp: 集群的Isp属性，如："BGP","CMCC","CUCC","CTCC","INTERNAL"。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isp: str
        :param _ClustersZone: 集群所在的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ClustersZone: :class:`tencentcloud.clb.v20180317.models.ClustersZone`
        """
        self._ClusterId = None
        self._Vip = None
        self._LoadBalancerId = None
        self._Idle = None
        self._ClusterName = None
        self._Isp = None
        self._ClustersZone = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Idle(self):
        return self._Idle

    @Idle.setter
    def Idle(self, Idle):
        self._Idle = Idle

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def ClustersZone(self):
        return self._ClustersZone

    @ClustersZone.setter
    def ClustersZone(self, ClustersZone):
        self._ClustersZone = ClustersZone


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Vip = params.get("Vip")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Idle = params.get("Idle")
        self._ClusterName = params.get("ClusterName")
        self._Isp = params.get("Isp")
        if params.get("ClustersZone") is not None:
            self._ClustersZone = ClustersZone()
            self._ClustersZone._deserialize(params.get("ClustersZone"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClustersZone(AbstractModel):
    """集群所在的可用区。

    """

    def __init__(self):
        r"""
        :param _MasterZone: 集群所在的主可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: list of str
        :param _SlaveZone: 集群所在的备可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZone: list of str
        """
        self._MasterZone = None
        self._SlaveZone = None

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone


    def _deserialize(self, params):
        self._MasterZone = params.get("MasterZone")
        self._SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigListItem(AbstractModel):
    """配置内容

    """

    def __init__(self):
        r"""
        :param _UconfigId: 配置ID
        :type UconfigId: str
        :param _ConfigType: 配置类型
        :type ConfigType: str
        :param _ConfigName: 配置名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param _ConfigContent: 配置内容
        :type ConfigContent: str
        :param _CreateTimestamp: 增加配置时间
        :type CreateTimestamp: str
        :param _UpdateTimestamp: 修改配置时间
        :type UpdateTimestamp: str
        """
        self._UconfigId = None
        self._ConfigType = None
        self._ConfigName = None
        self._ConfigContent = None
        self._CreateTimestamp = None
        self._UpdateTimestamp = None

    @property
    def UconfigId(self):
        return self._UconfigId

    @UconfigId.setter
    def UconfigId(self, UconfigId):
        self._UconfigId = UconfigId

    @property
    def ConfigType(self):
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

    @property
    def ConfigName(self):
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def ConfigContent(self):
        return self._ConfigContent

    @ConfigContent.setter
    def ConfigContent(self, ConfigContent):
        self._ConfigContent = ConfigContent

    @property
    def CreateTimestamp(self):
        return self._CreateTimestamp

    @CreateTimestamp.setter
    def CreateTimestamp(self, CreateTimestamp):
        self._CreateTimestamp = CreateTimestamp

    @property
    def UpdateTimestamp(self):
        return self._UpdateTimestamp

    @UpdateTimestamp.setter
    def UpdateTimestamp(self, UpdateTimestamp):
        self._UpdateTimestamp = UpdateTimestamp


    def _deserialize(self, params):
        self._UconfigId = params.get("UconfigId")
        self._ConfigType = params.get("ConfigType")
        self._ConfigName = params.get("ConfigName")
        self._ConfigContent = params.get("ConfigContent")
        self._CreateTimestamp = params.get("CreateTimestamp")
        self._UpdateTimestamp = params.get("UpdateTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogSetRequest(AbstractModel):
    """CreateClsLogSet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetName: 日志集的名字，不能和cls其他日志集重名。不填默认为clb_logset。
        :type LogsetName: str
        :param _Period: 日志集的保存周期，单位：天。
        :type Period: int
        :param _LogsetType: 日志集类型，ACCESS：访问日志，HEALTH：健康检查日志，默认ACCESS。
        :type LogsetType: str
        """
        self._LogsetName = None
        self._Period = None
        self._LogsetType = None

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def LogsetType(self):
        return self._LogsetType

    @LogsetType.setter
    def LogsetType(self, LogsetType):
        self._LogsetType = LogsetType


    def _deserialize(self, params):
        self._LogsetName = params.get("LogsetName")
        self._Period = params.get("Period")
        self._LogsetType = params.get("LogsetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogSetResponse(AbstractModel):
    """CreateClsLogSet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集的 ID。
        :type LogsetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogsetId = None
        self._RequestId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    """CreateListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _Ports: 要将监听器创建到哪些端口，每个端口对应一个新的监听器。
        :type Ports: list of int
        :param _Protocol: 监听器协议： TCP | UDP | HTTP | HTTPS | TCP_SSL | QUIC。
        :type Protocol: str
        :param _ListenerNames: 要创建的监听器名称列表，名称与Ports数组按序一一对应，如不需立即命名，则无需提供此参数。
        :type ListenerNames: list of str
        :param _HealthCheck: 健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL/QUIC监听器。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Certificate: 证书相关信息，此参数仅适用于TCP_SSL监听器和未开启SNI特性的HTTPS监听器。此参数和MultiCertInfo不能同时传入。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param _SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :type SessionExpireTime: int
        :param _Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。此参数仅适用于TCP/UDP/TCP_SSL/QUIC监听器。
        :type Scheduler: str
        :param _SniSwitch: 是否开启SNI特性，此参数仅适用于HTTPS监听器。
        :type SniSwitch: int
        :param _TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组。
        :type TargetType: str
        :param _SessionType: 会话保持类型。不传或传NORMAL表示默认会话保持类型。QUIC_CID 表示根据Quic Connection ID做会话保持。QUIC_CID只支持UDP协议。
        :type SessionType: str
        :param _KeepaliveEnable: 是否开启长连接，此参数仅适用于HTTP/HTTPS监听器，0:关闭；1:开启， 默认关闭。
        :type KeepaliveEnable: int
        :param _EndPort: 创建端口段监听器时必须传入此参数，用以标识结束端口。同时，入参Ports只允许传入一个成员，用以标识开始端口。【如果您需要体验端口段功能，请通过 [工单申请](https://console.cloud.tencent.com/workorder/category)】。
        :type EndPort: int
        :param _DeregisterTargetRst: 解绑后端目标时，是否发RST给客户端，此参数仅适用于TCP监听器。
        :type DeregisterTargetRst: bool
        :param _MultiCertInfo: 证书信息，支持同时传入不同算法类型的多本服务端证书；此参数仅适用于未开启SNI特性的HTTPS监听器。此参数和Certificate不能同时传入。
        :type MultiCertInfo: :class:`tencentcloud.clb.v20180317.models.MultiCertInfo`
        :param _MaxConn: 监听器最大连接数，只有TCP/UDP/TCP_SSL/QUIC监听器支持，不传或者传-1表示监听器维度不限速。
        :type MaxConn: int
        :param _MaxCps: 监听器最大新增连接数，只有TCP/UDP/TCP_SSL/QUIC监听器支持，不传或者传-1表示监听器维度不限速。
        :type MaxCps: int
        :param _IdleConnectTimeout: 空闲连接超时时间，此参数仅适用于TCP监听器，单位：秒。默认值：900，取值范围：共享型实例和独占型实例支持：300～900，性能容量型实例支持：300~2000。如需设置超过2000s，请通过 [工单申请](https://console.cloud.tencent.com/workorder/category),最大可设置到3600s。
        :type IdleConnectTimeout: int
        """
        self._LoadBalancerId = None
        self._Ports = None
        self._Protocol = None
        self._ListenerNames = None
        self._HealthCheck = None
        self._Certificate = None
        self._SessionExpireTime = None
        self._Scheduler = None
        self._SniSwitch = None
        self._TargetType = None
        self._SessionType = None
        self._KeepaliveEnable = None
        self._EndPort = None
        self._DeregisterTargetRst = None
        self._MultiCertInfo = None
        self._MaxConn = None
        self._MaxCps = None
        self._IdleConnectTimeout = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerNames(self):
        return self._ListenerNames

    @ListenerNames.setter
    def ListenerNames(self, ListenerNames):
        self._ListenerNames = ListenerNames

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def SessionType(self):
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def KeepaliveEnable(self):
        return self._KeepaliveEnable

    @KeepaliveEnable.setter
    def KeepaliveEnable(self, KeepaliveEnable):
        self._KeepaliveEnable = KeepaliveEnable

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort

    @property
    def DeregisterTargetRst(self):
        return self._DeregisterTargetRst

    @DeregisterTargetRst.setter
    def DeregisterTargetRst(self, DeregisterTargetRst):
        self._DeregisterTargetRst = DeregisterTargetRst

    @property
    def MultiCertInfo(self):
        return self._MultiCertInfo

    @MultiCertInfo.setter
    def MultiCertInfo(self, MultiCertInfo):
        self._MultiCertInfo = MultiCertInfo

    @property
    def MaxConn(self):
        return self._MaxConn

    @MaxConn.setter
    def MaxConn(self, MaxConn):
        self._MaxConn = MaxConn

    @property
    def MaxCps(self):
        return self._MaxCps

    @MaxCps.setter
    def MaxCps(self, MaxCps):
        self._MaxCps = MaxCps

    @property
    def IdleConnectTimeout(self):
        return self._IdleConnectTimeout

    @IdleConnectTimeout.setter
    def IdleConnectTimeout(self, IdleConnectTimeout):
        self._IdleConnectTimeout = IdleConnectTimeout


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Ports = params.get("Ports")
        self._Protocol = params.get("Protocol")
        self._ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._Scheduler = params.get("Scheduler")
        self._SniSwitch = params.get("SniSwitch")
        self._TargetType = params.get("TargetType")
        self._SessionType = params.get("SessionType")
        self._KeepaliveEnable = params.get("KeepaliveEnable")
        self._EndPort = params.get("EndPort")
        self._DeregisterTargetRst = params.get("DeregisterTargetRst")
        if params.get("MultiCertInfo") is not None:
            self._MultiCertInfo = MultiCertInfo()
            self._MultiCertInfo._deserialize(params.get("MultiCertInfo"))
        self._MaxConn = params.get("MaxConn")
        self._MaxCps = params.get("MaxCps")
        self._IdleConnectTimeout = params.get("IdleConnectTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    """CreateListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerIds: 创建的监听器的唯一标识数组。
        :type ListenerIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerIds = None
        self._RequestId = None

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListenerIds = params.get("ListenerIds")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
        :type LoadBalancerType: str
        :param _Forward: 负载均衡实例的类型。1：通用的负载均衡实例，目前只支持传入1。
        :type Forward: int
        :param _LoadBalancerName: 负载均衡实例的名称，只在创建一个实例的时候才会生效。规则：1-60 个英文、汉字、数字、连接线“-”或下划线“_”。
注意：如果名称与系统中已有负载均衡实例的名称相同，则系统将会自动生成此次创建的负载均衡实例的名称。
        :type LoadBalancerName: str
        :param _VpcId: 负载均衡后端目标设备所属的网络 ID，如vpc-12345678，可以通过 [DescribeVpcEx](https://cloud.tencent.com/document/product/215/1372) 接口获取。 不填此参数则默认为DefaultVPC。创建内网负载均衡实例时，此参数必填。
        :type VpcId: str
        :param _SubnetId: 在私有网络内购买内网负载均衡实例的情况下，必须指定子网 ID，内网负载均衡实例的 VIP 将从这个子网中产生。创建内网负载均衡实例时，此参数必填。
        :type SubnetId: str
        :param _ProjectId: 负载均衡实例所属的项目 ID，可以通过 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 接口获取。不填此参数则视为默认项目。
        :type ProjectId: int
        :param _AddressIPVersion: 仅适用于公网负载均衡。IP版本，可取值：IPV4、IPV6、IPv6FullChain，不区分大小写，默认值 IPV4。说明：取值为IPV6表示为IPV6 NAT64版本；取值为IPv6FullChain，表示为IPv6版本。
        :type AddressIPVersion: str
        :param _Number: 创建负载均衡的个数，默认值 1。
        :type Number: int
        :param _MasterZoneId: 仅适用于公网负载均衡。设置跨可用区容灾时的主可用区ID，例如 100001 或 ap-guangzhou-1
注：主可用区是需要承载流量的可用区，备可用区默认不承载流量，主可用区不可用时才使用备可用区。目前仅广州、上海、南京、北京、成都、深圳金融、中国香港、首尔、法兰克福、新加坡地域的 IPv4 版本的 CLB 支持主备可用区。可通过 [DescribeResources](https://cloud.tencent.com/document/api/214/70213) 接口查询一个地域的主可用区的列表。
        :type MasterZoneId: str
        :param _ZoneId: 仅适用于公网负载均衡。可用区ID，指定可用区以创建负载均衡实例。如：ap-guangzhou-1。
        :type ZoneId: str
        :param _InternetAccessible: 仅对内网属性的性能容量型实例和公网属性的所有实例生效。
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _VipIsp: 仅适用于公网负载均衡。目前仅广州、上海、南京、济南、杭州、福州、北京、石家庄、武汉、长沙、成都、重庆地域支持静态单线 IP 线路类型，如需体验，请联系商务经理申请。申请通过后，即可选择中国移动（CMCC）、中国联通（CUCC）或中国电信（CTCC）的运营商类型，网络计费模式只能使用按带宽包计费(BANDWIDTH_PACKAGE)。 如果不指定本参数，则默认使用BGP。可通过 [DescribeResources](https://cloud.tencent.com/document/api/214/70213)  接口查询一个地域所支持的Isp。
        :type VipIsp: str
        :param _Tags: 购买负载均衡的同时，给负载均衡打上标签，最大支持20个标签键值对。
        :type Tags: list of TagInfo
        :param _Vip: 指定VIP申请负载均衡。此参数选填，不填写此参数时自动分配VIP。IPv4和IPv6类型支持此参数，IPv6 NAT64类型不支持。
注意：当指定VIP创建内网实例、或公网IPv6 BGP实例时，若VIP不属于指定VPC子网的网段内时，会创建失败；若VIP已被占用，也会创建失败。
        :type Vip: str
        :param _BandwidthPackageId: 带宽包ID，指定此参数时，网络计费方式（InternetAccessible.InternetChargeType）只支持按带宽包计费（BANDWIDTH_PACKAGE）。非上移用户购买的 IPv6 负载均衡实例，且运营商类型非 BGP 时 ，不支持指定具体带宽包id。
        :type BandwidthPackageId: str
        :param _ExclusiveCluster: 独占型实例信息。若创建独占型的内网负载均衡实例，则此参数必填。
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param _SlaType: 性能容量型规格。
<ul><li>若需要创建性能容量型实例，则此参数必填，取值范围：<ul><li> SLA：超强型4规格 </li><li> clb.c2.medium：标准型规格 </li><li> clb.c3.small：高阶型1规格 </li><li> clb.c3.medium：高阶型2规格 </li><li> clb.c4.small：超强型1规格 </li><li> clb.c4.medium：超强型2规格 </li><li> clb.c4.large：超强型3规格 </li><li> clb.c4.xlarge：超强型4规格 </li></ul></li><li>若需要创建共享型实例，则无需填写此参数。</li></ul>如需了解规格详情，请参见[实例规格对比](https://cloud.tencent.com/document/product/214/84689)。
        :type SlaType: str
        :param _ClusterIds: 集群ID，集群标识，在需要配置公有云独占集群或本地专有集群时使用。公有云独占集群申请请[提交工单](https://console.cloud.tencent.com/workorder/category)，本地专有集群请参考[本地专有集群](https://cloud.tencent.com/document/product/1346)描述。
        :type ClusterIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _SnatPro: 是否支持绑定跨地域/跨Vpc绑定IP的功能。
        :type SnatPro: bool
        :param _SnatIps: 开启绑定跨地域/跨Vpc绑定IP的功能后，创建SnatIp。
        :type SnatIps: list of SnatIp
        :param _ClusterTag: Stgw独占集群的标签。
        :type ClusterTag: str
        :param _SlaveZoneId: 仅适用于公网负载均衡。设置跨可用区容灾时的备可用区ID，例如 100001 或 ap-guangzhou-1
注：备可用区是主可用区故障后，需要承载流量的可用区。可通过 [DescribeResources](https://cloud.tencent.com/document/api/214/70213) 接口查询一个地域的主/备可用区的列表。
        :type SlaveZoneId: str
        :param _EipAddressId: EIP 的唯一 ID，形如：eip-11112222，仅适用于内网负载均衡绑定EIP。
        :type EipAddressId: str
        :param _LoadBalancerPassToTarget: Target是否放通来自CLB的流量。开启放通（true）：只验证CLB上的安全组；不开启放通（false）：需同时验证CLB和后端实例上的安全组。
        :type LoadBalancerPassToTarget: bool
        :param _DynamicVip: 创建域名化负载均衡。
        :type DynamicVip: bool
        :param _Egress: 网络出口
        :type Egress: str
        """
        self._LoadBalancerType = None
        self._Forward = None
        self._LoadBalancerName = None
        self._VpcId = None
        self._SubnetId = None
        self._ProjectId = None
        self._AddressIPVersion = None
        self._Number = None
        self._MasterZoneId = None
        self._ZoneId = None
        self._InternetAccessible = None
        self._VipIsp = None
        self._Tags = None
        self._Vip = None
        self._BandwidthPackageId = None
        self._ExclusiveCluster = None
        self._SlaType = None
        self._ClusterIds = None
        self._ClientToken = None
        self._SnatPro = None
        self._SnatIps = None
        self._ClusterTag = None
        self._SlaveZoneId = None
        self._EipAddressId = None
        self._LoadBalancerPassToTarget = None
        self._DynamicVip = None
        self._Egress = None

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def MasterZoneId(self):
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VipIsp(self):
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def ExclusiveCluster(self):
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def SnatPro(self):
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def ClusterTag(self):
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def SlaveZoneId(self):
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId

    @property
    def EipAddressId(self):
        return self._EipAddressId

    @EipAddressId.setter
    def EipAddressId(self, EipAddressId):
        self._EipAddressId = EipAddressId

    @property
    def LoadBalancerPassToTarget(self):
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def DynamicVip(self):
        return self._DynamicVip

    @DynamicVip.setter
    def DynamicVip(self, DynamicVip):
        self._DynamicVip = DynamicVip

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Forward = params.get("Forward")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._Number = params.get("Number")
        self._MasterZoneId = params.get("MasterZoneId")
        self._ZoneId = params.get("ZoneId")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._VipIsp = params.get("VipIsp")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Vip = params.get("Vip")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        if params.get("ExclusiveCluster") is not None:
            self._ExclusiveCluster = ExclusiveCluster()
            self._ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self._SlaType = params.get("SlaType")
        self._ClusterIds = params.get("ClusterIds")
        self._ClientToken = params.get("ClientToken")
        self._SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self._SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self._SnatIps.append(obj)
        self._ClusterTag = params.get("ClusterTag")
        self._SlaveZoneId = params.get("SlaveZoneId")
        self._EipAddressId = params.get("EipAddressId")
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self._DynamicVip = params.get("DynamicVip")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 由负载均衡实例唯一 ID 组成的数组。
存在某些场景，如创建出现延迟时，此字段可能返回为空；此时可以根据接口返回的RequestId或DealName参数，通过DescribeTaskStatus接口查询创建的资源ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerIds: list of str
        :param _DealName: 订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerIds = None
        self._DealName = None
        self._RequestId = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancerSnatIpsRequest(AbstractModel):
    """CreateLoadBalancerSnatIps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡唯一性ID，例如：lb-12345678。
        :type LoadBalancerId: str
        :param _SnatIps: 添加的SnatIp信息，可指定IP申请，或者指定子网自动申请。单个CLB实例可申请的默认上限为10个。
        :type SnatIps: list of SnatIp
        :param _Number: 添加的SnatIp的个数，可与SnatIps一起使用，但若指定IP时，则不能指定创建的SnatIp个数。默认值为1，数量上限与用户配置有关，默认上限为10。
        :type Number: int
        """
        self._LoadBalancerId = None
        self._SnatIps = None
        self._Number = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SnatIps(self):
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("SnatIps") is not None:
            self._SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self._SnatIps.append(obj)
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerSnatIpsResponse(AbstractModel):
    """CreateLoadBalancerSnatIps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ListenerId: 监听器 ID。
        :type ListenerId: str
        :param _Rules: 新建转发规则的信息。
        :type Rules: list of RuleInput
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Rules = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInput()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LocationIds: 创建的转发规则的唯一标识数组。
        :type LocationIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LocationIds = None
        self._RequestId = None

    @property
    def LocationIds(self):
        return self._LocationIds

    @LocationIds.setter
    def LocationIds(self, LocationIds):
        self._LocationIds = LocationIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LocationIds = params.get("LocationIds")
        self._RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    """CreateTargetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupName: 目标组名称，限定50个字符
        :type TargetGroupName: str
        :param _VpcId: 目标组的vpcid属性，不填则使用默认vpc
        :type VpcId: str
        :param _Port: 目标组的默认端口， 后续添加服务器时可使用该默认端口
        :type Port: int
        :param _TargetGroupInstances: 目标组绑定的后端服务器
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupName = None
        self._VpcId = None
        self._Port = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupName = params.get("TargetGroupName")
        self._VpcId = params.get("VpcId")
        self._Port = params.get("Port")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetGroupResponse(AbstractModel):
    """CreateTargetGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 创建目标组后生成的id
        :type TargetGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TargetGroupId = None
        self._RequestId = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 日志主题的名称。
        :type TopicName: str
        :param _PartitionCount: 主题分区Partition的数量，不传参默认创建1个，最大创建允许10个，分裂/合并操作会改变分区数量，整体上限50个。
        :type PartitionCount: int
        :param _TopicType: 日志类型，ACCESS：访问日志，HEALTH：健康检查日志，默认ACCESS。
        :type TopicType: str
        :param _Period: 日志集的保存周期，单位：天，默认30天。
        :type Period: int
        :param _StorageType: 日志主题的存储类型，可选值 HOT（标准存储），COLD（低频存储）；默认为HOT。
        :type StorageType: str
        """
        self._TopicName = None
        self._PartitionCount = None
        self._TopicType = None
        self._Period = None
        self._StorageType = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionCount(self):
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._PartitionCount = params.get("PartitionCount")
        self._TopicType = params.get("TopicType")
        self._Period = params.get("Period")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题的 ID。
        :type TopicId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class CrossTargets(AbstractModel):
    """跨域2.0云联网下子机和网卡信息

    """

    def __init__(self):
        r"""
        :param _LocalVpcId: 本地私有网络ID，即负载均衡的VpcId。
        :type LocalVpcId: str
        :param _VpcId: 子机或网卡所属的私有网络ID。
        :type VpcId: str
        :param _IP: 子机或网卡的IP地址
        :type IP: str
        :param _VpcName: 子机或网卡所属的私有网络名称。
        :type VpcName: str
        :param _EniId: 子机的网卡ID。
        :type EniId: str
        :param _InstanceId: 子机实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 子机实例名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Region: 子机或者网卡所属的地域。
        :type Region: str
        """
        self._LocalVpcId = None
        self._VpcId = None
        self._IP = None
        self._VpcName = None
        self._EniId = None
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None

    @property
    def LocalVpcId(self):
        return self._LocalVpcId

    @LocalVpcId.setter
    def LocalVpcId(self, LocalVpcId):
        self._LocalVpcId = LocalVpcId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def EniId(self):
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._LocalVpcId = params.get("LocalVpcId")
        self._VpcId = params.get("VpcId")
        self._IP = params.get("IP")
        self._VpcName = params.get("VpcName")
        self._EniId = params.get("EniId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerRequest(AbstractModel):
    """DeleteListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 要删除的监听器ID。
        :type ListenerId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    """DeleteListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerIds: 指定删除的监听器ID数组，最大为20个。若不填则删除负载均衡的所有监听器。
        :type ListenerIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerIds = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
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
        


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 要删除的负载均衡实例 ID数组，数组大小最大支持20。
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoadBalancerSnatIpsRequest(AbstractModel):
    """DeleteLoadBalancerSnatIps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡唯一ID，例如：lb-12345678。
        :type LoadBalancerId: str
        :param _Ips: 删除SnatIp地址数组。
        :type Ips: list of str
        """
        self._LoadBalancerId = None
        self._Ips = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerSnatIpsResponse(AbstractModel):
    """DeleteLoadBalancerSnatIps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRewriteRequest(AbstractModel):
    """DeleteRewrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _SourceListenerId: 源监听器ID。
        :type SourceListenerId: str
        :param _TargetListenerId: 目标监听器ID。
        :type TargetListenerId: str
        :param _RewriteInfos: 转发规则之间的重定向关系。
        :type RewriteInfos: list of RewriteLocationMap
        """
        self._LoadBalancerId = None
        self._SourceListenerId = None
        self._TargetListenerId = None
        self._RewriteInfos = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SourceListenerId(self):
        return self._SourceListenerId

    @SourceListenerId.setter
    def SourceListenerId(self, SourceListenerId):
        self._SourceListenerId = SourceListenerId

    @property
    def TargetListenerId(self):
        return self._TargetListenerId

    @TargetListenerId.setter
    def TargetListenerId(self, TargetListenerId):
        self._TargetListenerId = TargetListenerId

    @property
    def RewriteInfos(self):
        return self._RewriteInfos

    @RewriteInfos.setter
    def RewriteInfos(self, RewriteInfos):
        self._RewriteInfos = RewriteInfos


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SourceListenerId = params.get("SourceListenerId")
        self._TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self._RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self._RewriteInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRewriteResponse(AbstractModel):
    """DeleteRewrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param _LocationIds: 要删除的转发规则的ID组成的数组。
        :type LocationIds: list of str
        :param _Domain: 要删除的转发规则的域名，如果是多域名，可以指定多域名列表中的任意一个。
        :type Domain: str
        :param _Url: 要删除的转发规则的转发路径。
        :type Url: str
        :param _NewDefaultServerDomain: 监听器下必须配置一个默认域名，当需要删除默认域名时，可以指定另一个域名作为新的默认域名，如果新的默认域名是多域名，可以指定多域名列表中的任意一个。
        :type NewDefaultServerDomain: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationIds = None
        self._Domain = None
        self._Url = None
        self._NewDefaultServerDomain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationIds(self):
        return self._LocationIds

    @LocationIds.setter
    def LocationIds(self, LocationIds):
        self._LocationIds = LocationIds

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def NewDefaultServerDomain(self):
        return self._NewDefaultServerDomain

    @NewDefaultServerDomain.setter
    def NewDefaultServerDomain(self, NewDefaultServerDomain):
        self._NewDefaultServerDomain = NewDefaultServerDomain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationIds = params.get("LocationIds")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._NewDefaultServerDomain = params.get("NewDefaultServerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTargetGroupsRequest(AbstractModel):
    """DeleteTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: 目标组的ID数组。
        :type TargetGroupIds: list of str
        """
        self._TargetGroupIds = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds


    def _deserialize(self, params):
        self._TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetGroupsResponse(AbstractModel):
    """DeleteTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeregisterFunctionTargetsRequest(AbstractModel):
    """DeregisterFunctionTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器 ID。
        :type ListenerId: str
        :param _FunctionTargets: 待解绑的云函数列表。
        :type FunctionTargets: list of FunctionTarget
        :param _LocationId: 目标转发规则的 ID，当将云函数从七层转发规则上解绑时，必须输入此参数或 Domain+Url 参数。
        :type LocationId: str
        :param _Domain: 目标转发规则的域名，若已经输入 LocationId 参数，则本参数不生效。
        :type Domain: str
        :param _Url: 目标转发规则的 URL，若已经输入 LocationId 参数，则本参数不生效。
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._FunctionTargets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def FunctionTargets(self):
        return self._FunctionTargets

    @FunctionTargets.setter
    def FunctionTargets(self, FunctionTargets):
        self._FunctionTargets = FunctionTargets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("FunctionTargets") is not None:
            self._FunctionTargets = []
            for item in params.get("FunctionTargets"):
                obj = FunctionTarget()
                obj._deserialize(item)
                self._FunctionTargets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterFunctionTargetsResponse(AbstractModel):
    """DeregisterFunctionTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeregisterTargetGroupInstancesRequest(AbstractModel):
    """DeregisterTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        :param _TargetGroupInstances: 待解绑的服务器信息。
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetGroupInstancesResponse(AbstractModel):
    """DeregisterTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeregisterTargetsFromClassicalLBRequest(AbstractModel):
    """DeregisterTargetsFromClassicalLB请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _InstanceIds: 后端服务的实例ID列表。
        :type InstanceIds: list of str
        """
        self._LoadBalancerId = None
        self._InstanceIds = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetsFromClassicalLBResponse(AbstractModel):
    """DeregisterTargetsFromClassicalLB返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeregisterTargetsRequest(AbstractModel):
    """DeregisterTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID，格式如 lb-12345678。
        :type LoadBalancerId: str
        :param _ListenerId: 监听器 ID，格式如 lbl-12345678。
        :type ListenerId: str
        :param _Targets: 要解绑的后端服务列表，数组长度最大支持20。
        :type Targets: list of Target
        :param _LocationId: 转发规则的ID，格式如 loc-12345678，当从七层转发规则解绑机器时，必须提供此参数或Domain+URL两者之一。
        :type LocationId: str
        :param _Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param _Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetsResponse(AbstractModel):
    """DeregisterTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeBlockIPListRequest(AbstractModel):
    """DescribeBlockIPList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _Offset: 数据偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回IP的最大个数，默认为 100000。
        :type Limit: int
        """
        self._LoadBalancerId = None
        self._Offset = None
        self._Limit = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockIPListResponse(AbstractModel):
    """DescribeBlockIPList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BlockedIPCount: 返回的IP的数量
        :type BlockedIPCount: int
        :param _ClientIPField: 获取用户真实IP的字段
        :type ClientIPField: str
        :param _BlockedIPList: 加入了12360黑名单的IP列表
        :type BlockedIPList: list of BlockedIP
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BlockedIPCount = None
        self._ClientIPField = None
        self._BlockedIPList = None
        self._RequestId = None

    @property
    def BlockedIPCount(self):
        return self._BlockedIPCount

    @BlockedIPCount.setter
    def BlockedIPCount(self, BlockedIPCount):
        self._BlockedIPCount = BlockedIPCount

    @property
    def ClientIPField(self):
        return self._ClientIPField

    @ClientIPField.setter
    def ClientIPField(self, ClientIPField):
        self._ClientIPField = ClientIPField

    @property
    def BlockedIPList(self):
        return self._BlockedIPList

    @BlockedIPList.setter
    def BlockedIPList(self, BlockedIPList):
        self._BlockedIPList = BlockedIPList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlockedIPCount = params.get("BlockedIPCount")
        self._ClientIPField = params.get("ClientIPField")
        if params.get("BlockedIPList") is not None:
            self._BlockedIPList = []
            for item in params.get("BlockedIPList"):
                obj = BlockedIP()
                obj._deserialize(item)
                self._BlockedIPList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBlockIPTaskRequest(AbstractModel):
    """DescribeBlockIPTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: ModifyBlockIPList 接口返回的异步任务的ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class DescribeBlockIPTaskResponse(AbstractModel):
    """DescribeBlockIPTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 1 running，2 fail，6 succ
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeClassicalLBByInstanceIdRequest(AbstractModel):
    """DescribeClassicalLBByInstanceId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 后端实例ID列表。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBByInstanceIdResponse(AbstractModel):
    """DescribeClassicalLBByInstanceId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerInfoList: 负载均衡相关信息列表。
        :type LoadBalancerInfoList: list of ClassicalLoadBalancerInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerInfoList = None
        self._RequestId = None

    @property
    def LoadBalancerInfoList(self):
        return self._LoadBalancerInfoList

    @LoadBalancerInfoList.setter
    def LoadBalancerInfoList(self, LoadBalancerInfoList):
        self._LoadBalancerInfoList = LoadBalancerInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancerInfoList") is not None:
            self._LoadBalancerInfoList = []
            for item in params.get("LoadBalancerInfoList"):
                obj = ClassicalLoadBalancerInfo()
                obj._deserialize(item)
                self._LoadBalancerInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassicalLBHealthStatusRequest(AbstractModel):
    """DescribeClassicalLBHealthStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBHealthStatusResponse(AbstractModel):
    """DescribeClassicalLBHealthStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthList: 后端健康状态列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthList: list of ClassicalHealth
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthList = None
        self._RequestId = None

    @property
    def HealthList(self):
        return self._HealthList

    @HealthList.setter
    def HealthList(self, HealthList):
        self._HealthList = HealthList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthList") is not None:
            self._HealthList = []
            for item in params.get("HealthList"):
                obj = ClassicalHealth()
                obj._deserialize(item)
                self._HealthList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassicalLBListenersRequest(AbstractModel):
    """DescribeClassicalLBListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerIds: 负载均衡监听器ID列表。
        :type ListenerIds: list of str
        :param _Protocol: 负载均衡监听的协议：'TCP', 'UDP', 'HTTP', 'HTTPS'。
        :type Protocol: str
        :param _ListenerPort: 负载均衡监听端口，范围为[1-65535]。
        :type ListenerPort: int
        :param _Status: 监听器的状态，0：创建中，1：运行中。
        :type Status: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._ListenerPort = None
        self._Status = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerPort(self):
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._ListenerPort = params.get("ListenerPort")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBListenersResponse(AbstractModel):
    """DescribeClassicalLBListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Listeners: 监听器列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ClassicalListener
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Listeners = None
        self._RequestId = None

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ClassicalListener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassicalLBTargetsRequest(AbstractModel):
    """DescribeClassicalLBTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        """
        self._LoadBalancerId = None

    @property
    def LoadBalancerId(self):
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
        


class DescribeClassicalLBTargetsResponse(AbstractModel):
    """DescribeClassicalLBTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Targets: 后端服务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of ClassicalTarget
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Targets = None
        self._RequestId = None

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClsLogSetRequest(AbstractModel):
    """DescribeClsLogSet请求参数结构体

    """


class DescribeClsLogSetResponse(AbstractModel):
    """DescribeClsLogSet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集的 ID。
        :type LogsetId: str
        :param _HealthLogsetId: 健康检查日志集的 ID。
        :type HealthLogsetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogsetId = None
        self._HealthLogsetId = None
        self._RequestId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def HealthLogsetId(self):
        return self._HealthLogsetId

    @HealthLogsetId.setter
    def HealthLogsetId(self, HealthLogsetId):
        self._HealthLogsetId = HealthLogsetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._HealthLogsetId = params.get("HealthLogsetId")
        self._RequestId = params.get("RequestId")


class DescribeClusterResourcesRequest(AbstractModel):
    """DescribeClusterResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回集群中资源列表数目，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 返回集群中资源列表起始偏移量，默认为0。
        :type Offset: int
        :param _Filters: 查询集群中资源列表条件，详细的过滤条件如下：
<li> cluster-id - String - 是否必填：否 - （过滤条件）按照 集群 的唯一ID过滤，如 ："tgw-12345678","stgw-12345678","vpcgw-12345678"。</li>
<li> vip - String - 是否必填：否 - （过滤条件）按照vip过滤。</li>
<li> loadbalancer-id - String - 是否必填：否 - （过滤条件）按照负载均衡唯一ID过滤。</li>
<li> idle - String 是否必填：否 - （过滤条件）按照是否闲置过滤，如"True","False"。</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeClusterResourcesResponse(AbstractModel):
    """DescribeClusterResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterResourceSet: 集群中资源列表。
        :type ClusterResourceSet: list of ClusterResource
        :param _TotalCount: 集群中资源总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterResourceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterResourceSet(self):
        return self._ClusterResourceSet

    @ClusterResourceSet.setter
    def ClusterResourceSet(self, ClusterResourceSet):
        self._ClusterResourceSet = ClusterResourceSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterResourceSet") is not None:
            self._ClusterResourceSet = []
            for item in params.get("ClusterResourceSet"):
                obj = ClusterResource()
                obj._deserialize(item)
                self._ClusterResourceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCrossTargetsRequest(AbstractModel):
    """DescribeCrossTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回后端服务列表数目，默认20，最大值100。
        :type Limit: int
        :param _Offset: 返回后端服务列表起始偏移量，默认0。
        :type Offset: int
        :param _Filters: 查询跨域2.0版本云联网后端子机和网卡服务列表条件，详细的过滤条件如下：
<li> vpc-id - String - 是否必填：否 - （过滤条件）按照 本地私有网络ID，即负载均衡的VpcId 过滤，如："vpc-12345678"。</li>
<li> ip - String - 是否必填：否 - （过滤条件）按照 后端服务ip 过滤，如："192.168.0.1"。</li>
<li> listener-id - String - 是否必填：否 - （过滤条件）按照 监听器ID 过滤，如："lbl-12345678"。</li>
<li> location-id - String - 是否必填：否 - （过滤条件）按照 七层监听器规则ID 过滤，如："loc-12345678"。</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeCrossTargetsResponse(AbstractModel):
    """DescribeCrossTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 后端服务列表总数。
        :type TotalCount: int
        :param _CrossTargetSet: 后端服务列表。
        :type CrossTargetSet: list of CrossTargets
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CrossTargetSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CrossTargetSet(self):
        return self._CrossTargetSet

    @CrossTargetSet.setter
    def CrossTargetSet(self, CrossTargetSet):
        self._CrossTargetSet = CrossTargetSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CrossTargetSet") is not None:
            self._CrossTargetSet = []
            for item in params.get("CrossTargetSet"):
                obj = CrossTargets()
                obj._deserialize(item)
                self._CrossTargetSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomizedConfigAssociateListRequest(AbstractModel):
    """DescribeCustomizedConfigAssociateList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UconfigId: 配置ID
        :type UconfigId: str
        :param _Offset: 拉取绑定关系列表开始位置，默认值 0
        :type Offset: int
        :param _Limit: 拉取绑定关系列表数目，默认值 20
        :type Limit: int
        :param _Domain: 搜索域名
        :type Domain: str
        """
        self._UconfigId = None
        self._Offset = None
        self._Limit = None
        self._Domain = None

    @property
    def UconfigId(self):
        return self._UconfigId

    @UconfigId.setter
    def UconfigId(self, UconfigId):
        self._UconfigId = UconfigId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._UconfigId = params.get("UconfigId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizedConfigAssociateListResponse(AbstractModel):
    """DescribeCustomizedConfigAssociateList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindList: 绑定关系列表
        :type BindList: list of BindDetailItem
        :param _TotalCount: 绑定关系总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BindList(self):
        return self._BindList

    @BindList.setter
    def BindList(self, BindList):
        self._BindList = BindList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BindList") is not None:
            self._BindList = []
            for item in params.get("BindList"):
                obj = BindDetailItem()
                obj._deserialize(item)
                self._BindList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCustomizedConfigListRequest(AbstractModel):
    """DescribeCustomizedConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigType: 配置类型:CLB 负载均衡维度。 SERVER 域名维度。 LOCATION 规则维度。
        :type ConfigType: str
        :param _Offset: 拉取页偏移，默认值0
        :type Offset: int
        :param _Limit: 拉取数目，默认值20
        :type Limit: int
        :param _ConfigName: 拉取指定配置名字，模糊匹配。
        :type ConfigName: str
        :param _UconfigIds: 配置ID
        :type UconfigIds: list of str
        :param _Filters: 过滤条件如下：
<li> loadbalancer-id - String - 是否必填：否 - （过滤条件）按照 负载均衡ID 过滤，如："lb-12345678"。</li>
<li> vip - String - 是否必填：否 - （过滤条件）按照 负载均衡Vip 过滤，如："1.1.1.1","2204::22:3"。</li>
        :type Filters: list of Filter
        """
        self._ConfigType = None
        self._Offset = None
        self._Limit = None
        self._ConfigName = None
        self._UconfigIds = None
        self._Filters = None

    @property
    def ConfigType(self):
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ConfigName(self):
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def UconfigIds(self):
        return self._UconfigIds

    @UconfigIds.setter
    def UconfigIds(self, UconfigIds):
        self._UconfigIds = UconfigIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ConfigType = params.get("ConfigType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ConfigName = params.get("ConfigName")
        self._UconfigIds = params.get("UconfigIds")
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
        


class DescribeCustomizedConfigListResponse(AbstractModel):
    """DescribeCustomizedConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigList: 配置列表
        :type ConfigList: list of ConfigListItem
        :param _TotalCount: 配置数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = ConfigListItem()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeExclusiveClustersRequest(AbstractModel):
    """DescribeExclusiveClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回集群列表数目，默认值为20，最大值为100。
        :type Limit: int
        :param _Offset: 返回集群列表起始偏移量，默认为0。
        :type Offset: int
        :param _Filters: 查询集群列表条件，详细的过滤条件如下：
<li> cluster-type - String - 是否必填：否 - （过滤条件）按照 集群 的类型过滤，包括"TGW","STGW","VPCGW"。</li>
<li> cluster-id - String - 是否必填：否 - （过滤条件）按照 集群 的唯一ID过滤，如 ："tgw-12345678","stgw-12345678","vpcgw-12345678"。</li>
<li> cluster-name - String - 是否必填：否 - （过滤条件）按照 集群 的名称过滤。</li>
<li> cluster-tag - String - 是否必填：否 - （过滤条件）按照 集群 的标签过滤。（只有TGW/STGW集群有集群标签） </li>
<li> vip - String - 是否必填：否 - （过滤条件）按照 集群 内的vip过滤。</li>
<li> loadblancer-id - String - 是否必填：否 - （过滤条件）按照 集群 内的负载均衡唯一ID过滤。</li>
<li> network - String - 是否必填：否 - （过滤条件）按照 集群 的网络类型过滤，如："Public","Private"。</li>
<li> zone - String - 是否必填：否 - （过滤条件）按照 集群 所在可用区过滤，如："ap-guangzhou-1"（广州一区）。</li>
<li> isp -- String - 是否必填：否 - （过滤条件）按照TGW集群的 Isp 类型过滤，如："BGP","CMCC","CUCC","CTCC","INTERNAL"。</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeExclusiveClustersResponse(AbstractModel):
    """DescribeExclusiveClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterSet: 集群列表。
        :type ClusterSet: list of Cluster
        :param _TotalCount: 集群总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterSet(self):
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = Cluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIdleLoadBalancersRequest(AbstractModel):
    """DescribeIdleLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 数据偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回负载均衡实例的数量，默认为20，最大值为100。
        :type Limit: int
        :param _LoadBalancerRegion: 负载均衡所在地域。
        :type LoadBalancerRegion: str
        """
        self._Offset = None
        self._Limit = None
        self._LoadBalancerRegion = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def LoadBalancerRegion(self):
        return self._LoadBalancerRegion

    @LoadBalancerRegion.setter
    def LoadBalancerRegion(self, LoadBalancerRegion):
        self._LoadBalancerRegion = LoadBalancerRegion


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._LoadBalancerRegion = params.get("LoadBalancerRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdleLoadBalancersResponse(AbstractModel):
    """DescribeIdleLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdleLoadBalancers: 闲置实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleLoadBalancers: list of IdleLoadBalancer
        :param _TotalCount: 所有闲置实例数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdleLoadBalancers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def IdleLoadBalancers(self):
        return self._IdleLoadBalancers

    @IdleLoadBalancers.setter
    def IdleLoadBalancers(self, IdleLoadBalancers):
        self._IdleLoadBalancers = IdleLoadBalancers

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IdleLoadBalancers") is not None:
            self._IdleLoadBalancers = []
            for item in params.get("IdleLoadBalancers"):
                obj = IdleLoadBalancer()
                obj._deserialize(item)
                self._IdleLoadBalancers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLBListenersRequest(AbstractModel):
    """DescribeLBListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Backends: 需要查询的内网ip列表
        :type Backends: list of LbRsItem
        """
        self._Backends = None

    @property
    def Backends(self):
        return self._Backends

    @Backends.setter
    def Backends(self, Backends):
        self._Backends = Backends


    def _deserialize(self, params):
        if params.get("Backends") is not None:
            self._Backends = []
            for item in params.get("Backends"):
                obj = LbRsItem()
                obj._deserialize(item)
                self._Backends.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLBListenersResponse(AbstractModel):
    """DescribeLBListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: 绑定的后端规则
        :type LoadBalancers: list of LBItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LBItem()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ListenerIds: 要查询的负载均衡监听器 ID 数组，最大为100个。
        :type ListenerIds: list of str
        :param _Protocol: 要查询的监听器协议类型，取值 TCP | UDP | HTTP | HTTPS | TCP_SSL | QUIC。
        :type Protocol: str
        :param _Port: 要查询的监听器的端口。
        :type Port: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._Port = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Listeners: 监听器列表。
        :type Listeners: list of Listener
        :param _TotalCount: 总的监听器个数（根据端口、协议、监听器ID过滤后）。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Listeners = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerListByCertIdRequest(AbstractModel):
    """DescribeLoadBalancerListByCertId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertIds: 服务端证书的ID，或客户端证书的ID
        :type CertIds: list of str
        """
        self._CertIds = None

    @property
    def CertIds(self):
        return self._CertIds

    @CertIds.setter
    def CertIds(self, CertIds):
        self._CertIds = CertIds


    def _deserialize(self, params):
        self._CertIds = params.get("CertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerListByCertIdResponse(AbstractModel):
    """DescribeLoadBalancerListByCertId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertSet: 证书ID，以及与该证书ID关联的负载均衡实例列表
        :type CertSet: list of CertIdRelatedWithLoadBalancers
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertSet = None
        self._RequestId = None

    @property
    def CertSet(self):
        return self._CertSet

    @CertSet.setter
    def CertSet(self, CertSet):
        self._CertSet = CertSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertSet") is not None:
            self._CertSet = []
            for item in params.get("CertSet"):
                obj = CertIdRelatedWithLoadBalancers()
                obj._deserialize(item)
                self._CertSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerOverviewRequest(AbstractModel):
    """DescribeLoadBalancerOverview请求参数结构体

    """


class DescribeLoadBalancerOverviewResponse(AbstractModel):
    """DescribeLoadBalancerOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 负载均衡总数
        :type TotalCount: int
        :param _RunningCount: 运行中的负载均衡数目
        :type RunningCount: int
        :param _IsolationCount: 隔离中的负载均衡数目
        :type IsolationCount: int
        :param _WillExpireCount: 即将到期的负载均衡数目
        :type WillExpireCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RunningCount = None
        self._IsolationCount = None
        self._WillExpireCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RunningCount(self):
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def IsolationCount(self):
        return self._IsolationCount

    @IsolationCount.setter
    def IsolationCount(self, IsolationCount):
        self._IsolationCount = IsolationCount

    @property
    def WillExpireCount(self):
        return self._WillExpireCount

    @WillExpireCount.setter
    def WillExpireCount(self, WillExpireCount):
        self._WillExpireCount = WillExpireCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._RunningCount = params.get("RunningCount")
        self._IsolationCount = params.get("IsolationCount")
        self._WillExpireCount = params.get("WillExpireCount")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerTrafficRequest(AbstractModel):
    """DescribeLoadBalancerTraffic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerRegion: 负载均衡所在地域，不传默认返回所有地域负载均衡。
        :type LoadBalancerRegion: str
        """
        self._LoadBalancerRegion = None

    @property
    def LoadBalancerRegion(self):
        return self._LoadBalancerRegion

    @LoadBalancerRegion.setter
    def LoadBalancerRegion(self, LoadBalancerRegion):
        self._LoadBalancerRegion = LoadBalancerRegion


    def _deserialize(self, params):
        self._LoadBalancerRegion = params.get("LoadBalancerRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerTrafficResponse(AbstractModel):
    """DescribeLoadBalancerTraffic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerTraffic: 按出带宽从高到低排序后的负载均衡信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerTraffic: list of LoadBalancerTraffic
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerTraffic = None
        self._RequestId = None

    @property
    def LoadBalancerTraffic(self):
        return self._LoadBalancerTraffic

    @LoadBalancerTraffic.setter
    def LoadBalancerTraffic(self, LoadBalancerTraffic):
        self._LoadBalancerTraffic = LoadBalancerTraffic

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancerTraffic") is not None:
            self._LoadBalancerTraffic = []
            for item in params.get("LoadBalancerTraffic"):
                obj = LoadBalancerTraffic()
                obj._deserialize(item)
                self._LoadBalancerTraffic.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersDetailRequest(AbstractModel):
    """DescribeLoadBalancersDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回负载均衡列表数目，默认20，最大值100。
        :type Limit: int
        :param _Offset: 返回负载均衡列表起始偏移量，默认0。
        :type Offset: int
        :param _Fields: 选择返回的Fields列表，系统仅会返回Fileds中填写的字段，可填写的字段详情请参见<a href="https://cloud.tencent.com/document/api/214/30694#LoadBalancerDetail">LoadBalancerDetail</a>。若未在Fileds填写相关字段，则此字段返回null。Fileds中默认添加LoadBalancerId和LoadBalancerName字段。
        :type Fields: list of str
        :param _TargetType: 当Fields包含TargetId、TargetAddress、TargetPort、TargetWeight等Fields时，必选选择导出目标组的Target或者非目标组Target，值范围NODE、GROUP。
        :type TargetType: str
        :param _Filters: 查询负载均衡详细信息列表条件，详细的过滤条件如下：
<li> loadbalancer-id - String - 是否必填：否 - （过滤条件）按照 负载均衡ID 过滤，如："lb-12345678"。</li>
<li> project-id - String - 是否必填：否 - （过滤条件）按照 项目ID 过滤，如："0","123"。</li>
<li> network - String - 是否必填：否 - （过滤条件）按照 负载均衡网络类型 过滤，如："Public","Private"。</li>
<li> vip - String - 是否必填：否 - （过滤条件）按照 负载均衡Vip 过滤，如："1.1.1.1","2204::22:3"。</li>
<li> target-ip - String - 是否必填：否 - （过滤条件）按照 后端目标内网Ip 过滤，如："1.1.1.1","2203::214:4"。</li>
<li> vpcid - String - 是否必填：否 - （过滤条件）按照 负载均衡所属vpcId 过滤，如："vpc-12345678"。</li>
<li> zone - String - 是否必填：否 - （过滤条件）按照 负载均衡所属的可用区 过滤，如："ap-guangzhou-1"。</li>
<li> tag-key - String - 是否必填：否 - （过滤条件）按照 负载均衡标签的标签键 过滤，如："name"。</li>
<li> tag:* - String - 是否必填：否 - （过滤条件）按照 负载均衡的标签 过滤，':' 后面跟的是标签键。如：过滤标签键name，标签值zhangsan,lisi，{"Name": "tag:name","Values": ["zhangsan", "lisi"]}。</li>
<li> fuzzy-search - String - 是否必填：否 - （过滤条件）按照 负载均衡Vip，负载均衡名称 模糊搜索，如："1.1"。</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Fields = None
        self._TargetType = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Fields = params.get("Fields")
        self._TargetType = params.get("TargetType")
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
        


class DescribeLoadBalancersDetailResponse(AbstractModel):
    """DescribeLoadBalancersDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 负载均衡详情列表总数。
        :type TotalCount: int
        :param _LoadBalancerDetailSet: 负载均衡详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerDetailSet: list of LoadBalancerDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerDetailSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerDetailSet(self):
        return self._LoadBalancerDetailSet

    @LoadBalancerDetailSet.setter
    def LoadBalancerDetailSet(self, LoadBalancerDetailSet):
        self._LoadBalancerDetailSet = LoadBalancerDetailSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerDetailSet") is not None:
            self._LoadBalancerDetailSet = []
            for item in params.get("LoadBalancerDetailSet"):
                obj = LoadBalancerDetail()
                obj._deserialize(item)
                self._LoadBalancerDetailSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 负载均衡实例ID。实例ID数量上限为20个。
        :type LoadBalancerIds: list of str
        :param _LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
        :type LoadBalancerType: str
        :param _Forward: 负载均衡实例的类型。1：通用的负载均衡实例，0：传统型负载均衡实例。如果不传此参数，则查询所有类型的负载均衡实例。
        :type Forward: int
        :param _LoadBalancerName: 负载均衡实例的名称。
        :type LoadBalancerName: str
        :param _Domain: 腾讯云为负载均衡实例分配的域名。
        :type Domain: str
        :param _LoadBalancerVips: 负载均衡实例的 VIP 地址，支持多个。
        :type LoadBalancerVips: list of str
        :param _BackendPublicIps: 负载均衡绑定的后端服务的外网 IP，只支持查询云服务器的公网 IP。
        :type BackendPublicIps: list of str
        :param _BackendPrivateIps: 负载均衡绑定的后端服务的内网 IP，只支持查询云服务器的内网 IP。
        :type BackendPrivateIps: list of str
        :param _Offset: 数据偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回负载均衡实例的数量，默认为20，最大值为100。
        :type Limit: int
        :param _OrderBy: 排序参数，支持以下字段：LoadBalancerName，CreateTime，Domain，LoadBalancerType。
        :type OrderBy: str
        :param _OrderType: 1：倒序，0：顺序，默认按照创建时间倒序。
        :type OrderType: int
        :param _SearchKey: 搜索字段，模糊匹配名称、域名、VIP。
        :type SearchKey: str
        :param _ProjectId: 负载均衡实例所属的项目 ID，可以通过 DescribeProject 接口获取。
        :type ProjectId: int
        :param _WithRs: 负载均衡是否绑定后端服务，0：没有绑定后端服务，1：绑定后端服务，-1：查询全部。
        :type WithRs: int
        :param _VpcId: 负载均衡实例所属私有网络唯一ID，如 vpc-bhqkbhdx，
基础网络可传入'0'。
        :type VpcId: str
        :param _SecurityGroup: 安全组ID，如 sg-m1cc****。
        :type SecurityGroup: str
        :param _MasterZone: 主可用区ID，如 ："100001" （对应的是广州一区）。
        :type MasterZone: str
        :param _Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为100。<br/>`Filter.Name`和`Filter.Values`皆为必填项。详细的过滤条件如下：
<li> charge-type - String - 是否必填：否 - （过滤条件）按照 CLB 的实例计费模式过滤，包括"PREPAID","POSTPAID_BY_HOUR"。</li>
<li> internet-charge-type - String - 是否必填：否 - （过滤条件）按照 CLB 的网络计费模式过滤，包括"BANDWIDTH_PREPAID","TRAFFIC_POSTPAID_BY_HOUR","BANDWIDTH_POSTPAID_BY_HOUR","BANDWIDTH_PACKAGE"。</li>
<li> master-zone-id - String - 是否必填：否 - （过滤条件）按照 CLB 的主可用区ID过滤，如 ："100001" （对应的是广州一区）。</li>
<li> tag-key - String - 是否必填：否 - （过滤条件）按照 CLB 标签的键过滤。</li>
<li> tag:tag-key - String - 是否必填：否 - （过滤条件）按照CLB标签键值对进行过滤，tag-key使用具体的标签键进行替换。</li>
<li> function-name - String - 是否必填：否 - （过滤条件）按照 CLB 后端绑定的SCF云函数的函数名称过滤。</li>
<li> function-name - String - 是否必填：否 - （过滤条件）按照 CLB 后端绑定的SCF云函数的函数名称过滤。</li>
<li> vip-isp - String - 是否必填：否 - （过滤条件）按照 CLB VIP的运营商类型过滤，如："BGP","INTERNAL","CMCC","CTCC","CUCC"等。</li>
<li> sla-type - String - 是否必填：否 - （过滤条件）按照 CLB 的性能容量型规格过滤，包括"clb.c2.medium","clb.c3.small","clb.c3.medium","clb.c4.small","clb.c4.medium","clb.c4.large","clb.c4.xlarge"。</li>
        :type Filters: list of Filter
        """
        self._LoadBalancerIds = None
        self._LoadBalancerType = None
        self._Forward = None
        self._LoadBalancerName = None
        self._Domain = None
        self._LoadBalancerVips = None
        self._BackendPublicIps = None
        self._BackendPrivateIps = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderType = None
        self._SearchKey = None
        self._ProjectId = None
        self._WithRs = None
        self._VpcId = None
        self._SecurityGroup = None
        self._MasterZone = None
        self._Filters = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerVips(self):
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def BackendPublicIps(self):
        return self._BackendPublicIps

    @BackendPublicIps.setter
    def BackendPublicIps(self, BackendPublicIps):
        self._BackendPublicIps = BackendPublicIps

    @property
    def BackendPrivateIps(self):
        return self._BackendPrivateIps

    @BackendPrivateIps.setter
    def BackendPrivateIps(self, BackendPrivateIps):
        self._BackendPrivateIps = BackendPrivateIps

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WithRs(self):
        return self._WithRs

    @WithRs.setter
    def WithRs(self, WithRs):
        self._WithRs = WithRs

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Forward = params.get("Forward")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Domain = params.get("Domain")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._BackendPublicIps = params.get("BackendPublicIps")
        self._BackendPrivateIps = params.get("BackendPrivateIps")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._SearchKey = params.get("SearchKey")
        self._ProjectId = params.get("ProjectId")
        self._WithRs = params.get("WithRs")
        self._VpcId = params.get("VpcId")
        self._SecurityGroup = params.get("SecurityGroup")
        self._MasterZone = params.get("MasterZone")
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
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足过滤条件的负载均衡实例总数。此数值与入参中的Limit无关。
        :type TotalCount: int
        :param _LoadBalancerSet: 返回的负载均衡实例数组。
        :type LoadBalancerSet: list of LoadBalancer
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerSet(self):
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQuotaRequest(AbstractModel):
    """DescribeQuota请求参数结构体

    """


class DescribeQuotaResponse(AbstractModel):
    """DescribeQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QuotaSet: 配额列表
        :type QuotaSet: list of Quota
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QuotaSet = None
        self._RequestId = None

    @property
    def QuotaSet(self):
        return self._QuotaSet

    @QuotaSet.setter
    def QuotaSet(self, QuotaSet):
        self._QuotaSet = QuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self._QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self._QuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesRequest(AbstractModel):
    """DescribeResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回可用区资源列表数目，默认20，最大值100。
        :type Limit: int
        :param _Offset: 返回可用区资源列表起始偏移量，默认0。
        :type Offset: int
        :param _Filters: 查询可用区资源列表条件，详细的过滤条件如下：
<li> zone - String - 是否必填：否 - （过滤条件）按照 可用区 过滤，如："ap-guangzhou-1"（广州一区）。</li>
<li> isp -- String - 是否必填：否 - （过滤条件）按照 Isp 类型过滤，如："BGP","CMCC","CUCC","CTCC"。</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeResourcesResponse(AbstractModel):
    """DescribeResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneResourceSet: 可用区支持的资源列表。
        :type ZoneResourceSet: list of ZoneResource
        :param _TotalCount: 可用区资源列表数目。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneResourceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ZoneResourceSet(self):
        return self._ZoneResourceSet

    @ZoneResourceSet.setter
    def ZoneResourceSet(self, ZoneResourceSet):
        self._ZoneResourceSet = ZoneResourceSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneResourceSet") is not None:
            self._ZoneResourceSet = []
            for item in params.get("ZoneResourceSet"):
                obj = ZoneResource()
                obj._deserialize(item)
                self._ZoneResourceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRewriteRequest(AbstractModel):
    """DescribeRewrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _SourceListenerIds: 负载均衡监听器ID数组。
        :type SourceListenerIds: list of str
        :param _SourceLocationIds: 负载均衡转发规则的ID数组。
        :type SourceLocationIds: list of str
        """
        self._LoadBalancerId = None
        self._SourceListenerIds = None
        self._SourceLocationIds = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SourceListenerIds(self):
        return self._SourceListenerIds

    @SourceListenerIds.setter
    def SourceListenerIds(self, SourceListenerIds):
        self._SourceListenerIds = SourceListenerIds

    @property
    def SourceLocationIds(self):
        return self._SourceLocationIds

    @SourceLocationIds.setter
    def SourceLocationIds(self, SourceLocationIds):
        self._SourceLocationIds = SourceLocationIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SourceListenerIds = params.get("SourceListenerIds")
        self._SourceLocationIds = params.get("SourceLocationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRewriteResponse(AbstractModel):
    """DescribeRewrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RewriteSet: 重定向转发规则构成的数组，若无重定向规则，则返回空数组。
        :type RewriteSet: list of RuleOutput
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RewriteSet = None
        self._RequestId = None

    @property
    def RewriteSet(self):
        return self._RewriteSet

    @RewriteSet.setter
    def RewriteSet(self, RewriteSet):
        self._RewriteSet = RewriteSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RewriteSet") is not None:
            self._RewriteSet = []
            for item in params.get("RewriteSet"):
                obj = RuleOutput()
                obj._deserialize(item)
                self._RewriteSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupInstancesRequest(AbstractModel):
    """DescribeTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，当前仅支持TargetGroupId，BindIP，InstanceId过滤。
        :type Filters: list of Filter
        :param _Limit: 显示数量限制，默认20。
        :type Limit: int
        :param _Offset: 显示的偏移量，默认为0。
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupInstancesResponse(AbstractModel):
    """DescribeTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 本次查询的结果数量。
        :type TotalCount: int
        :param _TargetGroupInstanceSet: 绑定的服务器信息。
        :type TargetGroupInstanceSet: list of TargetGroupBackend
        :param _RealCount: 实际统计数量，不受Limit、Offset、CAM的影响。
        :type RealCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupInstanceSet = None
        self._RealCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupInstanceSet(self):
        return self._TargetGroupInstanceSet

    @TargetGroupInstanceSet.setter
    def TargetGroupInstanceSet(self, TargetGroupInstanceSet):
        self._TargetGroupInstanceSet = TargetGroupInstanceSet

    @property
    def RealCount(self):
        return self._RealCount

    @RealCount.setter
    def RealCount(self, RealCount):
        self._RealCount = RealCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupInstanceSet") is not None:
            self._TargetGroupInstanceSet = []
            for item in params.get("TargetGroupInstanceSet"):
                obj = TargetGroupBackend()
                obj._deserialize(item)
                self._TargetGroupInstanceSet.append(obj)
        self._RealCount = params.get("RealCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupListRequest(AbstractModel):
    """DescribeTargetGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: 目标组ID数组。
        :type TargetGroupIds: list of str
        :param _Filters: 过滤条件数组，支持TargetGroupVpcId和TargetGroupName。与TargetGroupIds互斥，优先使用目标组ID。
        :type Filters: list of Filter
        :param _Offset: 显示的偏移起始量。
        :type Offset: int
        :param _Limit: 显示条数限制，默认为20。
        :type Limit: int
        """
        self._TargetGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TargetGroupIds = params.get("TargetGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupListResponse(AbstractModel):
    """DescribeTargetGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 显示的结果数量。
        :type TotalCount: int
        :param _TargetGroupSet: 显示的目标组信息集合。
        :type TargetGroupSet: list of TargetGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupSet(self):
        return self._TargetGroupSet

    @TargetGroupSet.setter
    def TargetGroupSet(self, TargetGroupSet):
        self._TargetGroupSet = TargetGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self._TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupsRequest(AbstractModel):
    """DescribeTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: 目标组ID，与Filters互斥。
        :type TargetGroupIds: list of str
        :param _Limit: 显示条数限制，默认为20。
        :type Limit: int
        :param _Offset: 显示的偏移起始量。
        :type Offset: int
        :param _Filters: 过滤条件数组，与TargetGroupIds互斥，支持TargetGroupVpcId和TargetGroupName。
        :type Filters: list of Filter
        """
        self._TargetGroupIds = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TargetGroupIds = params.get("TargetGroupIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeTargetGroupsResponse(AbstractModel):
    """DescribeTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 显示的结果数量。
        :type TotalCount: int
        :param _TargetGroupSet: 显示的目标组信息集合。
        :type TargetGroupSet: list of TargetGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupSet(self):
        return self._TargetGroupSet

    @TargetGroupSet.setter
    def TargetGroupSet(self, TargetGroupSet):
        self._TargetGroupSet = TargetGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self._TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 要查询的负载均衡实例ID列表。
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: 负载均衡实例列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancers: list of LoadBalancerHealth
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ListenerIds: 监听器 ID 列表。ID 数量上限为20个。
        :type ListenerIds: list of str
        :param _Protocol: 监听器协议类型。
        :type Protocol: str
        :param _Port: 监听器端口。
        :type Port: int
        :param _Filters: 查询负载均衡绑定的后端服务列表，过滤条件如下：
<li> location-id - String - 是否必填：否 - （过滤条件）按照 规则ID 过滤，如："loc-12345678"。</li>
<li> private-ip-address - String - 是否必填：否 - （过滤条件）按照 后端服务内网IP 过滤，如："172.16.1.1"。</li>
        :type Filters: list of Filter
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._Port = None
        self._Filters = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
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
        


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Listeners: 监听器后端绑定的机器信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ListenerBackend
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Listeners = None
        self._RequestId = None

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 请求ID，即接口返回的 RequestId 参数。
        :type TaskId: str
        :param _DealName: 订单ID。
注意：参数TaskId和DealName必须传一个。
        :type DealName: str
        """
        self._TaskId = None
        self._DealName = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务的当前状态。 0：成功，1：失败，2：进行中。
        :type Status: int
        :param _LoadBalancerIds: 由负载均衡实例唯一 ID 组成的数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._LoadBalancerIds = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._RequestId = params.get("RequestId")


class DisassociateTargetGroupsRequest(AbstractModel):
    """DisassociateTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Associations: 待解绑的规则关系数组。
        :type Associations: list of TargetGroupAssociation
        """
        self._Associations = None

    @property
    def Associations(self):
        return self._Associations

    @Associations.setter
    def Associations(self, Associations):
        self._Associations = Associations


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self._Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self._Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateTargetGroupsResponse(AbstractModel):
    """DisassociateTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ExclusiveCluster(AbstractModel):
    """独占集群

    """

    def __init__(self):
        r"""
        :param _L4Clusters: 4层独占集群列表
注意：此字段可能返回 null，表示取不到有效值。
        :type L4Clusters: list of ClusterItem
        :param _L7Clusters: 7层独占集群列表
注意：此字段可能返回 null，表示取不到有效值。
        :type L7Clusters: list of ClusterItem
        :param _ClassicalCluster: vpcgw集群
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassicalCluster: :class:`tencentcloud.clb.v20180317.models.ClusterItem`
        """
        self._L4Clusters = None
        self._L7Clusters = None
        self._ClassicalCluster = None

    @property
    def L4Clusters(self):
        return self._L4Clusters

    @L4Clusters.setter
    def L4Clusters(self, L4Clusters):
        self._L4Clusters = L4Clusters

    @property
    def L7Clusters(self):
        return self._L7Clusters

    @L7Clusters.setter
    def L7Clusters(self, L7Clusters):
        self._L7Clusters = L7Clusters

    @property
    def ClassicalCluster(self):
        return self._ClassicalCluster

    @ClassicalCluster.setter
    def ClassicalCluster(self, ClassicalCluster):
        self._ClassicalCluster = ClassicalCluster


    def _deserialize(self, params):
        if params.get("L4Clusters") is not None:
            self._L4Clusters = []
            for item in params.get("L4Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self._L4Clusters.append(obj)
        if params.get("L7Clusters") is not None:
            self._L7Clusters = []
            for item in params.get("L7Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self._L7Clusters.append(obj)
        if params.get("ClassicalCluster") is not None:
            self._ClassicalCluster = ClusterItem()
            self._ClassicalCluster._deserialize(params.get("ClassicalCluster"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraInfo(AbstractModel):
    """暂做保留，一般用户无需关注。

    """

    def __init__(self):
        r"""
        :param _ZhiTong: 是否开通VIP直通
注意：此字段可能返回 null，表示取不到有效值。
        :type ZhiTong: bool
        :param _TgwGroupName: TgwGroup名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TgwGroupName: str
        """
        self._ZhiTong = None
        self._TgwGroupName = None

    @property
    def ZhiTong(self):
        return self._ZhiTong

    @ZhiTong.setter
    def ZhiTong(self, ZhiTong):
        self._ZhiTong = ZhiTong

    @property
    def TgwGroupName(self):
        return self._TgwGroupName

    @TgwGroupName.setter
    def TgwGroupName(self, TgwGroupName):
        self._TgwGroupName = TgwGroupName


    def _deserialize(self, params):
        self._ZhiTong = params.get("ZhiTong")
        self._TgwGroupName = params.get("TgwGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤器的名称
        :type Name: str
        :param _Values: 过滤器的值数组
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
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
        


class FunctionInfo(AbstractModel):
    """SCF云函数（Serverless Cloud Function）相关信息。

    """

    def __init__(self):
        r"""
        :param _FunctionNamespace: 函数命名空间
        :type FunctionNamespace: str
        :param _FunctionName: 函数名称
        :type FunctionName: str
        :param _FunctionQualifier: 函数的版本名称或别名
        :type FunctionQualifier: str
        :param _FunctionQualifierType: 标识 FunctionQualifier 参数的类型，可取值： VERSION（版本）、ALIAS（别名）
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionQualifierType: str
        """
        self._FunctionNamespace = None
        self._FunctionName = None
        self._FunctionQualifier = None
        self._FunctionQualifierType = None

    @property
    def FunctionNamespace(self):
        return self._FunctionNamespace

    @FunctionNamespace.setter
    def FunctionNamespace(self, FunctionNamespace):
        self._FunctionNamespace = FunctionNamespace

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def FunctionQualifier(self):
        return self._FunctionQualifier

    @FunctionQualifier.setter
    def FunctionQualifier(self, FunctionQualifier):
        self._FunctionQualifier = FunctionQualifier

    @property
    def FunctionQualifierType(self):
        return self._FunctionQualifierType

    @FunctionQualifierType.setter
    def FunctionQualifierType(self, FunctionQualifierType):
        self._FunctionQualifierType = FunctionQualifierType


    def _deserialize(self, params):
        self._FunctionNamespace = params.get("FunctionNamespace")
        self._FunctionName = params.get("FunctionName")
        self._FunctionQualifier = params.get("FunctionQualifier")
        self._FunctionQualifierType = params.get("FunctionQualifierType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionTarget(AbstractModel):
    """SCF云函数（Serverless Cloud Function）作为后端服务

    """

    def __init__(self):
        r"""
        :param _Function: 云函数相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Function: :class:`tencentcloud.clb.v20180317.models.FunctionInfo`
        :param _Weight: 权重
        :type Weight: int
        """
        self._Function = None
        self._Weight = None

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        if params.get("Function") is not None:
            self._Function = FunctionInfo()
            self._Function._deserialize(params.get("Function"))
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheck(AbstractModel):
    """健康检查信息。
    注意，自定义探测相关参数 目前只有少量区域灰度支持。

    """

    def __init__(self):
        r"""
        :param _HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）。
        :type HealthSwitch: int
        :param _TimeOut: 健康检查的响应超时时间（仅适用于四层监听器），可选值：2~60，默认值：2，单位：秒。响应超时时间要小于检查间隔时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOut: int
        :param _IntervalTime: 健康检查探测间隔时间，默认值：5，IPv4 CLB实例的取值范围为：2-300，IPv6 CLB 实例的取值范围为：5-300。单位：秒。
说明：部分老旧 IPv4 CLB实例的取值范围为：5-300。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntervalTime: int
        :param _HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthNum: int
        :param _UnHealthNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发异常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnHealthNum: int
        :param _HttpCode: 健康检查状态码（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式）。可选值：1~31，默认 31。
1 表示探测后返回值 1xx 代表健康，2 表示返回 2xx 代表健康，4 表示返回 3xx 代表健康，8 表示返回 4xx 代表健康，16 表示返回 5xx 代表健康。若希望多种返回码都可代表健康，则将相应的值相加。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpCode: int
        :param _HttpCheckPath: 健康检查路径（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式）。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpCheckPath: str
        :param _HttpCheckDomain: 健康检查域名（仅适用于HTTP/HTTPS监听器和TCP监听器的HTTP健康检查方式。针对TCP监听器，当使用HTTP健康检查方式时，该参数为必填项）。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpCheckDomain: str
        :param _HttpCheckMethod: 健康检查方法（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式），默认值：HEAD，可选值HEAD或GET。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpCheckMethod: str
        :param _CheckPort: 自定义探测相关参数。健康检查端口，默认为后端服务的端口，除非您希望指定特定端口，否则建议留空。（仅适用于TCP/UDP监听器）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPort: int
        :param _ContextType: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查的输入格式，可取值：HEX或TEXT；取值为HEX时，SendContext和RecvContext的字符只能在0123456789ABCDEF中选取且长度必须是偶数位。（仅适用于TCP/UDP监听器）
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextType: str
        :param _SendContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查发送的请求内容，只允许ASCII可见字符，最大长度限制500。（仅适用于TCP/UDP监听器）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SendContext: str
        :param _RecvContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查返回的结果，只允许ASCII可见字符，最大长度限制500。（仅适用于TCP/UDP监听器）。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecvContext: str
        :param _CheckType: 健康检查使用的协议。取值 TCP | HTTP | HTTPS | GRPC | PING | CUSTOM，UDP监听器支持PING/CUSTOM，TCP监听器支持TCP/HTTP/CUSTOM，TCP_SSL/QUIC监听器支持TCP/HTTP，HTTP规则支持HTTP/GRPC，HTTPS规则支持HTTP/HTTPS/GRPC。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckType: str
        :param _HttpVersion: HTTP版本。健康检查协议CheckType的值取HTTP时，必传此字段，代表后端服务的HTTP版本：HTTP/1.0、HTTP/1.1；（仅适用于TCP监听器）
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpVersion: str
        :param _SourceIpType: 健康检查源IP类型：0（使用LB的VIP作为源IP），1（使用100.64网段IP作为源IP），默认值：0
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceIpType: int
        :param _ExtendedCode: GRPC健康检查状态码（仅适用于后端转发协议为GRPC的规则）。默认值为 12，可输入值为数值、多个数值、或者范围，例如 20 或 20,25 或 0-99
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtendedCode: str
        """
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnHealthNum = None
        self._HttpCode = None
        self._HttpCheckPath = None
        self._HttpCheckDomain = None
        self._HttpCheckMethod = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None
        self._CheckType = None
        self._HttpVersion = None
        self._SourceIpType = None
        self._ExtendedCode = None

    @property
    def HealthSwitch(self):
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnHealthNum(self):
        return self._UnHealthNum

    @UnHealthNum.setter
    def UnHealthNum(self, UnHealthNum):
        self._UnHealthNum = UnHealthNum

    @property
    def HttpCode(self):
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def HttpCheckPath(self):
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def HttpCheckDomain(self):
        return self._HttpCheckDomain

    @HttpCheckDomain.setter
    def HttpCheckDomain(self, HttpCheckDomain):
        self._HttpCheckDomain = HttpCheckDomain

    @property
    def HttpCheckMethod(self):
        return self._HttpCheckMethod

    @HttpCheckMethod.setter
    def HttpCheckMethod(self, HttpCheckMethod):
        self._HttpCheckMethod = HttpCheckMethod

    @property
    def CheckPort(self):
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def SendContext(self):
        return self._SendContext

    @SendContext.setter
    def SendContext(self, SendContext):
        self._SendContext = SendContext

    @property
    def RecvContext(self):
        return self._RecvContext

    @RecvContext.setter
    def RecvContext(self, RecvContext):
        self._RecvContext = RecvContext

    @property
    def CheckType(self):
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def HttpVersion(self):
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion

    @property
    def SourceIpType(self):
        return self._SourceIpType

    @SourceIpType.setter
    def SourceIpType(self, SourceIpType):
        self._SourceIpType = SourceIpType

    @property
    def ExtendedCode(self):
        return self._ExtendedCode

    @ExtendedCode.setter
    def ExtendedCode(self, ExtendedCode):
        self._ExtendedCode = ExtendedCode


    def _deserialize(self, params):
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnHealthNum = params.get("UnHealthNum")
        self._HttpCode = params.get("HttpCode")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._HttpCheckDomain = params.get("HttpCheckDomain")
        self._HttpCheckMethod = params.get("HttpCheckMethod")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        self._CheckType = params.get("CheckType")
        self._HttpVersion = params.get("HttpVersion")
        self._SourceIpType = params.get("SourceIpType")
        self._ExtendedCode = params.get("ExtendedCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdleLoadBalancer(AbstractModel):
    """闲置实例。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡名字
        :type LoadBalancerName: str
        :param _Region: 负载均衡所在地域
        :type Region: str
        :param _Vip: 负载均衡的vip
        :type Vip: str
        :param _IdleReason: 闲置原因。NO_RULES：没有规则，NO_RS：有规则没有绑定子机。
        :type IdleReason: str
        :param _Status: 负载均衡实例的状态，包括
0：创建中，1：正常运行。
        :type Status: int
        :param _Forward: 负载均衡类型标识，1：负载均衡，0：传统型负载均衡。
        :type Forward: int
        :param _Domain: 负载均衡域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Region = None
        self._Vip = None
        self._IdleReason = None
        self._Status = None
        self._Forward = None
        self._Domain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def IdleReason(self):
        return self._IdleReason

    @IdleReason.setter
    def IdleReason(self, IdleReason):
        self._IdleReason = IdleReason

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Forward(self):
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._IdleReason = params.get("IdleReason")
        self._Status = params.get("Status")
        self._Forward = params.get("Forward")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateLoadBalancerRequest(AbstractModel):
    """InquiryPriceCreateLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerType: 询价的负载均衡类型，OPEN为公网类型，INTERNAL为内网类型
        :type LoadBalancerType: str
        :param _LoadBalancerChargeType: 询价的收费类型，POSTPAID为按量计费，"PREPAID"为预付费包年包月
        :type LoadBalancerChargeType: str
        :param _LoadBalancerChargePrepaid: 询价的收费周期
        :type LoadBalancerChargePrepaid: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param _InternetAccessible: 询价的网络计费方式
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _GoodsNum: 询价的负载均衡实例个数，默认为1
        :type GoodsNum: int
        :param _ZoneId: 指定可用区询价。如：ap-guangzhou-1
        :type ZoneId: str
        :param _SlaType: 包年包月询价时传性能容量型规格，如：clb.c3.small。按量付费询价时传SLA
        :type SlaType: str
        :param _AddressIPVersion: IP版本，可取值：IPV4、IPV6、IPv6FullChain，不区分大小写，默认值 IPV4。说明：取值为IPV6表示为IPV6 NAT64版本；取值为IPv6FullChain，表示为IPv6版本。
        :type AddressIPVersion: str
        :param _VipIsp: 仅适用于公网负载均衡。目前仅广州、上海、南京、济南、杭州、福州、北京、石家庄、武汉、长沙、成都、重庆地域支持静态单线 IP 线路类型，如需体验，请联系商务经理申请。申请通过后，即可选择中国移动（CMCC）、中国联通（CUCC）或中国电信（CTCC）的运营商类型，网络计费模式只能使用按带宽包计费(BANDWIDTH_PACKAGE)。 如果不指定本参数，则默认使用BGP。可通过 DescribeResources 接口查询一个地域所支持的Isp。
示例值：CMCC
        :type VipIsp: str
        """
        self._LoadBalancerType = None
        self._LoadBalancerChargeType = None
        self._LoadBalancerChargePrepaid = None
        self._InternetAccessible = None
        self._GoodsNum = None
        self._ZoneId = None
        self._SlaType = None
        self._AddressIPVersion = None
        self._VipIsp = None

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def LoadBalancerChargeType(self):
        return self._LoadBalancerChargeType

    @LoadBalancerChargeType.setter
    def LoadBalancerChargeType(self, LoadBalancerChargeType):
        self._LoadBalancerChargeType = LoadBalancerChargeType

    @property
    def LoadBalancerChargePrepaid(self):
        return self._LoadBalancerChargePrepaid

    @LoadBalancerChargePrepaid.setter
    def LoadBalancerChargePrepaid(self, LoadBalancerChargePrepaid):
        self._LoadBalancerChargePrepaid = LoadBalancerChargePrepaid

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def VipIsp(self):
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp


    def _deserialize(self, params):
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._LoadBalancerChargeType = params.get("LoadBalancerChargeType")
        if params.get("LoadBalancerChargePrepaid") is not None:
            self._LoadBalancerChargePrepaid = LBChargePrepaid()
            self._LoadBalancerChargePrepaid._deserialize(params.get("LoadBalancerChargePrepaid"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._GoodsNum = params.get("GoodsNum")
        self._ZoneId = params.get("ZoneId")
        self._SlaType = params.get("SlaType")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._VipIsp = params.get("VipIsp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateLoadBalancerResponse(AbstractModel):
    """InquiryPriceCreateLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示对应的价格。
        :type Price: :class:`tencentcloud.clb.v20180317.models.Price`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceModifyLoadBalancerRequest(AbstractModel):
    """InquiryPriceModifyLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param _InternetAccessible: 修改后的网络带宽信息
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        """
        self._LoadBalancerId = None
        self._InternetAccessible = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceModifyLoadBalancerResponse(AbstractModel):
    """InquiryPriceModifyLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 描述价格信息
        :type Price: :class:`tencentcloud.clb.v20180317.models.Price`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRefundLoadBalancerRequest(AbstractModel):
    """InquiryPriceRefundLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        """
        self._LoadBalancerId = None

    @property
    def LoadBalancerId(self):
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
        


class InquiryPriceRefundLoadBalancerResponse(AbstractModel):
    """InquiryPriceRefundLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示对应的价格。
        :type Price: :class:`tencentcloud.clb.v20180317.models.Price`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewLoadBalancerRequest(AbstractModel):
    """InquiryPriceRenewLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param _LoadBalancerChargePrepaid: 续费周期
        :type LoadBalancerChargePrepaid: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        """
        self._LoadBalancerId = None
        self._LoadBalancerChargePrepaid = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerChargePrepaid(self):
        return self._LoadBalancerChargePrepaid

    @LoadBalancerChargePrepaid.setter
    def LoadBalancerChargePrepaid(self, LoadBalancerChargePrepaid):
        self._LoadBalancerChargePrepaid = LoadBalancerChargePrepaid


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("LoadBalancerChargePrepaid") is not None:
            self._LoadBalancerChargePrepaid = LBChargePrepaid()
            self._LoadBalancerChargePrepaid._deserialize(params.get("LoadBalancerChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewLoadBalancerResponse(AbstractModel):
    """InquiryPriceRenewLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 表示续费价格
        :type Price: :class:`tencentcloud.clb.v20180317.models.Price`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InternetAccessible(AbstractModel):
    """网络计费模式，最大出带宽

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR 按流量按小时后计费 ; BANDWIDTH_POSTPAID_BY_HOUR 按带宽按小时后计费;
BANDWIDTH_PACKAGE 按带宽包计费;
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 最大出带宽，单位Mbps，仅对公网属性的共享型、性能容量型和独占型 CLB 实例、以及内网属性的性能容量型 CLB 实例生效。
- 对于公网属性的共享型和独占型 CLB 实例，最大出带宽的范围为1Mbps-2048Mbps。
- 对于公网属性和内网属性的性能容量型 CLB实例，最大出带宽的范围为1Mbps-61440Mbps。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param _BandwidthpkgSubType: 带宽包的类型，如SINGLEISP
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthpkgSubType: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._BandwidthpkgSubType = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def BandwidthpkgSubType(self):
        return self._BandwidthpkgSubType

    @BandwidthpkgSubType.setter
    def BandwidthpkgSubType(self, BandwidthpkgSubType):
        self._BandwidthpkgSubType = BandwidthpkgSubType


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._BandwidthpkgSubType = params.get("BandwidthpkgSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """描述了单项的价格信息

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 后付费单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _ChargeUnit: 后续计价单元，可取值范围： 
HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）；
GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param _OriginalPrice: 预支费用的原价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _DiscountPrice: 预支费用的折扣价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _UnitPriceDiscount: 后付费的折扣单价，单位:元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _Discount: 折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        """
        self._UnitPrice = None
        self._ChargeUnit = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._UnitPriceDiscount = None
        self._Discount = None

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._Discount = params.get("Discount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LBChargePrepaid(AbstractModel):
    """lb实例包年包月相关配置属性

    """

    def __init__(self):
        r"""
        :param _RenewFlag: 续费类型：AUTO_RENEW 自动续费，  MANUAL_RENEW 手动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        :param _Period: 购买时长，单位：月
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        """
        self._RenewFlag = None
        self._Period = None

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._RenewFlag = params.get("RenewFlag")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LBItem(AbstractModel):
    """反查Lb绑定关系。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: lb的字符串id
        :type LoadBalancerId: str
        :param _Vip: lb的vip
        :type Vip: str
        :param _Listeners: 监听器规则
        :type Listeners: list of ListenerItem
        :param _Region: LB所在地域
        :type Region: str
        """
        self._LoadBalancerId = None
        self._Vip = None
        self._Listeners = None
        self._Region = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Vip = params.get("Vip")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerItem()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LbRsItem(AbstractModel):
    """查询类型

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc的字符串id，只支持字符串id。
        :type VpcId: str
        :param _PrivateIp: 需要查询后端的内网ip，可以是cvm和弹性网卡。
        :type PrivateIp: str
        """
        self._VpcId = None
        self._PrivateIp = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._PrivateIp = params.get("PrivateIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LbRsTargets(AbstractModel):
    """反查结果数据类型。

    """

    def __init__(self):
        r"""
        :param _Type: 内网ip类型。“cvm”或“eni”
        :type Type: str
        :param _PrivateIp: 后端实例的内网ip。
        :type PrivateIp: str
        :param _Port: 绑定后端实例的端口。
        :type Port: int
        :param _VpcId: rs的vpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param _Weight: rs的权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        """
        self._Type = None
        self._PrivateIp = None
        self._Port = None
        self._VpcId = None
        self._Weight = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._PrivateIp = params.get("PrivateIp")
        self._Port = params.get("Port")
        self._VpcId = params.get("VpcId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Listener(AbstractModel):
    """监听器的信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param _Protocol: 监听器协议
        :type Protocol: str
        :param _Port: 监听器端口
        :type Port: int
        :param _Certificate: 监听器绑定的证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param _HealthCheck: 监听器的健康检查信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Scheduler: 请求的调度方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheduler: str
        :param _SessionExpireTime: 会话保持时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionExpireTime: int
        :param _SniSwitch: 是否开启SNI特性，1：表示开启，0：表示不开启（本参数仅对于HTTPS监听器有意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type SniSwitch: int
        :param _Rules: 监听器下的全部转发规则（本参数仅对于HTTP/HTTPS监听器有意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of RuleOutput
        :param _ListenerName: 监听器的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _CreateTime: 监听器的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _EndPort: 端口段结束端口
注意：此字段可能返回 null，表示取不到有效值。
        :type EndPort: int
        :param _TargetType: 后端服务器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetType: str
        :param _TargetGroup: 绑定的目标组基本信息；当监听器绑定目标组时，会返回该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param _SessionType: 会话保持类型。NORMAL表示默认会话保持类型。QUIC_CID 表示根据Quic Connection ID做会话保持。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionType: str
        :param _KeepaliveEnable: 是否开启长连接，1开启，0关闭，（本参数仅对于HTTP/HTTPS监听器有意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepaliveEnable: int
        :param _Toa: 仅支持Nat64 CLB TCP监听器
注意：此字段可能返回 null，表示取不到有效值。
        :type Toa: bool
        :param _DeregisterTargetRst: 解绑后端目标时，是否发RST给客户端，（此参数仅对于TCP监听器有意义）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeregisterTargetRst: bool
        :param _AttrFlags: 监听器的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrFlags: list of str
        :param _TargetGroupList: 绑定的目标组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetGroupList: list of BasicTargetGroupInfo
        :param _MaxConn: 监听器最大连接数，-1表示监听器维度不限速。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConn: int
        :param _MaxCps: 监听器最大新增连接数，-1表示监听器维度不限速。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCps: int
        :param _IdleConnectTimeout: 空闲连接超时时间，仅支持TCP监听器。默认值:900；共享型实例和独占型实例取值范围：300～900，性能容量型实例取值范围:300～1980。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleConnectTimeout: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._Certificate = None
        self._HealthCheck = None
        self._Scheduler = None
        self._SessionExpireTime = None
        self._SniSwitch = None
        self._Rules = None
        self._ListenerName = None
        self._CreateTime = None
        self._EndPort = None
        self._TargetType = None
        self._TargetGroup = None
        self._SessionType = None
        self._KeepaliveEnable = None
        self._Toa = None
        self._DeregisterTargetRst = None
        self._AttrFlags = None
        self._TargetGroupList = None
        self._MaxConn = None
        self._MaxCps = None
        self._IdleConnectTimeout = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetGroup(self):
        return self._TargetGroup

    @TargetGroup.setter
    def TargetGroup(self, TargetGroup):
        self._TargetGroup = TargetGroup

    @property
    def SessionType(self):
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def KeepaliveEnable(self):
        return self._KeepaliveEnable

    @KeepaliveEnable.setter
    def KeepaliveEnable(self, KeepaliveEnable):
        self._KeepaliveEnable = KeepaliveEnable

    @property
    def Toa(self):
        return self._Toa

    @Toa.setter
    def Toa(self, Toa):
        self._Toa = Toa

    @property
    def DeregisterTargetRst(self):
        return self._DeregisterTargetRst

    @DeregisterTargetRst.setter
    def DeregisterTargetRst(self, DeregisterTargetRst):
        self._DeregisterTargetRst = DeregisterTargetRst

    @property
    def AttrFlags(self):
        return self._AttrFlags

    @AttrFlags.setter
    def AttrFlags(self, AttrFlags):
        self._AttrFlags = AttrFlags

    @property
    def TargetGroupList(self):
        return self._TargetGroupList

    @TargetGroupList.setter
    def TargetGroupList(self, TargetGroupList):
        self._TargetGroupList = TargetGroupList

    @property
    def MaxConn(self):
        return self._MaxConn

    @MaxConn.setter
    def MaxConn(self, MaxConn):
        self._MaxConn = MaxConn

    @property
    def MaxCps(self):
        return self._MaxCps

    @MaxCps.setter
    def MaxCps(self, MaxCps):
        self._MaxCps = MaxCps

    @property
    def IdleConnectTimeout(self):
        return self._IdleConnectTimeout

    @IdleConnectTimeout.setter
    def IdleConnectTimeout(self, IdleConnectTimeout):
        self._IdleConnectTimeout = IdleConnectTimeout


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Certificate") is not None:
            self._Certificate = CertificateOutput()
            self._Certificate._deserialize(params.get("Certificate"))
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._Scheduler = params.get("Scheduler")
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._SniSwitch = params.get("SniSwitch")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleOutput()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._ListenerName = params.get("ListenerName")
        self._CreateTime = params.get("CreateTime")
        self._EndPort = params.get("EndPort")
        self._TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self._TargetGroup = BasicTargetGroupInfo()
            self._TargetGroup._deserialize(params.get("TargetGroup"))
        self._SessionType = params.get("SessionType")
        self._KeepaliveEnable = params.get("KeepaliveEnable")
        self._Toa = params.get("Toa")
        self._DeregisterTargetRst = params.get("DeregisterTargetRst")
        self._AttrFlags = params.get("AttrFlags")
        if params.get("TargetGroupList") is not None:
            self._TargetGroupList = []
            for item in params.get("TargetGroupList"):
                obj = BasicTargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupList.append(obj)
        self._MaxConn = params.get("MaxConn")
        self._MaxCps = params.get("MaxCps")
        self._IdleConnectTimeout = params.get("IdleConnectTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerBackend(AbstractModel):
    """监听器上绑定的后端服务的信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID
        :type ListenerId: str
        :param _Protocol: 监听器的协议
        :type Protocol: str
        :param _Port: 监听器的端口
        :type Port: int
        :param _Rules: 监听器下的规则信息（仅适用于HTTP/HTTPS监听器）
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of RuleTargets
        :param _Targets: 监听器上绑定的后端服务列表（仅适用于TCP/UDP/TCP_SSL监听器）
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of Backend
        :param _EndPort: 若支持端口段，则为端口段结束端口；若不支持端口段，则为0
注意：此字段可能返回 null，表示取不到有效值。
        :type EndPort: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._Rules = None
        self._Targets = None
        self._EndPort = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleTargets()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerHealth(AbstractModel):
    """监听器的健康检查信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ListenerName: 监听器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _Protocol: 监听器的协议
        :type Protocol: str
        :param _Port: 监听器的端口
        :type Port: int
        :param _Rules: 监听器的转发规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of RuleHealth
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._Port = None
        self._Rules = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerItem(AbstractModel):
    """反查监听器类型

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _Protocol: 监听器协议
        :type Protocol: str
        :param _Port: 监听器端口
        :type Port: int
        :param _Rules: 绑定规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of RulesItems
        :param _Targets: 四层绑定对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of LbRsTargets
        :param _EndPort: 端口段监听器的结束端口
注意：此字段可能返回 null，表示取不到有效值。
        :type EndPort: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._Rules = None
        self._Targets = None
        self._EndPort = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RulesItems()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = LbRsTargets()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """负载均衡实例的信息

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例的名称。
        :type LoadBalancerName: str
        :param _LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
        :type LoadBalancerType: str
        :param _Forward: 负载均衡类型标识，1：负载均衡，0：传统型负载均衡。
        :type Forward: int
        :param _Domain: 负载均衡实例的域名，仅公网传统型负载均衡实例才提供该字段。逐步下线中，建议用LoadBalancerDomain替代。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _LoadBalancerVips: 负载均衡实例的 VIP 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerVips: list of str
        :param _Status: 负载均衡实例的状态，包括
0：创建中，1：正常运行。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 负载均衡实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _StatusTime: 负载均衡实例的上次状态转换时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusTime: str
        :param _ProjectId: 负载均衡实例所属的项目 ID， 0 表示默认项目。
        :type ProjectId: int
        :param _VpcId: 私有网络的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _OpenBgp: 高防 LB 的标识，1：高防负载均衡 0：非高防负载均衡。
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenBgp: int
        :param _Snat: 在 2016 年 12 月份之前的传统型内网负载均衡都是开启了 snat 的。
注意：此字段可能返回 null，表示取不到有效值。
        :type Snat: bool
        :param _Isolation: 0：表示未被隔离，1：表示被隔离。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isolation: int
        :param _Log: 用户开启日志的信息，日志只有公网属性创建了 HTTP 、HTTPS 监听器的负载均衡才会有日志。
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: str
        :param _SubnetId: 负载均衡实例所在的子网（仅对内网VPC型LB有意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Tags: 负载均衡实例的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param _SecureGroups: 负载均衡实例的安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecureGroups: list of str
        :param _TargetRegionInfo: 负载均衡实例绑定的后端设备的基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param _AnycastZone: anycast负载均衡的发布域，对于非anycast的负载均衡，此字段返回为空字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type AnycastZone: str
        :param _AddressIPVersion: IP版本，ipv4 | ipv6
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPVersion: str
        :param _NumericalVpcId: 数值形式的私有网络 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NumericalVpcId: int
        :param _VipIsp: 负载均衡IP地址所属的ISP
注意：此字段可能返回 null，表示取不到有效值。
        :type VipIsp: str
        :param _MasterZone: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: :class:`tencentcloud.clb.v20180317.models.ZoneInfo`
        :param _BackupZoneSet: 备可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupZoneSet: list of ZoneInfo
        :param _IsolatedTime: 负载均衡实例被隔离的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param _ExpireTime: 负载均衡实例的过期时间，仅对预付费负载均衡生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _ChargeType: 负载均衡实例的计费类型，PREPAID：包年包月，POSTPAID_BY_HOUR：按量计费
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param _NetworkAttributes: 负载均衡实例的网络属性
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _PrepaidAttributes: 负载均衡实例的预付费相关属性
注意：此字段可能返回 null，表示取不到有效值。
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param _LogSetId: 负载均衡日志服务(CLS)的日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSetId: str
        :param _LogTopicId: 负载均衡日志服务(CLS)的日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        :param _AddressIPv6: 负载均衡实例的IPv6地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPv6: str
        :param _ExtraInfo: 暂做保留，一般用户无需关注。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param _IsDDos: 是否可绑定高防包
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDDos: bool
        :param _ConfigId: 负载均衡维度的个性化配置ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param _LoadBalancerPassToTarget: 后端服务是否放通来自LB的流量
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerPassToTarget: bool
        :param _ExclusiveCluster: 内网独占集群
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param _IPv6Mode: IP地址版本为ipv6时此字段有意义， IPv6Nat64 | IPv6FullChain
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6Mode: str
        :param _SnatPro: 是否开启SnatPro。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnatPro: bool
        :param _SnatIps: 开启SnatPro负载均衡后，SnatIp列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnatIps: list of SnatIp
        :param _SlaType: 性能容量型规格
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaType: str
        :param _IsBlock: vip是否被封堵
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBlock: bool
        :param _IsBlockTime: 封堵或解封时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBlockTime: str
        :param _LocalBgp: IP类型是否是本地BGP
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalBgp: bool
        :param _ClusterTag: 7层独占标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterTag: str
        :param _MixIpTarget: 开启IPv6FullChain负载均衡7层监听器支持混绑IPv4/IPv6目标功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type MixIpTarget: bool
        :param _Zones: 私有网络内网负载均衡，就近接入模式下规则所落在的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        :param _NfvInfo: CLB是否为NFV，空：不是，l7nfv：七层是NFV。
注意：此字段可能返回 null，表示取不到有效值。
        :type NfvInfo: str
        :param _HealthLogSetId: 负载均衡日志服务(CLS)的健康检查日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthLogSetId: str
        :param _HealthLogTopicId: 负载均衡日志服务(CLS)的健康检查日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthLogTopicId: str
        :param _ClusterIds: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIds: list of str
        :param _AttributeFlags: 负载均衡的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type AttributeFlags: list of str
        :param _LoadBalancerDomain: 负载均衡实例的域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerDomain: str
        :param _Egress: 网络出口
注意：此字段可能返回 null，表示取不到有效值。
        :type Egress: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerType = None
        self._Forward = None
        self._Domain = None
        self._LoadBalancerVips = None
        self._Status = None
        self._CreateTime = None
        self._StatusTime = None
        self._ProjectId = None
        self._VpcId = None
        self._OpenBgp = None
        self._Snat = None
        self._Isolation = None
        self._Log = None
        self._SubnetId = None
        self._Tags = None
        self._SecureGroups = None
        self._TargetRegionInfo = None
        self._AnycastZone = None
        self._AddressIPVersion = None
        self._NumericalVpcId = None
        self._VipIsp = None
        self._MasterZone = None
        self._BackupZoneSet = None
        self._IsolatedTime = None
        self._ExpireTime = None
        self._ChargeType = None
        self._NetworkAttributes = None
        self._PrepaidAttributes = None
        self._LogSetId = None
        self._LogTopicId = None
        self._AddressIPv6 = None
        self._ExtraInfo = None
        self._IsDDos = None
        self._ConfigId = None
        self._LoadBalancerPassToTarget = None
        self._ExclusiveCluster = None
        self._IPv6Mode = None
        self._SnatPro = None
        self._SnatIps = None
        self._SlaType = None
        self._IsBlock = None
        self._IsBlockTime = None
        self._LocalBgp = None
        self._ClusterTag = None
        self._MixIpTarget = None
        self._Zones = None
        self._NfvInfo = None
        self._HealthLogSetId = None
        self._HealthLogTopicId = None
        self._ClusterIds = None
        self._AttributeFlags = None
        self._LoadBalancerDomain = None
        self._Egress = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerVips(self):
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StatusTime(self):
        return self._StatusTime

    @StatusTime.setter
    def StatusTime(self, StatusTime):
        self._StatusTime = StatusTime

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def OpenBgp(self):
        return self._OpenBgp

    @OpenBgp.setter
    def OpenBgp(self, OpenBgp):
        self._OpenBgp = OpenBgp

    @property
    def Snat(self):
        return self._Snat

    @Snat.setter
    def Snat(self, Snat):
        self._Snat = Snat

    @property
    def Isolation(self):
        return self._Isolation

    @Isolation.setter
    def Isolation(self, Isolation):
        self._Isolation = Isolation

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SecureGroups(self):
        return self._SecureGroups

    @SecureGroups.setter
    def SecureGroups(self, SecureGroups):
        self._SecureGroups = SecureGroups

    @property
    def TargetRegionInfo(self):
        return self._TargetRegionInfo

    @TargetRegionInfo.setter
    def TargetRegionInfo(self, TargetRegionInfo):
        self._TargetRegionInfo = TargetRegionInfo

    @property
    def AnycastZone(self):
        return self._AnycastZone

    @AnycastZone.setter
    def AnycastZone(self, AnycastZone):
        self._AnycastZone = AnycastZone

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def NumericalVpcId(self):
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def VipIsp(self):
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def BackupZoneSet(self):
        return self._BackupZoneSet

    @BackupZoneSet.setter
    def BackupZoneSet(self, BackupZoneSet):
        self._BackupZoneSet = BackupZoneSet

    @property
    def IsolatedTime(self):
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def NetworkAttributes(self):
        return self._NetworkAttributes

    @NetworkAttributes.setter
    def NetworkAttributes(self, NetworkAttributes):
        self._NetworkAttributes = NetworkAttributes

    @property
    def PrepaidAttributes(self):
        return self._PrepaidAttributes

    @PrepaidAttributes.setter
    def PrepaidAttributes(self, PrepaidAttributes):
        self._PrepaidAttributes = PrepaidAttributes

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def AddressIPv6(self):
        return self._AddressIPv6

    @AddressIPv6.setter
    def AddressIPv6(self, AddressIPv6):
        self._AddressIPv6 = AddressIPv6

    @property
    def ExtraInfo(self):
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def IsDDos(self):
        return self._IsDDos

    @IsDDos.setter
    def IsDDos(self, IsDDos):
        self._IsDDos = IsDDos

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def LoadBalancerPassToTarget(self):
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def ExclusiveCluster(self):
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def IPv6Mode(self):
        return self._IPv6Mode

    @IPv6Mode.setter
    def IPv6Mode(self, IPv6Mode):
        self._IPv6Mode = IPv6Mode

    @property
    def SnatPro(self):
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def IsBlock(self):
        return self._IsBlock

    @IsBlock.setter
    def IsBlock(self, IsBlock):
        self._IsBlock = IsBlock

    @property
    def IsBlockTime(self):
        return self._IsBlockTime

    @IsBlockTime.setter
    def IsBlockTime(self, IsBlockTime):
        self._IsBlockTime = IsBlockTime

    @property
    def LocalBgp(self):
        return self._LocalBgp

    @LocalBgp.setter
    def LocalBgp(self, LocalBgp):
        self._LocalBgp = LocalBgp

    @property
    def ClusterTag(self):
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def MixIpTarget(self):
        return self._MixIpTarget

    @MixIpTarget.setter
    def MixIpTarget(self, MixIpTarget):
        self._MixIpTarget = MixIpTarget

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def NfvInfo(self):
        return self._NfvInfo

    @NfvInfo.setter
    def NfvInfo(self, NfvInfo):
        self._NfvInfo = NfvInfo

    @property
    def HealthLogSetId(self):
        return self._HealthLogSetId

    @HealthLogSetId.setter
    def HealthLogSetId(self, HealthLogSetId):
        self._HealthLogSetId = HealthLogSetId

    @property
    def HealthLogTopicId(self):
        return self._HealthLogTopicId

    @HealthLogTopicId.setter
    def HealthLogTopicId(self, HealthLogTopicId):
        self._HealthLogTopicId = HealthLogTopicId

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def AttributeFlags(self):
        return self._AttributeFlags

    @AttributeFlags.setter
    def AttributeFlags(self, AttributeFlags):
        self._AttributeFlags = AttributeFlags

    @property
    def LoadBalancerDomain(self):
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Forward = params.get("Forward")
        self._Domain = params.get("Domain")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._StatusTime = params.get("StatusTime")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._OpenBgp = params.get("OpenBgp")
        self._Snat = params.get("Snat")
        self._Isolation = params.get("Isolation")
        self._Log = params.get("Log")
        self._SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SecureGroups = params.get("SecureGroups")
        if params.get("TargetRegionInfo") is not None:
            self._TargetRegionInfo = TargetRegionInfo()
            self._TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        self._AnycastZone = params.get("AnycastZone")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._NumericalVpcId = params.get("NumericalVpcId")
        self._VipIsp = params.get("VipIsp")
        if params.get("MasterZone") is not None:
            self._MasterZone = ZoneInfo()
            self._MasterZone._deserialize(params.get("MasterZone"))
        if params.get("BackupZoneSet") is not None:
            self._BackupZoneSet = []
            for item in params.get("BackupZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._BackupZoneSet.append(obj)
        self._IsolatedTime = params.get("IsolatedTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self._NetworkAttributes = InternetAccessible()
            self._NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self._PrepaidAttributes = LBChargePrepaid()
            self._PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        self._LogSetId = params.get("LogSetId")
        self._LogTopicId = params.get("LogTopicId")
        self._AddressIPv6 = params.get("AddressIPv6")
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._IsDDos = params.get("IsDDos")
        self._ConfigId = params.get("ConfigId")
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        if params.get("ExclusiveCluster") is not None:
            self._ExclusiveCluster = ExclusiveCluster()
            self._ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self._IPv6Mode = params.get("IPv6Mode")
        self._SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self._SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self._SnatIps.append(obj)
        self._SlaType = params.get("SlaType")
        self._IsBlock = params.get("IsBlock")
        self._IsBlockTime = params.get("IsBlockTime")
        self._LocalBgp = params.get("LocalBgp")
        self._ClusterTag = params.get("ClusterTag")
        self._MixIpTarget = params.get("MixIpTarget")
        self._Zones = params.get("Zones")
        self._NfvInfo = params.get("NfvInfo")
        self._HealthLogSetId = params.get("HealthLogSetId")
        self._HealthLogTopicId = params.get("HealthLogTopicId")
        self._ClusterIds = params.get("ClusterIds")
        self._AttributeFlags = params.get("AttributeFlags")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerDetail(AbstractModel):
    """负载均衡详细信息

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例的名称。
        :type LoadBalancerName: str
        :param _LoadBalancerType: 负载均衡实例的网络类型：
Public：公网属性， Private：内网属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _Status: 负载均衡实例的状态，包括
0：创建中，1：正常运行。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Address: 负载均衡实例的 VIP 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _AddressIPv6: 负载均衡实例 VIP 的IPv6地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPv6: str
        :param _AddressIPVersion: 负载均衡实例IP版本，IPv4 | IPv6。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPVersion: str
        :param _IPv6Mode: 负载均衡实例IPv6地址类型，IPv6Nat64 | IPv6FullChain。
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6Mode: str
        :param _Zone: 负载均衡实例所在可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _AddressIsp: 负载均衡实例IP地址所属的ISP。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIsp: str
        :param _VpcId: 负载均衡实例所属私有网络的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _ProjectId: 负载均衡实例所属的项目 ID， 0 表示默认项目。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _CreateTime: 负载均衡实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ChargeType: 负载均衡实例的计费类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param _NetworkAttributes: 负载均衡实例的网络属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _PrepaidAttributes: 负载均衡实例的预付费相关属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param _ExtraInfo: 暂做保留，一般用户无需关注。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param _ConfigId: 负载均衡维度的个性化配置ID，多个配置用逗号隔开。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param _Tags: 负载均衡实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param _ListenerId: 负载均衡监听器 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _Protocol: 监听器协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Port: 监听器端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _LocationId: 转发规则的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationId: str
        :param _Domain: 转发规则的域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Url: 转发规则的路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _TargetId: 后端目标ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetId: str
        :param _TargetAddress: 后端目标的IP地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAddress: str
        :param _TargetPort: 后端目标监听端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetPort: int
        :param _TargetWeight: 后端目标转发权重。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetWeight: int
        :param _Isolation: 0：表示未被隔离，1：表示被隔离。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isolation: int
        :param _SecurityGroup: 负载均衡绑定的安全组列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroup: list of str
        :param _LoadBalancerPassToTarget: 负载均衡安全组上移特性是否开启标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerPassToTarget: int
        :param _TargetHealth: 后端目标健康状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetHealth: str
        :param _Domains: 转发规则的域名列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: str
        :param _SlaveZone: 多可用区负载均衡实例所选备区
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZone: list of str
        :param _Zones: 内网负载均衡实例所在可用区，由白名单CLB_Internal_Zone控制
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        :param _SniSwitch: 是否开启SNI特性，1：表示开启，0：表示不开启（本参数仅对于HTTPS监听器有意义）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SniSwitch: int
        :param _LoadBalancerDomain: 负载均衡实例的域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerDomain: str
        :param _Egress: 网络出口
注意：此字段可能返回 null，表示取不到有效值。
        :type Egress: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerType = None
        self._Status = None
        self._Address = None
        self._AddressIPv6 = None
        self._AddressIPVersion = None
        self._IPv6Mode = None
        self._Zone = None
        self._AddressIsp = None
        self._VpcId = None
        self._ProjectId = None
        self._CreateTime = None
        self._ChargeType = None
        self._NetworkAttributes = None
        self._PrepaidAttributes = None
        self._ExtraInfo = None
        self._ConfigId = None
        self._Tags = None
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._TargetId = None
        self._TargetAddress = None
        self._TargetPort = None
        self._TargetWeight = None
        self._Isolation = None
        self._SecurityGroup = None
        self._LoadBalancerPassToTarget = None
        self._TargetHealth = None
        self._Domains = None
        self._SlaveZone = None
        self._Zones = None
        self._SniSwitch = None
        self._LoadBalancerDomain = None
        self._Egress = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AddressIPv6(self):
        return self._AddressIPv6

    @AddressIPv6.setter
    def AddressIPv6(self, AddressIPv6):
        self._AddressIPv6 = AddressIPv6

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def IPv6Mode(self):
        return self._IPv6Mode

    @IPv6Mode.setter
    def IPv6Mode(self, IPv6Mode):
        self._IPv6Mode = IPv6Mode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AddressIsp(self):
        return self._AddressIsp

    @AddressIsp.setter
    def AddressIsp(self, AddressIsp):
        self._AddressIsp = AddressIsp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def NetworkAttributes(self):
        return self._NetworkAttributes

    @NetworkAttributes.setter
    def NetworkAttributes(self, NetworkAttributes):
        self._NetworkAttributes = NetworkAttributes

    @property
    def PrepaidAttributes(self):
        return self._PrepaidAttributes

    @PrepaidAttributes.setter
    def PrepaidAttributes(self, PrepaidAttributes):
        self._PrepaidAttributes = PrepaidAttributes

    @property
    def ExtraInfo(self):
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetAddress(self):
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress

    @property
    def TargetPort(self):
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def TargetWeight(self):
        return self._TargetWeight

    @TargetWeight.setter
    def TargetWeight(self, TargetWeight):
        self._TargetWeight = TargetWeight

    @property
    def Isolation(self):
        return self._Isolation

    @Isolation.setter
    def Isolation(self, Isolation):
        self._Isolation = Isolation

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def LoadBalancerPassToTarget(self):
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def TargetHealth(self):
        return self._TargetHealth

    @TargetHealth.setter
    def TargetHealth(self, TargetHealth):
        self._TargetHealth = TargetHealth

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def LoadBalancerDomain(self):
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Status = params.get("Status")
        self._Address = params.get("Address")
        self._AddressIPv6 = params.get("AddressIPv6")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._IPv6Mode = params.get("IPv6Mode")
        self._Zone = params.get("Zone")
        self._AddressIsp = params.get("AddressIsp")
        self._VpcId = params.get("VpcId")
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self._NetworkAttributes = InternetAccessible()
            self._NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self._PrepaidAttributes = LBChargePrepaid()
            self._PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._ConfigId = params.get("ConfigId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._TargetId = params.get("TargetId")
        self._TargetAddress = params.get("TargetAddress")
        self._TargetPort = params.get("TargetPort")
        self._TargetWeight = params.get("TargetWeight")
        self._Isolation = params.get("Isolation")
        self._SecurityGroup = params.get("SecurityGroup")
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self._TargetHealth = params.get("TargetHealth")
        self._Domains = params.get("Domains")
        self._SlaveZone = params.get("SlaveZone")
        self._Zones = params.get("Zones")
        self._SniSwitch = params.get("SniSwitch")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerHealth(AbstractModel):
    """负载均衡实例的健康检查状态

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param _Listeners: 监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ListenerHealth
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self._Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerTraffic(AbstractModel):
    """负载均衡流量数据。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡名字
        :type LoadBalancerName: str
        :param _Region: 负载均衡所在地域
        :type Region: str
        :param _Vip: 负载均衡的vip
        :type Vip: str
        :param _OutBandwidth: 最大出带宽，单位：Mbps
        :type OutBandwidth: float
        :param _Domain: CLB域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Region = None
        self._Vip = None
        self._OutBandwidth = None
        self._Domain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def OutBandwidth(self):
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._OutBandwidth = params.get("OutBandwidth")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualRewriteRequest(AbstractModel):
    """ManualRewrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _SourceListenerId: 源监听器 ID。
        :type SourceListenerId: str
        :param _TargetListenerId: 目标监听器 ID。
        :type TargetListenerId: str
        :param _RewriteInfos: 转发规则之间的重定向关系。
        :type RewriteInfos: list of RewriteLocationMap
        """
        self._LoadBalancerId = None
        self._SourceListenerId = None
        self._TargetListenerId = None
        self._RewriteInfos = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SourceListenerId(self):
        return self._SourceListenerId

    @SourceListenerId.setter
    def SourceListenerId(self, SourceListenerId):
        self._SourceListenerId = SourceListenerId

    @property
    def TargetListenerId(self):
        return self._TargetListenerId

    @TargetListenerId.setter
    def TargetListenerId(self, TargetListenerId):
        self._TargetListenerId = TargetListenerId

    @property
    def RewriteInfos(self):
        return self._RewriteInfos

    @RewriteInfos.setter
    def RewriteInfos(self, RewriteInfos):
        self._RewriteInfos = RewriteInfos


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SourceListenerId = params.get("SourceListenerId")
        self._TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self._RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self._RewriteInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualRewriteResponse(AbstractModel):
    """ManualRewrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MigrateClassicalLoadBalancersRequest(AbstractModel):
    """MigrateClassicalLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 传统型负载均衡ID数组
        :type LoadBalancerIds: list of str
        :param _ExclusiveCluster: 独占集群信息
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        """
        self._LoadBalancerIds = None
        self._ExclusiveCluster = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ExclusiveCluster(self):
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ExclusiveCluster") is not None:
            self._ExclusiveCluster = ExclusiveCluster()
            self._ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateClassicalLoadBalancersResponse(AbstractModel):
    """MigrateClassicalLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBlockIPListRequest(AbstractModel):
    """ModifyBlockIPList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 负载均衡实例ID
        :type LoadBalancerIds: list of str
        :param _Type: 操作类型，可取：
<li> add_customized_field（首次设置header，开启黑名单功能）</li>
<li> set_customized_field（修改header）</li>
<li> del_customized_field（删除header）</li>
<li> add_blocked（添加黑名单）</li>
<li> del_blocked（删除黑名单）</li>
<li> flush_blocked（清空黑名单）</li>
        :type Type: str
        :param _ClientIPField: 客户端真实IP存放的header字段名
        :type ClientIPField: str
        :param _BlockIPList: 封禁IP列表，单次操作数组最大长度支持200000
        :type BlockIPList: list of str
        :param _ExpireTime: 过期时间，单位秒，默认值3600
        :type ExpireTime: int
        :param _AddStrategy: 添加IP的策略，可取：fifo（如果黑名单容量已满，新加入黑名单的IP采用先进先出策略）
        :type AddStrategy: str
        """
        self._LoadBalancerIds = None
        self._Type = None
        self._ClientIPField = None
        self._BlockIPList = None
        self._ExpireTime = None
        self._AddStrategy = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClientIPField(self):
        return self._ClientIPField

    @ClientIPField.setter
    def ClientIPField(self, ClientIPField):
        self._ClientIPField = ClientIPField

    @property
    def BlockIPList(self):
        return self._BlockIPList

    @BlockIPList.setter
    def BlockIPList(self, BlockIPList):
        self._BlockIPList = BlockIPList

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AddStrategy(self):
        return self._AddStrategy

    @AddStrategy.setter
    def AddStrategy(self, AddStrategy):
        self._AddStrategy = AddStrategy


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._Type = params.get("Type")
        self._ClientIPField = params.get("ClientIPField")
        self._BlockIPList = params.get("BlockIPList")
        self._ExpireTime = params.get("ExpireTime")
        self._AddStrategy = params.get("AddStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIPListResponse(AbstractModel):
    """ModifyBlockIPList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JodId: 异步任务的ID
        :type JodId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JodId = None
        self._RequestId = None

    @property
    def JodId(self):
        return self._JodId

    @JodId.setter
    def JodId(self, JodId):
        self._JodId = JodId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JodId = params.get("JodId")
        self._RequestId = params.get("RequestId")


class ModifyDomainAttributesRequest(AbstractModel):
    """ModifyDomainAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param _Domain: 域名（必须是已经创建的转发规则下的域名），如果是多域名，可以指定多域名列表中的任意一个。
        :type Domain: str
        :param _NewDomain: 要修改的新域名。NewDomain和NewDomains只能传一个。
        :type NewDomain: str
        :param _Certificate: 域名相关的证书信息，注意，仅对启用SNI的监听器适用，不可和MultiCertInfo 同时传入。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param _Http2: 是否开启Http2，注意，只有HTTPS域名才能开启Http2。
        :type Http2: bool
        :param _DefaultServer: 是否设为默认域名，注意，一个监听器下只能设置一个默认域名。
        :type DefaultServer: bool
        :param _Quic: 是否开启Quic，注意，只有HTTPS域名才能开启Quic
        :type Quic: bool
        :param _NewDefaultServerDomain: 监听器下必须配置一个默认域名，若要关闭原默认域名，必须同时指定另一个域名作为新的默认域名，如果新的默认域名是多域名，可以指定多域名列表中的任意一个。
        :type NewDefaultServerDomain: str
        :param _NewDomains: 要修改的新域名列表。NewDomain和NewDomains只能传一个。
        :type NewDomains: list of str
        :param _MultiCertInfo: 域名相关的证书信息，注意，仅对启用SNI的监听器适用；支持同时传入多本算法类型不同的服务器证书，不可和MultiCertInfo 同时传入。
        :type MultiCertInfo: :class:`tencentcloud.clb.v20180317.models.MultiCertInfo`
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domain = None
        self._NewDomain = None
        self._Certificate = None
        self._Http2 = None
        self._DefaultServer = None
        self._Quic = None
        self._NewDefaultServerDomain = None
        self._NewDomains = None
        self._MultiCertInfo = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def NewDomain(self):
        return self._NewDomain

    @NewDomain.setter
    def NewDomain(self, NewDomain):
        self._NewDomain = NewDomain

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def DefaultServer(self):
        return self._DefaultServer

    @DefaultServer.setter
    def DefaultServer(self, DefaultServer):
        self._DefaultServer = DefaultServer

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def NewDefaultServerDomain(self):
        return self._NewDefaultServerDomain

    @NewDefaultServerDomain.setter
    def NewDefaultServerDomain(self, NewDefaultServerDomain):
        self._NewDefaultServerDomain = NewDefaultServerDomain

    @property
    def NewDomains(self):
        return self._NewDomains

    @NewDomains.setter
    def NewDomains(self, NewDomains):
        self._NewDomains = NewDomains

    @property
    def MultiCertInfo(self):
        return self._MultiCertInfo

    @MultiCertInfo.setter
    def MultiCertInfo(self, MultiCertInfo):
        self._MultiCertInfo = MultiCertInfo


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._NewDomain = params.get("NewDomain")
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._Http2 = params.get("Http2")
        self._DefaultServer = params.get("DefaultServer")
        self._Quic = params.get("Quic")
        self._NewDefaultServerDomain = params.get("NewDefaultServerDomain")
        self._NewDomains = params.get("NewDomains")
        if params.get("MultiCertInfo") is not None:
            self._MultiCertInfo = MultiCertInfo()
            self._MultiCertInfo._deserialize(params.get("MultiCertInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainAttributesResponse(AbstractModel):
    """ModifyDomainAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器 ID。
        :type ListenerId: str
        :param _Domain: 监听器下的某个旧域名。
        :type Domain: str
        :param _NewDomain: 新域名，	长度限制为：1-120。有三种使用格式：非正则表达式格式，通配符格式，正则表达式格式。非正则表达式格式只能使用字母、数字、‘-’、‘.’。通配符格式的使用 ‘*’ 只能在开头或者结尾。正则表达式以'~'开头。
        :type NewDomain: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domain = None
        self._NewDomain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def NewDomain(self):
        return self._NewDomain

    @NewDomain.setter
    def NewDomain(self, NewDomain):
        self._NewDomain = NewDomain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._NewDomain = params.get("NewDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainResponse(AbstractModel):
    """ModifyDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyFunctionTargetsRequest(AbstractModel):
    """ModifyFunctionTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param _FunctionTargets: 要修改的后端云函数服务列表。
        :type FunctionTargets: list of FunctionTarget
        :param _LocationId: 转发规则的ID，当绑定机器到七层转发规则时，必须提供此参数或Domain+Url两者之一。
        :type LocationId: str
        :param _Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param _Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._FunctionTargets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def FunctionTargets(self):
        return self._FunctionTargets

    @FunctionTargets.setter
    def FunctionTargets(self, FunctionTargets):
        self._FunctionTargets = FunctionTargets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("FunctionTargets") is not None:
            self._FunctionTargets = []
            for item in params.get("FunctionTargets"):
                obj = FunctionTarget()
                obj._deserialize(item)
                self._FunctionTargets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFunctionTargetsResponse(AbstractModel):
    """ModifyFunctionTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    """ModifyListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param _ListenerName: 新的监听器名称。
        :type ListenerName: str
        :param _SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :type SessionExpireTime: int
        :param _HealthCheck: 健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL/QUIC监听器。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Certificate: 证书相关信息，此参数仅适用于HTTPS/TCP_SSL/QUIC监听器；此参数和MultiCertInfo不能同时传入。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param _Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。
        :type Scheduler: str
        :param _SniSwitch: 是否开启SNI特性，此参数仅适用于HTTPS监听器。注意：未开启SNI的监听器可以开启SNI；已开启SNI的监听器不能关闭SNI。
        :type SniSwitch: int
        :param _TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组。
        :type TargetType: str
        :param _KeepaliveEnable: 是否开启长连接，此参数仅适用于HTTP/HTTPS监听器。
        :type KeepaliveEnable: int
        :param _DeregisterTargetRst: 解绑后端目标时，是否发RST给客户端，此参数仅适用于TCP监听器。
        :type DeregisterTargetRst: bool
        :param _SessionType: 会话保持类型。NORMAL表示默认会话保持类型。QUIC_CID表示根据Quic Connection ID做会话保持。QUIC_CID只支持UDP协议。
        :type SessionType: str
        :param _MultiCertInfo: 证书信息，支持同时传入不同算法类型的多本服务端证书；此参数仅适用于未开启SNI特性的HTTPS监听器。此参数和Certificate不能同时传入。
        :type MultiCertInfo: :class:`tencentcloud.clb.v20180317.models.MultiCertInfo`
        :param _MaxConn: 监听器粒度并发连接数上限，当前仅性能容量型实例且仅TCP/UDP/TCP_SSL/QUIC监听器支持。取值范围：1-实例规格并发连接上限，其中-1表示关闭监听器粒度并发连接数限速。
        :type MaxConn: int
        :param _MaxCps: 监听器粒度新建连接数上限，当前仅性能容量型实例且仅TCP/UDP/TCP_SSL/QUIC监听器支持。取值范围：1-实例规格新建连接上限，其中-1表示关闭监听器粒度新建连接数限速。
        :type MaxCps: int
        :param _IdleConnectTimeout: 空闲连接超时时间，此参数仅适用于TCP监听器，单位：秒。默认值：900，取值范围：共享型实例和独占型实例支持：300～900，性能容量型实例支持：300~2000。如需设置超过2000s，请通过 [工单申请](https://console.cloud.tencent.com/workorder/category),最大可设置到3600s。
        :type IdleConnectTimeout: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._ListenerName = None
        self._SessionExpireTime = None
        self._HealthCheck = None
        self._Certificate = None
        self._Scheduler = None
        self._SniSwitch = None
        self._TargetType = None
        self._KeepaliveEnable = None
        self._DeregisterTargetRst = None
        self._SessionType = None
        self._MultiCertInfo = None
        self._MaxConn = None
        self._MaxCps = None
        self._IdleConnectTimeout = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def KeepaliveEnable(self):
        return self._KeepaliveEnable

    @KeepaliveEnable.setter
    def KeepaliveEnable(self, KeepaliveEnable):
        self._KeepaliveEnable = KeepaliveEnable

    @property
    def DeregisterTargetRst(self):
        return self._DeregisterTargetRst

    @DeregisterTargetRst.setter
    def DeregisterTargetRst(self, DeregisterTargetRst):
        self._DeregisterTargetRst = DeregisterTargetRst

    @property
    def SessionType(self):
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def MultiCertInfo(self):
        return self._MultiCertInfo

    @MultiCertInfo.setter
    def MultiCertInfo(self, MultiCertInfo):
        self._MultiCertInfo = MultiCertInfo

    @property
    def MaxConn(self):
        return self._MaxConn

    @MaxConn.setter
    def MaxConn(self, MaxConn):
        self._MaxConn = MaxConn

    @property
    def MaxCps(self):
        return self._MaxCps

    @MaxCps.setter
    def MaxCps(self, MaxCps):
        self._MaxCps = MaxCps

    @property
    def IdleConnectTimeout(self):
        return self._IdleConnectTimeout

    @IdleConnectTimeout.setter
    def IdleConnectTimeout(self, IdleConnectTimeout):
        self._IdleConnectTimeout = IdleConnectTimeout


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._Scheduler = params.get("Scheduler")
        self._SniSwitch = params.get("SniSwitch")
        self._TargetType = params.get("TargetType")
        self._KeepaliveEnable = params.get("KeepaliveEnable")
        self._DeregisterTargetRst = params.get("DeregisterTargetRst")
        self._SessionType = params.get("SessionType")
        if params.get("MultiCertInfo") is not None:
            self._MultiCertInfo = MultiCertInfo()
            self._MultiCertInfo._deserialize(params.get("MultiCertInfo"))
        self._MaxConn = params.get("MaxConn")
        self._MaxCps = params.get("MaxCps")
        self._IdleConnectTimeout = params.get("IdleConnectTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    """ModifyListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡的唯一ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例名称
        :type LoadBalancerName: str
        :param _TargetRegionInfo: 设置负载均衡跨地域绑定1.0的后端服务信息
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param _InternetChargeInfo: 网络计费相关参数
        :type InternetChargeInfo: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _LoadBalancerPassToTarget: Target是否放通来自CLB的流量。开启放通（true）：只验证CLB上的安全组；不开启放通（false）：需同时验证CLB和后端实例上的安全组。
        :type LoadBalancerPassToTarget: bool
        :param _SnatPro: 是否开启跨地域绑定2.0功能
        :type SnatPro: bool
        :param _DeleteProtect: 是否开启删除保护
        :type DeleteProtect: bool
        :param _ModifyClassicDomain: 将负载均衡二级域名由mycloud.com改为tencentclb.com，子域名也会变换。修改后mycloud.com域名将失效。
        :type ModifyClassicDomain: bool
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._TargetRegionInfo = None
        self._InternetChargeInfo = None
        self._LoadBalancerPassToTarget = None
        self._SnatPro = None
        self._DeleteProtect = None
        self._ModifyClassicDomain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def TargetRegionInfo(self):
        return self._TargetRegionInfo

    @TargetRegionInfo.setter
    def TargetRegionInfo(self, TargetRegionInfo):
        self._TargetRegionInfo = TargetRegionInfo

    @property
    def InternetChargeInfo(self):
        return self._InternetChargeInfo

    @InternetChargeInfo.setter
    def InternetChargeInfo(self, InternetChargeInfo):
        self._InternetChargeInfo = InternetChargeInfo

    @property
    def LoadBalancerPassToTarget(self):
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def SnatPro(self):
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def DeleteProtect(self):
        return self._DeleteProtect

    @DeleteProtect.setter
    def DeleteProtect(self, DeleteProtect):
        self._DeleteProtect = DeleteProtect

    @property
    def ModifyClassicDomain(self):
        return self._ModifyClassicDomain

    @ModifyClassicDomain.setter
    def ModifyClassicDomain(self, ModifyClassicDomain):
        self._ModifyClassicDomain = ModifyClassicDomain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("TargetRegionInfo") is not None:
            self._TargetRegionInfo = TargetRegionInfo()
            self._TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        if params.get("InternetChargeInfo") is not None:
            self._InternetChargeInfo = InternetAccessible()
            self._InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self._SnatPro = params.get("SnatPro")
        self._DeleteProtect = params.get("DeleteProtect")
        self._ModifyClassicDomain = params.get("ModifyClassicDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 切换负载均衡计费方式时，可用此参数查询切换任务是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerMixIpTargetRequest(AbstractModel):
    """ModifyLoadBalancerMixIpTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 负载均衡实例ID数组。
        :type LoadBalancerIds: list of str
        :param _MixIpTarget: 开启/关闭IPv6FullChain负载均衡7层监听器支持混绑IPv4/IPv6目标特性。
        :type MixIpTarget: bool
        """
        self._LoadBalancerIds = None
        self._MixIpTarget = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def MixIpTarget(self):
        return self._MixIpTarget

    @MixIpTarget.setter
    def MixIpTarget(self, MixIpTarget):
        self._MixIpTarget = MixIpTarget


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._MixIpTarget = params.get("MixIpTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerMixIpTargetResponse(AbstractModel):
    """ModifyLoadBalancerMixIpTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerSlaRequest(AbstractModel):
    """ModifyLoadBalancerSla请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerSla: 负载均衡实例信息。
        :type LoadBalancerSla: list of SlaUpdateParam
        :param _Force: 是否强制升级，默认否。
        :type Force: bool
        """
        self._LoadBalancerSla = None
        self._Force = None

    @property
    def LoadBalancerSla(self):
        return self._LoadBalancerSla

    @LoadBalancerSla.setter
    def LoadBalancerSla(self, LoadBalancerSla):
        self._LoadBalancerSla = LoadBalancerSla

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        if params.get("LoadBalancerSla") is not None:
            self._LoadBalancerSla = []
            for item in params.get("LoadBalancerSla"):
                obj = SlaUpdateParam()
                obj._deserialize(item)
                self._LoadBalancerSla.append(obj)
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerSlaResponse(AbstractModel):
    """ModifyLoadBalancerSla返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancersProjectRequest(AbstractModel):
    """ModifyLoadBalancersProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 一个或多个待操作的负载均衡实例ID。
        :type LoadBalancerIds: list of str
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        """
        self._LoadBalancerIds = None
        self._ProjectId = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancersProjectResponse(AbstractModel):
    """ModifyLoadBalancersProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器 ID。
        :type ListenerId: str
        :param _LocationId: 要修改的转发规则的 ID。
        :type LocationId: str
        :param _Url: 转发规则的新的转发路径，如不需修改Url，则不需提供此参数。
        :type Url: str
        :param _HealthCheck: 健康检查信息。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Scheduler: 规则的请求转发方式，可选值：WRR、LEAST_CONN、IP_HASH
分别表示按权重轮询、最小连接数、按IP哈希， 默认为 WRR。
        :type Scheduler: str
        :param _SessionExpireTime: 会话保持时间。
        :type SessionExpireTime: int
        :param _ForwardType: 负载均衡实例与后端服务之间的转发协议，默认HTTP，可取值：HTTP、HTTPS、TRPC。
        :type ForwardType: str
        :param _TrpcCallee: TRPC被调服务器路由，ForwardType为TRPC时必填。目前暂未对外开放。
        :type TrpcCallee: str
        :param _TrpcFunc: TRPC调用服务接口，ForwardType为TRPC时必填。目前暂未对外开放。
        :type TrpcFunc: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationId = None
        self._Url = None
        self._HealthCheck = None
        self._Scheduler = None
        self._SessionExpireTime = None
        self._ForwardType = None
        self._TrpcCallee = None
        self._TrpcFunc = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def ForwardType(self):
        return self._ForwardType

    @ForwardType.setter
    def ForwardType(self, ForwardType):
        self._ForwardType = ForwardType

    @property
    def TrpcCallee(self):
        return self._TrpcCallee

    @TrpcCallee.setter
    def TrpcCallee(self, TrpcCallee):
        self._TrpcCallee = TrpcCallee

    @property
    def TrpcFunc(self):
        return self._TrpcFunc

    @TrpcFunc.setter
    def TrpcFunc(self, TrpcFunc):
        self._TrpcFunc = TrpcFunc


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        self._Url = params.get("Url")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._Scheduler = params.get("Scheduler")
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._ForwardType = params.get("ForwardType")
        self._TrpcCallee = params.get("TrpcCallee")
        self._TrpcFunc = params.get("TrpcFunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetGroupAttributeRequest(AbstractModel):
    """ModifyTargetGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组的ID。
        :type TargetGroupId: str
        :param _TargetGroupName: 目标组的新名称。
        :type TargetGroupName: str
        :param _Port: 目标组的新默认端口。
        :type Port: int
        """
        self._TargetGroupId = None
        self._TargetGroupName = None
        self._Port = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupAttributeResponse(AbstractModel):
    """ModifyTargetGroupAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesPortRequest(AbstractModel):
    """ModifyTargetGroupInstancesPort请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        :param _TargetGroupInstances: 待修改端口的服务器数组。
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupInstancesPortResponse(AbstractModel):
    """ModifyTargetGroupInstancesPort返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesWeightRequest(AbstractModel):
    """ModifyTargetGroupInstancesWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        :param _TargetGroupInstances: 待修改权重的服务器数组。
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupInstancesWeightResponse(AbstractModel):
    """ModifyTargetGroupInstancesWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param _Targets: 要修改端口的后端服务列表。
        :type Targets: list of Target
        :param _NewPort: 后端服务绑定到监听器或转发规则的新端口。
        :type NewPort: int
        :param _LocationId: 转发规则的ID，当后端服务绑定到七层转发规则时，必须提供此参数或Domain+Url两者之一。
        :type LocationId: str
        :param _Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param _Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._NewPort = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def NewPort(self):
        return self._NewPort

    @NewPort.setter
    def NewPort(self, NewPort):
        self._NewPort = NewPort

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._NewPort = params.get("NewPort")
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param _LocationId: 转发规则的ID，当绑定机器到七层转发规则时，必须提供此参数或Domain+Url两者之一。
        :type LocationId: str
        :param _Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param _Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        :param _Targets: 要修改权重的后端服务列表。
        :type Targets: list of Target
        :param _Weight: 后端服务新的转发权重，取值范围：0~100，默认值10。如果设置了 Targets.Weight 参数，则此参数不生效。
        :type Weight: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Targets = None
        self._Weight = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MultiCertInfo(AbstractModel):
    """CLB监听器或规则绑定的多证书信息

    """

    def __init__(self):
        r"""
        :param _SSLMode: 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证
        :type SSLMode: str
        :param _CertList: 监听器或规则证书列表，单双向认证，多本服务端证书算法类型不能重复;若SSLMode为双向认证，证书列表必须包含一本ca证书。
        :type CertList: list of CertInfo
        """
        self._SSLMode = None
        self._CertList = None

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertList(self):
        return self._CertList

    @CertList.setter
    def CertList(self, CertList):
        self._CertList = CertList


    def _deserialize(self, params):
        self._SSLMode = params.get("SSLMode")
        if params.get("CertList") is not None:
            self._CertList = []
            for item in params.get("CertList"):
                obj = CertInfo()
                obj._deserialize(item)
                self._CertList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """表示负载均衡的价格

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 描述了实例价格。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancePrice: :class:`tencentcloud.clb.v20180317.models.ItemPrice`
        :param _BandwidthPrice: 描述了网络价格。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthPrice: :class:`tencentcloud.clb.v20180317.models.ItemPrice`
        :param _LcuPrice: 描述了lcu价格。
注意：此字段可能返回 null，表示取不到有效值。
        :type LcuPrice: :class:`tencentcloud.clb.v20180317.models.ItemPrice`
        """
        self._InstancePrice = None
        self._BandwidthPrice = None
        self._LcuPrice = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def BandwidthPrice(self):
        return self._BandwidthPrice

    @BandwidthPrice.setter
    def BandwidthPrice(self, BandwidthPrice):
        self._BandwidthPrice = BandwidthPrice

    @property
    def LcuPrice(self):
        return self._LcuPrice

    @LcuPrice.setter
    def LcuPrice(self, LcuPrice):
        self._LcuPrice = LcuPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self._BandwidthPrice = ItemPrice()
            self._BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        if params.get("LcuPrice") is not None:
            self._LcuPrice = ItemPrice()
            self._LcuPrice._deserialize(params.get("LcuPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """描述配额信息，所有配额均指当前地域下的配额。

    """

    def __init__(self):
        r"""
        :param _QuotaId: 配额名称，取值范围：
<li> TOTAL_OPEN_CLB_QUOTA：用户当前地域下的公网CLB配额 </li>
<li> TOTAL_INTERNAL_CLB_QUOTA：用户当前地域下的内网CLB配额 </li>
<li> TOTAL_LISTENER_QUOTA：一个CLB下的监听器配额 </li>
<li> TOTAL_LISTENER_RULE_QUOTA：一个监听器下的转发规则配额 </li>
<li> TOTAL_TARGET_BIND_QUOTA：一条转发规则下可绑定设备的配额 </li>
<li> TOTAL_SNAP_IP_QUOTA： 一个CLB实例下跨地域2.0的SNAT IP配额 </li>
<li>TOTAL_ISP_CLB_QUOTA：用户当前地域下的三网CLB配额 </li>
        :type QuotaId: str
        :param _QuotaCurrent: 当前使用数量，为 null 时表示无意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaCurrent: int
        :param _QuotaLimit: 配额数量。
        :type QuotaLimit: int
        """
        self._QuotaId = None
        self._QuotaCurrent = None
        self._QuotaLimit = None

    @property
    def QuotaId(self):
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def QuotaCurrent(self):
        return self._QuotaCurrent

    @QuotaCurrent.setter
    def QuotaCurrent(self, QuotaCurrent):
        self._QuotaCurrent = QuotaCurrent

    @property
    def QuotaLimit(self):
        return self._QuotaLimit

    @QuotaLimit.setter
    def QuotaLimit(self, QuotaLimit):
        self._QuotaLimit = QuotaLimit


    def _deserialize(self, params):
        self._QuotaId = params.get("QuotaId")
        self._QuotaCurrent = params.get("QuotaCurrent")
        self._QuotaLimit = params.get("QuotaLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterFunctionTargetsRequest(AbstractModel):
    """RegisterFunctionTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器 ID。
        :type ListenerId: str
        :param _FunctionTargets: 待绑定的云函数列表。
        :type FunctionTargets: list of FunctionTarget
        :param _LocationId: 目标转发规则的 ID，当将云函数绑定到七层转发规则时，必须输入此参数或 Domain+Url 参数。
        :type LocationId: str
        :param _Domain: 目标转发规则的域名，若已经输入 LocationId 参数，则本参数不生效。
        :type Domain: str
        :param _Url: 目标转发规则的 URL，若已经输入 LocationId 参数，则本参数不生效。
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._FunctionTargets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def FunctionTargets(self):
        return self._FunctionTargets

    @FunctionTargets.setter
    def FunctionTargets(self, FunctionTargets):
        self._FunctionTargets = FunctionTargets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("FunctionTargets") is not None:
            self._FunctionTargets = []
            for item in params.get("FunctionTargets"):
                obj = FunctionTarget()
                obj._deserialize(item)
                self._FunctionTargets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterFunctionTargetsResponse(AbstractModel):
    """RegisterFunctionTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RegisterTargetGroupInstancesRequest(AbstractModel):
    """RegisterTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param _TargetGroupInstances: 服务器实例数组
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetGroupInstancesResponse(AbstractModel):
    """RegisterTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RegisterTargetsRequest(AbstractModel):
    """RegisterTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param _Targets: 待绑定的后端服务列表，数组长度最大支持20。
        :type Targets: list of Target
        :param _LocationId: 转发规则的ID，当绑定后端服务到七层转发规则时，必须提供此参数或Domain+Url两者之一。
        :type LocationId: str
        :param _Domain: 目标转发规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param _Url: 目标转发规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetsResponse(AbstractModel):
    """RegisterTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RegisterTargetsWithClassicalLBRequest(AbstractModel):
    """RegisterTargetsWithClassicalLB请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param _Targets: 后端服务信息。
        :type Targets: list of ClassicalTargetInfo
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTargetInfo()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetsWithClassicalLBResponse(AbstractModel):
    """RegisterTargetsWithClassicalLB返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReplaceCertForLoadBalancersRequest(AbstractModel):
    """ReplaceCertForLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OldCertificateId: 需要被替换的证书的ID，可以是服务端证书或客户端证书
        :type OldCertificateId: str
        :param _Certificate: 新证书的内容等相关信息
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        """
        self._OldCertificateId = None
        self._Certificate = None

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate


    def _deserialize(self, params):
        self._OldCertificateId = params.get("OldCertificateId")
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertForLoadBalancersResponse(AbstractModel):
    """ReplaceCertForLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """资源详细信息

    """

    def __init__(self):
        r"""
        :param _Type: 运营商内具体资源信息，如"CMCC", "CUCC", "CTCC", "BGP", "INTERNAL"。
        :type Type: list of str
        :param _Isp: 运营商信息，如"CMCC", "CUCC", "CTCC", "BGP", "INTERNAL"。
        :type Isp: str
        :param _AvailabilitySet: 可用资源。
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailabilitySet: list of ResourceAvailability
        :param _TypeSet: 运营商类型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeSet: list of TypeInfo
        """
        self._Type = None
        self._Isp = None
        self._AvailabilitySet = None
        self._TypeSet = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def AvailabilitySet(self):
        return self._AvailabilitySet

    @AvailabilitySet.setter
    def AvailabilitySet(self, AvailabilitySet):
        self._AvailabilitySet = AvailabilitySet

    @property
    def TypeSet(self):
        return self._TypeSet

    @TypeSet.setter
    def TypeSet(self, TypeSet):
        self._TypeSet = TypeSet


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Isp = params.get("Isp")
        if params.get("AvailabilitySet") is not None:
            self._AvailabilitySet = []
            for item in params.get("AvailabilitySet"):
                obj = ResourceAvailability()
                obj._deserialize(item)
                self._AvailabilitySet.append(obj)
        if params.get("TypeSet") is not None:
            self._TypeSet = []
            for item in params.get("TypeSet"):
                obj = TypeInfo()
                obj._deserialize(item)
                self._TypeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceAvailability(AbstractModel):
    """资源可用性

    """

    def __init__(self):
        r"""
        :param _Type: 运营商内具体资源信息，如"CMCC", "CUCC", "CTCC", "BGP"。
        :type Type: str
        :param _Availability: 资源可用性，"Available"：可用，"Unavailable"：不可用
        :type Availability: str
        """
        self._Type = None
        self._Availability = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Availability(self):
        return self._Availability

    @Availability.setter
    def Availability(self, Availability):
        self._Availability = Availability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Availability = params.get("Availability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteLocationMap(AbstractModel):
    """转发规则之间的重定向关系

    """

    def __init__(self):
        r"""
        :param _SourceLocationId: 源转发规则ID
        :type SourceLocationId: str
        :param _TargetLocationId: 重定向目标转发规则的ID
        :type TargetLocationId: str
        :param _RewriteCode: 重定向状态码，可取值301,302,307
        :type RewriteCode: int
        :param _TakeUrl: 重定向是否携带匹配的url，配置RewriteCode时必填
        :type TakeUrl: bool
        :param _SourceDomain: 源转发的域名，必须是SourceLocationId对应的域名，配置RewriteCode时必填
        :type SourceDomain: str
        """
        self._SourceLocationId = None
        self._TargetLocationId = None
        self._RewriteCode = None
        self._TakeUrl = None
        self._SourceDomain = None

    @property
    def SourceLocationId(self):
        return self._SourceLocationId

    @SourceLocationId.setter
    def SourceLocationId(self, SourceLocationId):
        self._SourceLocationId = SourceLocationId

    @property
    def TargetLocationId(self):
        return self._TargetLocationId

    @TargetLocationId.setter
    def TargetLocationId(self, TargetLocationId):
        self._TargetLocationId = TargetLocationId

    @property
    def RewriteCode(self):
        return self._RewriteCode

    @RewriteCode.setter
    def RewriteCode(self, RewriteCode):
        self._RewriteCode = RewriteCode

    @property
    def TakeUrl(self):
        return self._TakeUrl

    @TakeUrl.setter
    def TakeUrl(self, TakeUrl):
        self._TakeUrl = TakeUrl

    @property
    def SourceDomain(self):
        return self._SourceDomain

    @SourceDomain.setter
    def SourceDomain(self, SourceDomain):
        self._SourceDomain = SourceDomain


    def _deserialize(self, params):
        self._SourceLocationId = params.get("SourceLocationId")
        self._TargetLocationId = params.get("TargetLocationId")
        self._RewriteCode = params.get("RewriteCode")
        self._TakeUrl = params.get("TakeUrl")
        self._SourceDomain = params.get("SourceDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteTarget(AbstractModel):
    """重定向目标的信息

    """

    def __init__(self):
        r"""
        :param _TargetListenerId: 重定向目标的监听器ID
注意：此字段可能返回 null，表示无重定向。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetListenerId: str
        :param _TargetLocationId: 重定向目标的转发规则ID
注意：此字段可能返回 null，表示无重定向。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetLocationId: str
        :param _RewriteCode: 重定向状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteCode: int
        :param _TakeUrl: 重定向是否携带匹配的url
注意：此字段可能返回 null，表示取不到有效值。
        :type TakeUrl: bool
        :param _RewriteType: 重定向类型，Manual: 手动重定向，Auto:  自动重定向
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteType: str
        """
        self._TargetListenerId = None
        self._TargetLocationId = None
        self._RewriteCode = None
        self._TakeUrl = None
        self._RewriteType = None

    @property
    def TargetListenerId(self):
        return self._TargetListenerId

    @TargetListenerId.setter
    def TargetListenerId(self, TargetListenerId):
        self._TargetListenerId = TargetListenerId

    @property
    def TargetLocationId(self):
        return self._TargetLocationId

    @TargetLocationId.setter
    def TargetLocationId(self, TargetLocationId):
        self._TargetLocationId = TargetLocationId

    @property
    def RewriteCode(self):
        return self._RewriteCode

    @RewriteCode.setter
    def RewriteCode(self, RewriteCode):
        self._RewriteCode = RewriteCode

    @property
    def TakeUrl(self):
        return self._TakeUrl

    @TakeUrl.setter
    def TakeUrl(self, TakeUrl):
        self._TakeUrl = TakeUrl

    @property
    def RewriteType(self):
        return self._RewriteType

    @RewriteType.setter
    def RewriteType(self, RewriteType):
        self._RewriteType = RewriteType


    def _deserialize(self, params):
        self._TargetListenerId = params.get("TargetListenerId")
        self._TargetLocationId = params.get("TargetLocationId")
        self._RewriteCode = params.get("RewriteCode")
        self._TakeUrl = params.get("TakeUrl")
        self._RewriteType = params.get("RewriteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RsTagRule(AbstractModel):
    """修改节点标签的数据类型

    """

    def __init__(self):
        r"""
        :param _ListenerId: 负载均衡监听器 ID。
        :type ListenerId: str
        :param _Targets: 要修改标签的后端机器列表。
        :type Targets: list of Target
        :param _LocationId: 转发规则的ID，七层规则时需要此参数，4层规则不需要。
        :type LocationId: str
        :param _Tag: 后端服务修改后的标签。此参数的优先级低于前述[Target](https://cloud.tencent.com/document/api/214/30694#Target)中的Tag参数，即最终的标签以Target中的Tag参数值为准，仅当Target中的Weight参数为空时，才以RsTagRule中的Tag参数为准。
        :type Tag: str
        """
        self._ListenerId = None
        self._Targets = None
        self._LocationId = None
        self._Tag = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RsWeightRule(AbstractModel):
    """修改节点权重的数据类型

    """

    def __init__(self):
        r"""
        :param _ListenerId: 负载均衡监听器 ID。
        :type ListenerId: str
        :param _Targets: 要修改权重的后端机器列表。
        :type Targets: list of Target
        :param _LocationId: 转发规则的ID，七层规则时需要此参数，4层规则不需要。
        :type LocationId: str
        :param _Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param _Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        :param _Weight: 后端服务修改后的转发权重，取值范围：[0，100]。此参数的优先级低于前述[Target](https://cloud.tencent.com/document/api/214/30694#Target)中的Weight参数，即最终的权重值以Target中的Weight参数值为准，仅当Target中的Weight参数为空时，才以RsWeightRule中的Weight参数为准。
        :type Weight: int
        """
        self._ListenerId = None
        self._Targets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Weight = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHealth(AbstractModel):
    """一条转发规则的健康检查状态

    """

    def __init__(self):
        r"""
        :param _LocationId: 转发规则ID
        :type LocationId: str
        :param _Domain: 转发规则的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Url: 转发规则的Url
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Targets: 本规则上绑定的后端服务的健康检查状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of TargetHealth
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Targets = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInput(AbstractModel):
    """HTTP/HTTPS转发规则（输入）

    """

    def __init__(self):
        r"""
        :param _Url: 转发规则的路径。长度限制为：1~200。
        :type Url: str
        :param _Domain: 转发规则的域名。长度限制为：1~80。Domain和Domains只需要传一个，单域名规则传Domain，多域名规则传Domains。
        :type Domain: str
        :param _SessionExpireTime: 会话保持时间。设置为0表示关闭会话保持，开启会话保持可取值30~3600，单位：秒。
        :type SessionExpireTime: int
        :param _HealthCheck: 健康检查信息。详情请参见：[健康检查](https://cloud.tencent.com/document/product/214/6097)
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Certificate: 证书信息；此参数和MultiCertInfo不能同时传入。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param _Scheduler: 规则的请求转发方式，可选值：WRR、LEAST_CONN、IP_HASH
分别表示按权重轮询、最小连接数、按IP哈希， 默认为 WRR。
        :type Scheduler: str
        :param _ForwardType: 负载均衡与后端服务之间的转发协议，目前支持 HTTP/HTTPS/GRPC/TRPC，TRPC暂未对外开放，默认HTTP。
        :type ForwardType: str
        :param _DefaultServer: 是否将该域名设为默认域名，注意，一个监听器下只能设置一个默认域名。
        :type DefaultServer: bool
        :param _Http2: 是否开启Http2，注意，只有HTTPS域名才能开启Http2。
        :type Http2: bool
        :param _TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组
        :type TargetType: str
        :param _TrpcCallee: TRPC被调服务器路由，ForwardType为TRPC时必填。目前暂未对外开放。
        :type TrpcCallee: str
        :param _TrpcFunc: TRPC调用服务接口，ForwardType为TRPC时必填。目前暂未对外开放
        :type TrpcFunc: str
        :param _Quic: 是否开启QUIC，注意，只有HTTPS域名才能开启QUIC
        :type Quic: bool
        :param _Domains: 转发规则的域名列表。每个域名的长度限制为：1~80。Domain和Domains只需要传一个，单域名规则传Domain，多域名规则传Domains。
        :type Domains: list of str
        :param _MultiCertInfo: 证书信息，支持同时传入不同算法类型的多本服务端证书；此参数和Certificate不能同时传入。
        :type MultiCertInfo: :class:`tencentcloud.clb.v20180317.models.MultiCertInfo`
        """
        self._Url = None
        self._Domain = None
        self._SessionExpireTime = None
        self._HealthCheck = None
        self._Certificate = None
        self._Scheduler = None
        self._ForwardType = None
        self._DefaultServer = None
        self._Http2 = None
        self._TargetType = None
        self._TrpcCallee = None
        self._TrpcFunc = None
        self._Quic = None
        self._Domains = None
        self._MultiCertInfo = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def ForwardType(self):
        return self._ForwardType

    @ForwardType.setter
    def ForwardType(self, ForwardType):
        self._ForwardType = ForwardType

    @property
    def DefaultServer(self):
        return self._DefaultServer

    @DefaultServer.setter
    def DefaultServer(self, DefaultServer):
        self._DefaultServer = DefaultServer

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TrpcCallee(self):
        return self._TrpcCallee

    @TrpcCallee.setter
    def TrpcCallee(self, TrpcCallee):
        self._TrpcCallee = TrpcCallee

    @property
    def TrpcFunc(self):
        return self._TrpcFunc

    @TrpcFunc.setter
    def TrpcFunc(self, TrpcFunc):
        self._TrpcFunc = TrpcFunc

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def MultiCertInfo(self):
        return self._MultiCertInfo

    @MultiCertInfo.setter
    def MultiCertInfo(self, MultiCertInfo):
        self._MultiCertInfo = MultiCertInfo


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Domain = params.get("Domain")
        self._SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._Scheduler = params.get("Scheduler")
        self._ForwardType = params.get("ForwardType")
        self._DefaultServer = params.get("DefaultServer")
        self._Http2 = params.get("Http2")
        self._TargetType = params.get("TargetType")
        self._TrpcCallee = params.get("TrpcCallee")
        self._TrpcFunc = params.get("TrpcFunc")
        self._Quic = params.get("Quic")
        self._Domains = params.get("Domains")
        if params.get("MultiCertInfo") is not None:
            self._MultiCertInfo = MultiCertInfo()
            self._MultiCertInfo._deserialize(params.get("MultiCertInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleOutput(AbstractModel):
    """HTTP/HTTPS监听器的转发规则（输出）

    """

    def __init__(self):
        r"""
        :param _LocationId: 转发规则的 ID
        :type LocationId: str
        :param _Domain: 转发规则的域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Url: 转发规则的路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _SessionExpireTime: 会话保持时间
        :type SessionExpireTime: int
        :param _HealthCheck: 健康检查信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Certificate: 证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param _Scheduler: 规则的请求转发方式
        :type Scheduler: str
        :param _ListenerId: 转发规则所属的监听器 ID
        :type ListenerId: str
        :param _RewriteTarget: 转发规则的重定向目标信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteTarget: :class:`tencentcloud.clb.v20180317.models.RewriteTarget`
        :param _HttpGzip: 是否开启gzip
        :type HttpGzip: bool
        :param _BeAutoCreated: 转发规则是否为自动创建
        :type BeAutoCreated: bool
        :param _DefaultServer: 是否作为默认域名
        :type DefaultServer: bool
        :param _Http2: 是否开启Http2
        :type Http2: bool
        :param _ForwardType: 负载均衡与后端服务之间的转发协议
        :type ForwardType: str
        :param _CreateTime: 转发规则的创建时间
        :type CreateTime: str
        :param _TargetType: 后端服务器类型
        :type TargetType: str
        :param _TargetGroup: 绑定的目标组基本信息；当规则绑定目标组时，会返回该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param _WafDomainId: WAF实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WafDomainId: str
        :param _TrpcCallee: TRPC被调服务器路由，ForwardType为TRPC时有效。目前暂未对外开放。
注意：此字段可能返回 null，表示取不到有效值。
        :type TrpcCallee: str
        :param _TrpcFunc: TRPC调用服务接口，ForwardType为TRPC时有效。目前暂未对外开放。
注意：此字段可能返回 null，表示取不到有效值。
        :type TrpcFunc: str
        :param _QuicStatus: QUIC状态
注意：此字段可能返回 null，表示取不到有效值。
        :type QuicStatus: str
        :param _Domains: 转发规则的域名列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of str
        :param _TargetGroupList: 绑定的目标组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetGroupList: list of BasicTargetGroupInfo
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._SessionExpireTime = None
        self._HealthCheck = None
        self._Certificate = None
        self._Scheduler = None
        self._ListenerId = None
        self._RewriteTarget = None
        self._HttpGzip = None
        self._BeAutoCreated = None
        self._DefaultServer = None
        self._Http2 = None
        self._ForwardType = None
        self._CreateTime = None
        self._TargetType = None
        self._TargetGroup = None
        self._WafDomainId = None
        self._TrpcCallee = None
        self._TrpcFunc = None
        self._QuicStatus = None
        self._Domains = None
        self._TargetGroupList = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RewriteTarget(self):
        return self._RewriteTarget

    @RewriteTarget.setter
    def RewriteTarget(self, RewriteTarget):
        self._RewriteTarget = RewriteTarget

    @property
    def HttpGzip(self):
        return self._HttpGzip

    @HttpGzip.setter
    def HttpGzip(self, HttpGzip):
        self._HttpGzip = HttpGzip

    @property
    def BeAutoCreated(self):
        return self._BeAutoCreated

    @BeAutoCreated.setter
    def BeAutoCreated(self, BeAutoCreated):
        self._BeAutoCreated = BeAutoCreated

    @property
    def DefaultServer(self):
        return self._DefaultServer

    @DefaultServer.setter
    def DefaultServer(self, DefaultServer):
        self._DefaultServer = DefaultServer

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def ForwardType(self):
        return self._ForwardType

    @ForwardType.setter
    def ForwardType(self, ForwardType):
        self._ForwardType = ForwardType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetGroup(self):
        return self._TargetGroup

    @TargetGroup.setter
    def TargetGroup(self, TargetGroup):
        self._TargetGroup = TargetGroup

    @property
    def WafDomainId(self):
        return self._WafDomainId

    @WafDomainId.setter
    def WafDomainId(self, WafDomainId):
        self._WafDomainId = WafDomainId

    @property
    def TrpcCallee(self):
        return self._TrpcCallee

    @TrpcCallee.setter
    def TrpcCallee(self, TrpcCallee):
        self._TrpcCallee = TrpcCallee

    @property
    def TrpcFunc(self):
        return self._TrpcFunc

    @TrpcFunc.setter
    def TrpcFunc(self, TrpcFunc):
        self._TrpcFunc = TrpcFunc

    @property
    def QuicStatus(self):
        return self._QuicStatus

    @QuicStatus.setter
    def QuicStatus(self, QuicStatus):
        self._QuicStatus = QuicStatus

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TargetGroupList(self):
        return self._TargetGroupList

    @TargetGroupList.setter
    def TargetGroupList(self, TargetGroupList):
        self._TargetGroupList = TargetGroupList


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self._Certificate = CertificateOutput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._Scheduler = params.get("Scheduler")
        self._ListenerId = params.get("ListenerId")
        if params.get("RewriteTarget") is not None:
            self._RewriteTarget = RewriteTarget()
            self._RewriteTarget._deserialize(params.get("RewriteTarget"))
        self._HttpGzip = params.get("HttpGzip")
        self._BeAutoCreated = params.get("BeAutoCreated")
        self._DefaultServer = params.get("DefaultServer")
        self._Http2 = params.get("Http2")
        self._ForwardType = params.get("ForwardType")
        self._CreateTime = params.get("CreateTime")
        self._TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self._TargetGroup = BasicTargetGroupInfo()
            self._TargetGroup._deserialize(params.get("TargetGroup"))
        self._WafDomainId = params.get("WafDomainId")
        self._TrpcCallee = params.get("TrpcCallee")
        self._TrpcFunc = params.get("TrpcFunc")
        self._QuicStatus = params.get("QuicStatus")
        self._Domains = params.get("Domains")
        if params.get("TargetGroupList") is not None:
            self._TargetGroupList = []
            for item in params.get("TargetGroupList"):
                obj = BasicTargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTargets(AbstractModel):
    """HTTP/HTTPS监听器下的转发规则绑定的后端服务信息

    """

    def __init__(self):
        r"""
        :param _LocationId: 转发规则的 ID
        :type LocationId: str
        :param _Domain: 转发规则的域名
        :type Domain: str
        :param _Url: 转发规则的路径。
        :type Url: str
        :param _Targets: 后端服务的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of Backend
        :param _FunctionTargets: 后端云函数的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionTargets: list of FunctionTarget
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Targets = None
        self._FunctionTargets = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def FunctionTargets(self):
        return self._FunctionTargets

    @FunctionTargets.setter
    def FunctionTargets(self, FunctionTargets):
        self._FunctionTargets = FunctionTargets


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self._Targets.append(obj)
        if params.get("FunctionTargets") is not None:
            self._FunctionTargets = []
            for item in params.get("FunctionTargets"):
                obj = FunctionTarget()
                obj._deserialize(item)
                self._FunctionTargets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesItems(AbstractModel):
    """七层规则对象

    """

    def __init__(self):
        r"""
        :param _LocationId: 规则id
        :type LocationId: str
        :param _Domain: 域名
        :type Domain: str
        :param _Url: uri
        :type Url: str
        :param _Targets: 绑定的后端对象
        :type Targets: list of LbRsTargets
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Targets = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = LbRsTargets()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCustomizedConfigForLoadBalancerRequest(AbstractModel):
    """SetCustomizedConfigForLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationType: 操作类型：'ADD', 'DELETE', 'UPDATE', 'BIND', 'UNBIND'
        :type OperationType: str
        :param _UconfigId: 除了创建个性化配置外，必传此字段，如：pz-1234abcd
        :type UconfigId: str
        :param _ConfigContent: 创建个性化配置或修改个性化配置的内容时，必传此字段
        :type ConfigContent: str
        :param _ConfigName: 创建个性化配置或修改个性化配置的名字时，必传此字段
        :type ConfigName: str
        :param _LoadBalancerIds: 绑定解绑时，必传此字段
        :type LoadBalancerIds: list of str
        """
        self._OperationType = None
        self._UconfigId = None
        self._ConfigContent = None
        self._ConfigName = None
        self._LoadBalancerIds = None

    @property
    def OperationType(self):
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def UconfigId(self):
        return self._UconfigId

    @UconfigId.setter
    def UconfigId(self, UconfigId):
        self._UconfigId = UconfigId

    @property
    def ConfigContent(self):
        return self._ConfigContent

    @ConfigContent.setter
    def ConfigContent(self, ConfigContent):
        self._ConfigContent = ConfigContent

    @property
    def ConfigName(self):
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._OperationType = params.get("OperationType")
        self._UconfigId = params.get("UconfigId")
        self._ConfigContent = params.get("ConfigContent")
        self._ConfigName = params.get("ConfigName")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCustomizedConfigForLoadBalancerResponse(AbstractModel):
    """SetCustomizedConfigForLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 个性化配置ID，如：pz-1234abcd
        :type ConfigId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigId = None
        self._RequestId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._RequestId = params.get("RequestId")


class SetLoadBalancerClsLogRequest(AbstractModel):
    """SetLoadBalancerClsLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _LogSetId: 日志服务(CLS)的日志集 ID。
<li>增加和更新日志主题时可调用 [DescribeLogsets](https://cloud.tencent.com/document/product/614/56454) 接口获取日志集 ID。</li>
<li>删除日志主题时，此参数填写为null即可。</li>
        :type LogSetId: str
        :param _LogTopicId: 日志服务(CLS)的日志主题 ID。
<li>增加和更新日志主题时可调用 [DescribeTopics](https://cloud.tencent.com/document/product/614/58624) 接口获取日志主题 ID。</li>
<li>删除日志主题时，此参数填写为null即可。</li>
        :type LogTopicId: str
        :param _LogType: 日志类型：
<li>ACCESS：访问日志</li>
<li>HEALTH：健康检查日志</li>
默认为ACCESS。
        :type LogType: str
        """
        self._LoadBalancerId = None
        self._LogSetId = None
        self._LogTopicId = None
        self._LogType = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LogSetId = params.get("LogSetId")
        self._LogTopicId = params.get("LogTopicId")
        self._LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerClsLogResponse(AbstractModel):
    """SetLoadBalancerClsLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _SecurityGroups: 安全组ID构成的数组，一个负载均衡实例最多可绑定50个安全组，如果要解绑所有安全组，可不传此参数，或传入空数组。
        :type SecurityGroups: list of str
        """
        self._LoadBalancerId = None
        self._SecurityGroups = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SecurityGroups(self):
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroup: 安全组ID，如 sg-12345678
        :type SecurityGroup: str
        :param _OperationType: ADD 绑定安全组；
DEL 解绑安全组
        :type OperationType: str
        :param _LoadBalancerIds: 负载均衡实例ID数组
        :type LoadBalancerIds: list of str
        """
        self._SecurityGroup = None
        self._OperationType = None
        self._LoadBalancerIds = None

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def OperationType(self):
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._SecurityGroup = params.get("SecurityGroup")
        self._OperationType = params.get("OperationType")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SlaUpdateParam(AbstractModel):
    """升级为性能容量型参数

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: lb的字符串ID
        :type LoadBalancerId: str
        :param _SlaType: 性能容量型规格，取值范围：
<li> SLA：超强型4规格 </li>
<li> clb.c2.medium：标准型规格 </li>
<li> clb.c3.small：高阶型1规格 </li>
<li> clb.c3.medium：高阶型2规格 </li>
<li> clb.c4.small：超强型1规格 </li>
<li> clb.c4.medium：超强型2规格 </li>
<li> clb.c4.large：超强型3规格 </li>
<li> clb.c4.xlarge：超强型4规格 </li>如需了解规格详情，请参见[实例规格对比](https://cloud.tencent.com/document/product/214/84689)
        :type SlaType: str
        """
        self._LoadBalancerId = None
        self._SlaType = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SlaType = params.get("SlaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnatIp(AbstractModel):
    """SnatIp的信息结构

    """

    def __init__(self):
        r"""
        :param _SubnetId: 私有网络子网的唯一性id，如subnet-12345678
        :type SubnetId: str
        :param _Ip: IP地址，如192.168.0.1
        :type Ip: str
        """
        self._SubnetId = None
        self._Ip = None

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecAvailability(AbstractModel):
    """规格可用性

    """

    def __init__(self):
        r"""
        :param _SpecType: 规格类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecType: str
        :param _Availability: 规格可用性
注意：此字段可能返回 null，表示取不到有效值。
        :type Availability: str
        """
        self._SpecType = None
        self._Availability = None

    @property
    def SpecType(self):
        return self._SpecType

    @SpecType.setter
    def SpecType(self, SpecType):
        self._SpecType = SpecType

    @property
    def Availability(self):
        return self._Availability

    @Availability.setter
    def Availability(self, Availability):
        self._Availability = Availability


    def _deserialize(self, params):
        self._SpecType = params.get("SpecType")
        self._Availability = params.get("Availability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """负载均衡的标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Target(AbstractModel):
    """转发目标，即绑定在负载均衡上的后端服务

    """

    def __init__(self):
        r"""
        :param _Port: 后端服务的监听端口。
注意：绑定CVM（云服务器）或ENI（弹性网卡）时必传此参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Type: 后端服务的类型，可取：CVM（云服务器）、ENI（弹性网卡）；作为入参时，目前本参数暂不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _InstanceId: 绑定CVM时需要传入此参数，代表CVM的唯一 ID，可通过 DescribeInstances 接口返回字段中的 InstanceId 字段获取。表示绑定主网卡主IP。
注意：参数 InstanceId、EniIp 有且只能传入其中一个参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Weight: 后端服务修改后的转发权重，取值范围：[0, 100]，默认为 10。此参数的优先级高于[RsWeightRule](https://cloud.tencent.com/document/api/214/30694#RsWeightRule)中的Weight参数，即最终的权重值以此Weight参数值为准，仅当此Weight参数为空时，才以RsWeightRule中的Weight参数为准。
        :type Weight: int
        :param _EniIp: 绑定IP时需要传入此参数，支持弹性网卡的IP和其他内网IP，如果是弹性网卡则必须先绑定至CVM，然后才能绑定到负载均衡实例。
注意：参数 InstanceId、EniIp 有且只能传入其中一个参数。如果绑定双栈IPV6子机，则必须传该参数。如果是跨地域绑定，则必须传该参数，不支持传InstanceId参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type EniIp: str
        :param _Tag: 标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        """
        self._Port = None
        self._Type = None
        self._InstanceId = None
        self._Weight = None
        self._EniIp = None
        self._Tag = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def EniIp(self):
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        self._EniIp = params.get("EniIp")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupAssociation(AbstractModel):
    """规则与目标组的关联关系

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param _TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _LocationId: 转发规则ID
        :type LocationId: str
        """
        self._LoadBalancerId = None
        self._TargetGroupId = None
        self._ListenerId = None
        self._LocationId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._TargetGroupId = params.get("TargetGroupId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupBackend(AbstractModel):
    """目标组绑定的后端服务器

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param _Type: 后端服务的类型，可取：CVM、ENI（即将支持）
        :type Type: str
        :param _InstanceId: 后端服务的唯一 ID
        :type InstanceId: str
        :param _Port: 后端服务的监听端口
        :type Port: int
        :param _Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param _PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param _PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param _InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _RegisteredTime: 后端服务被绑定的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        :param _EniId: 弹性网卡唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EniId: str
        :param _ZoneId: 后端服务的可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        """
        self._TargetGroupId = None
        self._Type = None
        self._InstanceId = None
        self._Port = None
        self._Weight = None
        self._PublicIpAddresses = None
        self._PrivateIpAddresses = None
        self._InstanceName = None
        self._RegisteredTime = None
        self._EniId = None
        self._ZoneId = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegisteredTime(self):
        return self._RegisteredTime

    @RegisteredTime.setter
    def RegisteredTime(self, RegisteredTime):
        self._RegisteredTime = RegisteredTime

    @property
    def EniId(self):
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._InstanceName = params.get("InstanceName")
        self._RegisteredTime = params.get("RegisteredTime")
        self._EniId = params.get("EniId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInfo(AbstractModel):
    """目标组信息

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param _VpcId: 目标组的vpcid
        :type VpcId: str
        :param _TargetGroupName: 目标组的名字
        :type TargetGroupName: str
        :param _Port: 目标组的默认端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _CreatedTime: 目标组的创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 目标组的修改时间
        :type UpdatedTime: str
        :param _AssociatedRule: 关联到的规则数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociatedRule: list of AssociationItem
        """
        self._TargetGroupId = None
        self._VpcId = None
        self._TargetGroupName = None
        self._Port = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._AssociatedRule = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def AssociatedRule(self):
        return self._AssociatedRule

    @AssociatedRule.setter
    def AssociatedRule(self, AssociatedRule):
        self._AssociatedRule = AssociatedRule


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._VpcId = params.get("VpcId")
        self._TargetGroupName = params.get("TargetGroupName")
        self._Port = params.get("Port")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        if params.get("AssociatedRule") is not None:
            self._AssociatedRule = []
            for item in params.get("AssociatedRule"):
                obj = AssociationItem()
                obj._deserialize(item)
                self._AssociatedRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInstance(AbstractModel):
    """目标组实例

    """

    def __init__(self):
        r"""
        :param _BindIP: 目标组实例的内网IP
        :type BindIP: str
        :param _Port: 目标组实例的端口
        :type Port: int
        :param _Weight: 目标组实例的权重
        :type Weight: int
        :param _NewPort: 目标组实例的新端口
        :type NewPort: int
        """
        self._BindIP = None
        self._Port = None
        self._Weight = None
        self._NewPort = None

    @property
    def BindIP(self):
        return self._BindIP

    @BindIP.setter
    def BindIP(self, BindIP):
        self._BindIP = BindIP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def NewPort(self):
        return self._NewPort

    @NewPort.setter
    def NewPort(self, NewPort):
        self._NewPort = NewPort


    def _deserialize(self, params):
        self._BindIP = params.get("BindIP")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._NewPort = params.get("NewPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHealth(AbstractModel):
    """描述一个Target的健康信息

    """

    def __init__(self):
        r"""
        :param _IP: Target的内网IP
        :type IP: str
        :param _Port: Target绑定的端口
        :type Port: int
        :param _HealthStatus: 当前健康状态，true：健康，false：不健康（包括尚未开始探测、探测中、状态异常等几种状态）。只有处于健康状态（且权重大于0），负载均衡才会向其转发流量。
        :type HealthStatus: bool
        :param _TargetId: Target的实例ID，如 ins-12345678
        :type TargetId: str
        :param _HealthStatusDetail: 当前健康状态的详细信息。如：Alive、Dead、Unknown。Alive状态为健康，Dead状态为异常，Unknown状态包括尚未开始探测、探测中、状态未知。
        :type HealthStatusDetail: str
        :param _HealthStatusDetial: (**该参数对象即将下线，不推荐使用，请使用HealthStatusDetail获取健康详情**) 当前健康状态的详细信息。如：Alive、Dead、Unknown。Alive状态为健康，Dead状态为异常，Unknown状态包括尚未开始探测、探测中、状态未知。
        :type HealthStatusDetial: str
        """
        self._IP = None
        self._Port = None
        self._HealthStatus = None
        self._TargetId = None
        self._HealthStatusDetail = None
        self._HealthStatusDetial = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def HealthStatusDetail(self):
        return self._HealthStatusDetail

    @HealthStatusDetail.setter
    def HealthStatusDetail(self, HealthStatusDetail):
        self._HealthStatusDetail = HealthStatusDetail

    @property
    def HealthStatusDetial(self):
        warnings.warn("parameter `HealthStatusDetial` is deprecated", DeprecationWarning) 

        return self._HealthStatusDetial

    @HealthStatusDetial.setter
    def HealthStatusDetial(self, HealthStatusDetial):
        warnings.warn("parameter `HealthStatusDetial` is deprecated", DeprecationWarning) 

        self._HealthStatusDetial = HealthStatusDetial


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        self._HealthStatus = params.get("HealthStatus")
        self._TargetId = params.get("TargetId")
        self._HealthStatusDetail = params.get("HealthStatusDetail")
        self._HealthStatusDetial = params.get("HealthStatusDetial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetRegionInfo(AbstractModel):
    """负载均衡实例所绑定的后端服务的信息，包括所属地域、所属网络。

    """

    def __init__(self):
        r"""
        :param _Region: Target所属地域，如 ap-guangzhou
        :type Region: str
        :param _VpcId: Target所属网络，私有网络格式如 vpc-abcd1234，如果是基础网络，则为"0"
        :type VpcId: str
        """
        self._Region = None
        self._VpcId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TypeInfo(AbstractModel):
    """运营商类型信息

    """

    def __init__(self):
        r"""
        :param _Type: 运营商类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _SpecAvailabilitySet: 规格可用性
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecAvailabilitySet: list of SpecAvailability
        """
        self._Type = None
        self._SpecAvailabilitySet = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SpecAvailabilitySet(self):
        return self._SpecAvailabilitySet

    @SpecAvailabilitySet.setter
    def SpecAvailabilitySet(self, SpecAvailabilitySet):
        self._SpecAvailabilitySet = SpecAvailabilitySet


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("SpecAvailabilitySet") is not None:
            self._SpecAvailabilitySet = []
            for item in params.get("SpecAvailabilitySet"):
                obj = SpecAvailability()
                obj._deserialize(item)
                self._SpecAvailabilitySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """可用区相关信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区数值形式的唯一ID，如：100001
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _Zone: 可用区字符串形式的唯一ID，如：ap-guangzhou-1
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _ZoneName: 可用区名称，如：广州一区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param _ZoneRegion: 可用区所属地域，如：ap-guangzhou
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneRegion: str
        :param _LocalZone: 可用区是否是LocalZone可用区，如：false
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalZone: bool
        :param _EdgeZone: 可用区是否是EdgeZone可用区，如：false
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeZone: bool
        """
        self._ZoneId = None
        self._Zone = None
        self._ZoneName = None
        self._ZoneRegion = None
        self._LocalZone = None
        self._EdgeZone = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneRegion(self):
        return self._ZoneRegion

    @ZoneRegion.setter
    def ZoneRegion(self, ZoneRegion):
        self._ZoneRegion = ZoneRegion

    @property
    def LocalZone(self):
        return self._LocalZone

    @LocalZone.setter
    def LocalZone(self, LocalZone):
        self._LocalZone = LocalZone

    @property
    def EdgeZone(self):
        return self._EdgeZone

    @EdgeZone.setter
    def EdgeZone(self, EdgeZone):
        self._EdgeZone = EdgeZone


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneRegion = params.get("ZoneRegion")
        self._LocalZone = params.get("LocalZone")
        self._EdgeZone = params.get("EdgeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResource(AbstractModel):
    """可用区资源列表

    """

    def __init__(self):
        r"""
        :param _MasterZone: 主可用区，如"ap-guangzhou-1"。
        :type MasterZone: str
        :param _ResourceSet: 资源列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceSet: list of Resource
        :param _SlaveZone: 备可用区，如"ap-guangzhou-2"，单可用区时，备可用区为null。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZone: str
        :param _IPVersion: IP版本，如IPv4，IPv6，IPv6_Nat。
        :type IPVersion: str
        :param _ZoneRegion: 可用区所属地域，如：ap-guangzhou
        :type ZoneRegion: str
        :param _LocalZone: 可用区是否是LocalZone可用区，如：false
        :type LocalZone: bool
        :param _ZoneResourceType: 可用区资源的类型，SHARED表示共享资源，EXCLUSIVE表示独占资源。
        :type ZoneResourceType: str
        :param _EdgeZone: 可用区是否是EdgeZone可用区，如：false
        :type EdgeZone: bool
        :param _Egress: 网络出口
注意：此字段可能返回 null，表示取不到有效值。
        :type Egress: str
        """
        self._MasterZone = None
        self._ResourceSet = None
        self._SlaveZone = None
        self._IPVersion = None
        self._ZoneRegion = None
        self._LocalZone = None
        self._ZoneResourceType = None
        self._EdgeZone = None
        self._Egress = None

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def ResourceSet(self):
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def IPVersion(self):
        return self._IPVersion

    @IPVersion.setter
    def IPVersion(self, IPVersion):
        self._IPVersion = IPVersion

    @property
    def ZoneRegion(self):
        return self._ZoneRegion

    @ZoneRegion.setter
    def ZoneRegion(self, ZoneRegion):
        self._ZoneRegion = ZoneRegion

    @property
    def LocalZone(self):
        return self._LocalZone

    @LocalZone.setter
    def LocalZone(self, LocalZone):
        self._LocalZone = LocalZone

    @property
    def ZoneResourceType(self):
        return self._ZoneResourceType

    @ZoneResourceType.setter
    def ZoneResourceType(self, ZoneResourceType):
        self._ZoneResourceType = ZoneResourceType

    @property
    def EdgeZone(self):
        return self._EdgeZone

    @EdgeZone.setter
    def EdgeZone(self, EdgeZone):
        self._EdgeZone = EdgeZone

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._MasterZone = params.get("MasterZone")
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._SlaveZone = params.get("SlaveZone")
        self._IPVersion = params.get("IPVersion")
        self._ZoneRegion = params.get("ZoneRegion")
        self._LocalZone = params.get("LocalZone")
        self._ZoneResourceType = params.get("ZoneResourceType")
        self._EdgeZone = params.get("EdgeZone")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        