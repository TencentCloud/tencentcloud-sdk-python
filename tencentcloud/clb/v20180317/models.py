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

from tencentcloud.common.abstract_model import AbstractModel


class AutoRewriteRequest(AbstractModel):
    """AutoRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param ListenerId: HTTPS:443监听器的ID
        :type ListenerId: str
        :param Domains: HTTPS:443监听器下需要重定向的域名
        :type Domains: list of str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domains = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domains = params.get("Domains")


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


class Backend(AbstractModel):
    """监听器绑定的后端服务的详细信息

    """

    def __init__(self):
        """
        :param Type: 后端服务的类型，可取：CVM、ENI（即将支持）
        :type Type: str
        :param InstanceId: 后端服务的唯一 ID，可通过 DescribeInstances 接口返回字段中的 unInstanceId 字段获取
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


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ModifyList: 要批量修改权重的列表
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


class CertificateInput(AbstractModel):
    """证书信息

    """

    def __init__(self):
        """
        :param SSLMode: 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证
        :type SSLMode: str
        :param CertId: 服务端证书的 ID，如果不填写此项则必须上传证书，包括 CertContent，CertKey，CertName。
        :type CertId: str
        :param CertCaId: 客户端证书的 ID，当监听器采用双向认证，即 SSLMode=mutual 时，如果不填写此项则必须上传客户端证书，包括 CertCaContent，CertCaName。
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


class CreateListenerRequest(AbstractModel):
    """CreateListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param Ports: 要将监听器创建到哪些端口，每个端口对应一个新的监听器
        :type Ports: list of int
        :param Protocol: 监听器协议： TCP | UDP | HTTP | HTTPS | TCP_SSL（TCP_SSL 正在内测中，如需使用请通过工单申请）
        :type Protocol: str
        :param ListenerNames: 要创建的监听器名称列表，名称与Ports数组按序一一对应，如不需立即命名，则无需提供此参数
        :type ListenerNames: list of str
        :param HealthCheck: 健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL监听器
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 证书相关信息，此参数仅适用于HTTPS/TCP_SSL监听器
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :type SessionExpireTime: int
        :param Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。此参数仅适用于TCP/UDP/TCP_SSL监听器。
        :type Scheduler: str
        :param SniSwitch: 是否开启SNI特性，此参数仅适用于HTTPS监听器。
        :type SniSwitch: int
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


class CreateListenerResponse(AbstractModel):
    """CreateListener返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerIds: 创建的监听器的唯一标识数组
        :type ListenerIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
        :type LoadBalancerType: str
        :param Forward: 负载均衡实例的类型。1：通用的负载均衡实例，目前只支持传入1
        :type Forward: int
        :param LoadBalancerName: 负载均衡实例的名称，只在创建一个实例的时候才会生效。规则：1-50 个英文、汉字、数字、连接线“-”或下划线“_”。
注意：如果名称与系统中已有负载均衡实例的名称相同，则系统将会自动生成此次创建的负载均衡实例的名称。
        :type LoadBalancerName: str
        :param VpcId: 负载均衡后端目标设备所属的网络 ID，可以通过 DescribeVpcEx 接口获取。 不传此参数则默认为基础网络（"0"）。
        :type VpcId: str
        :param SubnetId: 在私有网络内购买内网负载均衡实例的情况下，必须指定子网 ID，内网负载均衡实例的 VIP 将从这个子网中产生。其它情况不支持该参数。
        :type SubnetId: str
        :param ProjectId: 负载均衡实例所属的项目 ID，可以通过 DescribeProject 接口获取。不传此参数则视为默认项目。
        :type ProjectId: int
        :param AddressIPVersion: 仅适用于公网负载均衡。IP版本，IPV4 | IPV6，默认值 IPV4。
        :type AddressIPVersion: str
        :param Number: 创建负载均衡的个数，默认值 1。
        :type Number: int
        :param MasterZoneId: 仅适用于公网负载均衡。设置跨可用区容灾时的主可用区ID，例如 100001 或 ap-guangzhou-1
注：主可用区是需要承载流量的可用区，备可用区默认不承载流量，主可用区不可用时才使用备可用区，平台将为您自动选择最佳备可用区。可通过 DescribeMasterZones 接口查询一个地域的主可用区的列表。
        :type MasterZoneId: str
        :param ZoneId: 仅适用于公网负载均衡。可用区ID，指定可用区以创建负载均衡实例。如：ap-guangzhou-1
        :type ZoneId: str
        :param AnycastZone: 仅适用于公网负载均衡。Anycast的发布域，可取 ZONE_A 或 ZONE_B。仅带宽非上移用户支持此参数。
        :type AnycastZone: str
        :param InternetAccessible: 仅适用于公网负载均衡。负载均衡的网络计费方式，此参数仅对带宽上移用户生效。
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param Tags: 购买负载均衡同时，给负载均衡打上标签
        :type Tags: list of TagInfo
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
        self.AnycastZone = None
        self.InternetAccessible = None
        self.Tags = None


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
        self.AnycastZone = params.get("AnycastZone")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)


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


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 监听器 ID
        :type ListenerId: str
        :param Rules: 新建转发规则的信息
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


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 要删除的监听器 ID
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")


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


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 要删除的负载均衡实例 ID数组，数组大小最大支持20
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")


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


class DeleteRewriteRequest(AbstractModel):
    """DeleteRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param SourceListenerId: 源监听器ID
        :type SourceListenerId: str
        :param TargetListenerId: 目标监听器ID
        :type TargetListenerId: str
        :param RewriteInfos: 转发规则之间的重定向关系
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


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param LocationIds: 要删除的转发规则的ID组成的数组
        :type LocationIds: list of str
        :param Domain: 要删除的转发规则的域名，已提供LocationIds参数时本参数不生效
        :type Domain: str
        :param Url: 要删除的转发规则的转发路径，已提供LocationIds参数时本参数不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationIds = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationIds = params.get("LocationIds")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


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


