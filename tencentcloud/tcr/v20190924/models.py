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


class AccessVpc(AbstractModel):
    """内网接入信息

    """

    def __init__(self):
        r"""
        :param _VpcId: Vpc的Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        :param _Status: 内网接入状态
        :type Status: str
        :param _AccessIp: 内网接入Ip
        :type AccessIp: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._AccessIp = None

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccessIp(self):
        return self._AccessIp

    @AccessIp.setter
    def AccessIp(self, AccessIp):
        self._AccessIp = AccessIp


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._AccessIp = params.get("AccessIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoDelStrategyInfo(AbstractModel):
    """自动删除策略信息

    """

    def __init__(self):
        r"""
        :param _Username: 用户名
        :type Username: str
        :param _RepoName: 仓库名
        :type RepoName: str
        :param _Type: 类型
        :type Type: str
        :param _Value: 策略值
        :type Value: int
        :param _Valid: Valid
        :type Valid: int
        :param _CreationTime: 创建时间
        :type CreationTime: str
        """
        self._Username = None
        self._RepoName = None
        self._Type = None
        self._Value = None
        self._Valid = None
        self._CreationTime = None

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Valid(self):
        return self._Valid

    @Valid.setter
    def Valid(self, Valid):
        self._Valid = Valid

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._RepoName = params.get("RepoName")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        self._Valid = params.get("Valid")
        self._CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoDelStrategyInfoResp(AbstractModel):
    """获取自动删除策略

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _StrategyInfo: 自动删除策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyInfo: list of AutoDelStrategyInfo
        """
        self._TotalCount = None
        self._StrategyInfo = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StrategyInfo(self):
        return self._StrategyInfo

    @StrategyInfo.setter
    def StrategyInfo(self, StrategyInfo):
        self._StrategyInfo = StrategyInfo


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("StrategyInfo") is not None:
            self._StrategyInfo = []
            for item in params.get("StrategyInfo"):
                obj = AutoDelStrategyInfo()
                obj._deserialize(item)
                self._StrategyInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteImagePersonalRequest(AbstractModel):
    """BatchDeleteImagePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Tags: Tag列表
        :type Tags: list of str
        """
        self._RepoName = None
        self._Tags = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteImagePersonalResponse(AbstractModel):
    """BatchDeleteImagePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class BatchDeleteRepositoryPersonalRequest(AbstractModel):
    """BatchDeleteRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoNames: 仓库名称数组
        :type RepoNames: list of str
        """
        self._RepoNames = None

    @property
    def RepoNames(self):
        return self._RepoNames

    @RepoNames.setter
    def RepoNames(self, RepoNames):
        self._RepoNames = RepoNames


    def _deserialize(self, params):
        self._RepoNames = params.get("RepoNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteRepositoryPersonalResponse(AbstractModel):
    """BatchDeleteRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CVEWhitelistItem(AbstractModel):
    """命名空间漏洞白名单列表

    """

    def __init__(self):
        r"""
        :param _CVEID: 漏洞白名单 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CVEID: str
        """
        self._CVEID = None

    @property
    def CVEID(self):
        return self._CVEID

    @CVEID.setter
    def CVEID(self, CVEID):
        self._CVEID = CVEID


    def _deserialize(self, params):
        self._CVEID = params.get("CVEID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceNameRequest(AbstractModel):
    """CheckInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryName: 待创建的实例名称
        :type RegistryName: str
        """
        self._RegistryName = None

    @property
    def RegistryName(self):
        return self._RegistryName

    @RegistryName.setter
    def RegistryName(self, RegistryName):
        self._RegistryName = RegistryName


    def _deserialize(self, params):
        self._RegistryName = params.get("RegistryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceNameResponse(AbstractModel):
    """CheckInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsValidated: 检查结果，true为合法，false为非法
        :type IsValidated: bool
        :param _DetailCode: 1: Illegal（名子非法）, 2:Reserved（名字保留）, 3:Existed（名字已存在）
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsValidated = None
        self._DetailCode = None
        self._RequestId = None

    @property
    def IsValidated(self):
        return self._IsValidated

    @IsValidated.setter
    def IsValidated(self, IsValidated):
        self._IsValidated = IsValidated

    @property
    def DetailCode(self):
        return self._DetailCode

    @DetailCode.setter
    def DetailCode(self, DetailCode):
        self._DetailCode = DetailCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsValidated = params.get("IsValidated")
        self._DetailCode = params.get("DetailCode")
        self._RequestId = params.get("RequestId")


class CheckInstanceRequest(AbstractModel):
    """CheckInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 待检测的实例Id
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceResponse(AbstractModel):
    """CheckInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsValidated: 检查结果，true为合法，false为非法
        :type IsValidated: bool
        :param _RegionId: 实例所在的RegionId
        :type RegionId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsValidated = None
        self._RegionId = None
        self._RequestId = None

    @property
    def IsValidated(self):
        return self._IsValidated

    @IsValidated.setter
    def IsValidated(self, IsValidated):
        self._IsValidated = IsValidated

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsValidated = params.get("IsValidated")
        self._RegionId = params.get("RegionId")
        self._RequestId = params.get("RequestId")


class CreateApplicationTriggerPersonalRequest(AbstractModel):
    """CreateApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 触发器关联的镜像仓库，library/test格式
        :type RepoName: str
        :param _TriggerName: 触发器名称
        :type TriggerName: str
        :param _InvokeMethod: 触发方式，"all"全部触发，"taglist"指定tag触发，"regex"正则触发
        :type InvokeMethod: str
        :param _ClusterId: 应用所在TKE集群ID
        :type ClusterId: str
        :param _Namespace: 应用所在TKE集群命名空间
        :type Namespace: str
        :param _WorkloadType: 应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。
        :type WorkloadType: str
        :param _WorkloadName: 应用所在TKE集群工作负载名称
        :type WorkloadName: str
        :param _ContainerName: 应用所在TKE集群工作负载下容器名称
        :type ContainerName: str
        :param _ClusterRegion: 应用所在TKE集群地域
        :type ClusterRegion: int
        :param _InvokeExpr: 触发方式对应的表达式
        :type InvokeExpr: str
        """
        self._RepoName = None
        self._TriggerName = None
        self._InvokeMethod = None
        self._ClusterId = None
        self._Namespace = None
        self._WorkloadType = None
        self._WorkloadName = None
        self._ContainerName = None
        self._ClusterRegion = None
        self._InvokeExpr = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def InvokeMethod(self):
        return self._InvokeMethod

    @InvokeMethod.setter
    def InvokeMethod(self, InvokeMethod):
        self._InvokeMethod = InvokeMethod

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def WorkloadType(self):
        return self._WorkloadType

    @WorkloadType.setter
    def WorkloadType(self, WorkloadType):
        self._WorkloadType = WorkloadType

    @property
    def WorkloadName(self):
        return self._WorkloadName

    @WorkloadName.setter
    def WorkloadName(self, WorkloadName):
        self._WorkloadName = WorkloadName

    @property
    def ContainerName(self):
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def ClusterRegion(self):
        return self._ClusterRegion

    @ClusterRegion.setter
    def ClusterRegion(self, ClusterRegion):
        self._ClusterRegion = ClusterRegion

    @property
    def InvokeExpr(self):
        return self._InvokeExpr

    @InvokeExpr.setter
    def InvokeExpr(self, InvokeExpr):
        self._InvokeExpr = InvokeExpr


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._TriggerName = params.get("TriggerName")
        self._InvokeMethod = params.get("InvokeMethod")
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._WorkloadType = params.get("WorkloadType")
        self._WorkloadName = params.get("WorkloadName")
        self._ContainerName = params.get("ContainerName")
        self._ClusterRegion = params.get("ClusterRegion")
        self._InvokeExpr = params.get("InvokeExpr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationTriggerPersonalResponse(AbstractModel):
    """CreateApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateImageAccelerationServiceRequest(AbstractModel):
    """CreateImageAccelerationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _VpcId: 创建CFS的归属的VPCID
        :type VpcId: str
        :param _SubnetId: 创建CFS的归属的子网ID
        :type SubnetId: str
        :param _StorageType: 创建CFS的存储类型，其中 SD 为标准型存储， HP为性能存储。
        :type StorageType: str
        :param _PGroupId: 权限组 ID
        :type PGroupId: str
        :param _Zone: 可用区名称，例如ap-beijing-1，请参考 概览 文档中的地域与可用区列表
        :type Zone: str
        :param _TagSpecification: 云标签描述
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        """
        self._RegistryId = None
        self._VpcId = None
        self._SubnetId = None
        self._StorageType = None
        self._PGroupId = None
        self._Zone = None
        self._TagSpecification = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

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
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._StorageType = params.get("StorageType")
        self._PGroupId = params.get("PGroupId")
        self._Zone = params.get("Zone")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageAccelerationServiceResponse(AbstractModel):
    """CreateImageAccelerationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class CreateImmutableTagRulesRequest(AbstractModel):
    """CreateImmutableTagRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 Id
        :type RegistryId: str
        :param _NamespaceName: 命名空间
        :type NamespaceName: str
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._Rule = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        if params.get("Rule") is not None:
            self._Rule = ImmutableTagRule()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImmutableTagRulesResponse(AbstractModel):
    """CreateImmutableTagRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateInstanceCustomizedDomainRequest(AbstractModel):
    """CreateInstanceCustomizedDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _DomainName: 自定义域名
        :type DomainName: str
        :param _CertificateId: 证书ID
        :type CertificateId: str
        """
        self._RegistryId = None
        self._DomainName = None
        self._CertificateId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._DomainName = params.get("DomainName")
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceCustomizedDomainResponse(AbstractModel):
    """CreateInstanceCustomizedDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryName: 企业版实例名称
        :type RegistryName: str
        :param _RegistryType: 企业版实例类型（basic 基础版；standard 标准版；premium 高级版）
        :type RegistryType: str
        :param _TagSpecification: 云标签描述
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param _RegistryChargeType: 实例计费类型，0表示按量计费，1表示预付费，默认为按量计费
        :type RegistryChargeType: int
        :param _RegistryChargePrepaid: 预付费自动续费标识和购买时长
        :type RegistryChargePrepaid: :class:`tencentcloud.tcr.v20190924.models.RegistryChargePrepaid`
        :param _SyncTag: 是否同步TCR云标签至生成的COS Bucket
        :type SyncTag: bool
        :param _EnableCosMAZ: 是否开启Cos桶多AZ特性
        :type EnableCosMAZ: bool
        :param _DeletionProtection: 是否开启实例删除保护
        :type DeletionProtection: bool
        """
        self._RegistryName = None
        self._RegistryType = None
        self._TagSpecification = None
        self._RegistryChargeType = None
        self._RegistryChargePrepaid = None
        self._SyncTag = None
        self._EnableCosMAZ = None
        self._DeletionProtection = None

    @property
    def RegistryName(self):
        return self._RegistryName

    @RegistryName.setter
    def RegistryName(self, RegistryName):
        self._RegistryName = RegistryName

    @property
    def RegistryType(self):
        return self._RegistryType

    @RegistryType.setter
    def RegistryType(self, RegistryType):
        self._RegistryType = RegistryType

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def RegistryChargeType(self):
        return self._RegistryChargeType

    @RegistryChargeType.setter
    def RegistryChargeType(self, RegistryChargeType):
        self._RegistryChargeType = RegistryChargeType

    @property
    def RegistryChargePrepaid(self):
        return self._RegistryChargePrepaid

    @RegistryChargePrepaid.setter
    def RegistryChargePrepaid(self, RegistryChargePrepaid):
        self._RegistryChargePrepaid = RegistryChargePrepaid

    @property
    def SyncTag(self):
        return self._SyncTag

    @SyncTag.setter
    def SyncTag(self, SyncTag):
        self._SyncTag = SyncTag

    @property
    def EnableCosMAZ(self):
        return self._EnableCosMAZ

    @EnableCosMAZ.setter
    def EnableCosMAZ(self, EnableCosMAZ):
        self._EnableCosMAZ = EnableCosMAZ

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._RegistryName = params.get("RegistryName")
        self._RegistryType = params.get("RegistryType")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        self._RegistryChargeType = params.get("RegistryChargeType")
        if params.get("RegistryChargePrepaid") is not None:
            self._RegistryChargePrepaid = RegistryChargePrepaid()
            self._RegistryChargePrepaid._deserialize(params.get("RegistryChargePrepaid"))
        self._SyncTag = params.get("SyncTag")
        self._EnableCosMAZ = params.get("EnableCosMAZ")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 企业版实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class CreateInstanceTokenRequest(AbstractModel):
    """CreateInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _TokenType: 访问凭证类型，longterm 为长期访问凭证，temp 为临时访问凭证，默认是临时访问凭证，有效期1小时
        :type TokenType: str
        :param _Desc: 长期访问凭证描述信息
        :type Desc: str
        """
        self._RegistryId = None
        self._TokenType = None
        self._Desc = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def TokenType(self):
        return self._TokenType

    @TokenType.setter
    def TokenType(self, TokenType):
        self._TokenType = TokenType

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._TokenType = params.get("TokenType")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceTokenResponse(AbstractModel):
    """CreateInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Username: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param _Token: 访问凭证
        :type Token: str
        :param _ExpTime: 访问凭证过期时间戳，是一个时间戳数字，无单位
        :type ExpTime: int
        :param _TokenId: 长期凭证的TokenId，短期凭证没有TokenId
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Username = None
        self._Token = None
        self._ExpTime = None
        self._TokenId = None
        self._RequestId = None

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpTime(self):
        return self._ExpTime

    @ExpTime.setter
    def ExpTime(self, ExpTime):
        self._ExpTime = ExpTime

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._Token = params.get("Token")
        self._ExpTime = params.get("ExpTime")
        self._TokenId = params.get("TokenId")
        self._RequestId = params.get("RequestId")


class CreateInternalEndpointDnsRequest(AbstractModel):
    """CreateInternalEndpointDns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tcr实例id
        :type InstanceId: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _EniLBIp: tcr内网访问链路ip
        :type EniLBIp: str
        :param _UsePublicDomain: true：为默认域名，公网域名一致
false: 使用vpc域名
默认为vpc域名
        :type UsePublicDomain: bool
        :param _RegionName: 解析地域，需要保证和vpc处于同一地域，如果不填则默认为主实例地域
        :type RegionName: str
        :param _RegionId: 请求的地域ID，用于实例复制地域
        :type RegionId: int
        """
        self._InstanceId = None
        self._VpcId = None
        self._EniLBIp = None
        self._UsePublicDomain = None
        self._RegionName = None
        self._RegionId = None

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
    def EniLBIp(self):
        return self._EniLBIp

    @EniLBIp.setter
    def EniLBIp(self, EniLBIp):
        self._EniLBIp = EniLBIp

    @property
    def UsePublicDomain(self):
        return self._UsePublicDomain

    @UsePublicDomain.setter
    def UsePublicDomain(self, UsePublicDomain):
        self._UsePublicDomain = UsePublicDomain

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._EniLBIp = params.get("EniLBIp")
        self._UsePublicDomain = params.get("UsePublicDomain")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInternalEndpointDnsResponse(AbstractModel):
    """CreateInternalEndpointDns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateMultipleSecurityPolicyRequest(AbstractModel):
    """CreateMultipleSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _SecurityGroupPolicySet: 安全组策略
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self._RegistryId = None
        self._SecurityGroupPolicySet = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def SecurityGroupPolicySet(self):
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self._SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultipleSecurityPolicyResponse(AbstractModel):
    """CreateMultipleSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class CreateNamespacePersonalRequest(AbstractModel):
    """CreateNamespacePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名称
        :type Namespace: str
        """
        self._Namespace = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespacePersonalResponse(AbstractModel):
    """CreateNamespacePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间的名称（长度2-30个字符，只能包含小写字母、数字及分隔符("."、"_"、"-")，且不能以分隔符开头、结尾或连续）
        :type NamespaceName: str
        :param _IsPublic: 是否公开，true为公开，fale为私有
        :type IsPublic: bool
        :param _TagSpecification: 云标签描述
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param _IsAutoScan: 自动扫描级别，true为自动，false为手动
        :type IsAutoScan: bool
        :param _IsPreventVUL: 安全阻断级别，true为自动，false为手动
        :type IsPreventVUL: bool
        :param _Severity: 阻断漏洞等级，目前仅支持low、medium、high
        :type Severity: str
        :param _CVEWhitelistItems: 漏洞白名单列表
        :type CVEWhitelistItems: list of CVEWhitelistItem
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._IsPublic = None
        self._TagSpecification = None
        self._IsAutoScan = None
        self._IsPreventVUL = None
        self._Severity = None
        self._CVEWhitelistItems = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def IsAutoScan(self):
        return self._IsAutoScan

    @IsAutoScan.setter
    def IsAutoScan(self, IsAutoScan):
        self._IsAutoScan = IsAutoScan

    @property
    def IsPreventVUL(self):
        return self._IsPreventVUL

    @IsPreventVUL.setter
    def IsPreventVUL(self, IsPreventVUL):
        self._IsPreventVUL = IsPreventVUL

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def CVEWhitelistItems(self):
        return self._CVEWhitelistItems

    @CVEWhitelistItems.setter
    def CVEWhitelistItems(self, CVEWhitelistItems):
        self._CVEWhitelistItems = CVEWhitelistItems


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._IsPublic = params.get("IsPublic")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        self._IsAutoScan = params.get("IsAutoScan")
        self._IsPreventVUL = params.get("IsPreventVUL")
        self._Severity = params.get("Severity")
        if params.get("CVEWhitelistItems") is not None:
            self._CVEWhitelistItems = []
            for item in params.get("CVEWhitelistItems"):
                obj = CVEWhitelistItem()
                obj._deserialize(item)
                self._CVEWhitelistItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateReplicationInstanceRequest(AbstractModel):
    """CreateReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _ReplicationRegionId: 复制实例地域ID
        :type ReplicationRegionId: int
        :param _ReplicationRegionName: 复制实例地域名称
        :type ReplicationRegionName: str
        :param _SyncTag: 是否同步TCR云标签至生成的COS Bucket
        :type SyncTag: bool
        """
        self._RegistryId = None
        self._ReplicationRegionId = None
        self._ReplicationRegionName = None
        self._SyncTag = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId

    @property
    def ReplicationRegionName(self):
        return self._ReplicationRegionName

    @ReplicationRegionName.setter
    def ReplicationRegionName(self, ReplicationRegionName):
        self._ReplicationRegionName = ReplicationRegionName

    @property
    def SyncTag(self):
        return self._SyncTag

    @SyncTag.setter
    def SyncTag(self, SyncTag):
        self._SyncTag = SyncTag


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        self._ReplicationRegionName = params.get("ReplicationRegionName")
        self._SyncTag = params.get("SyncTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplicationInstanceResponse(AbstractModel):
    """CreateReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReplicationRegistryId: 企业版复制实例Id
        :type ReplicationRegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReplicationRegistryId = None
        self._RequestId = None

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._RequestId = params.get("RequestId")


class CreateRepositoryPersonalRequest(AbstractModel):
    """CreateRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Public: 是否公共,1:公共,0:私有
        :type Public: int
        :param _Description: 仓库描述
        :type Description: str
        """
        self._RepoName = None
        self._Public = None
        self._Description = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Public = params.get("Public")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRepositoryPersonalResponse(AbstractModel):
    """CreateRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _RepositoryName: 仓库名称
        :type RepositoryName: str
        :param _BriefDescription: 仓库简短描述
        :type BriefDescription: str
        :param _Description: 仓库详细描述
        :type Description: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._BriefDescription = None
        self._Description = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def BriefDescription(self):
        return self._BriefDescription

    @BriefDescription.setter
    def BriefDescription(self, BriefDescription):
        self._BriefDescription = BriefDescription

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._BriefDescription = params.get("BriefDescription")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRepositoryResponse(AbstractModel):
    """CreateRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _CidrBlock: 192.168.0.0/24
        :type CidrBlock: str
        :param _Description: 备注
        :type Description: str
        """
        self._RegistryId = None
        self._CidrBlock = None
        self._Description = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._CidrBlock = params.get("CidrBlock")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    """CreateSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class CreateServiceAccountRequest(AbstractModel):
    """CreateServiceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Name: 服务级账号名
        :type Name: str
        :param _Permissions: 策略列表
        :type Permissions: list of Permission
        :param _Description: 服务级账号描述
        :type Description: str
        :param _Duration: 有效期(单位：天)，从当前时间开始计算，优先级高于ExpiresAt
        :type Duration: int
        :param _ExpiresAt: 过期时间（时间戳，单位:毫秒）
        :type ExpiresAt: int
        :param _Disable: 是否禁用服务级账号
        :type Disable: bool
        """
        self._RegistryId = None
        self._Name = None
        self._Permissions = None
        self._Description = None
        self._Duration = None
        self._ExpiresAt = None
        self._Disable = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        self._Description = params.get("Description")
        self._Duration = params.get("Duration")
        self._ExpiresAt = params.get("ExpiresAt")
        self._Disable = params.get("Disable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceAccountResponse(AbstractModel):
    """CreateServiceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 服务级账号名（会自动加上前缀tcr$）
        :type Name: str
        :param _Password: 服务级账号密码，仅展示一次，请注意留存
        :type Password: str
        :param _ExpiresAt: 服务级账号失效时间（时间戳）
        :type ExpiresAt: int
        :param _CreateTime: 服务级账号创建时间
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Password = None
        self._ExpiresAt = None
        self._CreateTime = None
        self._RequestId = None

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
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._ExpiresAt = params.get("ExpiresAt")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class CreateSignaturePolicyRequest(AbstractModel):
    """CreateSignaturePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 Id
        :type RegistryId: str
        :param _Name: 策略名称
        :type Name: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _KmsId: KMS 密钥
        :type KmsId: str
        :param _KmsRegion: KMS 密钥所属地域
        :type KmsRegion: str
        :param _Domain: 用户自定义域名，为空时使用 TCR 实例默认域名生成签名
        :type Domain: str
        :param _Disabled: 禁用加签策略，默认为 false
        :type Disabled: bool
        """
        self._RegistryId = None
        self._Name = None
        self._NamespaceName = None
        self._KmsId = None
        self._KmsRegion = None
        self._Domain = None
        self._Disabled = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def KmsId(self):
        return self._KmsId

    @KmsId.setter
    def KmsId(self, KmsId):
        self._KmsId = KmsId

    @property
    def KmsRegion(self):
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._NamespaceName = params.get("NamespaceName")
        self._KmsId = params.get("KmsId")
        self._KmsRegion = params.get("KmsRegion")
        self._Domain = params.get("Domain")
        self._Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignaturePolicyResponse(AbstractModel):
    """CreateSignaturePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateSignatureRequest(AbstractModel):
    """CreateSignature请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _RepositoryName: 仓库名称
        :type RepositoryName: str
        :param _ImageVersion: Tag名称
        :type ImageVersion: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._ImageVersion = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._ImageVersion = params.get("ImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignatureResponse(AbstractModel):
    """CreateSignature返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateTagRetentionExecutionRequest(AbstractModel):
    """CreateTagRetentionExecution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _RetentionId: 版本保留规则Id
        :type RetentionId: int
        :param _DryRun: 是否模拟执行，默认值为false，即非模拟执行
        :type DryRun: bool
        """
        self._RegistryId = None
        self._RetentionId = None
        self._DryRun = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RetentionId = params.get("RetentionId")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagRetentionExecutionResponse(AbstractModel):
    """CreateTagRetentionExecution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateTagRetentionRuleRequest(AbstractModel):
    """CreateTagRetentionRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _NamespaceId: 命名空间的Id
        :type NamespaceId: int
        :param _RetentionRule: 保留策略
        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`
        :param _CronSetting: 执行周期，当前只能选择： manual;daily;weekly;monthly
        :type CronSetting: str
        :param _Disabled: 是否禁用规则，默认值为false
        :type Disabled: bool
        """
        self._RegistryId = None
        self._NamespaceId = None
        self._RetentionRule = None
        self._CronSetting = None
        self._Disabled = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def RetentionRule(self):
        return self._RetentionRule

    @RetentionRule.setter
    def RetentionRule(self, RetentionRule):
        self._RetentionRule = RetentionRule

    @property
    def CronSetting(self):
        return self._CronSetting

    @CronSetting.setter
    def CronSetting(self, CronSetting):
        self._CronSetting = CronSetting

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceId = params.get("NamespaceId")
        if params.get("RetentionRule") is not None:
            self._RetentionRule = RetentionRule()
            self._RetentionRule._deserialize(params.get("RetentionRule"))
        self._CronSetting = params.get("CronSetting")
        self._Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagRetentionRuleResponse(AbstractModel):
    """CreateTagRetentionRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateUserPersonalRequest(AbstractModel):
    """CreateUserPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Password: 用户密码，密码必须为8到16位
        :type Password: str
        """
        self._Password = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserPersonalResponse(AbstractModel):
    """CreateUserPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateWebhookTriggerRequest(AbstractModel):
    """CreateWebhookTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 Id
        :type RegistryId: str
        :param _Trigger: 触发器参数
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._RegistryId = None
        self._Trigger = None
        self._Namespace = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self._Trigger = WebhookTrigger()
            self._Trigger._deserialize(params.get("Trigger"))
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWebhookTriggerResponse(AbstractModel):
    """CreateWebhookTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Trigger: 新建的触发器
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Trigger = None
        self._RequestId = None

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Trigger") is not None:
            self._Trigger = WebhookTrigger()
            self._Trigger._deserialize(params.get("Trigger"))
        self._RequestId = params.get("RequestId")


class CustomizedDomainInfo(AbstractModel):
    """自定义域名信息

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _DomainName: 域名名称
        :type DomainName: str
        :param _Status: 域名创建状态（SUCCESS, FAILURE, CREATING, DELETING）
        :type Status: str
        """
        self._RegistryId = None
        self._CertId = None
        self._DomainName = None
        self._Status = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._CertId = params.get("CertId")
        self._DomainName = params.get("DomainName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationTriggerPersonalRequest(AbstractModel):
    """DeleteApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TriggerName: 触发器名称
        :type TriggerName: str
        """
        self._TriggerName = None

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName


    def _deserialize(self, params):
        self._TriggerName = params.get("TriggerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationTriggerPersonalResponse(AbstractModel):
    """DeleteApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteImageAccelerateServiceRequest(AbstractModel):
    """DeleteImageAccelerateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageAccelerateServiceResponse(AbstractModel):
    """DeleteImageAccelerateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteImageLifecycleGlobalPersonalRequest(AbstractModel):
    """DeleteImageLifecycleGlobalPersonal请求参数结构体

    """


class DeleteImageLifecycleGlobalPersonalResponse(AbstractModel):
    """DeleteImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteImagePersonalRequest(AbstractModel):
    """DeleteImagePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Tag: Tag名
        :type Tag: str
        """
        self._RepoName = None
        self._Tag = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagePersonalResponse(AbstractModel):
    """DeleteImagePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteImageRequest(AbstractModel):
    """DeleteImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param _ImageVersion: 镜像版本
        :type ImageVersion: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        """
        self._RegistryId = None
        self._RepositoryName = None
        self._ImageVersion = None
        self._NamespaceName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RepositoryName = params.get("RepositoryName")
        self._ImageVersion = params.get("ImageVersion")
        self._NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageResponse(AbstractModel):
    """DeleteImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteImmutableTagRulesRequest(AbstractModel):
    """DeleteImmutableTagRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 Id
        :type RegistryId: str
        :param _NamespaceName: 命名空间
        :type NamespaceName: str
        :param _RuleId: 规则 Id
        :type RuleId: int
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RuleId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImmutableTagRulesResponse(AbstractModel):
    """DeleteImmutableTagRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteInstanceCustomizedDomainRequest(AbstractModel):
    """DeleteInstanceCustomizedDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _DomainName: 自定义域名
        :type DomainName: str
        :param _CertificateId: 证书ID
        :type CertificateId: str
        """
        self._RegistryId = None
        self._DomainName = None
        self._CertificateId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._DomainName = params.get("DomainName")
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceCustomizedDomainResponse(AbstractModel):
    """DeleteInstanceCustomizedDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例id
        :type RegistryId: str
        :param _DeleteBucket: 是否删除存储桶，默认为false
        :type DeleteBucket: bool
        :param _DryRun: 是否dryRun模式，缺省值：false
        :type DryRun: bool
        """
        self._RegistryId = None
        self._DeleteBucket = None
        self._DryRun = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def DeleteBucket(self):
        return self._DeleteBucket

    @DeleteBucket.setter
    def DeleteBucket(self, DeleteBucket):
        self._DeleteBucket = DeleteBucket

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._DeleteBucket = params.get("DeleteBucket")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteInstanceTokenRequest(AbstractModel):
    """DeleteInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 ID
        :type RegistryId: str
        :param _TokenId: 访问凭证 ID
        :type TokenId: str
        """
        self._RegistryId = None
        self._TokenId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._TokenId = params.get("TokenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceTokenResponse(AbstractModel):
    """DeleteInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteInternalEndpointDnsRequest(AbstractModel):
    """DeleteInternalEndpointDns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tcr实例id
        :type InstanceId: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _EniLBIp: tcr内网访问链路ip
        :type EniLBIp: str
        :param _UsePublicDomain: true：使用默认域名
false:  使用带有vpc的域名
        :type UsePublicDomain: bool
        :param _RegionName: 解析地域，需要保证和vpc处于同一地域，如果不填则默认为主实例地域
        :type RegionName: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._EniLBIp = None
        self._UsePublicDomain = None
        self._RegionName = None

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
    def EniLBIp(self):
        return self._EniLBIp

    @EniLBIp.setter
    def EniLBIp(self, EniLBIp):
        self._EniLBIp = EniLBIp

    @property
    def UsePublicDomain(self):
        return self._UsePublicDomain

    @UsePublicDomain.setter
    def UsePublicDomain(self, UsePublicDomain):
        self._UsePublicDomain = UsePublicDomain

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._EniLBIp = params.get("EniLBIp")
        self._UsePublicDomain = params.get("UsePublicDomain")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInternalEndpointDnsResponse(AbstractModel):
    """DeleteInternalEndpointDns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteMultipleSecurityPolicyRequest(AbstractModel):
    """DeleteMultipleSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _SecurityGroupPolicySet: 安全组策略
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self._RegistryId = None
        self._SecurityGroupPolicySet = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def SecurityGroupPolicySet(self):
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self._SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMultipleSecurityPolicyResponse(AbstractModel):
    """DeleteMultipleSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class DeleteNamespacePersonalRequest(AbstractModel):
    """DeleteNamespacePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名称
        :type Namespace: str
        """
        self._Namespace = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespacePersonalResponse(AbstractModel):
    """DeleteNamespacePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间的名称
        :type NamespaceName: str
        """
        self._RegistryId = None
        self._NamespaceName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteReplicationInstanceRequest(AbstractModel):
    """DeleteReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例id
        :type RegistryId: str
        :param _ReplicationRegistryId: 复制实例ID
        :type ReplicationRegistryId: str
        :param _ReplicationRegionId: 复制实例地域Id
        :type ReplicationRegionId: int
        """
        self._RegistryId = None
        self._ReplicationRegistryId = None
        self._ReplicationRegionId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReplicationInstanceResponse(AbstractModel):
    """DeleteReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteRepositoryPersonalRequest(AbstractModel):
    """DeleteRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        """
        self._RepoName = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryPersonalResponse(AbstractModel):
    """DeleteRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _NamespaceName: 命名空间的名称
        :type NamespaceName: str
        :param _RepositoryName: 镜像仓库的名称
        :type RepositoryName: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryResponse(AbstractModel):
    """DeleteRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteRepositoryTagsRequest(AbstractModel):
    """DeleteRepositoryTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _RepositoryName: 仓库名称
        :type RepositoryName: str
        :param _Tags: Tag列表，单次请求Tag数量最大为20
        :type Tags: list of str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._Tags = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryTagsResponse(AbstractModel):
    """DeleteRepositoryTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _PolicyIndex: 白名单Id
        :type PolicyIndex: int
        :param _PolicyVersion: 白名单版本
        :type PolicyVersion: str
        :param _CidrBlock: 网段或IP(互斥)
        :type CidrBlock: str
        """
        self._RegistryId = None
        self._PolicyIndex = None
        self._PolicyVersion = None
        self._CidrBlock = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def PolicyIndex(self):
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def PolicyVersion(self):
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._PolicyIndex = params.get("PolicyIndex")
        self._PolicyVersion = params.get("PolicyVersion")
        self._CidrBlock = params.get("CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    """DeleteSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class DeleteServiceAccountRequest(AbstractModel):
    """DeleteServiceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id	
        :type RegistryId: str
        :param _Name: 服务级账号名
        :type Name: str
        """
        self._RegistryId = None
        self._Name = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceAccountResponse(AbstractModel):
    """DeleteServiceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteSignaturePolicyRequest(AbstractModel):
    """DeleteSignaturePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间的名称
        :type NamespaceName: str
        """
        self._RegistryId = None
        self._NamespaceName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSignaturePolicyResponse(AbstractModel):
    """DeleteSignaturePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteTagRetentionRuleRequest(AbstractModel):
    """DeleteTagRetentionRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _RetentionId: 版本保留规则的Id
        :type RetentionId: int
        """
        self._RegistryId = None
        self._RetentionId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RetentionId = params.get("RetentionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagRetentionRuleResponse(AbstractModel):
    """DeleteTagRetentionRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteWebhookTriggerRequest(AbstractModel):
    """DeleteWebhookTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Id: 触发器 Id
        :type Id: int
        """
        self._RegistryId = None
        self._Namespace = None
        self._Id = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Namespace = params.get("Namespace")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWebhookTriggerResponse(AbstractModel):
    """DeleteWebhookTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeApplicationTriggerLogPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerLogPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param _Order: 升序或降序
        :type Order: str
        :param _OrderBy: 按某列排序
        :type OrderBy: str
        """
        self._RepoName = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderBy = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationTriggerLogPersonalResp(AbstractModel):
    """查询应用更新触发器触发日志返回值

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回总数
        :type TotalCount: int
        :param _LogInfo: 触发日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogInfo: list of TriggerLogResp
        """
        self._TotalCount = None
        self._LogInfo = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogInfo(self):
        return self._LogInfo

    @LogInfo.setter
    def LogInfo(self, LogInfo):
        self._LogInfo = LogInfo


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LogInfo") is not None:
            self._LogInfo = []
            for item in params.get("LogInfo"):
                obj = TriggerLogResp()
                obj._deserialize(item)
                self._LogInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationTriggerLogPersonalResponse(AbstractModel):
    """DescribeApplicationTriggerLogPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 触发日志返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeApplicationTriggerLogPersonalResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationTriggerPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _TriggerName: 触发器名称
        :type TriggerName: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        """
        self._RepoName = None
        self._TriggerName = None
        self._Offset = None
        self._Limit = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

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
        self._RepoName = params.get("RepoName")
        self._TriggerName = params.get("TriggerName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationTriggerPersonalResp(AbstractModel):
    """拉取触发器列表返回值

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回条目总数
        :type TotalCount: int
        :param _TriggerInfo: 触发器列表
        :type TriggerInfo: list of TriggerResp
        """
        self._TotalCount = None
        self._TriggerInfo = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TriggerInfo(self):
        return self._TriggerInfo

    @TriggerInfo.setter
    def TriggerInfo(self, TriggerInfo):
        self._TriggerInfo = TriggerInfo


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TriggerInfo") is not None:
            self._TriggerInfo = []
            for item in params.get("TriggerInfo"):
                obj = TriggerResp()
                obj._deserialize(item)
                self._TriggerInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationTriggerPersonalResponse(AbstractModel):
    """DescribeApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 触发器列表返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeApplicationTriggerPersonalResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeChartDownloadInfoRequest(AbstractModel):
    """DescribeChartDownloadInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间
        :type NamespaceName: str
        :param _ChartName: Chart包的名称
        :type ChartName: str
        :param _ChartVersion: Chart包的版本
        :type ChartVersion: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._ChartName = None
        self._ChartVersion = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def ChartName(self):
        return self._ChartName

    @ChartName.setter
    def ChartName(self, ChartName):
        self._ChartName = ChartName

    @property
    def ChartVersion(self):
        return self._ChartVersion

    @ChartVersion.setter
    def ChartVersion(self, ChartVersion):
        self._ChartVersion = ChartVersion


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._ChartName = params.get("ChartName")
        self._ChartVersion = params.get("ChartVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChartDownloadInfoResponse(AbstractModel):
    """DescribeChartDownloadInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PreSignedDownloadURL: 用于下载的url的预签名地址
        :type PreSignedDownloadURL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PreSignedDownloadURL = None
        self._RequestId = None

    @property
    def PreSignedDownloadURL(self):
        return self._PreSignedDownloadURL

    @PreSignedDownloadURL.setter
    def PreSignedDownloadURL(self, PreSignedDownloadURL):
        self._PreSignedDownloadURL = PreSignedDownloadURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PreSignedDownloadURL = params.get("PreSignedDownloadURL")
        self._RequestId = params.get("RequestId")


class DescribeExternalEndpointStatusRequest(AbstractModel):
    """DescribeExternalEndpointStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExternalEndpointStatusResponse(AbstractModel):
    """DescribeExternalEndpointStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 开启公网访问状态，开启中（Opening）、已开启（Opened）、关闭（Closed）
        :type Status: str
        :param _Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Reason = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._RequestId = params.get("RequestId")


class DescribeFavorRepositoryPersonalRequest(AbstractModel):
    """DescribeFavorRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Limit: 分页Limit
        :type Limit: int
        :param _Offset: Offset用于分页
        :type Offset: int
        """
        self._RepoName = None
        self._Limit = None
        self._Offset = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

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
        self._RepoName = params.get("RepoName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFavorRepositoryPersonalResponse(AbstractModel):
    """DescribeFavorRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 个人收藏仓库列表返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.FavorResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = FavorResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeGCJobsRequest(AbstractModel):
    """DescribeGCJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 Id
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGCJobsResponse(AbstractModel):
    """DescribeGCJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Jobs: GC Job 列表
        :type Jobs: list of GCJobInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Jobs = None
        self._RequestId = None

    @property
    def Jobs(self):
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = GCJobInfo()
                obj._deserialize(item)
                self._Jobs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImageAccelerateServiceRequest(AbstractModel):
    """DescribeImageAccelerateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageAccelerateServiceResponse(AbstractModel):
    """DescribeImageAccelerateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 镜像加速状态
        :type Status: str
        :param _CFSVIP: CFS的VIP
        :type CFSVIP: str
        :param _IsEnable: 是否开通
        :type IsEnable: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._CFSVIP = None
        self._IsEnable = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CFSVIP(self):
        return self._CFSVIP

    @CFSVIP.setter
    def CFSVIP(self, CFSVIP):
        self._CFSVIP = CFSVIP

    @property
    def IsEnable(self):
        return self._IsEnable

    @IsEnable.setter
    def IsEnable(self, IsEnable):
        self._IsEnable = IsEnable

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CFSVIP = params.get("CFSVIP")
        self._IsEnable = params.get("IsEnable")
        self._RequestId = params.get("RequestId")


class DescribeImageFilterPersonalRequest(AbstractModel):
    """DescribeImageFilterPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Tag: Tag名
        :type Tag: str
        """
        self._RepoName = None
        self._Tag = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageFilterPersonalResponse(AbstractModel):
    """DescribeImageFilterPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回tag镜像内容相同的tag列表
        :type Data: :class:`tencentcloud.tcr.v20190924.models.SameImagesResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SameImagesResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeImageLifecycleGlobalPersonalRequest(AbstractModel):
    """DescribeImageLifecycleGlobalPersonal请求参数结构体

    """


class DescribeImageLifecycleGlobalPersonalResponse(AbstractModel):
    """DescribeImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 全局自动删除策略信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AutoDelStrategyInfoResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeImageLifecyclePersonalRequest(AbstractModel):
    """DescribeImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        """
        self._RepoName = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageLifecyclePersonalResponse(AbstractModel):
    """DescribeImageLifecyclePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 自动删除策略信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AutoDelStrategyInfoResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeImageManifestsRequest(AbstractModel):
    """DescribeImageManifests请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param _ImageVersion: 镜像版本
        :type ImageVersion: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._ImageVersion = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._ImageVersion = params.get("ImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageManifestsResponse(AbstractModel):
    """DescribeImageManifests返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Manifest: 镜像的Manifest信息
        :type Manifest: str
        :param _Config: 镜像的配置信息
        :type Config: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Manifest = None
        self._Config = None
        self._RequestId = None

    @property
    def Manifest(self):
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Manifest = params.get("Manifest")
        self._Config = params.get("Config")
        self._RequestId = params.get("RequestId")


class DescribeImagePersonalRequest(AbstractModel):
    """DescribeImagePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param _Tag: tag名称，可根据输入搜索
        :type Tag: str
        """
        self._RepoName = None
        self._Offset = None
        self._Limit = None
        self._Tag = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

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
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagePersonalResponse(AbstractModel):
    """DescribeImagePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 镜像tag信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.TagInfoResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TagInfoResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param _ImageVersion: 指定镜像版本进行查找，当前为模糊搜索
        :type ImageVersion: str
        :param _Limit: 每页个数，用于分页，默认20
        :type Limit: int
        :param _Offset: 页数，默认值为1
        :type Offset: int
        :param _Digest: 指定镜像 Digest 进行查找
        :type Digest: str
        :param _ExactMatch: 指定是否为精准匹配，true为精准匹配，不填为模糊匹配
        :type ExactMatch: bool
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._ImageVersion = None
        self._Limit = None
        self._Offset = None
        self._Digest = None
        self._ExactMatch = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

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
    def Digest(self):
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._ImageVersion = params.get("ImageVersion")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Digest = params.get("Digest")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageInfoList: 容器镜像信息列表
        :type ImageInfoList: list of TcrImageInfo
        :param _TotalCount: 容器镜像总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ImageInfoList(self):
        return self._ImageInfoList

    @ImageInfoList.setter
    def ImageInfoList(self, ImageInfoList):
        self._ImageInfoList = ImageInfoList

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
        if params.get("ImageInfoList") is not None:
            self._ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = TcrImageInfo()
                obj._deserialize(item)
                self._ImageInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeImmutableTagRulesRequest(AbstractModel):
    """DescribeImmutableTagRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 Id
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImmutableTagRulesResponse(AbstractModel):
    """DescribeImmutableTagRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of ImmutableTagRule
        :param _EmptyNs: 未创建规则的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type EmptyNs: list of str
        :param _Total: 规则总量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._EmptyNs = None
        self._Total = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def EmptyNs(self):
        return self._EmptyNs

    @EmptyNs.setter
    def EmptyNs(self, EmptyNs):
        self._EmptyNs = EmptyNs

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ImmutableTagRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._EmptyNs = params.get("EmptyNs")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeInstanceAllNamespacesRequest(AbstractModel):
    """DescribeInstanceAllNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页个数
        :type Limit: int
        :param _Offset: 起始偏移位置
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

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
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAllNamespacesResponse(AbstractModel):
    """DescribeInstanceAllNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeInstanceCustomizedDomainRequest(AbstractModel):
    """DescribeInstanceCustomizedDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _Limit: 分页Limit
        :type Limit: int
        :param _Offset: 分页Offset
        :type Offset: int
        """
        self._RegistryId = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

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
        self._RegistryId = params.get("RegistryId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceCustomizedDomainResponse(AbstractModel):
    """DescribeInstanceCustomizedDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInfoList: 域名信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainInfoList: list of CustomizedDomainInfo
        :param _TotalCount: 总个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainInfoList(self):
        return self._DomainInfoList

    @DomainInfoList.setter
    def DomainInfoList(self, DomainInfoList):
        self._DomainInfoList = DomainInfoList

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
        if params.get("DomainInfoList") is not None:
            self._DomainInfoList = []
            for item in params.get("DomainInfoList"):
                obj = CustomizedDomainInfo()
                obj._deserialize(item)
                self._DomainInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstanceStatusRequest(AbstractModel):
    """DescribeInstanceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryIds: 实例ID的数组
        :type RegistryIds: list of str
        """
        self._RegistryIds = None

    @property
    def RegistryIds(self):
        return self._RegistryIds

    @RegistryIds.setter
    def RegistryIds(self, RegistryIds):
        self._RegistryIds = RegistryIds


    def _deserialize(self, params):
        self._RegistryIds = params.get("RegistryIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceStatusResponse(AbstractModel):
    """DescribeInstanceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryStatusSet: 实例的状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryStatusSet: list of RegistryStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryStatusSet = None
        self._RequestId = None

    @property
    def RegistryStatusSet(self):
        return self._RegistryStatusSet

    @RegistryStatusSet.setter
    def RegistryStatusSet(self, RegistryStatusSet):
        self._RegistryStatusSet = RegistryStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegistryStatusSet") is not None:
            self._RegistryStatusSet = []
            for item in params.get("RegistryStatusSet"):
                obj = RegistryStatus()
                obj._deserialize(item)
                self._RegistryStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTokenRequest(AbstractModel):
    """DescribeInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 ID
        :type RegistryId: str
        :param _Limit: 分页单页数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        """
        self._RegistryId = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

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
        self._RegistryId = params.get("RegistryId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTokenResponse(AbstractModel):
    """DescribeInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 长期访问凭证总数
        :type TotalCount: int
        :param _Tokens: 长期访问凭证列表
        :type Tokens: list of TcrInstanceToken
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tokens = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tokens(self):
        return self._Tokens

    @Tokens.setter
    def Tokens(self, Tokens):
        self._Tokens = Tokens

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tokens") is not None:
            self._Tokens = []
            for item in params.get("Tokens"):
                obj = TcrInstanceToken()
                obj._deserialize(item)
                self._Tokens.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Registryids: 实例ID列表(为空时，
表示获取账号下所有实例)
        :type Registryids: list of str
        :param _Offset: 偏移量,默认0
        :type Offset: int
        :param _Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _AllRegion: 获取所有地域的实例，默认为False
        :type AllRegion: bool
        """
        self._Registryids = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._AllRegion = None

    @property
    def Registryids(self):
        return self._Registryids

    @Registryids.setter
    def Registryids(self, Registryids):
        self._Registryids = Registryids

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AllRegion(self):
        return self._AllRegion

    @AllRegion.setter
    def AllRegion(self, AllRegion):
        self._AllRegion = AllRegion


    def _deserialize(self, params):
        self._Registryids = params.get("Registryids")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._AllRegion = params.get("AllRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总实例个数
        :type TotalCount: int
        :param _Registries: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Registries: list of Registry
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Registries = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Registries(self):
        return self._Registries

    @Registries.setter
    def Registries(self, Registries):
        self._Registries = Registries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Registries") is not None:
            self._Registries = []
            for item in params.get("Registries"):
                obj = Registry()
                obj._deserialize(item)
                self._Registries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInternalEndpointDnsStatusRequest(AbstractModel):
    """DescribeInternalEndpointDnsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcSet: vpc列表
        :type VpcSet: list of VpcAndDomainInfo
        """
        self._VpcSet = None

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet


    def _deserialize(self, params):
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcAndDomainInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInternalEndpointDnsStatusResponse(AbstractModel):
    """DescribeInternalEndpointDnsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcSet: vpc私有域名解析状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcSet: list of VpcPrivateDomainStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcSet = None
        self._RequestId = None

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcPrivateDomainStatus()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInternalEndpointsRequest(AbstractModel):
    """DescribeInternalEndpoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInternalEndpointsResponse(AbstractModel):
    """DescribeInternalEndpoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessVpcSet: 内网接入信息的列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessVpcSet: list of AccessVpc
        :param _TotalCount: 内网接入总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessVpcSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccessVpcSet(self):
        return self._AccessVpcSet

    @AccessVpcSet.setter
    def AccessVpcSet(self, AccessVpcSet):
        self._AccessVpcSet = AccessVpcSet

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
        if params.get("AccessVpcSet") is not None:
            self._AccessVpcSet = []
            for item in params.get("AccessVpcSet"):
                obj = AccessVpc()
                obj._deserialize(item)
                self._AccessVpcSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNamespacePersonalRequest(AbstractModel):
    """DescribeNamespacePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间，支持模糊查询
        :type Namespace: str
        :param _Limit: 单页数量
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._Namespace = None
        self._Limit = None
        self._Offset = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
        self._Namespace = params.get("Namespace")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacePersonalResponse(AbstractModel):
    """DescribeNamespacePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 用户命名空间返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.NamespaceInfoResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = NamespaceInfoResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _NamespaceName: 指定命名空间，不填写默认查询所有命名空间
        :type NamespaceName: str
        :param _Limit: 每页个数
        :type Limit: int
        :param _Offset: 页面偏移（第几页）
        :type Offset: int
        :param _All: 列出所有命名空间
        :type All: bool
        :param _Filters: 过滤条件
- 按照【标签】过滤
   Name: Tags
   Value:   tagKey:tagVal

        :type Filters: list of Filter
        :param _KmsSignPolicy: 仅查询启用了 KMS 镜像签名的空间
        :type KmsSignPolicy: bool
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._Limit = None
        self._Offset = None
        self._All = None
        self._Filters = None
        self._KmsSignPolicy = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

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
    def All(self):
        return self._All

    @All.setter
    def All(self, All):
        self._All = All

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def KmsSignPolicy(self):
        return self._KmsSignPolicy

    @KmsSignPolicy.setter
    def KmsSignPolicy(self, KmsSignPolicy):
        self._KmsSignPolicy = KmsSignPolicy


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._All = params.get("All")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._KmsSignPolicy = params.get("KmsSignPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NamespaceList: 命名空间列表信息
        :type NamespaceList: list of TcrNamespaceInfo
        :param _TotalCount: 总个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NamespaceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NamespaceList(self):
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

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
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TcrNamespaceInfo()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的总数
        :type TotalCount: int
        :param _Regions: 地域信息列表
        :type Regions: list of Region
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Regions = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = Region()
                obj._deserialize(item)
                self._Regions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReplicationInstanceCreateTasksRequest(AbstractModel):
    """DescribeReplicationInstanceCreateTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReplicationRegistryId: 同步实例Id，见实例返回列表中的同步实例ID
        :type ReplicationRegistryId: str
        :param _ReplicationRegionId: 同步实例的地域ID，见实例返回列表中地域ID
        :type ReplicationRegionId: int
        """
        self._ReplicationRegistryId = None
        self._ReplicationRegionId = None

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId


    def _deserialize(self, params):
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceCreateTasksResponse(AbstractModel):
    """DescribeReplicationInstanceCreateTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskDetail: 任务详情
        :type TaskDetail: list of TaskDetail
        :param _Status: 整体任务状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskDetail = None
        self._Status = None
        self._RequestId = None

    @property
    def TaskDetail(self):
        return self._TaskDetail

    @TaskDetail.setter
    def TaskDetail(self, TaskDetail):
        self._TaskDetail = TaskDetail

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
        if params.get("TaskDetail") is not None:
            self._TaskDetail = []
            for item in params.get("TaskDetail"):
                obj = TaskDetail()
                obj._deserialize(item)
                self._TaskDetail.append(obj)
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeReplicationInstanceSyncStatusRequest(AbstractModel):
    """DescribeReplicationInstanceSyncStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例Id
        :type RegistryId: str
        :param _ReplicationRegistryId: 复制实例Id
        :type ReplicationRegistryId: str
        :param _ReplicationRegionId: 复制实例的地域Id
        :type ReplicationRegionId: int
        :param _ShowReplicationLog: 是否显示同步日志
        :type ShowReplicationLog: bool
        :param _Offset: 日志页号, 默认0
        :type Offset: int
        :param _Limit: 最大输出条数，默认5，最大为20
        :type Limit: int
        """
        self._RegistryId = None
        self._ReplicationRegistryId = None
        self._ReplicationRegionId = None
        self._ShowReplicationLog = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId

    @property
    def ShowReplicationLog(self):
        return self._ShowReplicationLog

    @ShowReplicationLog.setter
    def ShowReplicationLog(self, ShowReplicationLog):
        self._ShowReplicationLog = ShowReplicationLog

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
        self._RegistryId = params.get("RegistryId")
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        self._ShowReplicationLog = params.get("ShowReplicationLog")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceSyncStatusResponse(AbstractModel):
    """DescribeReplicationInstanceSyncStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReplicationStatus: 同步状态
        :type ReplicationStatus: str
        :param _ReplicationTime: 同步完成时间
        :type ReplicationTime: str
        :param _ReplicationLog: 同步日志
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicationLog: :class:`tencentcloud.tcr.v20190924.models.ReplicationLog`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReplicationStatus = None
        self._ReplicationTime = None
        self._ReplicationLog = None
        self._RequestId = None

    @property
    def ReplicationStatus(self):
        return self._ReplicationStatus

    @ReplicationStatus.setter
    def ReplicationStatus(self, ReplicationStatus):
        self._ReplicationStatus = ReplicationStatus

    @property
    def ReplicationTime(self):
        return self._ReplicationTime

    @ReplicationTime.setter
    def ReplicationTime(self, ReplicationTime):
        self._ReplicationTime = ReplicationTime

    @property
    def ReplicationLog(self):
        return self._ReplicationLog

    @ReplicationLog.setter
    def ReplicationLog(self, ReplicationLog):
        self._ReplicationLog = ReplicationLog

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReplicationStatus = params.get("ReplicationStatus")
        self._ReplicationTime = params.get("ReplicationTime")
        if params.get("ReplicationLog") is not None:
            self._ReplicationLog = ReplicationLog()
            self._ReplicationLog._deserialize(params.get("ReplicationLog"))
        self._RequestId = params.get("RequestId")


class DescribeReplicationInstancesRequest(AbstractModel):
    """DescribeReplicationInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Offset: 偏移量,默认0
        :type Offset: int
        :param _Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        """
        self._RegistryId = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

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
        self._RegistryId = params.get("RegistryId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstancesResponse(AbstractModel):
    """DescribeReplicationInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总实例个数
        :type TotalCount: int
        :param _ReplicationRegistries: 同步实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicationRegistries: list of ReplicationRegistry
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReplicationRegistries = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReplicationRegistries(self):
        return self._ReplicationRegistries

    @ReplicationRegistries.setter
    def ReplicationRegistries(self, ReplicationRegistries):
        self._ReplicationRegistries = ReplicationRegistries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ReplicationRegistries") is not None:
            self._ReplicationRegistries = []
            for item in params.get("ReplicationRegistries"):
                obj = ReplicationRegistry()
                obj._deserialize(item)
                self._ReplicationRegistries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRepositoriesRequest(AbstractModel):
    """DescribeRepositories请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _NamespaceName: 指定命名空间，不填写默认为查询所有命名空间下镜像仓库
        :type NamespaceName: str
        :param _RepositoryName: 指定镜像仓库，不填写默认查询指定命名空间下所有镜像仓库
        :type RepositoryName: str
        :param _Offset: 页数，用于分页
        :type Offset: int
        :param _Limit: 每页个数，用于分页
        :type Limit: int
        :param _SortBy: 基于字段排序，支持的值有-creation_time,-name, -update_time
        :type SortBy: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._Offset = None
        self._Limit = None
        self._SortBy = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

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
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoriesResponse(AbstractModel):
    """DescribeRepositories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RepositoryList: 仓库信息列表
        :type RepositoryList: list of TcrRepositoryInfo
        :param _TotalCount: 总个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RepositoryList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RepositoryList(self):
        return self._RepositoryList

    @RepositoryList.setter
    def RepositoryList(self, RepositoryList):
        self._RepositoryList = RepositoryList

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
        if params.get("RepositoryList") is not None:
            self._RepositoryList = []
            for item in params.get("RepositoryList"):
                obj = TcrRepositoryInfo()
                obj._deserialize(item)
                self._RepositoryList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRepositoryFilterPersonalRequest(AbstractModel):
    """DescribeRepositoryFilterPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 搜索镜像名
        :type RepoName: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回最大数量，默认 20，最大100
        :type Limit: int
        :param _Public: 筛选条件：1表示public，0表示private
        :type Public: int
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._RepoName = None
        self._Offset = None
        self._Limit = None
        self._Public = None
        self._Namespace = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

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
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Public = params.get("Public")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryFilterPersonalResponse(AbstractModel):
    """DescribeRepositoryFilterPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.SearchUserRepositoryResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SearchUserRepositoryResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRepositoryOwnerPersonalRequest(AbstractModel):
    """DescribeRepositoryOwnerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param _RepoName: 仓库名称
        :type RepoName: str
        """
        self._Offset = None
        self._Limit = None
        self._RepoName = None

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
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryOwnerPersonalResponse(AbstractModel):
    """DescribeRepositoryOwnerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepoInfoResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RepoInfoResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRepositoryPersonalRequest(AbstractModel):
    """DescribeRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名字
        :type RepoName: str
        """
        self._RepoName = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryPersonalResponse(AbstractModel):
    """DescribeRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepositoryInfoResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RepositoryInfoResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSecurityPoliciesRequest(AbstractModel):
    """DescribeSecurityPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例的Id
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPoliciesResponse(AbstractModel):
    """DescribeSecurityPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityPolicySet: 实例安全策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityPolicySet: list of SecurityPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityPolicySet = None
        self._RequestId = None

    @property
    def SecurityPolicySet(self):
        return self._SecurityPolicySet

    @SecurityPolicySet.setter
    def SecurityPolicySet(self, SecurityPolicySet):
        self._SecurityPolicySet = SecurityPolicySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityPolicySet") is not None:
            self._SecurityPolicySet = []
            for item in params.get("SecurityPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self._SecurityPolicySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceAccountsRequest(AbstractModel):
    """DescribeServiceAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _All: 列出所有服务级账号
        :type All: bool
        :param _EmbedPermission: 是否填充权限信息
        :type EmbedPermission: bool
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Offset: 偏移量,默认0
        :type Offset: int
        :param _Limit: 最大输出条数，默认20，最大为100（超出最大值，调整到最大值）
        :type Limit: int
        """
        self._RegistryId = None
        self._All = None
        self._EmbedPermission = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def All(self):
        return self._All

    @All.setter
    def All(self, All):
        self._All = All

    @property
    def EmbedPermission(self):
        return self._EmbedPermission

    @EmbedPermission.setter
    def EmbedPermission(self, EmbedPermission):
        self._EmbedPermission = EmbedPermission

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
        self._RegistryId = params.get("RegistryId")
        self._All = params.get("All")
        self._EmbedPermission = params.get("EmbedPermission")
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
        


class DescribeServiceAccountsResponse(AbstractModel):
    """DescribeServiceAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceAccounts: 服务级账号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceAccounts: list of ServiceAccount
        :param _TotalCount: 服务级账户数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceAccounts = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ServiceAccounts(self):
        return self._ServiceAccounts

    @ServiceAccounts.setter
    def ServiceAccounts(self, ServiceAccounts):
        self._ServiceAccounts = ServiceAccounts

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
        if params.get("ServiceAccounts") is not None:
            self._ServiceAccounts = []
            for item in params.get("ServiceAccounts"):
                obj = ServiceAccount()
                obj._deserialize(item)
                self._ServiceAccounts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTagRetentionExecutionRequest(AbstractModel):
    """DescribeTagRetentionExecution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _RetentionId: 规则Id
        :type RetentionId: int
        :param _Limit: 分页PageSize
        :type Limit: int
        :param _Offset: 分页Page
        :type Offset: int
        """
        self._RegistryId = None
        self._RetentionId = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

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
        self._RegistryId = params.get("RegistryId")
        self._RetentionId = params.get("RetentionId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionExecutionResponse(AbstractModel):
    """DescribeTagRetentionExecution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RetentionExecutionList: 版本保留执行记录列表
        :type RetentionExecutionList: list of RetentionExecution
        :param _TotalCount: 版本保留执行记录总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RetentionExecutionList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RetentionExecutionList(self):
        return self._RetentionExecutionList

    @RetentionExecutionList.setter
    def RetentionExecutionList(self, RetentionExecutionList):
        self._RetentionExecutionList = RetentionExecutionList

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
        if params.get("RetentionExecutionList") is not None:
            self._RetentionExecutionList = []
            for item in params.get("RetentionExecutionList"):
                obj = RetentionExecution()
                obj._deserialize(item)
                self._RetentionExecutionList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTagRetentionExecutionTaskRequest(AbstractModel):
    """DescribeTagRetentionExecutionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _RetentionId: 规则Id
        :type RetentionId: int
        :param _ExecutionId: 规则执行Id
        :type ExecutionId: int
        :param _Offset: 分页Page
        :type Offset: int
        :param _Limit: 分页PageSize
        :type Limit: int
        """
        self._RegistryId = None
        self._RetentionId = None
        self._ExecutionId = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def ExecutionId(self):
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

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
        self._RegistryId = params.get("RegistryId")
        self._RetentionId = params.get("RetentionId")
        self._ExecutionId = params.get("ExecutionId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionExecutionTaskResponse(AbstractModel):
    """DescribeTagRetentionExecutionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RetentionTaskList: 版本保留执行任务列表
        :type RetentionTaskList: list of RetentionTask
        :param _TotalCount: 版本保留执行任务总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RetentionTaskList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RetentionTaskList(self):
        return self._RetentionTaskList

    @RetentionTaskList.setter
    def RetentionTaskList(self, RetentionTaskList):
        self._RetentionTaskList = RetentionTaskList

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
        if params.get("RetentionTaskList") is not None:
            self._RetentionTaskList = []
            for item in params.get("RetentionTaskList"):
                obj = RetentionTask()
                obj._deserialize(item)
                self._RetentionTaskList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTagRetentionRulesRequest(AbstractModel):
    """DescribeTagRetentionRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _NamespaceName: 命名空间的名称
        :type NamespaceName: str
        :param _Limit: 分页PageSize
        :type Limit: int
        :param _Offset: 分页Page
        :type Offset: int
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

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
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionRulesResponse(AbstractModel):
    """DescribeTagRetentionRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RetentionPolicyList: 版本保留策略列表
        :type RetentionPolicyList: list of RetentionPolicy
        :param _TotalCount: 版本保留策略总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RetentionPolicyList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RetentionPolicyList(self):
        return self._RetentionPolicyList

    @RetentionPolicyList.setter
    def RetentionPolicyList(self, RetentionPolicyList):
        self._RetentionPolicyList = RetentionPolicyList

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
        if params.get("RetentionPolicyList") is not None:
            self._RetentionPolicyList = []
            for item in params.get("RetentionPolicyList"):
                obj = RetentionPolicy()
                obj._deserialize(item)
                self._RetentionPolicyList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserQuotaPersonalRequest(AbstractModel):
    """DescribeUserQuotaPersonal请求参数结构体

    """


class DescribeUserQuotaPersonalResponse(AbstractModel):
    """DescribeUserQuotaPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 配额返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RespLimit`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RespLimit()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeWebhookTriggerLogRequest(AbstractModel):
    """DescribeWebhookTriggerLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 Id
        :type RegistryId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Id: 触发器 Id
        :type Id: int
        :param _Limit: 分页单页数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        """
        self._RegistryId = None
        self._Namespace = None
        self._Id = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._RegistryId = params.get("RegistryId")
        self._Namespace = params.get("Namespace")
        self._Id = params.get("Id")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebhookTriggerLogResponse(AbstractModel):
    """DescribeWebhookTriggerLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Logs: 日志列表
        :type Logs: list of WebhookTriggerLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Logs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Logs(self):
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Logs") is not None:
            self._Logs = []
            for item in params.get("Logs"):
                obj = WebhookTriggerLog()
                obj._deserialize(item)
                self._Logs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWebhookTriggerRequest(AbstractModel):
    """DescribeWebhookTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Limit: 分页单页数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._RegistryId = None
        self._Limit = None
        self._Offset = None
        self._Namespace = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

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
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebhookTriggerResponse(AbstractModel):
    """DescribeWebhookTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 触发器总数
        :type TotalCount: int
        :param _Triggers: 触发器列表
        :type Triggers: list of WebhookTrigger
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Triggers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Triggers(self):
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self._Triggers = []
            for item in params.get("Triggers"):
                obj = WebhookTrigger()
                obj._deserialize(item)
                self._Triggers.append(obj)
        self._RequestId = params.get("RequestId")


class DownloadHelmChartRequest(AbstractModel):
    """DownloadHelmChart请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _ChartName: Helm chart名称
        :type ChartName: str
        :param _ChartVersion: Helm chart版本
        :type ChartVersion: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._ChartName = None
        self._ChartVersion = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def ChartName(self):
        return self._ChartName

    @ChartName.setter
    def ChartName(self, ChartName):
        self._ChartName = ChartName

    @property
    def ChartVersion(self):
        return self._ChartVersion

    @ChartVersion.setter
    def ChartVersion(self, ChartVersion):
        self._ChartVersion = ChartVersion


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._ChartName = params.get("ChartName")
        self._ChartVersion = params.get("ChartVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadHelmChartResponse(AbstractModel):
    """DownloadHelmChart返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TmpToken: 临时token
        :type TmpToken: str
        :param _TmpSecretId: 临时的secretId
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时的secretKey
        :type TmpSecretKey: str
        :param _Bucket: 存储桶信息
        :type Bucket: str
        :param _Region: 实例ID
        :type Region: str
        :param _Path: chart信息
        :type Path: str
        :param _StartTime: 开始时间时间戳
        :type StartTime: int
        :param _ExpiredTime: token过期时间时间戳
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TmpToken = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._Bucket = None
        self._Region = None
        self._Path = None
        self._StartTime = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def TmpToken(self):
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TmpToken = params.get("TmpToken")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Path = params.get("Path")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class DupImageTagResp(AbstractModel):
    """复制镜像tag返回值

    """

    def __init__(self):
        r"""
        :param _Digest: 镜像Digest值
        :type Digest: str
        """
        self._Digest = None

    @property
    def Digest(self):
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest


    def _deserialize(self, params):
        self._Digest = params.get("Digest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateImagePersonalRequest(AbstractModel):
    """DuplicateImagePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcImage: 源镜像名称，不包含domain。例如： tencentyun/foo:v1
        :type SrcImage: str
        :param _DestImage: 目的镜像名称，不包含domain。例如： tencentyun/foo:latest
        :type DestImage: str
        """
        self._SrcImage = None
        self._DestImage = None

    @property
    def SrcImage(self):
        return self._SrcImage

    @SrcImage.setter
    def SrcImage(self, SrcImage):
        self._SrcImage = SrcImage

    @property
    def DestImage(self):
        return self._DestImage

    @DestImage.setter
    def DestImage(self, DestImage):
        self._DestImage = DestImage


    def _deserialize(self, params):
        self._SrcImage = params.get("SrcImage")
        self._DestImage = params.get("DestImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateImagePersonalResponse(AbstractModel):
    """DuplicateImagePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 复制镜像返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DupImageTagResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DupImageTagResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DuplicateImageRequest(AbstractModel):
    """DuplicateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例id
        :type RegistryId: str
        :param _SourceNamespace: 源命名空间名称
        :type SourceNamespace: str
        :param _SourceRepo: 源镜像仓库名称
        :type SourceRepo: str
        :param _SourceReference: 源镜像tag或digest值，目前仅支持tag
        :type SourceReference: str
        :param _DestinationTag: 目标镜像版本
        :type DestinationTag: str
        :param _DestinationNamespace: 目标命名空间，不填默认与源一致
        :type DestinationNamespace: str
        :param _DestinationRepo: 目标镜像仓库，不填默认与源一致
        :type DestinationRepo: str
        :param _Override: 是否覆盖
        :type Override: bool
        """
        self._RegistryId = None
        self._SourceNamespace = None
        self._SourceRepo = None
        self._SourceReference = None
        self._DestinationTag = None
        self._DestinationNamespace = None
        self._DestinationRepo = None
        self._Override = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def SourceNamespace(self):
        return self._SourceNamespace

    @SourceNamespace.setter
    def SourceNamespace(self, SourceNamespace):
        self._SourceNamespace = SourceNamespace

    @property
    def SourceRepo(self):
        return self._SourceRepo

    @SourceRepo.setter
    def SourceRepo(self, SourceRepo):
        self._SourceRepo = SourceRepo

    @property
    def SourceReference(self):
        return self._SourceReference

    @SourceReference.setter
    def SourceReference(self, SourceReference):
        self._SourceReference = SourceReference

    @property
    def DestinationTag(self):
        return self._DestinationTag

    @DestinationTag.setter
    def DestinationTag(self, DestinationTag):
        self._DestinationTag = DestinationTag

    @property
    def DestinationNamespace(self):
        return self._DestinationNamespace

    @DestinationNamespace.setter
    def DestinationNamespace(self, DestinationNamespace):
        self._DestinationNamespace = DestinationNamespace

    @property
    def DestinationRepo(self):
        return self._DestinationRepo

    @DestinationRepo.setter
    def DestinationRepo(self, DestinationRepo):
        self._DestinationRepo = DestinationRepo

    @property
    def Override(self):
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._SourceNamespace = params.get("SourceNamespace")
        self._SourceRepo = params.get("SourceRepo")
        self._SourceReference = params.get("SourceReference")
        self._DestinationTag = params.get("DestinationTag")
        self._DestinationNamespace = params.get("DestinationNamespace")
        self._DestinationRepo = params.get("DestinationRepo")
        self._Override = params.get("Override")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateImageResponse(AbstractModel):
    """DuplicateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class FavorResp(AbstractModel):
    """用于获取收藏仓库的响应

    """

    def __init__(self):
        r"""
        :param _TotalCount: 收藏仓库的总数
        :type TotalCount: int
        :param _RepoInfo: 仓库信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoInfo: list of Favors
        """
        self._TotalCount = None
        self._RepoInfo = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RepoInfo(self):
        return self._RepoInfo

    @RepoInfo.setter
    def RepoInfo(self, RepoInfo):
        self._RepoInfo = RepoInfo


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self._RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = Favors()
                obj._deserialize(item)
                self._RepoInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Favors(AbstractModel):
    """仓库收藏

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名字
        :type RepoName: str
        :param _RepoType: 仓库类型
        :type RepoType: str
        :param _PullCount: Pull总共的次数
注意：此字段可能返回 null，表示取不到有效值。
        :type PullCount: int
        :param _FavorCount: 仓库收藏次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FavorCount: int
        :param _Public: 仓库是否公开
注意：此字段可能返回 null，表示取不到有效值。
        :type Public: int
        :param _IsQcloudOfficial: 是否为官方所有
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQcloudOfficial: bool
        :param _TagCount: 仓库Tag的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TagCount: int
        :param _Logo: Logo
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param _Region: 地域
        :type Region: str
        :param _RegionId: 地域的Id
        :type RegionId: int
        """
        self._RepoName = None
        self._RepoType = None
        self._PullCount = None
        self._FavorCount = None
        self._Public = None
        self._IsQcloudOfficial = None
        self._TagCount = None
        self._Logo = None
        self._Region = None
        self._RegionId = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def PullCount(self):
        return self._PullCount

    @PullCount.setter
    def PullCount(self, PullCount):
        self._PullCount = PullCount

    @property
    def FavorCount(self):
        return self._FavorCount

    @FavorCount.setter
    def FavorCount(self, FavorCount):
        self._FavorCount = FavorCount

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def IsQcloudOfficial(self):
        return self._IsQcloudOfficial

    @IsQcloudOfficial.setter
    def IsQcloudOfficial(self, IsQcloudOfficial):
        self._IsQcloudOfficial = IsQcloudOfficial

    @property
    def TagCount(self):
        return self._TagCount

    @TagCount.setter
    def TagCount(self, TagCount):
        self._TagCount = TagCount

    @property
    def Logo(self):
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._RepoType = params.get("RepoType")
        self._PullCount = params.get("PullCount")
        self._FavorCount = params.get("FavorCount")
        self._Public = params.get("Public")
        self._IsQcloudOfficial = params.get("IsQcloudOfficial")
        self._TagCount = params.get("TagCount")
        self._Logo = params.get("Logo")
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

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
        


class GCJobInfo(AbstractModel):
    """GC 执行信息

    """

    def __init__(self):
        r"""
        :param _ID: 作业 ID
        :type ID: int
        :param _JobStatus: 作业状态
        :type JobStatus: str
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Schedule: 调度信息
        :type Schedule: :class:`tencentcloud.tcr.v20190924.models.Schedule`
        """
        self._ID = None
        self._JobStatus = None
        self._CreationTime = None
        self._UpdateTime = None
        self._Schedule = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def JobStatus(self):
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Schedule(self):
        return self._Schedule

    @Schedule.setter
    def Schedule(self, Schedule):
        self._Schedule = Schedule


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._JobStatus = params.get("JobStatus")
        self._CreationTime = params.get("CreationTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Schedule") is not None:
            self._Schedule = Schedule()
            self._Schedule._deserialize(params.get("Schedule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """Header KV

    """

    def __init__(self):
        r"""
        :param _Key: Header Key
        :type Key: str
        :param _Values: Header Values
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImmutableTagRule(AbstractModel):
    """镜像 tag 不可变规则

    """

    def __init__(self):
        r"""
        :param _RepositoryPattern: 仓库匹配规则
        :type RepositoryPattern: str
        :param _TagPattern: Tag 匹配规则
        :type TagPattern: str
        :param _RepositoryDecoration: repoMatches或repoExcludes
        :type RepositoryDecoration: str
        :param _TagDecoration: matches或excludes
        :type TagDecoration: str
        :param _Disabled: 禁用规则
        :type Disabled: bool
        :param _RuleId: 规则 Id
        :type RuleId: int
        :param _NsName: 命名空间
        :type NsName: str
        """
        self._RepositoryPattern = None
        self._TagPattern = None
        self._RepositoryDecoration = None
        self._TagDecoration = None
        self._Disabled = None
        self._RuleId = None
        self._NsName = None

    @property
    def RepositoryPattern(self):
        return self._RepositoryPattern

    @RepositoryPattern.setter
    def RepositoryPattern(self, RepositoryPattern):
        self._RepositoryPattern = RepositoryPattern

    @property
    def TagPattern(self):
        return self._TagPattern

    @TagPattern.setter
    def TagPattern(self, TagPattern):
        self._TagPattern = TagPattern

    @property
    def RepositoryDecoration(self):
        return self._RepositoryDecoration

    @RepositoryDecoration.setter
    def RepositoryDecoration(self, RepositoryDecoration):
        self._RepositoryDecoration = RepositoryDecoration

    @property
    def TagDecoration(self):
        return self._TagDecoration

    @TagDecoration.setter
    def TagDecoration(self, TagDecoration):
        self._TagDecoration = TagDecoration

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def NsName(self):
        return self._NsName

    @NsName.setter
    def NsName(self, NsName):
        self._NsName = NsName


    def _deserialize(self, params):
        self._RepositoryPattern = params.get("RepositoryPattern")
        self._TagPattern = params.get("TagPattern")
        self._RepositoryDecoration = params.get("RepositoryDecoration")
        self._TagDecoration = params.get("TagDecoration")
        self._Disabled = params.get("Disabled")
        self._RuleId = params.get("RuleId")
        self._NsName = params.get("NsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueString(AbstractModel):
    """通用参数字符串键值对

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
        


class Limit(AbstractModel):
    """共享镜像仓库用户配额

    """

    def __init__(self):
        r"""
        :param _Username: 用户名
        :type Username: str
        :param _Type: 配额的类型
        :type Type: str
        :param _Value: 配置的值
        :type Value: int
        """
        self._Username = None
        self._Type = None
        self._Value = None

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageExternalEndpointRequest(AbstractModel):
    """ManageExternalEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Operation: 操作（Create/Delete）
        :type Operation: str
        """
        self._RegistryId = None
        self._Operation = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageExternalEndpointResponse(AbstractModel):
    """ManageExternalEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class ManageImageLifecycleGlobalPersonalRequest(AbstractModel):
    """ManageImageLifecycleGlobalPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: global_keep_last_days:全局保留最近几天的数据;global_keep_last_nums:全局保留最近多少个
        :type Type: str
        :param _Val: 策略值
        :type Val: int
        """
        self._Type = None
        self._Val = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Val(self):
        return self._Val

    @Val.setter
    def Val(self, Val):
        self._Val = Val


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Val = params.get("Val")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageImageLifecycleGlobalPersonalResponse(AbstractModel):
    """ManageImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ManageInternalEndpointRequest(AbstractModel):
    """ManageInternalEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Operation: Create/Delete
        :type Operation: str
        :param _VpcId: 需要接入的用户vpcid
        :type VpcId: str
        :param _SubnetId: 需要接入的用户子网id
        :type SubnetId: str
        :param _RegionId: 请求的地域ID，用于实例复制地域
        :type RegionId: int
        :param _RegionName: 请求的地域名称，用于实例复制地域
        :type RegionName: str
        """
        self._RegistryId = None
        self._Operation = None
        self._VpcId = None
        self._SubnetId = None
        self._RegionId = None
        self._RegionName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

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
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Operation = params.get("Operation")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageInternalEndpointResponse(AbstractModel):
    """ManageInternalEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class ManageReplicationRequest(AbstractModel):
    """ManageReplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceRegistryId: 复制源实例ID
        :type SourceRegistryId: str
        :param _DestinationRegistryId: 复制目标实例ID
        :type DestinationRegistryId: str
        :param _Rule: 同步规则
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ReplicationRule`
        :param _Description: 规则描述
        :type Description: str
        :param _DestinationRegionId: 目标实例的地域ID，如广州是1
        :type DestinationRegionId: int
        :param _PeerReplicationOption: 开启跨主账号实例同步配置项
        :type PeerReplicationOption: :class:`tencentcloud.tcr.v20190924.models.PeerReplicationOption`
        """
        self._SourceRegistryId = None
        self._DestinationRegistryId = None
        self._Rule = None
        self._Description = None
        self._DestinationRegionId = None
        self._PeerReplicationOption = None

    @property
    def SourceRegistryId(self):
        return self._SourceRegistryId

    @SourceRegistryId.setter
    def SourceRegistryId(self, SourceRegistryId):
        self._SourceRegistryId = SourceRegistryId

    @property
    def DestinationRegistryId(self):
        return self._DestinationRegistryId

    @DestinationRegistryId.setter
    def DestinationRegistryId(self, DestinationRegistryId):
        self._DestinationRegistryId = DestinationRegistryId

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DestinationRegionId(self):
        return self._DestinationRegionId

    @DestinationRegionId.setter
    def DestinationRegionId(self, DestinationRegionId):
        self._DestinationRegionId = DestinationRegionId

    @property
    def PeerReplicationOption(self):
        return self._PeerReplicationOption

    @PeerReplicationOption.setter
    def PeerReplicationOption(self, PeerReplicationOption):
        self._PeerReplicationOption = PeerReplicationOption


    def _deserialize(self, params):
        self._SourceRegistryId = params.get("SourceRegistryId")
        self._DestinationRegistryId = params.get("DestinationRegistryId")
        if params.get("Rule") is not None:
            self._Rule = ReplicationRule()
            self._Rule._deserialize(params.get("Rule"))
        self._Description = params.get("Description")
        self._DestinationRegionId = params.get("DestinationRegionId")
        if params.get("PeerReplicationOption") is not None:
            self._PeerReplicationOption = PeerReplicationOption()
            self._PeerReplicationOption._deserialize(params.get("PeerReplicationOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageReplicationResponse(AbstractModel):
    """ManageReplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyApplicationTriggerPersonalRequest(AbstractModel):
    """ModifyApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 触发器关联的镜像仓库，library/test格式
        :type RepoName: str
        :param _TriggerName: 触发器名称，必填参数
        :type TriggerName: str
        :param _InvokeMethod: 触发方式，"all"全部触发，"taglist"指定tag触发，"regex"正则触发
        :type InvokeMethod: str
        :param _InvokeExpr: 触发方式对应的表达式
        :type InvokeExpr: str
        :param _ClusterId: 应用所在TKE集群ID
        :type ClusterId: str
        :param _Namespace: 应用所在TKE集群命名空间
        :type Namespace: str
        :param _WorkloadType: 应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。
        :type WorkloadType: str
        :param _WorkloadName: 应用所在TKE集群工作负载名称
        :type WorkloadName: str
        :param _ContainerName: 应用所在TKE集群工作负载下容器名称
        :type ContainerName: str
        :param _ClusterRegion: 应用所在TKE集群地域数字ID，如1（广州）、16（成都）
        :type ClusterRegion: int
        :param _NewTriggerName: 新触发器名称
        :type NewTriggerName: str
        """
        self._RepoName = None
        self._TriggerName = None
        self._InvokeMethod = None
        self._InvokeExpr = None
        self._ClusterId = None
        self._Namespace = None
        self._WorkloadType = None
        self._WorkloadName = None
        self._ContainerName = None
        self._ClusterRegion = None
        self._NewTriggerName = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def InvokeMethod(self):
        return self._InvokeMethod

    @InvokeMethod.setter
    def InvokeMethod(self, InvokeMethod):
        self._InvokeMethod = InvokeMethod

    @property
    def InvokeExpr(self):
        return self._InvokeExpr

    @InvokeExpr.setter
    def InvokeExpr(self, InvokeExpr):
        self._InvokeExpr = InvokeExpr

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def WorkloadType(self):
        return self._WorkloadType

    @WorkloadType.setter
    def WorkloadType(self, WorkloadType):
        self._WorkloadType = WorkloadType

    @property
    def WorkloadName(self):
        return self._WorkloadName

    @WorkloadName.setter
    def WorkloadName(self, WorkloadName):
        self._WorkloadName = WorkloadName

    @property
    def ContainerName(self):
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def ClusterRegion(self):
        return self._ClusterRegion

    @ClusterRegion.setter
    def ClusterRegion(self, ClusterRegion):
        self._ClusterRegion = ClusterRegion

    @property
    def NewTriggerName(self):
        return self._NewTriggerName

    @NewTriggerName.setter
    def NewTriggerName(self, NewTriggerName):
        self._NewTriggerName = NewTriggerName


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._TriggerName = params.get("TriggerName")
        self._InvokeMethod = params.get("InvokeMethod")
        self._InvokeExpr = params.get("InvokeExpr")
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._WorkloadType = params.get("WorkloadType")
        self._WorkloadName = params.get("WorkloadName")
        self._ContainerName = params.get("ContainerName")
        self._ClusterRegion = params.get("ClusterRegion")
        self._NewTriggerName = params.get("NewTriggerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationTriggerPersonalResponse(AbstractModel):
    """ModifyApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyImmutableTagRulesRequest(AbstractModel):
    """ModifyImmutableTagRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例 Id
        :type RegistryId: str
        :param _NamespaceName: 命名空间
        :type NamespaceName: str
        :param _RuleId: 规则 Id
        :type RuleId: int
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RuleId = None
        self._Rule = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RuleId = params.get("RuleId")
        if params.get("Rule") is not None:
            self._Rule = ImmutableTagRule()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImmutableTagRulesResponse(AbstractModel):
    """ModifyImmutableTagRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _RegistryType: 实例的规格,
基础版：basic
标准版：standard
高级版：premium
        :type RegistryType: str
        :param _DeletionProtection: 实例删除保护，false为关闭
        :type DeletionProtection: bool
        """
        self._RegistryId = None
        self._RegistryType = None
        self._DeletionProtection = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RegistryType(self):
        return self._RegistryType

    @RegistryType.setter
    def RegistryType(self, RegistryType):
        self._RegistryType = RegistryType

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RegistryType = params.get("RegistryType")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstanceTokenRequest(AbstractModel):
    """ModifyInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TokenId: 实例长期访问凭证 ID
        :type TokenId: str
        :param _RegistryId: 实例 ID
        :type RegistryId: str
        :param _Enable: 启用或禁用实例长期访问凭证
        :type Enable: bool
        :param _Desc: 访问凭证描述
        :type Desc: str
        :param _ModifyFlag: 1为修改描述 2为操作启动禁用，默认值为2
        :type ModifyFlag: int
        """
        self._TokenId = None
        self._RegistryId = None
        self._Enable = None
        self._Desc = None
        self._ModifyFlag = None

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ModifyFlag(self):
        return self._ModifyFlag

    @ModifyFlag.setter
    def ModifyFlag(self, ModifyFlag):
        self._ModifyFlag = ModifyFlag


    def _deserialize(self, params):
        self._TokenId = params.get("TokenId")
        self._RegistryId = params.get("RegistryId")
        self._Enable = params.get("Enable")
        self._Desc = params.get("Desc")
        self._ModifyFlag = params.get("ModifyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceTokenResponse(AbstractModel):
    """ModifyInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _IsPublic: 访问级别，True为公开，False为私有
        :type IsPublic: bool
        :param _IsAutoScan: 扫描级别，True为自动，False为手动
        :type IsAutoScan: bool
        :param _IsPreventVUL: 阻断开关，True为开放，False为关闭
        :type IsPreventVUL: bool
        :param _Severity: 阻断漏洞等级，目前仅支持 low、medium、high
        :type Severity: str
        :param _CVEWhitelistItems: 漏洞白名单列表
        :type CVEWhitelistItems: list of CVEWhitelistItem
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._IsPublic = None
        self._IsAutoScan = None
        self._IsPreventVUL = None
        self._Severity = None
        self._CVEWhitelistItems = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def IsAutoScan(self):
        return self._IsAutoScan

    @IsAutoScan.setter
    def IsAutoScan(self, IsAutoScan):
        self._IsAutoScan = IsAutoScan

    @property
    def IsPreventVUL(self):
        return self._IsPreventVUL

    @IsPreventVUL.setter
    def IsPreventVUL(self, IsPreventVUL):
        self._IsPreventVUL = IsPreventVUL

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def CVEWhitelistItems(self):
        return self._CVEWhitelistItems

    @CVEWhitelistItems.setter
    def CVEWhitelistItems(self, CVEWhitelistItems):
        self._CVEWhitelistItems = CVEWhitelistItems


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._IsPublic = params.get("IsPublic")
        self._IsAutoScan = params.get("IsAutoScan")
        self._IsPreventVUL = params.get("IsPreventVUL")
        self._Severity = params.get("Severity")
        if params.get("CVEWhitelistItems") is not None:
            self._CVEWhitelistItems = []
            for item in params.get("CVEWhitelistItems"):
                obj = CVEWhitelistItem()
                obj._deserialize(item)
                self._CVEWhitelistItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyRepositoryAccessPersonalRequest(AbstractModel):
    """ModifyRepositoryAccessPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Public: 默认值为0, 1公共，0私有
        :type Public: int
        """
        self._RepoName = None
        self._Public = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Public = params.get("Public")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRepositoryAccessPersonalResponse(AbstractModel):
    """ModifyRepositoryAccessPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyRepositoryInfoPersonalRequest(AbstractModel):
    """ModifyRepositoryInfoPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _Description: 仓库描述
        :type Description: str
        """
        self._RepoName = None
        self._Description = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRepositoryInfoPersonalResponse(AbstractModel):
    """ModifyRepositoryInfoPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyRepositoryRequest(AbstractModel):
    """ModifyRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param _BriefDescription: 仓库简短描述
        :type BriefDescription: str
        :param _Description: 仓库详细描述
        :type Description: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._BriefDescription = None
        self._Description = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def BriefDescription(self):
        return self._BriefDescription

    @BriefDescription.setter
    def BriefDescription(self, BriefDescription):
        self._BriefDescription = BriefDescription

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._BriefDescription = params.get("BriefDescription")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRepositoryResponse(AbstractModel):
    """ModifyRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例的Id
        :type RegistryId: str
        :param _PolicyIndex: PolicyId
        :type PolicyIndex: int
        :param _CidrBlock: 192.168.0.0/24 白名单Ip
        :type CidrBlock: str
        :param _Description: 备注
        :type Description: str
        """
        self._RegistryId = None
        self._PolicyIndex = None
        self._CidrBlock = None
        self._Description = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def PolicyIndex(self):
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._PolicyIndex = params.get("PolicyIndex")
        self._CidrBlock = params.get("CidrBlock")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class ModifyServiceAccountPasswordRequest(AbstractModel):
    """ModifyServiceAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Name: 服务级账号名
        :type Name: str
        :param _Random: 是否随机生成密码
        :type Random: bool
        :param _Password: 服务级账号密码，长度在8到20之间且需包含至少一个大写字符，一个小写字符和一个数字
        :type Password: str
        """
        self._RegistryId = None
        self._Name = None
        self._Random = None
        self._Password = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Random(self):
        return self._Random

    @Random.setter
    def Random(self, Random):
        self._Random = Random

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._Random = params.get("Random")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceAccountPasswordResponse(AbstractModel):
    """ModifyServiceAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Password: 自定义用户密码，仅展示一次，请注意留存	
        :type Password: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Password = None
        self._RequestId = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._RequestId = params.get("RequestId")


class ModifyServiceAccountRequest(AbstractModel):
    """ModifyServiceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Name: 服务级账号名
        :type Name: str
        :param _Description: 服务级账号描述
        :type Description: str
        :param _Duration: 有效期(单位：天)，从当前时间开始计算，优先级高于ExpiresAt
        :type Duration: int
        :param _ExpiresAt: 过期时间（时间戳，单位:毫秒）
        :type ExpiresAt: int
        :param _Disable: 是否禁用服务级账号
        :type Disable: bool
        :param _Permissions: 策略列表
        :type Permissions: list of Permission
        """
        self._RegistryId = None
        self._Name = None
        self._Description = None
        self._Duration = None
        self._ExpiresAt = None
        self._Disable = None
        self._Permissions = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Duration = params.get("Duration")
        self._ExpiresAt = params.get("ExpiresAt")
        self._Disable = params.get("Disable")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceAccountResponse(AbstractModel):
    """ModifyServiceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyTagRetentionRuleRequest(AbstractModel):
    """ModifyTagRetentionRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例iD
        :type RegistryId: str
        :param _NamespaceId: 命名空间的Id，必须填写原有的命名空间id
        :type NamespaceId: int
        :param _RetentionRule: 保留策略
        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`
        :param _CronSetting: 执行周期，必须填写为原来的设置
        :type CronSetting: str
        :param _RetentionId: 规则Id
        :type RetentionId: int
        :param _Disabled: 是否禁用规则
        :type Disabled: bool
        """
        self._RegistryId = None
        self._NamespaceId = None
        self._RetentionRule = None
        self._CronSetting = None
        self._RetentionId = None
        self._Disabled = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def RetentionRule(self):
        return self._RetentionRule

    @RetentionRule.setter
    def RetentionRule(self, RetentionRule):
        self._RetentionRule = RetentionRule

    @property
    def CronSetting(self):
        return self._CronSetting

    @CronSetting.setter
    def CronSetting(self, CronSetting):
        self._CronSetting = CronSetting

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceId = params.get("NamespaceId")
        if params.get("RetentionRule") is not None:
            self._RetentionRule = RetentionRule()
            self._RetentionRule._deserialize(params.get("RetentionRule"))
        self._CronSetting = params.get("CronSetting")
        self._RetentionId = params.get("RetentionId")
        self._Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTagRetentionRuleResponse(AbstractModel):
    """ModifyTagRetentionRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyUserPasswordPersonalRequest(AbstractModel):
    """ModifyUserPasswordPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Password: 更新后的密码
        :type Password: str
        """
        self._Password = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserPasswordPersonalResponse(AbstractModel):
    """ModifyUserPasswordPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyWebhookTriggerRequest(AbstractModel):
    """ModifyWebhookTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _Trigger: 触发器参数
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._RegistryId = None
        self._Trigger = None
        self._Namespace = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self._Trigger = WebhookTrigger()
            self._Trigger._deserialize(params.get("Trigger"))
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebhookTriggerResponse(AbstractModel):
    """ModifyWebhookTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class NamespaceInfo(AbstractModel):
    """命名空间信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _RepoCount: 命名空间下仓库数量
        :type RepoCount: int
        """
        self._Namespace = None
        self._CreationTime = None
        self._RepoCount = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def RepoCount(self):
        return self._RepoCount

    @RepoCount.setter
    def RepoCount(self, RepoCount):
        self._RepoCount = RepoCount


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._CreationTime = params.get("CreationTime")
        self._RepoCount = params.get("RepoCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceInfoResp(AbstractModel):
    """获取命名空间信息返回

    """

    def __init__(self):
        r"""
        :param _NamespaceCount: 命名空间数量
        :type NamespaceCount: int
        :param _NamespaceInfo: 命名空间信息
        :type NamespaceInfo: list of NamespaceInfo
        """
        self._NamespaceCount = None
        self._NamespaceInfo = None

    @property
    def NamespaceCount(self):
        return self._NamespaceCount

    @NamespaceCount.setter
    def NamespaceCount(self, NamespaceCount):
        self._NamespaceCount = NamespaceCount

    @property
    def NamespaceInfo(self):
        return self._NamespaceInfo

    @NamespaceInfo.setter
    def NamespaceInfo(self, NamespaceInfo):
        self._NamespaceInfo = NamespaceInfo


    def _deserialize(self, params):
        self._NamespaceCount = params.get("NamespaceCount")
        if params.get("NamespaceInfo") is not None:
            self._NamespaceInfo = []
            for item in params.get("NamespaceInfo"):
                obj = NamespaceInfo()
                obj._deserialize(item)
                self._NamespaceInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceIsExistsResp(AbstractModel):
    """NamespaceIsExists返回类型

    """

    def __init__(self):
        r"""
        :param _IsExist: 命名空间是否存在
        :type IsExist: bool
        :param _IsPreserved: 是否为保留命名空间
        :type IsPreserved: bool
        """
        self._IsExist = None
        self._IsPreserved = None

    @property
    def IsExist(self):
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

    @property
    def IsPreserved(self):
        return self._IsPreserved

    @IsPreserved.setter
    def IsPreserved(self, IsPreserved):
        self._IsPreserved = IsPreserved


    def _deserialize(self, params):
        self._IsExist = params.get("IsExist")
        self._IsPreserved = params.get("IsPreserved")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeerReplicationOption(AbstractModel):
    """跨主账号实例同步参数

    """

    def __init__(self):
        r"""
        :param _PeerRegistryUin: 待同步实例的uin
        :type PeerRegistryUin: str
        :param _PeerRegistryToken: 待同步实例的访问永久Token
        :type PeerRegistryToken: str
        :param _EnablePeerReplication: 是否开启跨主账号实例同步
        :type EnablePeerReplication: bool
        """
        self._PeerRegistryUin = None
        self._PeerRegistryToken = None
        self._EnablePeerReplication = None

    @property
    def PeerRegistryUin(self):
        return self._PeerRegistryUin

    @PeerRegistryUin.setter
    def PeerRegistryUin(self, PeerRegistryUin):
        self._PeerRegistryUin = PeerRegistryUin

    @property
    def PeerRegistryToken(self):
        return self._PeerRegistryToken

    @PeerRegistryToken.setter
    def PeerRegistryToken(self, PeerRegistryToken):
        self._PeerRegistryToken = PeerRegistryToken

    @property
    def EnablePeerReplication(self):
        return self._EnablePeerReplication

    @EnablePeerReplication.setter
    def EnablePeerReplication(self, EnablePeerReplication):
        self._EnablePeerReplication = EnablePeerReplication


    def _deserialize(self, params):
        self._PeerRegistryUin = params.get("PeerRegistryUin")
        self._PeerRegistryToken = params.get("PeerRegistryToken")
        self._EnablePeerReplication = params.get("EnablePeerReplication")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Permission(AbstractModel):
    """策略

    """

    def __init__(self):
        r"""
        :param _Resource: 资源路径，目前仅支持Namespace
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Actions: 动作，目前仅支持：tcr:PushRepository、tcr:PullRepository、tcr:CreateRepository、tcr:CreateHelmChart、tcr:DescribeHelmCharts
注意：此字段可能返回 null，表示取不到有效值。
        :type Actions: list of str
        """
        self._Resource = None
        self._Actions = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param _Alias: gz
        :type Alias: str
        :param _RegionId: 1
        :type RegionId: int
        :param _RegionName: ap-guangzhou
        :type RegionName: str
        :param _Status: alluser
        :type Status: str
        :param _Remark: remark
        :type Remark: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _Id: id
        :type Id: int
        """
        self._Alias = None
        self._RegionId = None
        self._RegionName = None
        self._Status = None
        self._Remark = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Id = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Registry(AbstractModel):
    """实例信息结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例ID
        :type RegistryId: str
        :param _RegistryName: 实例名称
        :type RegistryName: str
        :param _RegistryType: 实例规格
        :type RegistryType: str
        :param _Status: 实例状态
        :type Status: str
        :param _PublicDomain: 实例的公共访问地址
        :type PublicDomain: str
        :param _CreatedAt: 实例创建时间
        :type CreatedAt: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _RegionId: 地域Id
        :type RegionId: int
        :param _EnableAnonymous: 是否支持匿名
        :type EnableAnonymous: bool
        :param _TokenValidTime: Token有效时间
        :type TokenValidTime: int
        :param _InternalEndpoint: 实例内部访问地址
        :type InternalEndpoint: str
        :param _TagSpecification: 实例云标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param _ExpiredAt: 实例过期时间（预付费）
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredAt: str
        :param _PayMod: 实例付费类型，0表示后付费，1表示预付费
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMod: int
        :param _RenewFlag: 预付费续费标识，0表示手动续费，1表示自动续费，2不续费并且不通知
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _DeletionProtection: 是否开启实例删除保护，false表示不开启
        :type DeletionProtection: bool
        """
        self._RegistryId = None
        self._RegistryName = None
        self._RegistryType = None
        self._Status = None
        self._PublicDomain = None
        self._CreatedAt = None
        self._RegionName = None
        self._RegionId = None
        self._EnableAnonymous = None
        self._TokenValidTime = None
        self._InternalEndpoint = None
        self._TagSpecification = None
        self._ExpiredAt = None
        self._PayMod = None
        self._RenewFlag = None
        self._DeletionProtection = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RegistryName(self):
        return self._RegistryName

    @RegistryName.setter
    def RegistryName(self, RegistryName):
        self._RegistryName = RegistryName

    @property
    def RegistryType(self):
        return self._RegistryType

    @RegistryType.setter
    def RegistryType(self, RegistryType):
        self._RegistryType = RegistryType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PublicDomain(self):
        return self._PublicDomain

    @PublicDomain.setter
    def PublicDomain(self, PublicDomain):
        self._PublicDomain = PublicDomain

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def EnableAnonymous(self):
        return self._EnableAnonymous

    @EnableAnonymous.setter
    def EnableAnonymous(self, EnableAnonymous):
        self._EnableAnonymous = EnableAnonymous

    @property
    def TokenValidTime(self):
        return self._TokenValidTime

    @TokenValidTime.setter
    def TokenValidTime(self, TokenValidTime):
        self._TokenValidTime = TokenValidTime

    @property
    def InternalEndpoint(self):
        return self._InternalEndpoint

    @InternalEndpoint.setter
    def InternalEndpoint(self, InternalEndpoint):
        self._InternalEndpoint = InternalEndpoint

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def ExpiredAt(self):
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def PayMod(self):
        return self._PayMod

    @PayMod.setter
    def PayMod(self, PayMod):
        self._PayMod = PayMod

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RegistryName = params.get("RegistryName")
        self._RegistryType = params.get("RegistryType")
        self._Status = params.get("Status")
        self._PublicDomain = params.get("PublicDomain")
        self._CreatedAt = params.get("CreatedAt")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._EnableAnonymous = params.get("EnableAnonymous")
        self._TokenValidTime = params.get("TokenValidTime")
        self._InternalEndpoint = params.get("InternalEndpoint")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        self._ExpiredAt = params.get("ExpiredAt")
        self._PayMod = params.get("PayMod")
        self._RenewFlag = params.get("RenewFlag")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryChargePrepaid(AbstractModel):
    """实例预付费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月
        :type Period: int
        :param _RenewFlag: 自动续费标识，0：手动续费，1：自动续费，2：不续费并且不通知
        :type RenewFlag: int
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryCondition(AbstractModel):
    """实例创建过程

    """

    def __init__(self):
        r"""
        :param _Type: 实例创建过程类型
        :type Type: str
        :param _Status: 实例创建过程状态
        :type Status: str
        :param _Reason: 转换到该过程的简明原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self._Type = None
        self._Status = None
        self._Reason = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryStatus(AbstractModel):
    """实例状态

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例的Id
        :type RegistryId: str
        :param _Status: 实例的状态
        :type Status: str
        :param _Conditions: 附加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of RegistryCondition
        """
        self._RegistryId = None
        self._Status = None
        self._Conditions = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Status = params.get("Status")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RegistryCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 实例Id
        :type RegistryId: str
        :param _RegistryChargePrepaid: 预付费自动续费标识和购买时长,0：手动续费，1：自动续费，2：不续费并且不通知;单位为月
        :type RegistryChargePrepaid: :class:`tencentcloud.tcr.v20190924.models.RegistryChargePrepaid`
        :param _Flag: 0 续费， 1按量转包年包月
        :type Flag: int
        """
        self._RegistryId = None
        self._RegistryChargePrepaid = None
        self._Flag = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RegistryChargePrepaid(self):
        return self._RegistryChargePrepaid

    @RegistryChargePrepaid.setter
    def RegistryChargePrepaid(self, RegistryChargePrepaid):
        self._RegistryChargePrepaid = RegistryChargePrepaid

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("RegistryChargePrepaid") is not None:
            self._RegistryChargePrepaid = RegistryChargePrepaid()
            self._RegistryChargePrepaid._deserialize(params.get("RegistryChargePrepaid"))
        self._Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: 企业版实例Id
        :type RegistryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class ReplicationFilter(AbstractModel):
    """同步规则过滤器

    """

    def __init__(self):
        r"""
        :param _Type: 类型（name、tag和resource）
        :type Type: str
        :param _Value: 默认为空
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationLog(AbstractModel):
    """同步日志

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _Source: 源资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _Destination: 目的资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Destination: str
        :param _Status: 同步状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._ResourceType = None
        self._Source = None
        self._Destination = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Destination(self):
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._Source = params.get("Source")
        self._Destination = params.get("Destination")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRegistry(AbstractModel):
    """企业版复制实例

    """

    def __init__(self):
        r"""
        :param _RegistryId: 主实例ID
        :type RegistryId: str
        :param _ReplicationRegistryId: 复制实例ID
        :type ReplicationRegistryId: str
        :param _ReplicationRegionId: 复制实例的地域ID
        :type ReplicationRegionId: int
        :param _ReplicationRegionName: 复制实例的地域名称
        :type ReplicationRegionName: str
        :param _Status: 复制实例的状态
        :type Status: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        """
        self._RegistryId = None
        self._ReplicationRegistryId = None
        self._ReplicationRegionId = None
        self._ReplicationRegionName = None
        self._Status = None
        self._CreatedAt = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId

    @property
    def ReplicationRegionName(self):
        return self._ReplicationRegionName

    @ReplicationRegionName.setter
    def ReplicationRegionName(self, ReplicationRegionName):
        self._ReplicationRegionName = ReplicationRegionName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        self._ReplicationRegionName = params.get("ReplicationRegionName")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRule(AbstractModel):
    """同步规则

    """

    def __init__(self):
        r"""
        :param _Name: 同步规则名称
        :type Name: str
        :param _DestNamespace: 目标命名空间
        :type DestNamespace: str
        :param _Override: 是否覆盖
        :type Override: bool
        :param _Filters: 同步过滤条件
        :type Filters: list of ReplicationFilter
        """
        self._Name = None
        self._DestNamespace = None
        self._Override = None
        self._Filters = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DestNamespace(self):
        return self._DestNamespace

    @DestNamespace.setter
    def DestNamespace(self, DestNamespace):
        self._DestNamespace = DestNamespace

    @property
    def Override(self):
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DestNamespace = params.get("DestNamespace")
        self._Override = params.get("Override")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ReplicationFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepoInfo(AbstractModel):
    """仓库的信息

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        :param _RepoType: 仓库类型
        :type RepoType: str
        :param _TagCount: Tag数量
        :type TagCount: int
        :param _Public: 是否为公开
        :type Public: int
        :param _IsUserFavor: 是否为用户收藏
        :type IsUserFavor: bool
        :param _IsQcloudOfficial: 是否为腾讯云官方仓库
        :type IsQcloudOfficial: bool
        :param _FavorCount: 被收藏的个数
        :type FavorCount: int
        :param _PullCount: 拉取的数量
        :type PullCount: int
        :param _Description: 描述
        :type Description: str
        :param _CreationTime: 仓库创建时间
        :type CreationTime: str
        :param _UpdateTime: 仓库更新时间
        :type UpdateTime: str
        """
        self._RepoName = None
        self._RepoType = None
        self._TagCount = None
        self._Public = None
        self._IsUserFavor = None
        self._IsQcloudOfficial = None
        self._FavorCount = None
        self._PullCount = None
        self._Description = None
        self._CreationTime = None
        self._UpdateTime = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def TagCount(self):
        return self._TagCount

    @TagCount.setter
    def TagCount(self, TagCount):
        self._TagCount = TagCount

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def IsUserFavor(self):
        return self._IsUserFavor

    @IsUserFavor.setter
    def IsUserFavor(self, IsUserFavor):
        self._IsUserFavor = IsUserFavor

    @property
    def IsQcloudOfficial(self):
        return self._IsQcloudOfficial

    @IsQcloudOfficial.setter
    def IsQcloudOfficial(self, IsQcloudOfficial):
        self._IsQcloudOfficial = IsQcloudOfficial

    @property
    def FavorCount(self):
        return self._FavorCount

    @FavorCount.setter
    def FavorCount(self, FavorCount):
        self._FavorCount = FavorCount

    @property
    def PullCount(self):
        return self._PullCount

    @PullCount.setter
    def PullCount(self, PullCount):
        self._PullCount = PullCount

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._RepoType = params.get("RepoType")
        self._TagCount = params.get("TagCount")
        self._Public = params.get("Public")
        self._IsUserFavor = params.get("IsUserFavor")
        self._IsQcloudOfficial = params.get("IsQcloudOfficial")
        self._FavorCount = params.get("FavorCount")
        self._PullCount = params.get("PullCount")
        self._Description = params.get("Description")
        self._CreationTime = params.get("CreationTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepoInfoResp(AbstractModel):
    """仓库信息的返回信息

    """

    def __init__(self):
        r"""
        :param _TotalCount: 仓库总数
        :type TotalCount: int
        :param _RepoInfo: 仓库信息列表
        :type RepoInfo: list of RepoInfo
        :param _Server: Server信息
        :type Server: str
        """
        self._TotalCount = None
        self._RepoInfo = None
        self._Server = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RepoInfo(self):
        return self._RepoInfo

    @RepoInfo.setter
    def RepoInfo(self, RepoInfo):
        self._RepoInfo = RepoInfo

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self._RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = RepoInfo()
                obj._deserialize(item)
                self._RepoInfo.append(obj)
        self._Server = params.get("Server")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepoIsExistResp(AbstractModel):
    """仓库是否存在的返回值

    """

    def __init__(self):
        r"""
        :param _IsExist: 仓库是否存在
        :type IsExist: bool
        """
        self._IsExist = None

    @property
    def IsExist(self):
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist


    def _deserialize(self, params):
        self._IsExist = params.get("IsExist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepositoryInfoResp(AbstractModel):
    """查询共享版仓库信息返回

    """

    def __init__(self):
        r"""
        :param _RepoName: 镜像仓库名字
        :type RepoName: str
        :param _RepoType: 镜像仓库类型
        :type RepoType: str
        :param _Server: 镜像仓库服务地址
        :type Server: str
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _Description: 镜像仓库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Public: 是否为公有镜像
        :type Public: int
        :param _PullCount: 下载次数
        :type PullCount: int
        :param _FavorCount: 收藏次数
        :type FavorCount: int
        :param _IsUserFavor: 是否为用户收藏
        :type IsUserFavor: bool
        :param _IsQcloudOfficial: 是否为腾讯云官方镜像
        :type IsQcloudOfficial: bool
        """
        self._RepoName = None
        self._RepoType = None
        self._Server = None
        self._CreationTime = None
        self._Description = None
        self._Public = None
        self._PullCount = None
        self._FavorCount = None
        self._IsUserFavor = None
        self._IsQcloudOfficial = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def PullCount(self):
        return self._PullCount

    @PullCount.setter
    def PullCount(self, PullCount):
        self._PullCount = PullCount

    @property
    def FavorCount(self):
        return self._FavorCount

    @FavorCount.setter
    def FavorCount(self, FavorCount):
        self._FavorCount = FavorCount

    @property
    def IsUserFavor(self):
        return self._IsUserFavor

    @IsUserFavor.setter
    def IsUserFavor(self, IsUserFavor):
        self._IsUserFavor = IsUserFavor

    @property
    def IsQcloudOfficial(self):
        return self._IsQcloudOfficial

    @IsQcloudOfficial.setter
    def IsQcloudOfficial(self, IsQcloudOfficial):
        self._IsQcloudOfficial = IsQcloudOfficial


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._RepoType = params.get("RepoType")
        self._Server = params.get("Server")
        self._CreationTime = params.get("CreationTime")
        self._Description = params.get("Description")
        self._Public = params.get("Public")
        self._PullCount = params.get("PullCount")
        self._FavorCount = params.get("FavorCount")
        self._IsUserFavor = params.get("IsUserFavor")
        self._IsQcloudOfficial = params.get("IsQcloudOfficial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RespLimit(AbstractModel):
    """用户配额返回值

    """

    def __init__(self):
        r"""
        :param _LimitInfo: 配额信息
        :type LimitInfo: list of Limit
        """
        self._LimitInfo = None

    @property
    def LimitInfo(self):
        return self._LimitInfo

    @LimitInfo.setter
    def LimitInfo(self, LimitInfo):
        self._LimitInfo = LimitInfo


    def _deserialize(self, params):
        if params.get("LimitInfo") is not None:
            self._LimitInfo = []
            for item in params.get("LimitInfo"):
                obj = Limit()
                obj._deserialize(item)
                self._LimitInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionExecution(AbstractModel):
    """版本保留规则执行

    """

    def __init__(self):
        r"""
        :param _ExecutionId: 执行Id
        :type ExecutionId: int
        :param _RetentionId: 所属规则id
        :type RetentionId: int
        :param _StartTime: 执行的开始时间
        :type StartTime: str
        :param _EndTime: 执行的结束时间
        :type EndTime: str
        :param _Status: 执行的状态，Failed, Succeed, Stopped, InProgress
        :type Status: str
        """
        self._ExecutionId = None
        self._RetentionId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None

    @property
    def ExecutionId(self):
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ExecutionId = params.get("ExecutionId")
        self._RetentionId = params.get("RetentionId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionPolicy(AbstractModel):
    """版本保留策略

    """

    def __init__(self):
        r"""
        :param _RetentionId: 版本保留策略Id
        :type RetentionId: int
        :param _NamespaceName: 命名空间的名称
        :type NamespaceName: str
        :param _RetentionRuleList: 规则列表
        :type RetentionRuleList: list of RetentionRule
        :param _CronSetting: 定期执行方式
        :type CronSetting: str
        :param _Disabled: 是否启用规则
        :type Disabled: bool
        :param _NextExecutionTime: 基于当前时间根据cronSetting后下一次任务要执行的时间，仅做参考使用
        :type NextExecutionTime: str
        """
        self._RetentionId = None
        self._NamespaceName = None
        self._RetentionRuleList = None
        self._CronSetting = None
        self._Disabled = None
        self._NextExecutionTime = None

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RetentionRuleList(self):
        return self._RetentionRuleList

    @RetentionRuleList.setter
    def RetentionRuleList(self, RetentionRuleList):
        self._RetentionRuleList = RetentionRuleList

    @property
    def CronSetting(self):
        return self._CronSetting

    @CronSetting.setter
    def CronSetting(self, CronSetting):
        self._CronSetting = CronSetting

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def NextExecutionTime(self):
        return self._NextExecutionTime

    @NextExecutionTime.setter
    def NextExecutionTime(self, NextExecutionTime):
        self._NextExecutionTime = NextExecutionTime


    def _deserialize(self, params):
        self._RetentionId = params.get("RetentionId")
        self._NamespaceName = params.get("NamespaceName")
        if params.get("RetentionRuleList") is not None:
            self._RetentionRuleList = []
            for item in params.get("RetentionRuleList"):
                obj = RetentionRule()
                obj._deserialize(item)
                self._RetentionRuleList.append(obj)
        self._CronSetting = params.get("CronSetting")
        self._Disabled = params.get("Disabled")
        self._NextExecutionTime = params.get("NextExecutionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionRule(AbstractModel):
    """版本保留规则

    """

    def __init__(self):
        r"""
        :param _Key: 支持的策略，可选值为latestPushedK（保留最新推送多少个版本）nDaysSinceLastPush（保留近天内推送）
        :type Key: str
        :param _Value: 规则设置下的对应值
        :type Value: int
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
        


class RetentionTask(AbstractModel):
    """版本保留执行的规则

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _ExecutionId: 所属的规则执行Id
        :type ExecutionId: int
        :param _StartTime: 任务开始时间
        :type StartTime: str
        :param _EndTime: 任务结束时间
        :type EndTime: str
        :param _Status: 任务的执行状态，Failed, Succeed, Stopped, InProgress
        :type Status: str
        :param _Total: 总tag数
        :type Total: int
        :param _Retained: 保留tag数
        :type Retained: int
        :param _Repository: 应用的仓库
        :type Repository: str
        """
        self._TaskId = None
        self._ExecutionId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Total = None
        self._Retained = None
        self._Repository = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ExecutionId(self):
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Retained(self):
        return self._Retained

    @Retained.setter
    def Retained(self, Retained):
        self._Retained = Retained

    @property
    def Repository(self):
        return self._Repository

    @Repository.setter
    def Repository(self, Repository):
        self._Repository = Repository


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ExecutionId = params.get("ExecutionId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Total = params.get("Total")
        self._Retained = params.get("Retained")
        self._Repository = params.get("Repository")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SameImagesResp(AbstractModel):
    """指定tag镜像内容相同的tag列表

    """

    def __init__(self):
        r"""
        :param _SameImages: tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SameImages: list of str
        """
        self._SameImages = None

    @property
    def SameImages(self):
        return self._SameImages

    @SameImages.setter
    def SameImages(self, SameImages):
        self._SameImages = SameImages


    def _deserialize(self, params):
        self._SameImages = params.get("SameImages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Schedule(AbstractModel):
    """作业调度信息

    """

    def __init__(self):
        r"""
        :param _Type: 类型：Hourly, Daily, Weekly, Custom, Manual, Dryrun, None
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchUserRepositoryResp(AbstractModel):
    """获取满足输入搜索条件的用户镜像仓库

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总个数
        :type TotalCount: int
        :param _RepoInfo: 仓库列表
        :type RepoInfo: list of RepoInfo
        :param _Server: Server
        :type Server: str
        :param _PrivilegeFiltered: PrivilegeFiltered
        :type PrivilegeFiltered: bool
        """
        self._TotalCount = None
        self._RepoInfo = None
        self._Server = None
        self._PrivilegeFiltered = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RepoInfo(self):
        return self._RepoInfo

    @RepoInfo.setter
    def RepoInfo(self, RepoInfo):
        self._RepoInfo = RepoInfo

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def PrivilegeFiltered(self):
        return self._PrivilegeFiltered

    @PrivilegeFiltered.setter
    def PrivilegeFiltered(self, PrivilegeFiltered):
        self._PrivilegeFiltered = PrivilegeFiltered


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self._RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = RepoInfo()
                obj._deserialize(item)
                self._RepoInfo.append(obj)
        self._Server = params.get("Server")
        self._PrivilegeFiltered = params.get("PrivilegeFiltered")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicy(AbstractModel):
    """安全策略

    """

    def __init__(self):
        r"""
        :param _PolicyIndex: 策略索引
        :type PolicyIndex: int
        :param _Description: 备注
        :type Description: str
        :param _CidrBlock: 运行访问的公网IP地址端
        :type CidrBlock: str
        :param _PolicyVersion: 安全策略的版本
        :type PolicyVersion: str
        """
        self._PolicyIndex = None
        self._Description = None
        self._CidrBlock = None
        self._PolicyVersion = None

    @property
    def PolicyIndex(self):
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def PolicyVersion(self):
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion


    def _deserialize(self, params):
        self._PolicyIndex = params.get("PolicyIndex")
        self._Description = params.get("Description")
        self._CidrBlock = params.get("CidrBlock")
        self._PolicyVersion = params.get("PolicyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceAccount(AbstractModel):
    """服务级账号

    """

    def __init__(self):
        r"""
        :param _Name: 服务级账号名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Disable: 是否禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Disable: bool
        :param _ExpiresAt: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiresAt: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Permissions: 策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Permissions: list of Permission
        """
        self._Name = None
        self._Description = None
        self._Disable = None
        self._ExpiresAt = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Permissions = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Disable = params.get("Disable")
        self._ExpiresAt = params.get("ExpiresAt")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """云标签Tag

    """

    def __init__(self):
        r"""
        :param _Key: 云标签的key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 云标签的值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class TagInfo(AbstractModel):
    """镜像tag信息

    """

    def __init__(self):
        r"""
        :param _TagName: Tag名称
        :type TagName: str
        :param _TagId: 制品的 ID
        :type TagId: str
        :param _ImageId: docker image 可以看到的id
        :type ImageId: str
        :param _Size: 大小
        :type Size: str
        :param _CreationTime: 制品的创建时间
        :type CreationTime: str
        :param _DurationDays: 制品创建至今时间长度
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationDays: str
        :param _Author: 标注的制品作者
        :type Author: str
        :param _Architecture: 标注的制品平台
        :type Architecture: str
        :param _DockerVersion: 创建制品的 Docker 版本
        :type DockerVersion: str
        :param _OS: 标注的制品操作系统
        :type OS: str
        :param _SizeByte: 制品大小
        :type SizeByte: int
        :param _Id: 序号
        :type Id: int
        :param _UpdateTime: 数据更新时间
        :type UpdateTime: str
        :param _PushTime: 制品更新时间
        :type PushTime: str
        :param _Kind: 制品类型
        :type Kind: str
        """
        self._TagName = None
        self._TagId = None
        self._ImageId = None
        self._Size = None
        self._CreationTime = None
        self._DurationDays = None
        self._Author = None
        self._Architecture = None
        self._DockerVersion = None
        self._OS = None
        self._SizeByte = None
        self._Id = None
        self._UpdateTime = None
        self._PushTime = None
        self._Kind = None

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def DurationDays(self):
        return self._DurationDays

    @DurationDays.setter
    def DurationDays(self, DurationDays):
        self._DurationDays = DurationDays

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def DockerVersion(self):
        return self._DockerVersion

    @DockerVersion.setter
    def DockerVersion(self, DockerVersion):
        self._DockerVersion = DockerVersion

    @property
    def OS(self):
        return self._OS

    @OS.setter
    def OS(self, OS):
        self._OS = OS

    @property
    def SizeByte(self):
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PushTime(self):
        return self._PushTime

    @PushTime.setter
    def PushTime(self, PushTime):
        self._PushTime = PushTime

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._TagName = params.get("TagName")
        self._TagId = params.get("TagId")
        self._ImageId = params.get("ImageId")
        self._Size = params.get("Size")
        self._CreationTime = params.get("CreationTime")
        self._DurationDays = params.get("DurationDays")
        self._Author = params.get("Author")
        self._Architecture = params.get("Architecture")
        self._DockerVersion = params.get("DockerVersion")
        self._OS = params.get("OS")
        self._SizeByte = params.get("SizeByte")
        self._Id = params.get("Id")
        self._UpdateTime = params.get("UpdateTime")
        self._PushTime = params.get("PushTime")
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfoResp(AbstractModel):
    """Tag列表的返回值

    """

    def __init__(self):
        r"""
        :param _TagCount: Tag的总数
        :type TagCount: int
        :param _TagInfo: TagInfo列表
        :type TagInfo: list of TagInfo
        :param _Server: Server
        :type Server: str
        :param _RepoName: 仓库名称
        :type RepoName: str
        """
        self._TagCount = None
        self._TagInfo = None
        self._Server = None
        self._RepoName = None

    @property
    def TagCount(self):
        return self._TagCount

    @TagCount.setter
    def TagCount(self, TagCount):
        self._TagCount = TagCount

    @property
    def TagInfo(self):
        return self._TagInfo

    @TagInfo.setter
    def TagInfo(self, TagInfo):
        self._TagInfo = TagInfo

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName


    def _deserialize(self, params):
        self._TagCount = params.get("TagCount")
        if params.get("TagInfo") is not None:
            self._TagInfo = []
            for item in params.get("TagInfo"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagInfo.append(obj)
        self._Server = params.get("Server")
        self._RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """云标签

    """

    def __init__(self):
        r"""
        :param _ResourceType: 默认值为instance
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _Tags: 云标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """任务详情

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务
        :type TaskName: str
        :param _TaskUUID: 任务UUID
        :type TaskUUID: str
        :param _TaskStatus: 任务状态
        :type TaskStatus: str
        :param _TaskMessage: 任务的状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMessage: str
        :param _CreatedTime: 任务开始时间
        :type CreatedTime: str
        :param _FinishedTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedTime: str
        """
        self._TaskName = None
        self._TaskUUID = None
        self._TaskStatus = None
        self._TaskMessage = None
        self._CreatedTime = None
        self._FinishedTime = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskUUID(self):
        return self._TaskUUID

    @TaskUUID.setter
    def TaskUUID(self, TaskUUID):
        self._TaskUUID = TaskUUID

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskMessage(self):
        return self._TaskMessage

    @TaskMessage.setter
    def TaskMessage(self, TaskMessage):
        self._TaskMessage = TaskMessage

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def FinishedTime(self):
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskUUID = params.get("TaskUUID")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskMessage = params.get("TaskMessage")
        self._CreatedTime = params.get("CreatedTime")
        self._FinishedTime = params.get("FinishedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrImageInfo(AbstractModel):
    """镜像信息

    """

    def __init__(self):
        r"""
        :param _Digest: 哈希值
        :type Digest: str
        :param _Size: 镜像体积（单位：字节）
        :type Size: int
        :param _ImageVersion: Tag名称
        :type ImageVersion: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Kind: 制品类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: str
        :param _KmsSignature: KMS 签名信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsSignature: str
        """
        self._Digest = None
        self._Size = None
        self._ImageVersion = None
        self._UpdateTime = None
        self._Kind = None
        self._KmsSignature = None

    @property
    def Digest(self):
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def KmsSignature(self):
        return self._KmsSignature

    @KmsSignature.setter
    def KmsSignature(self, KmsSignature):
        self._KmsSignature = KmsSignature


    def _deserialize(self, params):
        self._Digest = params.get("Digest")
        self._Size = params.get("Size")
        self._ImageVersion = params.get("ImageVersion")
        self._UpdateTime = params.get("UpdateTime")
        self._Kind = params.get("Kind")
        self._KmsSignature = params.get("KmsSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrInstanceToken(AbstractModel):
    """实例登录令牌

    """

    def __init__(self):
        r"""
        :param _Id: 令牌ID
        :type Id: str
        :param _Desc: 令牌描述
        :type Desc: str
        :param _RegistryId: 令牌所属实例ID
        :type RegistryId: str
        :param _Enabled: 令牌启用状态
        :type Enabled: bool
        :param _CreatedAt: 令牌创建时间
        :type CreatedAt: str
        :param _ExpiredAt: 令牌过期时间戳
        :type ExpiredAt: int
        """
        self._Id = None
        self._Desc = None
        self._RegistryId = None
        self._Enabled = None
        self._CreatedAt = None
        self._ExpiredAt = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ExpiredAt(self):
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Desc = params.get("Desc")
        self._RegistryId = params.get("RegistryId")
        self._Enabled = params.get("Enabled")
        self._CreatedAt = params.get("CreatedAt")
        self._ExpiredAt = params.get("ExpiredAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrNamespaceInfo(AbstractModel):
    """Tcr 命名空间的描述

    """

    def __init__(self):
        r"""
        :param _Name: 命名空间名称
        :type Name: str
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _Public: 访问级别
        :type Public: bool
        :param _NamespaceId: 命名空间的Id
        :type NamespaceId: int
        :param _TagSpecification: 实例云标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param _Metadata: 命名空间元数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: list of KeyValueString
        :param _CVEWhitelistItems: 漏洞白名单列表
        :type CVEWhitelistItems: list of CVEWhitelistItem
        :param _AutoScan: 扫描级别，true为自动，false为手动
        :type AutoScan: bool
        :param _PreventVUL: 安全阻断级别，true为开启，false为关闭
        :type PreventVUL: bool
        :param _Severity: 阻断漏洞等级，目前仅支持low、medium、high, 为""时表示没有设置
        :type Severity: str
        """
        self._Name = None
        self._CreationTime = None
        self._Public = None
        self._NamespaceId = None
        self._TagSpecification = None
        self._Metadata = None
        self._CVEWhitelistItems = None
        self._AutoScan = None
        self._PreventVUL = None
        self._Severity = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def Metadata(self):
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def CVEWhitelistItems(self):
        return self._CVEWhitelistItems

    @CVEWhitelistItems.setter
    def CVEWhitelistItems(self, CVEWhitelistItems):
        self._CVEWhitelistItems = CVEWhitelistItems

    @property
    def AutoScan(self):
        return self._AutoScan

    @AutoScan.setter
    def AutoScan(self, AutoScan):
        self._AutoScan = AutoScan

    @property
    def PreventVUL(self):
        return self._PreventVUL

    @PreventVUL.setter
    def PreventVUL(self, PreventVUL):
        self._PreventVUL = PreventVUL

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreationTime = params.get("CreationTime")
        self._Public = params.get("Public")
        self._NamespaceId = params.get("NamespaceId")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        if params.get("Metadata") is not None:
            self._Metadata = []
            for item in params.get("Metadata"):
                obj = KeyValueString()
                obj._deserialize(item)
                self._Metadata.append(obj)
        if params.get("CVEWhitelistItems") is not None:
            self._CVEWhitelistItems = []
            for item in params.get("CVEWhitelistItems"):
                obj = CVEWhitelistItem()
                obj._deserialize(item)
                self._CVEWhitelistItems.append(obj)
        self._AutoScan = params.get("AutoScan")
        self._PreventVUL = params.get("PreventVUL")
        self._Severity = params.get("Severity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrRepositoryInfo(AbstractModel):
    """Tcr镜像仓库信息

    """

    def __init__(self):
        r"""
        :param _Name: 仓库名称
        :type Name: str
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _CreationTime: 创建时间，格式"2006-01-02 15:04:05.999999999 -0700 MST"
        :type CreationTime: str
        :param _Public: 是否公开
        :type Public: bool
        :param _Description: 仓库详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _BriefDescription: 简单描述
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefDescription: str
        :param _UpdateTime: 更新时间，格式"2006-01-02 15:04:05.999999999 -0700 MST"
        :type UpdateTime: str
        """
        self._Name = None
        self._Namespace = None
        self._CreationTime = None
        self._Public = None
        self._Description = None
        self._BriefDescription = None
        self._UpdateTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def BriefDescription(self):
        return self._BriefDescription

    @BriefDescription.setter
    def BriefDescription(self, BriefDescription):
        self._BriefDescription = BriefDescription

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._CreationTime = params.get("CreationTime")
        self._Public = params.get("Public")
        self._Description = params.get("Description")
        self._BriefDescription = params.get("BriefDescription")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInvokeCondition(AbstractModel):
    """触发器触发条件

    """

    def __init__(self):
        r"""
        :param _InvokeMethod: 触发方式
        :type InvokeMethod: str
        :param _InvokeExpr: 触发表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeExpr: str
        """
        self._InvokeMethod = None
        self._InvokeExpr = None

    @property
    def InvokeMethod(self):
        return self._InvokeMethod

    @InvokeMethod.setter
    def InvokeMethod(self, InvokeMethod):
        self._InvokeMethod = InvokeMethod

    @property
    def InvokeExpr(self):
        return self._InvokeExpr

    @InvokeExpr.setter
    def InvokeExpr(self, InvokeExpr):
        self._InvokeExpr = InvokeExpr


    def _deserialize(self, params):
        self._InvokeMethod = params.get("InvokeMethod")
        self._InvokeExpr = params.get("InvokeExpr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInvokePara(AbstractModel):
    """触发器触发参数

    """

    def __init__(self):
        r"""
        :param _AppId: AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _ClusterId: TKE集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Namespace: TKE集群命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _ServiceName: TKE集群工作负载名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _ContainerName: TKE集群工作负载中容器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param _ClusterRegion: TKE集群地域数字ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterRegion: int
        """
        self._AppId = None
        self._ClusterId = None
        self._Namespace = None
        self._ServiceName = None
        self._ContainerName = None
        self._ClusterRegion = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ContainerName(self):
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def ClusterRegion(self):
        return self._ClusterRegion

    @ClusterRegion.setter
    def ClusterRegion(self, ClusterRegion):
        self._ClusterRegion = ClusterRegion


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._ServiceName = params.get("ServiceName")
        self._ContainerName = params.get("ContainerName")
        self._ClusterRegion = params.get("ClusterRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInvokeResult(AbstractModel):
    """触发器触发结果

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 请求TKE返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: int
        :param _ReturnMsg: 请求TKE返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnMsg: str
        """
        self._ReturnCode = None
        self._ReturnMsg = None

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerLogResp(AbstractModel):
    """触发器日志

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param _TagName: Tag名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param _TriggerName: 触发器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param _InvokeSource: 触发方式
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeSource: str
        :param _InvokeAction: 触发动作
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeAction: str
        :param _InvokeTime: 触发时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeTime: str
        :param _InvokeCondition: 触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeCondition: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeCondition`
        :param _InvokePara: 触发参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokePara: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokePara`
        :param _InvokeResult: 触发结果
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeResult: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeResult`
        """
        self._RepoName = None
        self._TagName = None
        self._TriggerName = None
        self._InvokeSource = None
        self._InvokeAction = None
        self._InvokeTime = None
        self._InvokeCondition = None
        self._InvokePara = None
        self._InvokeResult = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def InvokeSource(self):
        return self._InvokeSource

    @InvokeSource.setter
    def InvokeSource(self, InvokeSource):
        self._InvokeSource = InvokeSource

    @property
    def InvokeAction(self):
        return self._InvokeAction

    @InvokeAction.setter
    def InvokeAction(self, InvokeAction):
        self._InvokeAction = InvokeAction

    @property
    def InvokeTime(self):
        return self._InvokeTime

    @InvokeTime.setter
    def InvokeTime(self, InvokeTime):
        self._InvokeTime = InvokeTime

    @property
    def InvokeCondition(self):
        return self._InvokeCondition

    @InvokeCondition.setter
    def InvokeCondition(self, InvokeCondition):
        self._InvokeCondition = InvokeCondition

    @property
    def InvokePara(self):
        return self._InvokePara

    @InvokePara.setter
    def InvokePara(self, InvokePara):
        self._InvokePara = InvokePara

    @property
    def InvokeResult(self):
        return self._InvokeResult

    @InvokeResult.setter
    def InvokeResult(self, InvokeResult):
        self._InvokeResult = InvokeResult


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        self._TagName = params.get("TagName")
        self._TriggerName = params.get("TriggerName")
        self._InvokeSource = params.get("InvokeSource")
        self._InvokeAction = params.get("InvokeAction")
        self._InvokeTime = params.get("InvokeTime")
        if params.get("InvokeCondition") is not None:
            self._InvokeCondition = TriggerInvokeCondition()
            self._InvokeCondition._deserialize(params.get("InvokeCondition"))
        if params.get("InvokePara") is not None:
            self._InvokePara = TriggerInvokePara()
            self._InvokePara._deserialize(params.get("InvokePara"))
        if params.get("InvokeResult") is not None:
            self._InvokeResult = TriggerInvokeResult()
            self._InvokeResult._deserialize(params.get("InvokeResult"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerResp(AbstractModel):
    """触发器返回值

    """

    def __init__(self):
        r"""
        :param _TriggerName: 触发器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param _InvokeSource: 触发来源
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeSource: str
        :param _InvokeAction: 触发动作
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeAction: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _InvokeCondition: 触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeCondition: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeCondition`
        :param _InvokePara: 触发器参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokePara: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokePara`
        """
        self._TriggerName = None
        self._InvokeSource = None
        self._InvokeAction = None
        self._CreateTime = None
        self._UpdateTime = None
        self._InvokeCondition = None
        self._InvokePara = None

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def InvokeSource(self):
        return self._InvokeSource

    @InvokeSource.setter
    def InvokeSource(self, InvokeSource):
        self._InvokeSource = InvokeSource

    @property
    def InvokeAction(self):
        return self._InvokeAction

    @InvokeAction.setter
    def InvokeAction(self, InvokeAction):
        self._InvokeAction = InvokeAction

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InvokeCondition(self):
        return self._InvokeCondition

    @InvokeCondition.setter
    def InvokeCondition(self, InvokeCondition):
        self._InvokeCondition = InvokeCondition

    @property
    def InvokePara(self):
        return self._InvokePara

    @InvokePara.setter
    def InvokePara(self, InvokePara):
        self._InvokePara = InvokePara


    def _deserialize(self, params):
        self._TriggerName = params.get("TriggerName")
        self._InvokeSource = params.get("InvokeSource")
        self._InvokeAction = params.get("InvokeAction")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("InvokeCondition") is not None:
            self._InvokeCondition = TriggerInvokeCondition()
            self._InvokeCondition._deserialize(params.get("InvokeCondition"))
        if params.get("InvokePara") is not None:
            self._InvokePara = TriggerInvokePara()
            self._InvokePara._deserialize(params.get("InvokePara"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValidateNamespaceExistPersonalRequest(AbstractModel):
    """ValidateNamespaceExistPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名称
        :type Namespace: str
        """
        self._Namespace = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValidateNamespaceExistPersonalResponse(AbstractModel):
    """ValidateNamespaceExistPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 验证命名空间是否存在返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.NamespaceIsExistsResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = NamespaceIsExistsResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ValidateRepositoryExistPersonalRequest(AbstractModel):
    """ValidateRepositoryExistPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RepoName: 仓库名称
        :type RepoName: str
        """
        self._RepoName = None

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName


    def _deserialize(self, params):
        self._RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValidateRepositoryExistPersonalResponse(AbstractModel):
    """ValidateRepositoryExistPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 验证个人版仓库是否存在返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepoIsExistResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RepoIsExistResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VpcAndDomainInfo(AbstractModel):
    """vpc和domain信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: tcr实例id
        :type InstanceId: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _EniLBIp: tcr内网访问链路ip
        :type EniLBIp: str
        :param _UsePublicDomain: true：use instance name as subdomain
false: use instancename+"-vpc" as subdomain
        :type UsePublicDomain: bool
        :param _RegionName: 解析地域，需要保证和vpc处于同一地域，如果不填则默认为主实例地域
        :type RegionName: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._EniLBIp = None
        self._UsePublicDomain = None
        self._RegionName = None

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
    def EniLBIp(self):
        return self._EniLBIp

    @EniLBIp.setter
    def EniLBIp(self, EniLBIp):
        self._EniLBIp = EniLBIp

    @property
    def UsePublicDomain(self):
        return self._UsePublicDomain

    @UsePublicDomain.setter
    def UsePublicDomain(self, UsePublicDomain):
        self._UsePublicDomain = UsePublicDomain

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._EniLBIp = params.get("EniLBIp")
        self._UsePublicDomain = params.get("UsePublicDomain")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcPrivateDomainStatus(AbstractModel):
    """vpc私有域名解析状态

    """

    def __init__(self):
        r"""
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _VpcId: unique vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _Status: ENABLE代表已经开启，DISABLE代表未开启，ERROR代表查询出错
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Region = None
        self._VpcId = None
        self._Status = None

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

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTarget(AbstractModel):
    """触发器目标

    """

    def __init__(self):
        r"""
        :param _Address: 目标地址
        :type Address: str
        :param _Headers: 自定义 Headers
        :type Headers: list of Header
        """
        self._Address = None
        self._Headers = None

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Address = params.get("Address")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTrigger(AbstractModel):
    """Webhook 触发器

    """

    def __init__(self):
        r"""
        :param _Name: 触发器名称
        :type Name: str
        :param _Targets: 触发器目标
        :type Targets: list of WebhookTarget
        :param _EventTypes: 触发动作
        :type EventTypes: list of str
        :param _Condition: 触发规则
        :type Condition: str
        :param _Enabled: 启用触发器
        :type Enabled: bool
        :param _Id: 触发器Id
        :type Id: int
        :param _Description: 触发器描述
        :type Description: str
        :param _NamespaceId: 触发器所属命名空间 Id
        :type NamespaceId: int
        """
        self._Name = None
        self._Targets = None
        self._EventTypes = None
        self._Condition = None
        self._Enabled = None
        self._Id = None
        self._Description = None
        self._NamespaceId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EventTypes(self):
        return self._EventTypes

    @EventTypes.setter
    def EventTypes(self, EventTypes):
        self._EventTypes = EventTypes

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = WebhookTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._EventTypes = params.get("EventTypes")
        self._Condition = params.get("Condition")
        self._Enabled = params.get("Enabled")
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._NamespaceId = params.get("NamespaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTriggerLog(AbstractModel):
    """触发器日志

    """

    def __init__(self):
        r"""
        :param _Id: 日志 Id
        :type Id: int
        :param _TriggerId: 触发器 Id
        :type TriggerId: int
        :param _EventType: 事件类型
        :type EventType: str
        :param _NotifyType: 通知类型
        :type NotifyType: str
        :param _Detail: 详情
        :type Detail: str
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Status: 状态
        :type Status: str
        """
        self._Id = None
        self._TriggerId = None
        self._EventType = None
        self._NotifyType = None
        self._Detail = None
        self._CreationTime = None
        self._UpdateTime = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TriggerId(self):
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TriggerId = params.get("TriggerId")
        self._EventType = params.get("EventType")
        self._NotifyType = params.get("NotifyType")
        self._Detail = params.get("Detail")
        self._CreationTime = params.get("CreationTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        