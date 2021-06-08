# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
        """
        :param Associations: 绑定的关系数组。
        :type Associations: list of TargetGroupAssociation
        """
        self.Associations = None


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self.Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self.Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AssociateTargetGroupsResponse(AbstractModel):
    """AssociateTargetGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AssociationItem(AbstractModel):
    """目标组关联到的规则

    """

    def __init__(self):
        """
        :param LoadBalancerId: 关联到的负载均衡ID
        :type LoadBalancerId: str
        :param ListenerId: 关联到的监听器ID
        :type ListenerId: str
        :param LocationId: 关联到的转发规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationId: str
        :param Protocol: 关联到的监听器协议类型，如HTTP,TCP,
        :type Protocol: str
        :param Port: 关联到的监听器端口
        :type Port: int
        :param Domain: 关联到的转发规则域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Url: 关联到的转发规则URL
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param LoadBalancerName: 负载均衡名称
        :type LoadBalancerName: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Protocol = None
        self.Port = None
        self.Domain = None
        self.Url = None
        self.LoadBalancerName = None
        self.ListenerName = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.ListenerName = params.get("ListenerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AutoRewriteRequest(AbstractModel):
    """AutoRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: HTTPS:443监听器的ID。
        :type ListenerId: str
        :param Domains: HTTPS:443监听器下需要重定向的域名，若不填，则对HTTPS:443监听器下的所有域名都设置重定向。
        :type Domains: list of str
        :param RewriteCodes: 重定向状态码，可取值301,302,307。
        :type RewriteCodes: list of int
        :param TakeUrls: 重定向是否携带匹配的URL。
        :type TakeUrls: list of bool
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domains = None
        self.RewriteCodes = None
        self.TakeUrls = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domains = params.get("Domains")
        self.RewriteCodes = params.get("RewriteCodes")
        self.TakeUrls = params.get("TakeUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AutoRewriteResponse(AbstractModel):
    """AutoRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Backend(AbstractModel):
    """监听器绑定的后端服务的详细信息

    """

    def __init__(self):
        """
        :param Type: 后端服务的类型，可取：CVM、ENI
        :type Type: str
        :param InstanceId: 后端服务的唯一 ID，如 ins-abcd1234
        :type InstanceId: str
        :param Port: 后端服务的监听端口
        :type Port: int
        :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param RegisteredTime: 后端服务被绑定的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        :param EniId: 弹性网卡唯一ID，如 eni-1234abcd
注意：此字段可能返回 null，表示取不到有效值。
        :type EniId: str
        """
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None
        self.EniId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BasicTargetGroupInfo(AbstractModel):
    """监听器或者转发规则绑定的目标组基本信息

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param TargetGroupName: 目标组名称
        :type TargetGroupName: str
        """
        self.TargetGroupId = None
        self.TargetGroupName = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.TargetGroupName = params.get("TargetGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID。
        :type LoadBalancerId: str
        :param Targets: 解绑目标。
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets返回参数结构体

    """

    def __init__(self):
        """
        :param FailListenerIdSet: 解绑失败的监听器ID。
        :type FailListenerIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param ModifyList: 要批量修改权重的列表。
        :type ModifyList: list of RsWeightRule
        """
        self.LoadBalancerId = None
        self.ModifyList = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self.ModifyList = []
            for item in params.get("ModifyList"):
                obj = RsWeightRule()
                obj._deserialize(item)
                self.ModifyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID。
        :type LoadBalancerId: str
        :param Targets: 绑定目标。
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets返回参数结构体

    """

    def __init__(self):
        """
        :param FailListenerIdSet: 绑定失败的监听器ID，如为空表示全部绑定成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailListenerIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchTarget(AbstractModel):
    """批量绑定类型

    """

    def __init__(self):
        """
        :param ListenerId: 监听器 ID。
        :type ListenerId: str
        :param Port: 绑定端口。
        :type Port: int
        :param InstanceId: 子机 ID。表示绑定主网卡主 IP。
        :type InstanceId: str
        :param EniIp: 绑定 IP 时需要传入此参数，支持弹性网卡的 IP 和其他内网 IP，如果是弹性网卡则必须先绑定至CVM，然后才能绑定到负载均衡实例。
注意：参数 InstanceId、EniIp 只能传入一个且必须传入一个。如果绑定双栈IPV6子机，必须传该参数。
        :type EniIp: str
        :param Weight: 子机权重，范围[0, 100]。绑定时如果不存在，则默认为10。
        :type Weight: int
        :param LocationId: 七层规则 ID。
        :type LocationId: str
        """
        self.ListenerId = None
        self.Port = None
        self.InstanceId = None
        self.EniIp = None
        self.Weight = None
        self.LocationId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.EniIp = params.get("EniIp")
        self.Weight = params.get("Weight")
        self.LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BlockedIP(AbstractModel):
    """加入了12306黑名单的IP

    """

    def __init__(self):
        """
        :param IP: 黑名单IP
        :type IP: str
        :param CreateTime: 加入黑名单的时间
        :type CreateTime: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        """
        self.IP = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CertIdRelatedWithLoadBalancers(AbstractModel):
    """证书ID，以及与该证书ID关联的负载均衡实例列表

    """

    def __init__(self):
        """
        :param CertId: 证书ID
        :type CertId: str
        :param LoadBalancers: 与证书关联的负载均衡实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancers: list of LoadBalancer
        """
        self.CertId = None
        self.LoadBalancers = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CertificateInput(AbstractModel):
    """证书信息

    """

    def __init__(self):
        """
        :param SSLMode: 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证
        :type SSLMode: str
        :param CertId: 服务端证书的 ID，如果不填写此项则必须上传证书，包括 CertContent，CertKey，CertName。
        :type CertId: str
        :param CertCaId: 客户端证书的 ID，当监听器采用双向认证，即 SSLMode=MUTUAL 时，如果不填写此项则必须上传客户端证书，包括 CertCaContent，CertCaName。
        :type CertCaId: str
        :param CertName: 上传服务端证书的名称，如果没有 CertId，则此项必传。
        :type CertName: str
        :param CertKey: 上传服务端证书的 key，如果没有 CertId，则此项必传。
        :type CertKey: str
        :param CertContent: 上传服务端证书的内容，如果没有 CertId，则此项必传。
        :type CertContent: str
        :param CertCaName: 上传客户端 CA 证书的名称，如果 SSLMode=mutual，如果没有 CertCaId，则此项必传。
        :type CertCaName: str
        :param CertCaContent: 上传客户端证书的内容，如果 SSLMode=mutual，如果没有 CertCaId，则此项必传。
        :type CertCaContent: str
        """
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None
        self.CertName = None
        self.CertKey = None
        self.CertContent = None
        self.CertCaName = None
        self.CertCaContent = None


    def _deserialize(self, params):
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.CertName = params.get("CertName")
        self.CertKey = params.get("CertKey")
        self.CertContent = params.get("CertContent")
        self.CertCaName = params.get("CertCaName")
        self.CertCaContent = params.get("CertCaContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CertificateOutput(AbstractModel):
    """证书相关信息

    """

    def __init__(self):
        """
        :param SSLMode: 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证
        :type SSLMode: str
        :param CertId: 服务端证书的 ID。
        :type CertId: str
        :param CertCaId: 客户端证书的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertCaId: str
        """
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None


    def _deserialize(self, params):
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClassicalHealth(AbstractModel):
    """传统型负载均衡后端服务的健康状态

    """

    def __init__(self):
        """
        :param IP: 后端服务的内网 IP
        :type IP: str
        :param Port: 后端服务的端口
        :type Port: int
        :param ListenerPort: 负载均衡的监听端口
        :type ListenerPort: int
        :param Protocol: 转发协议
        :type Protocol: str
        :param HealthStatus: 健康检查结果，1 表示健康，0 表示不健康
        :type HealthStatus: int
        """
        self.IP = None
        self.Port = None
        self.ListenerPort = None
        self.Protocol = None
        self.HealthStatus = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.ListenerPort = params.get("ListenerPort")
        self.Protocol = params.get("Protocol")
        self.HealthStatus = params.get("HealthStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClassicalListener(AbstractModel):
    """传统型负载均衡监听器信息

    """

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器ID
        :type ListenerId: str
        :param ListenerPort: 负载均衡监听器端口
        :type ListenerPort: int
        :param InstancePort: 监听器后端转发端口
        :type InstancePort: int
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Protocol: 监听器协议类型
        :type Protocol: str
        :param SessionExpire: 会话保持时间
        :type SessionExpire: int
        :param HealthSwitch: 是否开启了健康检查：1（开启）、0（关闭）
        :type HealthSwitch: int
        :param TimeOut: 响应超时时间
        :type TimeOut: int
        :param IntervalTime: 检查间隔
        :type IntervalTime: int
        :param HealthNum: 健康阈值
        :type HealthNum: int
        :param UnhealthNum: 不健康阈值
        :type UnhealthNum: int
        :param HttpHash: 传统型公网负载均衡的 HTTP、HTTPS 监听器的请求均衡方法。wrr 表示按权重轮询，ip_hash 表示根据访问的源 IP 进行一致性哈希方式来分发
        :type HttpHash: str
        :param HttpCode: 传统型公网负载均衡的 HTTP、HTTPS 监听器的健康检查返回码。具体可参考创建监听器中对该字段的解释
        :type HttpCode: int
        :param HttpCheckPath: 传统型公网负载均衡的 HTTP、HTTPS 监听器的健康检查路径
        :type HttpCheckPath: str
        :param SSLMode: 传统型公网负载均衡的 HTTPS 监听器的认证方式
        :type SSLMode: str
        :param CertId: 传统型公网负载均衡的 HTTPS 监听器的服务端证书 ID
        :type CertId: str
        :param CertCaId: 传统型公网负载均衡的 HTTPS 监听器的客户端证书 ID
        :type CertCaId: str
        :param Status: 监听器的状态，0 表示创建中，1 表示运行中
        :type Status: int
        """
        self.ListenerId = None
        self.ListenerPort = None
        self.InstancePort = None
        self.ListenerName = None
        self.Protocol = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpHash = None
        self.HttpCode = None
        self.HttpCheckPath = None
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None
        self.Status = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerPort = params.get("ListenerPort")
        self.InstancePort = params.get("InstancePort")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpHash = params.get("HttpHash")
        self.HttpCode = params.get("HttpCode")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClassicalLoadBalancerInfo(AbstractModel):
    """负载均衡信息

    """

    def __init__(self):
        """
        :param InstanceId: 后端实例ID
        :type InstanceId: str
        :param LoadBalancerIds: 负载均衡实例ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerIds: list of str
        """
        self.InstanceId = None
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClassicalTarget(AbstractModel):
    """传统型负载均衡的后端服务相关信息

    """

    def __init__(self):
        """
        :param Type: 后端服务的类型，可取值：CVM、ENI（即将支持）
        :type Type: str
        :param InstanceId: 后端服务的唯一 ID，可通过 DescribeInstances 接口返回字段中的 unInstanceId 字段获取
        :type InstanceId: str
        :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param RunFlag: 后端服务的状态
1：故障，2：运行中，3：创建中，4：已关机，5：已退还，6：退还中， 7：重启中，8：开机中，9：关机中，10：密码重置中，11：格式化中，12：镜像制作中，13：带宽设置中，14：重装系统中，19：升级中，21：热迁移中
注意：此字段可能返回 null，表示取不到有效值。
        :type RunFlag: int
        """
        self.Type = None
        self.InstanceId = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RunFlag = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RunFlag = params.get("RunFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClassicalTargetInfo(AbstractModel):
    """传统型负载均衡的后端信息

    """

    def __init__(self):
        """
        :param InstanceId: 后端实例ID
        :type InstanceId: str
        :param Weight: 权重，取值范围 [0, 100]
        :type Weight: int
        """
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Cluster(AbstractModel):
    """集群的详细信息，如集群ID，名称，类型，可用区，标签等

    """

    def __init__(self):
        """
        :param ClusterId: 集群唯一ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterType: 集群类型，如TGW，STGW，VPCGW
        :type ClusterType: str
        :param ClusterTag: 集群标签，只有STGW集群有标签
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterTag: str
        :param Zone: 集群所在可用区，如ap-guangzhou-1
        :type Zone: str
        :param Network: 集群网络类型，如Public，Private
        :type Network: str
        :param MaxConn: 最大连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConn: int
        :param MaxInFlow: 最大入带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxInFlow: int
        :param MaxInPkg: 最大入包量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxInPkg: int
        :param MaxOutFlow: 最大出带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxOutFlow: int
        :param MaxOutPkg: 最大出包量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxOutPkg: int
        :param MaxNewConn: 最大新建连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNewConn: int
        :param HTTPMaxNewConn: http最大新建连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPMaxNewConn: int
        :param HTTPSMaxNewConn: https最大新建连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPSMaxNewConn: int
        :param HTTPQps: http QPS
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPQps: int
        :param HTTPSQps: https QPS
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPSQps: int
        :param ResourceCount: 集群内资源总数目
        :type ResourceCount: int
        :param IdleResourceCount: 集群内空闲资源数目
注意：此字段可能返回 null，表示取不到有效值。
        :type IdleResourceCount: int
        :param LoadBalanceDirectorCount: 集群内转发机的数目
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalanceDirectorCount: int
        :param Isp: 集群的Isp属性，如："BGP","CMCC","CUCC","CTCC","INTERNAL"。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isp: str
        :param ClustersZone: 集群所在的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ClustersZone: :class:`tencentcloud.clb.v20180317.models.ClustersZone`
        :param ClustersVersion: 集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ClustersVersion: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterType = None
        self.ClusterTag = None
        self.Zone = None
        self.Network = None
        self.MaxConn = None
        self.MaxInFlow = None
        self.MaxInPkg = None
        self.MaxOutFlow = None
        self.MaxOutPkg = None
        self.MaxNewConn = None
        self.HTTPMaxNewConn = None
        self.HTTPSMaxNewConn = None
        self.HTTPQps = None
        self.HTTPSQps = None
        self.ResourceCount = None
        self.IdleResourceCount = None
        self.LoadBalanceDirectorCount = None
        self.Isp = None
        self.ClustersZone = None
        self.ClustersVersion = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.ClusterTag = params.get("ClusterTag")
        self.Zone = params.get("Zone")
        self.Network = params.get("Network")
        self.MaxConn = params.get("MaxConn")
        self.MaxInFlow = params.get("MaxInFlow")
        self.MaxInPkg = params.get("MaxInPkg")
        self.MaxOutFlow = params.get("MaxOutFlow")
        self.MaxOutPkg = params.get("MaxOutPkg")
        self.MaxNewConn = params.get("MaxNewConn")
        self.HTTPMaxNewConn = params.get("HTTPMaxNewConn")
        self.HTTPSMaxNewConn = params.get("HTTPSMaxNewConn")
        self.HTTPQps = params.get("HTTPQps")
        self.HTTPSQps = params.get("HTTPSQps")
        self.ResourceCount = params.get("ResourceCount")
        self.IdleResourceCount = params.get("IdleResourceCount")
        self.LoadBalanceDirectorCount = params.get("LoadBalanceDirectorCount")
        self.Isp = params.get("Isp")
        if params.get("ClustersZone") is not None:
            self.ClustersZone = ClustersZone()
            self.ClustersZone._deserialize(params.get("ClustersZone"))
        self.ClustersVersion = params.get("ClustersVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterItem(AbstractModel):
    """独占集群信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群唯一ID
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param Zone: 集群所在可用区，如ap-guangzhou-1
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Zone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterResource(AbstractModel):
    """集群内资源类型

    """

    def __init__(self):
        """
        :param ClusterId: 集群唯一ID，如tgw-12345678。
        :type ClusterId: str
        :param Vip: ip地址。
        :type Vip: str
        :param LoadBalancerId: 负载均衡唯一ID，如lb-12345678。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerId: str
        :param Idle: 资源是否闲置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Idle: str
        :param ClusterName: 集群名称。
        :type ClusterName: str
        """
        self.ClusterId = None
        self.Vip = None
        self.LoadBalancerId = None
        self.Idle = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Vip = params.get("Vip")
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Idle = params.get("Idle")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClustersZone(AbstractModel):
    """集群所在的可用区。

    """

    def __init__(self):
        """
        :param MasterZone: 集群所在的主可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: list of str
        :param SlaveZone: 集群所在的备可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZone: list of str
        """
        self.MasterZone = None
        self.SlaveZone = None


    def _deserialize(self, params):
        self.MasterZone = params.get("MasterZone")
        self.SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClsLogSetRequest(AbstractModel):
    """CreateClsLogSet请求参数结构体

    """

    def __init__(self):
        """
        :param Period: 日志集的保存周期，单位：天，最大 90。
        :type Period: int
        :param LogsetName: 日志集的名字，不能和cls其他日志集重名。不填默认为clb_logset。
        :type LogsetName: str
        :param LogsetType: 日志集类型，ACCESS：访问日志，HEALTH：健康检查日志，默认ACCESS。
        :type LogsetType: str
        """
        self.Period = None
        self.LogsetName = None
        self.LogsetType = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.LogsetName = params.get("LogsetName")
        self.LogsetType = params.get("LogsetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClsLogSetResponse(AbstractModel):
    """CreateClsLogSet返回参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集的 ID。
        :type LogsetId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogsetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateListenerRequest(AbstractModel):
    """CreateListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param Ports: 要将监听器创建到哪些端口，每个端口对应一个新的监听器。
        :type Ports: list of int
        :param Protocol: 监听器协议： TCP | UDP | HTTP | HTTPS | TCP_SSL（TCP_SSL 正在内测中，如需使用请通过工单申请）。
        :type Protocol: str
        :param ListenerNames: 要创建的监听器名称列表，名称与Ports数组按序一一对应，如不需立即命名，则无需提供此参数。
        :type ListenerNames: list of str
        :param HealthCheck: 健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL监听器。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 证书相关信息，此参数仅适用于TCP_SSL监听器和未开启SNI特性的HTTPS监听器。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :type SessionExpireTime: int
        :param Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。此参数仅适用于TCP/UDP/TCP_SSL监听器。
        :type Scheduler: str
        :param SniSwitch: 是否开启SNI特性，此参数仅适用于HTTPS监听器。
        :type SniSwitch: int
        :param TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组。
        :type TargetType: str
        :param SessionType: 会话保持类型。不传或传NORMAL表示默认会话保持类型。QUIC_CID 表示根据Quic Connection ID做会话保持。QUIC_CID只支持UDP协议。
        :type SessionType: str
        :param KeepaliveEnable: 是否开启长连接，此参数仅适用于HTTP/HTTPS监听器，0:关闭；1:开启， 默认关闭。
        :type KeepaliveEnable: int
        :param EndPort: 创建端口段监听器时必须传入此参数，用以标识结束端口。同时，入参Ports只允许传入一个成员，用以标识开始端口。【如果您需要体验端口段功能，请通过 [工单申请](https://console.cloud.tencent.com/workorder/category)】。
        :type EndPort: int
        :param DeregisterTargetRst: 解绑后端目标时，是否发RST给客户端，此参数仅适用于TCP监听器。
        :type DeregisterTargetRst: bool
        """
        self.LoadBalancerId = None
        self.Ports = None
        self.Protocol = None
        self.ListenerNames = None
        self.HealthCheck = None
        self.Certificate = None
        self.SessionExpireTime = None
        self.Scheduler = None
        self.SniSwitch = None
        self.TargetType = None
        self.SessionType = None
        self.KeepaliveEnable = None
        self.EndPort = None
        self.DeregisterTargetRst = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ports = params.get("Ports")
        self.Protocol = params.get("Protocol")
        self.ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.Scheduler = params.get("Scheduler")
        self.SniSwitch = params.get("SniSwitch")
        self.TargetType = params.get("TargetType")
        self.SessionType = params.get("SessionType")
        self.KeepaliveEnable = params.get("KeepaliveEnable")
        self.EndPort = params.get("EndPort")
        self.DeregisterTargetRst = params.get("DeregisterTargetRst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateListenerResponse(AbstractModel):
    """CreateListener返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerIds: 创建的监听器的唯一标识数组。
        :type ListenerIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
        :type LoadBalancerType: str
        :param Forward: 负载均衡实例的类型。1：通用的负载均衡实例，目前只支持传入1。
        :type Forward: int
        :param LoadBalancerName: 负载均衡实例的名称，只在创建一个实例的时候才会生效。规则：1-60 个英文、汉字、数字、连接线“-”或下划线“_”。
注意：如果名称与系统中已有负载均衡实例的名称相同，则系统将会自动生成此次创建的负载均衡实例的名称。
        :type LoadBalancerName: str
        :param VpcId: 负载均衡后端目标设备所属的网络 ID，如vpc-12345678，可以通过 DescribeVpcEx 接口获取。 不传此参数则默认为基础网络（"0"）。
        :type VpcId: str
        :param SubnetId: 在私有网络内购买内网负载均衡实例的情况下，必须指定子网 ID，内网负载均衡实例的 VIP 将从这个子网中产生。
        :type SubnetId: str
        :param ProjectId: 负载均衡实例所属的项目 ID，可以通过 DescribeProject 接口获取。不传此参数则视为默认项目。
        :type ProjectId: int
        :param AddressIPVersion: 仅适用于公网负载均衡。IP版本，可取值：IPV4、IPV6、IPv6FullChain，默认值 IPV4。
        :type AddressIPVersion: str
        :param Number: 创建负载均衡的个数，默认值 1。
        :type Number: int
        :param MasterZoneId: 仅适用于公网负载均衡。设置跨可用区容灾时的主可用区ID，例如 100001 或 ap-guangzhou-1
注：主可用区是需要承载流量的可用区，备可用区默认不承载流量，主可用区不可用时才使用备可用区，平台将为您自动选择最佳备可用区。可通过 DescribeMasterZones 接口查询一个地域的主可用区的列表。
        :type MasterZoneId: str
        :param ZoneId: 仅适用于公网负载均衡。可用区ID，指定可用区以创建负载均衡实例。如：ap-guangzhou-1。
        :type ZoneId: str
        :param InternetAccessible: 仅适用于公网负载均衡。负载均衡的网络计费模式。
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param VipIsp: 仅适用于公网负载均衡。CMCC | CTCC | CUCC，分别对应 移动 | 电信 | 联通，如果不指定本参数，则默认使用BGP。可通过 DescribeSingleIsp 接口查询一个地域所支持的Isp。如果指定运营商，则网络计费式只能使用按带宽包计费(BANDWIDTH_PACKAGE)。
        :type VipIsp: str
        :param Tags: 购买负载均衡同时，给负载均衡打上标签。
        :type Tags: list of TagInfo
        :param Vip: 指定Vip申请负载均衡。
        :type Vip: str
        :param BandwidthPackageId: 带宽包ID，指定此参数时，网络计费方式（InternetAccessible.InternetChargeType）只支持按带宽包计费（BANDWIDTH_PACKAGE）。
        :type BandwidthPackageId: str
        :param ExclusiveCluster: 独占集群信息。
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param SnatPro: 是否支持绑定跨地域/跨Vpc绑定IP的功能。
        :type SnatPro: bool
        :param SnatIps: 开启绑定跨地域/跨Vpc绑定IP的功能后，创建SnatIp。
        :type SnatIps: list of SnatIp
        :param ClusterTag: Stgw独占集群的标签。
        :type ClusterTag: str
        :param SlaveZoneId: 仅适用于公网负载均衡。设置跨可用区容灾时的备可用区ID，例如 100001 或 ap-guangzhou-1
注：备可用区是主可用区故障后，需要承载流量的可用区。可通过 DescribeMasterZones 接口查询一个地域的主/备可用区的列表。
        :type SlaveZoneId: str
        :param EipAddressId: EIP 的唯一 ID，形如：eip-11112222，仅适用于内网负载均衡绑定EIP。
        :type EipAddressId: str
        """
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.AddressIPVersion = None
        self.Number = None
        self.MasterZoneId = None
        self.ZoneId = None
        self.InternetAccessible = None
        self.VipIsp = None
        self.Tags = None
        self.Vip = None
        self.BandwidthPackageId = None
        self.ExclusiveCluster = None
        self.ClientToken = None
        self.SnatPro = None
        self.SnatIps = None
        self.ClusterTag = None
        self.SlaveZoneId = None
        self.EipAddressId = None


    def _deserialize(self, params):
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.Number = params.get("Number")
        self.MasterZoneId = params.get("MasterZoneId")
        self.ZoneId = params.get("ZoneId")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.VipIsp = params.get("VipIsp")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Vip = params.get("Vip")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        if params.get("ExclusiveCluster") is not None:
            self.ExclusiveCluster = ExclusiveCluster()
            self.ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self.ClientToken = params.get("ClientToken")
        self.SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)
        self.ClusterTag = params.get("ClusterTag")
        self.SlaveZoneId = params.get("SlaveZoneId")
        self.EipAddressId = params.get("EipAddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 由负载均衡实例唯一 ID 组成的数组。
        :type LoadBalancerIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLoadBalancerSnatIpsRequest(AbstractModel):
    """CreateLoadBalancerSnatIps请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡唯一性ID，例如：lb-12345678。
        :type LoadBalancerId: str
        :param SnatIps: 添加SnatIp信息，可指定IP申请，或者指定子网自动申请。
        :type SnatIps: list of SnatIp
        """
        self.LoadBalancerId = None
        self.SnatIps = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLoadBalancerSnatIpsResponse(AbstractModel):
    """CreateLoadBalancerSnatIps返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param ListenerId: 监听器 ID。
        :type ListenerId: str
        :param Rules: 新建转发规则的信息。
        :type Rules: list of RuleInput
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Rules = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInput()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        """
        :param LocationIds: 创建的转发规则的唯一标识数组。
        :type LocationIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LocationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LocationIds = params.get("LocationIds")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateTargetGroupRequest(AbstractModel):
    """CreateTargetGroup请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupName: 目标组名称，限定50个字符
        :type TargetGroupName: str
        :param VpcId: 目标组的vpcid属性，不填则使用默认vpc
        :type VpcId: str
        :param Port: 目标组的默认端口， 后续添加服务器时可使用该默认端口
        :type Port: int
        :param TargetGroupInstances: 目标组绑定的后端服务器
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupName = None
        self.VpcId = None
        self.Port = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupName = params.get("TargetGroupName")
        self.VpcId = params.get("VpcId")
        self.Port = params.get("Port")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateTargetGroupResponse(AbstractModel):
    """CreateTargetGroup返回参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupId: 创建目标组后生成的id
        :type TargetGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TargetGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 日志主题的名称。
        :type TopicName: str
        :param PartitionCount: 主题分区Partition的数量，不传参默认创建1个，最大创建允许10个，分裂/合并操作会改变分区数量，整体上限50个。
        :type PartitionCount: int
        :param TopicType: 日志类型，ACCESS：访问日志，HEALTH：健康检查日志，默认ACCESS。
        :type TopicType: str
        """
        self.TopicName = None
        self.PartitionCount = None
        self.TopicType = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.PartitionCount = params.get("PartitionCount")
        self.TopicType = params.get("TopicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题的 ID。
        :type TopicId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteListenerRequest(AbstractModel):
    """DeleteListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: 要删除的监听器ID。
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteListenerResponse(AbstractModel):
    """DeleteListener返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerIds: 指定删除的监听器ID数组，若不填则删除负载均衡的所有监听器。
        :type ListenerIds: list of str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 要删除的负载均衡实例 ID数组，数组大小最大支持20。
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLoadBalancerSnatIpsRequest(AbstractModel):
    """DeleteLoadBalancerSnatIps请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡唯一ID，例如：lb-12345678。
        :type LoadBalancerId: str
        :param Ips: 删除SnatIp地址数组。
        :type Ips: list of str
        """
        self.LoadBalancerId = None
        self.Ips = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLoadBalancerSnatIpsResponse(AbstractModel):
    """DeleteLoadBalancerSnatIps返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteRewriteRequest(AbstractModel):
    """DeleteRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param SourceListenerId: 源监听器ID。
        :type SourceListenerId: str
        :param TargetListenerId: 目标监听器ID。
        :type TargetListenerId: str
        :param RewriteInfos: 转发规则之间的重定向关系。
        :type RewriteInfos: list of RewriteLocationMap
        """
        self.LoadBalancerId = None
        self.SourceListenerId = None
        self.TargetListenerId = None
        self.RewriteInfos = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerId = params.get("SourceListenerId")
        self.TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self.RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self.RewriteInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteRewriteResponse(AbstractModel):
    """DeleteRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param LocationIds: 要删除的转发规则的ID组成的数组。
        :type LocationIds: list of str
        :param Domain: 要删除的转发规则的域名，已提供LocationIds参数时本参数不生效。
        :type Domain: str
        :param Url: 要删除的转发规则的转发路径，已提供LocationIds参数时本参数不生效。
        :type Url: str
        :param NewDefaultServerDomain: 监听器下必须配置一个默认域名，当需要删除默认域名时，可以指定另一个域名作为新的默认域名。
        :type NewDefaultServerDomain: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationIds = None
        self.Domain = None
        self.Url = None
        self.NewDefaultServerDomain = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationIds = params.get("LocationIds")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.NewDefaultServerDomain = params.get("NewDefaultServerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteTargetGroupsRequest(AbstractModel):
    """DeleteTargetGroups请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupIds: 目标组的ID数组。
        :type TargetGroupIds: list of str
        """
        self.TargetGroupIds = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteTargetGroupsResponse(AbstractModel):
    """DeleteTargetGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeregisterTargetGroupInstancesRequest(AbstractModel):
    """DeregisterTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        :param TargetGroupInstances: 待解绑的服务器信息。
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeregisterTargetGroupInstancesResponse(AbstractModel):
    """DeregisterTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeregisterTargetsFromClassicalLBRequest(AbstractModel):
    """DeregisterTargetsFromClassicalLB请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param InstanceIds: 后端服务的实例ID列表。
        :type InstanceIds: list of str
        """
        self.LoadBalancerId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeregisterTargetsFromClassicalLBResponse(AbstractModel):
    """DeregisterTargetsFromClassicalLB返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeregisterTargetsRequest(AbstractModel):
    """DeregisterTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID，格式如 lb-12345678。
        :type LoadBalancerId: str
        :param ListenerId: 监听器 ID，格式如 lbl-12345678。
        :type ListenerId: str
        :param Targets: 要解绑的后端服务列表，数组长度最大支持20。
        :type Targets: list of Target
        :param LocationId: 转发规则的ID，格式如 loc-12345678，当从七层转发规则解绑机器时，必须提供此参数或Domain+URL两者之一。
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeregisterTargetsResponse(AbstractModel):
    """DeregisterTargets返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBlockIPListRequest(AbstractModel):
    """DescribeBlockIPList请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param Offset: 数据偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回IP的最大个数，默认为 100000。
        :type Limit: int
        """
        self.LoadBalancerId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBlockIPListResponse(AbstractModel):
    """DescribeBlockIPList返回参数结构体

    """

    def __init__(self):
        """
        :param BlockedIPCount: 返回的IP的数量
        :type BlockedIPCount: int
        :param ClientIPField: 获取用户真实IP的字段
        :type ClientIPField: str
        :param BlockedIPList: 加入了12360黑名单的IP列表
        :type BlockedIPList: list of BlockedIP
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlockedIPCount = None
        self.ClientIPField = None
        self.BlockedIPList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlockedIPCount = params.get("BlockedIPCount")
        self.ClientIPField = params.get("ClientIPField")
        if params.get("BlockedIPList") is not None:
            self.BlockedIPList = []
            for item in params.get("BlockedIPList"):
                obj = BlockedIP()
                obj._deserialize(item)
                self.BlockedIPList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBlockIPTaskRequest(AbstractModel):
    """DescribeBlockIPTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: ModifyBlockIPList 接口返回的异步任务的ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBlockIPTaskResponse(AbstractModel):
    """DescribeBlockIPTask返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 1 running，2 fail，6 succ
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClassicalLBByInstanceIdRequest(AbstractModel):
    """DescribeClassicalLBByInstanceId请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 后端实例ID列表。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClassicalLBByInstanceIdResponse(AbstractModel):
    """DescribeClassicalLBByInstanceId返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerInfoList: 负载均衡相关信息列表。
        :type LoadBalancerInfoList: list of ClassicalLoadBalancerInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerInfoList") is not None:
            self.LoadBalancerInfoList = []
            for item in params.get("LoadBalancerInfoList"):
                obj = ClassicalLoadBalancerInfo()
                obj._deserialize(item)
                self.LoadBalancerInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClassicalLBHealthStatusRequest(AbstractModel):
    """DescribeClassicalLBHealthStatus请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClassicalLBHealthStatusResponse(AbstractModel):
    """DescribeClassicalLBHealthStatus返回参数结构体

    """

    def __init__(self):
        """
        :param HealthList: 后端健康状态列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthList: list of ClassicalHealth
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HealthList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthList") is not None:
            self.HealthList = []
            for item in params.get("HealthList"):
                obj = ClassicalHealth()
                obj._deserialize(item)
                self.HealthList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClassicalLBListenersRequest(AbstractModel):
    """DescribeClassicalLBListeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerIds: 负载均衡监听器ID列表。
        :type ListenerIds: list of str
        :param Protocol: 负载均衡监听的协议：'TCP', 'UDP', 'HTTP', 'HTTPS'。
        :type Protocol: str
        :param ListenerPort: 负载均衡监听端口，范围为[1-65535]。
        :type ListenerPort: int
        :param Status: 监听器的状态，0：创建中，1：运行中。
        :type Status: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.ListenerPort = None
        self.Status = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.ListenerPort = params.get("ListenerPort")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClassicalLBListenersResponse(AbstractModel):
    """DescribeClassicalLBListeners返回参数结构体

    """

    def __init__(self):
        """
        :param Listeners: 监听器列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ClassicalListener
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ClassicalListener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClassicalLBTargetsRequest(AbstractModel):
    """DescribeClassicalLBTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        """
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClassicalLBTargetsResponse(AbstractModel):
    """DescribeClassicalLBTargets返回参数结构体

    """

    def __init__(self):
        """
        :param Targets: 后端服务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of ClassicalTarget
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Targets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClsLogSetRequest(AbstractModel):
    """DescribeClsLogSet请求参数结构体

    """


class DescribeClsLogSetResponse(AbstractModel):
    """DescribeClsLogSet返回参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集的 ID。
        :type LogsetId: str
        :param HealthLogsetId: 健康检查日志集的 ID。
        :type HealthLogsetId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogsetId = None
        self.HealthLogsetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.HealthLogsetId = params.get("HealthLogsetId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterResourcesRequest(AbstractModel):
    """DescribeClusterResources请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回集群中资源列表数目，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 返回集群中资源列表起始偏移量，默认为0。
        :type Offset: int
        :param Filters: 查询集群中资源列表条件，详细的过滤条件如下：
<li> cluster-id - String - 是否必填：否 - （过滤条件）按照 集群 的唯一ID过滤，如 ："tgw-12345678","stgw-12345678","vpcgw-12345678"。</li>
<li> vip - String - 是否必填：否 - （过滤条件）按照vip过滤。</li>
<li> loadblancer-id - String - 是否必填：否 - （过滤条件）按照负载均衡唯一ID过滤。</li>
<li> idle - String 是否必填：否 - （过滤条件）按照是否闲置过滤，如"True","False"。</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterResourcesResponse(AbstractModel):
    """DescribeClusterResources返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterResourceSet: 集群中资源列表。
        :type ClusterResourceSet: list of ClusterResource
        :param TotalCount: 集群中资源总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterResourceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterResourceSet") is not None:
            self.ClusterResourceSet = []
            for item in params.get("ClusterResourceSet"):
                obj = ClusterResource()
                obj._deserialize(item)
                self.ClusterResourceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeExclusiveClustersRequest(AbstractModel):
    """DescribeExclusiveClusters请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回集群列表数目，默认值为20，最大值为100。
        :type Limit: int
        :param Offset: 返回集群列表起始偏移量，默认为0。
        :type Offset: int
        :param Filters: 查询集群列表条件，详细的过滤条件如下：
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
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeExclusiveClustersResponse(AbstractModel):
    """DescribeExclusiveClusters返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterSet: 集群列表。
        :type ClusterSet: list of Cluster
        :param TotalCount: 集群总数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterSet") is not None:
            self.ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = Cluster()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerIds: 要查询的负载均衡监听器ID数组。
        :type ListenerIds: list of str
        :param Protocol: 要查询的监听器协议类型，取值 TCP | UDP | HTTP | HTTPS | TCP_SSL。
        :type Protocol: str
        :param Port: 要查询的监听器的端口。
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners返回参数结构体

    """

    def __init__(self):
        """
        :param Listeners: 监听器列表。
        :type Listeners: list of Listener
        :param TotalCount: 总的监听器个数（根据端口、协议、监听器ID过滤后）。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLoadBalancerListByCertIdRequest(AbstractModel):
    """DescribeLoadBalancerListByCertId请求参数结构体

    """

    def __init__(self):
        """
        :param CertIds: 服务端证书的ID，或客户端证书的ID
        :type CertIds: list of str
        """
        self.CertIds = None


    def _deserialize(self, params):
        self.CertIds = params.get("CertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLoadBalancerListByCertIdResponse(AbstractModel):
    """DescribeLoadBalancerListByCertId返回参数结构体

    """

    def __init__(self):
        """
        :param CertSet: 证书ID，以及与该证书ID关联的负载均衡实例列表
        :type CertSet: list of CertIdRelatedWithLoadBalancers
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertSet") is not None:
            self.CertSet = []
            for item in params.get("CertSet"):
                obj = CertIdRelatedWithLoadBalancers()
                obj._deserialize(item)
                self.CertSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLoadBalancerTrafficRequest(AbstractModel):
    """DescribeLoadBalancerTraffic请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerRegion: 负载均衡所在地域，不传默认返回所有地域负载均衡。
        :type LoadBalancerRegion: str
        """
        self.LoadBalancerRegion = None


    def _deserialize(self, params):
        self.LoadBalancerRegion = params.get("LoadBalancerRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLoadBalancerTrafficResponse(AbstractModel):
    """DescribeLoadBalancerTraffic返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerTraffic: 按出带宽从高到低排序后的负载均衡信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerTraffic: list of LoadBalancerTraffic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerTraffic = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerTraffic") is not None:
            self.LoadBalancerTraffic = []
            for item in params.get("LoadBalancerTraffic"):
                obj = LoadBalancerTraffic()
                obj._deserialize(item)
                self.LoadBalancerTraffic.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLoadBalancersDetailRequest(AbstractModel):
    """DescribeLoadBalancersDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回负载均衡列表数目，默认20，最大值100。
        :type Limit: int
        :param Offset: 返回负载均衡列表起始偏移量，默认0。
        :type Offset: int
        :param Fields: 选择返回的Fields列表，默认添加LoadBalancerId和LoadBalancerName。
        :type Fields: list of str
        :param TargetType: 当Fields包含TargetId、TargetAddress、TargetPort、TargetWeight等Fields时，必选选择导出目标组的Target或者非目标组Target，值范围NODE、GROUP。
        :type TargetType: str
        :param Filters: 查询负载均衡详细信息列表条件，详细的过滤条件如下：
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
        self.Limit = None
        self.Offset = None
        self.Fields = None
        self.TargetType = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Fields = params.get("Fields")
        self.TargetType = params.get("TargetType")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLoadBalancersDetailResponse(AbstractModel):
    """DescribeLoadBalancersDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 负载均衡详情列表总数。
        :type TotalCount: int
        :param LoadBalancerDetailSet: 负载均衡详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerDetailSet: list of LoadBalancerDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoadBalancerDetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerDetailSet") is not None:
            self.LoadBalancerDetailSet = []
            for item in params.get("LoadBalancerDetailSet"):
                obj = LoadBalancerDetail()
                obj._deserialize(item)
                self.LoadBalancerDetailSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 负载均衡实例ID。
        :type LoadBalancerIds: list of str
        :param LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
        :type LoadBalancerType: str
        :param Forward: 负载均衡实例的类型。1：通用的负载均衡实例，0：传统型负载均衡实例。如果不传此参数，则查询所有类型的负载均衡实例。
        :type Forward: int
        :param LoadBalancerName: 负载均衡实例的名称。
        :type LoadBalancerName: str
        :param Domain: 腾讯云为负载均衡实例分配的域名，本参数仅对传统型公网负载均衡才有意义。
        :type Domain: str
        :param LoadBalancerVips: 负载均衡实例的 VIP 地址，支持多个。
        :type LoadBalancerVips: list of str
        :param BackendPublicIps: 负载均衡绑定的后端服务的外网 IP。
        :type BackendPublicIps: list of str
        :param BackendPrivateIps: 负载均衡绑定的后端服务的内网 IP。
        :type BackendPrivateIps: list of str
        :param Offset: 数据偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回负载均衡实例的数量，默认为20，最大值为100。
        :type Limit: int
        :param OrderBy: 排序参数，支持以下字段：LoadBalancerName，CreateTime，Domain，LoadBalancerType。
        :type OrderBy: str
        :param OrderType: 1：倒序，0：顺序，默认按照创建时间倒序。
        :type OrderType: int
        :param SearchKey: 搜索字段，模糊匹配名称、域名、VIP。
        :type SearchKey: str
        :param ProjectId: 负载均衡实例所属的项目 ID，可以通过 DescribeProject 接口获取。
        :type ProjectId: int
        :param WithRs: 负载均衡是否绑定后端服务，0：没有绑定后端服务，1：绑定后端服务，-1：查询全部。
        :type WithRs: int
        :param VpcId: 负载均衡实例所属私有网络唯一ID，如 vpc-bhqkbhdx，
基础网络可传入'0'。
        :type VpcId: str
        :param SecurityGroup: 安全组ID，如 sg-m1cc****。
        :type SecurityGroup: str
        :param MasterZone: 主可用区ID，如 ："100001" （对应的是广州一区）。
        :type MasterZone: str
        :param Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为100。详细的过滤条件如下：
<li> internet-charge-type - String - 是否必填：否 - （过滤条件）按照 CLB 的网络计费模式过滤，包括"BANDWIDTH_PREPAID","TRAFFIC_POSTPAID_BY_HOUR","BANDWIDTH_POSTPAID_BY_HOUR","BANDWIDTH_PACKAGE"。</li>
<li> master-zone-id - String - 是否必填：否 - （过滤条件）按照 CLB 的主可用区ID过滤，如 ："100001" （对应的是广州一区）。</li>
<li> tag-key - String - 是否必填：否 - （过滤条件）按照 CLB 标签的键过滤。</li>
<li> tag:tag-key - String - 是否必填：否 - （过滤条件）按照CLB标签键值对进行过滤，tag-key使用具体的标签键进行替换。</li>
<li> function-name - String - 是否必填：否 - （过滤条件）按照 CLB 后端绑定的SCF云函数的函数名称过滤。</li>
<li> function-name - String - 是否必填：否 - （过滤条件）按照 CLB 后端绑定的SCF云函数的函数名称过滤。</li>
<li> vip-isp - String - 是否必填：否 - （过滤条件）按照 CLB VIP的运营商类型过滤，如："BGP","INTERNAL","CMCC","CTCC","CUCC"等。</li>
        :type Filters: list of Filter
        """
        self.LoadBalancerIds = None
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.BackendPublicIps = None
        self.BackendPrivateIps = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None
        self.SearchKey = None
        self.ProjectId = None
        self.WithRs = None
        self.VpcId = None
        self.SecurityGroup = None
        self.MasterZone = None
        self.Filters = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.BackendPublicIps = params.get("BackendPublicIps")
        self.BackendPrivateIps = params.get("BackendPrivateIps")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.SearchKey = params.get("SearchKey")
        self.ProjectId = params.get("ProjectId")
        self.WithRs = params.get("WithRs")
        self.VpcId = params.get("VpcId")
        self.SecurityGroup = params.get("SecurityGroup")
        self.MasterZone = params.get("MasterZone")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 满足过滤条件的负载均衡实例总数。此数值与入参中的Limit无关。
        :type TotalCount: int
        :param LoadBalancerSet: 返回的负载均衡实例数组。
        :type LoadBalancerSet: list of LoadBalancer
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeQuotaRequest(AbstractModel):
    """DescribeQuota请求参数结构体

    """


class DescribeQuotaResponse(AbstractModel):
    """DescribeQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaSet: 配额列表
        :type QuotaSet: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRewriteRequest(AbstractModel):
    """DescribeRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param SourceListenerIds: 负载均衡监听器ID数组。
        :type SourceListenerIds: list of str
        :param SourceLocationIds: 负载均衡转发规则的ID数组。
        :type SourceLocationIds: list of str
        """
        self.LoadBalancerId = None
        self.SourceListenerIds = None
        self.SourceLocationIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerIds = params.get("SourceListenerIds")
        self.SourceLocationIds = params.get("SourceLocationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRewriteResponse(AbstractModel):
    """DescribeRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param RewriteSet: 重定向转发规则构成的数组，若无重定向规则，则返回空数组。
        :type RewriteSet: list of RuleOutput
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RewriteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RewriteSet") is not None:
            self.RewriteSet = []
            for item in params.get("RewriteSet"):
                obj = RuleOutput()
                obj._deserialize(item)
                self.RewriteSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetGroupInstancesRequest(AbstractModel):
    """DescribeTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件，当前仅支持TargetGroupId，BindIP，InstanceId过滤
        :type Filters: list of Filter
        :param Limit: 显示数量限制，默认20
        :type Limit: int
        :param Offset: 显示的偏移量，默认为0
        :type Offset: int
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetGroupInstancesResponse(AbstractModel):
    """DescribeTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 本次查询的结果数量
        :type TotalCount: int
        :param TargetGroupInstanceSet: 绑定的服务器信息
        :type TargetGroupInstanceSet: list of TargetGroupBackend
        :param RealCount: 实际统计数量，不受Limit，Offset，CAM的影响
        :type RealCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupInstanceSet = None
        self.RealCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupInstanceSet") is not None:
            self.TargetGroupInstanceSet = []
            for item in params.get("TargetGroupInstanceSet"):
                obj = TargetGroupBackend()
                obj._deserialize(item)
                self.TargetGroupInstanceSet.append(obj)
        self.RealCount = params.get("RealCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetGroupListRequest(AbstractModel):
    """DescribeTargetGroupList请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupIds: 目标组ID数组。
        :type TargetGroupIds: list of str
        :param Filters: 过滤条件数组，支持TargetGroupVpcId和TargetGroupName。与TargetGroupIds互斥，优先使用目标组ID。
        :type Filters: list of Filter
        :param Offset: 显示的偏移起始量。
        :type Offset: int
        :param Limit: 显示条数限制，默认为20。
        :type Limit: int
        """
        self.TargetGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetGroupListResponse(AbstractModel):
    """DescribeTargetGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 显示的结果数量。
        :type TotalCount: int
        :param TargetGroupSet: 显示的目标组信息集合。
        :type TargetGroupSet: list of TargetGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self.TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self.TargetGroupSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetGroupsRequest(AbstractModel):
    """DescribeTargetGroups请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupIds: 目标组ID，与Filters互斥。
        :type TargetGroupIds: list of str
        :param Limit: 显示条数限制，默认为20。
        :type Limit: int
        :param Offset: 显示的偏移起始量。
        :type Offset: int
        :param Filters: 过滤条件数组，与TargetGroupIds互斥，支持TargetGroupVpcId和TargetGroupName。
        :type Filters: list of Filter
        """
        self.TargetGroupIds = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetGroupsResponse(AbstractModel):
    """DescribeTargetGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 显示的结果数量。
        :type TotalCount: int
        :param TargetGroupSet: 显示的目标组信息集合。
        :type TargetGroupSet: list of TargetGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self.TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self.TargetGroupSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 要查询的负载均衡实例ID列表。
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancers: 负载均衡实例列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancers: list of LoadBalancerHealth
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancers = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerIds: 监听器ID列表。
        :type ListenerIds: list of str
        :param Protocol: 监听器协议类型。
        :type Protocol: str
        :param Port: 监听器端口。
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets返回参数结构体

    """

    def __init__(self):
        """
        :param Listeners: 监听器后端绑定的机器信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ListenerBackend
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 请求ID，即接口返回的 RequestId 参数。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务的当前状态。 0：成功，1：失败，2：进行中。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisassociateTargetGroupsRequest(AbstractModel):
    """DisassociateTargetGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Associations: 待解绑的规则关系数组。
        :type Associations: list of TargetGroupAssociation
        """
        self.Associations = None


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self.Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self.Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisassociateTargetGroupsResponse(AbstractModel):
    """DisassociateTargetGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExclusiveCluster(AbstractModel):
    """独占集群

    """

    def __init__(self):
        """
        :param L4Clusters: 4层独占集群列表
注意：此字段可能返回 null，表示取不到有效值。
        :type L4Clusters: list of ClusterItem
        :param L7Clusters: 7层独占集群列表
注意：此字段可能返回 null，表示取不到有效值。
        :type L7Clusters: list of ClusterItem
        :param ClassicalCluster: vpcgw集群
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassicalCluster: :class:`tencentcloud.clb.v20180317.models.ClusterItem`
        """
        self.L4Clusters = None
        self.L7Clusters = None
        self.ClassicalCluster = None


    def _deserialize(self, params):
        if params.get("L4Clusters") is not None:
            self.L4Clusters = []
            for item in params.get("L4Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self.L4Clusters.append(obj)
        if params.get("L7Clusters") is not None:
            self.L7Clusters = []
            for item in params.get("L7Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self.L7Clusters.append(obj)
        if params.get("ClassicalCluster") is not None:
            self.ClassicalCluster = ClusterItem()
            self.ClassicalCluster._deserialize(params.get("ClassicalCluster"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExtraInfo(AbstractModel):
    """暂做保留，一般用户无需关注。

    """

    def __init__(self):
        """
        :param ZhiTong: 是否开通VIP直通
注意：此字段可能返回 null，表示取不到有效值。
        :type ZhiTong: bool
        :param TgwGroupName: TgwGroup名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TgwGroupName: str
        """
        self.ZhiTong = None
        self.TgwGroupName = None


    def _deserialize(self, params):
        self.ZhiTong = params.get("ZhiTong")
        self.TgwGroupName = params.get("TgwGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Filter(AbstractModel):
    """过滤器条件

    """

    def __init__(self):
        """
        :param Name: 过滤器的名称
        :type Name: str
        :param Values: 过滤器的值数组
        :type Values: list of str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HealthCheck(AbstractModel):
    """健康检查信息。
    注意，自定义探测相关参数 目前只有少量区域灰度支持。

    """

    def __init__(self):
        """
        :param HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）。
        :type HealthSwitch: int
        :param TimeOut: 健康检查的响应超时时间（仅适用于四层监听器），可选值：2~60，默认值：2，单位：秒。响应超时时间要小于检查间隔时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOut: int
        :param IntervalTime: 健康检查探测间隔时间，默认值：5，可选值：5~300，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntervalTime: int
        :param HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthNum: int
        :param UnHealthNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发异常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnHealthNum: int
        :param HttpCode: 健康检查状态码（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式）。可选值：1~31，默认 31。
1 表示探测后返回值 1xx 代表健康，2 表示返回 2xx 代表健康，4 表示返回 3xx 代表健康，8 表示返回 4xx 代表健康，16 表示返回 5xx 代表健康。若希望多种返回码都可代表健康，则将相应的值相加。注意：TCP监听器的HTTP健康检查方式，只支持指定一种健康检查状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpCode: int
        :param HttpCheckPath: 健康检查路径（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式）。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpCheckPath: str
        :param HttpCheckDomain: 健康检查域名（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式）。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpCheckDomain: str
        :param HttpCheckMethod: 健康检查方法（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式），默认值：HEAD，可选值HEAD或GET。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpCheckMethod: str
        :param CheckPort: 自定义探测相关参数。健康检查端口，默认为后端服务的端口，除非您希望指定特定端口，否则建议留空。（仅适用于TCP/UDP监听器）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPort: int
        :param ContextType: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查的输入格式，可取值：HEX或TEXT；取值为HEX时，SendContext和RecvContext的字符只能在0123456789ABCDEF中选取且长度必须是偶数位。（仅适用于TCP/UDP监听器）
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextType: str
        :param SendContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查发送的请求内容，只允许ASCII可见字符，最大长度限制500。（仅适用于TCP/UDP监听器）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SendContext: str
        :param RecvContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查返回的结果，只允许ASCII可见字符，最大长度限制500。（仅适用于TCP/UDP监听器）。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecvContext: str
        :param CheckType: 自定义探测相关参数。健康检查使用的协议：TCP | HTTP | CUSTOM（仅适用于TCP/UDP监听器，其中UDP监听器只支持CUSTOM；如果使用自定义健康检查功能，则必传）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckType: str
        :param HttpVersion: 自定义探测相关参数。健康检查协议CheckType的值取HTTP时，必传此字段，代表后端服务的HTTP版本：HTTP/1.0、HTTP/1.1；（仅适用于TCP监听器）
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpVersion: str
        """
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnHealthNum = None
        self.HttpCode = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.HttpCheckMethod = None
        self.CheckPort = None
        self.ContextType = None
        self.SendContext = None
        self.RecvContext = None
        self.CheckType = None
        self.HttpVersion = None


    def _deserialize(self, params):
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnHealthNum = params.get("UnHealthNum")
        self.HttpCode = params.get("HttpCode")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.HttpCheckMethod = params.get("HttpCheckMethod")
        self.CheckPort = params.get("CheckPort")
        self.ContextType = params.get("ContextType")
        self.SendContext = params.get("SendContext")
        self.RecvContext = params.get("RecvContext")
        self.CheckType = params.get("CheckType")
        self.HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InternetAccessible(AbstractModel):
    """网络计费模式，最大出带宽

    """

    def __init__(self):
        """
        :param InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR 按流量按小时后计费 ; BANDWIDTH_POSTPAID_BY_HOUR 按带宽按小时后计费;
BANDWIDTH_PACKAGE 按带宽包计费;
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 最大出带宽，单位Mbps，范围支持0到2048，仅对公网属性的LB生效，默认值 10
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param BandwidthpkgSubType: 带宽包的类型，如SINGLEISP
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthpkgSubType: str
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.BandwidthpkgSubType = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.BandwidthpkgSubType = params.get("BandwidthpkgSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LBChargePrepaid(AbstractModel):
    """lb实例包年包月相关配置属性

    """

    def __init__(self):
        """
        :param RenewFlag: 续费类型：AUTO_RENEW 自动续费，  MANUAL_RENEW 手动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        :param Period: 购买时长，单位：月
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        """
        self.RenewFlag = None
        self.Period = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Listener(AbstractModel):
    """监听器的信息

    """

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Protocol: 监听器协议
        :type Protocol: str
        :param Port: 监听器端口
        :type Port: int
        :param Certificate: 监听器绑定的证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param HealthCheck: 监听器的健康检查信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Scheduler: 请求的调度方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheduler: str
        :param SessionExpireTime: 会话保持时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionExpireTime: int
        :param SniSwitch: 是否开启SNI特性（本参数仅对于HTTPS监听器有意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type SniSwitch: int
        :param Rules: 监听器下的全部转发规则（本参数仅对于HTTP/HTTPS监听器有意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of RuleOutput
        :param ListenerName: 监听器的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param CreateTime: 监听器的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param EndPort: 端口段结束端口
注意：此字段可能返回 null，表示取不到有效值。
        :type EndPort: int
        :param TargetType: 后端服务器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetType: str
        :param TargetGroup: 绑定的目标组基本信息；当监听器绑定目标组时，会返回该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param SessionType: 会话保持类型。NORMAL表示默认会话保持类型。QUIC_CID 表示根据Quic Connection ID做会话保持。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionType: str
        :param KeepaliveEnable: 是否开启长连接，1开启，0关闭，（本参数仅对于HTTP/HTTPS监听器有意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepaliveEnable: int
        :param Toa: 仅支持Nat64 CLB TCP监听器
注意：此字段可能返回 null，表示取不到有效值。
        :type Toa: bool
        :param DeregisterTargetRst: 解绑后端目标时，是否发RST给客户端，（此参数仅对于TCP监听器有意义）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeregisterTargetRst: bool
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Certificate = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.SniSwitch = None
        self.Rules = None
        self.ListenerName = None
        self.CreateTime = None
        self.EndPort = None
        self.TargetType = None
        self.TargetGroup = None
        self.SessionType = None
        self.KeepaliveEnable = None
        self.Toa = None
        self.DeregisterTargetRst = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateOutput()
            self.Certificate._deserialize(params.get("Certificate"))
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.SniSwitch = params.get("SniSwitch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleOutput()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.ListenerName = params.get("ListenerName")
        self.CreateTime = params.get("CreateTime")
        self.EndPort = params.get("EndPort")
        self.TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self.TargetGroup = BasicTargetGroupInfo()
            self.TargetGroup._deserialize(params.get("TargetGroup"))
        self.SessionType = params.get("SessionType")
        self.KeepaliveEnable = params.get("KeepaliveEnable")
        self.Toa = params.get("Toa")
        self.DeregisterTargetRst = params.get("DeregisterTargetRst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListenerBackend(AbstractModel):
    """监听器上绑定的后端服务的信息

    """

    def __init__(self):
        """
        :param ListenerId: 监听器 ID
        :type ListenerId: str
        :param Protocol: 监听器的协议
        :type Protocol: str
        :param Port: 监听器的端口
        :type Port: int
        :param Rules: 监听器下的规则信息（仅适用于HTTP/HTTPS监听器）
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of RuleTargets
        :param Targets: 监听器上绑定的后端服务列表（仅适用于TCP/UDP/TCP_SSL监听器）
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of Backend
        :param EndPort: 若支持端口段，则为端口段结束端口；若不支持端口段，则为0
注意：此字段可能返回 null，表示取不到有效值。
        :type EndPort: int
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Rules = None
        self.Targets = None
        self.EndPort = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleTargets()
                obj._deserialize(item)
                self.Rules.append(obj)
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListenerHealth(AbstractModel):
    """监听器的健康检查信息

    """

    def __init__(self):
        """
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param ListenerName: 监听器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param Protocol: 监听器的协议
        :type Protocol: str
        :param Port: 监听器的端口
        :type Port: int
        :param Rules: 监听器的转发规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of RuleHealth
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.Port = None
        self.Rules = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LoadBalancer(AbstractModel):
    """负载均衡实例的信息

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param LoadBalancerName: 负载均衡实例的名称。
        :type LoadBalancerName: str
        :param LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
        :type LoadBalancerType: str
        :param Forward: 负载均衡类型标识，1：负载均衡，0：传统型负载均衡。
        :type Forward: int
        :param Domain: 负载均衡实例的域名，仅公网传统型负载均衡实例才提供该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param LoadBalancerVips: 负载均衡实例的 VIP 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerVips: list of str
        :param Status: 负载均衡实例的状态，包括
0：创建中，1：正常运行。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CreateTime: 负载均衡实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param StatusTime: 负载均衡实例的上次状态转换时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusTime: str
        :param ProjectId: 负载均衡实例所属的项目 ID， 0 表示默认项目。
        :type ProjectId: int
        :param VpcId: 私有网络的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param OpenBgp: 高防 LB 的标识，1：高防负载均衡 0：非高防负载均衡。
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenBgp: int
        :param Snat: 在 2016 年 12 月份之前的传统型内网负载均衡都是开启了 snat 的。
注意：此字段可能返回 null，表示取不到有效值。
        :type Snat: bool
        :param Isolation: 0：表示未被隔离，1：表示被隔离。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isolation: int
        :param Log: 用户开启日志的信息，日志只有公网属性创建了 HTTP 、HTTPS 监听器的负载均衡才会有日志。
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: str
        :param SubnetId: 负载均衡实例所在的子网（仅对内网VPC型LB有意义）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Tags: 负载均衡实例的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param SecureGroups: 负载均衡实例的安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecureGroups: list of str
        :param TargetRegionInfo: 负载均衡实例绑定的后端设备的基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param AnycastZone: anycast负载均衡的发布域，对于非anycast的负载均衡，此字段返回为空字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type AnycastZone: str
        :param AddressIPVersion: IP版本，ipv4 | ipv6
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPVersion: str
        :param NumericalVpcId: 数值形式的私有网络 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NumericalVpcId: int
        :param VipIsp: 负载均衡IP地址所属的ISP
注意：此字段可能返回 null，表示取不到有效值。
        :type VipIsp: str
        :param MasterZone: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: :class:`tencentcloud.clb.v20180317.models.ZoneInfo`
        :param BackupZoneSet: 备可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupZoneSet: list of ZoneInfo
        :param IsolatedTime: 负载均衡实例被隔离的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param ExpireTime: 负载均衡实例的过期时间，仅对预付费负载均衡生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param ChargeType: 负载均衡实例的计费类型，PREPAID：包年包月，POSTPAID_BY_HOUR：按量计费
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param NetworkAttributes: 负载均衡实例的网络属性
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param PrepaidAttributes: 负载均衡实例的预付费相关属性
注意：此字段可能返回 null，表示取不到有效值。
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param LogSetId: 负载均衡日志服务(CLS)的日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSetId: str
        :param LogTopicId: 负载均衡日志服务(CLS)的日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        :param AddressIPv6: 负载均衡实例的IPv6地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPv6: str
        :param ExtraInfo: 暂做保留，一般用户无需关注。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param IsDDos: 是否可绑定高防包
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDDos: bool
        :param ConfigId: 负载均衡维度的个性化配置ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param LoadBalancerPassToTarget: 后端服务是否放通来自LB的流量
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerPassToTarget: bool
        :param ExclusiveCluster: 内网独占集群
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param IPv6Mode: IP地址版本为ipv6时此字段有意义， IPv6Nat64 | IPv6FullChain
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6Mode: str
        :param SnatPro: 是否开启SnatPro。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnatPro: bool
        :param SnatIps: 开启SnatPro负载均衡后，SnatIp列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnatIps: list of SnatIp
        :param SlaType: 性能保障规格
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaType: str
        :param IsBlock: vip是否被封堵
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBlock: bool
        :param IsBlockTime: 封堵或解封时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBlockTime: str
        :param LocalBgp: IP类型是否是本地BGP
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalBgp: bool
        :param ClusterTag: 7层独占标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterTag: str
        :param MixIpTarget: 开启IPv6FullChain负载均衡7层监听器支持混绑IPv4/IPv6目标功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type MixIpTarget: bool
        :param Zones: 私有网络内网负载均衡，就近接入模式下规则所落在的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        :param NfvInfo: CLB是否为NFV，空：不是，l7nfv：七层是NFV。
注意：此字段可能返回 null，表示取不到有效值。
        :type NfvInfo: str
        :param HealthLogSetId: 负载均衡日志服务(CLS)的健康检查日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthLogSetId: str
        :param HealthLogTopicId: 负载均衡日志服务(CLS)的健康检查日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthLogTopicId: str
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.Forward = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.Status = None
        self.CreateTime = None
        self.StatusTime = None
        self.ProjectId = None
        self.VpcId = None
        self.OpenBgp = None
        self.Snat = None
        self.Isolation = None
        self.Log = None
        self.SubnetId = None
        self.Tags = None
        self.SecureGroups = None
        self.TargetRegionInfo = None
        self.AnycastZone = None
        self.AddressIPVersion = None
        self.NumericalVpcId = None
        self.VipIsp = None
        self.MasterZone = None
        self.BackupZoneSet = None
        self.IsolatedTime = None
        self.ExpireTime = None
        self.ChargeType = None
        self.NetworkAttributes = None
        self.PrepaidAttributes = None
        self.LogSetId = None
        self.LogTopicId = None
        self.AddressIPv6 = None
        self.ExtraInfo = None
        self.IsDDos = None
        self.ConfigId = None
        self.LoadBalancerPassToTarget = None
        self.ExclusiveCluster = None
        self.IPv6Mode = None
        self.SnatPro = None
        self.SnatIps = None
        self.SlaType = None
        self.IsBlock = None
        self.IsBlockTime = None
        self.LocalBgp = None
        self.ClusterTag = None
        self.MixIpTarget = None
        self.Zones = None
        self.NfvInfo = None
        self.HealthLogSetId = None
        self.HealthLogTopicId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StatusTime = params.get("StatusTime")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.OpenBgp = params.get("OpenBgp")
        self.Snat = params.get("Snat")
        self.Isolation = params.get("Isolation")
        self.Log = params.get("Log")
        self.SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SecureGroups = params.get("SecureGroups")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        self.AnycastZone = params.get("AnycastZone")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.NumericalVpcId = params.get("NumericalVpcId")
        self.VipIsp = params.get("VipIsp")
        if params.get("MasterZone") is not None:
            self.MasterZone = ZoneInfo()
            self.MasterZone._deserialize(params.get("MasterZone"))
        if params.get("BackupZoneSet") is not None:
            self.BackupZoneSet = []
            for item in params.get("BackupZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.BackupZoneSet.append(obj)
        self.IsolatedTime = params.get("IsolatedTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self.NetworkAttributes = InternetAccessible()
            self.NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self.PrepaidAttributes = LBChargePrepaid()
            self.PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")
        self.AddressIPv6 = params.get("AddressIPv6")
        if params.get("ExtraInfo") is not None:
            self.ExtraInfo = ExtraInfo()
            self.ExtraInfo._deserialize(params.get("ExtraInfo"))
        self.IsDDos = params.get("IsDDos")
        self.ConfigId = params.get("ConfigId")
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        if params.get("ExclusiveCluster") is not None:
            self.ExclusiveCluster = ExclusiveCluster()
            self.ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self.IPv6Mode = params.get("IPv6Mode")
        self.SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)
        self.SlaType = params.get("SlaType")
        self.IsBlock = params.get("IsBlock")
        self.IsBlockTime = params.get("IsBlockTime")
        self.LocalBgp = params.get("LocalBgp")
        self.ClusterTag = params.get("ClusterTag")
        self.MixIpTarget = params.get("MixIpTarget")
        self.Zones = params.get("Zones")
        self.NfvInfo = params.get("NfvInfo")
        self.HealthLogSetId = params.get("HealthLogSetId")
        self.HealthLogTopicId = params.get("HealthLogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LoadBalancerDetail(AbstractModel):
    """负载均衡详细信息

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param LoadBalancerName: 负载均衡实例的名称。
        :type LoadBalancerName: str
        :param LoadBalancerType: 负载均衡实例的网络类型：
Public：公网属性， Private：内网属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param Status: 负载均衡实例的状态，包括
0：创建中，1：正常运行。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Address: 负载均衡实例的 VIP 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param AddressIPv6: 负载均衡实例 VIP 的IPv6地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPv6: str
        :param AddressIPVersion: 负载均衡实例IP版本，IPv4 | IPv6。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPVersion: str
        :param IPv6Mode: 负载均衡实例IPv6地址类型，IPv6Nat64 | IPv6FullChain。
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6Mode: str
        :param Zone: 负载均衡实例所在可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param AddressIsp: 负载均衡实例IP地址所属的ISP。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIsp: str
        :param VpcId: 负载均衡实例所属私有网络的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param ProjectId: 负载均衡实例所属的项目 ID， 0 表示默认项目。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param CreateTime: 负载均衡实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ChargeType: 负载均衡实例的计费类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param NetworkAttributes: 负载均衡实例的网络属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param PrepaidAttributes: 负载均衡实例的预付费相关属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param ExtraInfo: 暂做保留，一般用户无需关注。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param ConfigId: 负载均衡维度的个性化配置ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param Tags: 负载均衡实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param ListenerId: 负载均衡监听器 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param Protocol: 监听器协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param Port: 监听器端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param LocationId: 转发规则的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationId: str
        :param Domain: 转发规则的域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Url: 转发规则的路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param TargetId: 后端目标ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetId: str
        :param TargetAddress: 后端目标的IP地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAddress: str
        :param TargetPort: 后端目标监听端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetPort: int
        :param TargetWeight: 后端目标转发权重。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetWeight: int
        :param Isolation: 0：表示未被隔离，1：表示被隔离。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isolation: int
        :param SecurityGroup: 负载均衡绑定的安全组列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroup: list of str
        :param LoadBalancerPassToTarget: 负载均衡安全组上移特性是否开启标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerPassToTarget: int
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.Status = None
        self.Address = None
        self.AddressIPv6 = None
        self.AddressIPVersion = None
        self.IPv6Mode = None
        self.Zone = None
        self.AddressIsp = None
        self.VpcId = None
        self.ProjectId = None
        self.CreateTime = None
        self.ChargeType = None
        self.NetworkAttributes = None
        self.PrepaidAttributes = None
        self.ExtraInfo = None
        self.ConfigId = None
        self.Tags = None
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.TargetId = None
        self.TargetAddress = None
        self.TargetPort = None
        self.TargetWeight = None
        self.Isolation = None
        self.SecurityGroup = None
        self.LoadBalancerPassToTarget = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Status = params.get("Status")
        self.Address = params.get("Address")
        self.AddressIPv6 = params.get("AddressIPv6")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.IPv6Mode = params.get("IPv6Mode")
        self.Zone = params.get("Zone")
        self.AddressIsp = params.get("AddressIsp")
        self.VpcId = params.get("VpcId")
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self.NetworkAttributes = InternetAccessible()
            self.NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self.PrepaidAttributes = LBChargePrepaid()
            self.PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        if params.get("ExtraInfo") is not None:
            self.ExtraInfo = ExtraInfo()
            self.ExtraInfo._deserialize(params.get("ExtraInfo"))
        self.ConfigId = params.get("ConfigId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.TargetId = params.get("TargetId")
        self.TargetAddress = params.get("TargetAddress")
        self.TargetPort = params.get("TargetPort")
        self.TargetWeight = params.get("TargetWeight")
        self.Isolation = params.get("Isolation")
        self.SecurityGroup = params.get("SecurityGroup")
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LoadBalancerHealth(AbstractModel):
    """负载均衡实例的健康检查状态

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param LoadBalancerName: 负载均衡实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param Listeners: 监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ListenerHealth
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Listeners = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self.Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LoadBalancerTraffic(AbstractModel):
    """负载均衡流量数据。

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param LoadBalancerName: 负载均衡名字
        :type LoadBalancerName: str
        :param Region: 负载均衡所在地域
        :type Region: str
        :param Vip: 负载均衡的vip
        :type Vip: str
        :param OutBandwidth: 最大出带宽，单位：Mbps
        :type OutBandwidth: float
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Region = None
        self.Vip = None
        self.OutBandwidth = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.Region = params.get("Region")
        self.Vip = params.get("Vip")
        self.OutBandwidth = params.get("OutBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ManualRewriteRequest(AbstractModel):
    """ManualRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param SourceListenerId: 源监听器 ID。
        :type SourceListenerId: str
        :param TargetListenerId: 目标监听器 ID。
        :type TargetListenerId: str
        :param RewriteInfos: 转发规则之间的重定向关系。
        :type RewriteInfos: list of RewriteLocationMap
        """
        self.LoadBalancerId = None
        self.SourceListenerId = None
        self.TargetListenerId = None
        self.RewriteInfos = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerId = params.get("SourceListenerId")
        self.TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self.RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self.RewriteInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ManualRewriteResponse(AbstractModel):
    """ManualRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyBlockIPListRequest(AbstractModel):
    """ModifyBlockIPList请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 负载均衡实例ID
        :type LoadBalancerIds: list of str
        :param Type: 操作类型，可取：
<li> add_customized_field（首次设置header，开启黑名单功能）</li>
<li> set_customized_field（修改header）</li>
<li> del_customized_field（删除header）</li>
<li> add_blocked（添加黑名单）</li>
<li> del_blocked（删除黑名单）</li>
<li> flush_blocked（清空黑名单）</li>
        :type Type: str
        :param ClientIPField: 客户端真实IP存放的header字段名
        :type ClientIPField: str
        :param BlockIPList: 封禁IP列表，单次操作数组最大长度支持200000
        :type BlockIPList: list of str
        :param ExpireTime: 过期时间，单位秒，默认值3600
        :type ExpireTime: int
        :param AddStrategy: 添加IP的策略，可取：fifo（如果黑名单容量已满，新加入黑名单的IP采用先进先出策略）
        :type AddStrategy: str
        """
        self.LoadBalancerIds = None
        self.Type = None
        self.ClientIPField = None
        self.BlockIPList = None
        self.ExpireTime = None
        self.AddStrategy = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.Type = params.get("Type")
        self.ClientIPField = params.get("ClientIPField")
        self.BlockIPList = params.get("BlockIPList")
        self.ExpireTime = params.get("ExpireTime")
        self.AddStrategy = params.get("AddStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyBlockIPListResponse(AbstractModel):
    """ModifyBlockIPList返回参数结构体

    """

    def __init__(self):
        """
        :param JodId: 异步任务的ID
        :type JodId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JodId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JodId = params.get("JodId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDomainAttributesRequest(AbstractModel):
    """ModifyDomainAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param Domain: 域名（必须是已经创建的转发规则下的域名）。
        :type Domain: str
        :param NewDomain: 要修改的新域名。
        :type NewDomain: str
        :param Certificate: 域名相关的证书信息，注意，仅对启用SNI的监听器适用。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Http2: 是否开启Http2，注意，只有HTTPS域名才能开启Http2。
        :type Http2: bool
        :param DefaultServer: 是否设为默认域名，注意，一个监听器下只能设置一个默认域名。
        :type DefaultServer: bool
        :param NewDefaultServerDomain: 监听器下必须配置一个默认域名，若要关闭原默认域名，必须同时指定另一个域名作为新的默认域名。
        :type NewDefaultServerDomain: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.NewDomain = None
        self.Certificate = None
        self.Http2 = None
        self.DefaultServer = None
        self.NewDefaultServerDomain = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.NewDomain = params.get("NewDomain")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Http2 = params.get("Http2")
        self.DefaultServer = params.get("DefaultServer")
        self.NewDefaultServerDomain = params.get("NewDefaultServerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDomainAttributesResponse(AbstractModel):
    """ModifyDomainAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Domain: 监听器下的某个旧域名。
        :type Domain: str
        :param NewDomain: 新域名，	长度限制为：1-120。有三种使用格式：非正则表达式格式，通配符格式，正则表达式格式。非正则表达式格式只能使用字母、数字、‘-’、‘.’。通配符格式的使用 ‘*’ 只能在开头或者结尾。正则表达式以'~'开头。
        :type NewDomain: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.NewDomain = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.NewDomain = params.get("NewDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDomainResponse(AbstractModel):
    """ModifyDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyListenerRequest(AbstractModel):
    """ModifyListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param ListenerName: 新的监听器名称。
        :type ListenerName: str
        :param SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :type SessionExpireTime: int
        :param HealthCheck: 健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL监听器。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 证书相关信息，此参数仅适用于HTTPS/TCP_SSL监听器。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。
        :type Scheduler: str
        :param SniSwitch: 是否开启SNI特性，此参数仅适用于HTTPS监听器。注意：未开启SNI的监听器可以开启SNI；已开启SNI的监听器不能关闭SNI。
        :type SniSwitch: int
        :param KeepaliveEnable: 是否开启长连接，此参数仅适用于HTTP/HTTPS监听器。
        :type KeepaliveEnable: int
        :param DeregisterTargetRst: 解绑后端目标时，是否发RST给客户端，此参数仅适用于TCP监听器。
        :type DeregisterTargetRst: bool
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.SniSwitch = None
        self.KeepaliveEnable = None
        self.DeregisterTargetRst = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.SniSwitch = params.get("SniSwitch")
        self.KeepaliveEnable = params.get("KeepaliveEnable")
        self.DeregisterTargetRst = params.get("DeregisterTargetRst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyListenerResponse(AbstractModel):
    """ModifyListener返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡的唯一ID
        :type LoadBalancerId: str
        :param LoadBalancerName: 负载均衡实例名称
        :type LoadBalancerName: str
        :param TargetRegionInfo: 负载均衡绑定的后端服务的地域信息
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param InternetChargeInfo: 网络计费相关参数
        :type InternetChargeInfo: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param LoadBalancerPassToTarget: Target是否放通来自CLB的流量。开启放通（true）：只验证CLB上的安全组；不开启放通（false）：需同时验证CLB和后端实例上的安全组。
        :type LoadBalancerPassToTarget: bool
        :param SnatPro: 是否开启SnatPro
        :type SnatPro: bool
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.TargetRegionInfo = None
        self.InternetChargeInfo = None
        self.LoadBalancerPassToTarget = None
        self.SnatPro = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        if params.get("InternetChargeInfo") is not None:
            self.InternetChargeInfo = InternetAccessible()
            self.InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self.SnatPro = params.get("SnatPro")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 切换负载均衡计费方式时，可用此参数查询切换任务是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID。
        :type ListenerId: str
        :param LocationId: 要修改的转发规则的 ID。
        :type LocationId: str
        :param Url: 转发规则的新的转发路径，如不需修改Url，则不需提供此参数。
        :type Url: str
        :param HealthCheck: 健康检查信息。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Scheduler: 规则的请求转发方式，可选值：WRR、LEAST_CONN、IP_HASH
分别表示按权重轮询、最小连接数、按IP哈希， 默认为 WRR。
        :type Scheduler: str
        :param SessionExpireTime: 会话保持时间。
        :type SessionExpireTime: int
        :param ForwardType: 负载均衡实例与后端服务之间的转发协议，默认HTTP，可取值：HTTP、HTTPS、TRPC。
        :type ForwardType: str
        :param TrpcCallee: TRPC被调服务器路由，ForwardType为TRPC时必填。
        :type TrpcCallee: str
        :param TrpcFunc: TRPC调用服务接口，ForwardType为TRPC时必填。
        :type TrpcFunc: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Url = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.ForwardType = None
        self.TrpcCallee = None
        self.TrpcFunc = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Url = params.get("Url")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.ForwardType = params.get("ForwardType")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetGroupAttributeRequest(AbstractModel):
    """ModifyTargetGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标组的ID。
        :type TargetGroupId: str
        :param TargetGroupName: 目标组的新名称。
        :type TargetGroupName: str
        :param Port: 目标组的新默认端口。
        :type Port: int
        """
        self.TargetGroupId = None
        self.TargetGroupName = None
        self.Port = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.TargetGroupName = params.get("TargetGroupName")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetGroupAttributeResponse(AbstractModel):
    """ModifyTargetGroupAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetGroupInstancesPortRequest(AbstractModel):
    """ModifyTargetGroupInstancesPort请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        :param TargetGroupInstances: 待修改端口的服务器数组。
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetGroupInstancesPortResponse(AbstractModel):
    """ModifyTargetGroupInstancesPort返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetGroupInstancesWeightRequest(AbstractModel):
    """ModifyTargetGroupInstancesWeight请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        :param TargetGroupInstances: 待修改权重的服务器数组。
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetGroupInstancesWeightResponse(AbstractModel):
    """ModifyTargetGroupInstancesWeight返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param Targets: 要修改端口的后端服务列表。
        :type Targets: list of Target
        :param NewPort: 后端服务绑定到监听器或转发规则的新端口。
        :type NewPort: int
        :param LocationId: 转发规则的ID，当后端服务绑定到七层转发规则时，必须提供此参数或Domain+Url两者之一。
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.NewPort = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.NewPort = params.get("NewPort")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param LocationId: 转发规则的ID，当绑定机器到七层转发规则时，必须提供此参数或Domain+Url两者之一。
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        :param Targets: 要修改权重的后端服务列表。
        :type Targets: list of Target
        :param Weight: 后端服务新的转发权重，取值范围：0~100，默认值10。如果设置了 Targets.Weight 参数，则此参数不生效。
        :type Weight: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None
        self.Weight = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Quota(AbstractModel):
    """描述配额信息，所有配额均指当前地域下的配额。

    """

    def __init__(self):
        """
        :param QuotaId: 配额名称，取值范围：
<li> TOTAL_OPEN_CLB_QUOTA: 用户当前地域下的公网LB配额 </li>
<li> TOTAL_INTERNAL_CLB_QUOTA: 用户当前地域下的内网LB配额 </li>
<li> TOTAL_LISTENER_QUOTA: 一个CLB下的监听器配额 </li>
<li> TOTAL_LISTENER_RULE_QUOTA: 一个监听器下的转发规则配额 </li>
<li> TOTAL_TARGET_BIND_QUOTA: 一条转发规则下绑定设备配额 </li>
        :type QuotaId: str
        :param QuotaCurrent: 当前使用数量，为 null 时表示无意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaCurrent: int
        :param QuotaLimit: 配额数量。
        :type QuotaLimit: int
        """
        self.QuotaId = None
        self.QuotaCurrent = None
        self.QuotaLimit = None


    def _deserialize(self, params):
        self.QuotaId = params.get("QuotaId")
        self.QuotaCurrent = params.get("QuotaCurrent")
        self.QuotaLimit = params.get("QuotaLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegisterTargetGroupInstancesRequest(AbstractModel):
    """RegisterTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 服务器实例数组
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegisterTargetGroupInstancesResponse(AbstractModel):
    """RegisterTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegisterTargetsRequest(AbstractModel):
    """RegisterTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID。
        :type ListenerId: str
        :param Targets: 待绑定的后端服务列表，数组长度最大支持20。
        :type Targets: list of Target
        :param LocationId: 转发规则的ID，当绑定后端服务到七层转发规则时，必须提供此参数或Domain+Url两者之一。
        :type LocationId: str
        :param Domain: 目标转发规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param Url: 目标转发规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegisterTargetsResponse(AbstractModel):
    """RegisterTargets返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegisterTargetsWithClassicalLBRequest(AbstractModel):
    """RegisterTargetsWithClassicalLB请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID。
        :type LoadBalancerId: str
        :param Targets: 后端服务信息。
        :type Targets: list of ClassicalTargetInfo
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTargetInfo()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegisterTargetsWithClassicalLBResponse(AbstractModel):
    """RegisterTargetsWithClassicalLB返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReplaceCertForLoadBalancersRequest(AbstractModel):
    """ReplaceCertForLoadBalancers请求参数结构体

    """

    def __init__(self):
        """
        :param OldCertificateId: 需要被替换的证书的ID，可以是服务端证书或客户端证书
        :type OldCertificateId: str
        :param Certificate: 新证书的内容等相关信息
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        """
        self.OldCertificateId = None
        self.Certificate = None


    def _deserialize(self, params):
        self.OldCertificateId = params.get("OldCertificateId")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReplaceCertForLoadBalancersResponse(AbstractModel):
    """ReplaceCertForLoadBalancers返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RewriteLocationMap(AbstractModel):
    """转发规则之间的重定向关系

    """

    def __init__(self):
        """
        :param SourceLocationId: 源转发规则ID
        :type SourceLocationId: str
        :param TargetLocationId: 重定向至的目标转发规则ID
        :type TargetLocationId: str
        :param RewriteCode: 重定向状态码，可取值301,302,307
        :type RewriteCode: int
        :param TakeUrl: 重定向是否携带匹配的url，配置RewriteCode时必填
        :type TakeUrl: bool
        :param SourceDomain: 源转发的域名，必须是SourceLocationId对应的域名，配置RewriteCode时必填
        :type SourceDomain: str
        """
        self.SourceLocationId = None
        self.TargetLocationId = None
        self.RewriteCode = None
        self.TakeUrl = None
        self.SourceDomain = None


    def _deserialize(self, params):
        self.SourceLocationId = params.get("SourceLocationId")
        self.TargetLocationId = params.get("TargetLocationId")
        self.RewriteCode = params.get("RewriteCode")
        self.TakeUrl = params.get("TakeUrl")
        self.SourceDomain = params.get("SourceDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RewriteTarget(AbstractModel):
    """重定向目标的信息

    """

    def __init__(self):
        """
        :param TargetListenerId: 重定向目标的监听器ID
注意：此字段可能返回 null，表示无重定向。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetListenerId: str
        :param TargetLocationId: 重定向目标的转发规则ID
注意：此字段可能返回 null，表示无重定向。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetLocationId: str
        :param RewriteCode: 重定向状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteCode: int
        :param TakeUrl: 重定向是否携带匹配的url
注意：此字段可能返回 null，表示取不到有效值。
        :type TakeUrl: bool
        :param RewriteType: 重定向类型，Manual: 手动重定向，Auto:  自动重定向
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteType: str
        """
        self.TargetListenerId = None
        self.TargetLocationId = None
        self.RewriteCode = None
        self.TakeUrl = None
        self.RewriteType = None


    def _deserialize(self, params):
        self.TargetListenerId = params.get("TargetListenerId")
        self.TargetLocationId = params.get("TargetLocationId")
        self.RewriteCode = params.get("RewriteCode")
        self.TakeUrl = params.get("TakeUrl")
        self.RewriteType = params.get("RewriteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RsWeightRule(AbstractModel):
    """修改节点权重的数据类型

    """

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器 ID。
        :type ListenerId: str
        :param Targets: 要修改权重的后端机器列表。
        :type Targets: list of Target
        :param LocationId: 转发规则的ID，七层规则时需要此参数，4层规则不需要。
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效。
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效。
        :type Url: str
        :param Weight: 后端服务修改后的转发权重，取值范围：[0，100]。此参数的优先级低于前述[Target](https://cloud.tencent.com/document/api/214/30694#Target)中的Weight参数，即最终的权重值以Target中的Weight参数值为准，仅当Target中的Weight参数为空时，才以RsWeightRule中的Weight参数为准。
        :type Weight: int
        """
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Weight = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleHealth(AbstractModel):
    """一条转发规则的健康检查状态

    """

    def __init__(self):
        """
        :param LocationId: 转发规则ID
        :type LocationId: str
        :param Domain: 转发规则的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Url: 转发规则的Url
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Targets: 本规则上绑定的后端服务的健康检查状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of TargetHealth
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleInput(AbstractModel):
    """HTTP/HTTPS转发规则（输入）

    """

    def __init__(self):
        """
        :param Domain: 转发规则的域名。长度限制为：1~80。
        :type Domain: str
        :param Url: 转发规则的路径。长度限制为：1~200。
        :type Url: str
        :param SessionExpireTime: 会话保持时间。设置为0表示关闭会话保持，开启会话保持可取值30~3600，单位：秒。
        :type SessionExpireTime: int
        :param HealthCheck: 健康检查信息。详情请参见：[健康检查](https://cloud.tencent.com/document/product/214/6097)
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 证书信息
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: 规则的请求转发方式，可选值：WRR、LEAST_CONN、IP_HASH
分别表示按权重轮询、最小连接数、按IP哈希， 默认为 WRR。
        :type Scheduler: str
        :param ForwardType: 负载均衡与后端服务之间的转发协议，目前支持 HTTP/HTTPS/TRPC
        :type ForwardType: str
        :param DefaultServer: 是否将该域名设为默认域名，注意，一个监听器下只能设置一个默认域名。
        :type DefaultServer: bool
        :param Http2: 是否开启Http2，注意，只有HTTPS域名才能开启Http2。
        :type Http2: bool
        :param TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组
        :type TargetType: str
        :param TrpcCallee: TRPC被调服务器路由，ForwardType为TRPC时必填
        :type TrpcCallee: str
        :param TrpcFunc: TRPC调用服务接口，ForwardType为TRPC时必填
        :type TrpcFunc: str
        :param Quic: 是否开启QUIC，注意，只有HTTPS域名才能开启QUIC
        :type Quic: bool
        """
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.ForwardType = None
        self.DefaultServer = None
        self.Http2 = None
        self.TargetType = None
        self.TrpcCallee = None
        self.TrpcFunc = None
        self.Quic = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.ForwardType = params.get("ForwardType")
        self.DefaultServer = params.get("DefaultServer")
        self.Http2 = params.get("Http2")
        self.TargetType = params.get("TargetType")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")
        self.Quic = params.get("Quic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleOutput(AbstractModel):
    """HTTP/HTTPS监听器的转发规则（输出）

    """

    def __init__(self):
        """
        :param LocationId: 转发规则的 ID
        :type LocationId: str
        :param Domain: 转发规则的域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Url: 转发规则的路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param SessionExpireTime: 会话保持时间
        :type SessionExpireTime: int
        :param HealthCheck: 健康检查信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param Scheduler: 规则的请求转发方式
        :type Scheduler: str
        :param ListenerId: 转发规则所属的监听器 ID
        :type ListenerId: str
        :param RewriteTarget: 转发规则的重定向目标信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteTarget: :class:`tencentcloud.clb.v20180317.models.RewriteTarget`
        :param HttpGzip: 是否开启gzip
        :type HttpGzip: bool
        :param BeAutoCreated: 转发规则是否为自动创建
        :type BeAutoCreated: bool
        :param DefaultServer: 是否作为默认域名
        :type DefaultServer: bool
        :param Http2: 是否开启Http2
        :type Http2: bool
        :param ForwardType: 负载均衡与后端服务之间的转发协议
        :type ForwardType: str
        :param CreateTime: 转发规则的创建时间
        :type CreateTime: str
        :param TargetType: 后端服务器类型
        :type TargetType: str
        :param TargetGroup: 绑定的目标组基本信息；当规则绑定目标组时，会返回该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param WafDomainId: WAF实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WafDomainId: str
        :param TrpcCallee: TRPC被调服务器路由，ForwardType为TRPC时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TrpcCallee: str
        :param TrpcFunc: TRPC调用服务接口，ForwardType为TRPC时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TrpcFunc: str
        :param QuicStatus: QUIC状态
注意：此字段可能返回 null，表示取不到有效值。
        :type QuicStatus: str
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.ListenerId = None
        self.RewriteTarget = None
        self.HttpGzip = None
        self.BeAutoCreated = None
        self.DefaultServer = None
        self.Http2 = None
        self.ForwardType = None
        self.CreateTime = None
        self.TargetType = None
        self.TargetGroup = None
        self.WafDomainId = None
        self.TrpcCallee = None
        self.TrpcFunc = None
        self.QuicStatus = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateOutput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.ListenerId = params.get("ListenerId")
        if params.get("RewriteTarget") is not None:
            self.RewriteTarget = RewriteTarget()
            self.RewriteTarget._deserialize(params.get("RewriteTarget"))
        self.HttpGzip = params.get("HttpGzip")
        self.BeAutoCreated = params.get("BeAutoCreated")
        self.DefaultServer = params.get("DefaultServer")
        self.Http2 = params.get("Http2")
        self.ForwardType = params.get("ForwardType")
        self.CreateTime = params.get("CreateTime")
        self.TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self.TargetGroup = BasicTargetGroupInfo()
            self.TargetGroup._deserialize(params.get("TargetGroup"))
        self.WafDomainId = params.get("WafDomainId")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")
        self.QuicStatus = params.get("QuicStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleTargets(AbstractModel):
    """HTTP/HTTPS监听器下的转发规则绑定的后端服务信息

    """

    def __init__(self):
        """
        :param LocationId: 转发规则的 ID
        :type LocationId: str
        :param Domain: 转发规则的域名
        :type Domain: str
        :param Url: 转发规则的路径。
        :type Url: str
        :param Targets: 后端服务的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of Backend
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetLoadBalancerClsLogRequest(AbstractModel):
    """SetLoadBalancerClsLog请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param LogSetId: 日志服务(CLS)的日志集ID。
        :type LogSetId: str
        :param LogTopicId: 日志服务(CLS)的日志主题ID。
        :type LogTopicId: str
        :param LogType: 日志类型，ACCESS：访问日志，HEALTH：健康检查日志，默认ACCESS。
        :type LogType: str
        """
        self.LoadBalancerId = None
        self.LogSetId = None
        self.LogTopicId = None
        self.LogType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")
        self.LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetLoadBalancerClsLogResponse(AbstractModel):
    """SetLoadBalancerClsLog返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param SecurityGroups: 安全组ID构成的数组，一个负载均衡实例最多可绑定50个安全组，如果要解绑所有安全组，可不传此参数，或传入空数组。
        :type SecurityGroups: list of str
        """
        self.LoadBalancerId = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全组ID，如 sg-12345678
        :type SecurityGroup: str
        :param OperationType: ADD 绑定安全组；
DEL 解绑安全组
        :type OperationType: str
        :param LoadBalancerIds: 负载均衡实例ID数组
        :type LoadBalancerIds: list of str
        """
        self.SecurityGroup = None
        self.OperationType = None
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.SecurityGroup = params.get("SecurityGroup")
        self.OperationType = params.get("OperationType")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SnatIp(AbstractModel):
    """SnatIp的信息结构

    """

    def __init__(self):
        """
        :param SubnetId: 私有网络子网的唯一性id，如subnet-12345678
        :type SubnetId: str
        :param Ip: IP地址，如192.168.0.1
        :type Ip: str
        """
        self.SubnetId = None
        self.Ip = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TagInfo(AbstractModel):
    """负载均衡的标签信息

    """

    def __init__(self):
        """
        :param TagKey: 标签的键
        :type TagKey: str
        :param TagValue: 标签的值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Target(AbstractModel):
    """转发目标，即绑定在负载均衡上的后端服务

    """

    def __init__(self):
        """
        :param Port: 后端服务的监听端口。
注意：绑定CVM（云服务器）或ENI（弹性网卡）时必传此参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Type: 后端服务的类型，可取：CVM（云服务器）、ENI（弹性网卡）；作为入参时，目前本参数暂不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param InstanceId: 绑定CVM时需要传入此参数，代表CVM的唯一 ID，可通过 DescribeInstances 接口返回字段中的 InstanceId 字段获取。表示绑定主网卡主IP。
注意：参数 InstanceId、EniIp 只能传入一个且必须传入一个。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Weight: 后端服务修改后的转发权重，取值范围：[0, 100]，默认为 10。此参数的优先级高于[RsWeightRule](https://cloud.tencent.com/document/api/214/30694#RsWeightRule)中的Weight参数，即最终的权重值以此Weight参数值为准，仅当此Weight参数为空时，才以RsWeightRule中的Weight参数为准。
        :type Weight: int
        :param EniIp: 绑定IP时需要传入此参数，支持弹性网卡的IP和其他内网IP，如果是弹性网卡则必须先绑定至CVM，然后才能绑定到负载均衡实例。
注意：参数 InstanceId、EniIp 只能传入一个且必须传入一个。如果绑定双栈IPV6子机，必须传该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type EniIp: str
        """
        self.Port = None
        self.Type = None
        self.InstanceId = None
        self.Weight = None
        self.EniIp = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.EniIp = params.get("EniIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TargetGroupAssociation(AbstractModel):
    """规则与目标组的关联关系

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param LocationId: 转发规则ID
        :type LocationId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.TargetGroupId = None
        self.LocationId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.TargetGroupId = params.get("TargetGroupId")
        self.LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TargetGroupBackend(AbstractModel):
    """目标组绑定的后端服务器

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param Type: 后端服务的类型，可取：CVM、ENI（即将支持）
        :type Type: str
        :param InstanceId: 后端服务的唯一 ID
        :type InstanceId: str
        :param Port: 后端服务的监听端口
        :type Port: int
        :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param RegisteredTime: 后端服务被绑定的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        :param EniId: 弹性网卡唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EniId: str
        :param ZoneId: 后端服务的可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        """
        self.TargetGroupId = None
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None
        self.EniId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TargetGroupInfo(AbstractModel):
    """目标组信息

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param VpcId: 目标组的vpcid
        :type VpcId: str
        :param TargetGroupName: 目标组的名字
        :type TargetGroupName: str
        :param Port: 目标组的默认端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param CreatedTime: 目标组的创建时间
        :type CreatedTime: str
        :param UpdatedTime: 目标组的修改时间
        :type UpdatedTime: str
        :param AssociatedRule: 关联到的规则数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociatedRule: list of AssociationItem
        """
        self.TargetGroupId = None
        self.VpcId = None
        self.TargetGroupName = None
        self.Port = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.AssociatedRule = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.VpcId = params.get("VpcId")
        self.TargetGroupName = params.get("TargetGroupName")
        self.Port = params.get("Port")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        if params.get("AssociatedRule") is not None:
            self.AssociatedRule = []
            for item in params.get("AssociatedRule"):
                obj = AssociationItem()
                obj._deserialize(item)
                self.AssociatedRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TargetGroupInstance(AbstractModel):
    """目标组实例

    """

    def __init__(self):
        """
        :param BindIP: 目标组实例的内网IP
        :type BindIP: str
        :param Port: 目标组实例的端口
        :type Port: int
        :param Weight: 目标组实例的权重
        :type Weight: int
        :param NewPort: 目标组实例的新端口
        :type NewPort: int
        """
        self.BindIP = None
        self.Port = None
        self.Weight = None
        self.NewPort = None


    def _deserialize(self, params):
        self.BindIP = params.get("BindIP")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.NewPort = params.get("NewPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TargetHealth(AbstractModel):
    """描述一个Target的健康信息

    """

    def __init__(self):
        """
        :param IP: Target的内网IP
        :type IP: str
        :param Port: Target绑定的端口
        :type Port: int
        :param HealthStatus: 当前健康状态，true：健康，false：不健康（包括尚未开始探测、探测中、状态异常等几种状态）。只有处于健康状态（且权重大于0），负载均衡才会向其转发流量。
        :type HealthStatus: bool
        :param TargetId: Target的实例ID，如 ins-12345678
        :type TargetId: str
        :param HealthStatusDetial: 当前健康状态的详细信息。如：Alive、Dead、Unknown。Alive状态为健康，Dead状态为异常，Unknown状态包括尚未开始探测、探测中、状态未知。
        :type HealthStatusDetial: str
        """
        self.IP = None
        self.Port = None
        self.HealthStatus = None
        self.TargetId = None
        self.HealthStatusDetial = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.HealthStatus = params.get("HealthStatus")
        self.TargetId = params.get("TargetId")
        self.HealthStatusDetial = params.get("HealthStatusDetial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TargetRegionInfo(AbstractModel):
    """负载均衡实例所绑定的后端服务的信息，包括所属地域、所属网络。

    """

    def __init__(self):
        """
        :param Region: Target所属地域，如 ap-guangzhou
        :type Region: str
        :param VpcId: Target所属网络，私有网络格式如 vpc-abcd1234，如果是基础网络，则为"0"
        :type VpcId: str
        """
        self.Region = None
        self.VpcId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ZoneInfo(AbstractModel):
    """可用区相关信息

    """

    def __init__(self):
        """
        :param ZoneId: 可用区数值形式的唯一ID，如：100001
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param Zone: 可用区字符串形式的唯一ID，如：ap-guangzhou-1
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param ZoneName: 可用区名称，如：广州一区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param ZoneRegion: 可用区所属地域，如：ap-guangzhou
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneRegion: str
        :param LocalZone: 可用区是否是LocalZone可用区，如：false
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalZone: bool
        """
        self.ZoneId = None
        self.Zone = None
        self.ZoneName = None
        self.ZoneRegion = None
        self.LocalZone = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneRegion = params.get("ZoneRegion")
        self.LocalZone = params.get("LocalZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        