class DeregisterTargetsFromClassicalLBRequest(AbstractModel):
    """DeregisterTargetsFromClassicalLB请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param InstanceIds: 后端服务的实例ID列表
        :type InstanceIds: list of str
        """
        self.LoadBalancerId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.InstanceIds = params.get("InstanceIds")


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


class DeregisterTargetsRequest(AbstractModel):
    """DeregisterTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID，格式如 lb-12345678
        :type LoadBalancerId: str
        :param ListenerId: 监听器 ID，格式如 lbl-12345678
        :type ListenerId: str
        :param Targets: 要解绑的后端服务列表，数组长度最大支持20
        :type Targets: list of Target
        :param LocationId: 转发规则的ID，格式如 loc-12345678，当从七层转发规则解绑机器时，必须提供此参数或Domain+Url两者之一
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效
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


class DescribeClassicalLBByInstanceIdRequest(AbstractModel):
    """DescribeClassicalLBByInstanceId请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 后端实例ID列表
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeClassicalLBByInstanceIdResponse(AbstractModel):
    """DescribeClassicalLBByInstanceId返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerInfoList: 负载均衡相关信息列表
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


class DescribeClassicalLBHealthStatusRequest(AbstractModel):
    """DescribeClassicalLBHealthStatus请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")


class DescribeClassicalLBHealthStatusResponse(AbstractModel):
    """DescribeClassicalLBHealthStatus返回参数结构体

    """

    def __init__(self):
        """
        :param HealthList: 后端健康状态列表
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


class DescribeClassicalLBListenersRequest(AbstractModel):
    """DescribeClassicalLBListeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 负载均衡监听器ID列表
        :type ListenerIds: list of str
        :param Protocol: 负载均衡监听的协议, 'TCP', 'UDP', 'HTTP', 'HTTPS'
        :type Protocol: str
        :param ListenerPort: 负载均衡监听端口， 范围[1-65535]
        :type ListenerPort: int
        :param Status: 监听器的状态，0 表示创建中，1 表示运行中
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


class DescribeClassicalLBListenersResponse(AbstractModel):
    """DescribeClassicalLBListeners返回参数结构体

    """

    def __init__(self):
        """
        :param Listeners: 监听器列表
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


class DescribeClassicalLBTargetsRequest(AbstractModel):
    """DescribeClassicalLBTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        """
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")


class DescribeClassicalLBTargetsResponse(AbstractModel):
    """DescribeClassicalLBTargets返回参数结构体

    """

    def __init__(self):
        """
        :param Targets: 后端服务列表
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


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 要查询的负载均衡监听器 ID数组
        :type ListenerIds: list of str
        :param Protocol: 要查询的监听器协议类型，取值 TCP | UDP | HTTP | HTTPS | TCP_SSL
        :type Protocol: str
        :param Port: 要查询的监听器的端口
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


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners返回参数结构体

    """

    def __init__(self):
        """
        :param Listeners: 监听器列表
        :type Listeners: list of Listener
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 负载均衡实例 ID。
        :type LoadBalancerIds: list of str
        :param LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
        :type LoadBalancerType: str
        :param Forward: 负载均衡实例的类型。1：通用的负载均衡实例，0：传统型负载均衡实例
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
        :param Offset: 数据偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回负载均衡实例的个数，默认为 20。
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
        :param VpcId: 负载均衡实例所属私有网络，如 vpc-bhqkbhdx，
