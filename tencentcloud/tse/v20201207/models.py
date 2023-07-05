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
        :param _Name: 环境名称
        :type Name: str
        :param _EngineResourceSpec: 环境内引擎的节点规格 ID
-1C2G
-2C4G
兼容原spec-xxxxxx形式的规格ID
        :type EngineResourceSpec: str
        :param _EngineNodeNum: 环境内引擎的节点数量
        :type EngineNodeNum: int
        :param _StorageCapacity: 配置存储空间大小，以GB为单位
        :type StorageCapacity: int
        :param _VpcId: VPC ID。在 VPC 的子网内分配一个 IP 作为 ConfigServer 的访问地址
        :type VpcId: str
        :param _SubnetId: 子网 ID。在 VPC 的子网内分配一个 IP 作为 ConfigServer 的访问地址
        :type SubnetId: str
        :param _EnvDesc: 环境描述
        :type EnvDesc: str
        """
        self._Name = None
        self._EngineResourceSpec = None
        self._EngineNodeNum = None
        self._StorageCapacity = None
        self._VpcId = None
        self._SubnetId = None
        self._EnvDesc = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EngineResourceSpec(self):
        return self._EngineResourceSpec

    @EngineResourceSpec.setter
    def EngineResourceSpec(self, EngineResourceSpec):
        self._EngineResourceSpec = EngineResourceSpec

    @property
    def EngineNodeNum(self):
        return self._EngineNodeNum

    @EngineNodeNum.setter
    def EngineNodeNum(self, EngineNodeNum):
        self._EngineNodeNum = EngineNodeNum

    @property
    def StorageCapacity(self):
        return self._StorageCapacity

    @StorageCapacity.setter
    def StorageCapacity(self, StorageCapacity):
        self._StorageCapacity = StorageCapacity

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
    def EnvDesc(self):
        return self._EnvDesc

    @EnvDesc.setter
    def EnvDesc(self, EnvDesc):
        self._EnvDesc = EnvDesc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EngineResourceSpec = params.get("EngineResourceSpec")
        self._EngineNodeNum = params.get("EngineNodeNum")
        self._StorageCapacity = params.get("StorageCapacity")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._EnvDesc = params.get("EnvDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundK8SInfo(AbstractModel):
    """服务治理引擎绑定的kubernetes信息

    """

    def __init__(self):
        r"""
        :param _BoundClusterId: 绑定的kubernetes集群ID
        :type BoundClusterId: str
        :param _BoundClusterType: 绑定的kubernetes的集群类型，分tke和eks两种
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundClusterType: str
        :param _SyncMode: 服务同步模式，all为全量同步，demand为按需同步
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncMode: str
        """
        self._BoundClusterId = None
        self._BoundClusterType = None
        self._SyncMode = None

    @property
    def BoundClusterId(self):
        return self._BoundClusterId

    @BoundClusterId.setter
    def BoundClusterId(self, BoundClusterId):
        self._BoundClusterId = BoundClusterId

    @property
    def BoundClusterType(self):
        return self._BoundClusterType

    @BoundClusterType.setter
    def BoundClusterType(self, BoundClusterType):
        self._BoundClusterType = BoundClusterType

    @property
    def SyncMode(self):
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode


    def _deserialize(self, params):
        self._BoundClusterId = params.get("BoundClusterId")
        self._BoundClusterType = params.get("BoundClusterType")
        self._SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayNode(AbstractModel):
    """云原生API网关节点信息。

    """

    def __init__(self):
        r"""
        :param _NodeId: 云原生网关节点 id
        :type NodeId: str
        :param _NodeIp: 节点 ip
        :type NodeIp: str
        :param _ZoneId: Zone id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _Zone: Zone
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _GroupId: 分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 分组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._NodeId = None
        self._NodeIp = None
        self._ZoneId = None
        self._Zone = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeIp(self):
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

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
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeIp = params.get("NodeIp")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEngineRequest(AbstractModel):
    """CreateEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineType: 引擎类型。参考值：
- zookeeper
- nacos
- consul
- apollo
- eureka
- polaris
        :type EngineType: str
        :param _EngineVersion: 引擎的开源版本。每种引擎支持的开源版本不同，请参考产品文档或者控制台购买页
        :type EngineVersion: str
        :param _EngineProductVersion: 引擎的产品版本。参考值：
- STANDARD： 标准版

引擎各版本及可选择的规格、节点数说明：
apollo - STANDARD版本
规格列表：1C2G、2C4G、4C8G、8C16G、16C32G
节点数：1，2，3，4，5

eureka - STANDARD版本
规格列表：1C2G、2C4G、4C8G、8C16G、16C32G
节点数：3，4，5

polarismesh - STANDARD版本
规格列表：NUM50、NUM100、NUM200、NUM500、NUM1000、NUM5000、NUM10000、NUM50000

兼容原spec-xxxxxx形式的规格ID
        :type EngineProductVersion: str
        :param _EngineRegion: 引擎所在地域。参考值说明：
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
        :param _EngineName: 引擎名称。参考值：
- eurek-test
        :type EngineName: str
        :param _TradeType: 付费类型。参考值：
- 0：后付费
- 1：预付费（接口暂不支持创建预付费实例）
        :type TradeType: int
        :param _EngineResourceSpec: 引擎的节点规格 ID。参见EngineProductVersion字段说明
        :type EngineResourceSpec: str
        :param _EngineNodeNum: 引擎的节点数量。参见EngineProductVersion字段说明
        :type EngineNodeNum: int
        :param _VpcId: VPC ID。在 VPC 的子网内分配一个 IP 作为引擎的访问地址。参考值：
- vpc-conz6aix
        :type VpcId: str
        :param _SubnetId: 子网 ID。在 VPC 的子网内分配一个 IP 作为引擎的访问地址。参考值：
- subnet-ahde9me9
        :type SubnetId: str
        :param _ApolloEnvParams: Apollo 环境配置参数列表。参数说明：
如果创建Apollo类型，此参数为必填的环境信息列表，最多可选4个环境。环境信息参数说明：
- Name：环境名。参考值：prod, dev, fat, uat
- EngineResourceSpec：环境内引擎的节点规格ID。参见EngineProductVersion参数说明
- EngineNodeNum：环境内引擎的节点数量。参见EngineProductVersion参数说明，其中prod环境支持的节点数为2，3，4，5
- StorageCapacity：配置存储空间大小，以GB为单位，步长为5.参考值：35
- VpcId：VPC ID。参考值：vpc-conz6aix
- SubnetId：子网 ID。参考值：subnet-ahde9me9
        :type ApolloEnvParams: list of ApolloEnvParam
        :param _EngineTags: 引擎的标签列表。用户自定义的key/value形式，无参考值
        :type EngineTags: list of InstanceTagInfo
        :param _EngineAdmin: 引擎的初始帐号信息。可设置参数：
- Name：控制台初始用户名
- Password：控制台初始密码
- Token：引擎接口的管理员 Token
        :type EngineAdmin: :class:`tencentcloud.tse.v20201207.models.EngineAdmin`
        :param _PrepaidPeriod: 预付费时长，以月为单位
        :type PrepaidPeriod: int
        :param _PrepaidRenewFlag: 自动续费标记，仅预付费使用。参考值：
- 0：不自动续费
- 1：自动续费
        :type PrepaidRenewFlag: int
        :param _EngineRegionInfos: 跨地域部署的引擎地域配置详情
        :type EngineRegionInfos: list of EngineRegionInfo
        """
        self._EngineType = None
        self._EngineVersion = None
        self._EngineProductVersion = None
        self._EngineRegion = None
        self._EngineName = None
        self._TradeType = None
        self._EngineResourceSpec = None
        self._EngineNodeNum = None
        self._VpcId = None
        self._SubnetId = None
        self._ApolloEnvParams = None
        self._EngineTags = None
        self._EngineAdmin = None
        self._PrepaidPeriod = None
        self._PrepaidRenewFlag = None
        self._EngineRegionInfos = None

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def EngineProductVersion(self):
        return self._EngineProductVersion

    @EngineProductVersion.setter
    def EngineProductVersion(self, EngineProductVersion):
        self._EngineProductVersion = EngineProductVersion

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def EngineName(self):
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def TradeType(self):
        return self._TradeType

    @TradeType.setter
    def TradeType(self, TradeType):
        self._TradeType = TradeType

    @property
    def EngineResourceSpec(self):
        return self._EngineResourceSpec

    @EngineResourceSpec.setter
    def EngineResourceSpec(self, EngineResourceSpec):
        self._EngineResourceSpec = EngineResourceSpec

    @property
    def EngineNodeNum(self):
        return self._EngineNodeNum

    @EngineNodeNum.setter
    def EngineNodeNum(self, EngineNodeNum):
        self._EngineNodeNum = EngineNodeNum

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
    def ApolloEnvParams(self):
        return self._ApolloEnvParams

    @ApolloEnvParams.setter
    def ApolloEnvParams(self, ApolloEnvParams):
        self._ApolloEnvParams = ApolloEnvParams

    @property
    def EngineTags(self):
        return self._EngineTags

    @EngineTags.setter
    def EngineTags(self, EngineTags):
        self._EngineTags = EngineTags

    @property
    def EngineAdmin(self):
        return self._EngineAdmin

    @EngineAdmin.setter
    def EngineAdmin(self, EngineAdmin):
        self._EngineAdmin = EngineAdmin

    @property
    def PrepaidPeriod(self):
        return self._PrepaidPeriod

    @PrepaidPeriod.setter
    def PrepaidPeriod(self, PrepaidPeriod):
        self._PrepaidPeriod = PrepaidPeriod

    @property
    def PrepaidRenewFlag(self):
        return self._PrepaidRenewFlag

    @PrepaidRenewFlag.setter
    def PrepaidRenewFlag(self, PrepaidRenewFlag):
        self._PrepaidRenewFlag = PrepaidRenewFlag

    @property
    def EngineRegionInfos(self):
        return self._EngineRegionInfos

    @EngineRegionInfos.setter
    def EngineRegionInfos(self, EngineRegionInfos):
        self._EngineRegionInfos = EngineRegionInfos


    def _deserialize(self, params):
        self._EngineType = params.get("EngineType")
        self._EngineVersion = params.get("EngineVersion")
        self._EngineProductVersion = params.get("EngineProductVersion")
        self._EngineRegion = params.get("EngineRegion")
        self._EngineName = params.get("EngineName")
        self._TradeType = params.get("TradeType")
        self._EngineResourceSpec = params.get("EngineResourceSpec")
        self._EngineNodeNum = params.get("EngineNodeNum")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("ApolloEnvParams") is not None:
            self._ApolloEnvParams = []
            for item in params.get("ApolloEnvParams"):
                obj = ApolloEnvParam()
                obj._deserialize(item)
                self._ApolloEnvParams.append(obj)
        if params.get("EngineTags") is not None:
            self._EngineTags = []
            for item in params.get("EngineTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._EngineTags.append(obj)
        if params.get("EngineAdmin") is not None:
            self._EngineAdmin = EngineAdmin()
            self._EngineAdmin._deserialize(params.get("EngineAdmin"))
        self._PrepaidPeriod = params.get("PrepaidPeriod")
        self._PrepaidRenewFlag = params.get("PrepaidRenewFlag")
        if params.get("EngineRegionInfos") is not None:
            self._EngineRegionInfos = []
            for item in params.get("EngineRegionInfos"):
                obj = EngineRegionInfo()
                obj._deserialize(item)
                self._EngineRegionInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEngineResponse(AbstractModel):
    """CreateEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎实例 ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DeleteEngineRequest(AbstractModel):
    """DeleteEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎实例 ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEngineResponse(AbstractModel):
    """DeleteEngine返回参数结构体

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


class DescribeCloudNativeAPIGatewayNodesRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 实例分组id
        :type GroupId: str
        :param _Limit: 翻页获取多少个
        :type Limit: int
        :param _Offset: 翻页从第几个开始获取
        :type Offset: int
        """
        self._GatewayId = None
        self._GroupId = None
        self._Limit = None
        self._Offset = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayNodesResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生网关节点列表结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeCloudNativeAPIGatewayNodesResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayNodesResult(AbstractModel):
    """获取网关节点信息

    """

    def __init__(self):
        r"""
        :param _TotalCount: 获取云原生API网关节点列表响应结果。
        :type TotalCount: int
        :param _NodeList: 云原生API网关节点列表。
        :type NodeList: list of CloudNativeAPIGatewayNode
        """
        self._TotalCount = None
        self._NodeList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = CloudNativeAPIGatewayNode()
                obj._deserialize(item)
                self._NodeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceRegionInfo(AbstractModel):
    """实例地域信息描述

    """

    def __init__(self):
        r"""
        :param _EngineRegion: 引擎部署地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        :param _Replica: 引擎在该地域的副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replica: int
        :param _SpecId: 引擎在该地域的规格id
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecId: str
        :param _IntranetVpcInfos: 内网的网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetVpcInfos: list of VpcInfo
        :param _EnableClientInternet: 是否开公网
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableClientInternet: bool
        """
        self._EngineRegion = None
        self._Replica = None
        self._SpecId = None
        self._IntranetVpcInfos = None
        self._EnableClientInternet = None

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def Replica(self):
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def IntranetVpcInfos(self):
        return self._IntranetVpcInfos

    @IntranetVpcInfos.setter
    def IntranetVpcInfos(self, IntranetVpcInfos):
        self._IntranetVpcInfos = IntranetVpcInfos

    @property
    def EnableClientInternet(self):
        return self._EnableClientInternet

    @EnableClientInternet.setter
    def EnableClientInternet(self, EnableClientInternet):
        self._EnableClientInternet = EnableClientInternet


    def _deserialize(self, params):
        self._EngineRegion = params.get("EngineRegion")
        self._Replica = params.get("Replica")
        self._SpecId = params.get("SpecId")
        if params.get("IntranetVpcInfos") is not None:
            self._IntranetVpcInfos = []
            for item in params.get("IntranetVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._IntranetVpcInfos.append(obj)
        self._EnableClientInternet = params.get("EnableClientInternet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosReplicasRequest(AbstractModel):
    """DescribeNacosReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎实例ID
        :type InstanceId: str
        :param _Limit: 副本列表Limit
        :type Limit: int
        :param _Offset: 副本列表Offset
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosReplicasResponse(AbstractModel):
    """DescribeNacosReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Replicas: 引擎实例副本信息
        :type Replicas: list of NacosReplica
        :param _TotalCount: 副本个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Replicas = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

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
        if params.get("Replicas") is not None:
            self._Replicas = []
            for item in params.get("Replicas"):
                obj = NacosReplica()
                obj._deserialize(item)
                self._Replicas.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNacosServerInterfacesRequest(AbstractModel):
    """DescribeNacosServerInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Limit: 返回的列表个数
        :type Limit: int
        :param _Offset: 返回的列表起始偏移量
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosServerInterfacesResponse(AbstractModel):
    """DescribeNacosServerInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 接口总个数
        :type TotalCount: int
        :param _Content: 接口列表
        :type Content: list of NacosServerInterface
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = NacosServerInterface()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSREInstanceAccessAddressRequest(AbstractModel):
    """DescribeSREInstanceAccessAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 注册引擎实例Id
        :type InstanceId: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Workload: 引擎其他组件名称（pushgateway、polaris-limiter）
        :type Workload: str
        :param _EngineRegion: 部署地域
        :type EngineRegion: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Workload = None
        self._EngineRegion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Workload(self):
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Workload = params.get("Workload")
        self._EngineRegion = params.get("EngineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstanceAccessAddressResponse(AbstractModel):
    """DescribeSREInstanceAccessAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntranetAddress: 内网访问地址
        :type IntranetAddress: str
        :param _InternetAddress: 公网访问地址
        :type InternetAddress: str
        :param _EnvAddressInfos: apollo多环境公网ip
        :type EnvAddressInfos: list of EnvAddressInfo
        :param _ConsoleInternetAddress: 控制台公网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleInternetAddress: str
        :param _ConsoleIntranetAddress: 控制台内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleIntranetAddress: str
        :param _InternetBandWidth: 客户端公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetBandWidth: int
        :param _ConsoleInternetBandWidth: 控制台公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleInternetBandWidth: int
        :param _LimiterAddressInfos: 北极星限流server节点接入IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LimiterAddressInfos: list of PolarisLimiterAddress
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntranetAddress = None
        self._InternetAddress = None
        self._EnvAddressInfos = None
        self._ConsoleInternetAddress = None
        self._ConsoleIntranetAddress = None
        self._InternetBandWidth = None
        self._ConsoleInternetBandWidth = None
        self._LimiterAddressInfos = None
        self._RequestId = None

    @property
    def IntranetAddress(self):
        return self._IntranetAddress

    @IntranetAddress.setter
    def IntranetAddress(self, IntranetAddress):
        self._IntranetAddress = IntranetAddress

    @property
    def InternetAddress(self):
        return self._InternetAddress

    @InternetAddress.setter
    def InternetAddress(self, InternetAddress):
        self._InternetAddress = InternetAddress

    @property
    def EnvAddressInfos(self):
        return self._EnvAddressInfos

    @EnvAddressInfos.setter
    def EnvAddressInfos(self, EnvAddressInfos):
        self._EnvAddressInfos = EnvAddressInfos

    @property
    def ConsoleInternetAddress(self):
        return self._ConsoleInternetAddress

    @ConsoleInternetAddress.setter
    def ConsoleInternetAddress(self, ConsoleInternetAddress):
        self._ConsoleInternetAddress = ConsoleInternetAddress

    @property
    def ConsoleIntranetAddress(self):
        return self._ConsoleIntranetAddress

    @ConsoleIntranetAddress.setter
    def ConsoleIntranetAddress(self, ConsoleIntranetAddress):
        self._ConsoleIntranetAddress = ConsoleIntranetAddress

    @property
    def InternetBandWidth(self):
        return self._InternetBandWidth

    @InternetBandWidth.setter
    def InternetBandWidth(self, InternetBandWidth):
        self._InternetBandWidth = InternetBandWidth

    @property
    def ConsoleInternetBandWidth(self):
        return self._ConsoleInternetBandWidth

    @ConsoleInternetBandWidth.setter
    def ConsoleInternetBandWidth(self, ConsoleInternetBandWidth):
        self._ConsoleInternetBandWidth = ConsoleInternetBandWidth

    @property
    def LimiterAddressInfos(self):
        return self._LimiterAddressInfos

    @LimiterAddressInfos.setter
    def LimiterAddressInfos(self, LimiterAddressInfos):
        self._LimiterAddressInfos = LimiterAddressInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IntranetAddress = params.get("IntranetAddress")
        self._InternetAddress = params.get("InternetAddress")
        if params.get("EnvAddressInfos") is not None:
            self._EnvAddressInfos = []
            for item in params.get("EnvAddressInfos"):
                obj = EnvAddressInfo()
                obj._deserialize(item)
                self._EnvAddressInfos.append(obj)
        self._ConsoleInternetAddress = params.get("ConsoleInternetAddress")
        self._ConsoleIntranetAddress = params.get("ConsoleIntranetAddress")
        self._InternetBandWidth = params.get("InternetBandWidth")
        self._ConsoleInternetBandWidth = params.get("ConsoleInternetBandWidth")
        if params.get("LimiterAddressInfos") is not None:
            self._LimiterAddressInfos = []
            for item in params.get("LimiterAddressInfos"):
                obj = PolarisLimiterAddress()
                obj._deserialize(item)
                self._LimiterAddressInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSREInstancesRequest(AbstractModel):
    """DescribeSREInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 请求过滤参数
        :type Filters: list of Filter
        :param _Limit: 翻页单页查询限制数量[0,1000], 默认值0
        :type Limit: int
        :param _Offset: 翻页单页偏移量，默认值0
        :type Offset: int
        :param _QueryType: 查询类型
        :type QueryType: str
        :param _QuerySource: 调用方来源
        :type QuerySource: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._QueryType = None
        self._QuerySource = None

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

    @property
    def QueryType(self):
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def QuerySource(self):
        return self._QuerySource

    @QuerySource.setter
    def QuerySource(self, QuerySource):
        self._QuerySource = QuerySource


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._QueryType = params.get("QueryType")
        self._QuerySource = params.get("QuerySource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstancesResponse(AbstractModel):
    """DescribeSREInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _Content: 实例记录
        :type Content: list of SREInstance
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = SREInstance()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZookeeperReplicasRequest(AbstractModel):
    """DescribeZookeeperReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 注册引擎实例ID
        :type InstanceId: str
        :param _Limit: 副本列表Limit
        :type Limit: int
        :param _Offset: 副本列表Offset
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZookeeperReplicasResponse(AbstractModel):
    """DescribeZookeeperReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Replicas: 注册引擎实例副本信息
        :type Replicas: list of ZookeeperReplica
        :param _TotalCount: 副本个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Replicas = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

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
        if params.get("Replicas") is not None:
            self._Replicas = []
            for item in params.get("Replicas"):
                obj = ZookeeperReplica()
                obj._deserialize(item)
                self._Replicas.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeZookeeperServerInterfacesRequest(AbstractModel):
    """DescribeZookeeperServerInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Limit: 返回的列表个数
        :type Limit: int
        :param _Offset: 返回的列表起始偏移量
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZookeeperServerInterfacesResponse(AbstractModel):
    """DescribeZookeeperServerInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 接口总个数
        :type TotalCount: int
        :param _Content: 接口列表
        :type Content: list of ZookeeperServerInterface
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = ZookeeperServerInterface()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class EngineAdmin(AbstractModel):
    """引擎的初始管理帐号

    """

    def __init__(self):
        r"""
        :param _Name: 控制台初始用户名
        :type Name: str
        :param _Password: 控制台初始密码
        :type Password: str
        :param _Token: 引擎接口的管理员 Token
        :type Token: str
        """
        self._Name = None
        self._Password = None
        self._Token = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EngineRegionInfo(AbstractModel):
    """引擎地域配置详情

    """

    def __init__(self):
        r"""
        :param _EngineRegion: 引擎节点所在地域
        :type EngineRegion: str
        :param _Replica: 此地域节点分配数量
        :type Replica: int
        :param _VpcInfos: 集群网络信息
        :type VpcInfos: list of VpcInfo
        """
        self._EngineRegion = None
        self._Replica = None
        self._VpcInfos = None

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def Replica(self):
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def VpcInfos(self):
        return self._VpcInfos

    @VpcInfos.setter
    def VpcInfos(self, VpcInfos):
        self._VpcInfos = VpcInfos


    def _deserialize(self, params):
        self._EngineRegion = params.get("EngineRegion")
        self._Replica = params.get("Replica")
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvAddressInfo(AbstractModel):
    """多环境网络信息

    """

    def __init__(self):
        r"""
        :param _EnvName: 环境名
        :type EnvName: str
        :param _EnableConfigInternet: 是否开启config公网
        :type EnableConfigInternet: bool
        :param _ConfigInternetServiceIp: config公网ip
        :type ConfigInternetServiceIp: str
        :param _ConfigIntranetAddress: config内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigIntranetAddress: str
        :param _EnableConfigIntranet: 是否开启config内网clb
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConfigIntranet: bool
        :param _InternetBandWidth: 客户端公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetBandWidth: int
        """
        self._EnvName = None
        self._EnableConfigInternet = None
        self._ConfigInternetServiceIp = None
        self._ConfigIntranetAddress = None
        self._EnableConfigIntranet = None
        self._InternetBandWidth = None

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnableConfigInternet(self):
        return self._EnableConfigInternet

    @EnableConfigInternet.setter
    def EnableConfigInternet(self, EnableConfigInternet):
        self._EnableConfigInternet = EnableConfigInternet

    @property
    def ConfigInternetServiceIp(self):
        return self._ConfigInternetServiceIp

    @ConfigInternetServiceIp.setter
    def ConfigInternetServiceIp(self, ConfigInternetServiceIp):
        self._ConfigInternetServiceIp = ConfigInternetServiceIp

    @property
    def ConfigIntranetAddress(self):
        return self._ConfigIntranetAddress

    @ConfigIntranetAddress.setter
    def ConfigIntranetAddress(self, ConfigIntranetAddress):
        self._ConfigIntranetAddress = ConfigIntranetAddress

    @property
    def EnableConfigIntranet(self):
        return self._EnableConfigIntranet

    @EnableConfigIntranet.setter
    def EnableConfigIntranet(self, EnableConfigIntranet):
        self._EnableConfigIntranet = EnableConfigIntranet

    @property
    def InternetBandWidth(self):
        return self._InternetBandWidth

    @InternetBandWidth.setter
    def InternetBandWidth(self, InternetBandWidth):
        self._InternetBandWidth = InternetBandWidth


    def _deserialize(self, params):
        self._EnvName = params.get("EnvName")
        self._EnableConfigInternet = params.get("EnableConfigInternet")
        self._ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        self._ConfigIntranetAddress = params.get("ConfigIntranetAddress")
        self._EnableConfigIntranet = params.get("EnableConfigIntranet")
        self._InternetBandWidth = params.get("InternetBandWidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """环境具体信息

    """

    def __init__(self):
        r"""
        :param _EnvName: 环境名称
        :type EnvName: str
        :param _VpcInfos: 环境对应的网络信息
        :type VpcInfos: list of VpcInfo
        :param _StorageCapacity: 云硬盘容量
        :type StorageCapacity: int
        :param _Status: 运行状态
        :type Status: str
        :param _AdminServiceIp: Admin service 访问地址
        :type AdminServiceIp: str
        :param _ConfigServiceIp: Config service访问地址
        :type ConfigServiceIp: str
        :param _EnableConfigInternet: 是否开启config-server公网
        :type EnableConfigInternet: bool
        :param _ConfigInternetServiceIp: config-server公网访问地址
        :type ConfigInternetServiceIp: str
        :param _SpecId: 规格ID
        :type SpecId: str
        :param _EnvReplica: 环境的节点数
        :type EnvReplica: int
        :param _RunningCount: 环境运行的节点数
        :type RunningCount: int
        :param _AliasEnvName: 环境别名
        :type AliasEnvName: str
        :param _EnvDesc: 环境描述
        :type EnvDesc: str
        :param _ClientBandWidth: 客户端带宽
        :type ClientBandWidth: int
        :param _EnableConfigIntranet: 客户端内网开关
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConfigIntranet: bool
        """
        self._EnvName = None
        self._VpcInfos = None
        self._StorageCapacity = None
        self._Status = None
        self._AdminServiceIp = None
        self._ConfigServiceIp = None
        self._EnableConfigInternet = None
        self._ConfigInternetServiceIp = None
        self._SpecId = None
        self._EnvReplica = None
        self._RunningCount = None
        self._AliasEnvName = None
        self._EnvDesc = None
        self._ClientBandWidth = None
        self._EnableConfigIntranet = None

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def VpcInfos(self):
        return self._VpcInfos

    @VpcInfos.setter
    def VpcInfos(self, VpcInfos):
        self._VpcInfos = VpcInfos

    @property
    def StorageCapacity(self):
        return self._StorageCapacity

    @StorageCapacity.setter
    def StorageCapacity(self, StorageCapacity):
        self._StorageCapacity = StorageCapacity

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AdminServiceIp(self):
        return self._AdminServiceIp

    @AdminServiceIp.setter
    def AdminServiceIp(self, AdminServiceIp):
        self._AdminServiceIp = AdminServiceIp

    @property
    def ConfigServiceIp(self):
        return self._ConfigServiceIp

    @ConfigServiceIp.setter
    def ConfigServiceIp(self, ConfigServiceIp):
        self._ConfigServiceIp = ConfigServiceIp

    @property
    def EnableConfigInternet(self):
        return self._EnableConfigInternet

    @EnableConfigInternet.setter
    def EnableConfigInternet(self, EnableConfigInternet):
        self._EnableConfigInternet = EnableConfigInternet

    @property
    def ConfigInternetServiceIp(self):
        return self._ConfigInternetServiceIp

    @ConfigInternetServiceIp.setter
    def ConfigInternetServiceIp(self, ConfigInternetServiceIp):
        self._ConfigInternetServiceIp = ConfigInternetServiceIp

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def EnvReplica(self):
        return self._EnvReplica

    @EnvReplica.setter
    def EnvReplica(self, EnvReplica):
        self._EnvReplica = EnvReplica

    @property
    def RunningCount(self):
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def AliasEnvName(self):
        return self._AliasEnvName

    @AliasEnvName.setter
    def AliasEnvName(self, AliasEnvName):
        self._AliasEnvName = AliasEnvName

    @property
    def EnvDesc(self):
        return self._EnvDesc

    @EnvDesc.setter
    def EnvDesc(self, EnvDesc):
        self._EnvDesc = EnvDesc

    @property
    def ClientBandWidth(self):
        return self._ClientBandWidth

    @ClientBandWidth.setter
    def ClientBandWidth(self, ClientBandWidth):
        self._ClientBandWidth = ClientBandWidth

    @property
    def EnableConfigIntranet(self):
        return self._EnableConfigIntranet

    @EnableConfigIntranet.setter
    def EnableConfigIntranet(self, EnableConfigIntranet):
        self._EnableConfigIntranet = EnableConfigIntranet


    def _deserialize(self, params):
        self._EnvName = params.get("EnvName")
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
        self._StorageCapacity = params.get("StorageCapacity")
        self._Status = params.get("Status")
        self._AdminServiceIp = params.get("AdminServiceIp")
        self._ConfigServiceIp = params.get("ConfigServiceIp")
        self._EnableConfigInternet = params.get("EnableConfigInternet")
        self._ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        self._SpecId = params.get("SpecId")
        self._EnvReplica = params.get("EnvReplica")
        self._RunningCount = params.get("RunningCount")
        self._AliasEnvName = params.get("AliasEnvName")
        self._EnvDesc = params.get("EnvDesc")
        self._ClientBandWidth = params.get("ClientBandWidth")
        self._EnableConfigIntranet = params.get("EnableConfigIntranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤通用对象

    """

    def __init__(self):
        r"""
        :param _Name: 过滤参数名
        :type Name: str
        :param _Values: 过滤参数值
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
        


class InstanceTagInfo(AbstractModel):
    """引擎实例的标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
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
        


class KVPair(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NacosReplica(AbstractModel):
    """Nacos副本信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Role: 角色
        :type Role: str
        :param _Status: 状态
        :type Status: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Zone: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _VpcId: VPC ID	
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        """
        self._Name = None
        self._Role = None
        self._Status = None
        self._SubnetId = None
        self._Zone = None
        self._ZoneId = None
        self._VpcId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._SubnetId = params.get("SubnetId")
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NacosServerInterface(AbstractModel):
    """nacos服务端接口列表，用于云监控

    """

    def __init__(self):
        r"""
        :param _Interface: 接口名
注意：此字段可能返回 null，表示取不到有效值。
        :type Interface: str
        """
        self._Interface = None

    @property
    def Interface(self):
        return self._Interface

    @Interface.setter
    def Interface(self, Interface):
        self._Interface = Interface


    def _deserialize(self, params):
        self._Interface = params.get("Interface")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolarisLimiterAddress(AbstractModel):
    """查询Limiter的接入地址

    """

    def __init__(self):
        r"""
        :param _IntranetAddress: VPC接入IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetAddress: str
        """
        self._IntranetAddress = None

    @property
    def IntranetAddress(self):
        return self._IntranetAddress

    @IntranetAddress.setter
    def IntranetAddress(self, IntranetAddress):
        self._IntranetAddress = IntranetAddress


    def _deserialize(self, params):
        self._IntranetAddress = params.get("IntranetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SREInstance(AbstractModel):
    """微服务注册引擎实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Name: 名称
        :type Name: str
        :param _Edition: 版本号
        :type Edition: str
        :param _Status: 状态, 枚举值:creating/create_fail/running/updating/update_fail/restarting/restart_fail/destroying/destroy_fail
        :type Status: str
        :param _SpecId: 规格ID
        :type SpecId: str
        :param _Replica: 副本数
        :type Replica: int
        :param _Type: 类型
        :type Type: str
        :param _VpcId: Vpc iD
        :type VpcId: str
        :param _SubnetIds: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _EnableStorage: 是否开启持久化存储
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableStorage: bool
        :param _StorageType: 数据存储方式
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param _StorageCapacity: 云硬盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageCapacity: int
        :param _Paymode: 计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Paymode: str
        :param _EKSClusterID: EKS集群的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSClusterID: str
        :param _CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _EnvInfos: 环境配置信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvInfos: list of EnvInfo
        :param _EngineRegion: 引擎所在的区域
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        :param _EnableInternet: 注册引擎是否开启公网
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableInternet: bool
        :param _VpcInfos: 私有网络列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcInfos: list of VpcInfo
        :param _ServiceGovernanceInfos: 服务治理相关信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGovernanceInfos: list of ServiceGovernanceInfo
        :param _Tags: 实例的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of KVPair
        :param _EnableConsoleInternet: 引擎实例是否开启控制台公网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConsoleInternet: bool
        :param _EnableConsoleIntranet: 引擎实例是否开启控制台内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConsoleIntranet: bool
        :param _ConfigInfoVisible: 引擎实例是否展示参数配置页面
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigInfoVisible: bool
        :param _ConsoleDefaultPwd: 引擎实例控制台默认密码
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleDefaultPwd: str
        :param _TradeType: 交易付费类型，0后付费/1预付费
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeType: int
        :param _AutoRenewFlag: 自动续费标记：0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _CurDeadline: 预付费到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurDeadline: str
        :param _IsolateTime: 隔离开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param _RegionInfos: 实例地域相关的描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionInfos: list of DescribeInstanceRegionInfo
        :param _EKSType: 所在EKS环境，分为common和yunti
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSType: str
        :param _FeatureVersion: 引擎的产品版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureVersion: str
        :param _EnableClientIntranet: 引擎实例是否开启客户端内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableClientIntranet: bool
        """
        self._InstanceId = None
        self._Name = None
        self._Edition = None
        self._Status = None
        self._SpecId = None
        self._Replica = None
        self._Type = None
        self._VpcId = None
        self._SubnetIds = None
        self._EnableStorage = None
        self._StorageType = None
        self._StorageCapacity = None
        self._Paymode = None
        self._EKSClusterID = None
        self._CreateTime = None
        self._EnvInfos = None
        self._EngineRegion = None
        self._EnableInternet = None
        self._VpcInfos = None
        self._ServiceGovernanceInfos = None
        self._Tags = None
        self._EnableConsoleInternet = None
        self._EnableConsoleIntranet = None
        self._ConfigInfoVisible = None
        self._ConsoleDefaultPwd = None
        self._TradeType = None
        self._AutoRenewFlag = None
        self._CurDeadline = None
        self._IsolateTime = None
        self._RegionInfos = None
        self._EKSType = None
        self._FeatureVersion = None
        self._EnableClientIntranet = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def Replica(self):
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def EnableStorage(self):
        return self._EnableStorage

    @EnableStorage.setter
    def EnableStorage(self, EnableStorage):
        self._EnableStorage = EnableStorage

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageCapacity(self):
        return self._StorageCapacity

    @StorageCapacity.setter
    def StorageCapacity(self, StorageCapacity):
        self._StorageCapacity = StorageCapacity

    @property
    def Paymode(self):
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def EKSClusterID(self):
        return self._EKSClusterID

    @EKSClusterID.setter
    def EKSClusterID(self, EKSClusterID):
        self._EKSClusterID = EKSClusterID

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnvInfos(self):
        return self._EnvInfos

    @EnvInfos.setter
    def EnvInfos(self, EnvInfos):
        self._EnvInfos = EnvInfos

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def EnableInternet(self):
        return self._EnableInternet

    @EnableInternet.setter
    def EnableInternet(self, EnableInternet):
        self._EnableInternet = EnableInternet

    @property
    def VpcInfos(self):
        return self._VpcInfos

    @VpcInfos.setter
    def VpcInfos(self, VpcInfos):
        self._VpcInfos = VpcInfos

    @property
    def ServiceGovernanceInfos(self):
        return self._ServiceGovernanceInfos

    @ServiceGovernanceInfos.setter
    def ServiceGovernanceInfos(self, ServiceGovernanceInfos):
        self._ServiceGovernanceInfos = ServiceGovernanceInfos

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnableConsoleInternet(self):
        return self._EnableConsoleInternet

    @EnableConsoleInternet.setter
    def EnableConsoleInternet(self, EnableConsoleInternet):
        self._EnableConsoleInternet = EnableConsoleInternet

    @property
    def EnableConsoleIntranet(self):
        return self._EnableConsoleIntranet

    @EnableConsoleIntranet.setter
    def EnableConsoleIntranet(self, EnableConsoleIntranet):
        self._EnableConsoleIntranet = EnableConsoleIntranet

    @property
    def ConfigInfoVisible(self):
        return self._ConfigInfoVisible

    @ConfigInfoVisible.setter
    def ConfigInfoVisible(self, ConfigInfoVisible):
        self._ConfigInfoVisible = ConfigInfoVisible

    @property
    def ConsoleDefaultPwd(self):
        return self._ConsoleDefaultPwd

    @ConsoleDefaultPwd.setter
    def ConsoleDefaultPwd(self, ConsoleDefaultPwd):
        self._ConsoleDefaultPwd = ConsoleDefaultPwd

    @property
    def TradeType(self):
        return self._TradeType

    @TradeType.setter
    def TradeType(self, TradeType):
        self._TradeType = TradeType

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def RegionInfos(self):
        return self._RegionInfos

    @RegionInfos.setter
    def RegionInfos(self, RegionInfos):
        self._RegionInfos = RegionInfos

    @property
    def EKSType(self):
        return self._EKSType

    @EKSType.setter
    def EKSType(self, EKSType):
        self._EKSType = EKSType

    @property
    def FeatureVersion(self):
        return self._FeatureVersion

    @FeatureVersion.setter
    def FeatureVersion(self, FeatureVersion):
        self._FeatureVersion = FeatureVersion

    @property
    def EnableClientIntranet(self):
        return self._EnableClientIntranet

    @EnableClientIntranet.setter
    def EnableClientIntranet(self, EnableClientIntranet):
        self._EnableClientIntranet = EnableClientIntranet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Edition = params.get("Edition")
        self._Status = params.get("Status")
        self._SpecId = params.get("SpecId")
        self._Replica = params.get("Replica")
        self._Type = params.get("Type")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._EnableStorage = params.get("EnableStorage")
        self._StorageType = params.get("StorageType")
        self._StorageCapacity = params.get("StorageCapacity")
        self._Paymode = params.get("Paymode")
        self._EKSClusterID = params.get("EKSClusterID")
        self._CreateTime = params.get("CreateTime")
        if params.get("EnvInfos") is not None:
            self._EnvInfos = []
            for item in params.get("EnvInfos"):
                obj = EnvInfo()
                obj._deserialize(item)
                self._EnvInfos.append(obj)
        self._EngineRegion = params.get("EngineRegion")
        self._EnableInternet = params.get("EnableInternet")
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
        if params.get("ServiceGovernanceInfos") is not None:
            self._ServiceGovernanceInfos = []
            for item in params.get("ServiceGovernanceInfos"):
                obj = ServiceGovernanceInfo()
                obj._deserialize(item)
                self._ServiceGovernanceInfos.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = KVPair()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnableConsoleInternet = params.get("EnableConsoleInternet")
        self._EnableConsoleIntranet = params.get("EnableConsoleIntranet")
        self._ConfigInfoVisible = params.get("ConfigInfoVisible")
        self._ConsoleDefaultPwd = params.get("ConsoleDefaultPwd")
        self._TradeType = params.get("TradeType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        self._IsolateTime = params.get("IsolateTime")
        if params.get("RegionInfos") is not None:
            self._RegionInfos = []
            for item in params.get("RegionInfos"):
                obj = DescribeInstanceRegionInfo()
                obj._deserialize(item)
                self._RegionInfos.append(obj)
        self._EKSType = params.get("EKSType")
        self._FeatureVersion = params.get("FeatureVersion")
        self._EnableClientIntranet = params.get("EnableClientIntranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceGovernanceInfo(AbstractModel):
    """服务治理相关的信息

    """

    def __init__(self):
        r"""
        :param _EngineRegion: 引擎所在的地域
        :type EngineRegion: str
        :param _BoundK8SInfos: 服务治理引擎绑定的kubernetes集群信息
        :type BoundK8SInfos: list of BoundK8SInfo
        :param _VpcInfos: 服务治理引擎绑定的网络信息
        :type VpcInfos: list of VpcInfo
        :param _AuthOpen: 当前实例鉴权是否开启
        :type AuthOpen: bool
        :param _Features: 该实例支持的功能，鉴权就是 Auth
        :type Features: list of str
        :param _MainPassword: 主账户名默认为 polaris，该值为主账户的默认密码
        :type MainPassword: str
        :param _PgwVpcInfos: 服务治理pushgateway引擎绑定的网络信息
        :type PgwVpcInfos: list of VpcInfo
        :param _LimiterVpcInfos: 服务治理限流server引擎绑定的网络信息
        :type LimiterVpcInfos: list of VpcInfo
        """
        self._EngineRegion = None
        self._BoundK8SInfos = None
        self._VpcInfos = None
        self._AuthOpen = None
        self._Features = None
        self._MainPassword = None
        self._PgwVpcInfos = None
        self._LimiterVpcInfos = None

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def BoundK8SInfos(self):
        return self._BoundK8SInfos

    @BoundK8SInfos.setter
    def BoundK8SInfos(self, BoundK8SInfos):
        self._BoundK8SInfos = BoundK8SInfos

    @property
    def VpcInfos(self):
        return self._VpcInfos

    @VpcInfos.setter
    def VpcInfos(self, VpcInfos):
        self._VpcInfos = VpcInfos

    @property
    def AuthOpen(self):
        return self._AuthOpen

    @AuthOpen.setter
    def AuthOpen(self, AuthOpen):
        self._AuthOpen = AuthOpen

    @property
    def Features(self):
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def MainPassword(self):
        return self._MainPassword

    @MainPassword.setter
    def MainPassword(self, MainPassword):
        self._MainPassword = MainPassword

    @property
    def PgwVpcInfos(self):
        return self._PgwVpcInfos

    @PgwVpcInfos.setter
    def PgwVpcInfos(self, PgwVpcInfos):
        self._PgwVpcInfos = PgwVpcInfos

    @property
    def LimiterVpcInfos(self):
        return self._LimiterVpcInfos

    @LimiterVpcInfos.setter
    def LimiterVpcInfos(self, LimiterVpcInfos):
        self._LimiterVpcInfos = LimiterVpcInfos


    def _deserialize(self, params):
        self._EngineRegion = params.get("EngineRegion")
        if params.get("BoundK8SInfos") is not None:
            self._BoundK8SInfos = []
            for item in params.get("BoundK8SInfos"):
                obj = BoundK8SInfo()
                obj._deserialize(item)
                self._BoundK8SInfos.append(obj)
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
        self._AuthOpen = params.get("AuthOpen")
        self._Features = params.get("Features")
        self._MainPassword = params.get("MainPassword")
        if params.get("PgwVpcInfos") is not None:
            self._PgwVpcInfos = []
            for item in params.get("PgwVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._PgwVpcInfos.append(obj)
        if params.get("LimiterVpcInfos") is not None:
            self._LimiterVpcInfos = []
            for item in params.get("LimiterVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._LimiterVpcInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEngineInternetAccessRequest(AbstractModel):
    """UpdateEngineInternetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎ID
        :type InstanceId: str
        :param _EngineType: 引擎类型
        :type EngineType: str
        :param _EnableClientInternetAccess: 是否开启客户端公网访问，true开 false关
        :type EnableClientInternetAccess: bool
        """
        self._InstanceId = None
        self._EngineType = None
        self._EnableClientInternetAccess = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def EnableClientInternetAccess(self):
        return self._EnableClientInternetAccess

    @EnableClientInternetAccess.setter
    def EnableClientInternetAccess(self, EnableClientInternetAccess):
        self._EnableClientInternetAccess = EnableClientInternetAccess


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EngineType = params.get("EngineType")
        self._EnableClientInternetAccess = params.get("EnableClientInternetAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEngineInternetAccessResponse(AbstractModel):
    """UpdateEngineInternetAccess返回参数结构体

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


class VpcInfo(AbstractModel):
    """私有网络信息

    """

    def __init__(self):
        r"""
        :param _VpcId: Vpc Id
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _IntranetAddress: 内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetAddress: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._IntranetAddress = None

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
    def IntranetAddress(self):
        return self._IntranetAddress

    @IntranetAddress.setter
    def IntranetAddress(self, IntranetAddress):
        self._IntranetAddress = IntranetAddress


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._IntranetAddress = params.get("IntranetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZookeeperReplica(AbstractModel):
    """Zookeeper副本信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Role: 角色
        :type Role: str
        :param _Status: 状态
        :type Status: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Zone: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _AliasName: 别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param _VpcId: VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        """
        self._Name = None
        self._Role = None
        self._Status = None
        self._SubnetId = None
        self._Zone = None
        self._ZoneId = None
        self._AliasName = None
        self._VpcId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._SubnetId = params.get("SubnetId")
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._AliasName = params.get("AliasName")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZookeeperServerInterface(AbstractModel):
    """Zookeeper服务端接口列表，用于云监控

    """

    def __init__(self):
        r"""
        :param _Interface: 接口名
注意：此字段可能返回 null，表示取不到有效值。
        :type Interface: str
        """
        self._Interface = None

    @property
    def Interface(self):
        return self._Interface

    @Interface.setter
    def Interface(self, Interface):
        self._Interface = Interface


    def _deserialize(self, params):
        self._Interface = params.get("Interface")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        