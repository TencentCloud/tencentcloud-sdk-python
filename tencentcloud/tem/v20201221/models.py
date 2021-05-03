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


class CosToken(AbstractModel):
    """Cos token

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID
        :type RequestId: str
        :param Bucket: 存储桶桶名
        :type Bucket: str
        :param Region: 存储桶所在区域
        :type Region: str
        :param TmpSecretId: 临时密钥的SecretId
        :type TmpSecretId: str
        :param TmpSecretKey: 临时密钥的SecretKey
        :type TmpSecretKey: str
        :param SessionToken: 临时密钥的 sessionToken
        :type SessionToken: str
        :param StartTime: 临时密钥获取的开始时间
        :type StartTime: str
        :param ExpiredTime: 临时密钥的 expiredTime
        :type ExpiredTime: str
        :param FullPath: 包完整路径
        :type FullPath: str
        """
        self.RequestId = None
        self.Bucket = None
        self.Region = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.SessionToken = None
        self.StartTime = None
        self.ExpiredTime = None
        self.FullPath = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.SessionToken = params.get("SessionToken")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.FullPath = params.get("FullPath")


class CreateCosTokenRequest(AbstractModel):
    """CreateCosToken请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param VersionId: 服务版本ID
        :type VersionId: str
        :param PkgName: 包名
        :type PkgName: str
        :param OptType: optType 1上传  2查询
        :type OptType: int
        :param SourceChannel: 来源 channel
        :type SourceChannel: int
        """
        self.ServiceId = None
        self.VersionId = None
        self.PkgName = None
        self.OptType = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.VersionId = params.get("VersionId")
        self.PkgName = params.get("PkgName")
        self.OptType = params.get("OptType")
        self.SourceChannel = params.get("SourceChannel")


class CreateCosTokenResponse(AbstractModel):
    """CreateCosToken返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功时为CosToken对象，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tem.v20201221.models.CosToken`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosToken()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param Vpc: 私有网络名称
        :type Vpc: str
        :param SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param Description: 命名空间描述
        :type Description: str
        :param K8sVersion: K8s version
        :type K8sVersion: str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.NamespaceName = None
        self.Vpc = None
        self.SubnetIds = None
        self.Description = None
        self.K8sVersion = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceName = params.get("NamespaceName")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.Description = params.get("Description")
        self.K8sVersion = params.get("K8sVersion")
        self.SourceChannel = params.get("SourceChannel")


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页limit
        :type Limit: int
        :param Offset: 分页下标
        :type Offset: int
        :param SourceChannel: 来源source
        :type SourceChannel: int
        """
        self.Limit = None
        self.Offset = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceChannel = params.get("SourceChannel")


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.tem.v20201221.models.NamespacePage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = NamespacePage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class IngressInfo(AbstractModel):
    """Ingress 配置

    """

    def __init__(self):
        """
        :param NamespaceId: tem namespaceId
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param EksNamespace: eks namespace
        :type EksNamespace: str
        :param AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param Name: ingress name
        :type Name: str
        :param Rules: rules 配置
        :type Rules: list of IngressRule
        :param ClbId: clb ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClbId: str
        :param Tls: tls 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tls: list of IngressTls
        :param ClusterId: eks clusterId
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Vip: clb ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.AddressIPVersion = None
        self.Name = None
        self.Rules = None
        self.ClbId = None
        self.Tls = None
        self.ClusterId = None
        self.Vip = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.Name = params.get("Name")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = IngressRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.ClbId = params.get("ClbId")
        if params.get("Tls") is not None:
            self.Tls = []
            for item in params.get("Tls"):
                obj = IngressTls()
                obj._deserialize(item)
                self.Tls.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.Vip = params.get("Vip")


class IngressRule(AbstractModel):
    """ingress rule 配置

    """

    def __init__(self):
        """
        :param Http: ingress rule value
        :type Http: :class:`tencentcloud.tem.v20201221.models.IngressRuleValue`
        :param Host: host 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        """
        self.Http = None
        self.Host = None


    def _deserialize(self, params):
        if params.get("Http") is not None:
            self.Http = IngressRuleValue()
            self.Http._deserialize(params.get("Http"))
        self.Host = params.get("Host")


class IngressRuleBackend(AbstractModel):
    """Ingress 规则 backend 配置

    """

    def __init__(self):
        """
        :param ServiceName: eks service 名
        :type ServiceName: str
        :param ServicePort: eks service 端口
        :type ServicePort: int
        """
        self.ServiceName = None
        self.ServicePort = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.ServicePort = params.get("ServicePort")


class IngressRulePath(AbstractModel):
    """Ingress Rule Path 配置

    """

    def __init__(self):
        """
        :param Path: path 信息
        :type Path: str
        :param Backend: backend 配置
        :type Backend: :class:`tencentcloud.tem.v20201221.models.IngressRuleBackend`
        """
        self.Path = None
        self.Backend = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        if params.get("Backend") is not None:
            self.Backend = IngressRuleBackend()
            self.Backend._deserialize(params.get("Backend"))


class IngressRuleValue(AbstractModel):
    """Ingress Rule Value 配置

    """

    def __init__(self):
        """
        :param Paths: rule 整体配置
        :type Paths: list of IngressRulePath
        """
        self.Paths = None


    def _deserialize(self, params):
        if params.get("Paths") is not None:
            self.Paths = []
            for item in params.get("Paths"):
                obj = IngressRulePath()
                obj._deserialize(item)
                self.Paths.append(obj)


class IngressTls(AbstractModel):
    """ingress tls 配置

    """

    def __init__(self):
        """
        :param Hosts: host 数组
        :type Hosts: list of str
        :param SecretName: secret name
        :type SecretName: str
        """
        self.Hosts = None
        self.SecretName = None


    def _deserialize(self, params):
        self.Hosts = params.get("Hosts")
        self.SecretName = params.get("SecretName")


class ModifyIngressRequest(AbstractModel):
    """ModifyIngress请求参数结构体

    """

    def __init__(self):
        """
        :param Ingress: Ingress 规则配置
        :type Ingress: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.Ingress = None
        self.SourceChannel = None


    def _deserialize(self, params):
        if params.get("Ingress") is not None:
            self.Ingress = IngressInfo()
            self.Ingress._deserialize(params.get("Ingress"))
        self.SourceChannel = params.get("SourceChannel")