基础网络不支持通过VpcId查询。
        :type VpcId: str
        :param SecurityGroup: 安全组ID，如 sg-m1cc9123
        :type SecurityGroup: str
        :param MasterZone: 主可用区ID，如 ："100001" （对应的是广州一区）
        :type MasterZone: str
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


class DescribeRewriteRequest(AbstractModel):
    """DescribeRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param SourceListenerIds: 负载均衡监听器ID数组
        :type SourceListenerIds: list of str
        :param SourceLocationIds: 负载均衡转发规则的ID数组
        :type SourceLocationIds: list of str
        """
        self.LoadBalancerId = None
        self.SourceListenerIds = None
        self.SourceLocationIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerIds = params.get("SourceListenerIds")
        self.SourceLocationIds = params.get("SourceLocationIds")


class DescribeRewriteResponse(AbstractModel):
    """DescribeRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param RewriteSet: 重定向转发规则构成的数组，若无重定向规则，则返回空数组
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


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 要查询的负载均衡实例 ID列表
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancers: 负载均衡实例列表
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


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 监听器 ID列表
        :type ListenerIds: list of str
        :param Protocol: 监听器协议类型
        :type Protocol: str
        :param Port: 监听器端口
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


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets返回参数结构体

    """

    def __init__(self):
        """
        :param Listeners: 监听器后端绑定的机器信息
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


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 请求ID，即接口返回的 RequestId 参数
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


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


class InternetAccessible(AbstractModel):
    """网络计费方式，最大出带宽

    """

    def __init__(self):
        """
        :param InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR 按流量按小时后计费 ; BANDWIDTH_POSTPAID_BY_HOUR 按带宽按小时后计费;
BANDWIDTH_PACKAGE 按带宽包计费（当前，只有指定运营商时才支持此种计费模式）
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 最大出带宽，单位Mbps，范围支持0到65535，仅对公网属性的LB生效，默认值 10
        :type InternetMaxBandwidthOut: int
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class LBChargePrepaid(AbstractModel):
    """lb实例包年包月相关配置属性

    """

    def __init__(self):
        """
        :param RenewFlag: 续费类型：AUTO_RENEW 自动续费，  MANUAL_RENEW 手动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        :param Period: 周期，表示多少个月（保留字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        """
        self.RenewFlag = None
        self.Period = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Period = params.get("Period")


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
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Rules = None
        self.Targets = None


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
        :param ChargeType: 负载均衡实例的计费类型
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


class ManualRewriteRequest(AbstractModel):
    """ManualRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param SourceListenerId: 源监听器ID
        :type SourceListenerId: str
        :param TargetListenerId: 目标监听器ID
        :type TargetListenerId: str
        :param RewriteInfos: 转发规则之间的重定向关系
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


class ModifyListenerRequest(AbstractModel):
    """ModifyListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param ListenerName: 新的监听器名称
        :type ListenerName: str
        :param SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :type SessionExpireTime: int
        :param HealthCheck: 健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL监听器
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 证书相关信息，此参数仅适用于HTTPS/TCP_SSL监听器
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。
        :type Scheduler: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None


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
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.TargetRegionInfo = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param LocationId: 要修改的转发规则的 ID。
        :type LocationId: str
        :param Url: 转发规则的新的转发路径，如不需修改Url，则不需提供此参数
        :type Url: str
        :param HealthCheck: 健康检查信息
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Scheduler: 规则的请求转发方式，可选值：WRR、LEAST_CONN、IP_HASH
分别表示按权重轮询、最小连接数、按IP哈希， 默认为 WRR。
        :type Scheduler: str
        :param SessionExpireTime: 会话保持时间
        :type SessionExpireTime: int
        :param ForwardType: 负载均衡实例与后端服务之间的转发协议，默认HTTP，可取值：HTTP、HTTPS
        :type ForwardType: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Url = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.ForwardType = None


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


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Targets: 要修改端口的后端服务列表
        :type Targets: list of Target
        :param NewPort: 后端服务绑定到监听器或转发规则的新端口
        :type NewPort: int
        :param LocationId: 转发规则的ID，当后端服务绑定到七层转发规则时，必须提供此参数或Domain+Url两者之一
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效
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


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param LocationId: 转发规则的ID，当绑定机器到七层转发规则时，必须提供此参数或Domain+Url两者之一
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效
        :type Url: str
        :param Targets: 要修改权重的后端服务列表
        :type Targets: list of Target
        :param Weight: 后端服务服务新的转发权重，取值范围：0~100，默认值10。如果设置了 Targets.Weight 参数，则此参数不生效。
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


