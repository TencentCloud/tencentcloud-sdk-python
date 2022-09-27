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


class ApolloEnvParam(AbstractModel):
    """Apollo 环境配置参数

    """

    def __init__(self):
        r"""
        :param Name: 环境名称
        :type Name: str
        :param EngineResourceSpec: 环境内引擎的节点规格 ID
        :type EngineResourceSpec: str
        :param EngineNodeNum: 环境内引擎的节点数量
        :type EngineNodeNum: int
        :param StorageCapacity: 配置存储空间大小，以GB为单位
        :type StorageCapacity: int
        :param VpcId: VPC ID。在 VPC 的子网内分配一个 IP 作为 ConfigServer 的访问地址
        :type VpcId: str
        :param SubnetId: 子网 ID。在 VPC 的子网内分配一个 IP 作为 ConfigServer 的访问地址
        :type SubnetId: str
        """
        self.Name = None
        self.EngineResourceSpec = None
        self.EngineNodeNum = None
        self.StorageCapacity = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.EngineResourceSpec = params.get("EngineResourceSpec")
        self.EngineNodeNum = params.get("EngineNodeNum")
        self.StorageCapacity = params.get("StorageCapacity")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundK8SInfo(AbstractModel):
    """服务治理引擎绑定的kubernetes信息

    """

    def __init__(self):
        r"""
        :param BoundClusterId: 绑定的kubernetes集群ID
        :type BoundClusterId: str
        :param BoundClusterType: 绑定的kubernetes的集群类型，分tke和eks两种
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundClusterType: str
        :param SyncMode: 服务同步模式，all为全量同步，demand为按需同步
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncMode: str
        """
        self.BoundClusterId = None
        self.BoundClusterType = None
        self.SyncMode = None


    def _deserialize(self, params):
        self.BoundClusterId = params.get("BoundClusterId")
        self.BoundClusterType = params.get("BoundClusterType")
        self.SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayNode(AbstractModel):
    """云原生API网关节点信息。

    """

    def __init__(self):
        r"""
        :param NodeId: 云原生网关节点 id
        :type NodeId: str
        :param NodeIp: 节点 ip
        :type NodeIp: str
        """
        self.NodeId = None
        self.NodeIp = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeIp = params.get("NodeIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEngineRequest(AbstractModel):
    """CreateEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param EngineType: 引擎类型。参考值：
- zookeeper
- nacos
- consul
- apollo
- eureka
- polaris
        :type EngineType: str
        :param EngineVersion: 引擎的开源版本。每种引擎支持的开源版本不同，请参考产品文档或者控制台购买页
        :type EngineVersion: str
        :param EngineProductVersion: 引擎的产品版本。参考值：
- STANDARD： 标准版

引擎各版本及可选择的规格、节点数说明：
apollo - STANDARD版本
规格列表：spec-qcr53kf1t（1C2G）,spec-qdr53kf2w（2C4G）
节点数：1，2，3，4，5

eureka - STANDARD版本
规格列表：spec-qvj6k7t4q（1C2G）,spec-qcr53kfjt（2C4G）,spec-qvj6k7t4m（4G8G）,spec-qcr54kfjt（8C16G）,spec-qcr55kfjt（16C32G）
节点数：3，4，5
        :type EngineProductVersion: str
        :param EngineRegion: 引擎所在地域。参考值说明：
中国区 参考值：
- ap-guangzhou：广州
- ap-beijing：北京
- ap-chengdu：成都
- ap-chongqing：重庆
- ap-nanjing：南京
- ap-shanghai：上海
- ap-hongkong：香港
- ap-taipei：台北
亚太区 参考值：
- ap-jakarta：雅加达
- ap-singapore：新加坡
北美区 参考值
- na-toronto：多伦多
金融专区 参考值
- ap-beijing-fsi：北京金融
- ap-shanghai-fsi：上海金融
- ap-shenzhen-fsi：深圳金融
        :type EngineRegion: str
        :param EngineName: 引擎名称。参考值：
- eurek-test
        :type EngineName: str
        :param TradeType: 付费类型。参考值：
- 0：后付费
- 1：预付费
        :type TradeType: int
        :param EngineResourceSpec: 引擎的节点规格 ID。参见EngineProductVersion字段说明
        :type EngineResourceSpec: str
        :param EngineNodeNum: 引擎的节点数量。参见EngineProductVersion字段说明
        :type EngineNodeNum: int
        :param VpcId: VPC ID。在 VPC 的子网内分配一个 IP 作为引擎的访问地址。参考值：
- vpc-conz6aix
        :type VpcId: str
        :param SubnetId: 子网 ID。在 VPC 的子网内分配一个 IP 作为引擎的访问地址。参考值：
- subnet-ahde9me9
        :type SubnetId: str
        :param ApolloEnvParams: Apollo 环境配置参数列表。参数说明：
如果创建Apollo类型，此参数为必填的环境信息列表，最多可选4个环境。环境信息参数说明：
- Name：环境名。参考值：prod, dev, fat, uat
- EngineResourceSpec：环境内引擎的节点规格ID。参见EngineProductVersion参数说明
- EngineNodeNum：环境内引擎的节点数量。参见EngineProductVersion参数说明，其中prod环境支持的节点数为2，3，4，5
- StorageCapacity：配置存储空间大小，以GB为单位，步长为5.参考值：35
- VpcId：VPC ID。参考值：vpc-conz6aix
- SubnetId：子网 ID。参考值：subnet-ahde9me9
        :type ApolloEnvParams: list of ApolloEnvParam
        :param EngineTags: 引擎的标签列表。用户自定义的key/value形式，无参考值
        :type EngineTags: list of InstanceTagInfo
        :param EngineAdmin: 引擎的初始帐号信息。可设置参数：
- Name：控制台初始用户名
- Password：控制台初始密码
- Token：引擎接口的管理员 Token
        :type EngineAdmin: :class:`tencentcloud.tse.v20201207.models.EngineAdmin`
        :param PrepaidPeriod: 预付费时长，以月为单位
        :type PrepaidPeriod: int
        :param PrepaidRenewFlag: 自动续费标记，仅预付费使用。参考值：
- 0：不自动续费
- 1：自动续费
        :type PrepaidRenewFlag: int
        """
        self.EngineType = None
        self.EngineVersion = None
        self.EngineProductVersion = None
        self.EngineRegion = None
        self.EngineName = None
        self.TradeType = None
        self.EngineResourceSpec = None
        self.EngineNodeNum = None
        self.VpcId = None
        self.SubnetId = None
        self.ApolloEnvParams = None
        self.EngineTags = None
        self.EngineAdmin = None
        self.PrepaidPeriod = None
        self.PrepaidRenewFlag = None


    def _deserialize(self, params):
        self.EngineType = params.get("EngineType")
        self.EngineVersion = params.get("EngineVersion")
        self.EngineProductVersion = params.get("EngineProductVersion")
        self.EngineRegion = params.get("EngineRegion")
        self.EngineName = params.get("EngineName")
        self.TradeType = params.get("TradeType")
        self.EngineResourceSpec = params.get("EngineResourceSpec")
        self.EngineNodeNum = params.get("EngineNodeNum")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("ApolloEnvParams") is not None:
            self.ApolloEnvParams = []
            for item in params.get("ApolloEnvParams"):
                obj = ApolloEnvParam()
                obj._deserialize(item)
                self.ApolloEnvParams.append(obj)
        if params.get("EngineTags") is not None:
            self.EngineTags = []
            for item in params.get("EngineTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self.EngineTags.append(obj)
        if params.get("EngineAdmin") is not None:
            self.EngineAdmin = EngineAdmin()
            self.EngineAdmin._deserialize(params.get("EngineAdmin"))
        self.PrepaidPeriod = params.get("PrepaidPeriod")
        self.PrepaidRenewFlag = params.get("PrepaidRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEngineResponse(AbstractModel):
    """CreateEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 引擎实例 ID
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DeleteEngineRequest(AbstractModel):
    """DeleteEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 引擎实例 ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEngineResponse(AbstractModel):
    """DeleteEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayNodesRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param GroupId: 实例分组id
        :type GroupId: str
        :param Limit: 翻页获取多少个
        :type Limit: int
        :param Offset: 翻页从第几个开始获取
        :type Offset: int
        """
        self.GatewayId = None
        self.GroupId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.GroupId = params.get("GroupId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayNodesResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 获取云原生网关节点列表结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeCloudNativeAPIGatewayNodesResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayNodesResult(AbstractModel):
    """获取网关节点信息

    """

    def __init__(self):
        r"""
        :param TotalCount: 获取云原生API网关节点列表响应结果。
        :type TotalCount: int
        :param NodeList: 云原生API网关节点列表。
        :type NodeList: list of CloudNativeAPIGatewayNode
        """
        self.TotalCount = None
        self.NodeList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NodeList") is not None:
            self.NodeList = []
            for item in params.get("NodeList"):
                obj = CloudNativeAPIGatewayNode()
                obj._deserialize(item)
                self.NodeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceRegionInfo(AbstractModel):
    """实例地域信息描述

    """

    def __init__(self):
        r"""
        :param EngineRegion: 引擎部署地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        :param Replica: 引擎在该地域的副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replica: int
        :param SpecId: 引擎在该地域的规格id
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecId: str
        :param IntranetVpcInfos: 内网的网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetVpcInfos: list of VpcInfo
        :param EnableClientInternet: 是否开公网
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableClientInternet: bool
        """
        self.EngineRegion = None
        self.Replica = None
        self.SpecId = None
        self.IntranetVpcInfos = None
        self.EnableClientInternet = None


    def _deserialize(self, params):
        self.EngineRegion = params.get("EngineRegion")
        self.Replica = params.get("Replica")
        self.SpecId = params.get("SpecId")
        if params.get("IntranetVpcInfos") is not None:
            self.IntranetVpcInfos = []
            for item in params.get("IntranetVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.IntranetVpcInfos.append(obj)
        self.EnableClientInternet = params.get("EnableClientInternet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosReplicasRequest(AbstractModel):
    """DescribeNacosReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 引擎实例ID
        :type InstanceId: str
        :param Limit: 副本列表Limit
        :type Limit: int
        :param Offset: 副本列表Offset
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosReplicasResponse(AbstractModel):
    """DescribeNacosReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param Replicas: 引擎实例副本信息
        :type Replicas: list of NacosReplica
        :param TotalCount: 副本个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Replicas = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Replicas") is not None:
            self.Replicas = []
            for item in params.get("Replicas"):
                obj = NacosReplica()
                obj._deserialize(item)
                self.Replicas.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNacosServerInterfacesRequest(AbstractModel):
    """DescribeNacosServerInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Limit: 返回的列表个数
        :type Limit: int
        :param Offset: 返回的列表起始偏移量
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosServerInterfacesResponse(AbstractModel):
    """DescribeNacosServerInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 接口总个数
        :type TotalCount: int
        :param Content: 接口列表
        :type Content: list of NacosServerInterface
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = NacosServerInterface()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSREInstanceAccessAddressRequest(AbstractModel):
    """DescribeSREInstanceAccessAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 注册引擎实例Id
        :type InstanceId: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Workload: 引擎其他组件名称（pushgateway）
        :type Workload: str
        :param EngineRegion: 部署地域
        :type EngineRegion: str
        """
        self.InstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.Workload = None
        self.EngineRegion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Workload = params.get("Workload")
        self.EngineRegion = params.get("EngineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstanceAccessAddressResponse(AbstractModel):
    """DescribeSREInstanceAccessAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param IntranetAddress: 内网访问地址
        :type IntranetAddress: str
        :param InternetAddress: 公网访问地址
        :type InternetAddress: str
        :param EnvAddressInfos: apollo多环境公网ip
        :type EnvAddressInfos: list of EnvAddressInfo
        :param ConsoleInternetAddress: 控制台公网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleInternetAddress: str
        :param ConsoleIntranetAddress: 控制台内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleIntranetAddress: str
        :param InternetBandWidth: 客户端公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetBandWidth: int
        :param ConsoleInternetBandWidth: 控制台公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleInternetBandWidth: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IntranetAddress = None
        self.InternetAddress = None
        self.EnvAddressInfos = None
        self.ConsoleInternetAddress = None
        self.ConsoleIntranetAddress = None
        self.InternetBandWidth = None
        self.ConsoleInternetBandWidth = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IntranetAddress = params.get("IntranetAddress")
        self.InternetAddress = params.get("InternetAddress")
        if params.get("EnvAddressInfos") is not None:
            self.EnvAddressInfos = []
            for item in params.get("EnvAddressInfos"):
                obj = EnvAddressInfo()
                obj._deserialize(item)
                self.EnvAddressInfos.append(obj)
        self.ConsoleInternetAddress = params.get("ConsoleInternetAddress")
        self.ConsoleIntranetAddress = params.get("ConsoleIntranetAddress")
        self.InternetBandWidth = params.get("InternetBandWidth")
        self.ConsoleInternetBandWidth = params.get("ConsoleInternetBandWidth")
        self.RequestId = params.get("RequestId")


class DescribeSREInstancesRequest(AbstractModel):
    """DescribeSREInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 请求过滤参数
        :type Filters: list of Filter
        :param Limit: 翻页单页查询限制数量[0,1000], 默认值0
        :type Limit: int
        :param Offset: 翻页单页偏移量，默认值0
        :type Offset: int
        :param QueryType: 查询类型
        :type QueryType: str
        :param QuerySource: 调用方来源
        :type QuerySource: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.QueryType = None
        self.QuerySource = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.QueryType = params.get("QueryType")
        self.QuerySource = params.get("QuerySource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstancesResponse(AbstractModel):
    """DescribeSREInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param Content: 实例记录
        :type Content: list of SREInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = SREInstance()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZookeeperReplicasRequest(AbstractModel):
    """DescribeZookeeperReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 注册引擎实例ID
        :type InstanceId: str
        :param Limit: 副本列表Limit
        :type Limit: int
        :param Offset: 副本列表Offset
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZookeeperReplicasResponse(AbstractModel):
    """DescribeZookeeperReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param Replicas: 注册引擎实例副本信息
        :type Replicas: list of ZookeeperReplica
        :param TotalCount: 副本个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Replicas = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Replicas") is not None:
            self.Replicas = []
            for item in params.get("Replicas"):
                obj = ZookeeperReplica()
                obj._deserialize(item)
                self.Replicas.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeZookeeperServerInterfacesRequest(AbstractModel):
    """DescribeZookeeperServerInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Limit: 返回的列表个数
        :type Limit: int
        :param Offset: 返回的列表起始偏移量
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZookeeperServerInterfacesResponse(AbstractModel):
    """DescribeZookeeperServerInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 接口总个数
        :type TotalCount: int
        :param Content: 接口列表
        :type Content: list of ZookeeperServerInterface
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ZookeeperServerInterface()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class EngineAdmin(AbstractModel):
    """引擎的初始管理帐号

    """

    def __init__(self):
        r"""
        :param Name: 控制台初始用户名
        :type Name: str
        :param Password: 控制台初始密码
        :type Password: str
        :param Token: 引擎接口的管理员 Token
        :type Token: str
        """
        self.Name = None
        self.Password = None
        self.Token = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvAddressInfo(AbstractModel):
    """多环境网络信息

    """

    def __init__(self):
        r"""
        :param EnvName: 环境名
        :type EnvName: str
        :param EnableConfigInternet: 是否开启config公网
        :type EnableConfigInternet: bool
        :param ConfigInternetServiceIp: config公网ip
        :type ConfigInternetServiceIp: str
        :param ConfigIntranetAddress: config内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigIntranetAddress: str
        """
        self.EnvName = None
        self.EnableConfigInternet = None
        self.ConfigInternetServiceIp = None
        self.ConfigIntranetAddress = None


    def _deserialize(self, params):
        self.EnvName = params.get("EnvName")
        self.EnableConfigInternet = params.get("EnableConfigInternet")
        self.ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        self.ConfigIntranetAddress = params.get("ConfigIntranetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """环境具体信息

    """

    def __init__(self):
        r"""
        :param EnvName: 环境名称
        :type EnvName: str
        :param VpcInfos: 环境对应的网络信息
        :type VpcInfos: list of VpcInfo
        :param StorageCapacity: 云硬盘容量
        :type StorageCapacity: int
        :param Status: 运行状态
        :type Status: str
        :param AdminServiceIp: Admin service 访问地址
        :type AdminServiceIp: str
        :param ConfigServiceIp: Config service访问地址
        :type ConfigServiceIp: str
        :param EnableConfigInternet: 是否开启config-server公网
        :type EnableConfigInternet: bool
        :param ConfigInternetServiceIp: config-server公网访问地址
        :type ConfigInternetServiceIp: str
        :param SpecId: 规格ID
        :type SpecId: str
        :param EnvReplica: 环境的节点数
        :type EnvReplica: int
        :param RunningCount: 环境运行的节点数
        :type RunningCount: int
        :param AliasEnvName: 环境别名
        :type AliasEnvName: str
        :param EnvDesc: 环境描述
        :type EnvDesc: str
        :param ClientBandWidth: 客户端带宽
        :type ClientBandWidth: int
        """
        self.EnvName = None
        self.VpcInfos = None
        self.StorageCapacity = None
        self.Status = None
        self.AdminServiceIp = None
        self.ConfigServiceIp = None
        self.EnableConfigInternet = None
        self.ConfigInternetServiceIp = None
        self.SpecId = None
        self.EnvReplica = None
        self.RunningCount = None
        self.AliasEnvName = None
        self.EnvDesc = None
        self.ClientBandWidth = None


    def _deserialize(self, params):
        self.EnvName = params.get("EnvName")
        if params.get("VpcInfos") is not None:
            self.VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcInfos.append(obj)
        self.StorageCapacity = params.get("StorageCapacity")
        self.Status = params.get("Status")
        self.AdminServiceIp = params.get("AdminServiceIp")
        self.ConfigServiceIp = params.get("ConfigServiceIp")
        self.EnableConfigInternet = params.get("EnableConfigInternet")
        self.ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        self.SpecId = params.get("SpecId")
        self.EnvReplica = params.get("EnvReplica")
        self.RunningCount = params.get("RunningCount")
        self.AliasEnvName = params.get("AliasEnvName")
        self.EnvDesc = params.get("EnvDesc")
        self.ClientBandWidth = params.get("ClientBandWidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤通用对象

    """

    def __init__(self):
        r"""
        :param Name: 过滤参数名
        :type Name: str
        :param Values: 过滤参数值
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTagInfo(AbstractModel):
    """引擎实例的标签信息

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param Key: 键
        :type Key: str
        :param Value: 值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NacosReplica(AbstractModel):
    """Nacos副本信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Role: 角色
        :type Role: str
        :param Status: 状态
        :type Status: str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Zone: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        """
        self.Name = None
        self.Role = None
        self.Status = None
        self.SubnetId = None
        self.Zone = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Role = params.get("Role")
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NacosServerInterface(AbstractModel):
    """nacos服务端接口列表，用于云监控

    """

    def __init__(self):
        r"""
        :param Interface: 接口名
注意：此字段可能返回 null，表示取不到有效值。
        :type Interface: str
        """
        self.Interface = None


    def _deserialize(self, params):
        self.Interface = params.get("Interface")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SREInstance(AbstractModel):
    """微服务注册引擎实例

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Name: 名称
        :type Name: str
        :param Edition: 版本号
        :type Edition: str
        :param Status: 状态, 枚举值:creating/create_fail/running/updating/update_fail/restarting/restart_fail/destroying/destroy_fail
        :type Status: str
        :param SpecId: 规格ID
        :type SpecId: str
        :param Replica: 副本数
        :type Replica: int
        :param Type: 类型
        :type Type: str
        :param VpcId: Vpc iD
        :type VpcId: str
        :param SubnetIds: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param EnableStorage: 是否开启持久化存储
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableStorage: bool
        :param StorageType: 数据存储方式
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param StorageCapacity: 云硬盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageCapacity: int
        :param Paymode: 计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Paymode: str
        :param EKSClusterID: EKS集群的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSClusterID: str
        :param CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param EnvInfos: 环境配置信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvInfos: list of EnvInfo
        :param EngineRegion: 引擎所在的区域
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        :param EnableInternet: 注册引擎是否开启公网
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableInternet: bool
        :param VpcInfos: 私有网络列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcInfos: list of VpcInfo
        :param ServiceGovernanceInfos: 服务治理相关信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGovernanceInfos: list of ServiceGovernanceInfo
        :param Tags: 实例的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of KVPair
        :param EnableConsoleInternet: 引擎实例是否开启控制台公网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConsoleInternet: bool
        :param EnableConsoleIntranet: 引擎实例是否开启控制台内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConsoleIntranet: bool
        :param ConfigInfoVisible: 引擎实例是否展示参数配置页面
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigInfoVisible: bool
        :param ConsoleDefaultPwd: 引擎实例控制台默认密码
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleDefaultPwd: str
        :param TradeType: 交易付费类型，0后付费/1预付费
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeType: int
        :param AutoRenewFlag: 自动续费标记：0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param CurDeadline: 预付费到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurDeadline: str
        :param IsolateTime: 隔离开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param RegionInfos: 实例地域相关的描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionInfos: list of DescribeInstanceRegionInfo
        """
        self.InstanceId = None
        self.Name = None
        self.Edition = None
        self.Status = None
        self.SpecId = None
        self.Replica = None
        self.Type = None
        self.VpcId = None
        self.SubnetIds = None
        self.EnableStorage = None
        self.StorageType = None
        self.StorageCapacity = None
        self.Paymode = None
        self.EKSClusterID = None
        self.CreateTime = None
        self.EnvInfos = None
        self.EngineRegion = None
        self.EnableInternet = None
        self.VpcInfos = None
        self.ServiceGovernanceInfos = None
        self.Tags = None
        self.EnableConsoleInternet = None
        self.EnableConsoleIntranet = None
        self.ConfigInfoVisible = None
        self.ConsoleDefaultPwd = None
        self.TradeType = None
        self.AutoRenewFlag = None
        self.CurDeadline = None
        self.IsolateTime = None
        self.RegionInfos = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Edition = params.get("Edition")
        self.Status = params.get("Status")
        self.SpecId = params.get("SpecId")
        self.Replica = params.get("Replica")
        self.Type = params.get("Type")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.EnableStorage = params.get("EnableStorage")
        self.StorageType = params.get("StorageType")
        self.StorageCapacity = params.get("StorageCapacity")
        self.Paymode = params.get("Paymode")
        self.EKSClusterID = params.get("EKSClusterID")
        self.CreateTime = params.get("CreateTime")
        if params.get("EnvInfos") is not None:
            self.EnvInfos = []
            for item in params.get("EnvInfos"):
                obj = EnvInfo()
                obj._deserialize(item)
                self.EnvInfos.append(obj)
        self.EngineRegion = params.get("EngineRegion")
        self.EnableInternet = params.get("EnableInternet")
        if params.get("VpcInfos") is not None:
            self.VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcInfos.append(obj)
        if params.get("ServiceGovernanceInfos") is not None:
            self.ServiceGovernanceInfos = []
            for item in params.get("ServiceGovernanceInfos"):
                obj = ServiceGovernanceInfo()
                obj._deserialize(item)
                self.ServiceGovernanceInfos.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = KVPair()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.EnableConsoleInternet = params.get("EnableConsoleInternet")
        self.EnableConsoleIntranet = params.get("EnableConsoleIntranet")
        self.ConfigInfoVisible = params.get("ConfigInfoVisible")
        self.ConsoleDefaultPwd = params.get("ConsoleDefaultPwd")
        self.TradeType = params.get("TradeType")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.CurDeadline = params.get("CurDeadline")
        self.IsolateTime = params.get("IsolateTime")
        if params.get("RegionInfos") is not None:
            self.RegionInfos = []
            for item in params.get("RegionInfos"):
                obj = DescribeInstanceRegionInfo()
                obj._deserialize(item)
                self.RegionInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceGovernanceInfo(AbstractModel):
    """服务治理相关的信息

    """

    def __init__(self):
        r"""
        :param EngineRegion: 引擎所在的地域
        :type EngineRegion: str
        :param BoundK8SInfos: 服务治理引擎绑定的kubernetes集群信息
        :type BoundK8SInfos: list of BoundK8SInfo
        :param VpcInfos: 服务治理引擎绑定的网络信息
        :type VpcInfos: list of VpcInfo
        :param AuthOpen: 当前实例鉴权是否开启
        :type AuthOpen: bool
        :param Features: 该实例支持的功能，鉴权就是 Auth
        :type Features: list of str
        :param MainPassword: 主账户名默认为 polaris，该值为主账户的默认密码
        :type MainPassword: str
        :param PgwVpcInfos: 服务治理pushgateway引擎绑定的网络信息
        :type PgwVpcInfos: list of VpcInfo
        """
        self.EngineRegion = None
        self.BoundK8SInfos = None
        self.VpcInfos = None
        self.AuthOpen = None
        self.Features = None
        self.MainPassword = None
        self.PgwVpcInfos = None


    def _deserialize(self, params):
        self.EngineRegion = params.get("EngineRegion")
        if params.get("BoundK8SInfos") is not None:
            self.BoundK8SInfos = []
            for item in params.get("BoundK8SInfos"):
                obj = BoundK8SInfo()
                obj._deserialize(item)
                self.BoundK8SInfos.append(obj)
        if params.get("VpcInfos") is not None:
            self.VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcInfos.append(obj)
        self.AuthOpen = params.get("AuthOpen")
        self.Features = params.get("Features")
        self.MainPassword = params.get("MainPassword")
        if params.get("PgwVpcInfos") is not None:
            self.PgwVpcInfos = []
            for item in params.get("PgwVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.PgwVpcInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """私有网络信息

    """

    def __init__(self):
        r"""
        :param VpcId: Vpc Id
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param IntranetAddress: 内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetAddress: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.IntranetAddress = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.IntranetAddress = params.get("IntranetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZookeeperReplica(AbstractModel):
    """Zookeeper副本信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Role: 角色
        :type Role: str
        :param Status: 状态
        :type Status: str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Zone: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param AliasName: 别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        """
        self.Name = None
        self.Role = None
        self.Status = None
        self.SubnetId = None
        self.Zone = None
        self.ZoneId = None
        self.AliasName = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Role = params.get("Role")
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.AliasName = params.get("AliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZookeeperServerInterface(AbstractModel):
    """Zookeeper服务端接口列表，用于云监控

    """

    def __init__(self):
        r"""
        :param Interface: 接口名
注意：此字段可能返回 null，表示取不到有效值。
        :type Interface: str
        """
        self.Interface = None


    def _deserialize(self, params):
        self.Interface = params.get("Interface")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        