class ModifyIngressResponse(AbstractModel):
    """ModifyIngress返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param NamespaceId: 环境id
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param Description: 命名空间描述
        :type Description: str
        :param Vpc: 私有网络名称
        :type Vpc: str
        :param SubnetIds: 子网网络
        :type SubnetIds: list of str
        :param SourceChannel: 来源渠道
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.NamespaceName = None
        self.Description = None
        self.Vpc = None
        self.SubnetIds = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.Description = params.get("Description")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.SourceChannel = params.get("SourceChannel")


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class NamespacePage(AbstractModel):
    """命名空间分页

    """

    def __init__(self):
        """
        :param Records: 分页内容
        :type Records: list of TemNamespaceInfo
        :param Total: 总数
        :type Total: int
        :param Size: 条目数
        :type Size: int
        :param Pages: 页数
        :type Pages: int
        """
        self.Records = None
        self.Total = None
        self.Size = None
        self.Pages = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = TemNamespaceInfo()
                obj._deserialize(item)
                self.Records.append(obj)
        self.Total = params.get("Total")
        self.Size = params.get("Size")
        self.Pages = params.get("Pages")


class TemNamespaceInfo(AbstractModel):
    """命名空间对象

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间id
        :type NamespaceId: str
        :param Channel: 渠道
        :type Channel: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param Region: 区域名称
        :type Region: str
        :param Description: 命名空间描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Status: 状态,1:已销毁;0:正常
        :type Status: int
        :param Vpc: vpc网络
        :type Vpc: str
        :param CreateDate: 创建时间
        :type CreateDate: str
        :param ModifyDate: 修改时间
        :type ModifyDate: str
        :param Modifier: 修改人
        :type Modifier: str
        :param Creator: 创建人
        :type Creator: str
        :param ServiceNum: 服务数
        :type ServiceNum: int
        :param RunInstancesNum: 运行实例数
        :type RunInstancesNum: int
        :param SubnetId: 子网络
        :type SubnetId: str
        :param TcbEnvStatus: tcb环境状态
        :type TcbEnvStatus: str
        :param ClusterStatus: eks cluster status
        :type ClusterStatus: str
        """
        self.NamespaceId = None
        self.Channel = None
        self.NamespaceName = None
        self.Region = None
        self.Description = None
        self.Status = None
        self.Vpc = None
        self.CreateDate = None
        self.ModifyDate = None
        self.Modifier = None
        self.Creator = None
        self.ServiceNum = None
        self.RunInstancesNum = None
        self.SubnetId = None
        self.TcbEnvStatus = None
        self.ClusterStatus = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.Channel = params.get("Channel")
        self.NamespaceName = params.get("NamespaceName")
        self.Region = params.get("Region")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.Vpc = params.get("Vpc")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        self.ServiceNum = params.get("ServiceNum")
        self.RunInstancesNum = params.get("RunInstancesNum")
        self.SubnetId = params.get("SubnetId")
        self.TcbEnvStatus = params.get("TcbEnvStatus")
        self.ClusterStatus = params.get("ClusterStatus")