class RegisterTargetsRequest(AbstractModel):
    """RegisterTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Targets: 待绑定的后端服务列表，数组长度最大支持20
        :type Targets: list of Target
        :param LocationId: 转发规则的ID，当绑定后端服务到七层转发规则时，必须提供此参数或Domain+Url两者之一
        :type LocationId: str
        :param Domain: 目标转发规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标转发规则的URL，提供LocationId参数时本参数不生效
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


class RegisterTargetsWithClassicalLBRequest(AbstractModel):
    """RegisterTargetsWithClassicalLB请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param Targets: 后端服务信息
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


class RewriteLocationMap(AbstractModel):
    """转发规则之间的重定向关系

    """

    def __init__(self):
        """
        :param SourceLocationId: 源转发规则ID
        :type SourceLocationId: str
        :param TargetLocationId: 重定向至的目标转发规则ID
        :type TargetLocationId: str
        """
        self.SourceLocationId = None
        self.TargetLocationId = None


    def _deserialize(self, params):
        self.SourceLocationId = params.get("SourceLocationId")
        self.TargetLocationId = params.get("TargetLocationId")


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
        """
        self.TargetListenerId = None
        self.TargetLocationId = None


    def _deserialize(self, params):
        self.TargetListenerId = params.get("TargetListenerId")
        self.TargetLocationId = params.get("TargetLocationId")


class RsWeightRule(AbstractModel):
    """修改节点权重的数据类型

    """

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param LocationId: 转发规则的ID
        :type LocationId: str
        :param Targets: 要修改权重的后端机器列表
        :type Targets: list of Target
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效
        :type Url: str
        :param Weight: 后端服务新的转发权重，取值范围：0~100。
        :type Weight: int
        """
        self.ListenerId = None
        self.LocationId = None
        self.Targets = None
        self.Domain = None
        self.Url = None
        self.Weight = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.Weight = params.get("Weight")


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
        :param Targets: 本规则上绑定的后端的健康检查状态
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
        :param HealthCheck: 健康检查信息
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 证书信息
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: 规则的请求转发方式，可选值：WRR、LEAST_CONN、IP_HASH
分别表示按权重轮询、最小连接数、按IP哈希， 默认为 WRR。
        :type Scheduler: str
        :param ForwardType: 负载均衡与后端服务之间的转发协议，目前支持 HTTP
        :type ForwardType: str
        :param DefaultServer: 是否将该域名设为默认域名，注意，一个监听器下只能设置一个默认域名。
        :type DefaultServer: bool
        :param Http2: 是否开启Http2，注意，只用HTTPS域名才能开启Http2。
        :type Http2: bool
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


class Target(AbstractModel):
    """转发目标，即绑定在负载均衡上的后端服务

    """

    def __init__(self):
        """
        :param Port: 后端服务的监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Type: 后端服务的类型，可取：CVM（云服务器）、ENI（弹性网卡）；作为入参时，目前本参数暂不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param InstanceId: 绑定CVM时需要传入此参数，代表CVM的唯一 ID，可通过 DescribeInstances 接口返回字段中的 InstanceId 字段获取。
注意：参数 InstanceId 和 EniIp 只能传入一个且必须传入一个。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param EniIp: 绑定弹性网卡时需要传入此参数，代表弹性网卡的IP，弹性网卡必须先绑定至CVM，然后才能绑定到负载均衡实例。注意：参数 InstanceId 和 EniIp 只能传入一个且必须传入一个。注意：绑定弹性网卡需要先提交工单开白名单使用。
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


class TargetHealth(AbstractModel):
    """描述一个Target的健康信息

    """

    def __init__(self):
        """
        :param IP: Target的内网IP
        :type IP: str
        :param Port: Target绑定的端口
        :type Port: int
        :param HealthStatus: 当前健康状态，true：健康，false：不健康。
        :type HealthStatus: bool
        :param TargetId: Target的实例ID，如 ins-12345678
        :type TargetId: str
        """
        self.IP = None
        self.Port = None
        self.HealthStatus = None
        self.TargetId = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.HealthStatus = params.get("HealthStatus")
        self.TargetId = params.get("TargetId")


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
        """
        self.ZoneId = None
        self.Zone = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")