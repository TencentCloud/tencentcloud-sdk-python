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


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 要绑定的安全组 ID，类似sg-efil7***。
        :type SecurityGroupIds: list of str
        :param _InstanceIds: 实例 ID，格式如：vdb-c1nl9***，支持指定多个实例
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        """要绑定的安全组 ID，类似sg-efil7***。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        """实例 ID，格式如：vdb-c1nl9***，支持指定多个实例
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _VpcId: 私有网络 ID。
        :type VpcId: str
        :param _SubnetId: 私有网络 VPC 的子网 ID。
        :type SubnetId: str
        :param _PayMode: 指定实例计费方式。
- 0：按量付费。
- 1：包年包月。
        :type PayMode: int
        :param _InstanceName: 设置实例名称。仅支持长度不超过 60 的中文/英文/数字/-/_。
        :type InstanceName: str
        :param _SecurityGroupIds: 安全组 ID。
        :type SecurityGroupIds: list of str
        :param _PayPeriod: 若计费方式为包年包月，指定包年包月续费的时长。
- 单位：月。
- 取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。默认为1。
        :type PayPeriod: int
        :param _AutoRenew: 若为包年包月计费，需指定是否开启自动续费。
- 0：不开启自动续费。
- 1：开启自动续费。
        :type AutoRenew: int
        :param _Params: 实例额外参数，通过json提交。
        :type Params: str
        :param _ResourceTags: 以数组形式列出标签信息。
        :type ResourceTags: list of Tag
        :param _Project: 指定实例所属项目 ID。
        :type Project: str
        :param _InstanceType: 实例类型。
- base：免费测试版。
- single：单机版。
- cluster：高可用版。
        :type InstanceType: str
        :param _Mode: 实例类型为高可用版，需指定可用区选项。
- two：两可用区。
- three：三可用区。
        :type Mode: str
        :param _GoodsNum: 购买实例数量。
        :type GoodsNum: int
        :param _NetworkType: 网络类型。
VPC或TCS
        :type NetworkType: str
        :param _TemplateId: 实例所应用的参数模板 ID。
        :type TemplateId: str
        :param _Components: 组件具体设置列表。
        :type Components: list of CreateInstancesComponent
        :param _Zone: 实例类型为高可用版，通过该参数指定主可用区。
        :type Zone: str
        :param _SlaveZones: 实例类型为高可用版，通过该参数指定备可用区。
        :type SlaveZones: list of str
        :param _IsNoExpired: 是否长期有效
        :type IsNoExpired: bool
        :param _EngineName: 引擎名称，业务自定义。
        :type EngineName: str
        :param _EngineVersion: 引擎版本，业务自定义。
        :type EngineVersion: str
        :param _Brief: 实例描述。
        :type Brief: str
        :param _Chief: 负责人信息。
        :type Chief: str
        :param _DBA: DBA人员信息
        :type DBA: str
        :param _NodeType: 指定实例的节点类型。具体信息，请参见[选择节点类型](https://cloud.tencent.com/document/product/1709/113399)。
- compute：计费型。
- normal：标准型。
- store：存储型。
        :type NodeType: str
        :param _Cpu: 指定实例所需的 CPU 核数。实例类型不同，支持的 CPU 核数存在差异。
- 计算型： 1、2、4、8、16、24、32。
- 标准型： 1、2、4、8、12、16。
- 存储型： 1、2、4、6、8。
        :type Cpu: int
        :param _Memory: 指定实例所需的内存大小。单位：GB。选择具体规格，请参见[配置规格（选型）](https://cloud.tencent.com/document/product/1709/113399)。
        :type Memory: int
        :param _DiskSize: 指定实例所需的磁盘大小，单位：GB。选择具体规格，请参见[配置规格（选型）](https://cloud.tencent.com/document/product/1709/113399)。
        :type DiskSize: int
        :param _WorkerNodeNum: 指定实例所需配置的节点数量。选择方法，请参见[配置规格（选型）](https://cloud.tencent.com/document/product/1709/113399)。
        :type WorkerNodeNum: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._InstanceName = None
        self._SecurityGroupIds = None
        self._PayPeriod = None
        self._AutoRenew = None
        self._Params = None
        self._ResourceTags = None
        self._Project = None
        self._InstanceType = None
        self._Mode = None
        self._GoodsNum = None
        self._NetworkType = None
        self._TemplateId = None
        self._Components = None
        self._Zone = None
        self._SlaveZones = None
        self._IsNoExpired = None
        self._EngineName = None
        self._EngineVersion = None
        self._Brief = None
        self._Chief = None
        self._DBA = None
        self._NodeType = None
        self._Cpu = None
        self._Memory = None
        self._DiskSize = None
        self._WorkerNodeNum = None

    @property
    def VpcId(self):
        """私有网络 ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络 VPC 的子网 ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PayMode(self):
        """指定实例计费方式。
- 0：按量付费。
- 1：包年包月。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceName(self):
        """设置实例名称。仅支持长度不超过 60 的中文/英文/数字/-/_。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SecurityGroupIds(self):
        """安全组 ID。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def PayPeriod(self):
        """若计费方式为包年包月，指定包年包月续费的时长。
- 单位：月。
- 取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。默认为1。
        :rtype: int
        """
        return self._PayPeriod

    @PayPeriod.setter
    def PayPeriod(self, PayPeriod):
        self._PayPeriod = PayPeriod

    @property
    def AutoRenew(self):
        """若为包年包月计费，需指定是否开启自动续费。
- 0：不开启自动续费。
- 1：开启自动续费。
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Params(self):
        """实例额外参数，通过json提交。
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def ResourceTags(self):
        """以数组形式列出标签信息。
        :rtype: list of Tag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Project(self):
        warnings.warn("parameter `Project` is deprecated", DeprecationWarning) 

        """指定实例所属项目 ID。
        :rtype: str
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        warnings.warn("parameter `Project` is deprecated", DeprecationWarning) 

        self._Project = Project

    @property
    def InstanceType(self):
        """实例类型。
- base：免费测试版。
- single：单机版。
- cluster：高可用版。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Mode(self):
        """实例类型为高可用版，需指定可用区选项。
- two：两可用区。
- three：三可用区。
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def GoodsNum(self):
        """购买实例数量。
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def NetworkType(self):
        warnings.warn("parameter `NetworkType` is deprecated", DeprecationWarning) 

        """网络类型。
VPC或TCS
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        warnings.warn("parameter `NetworkType` is deprecated", DeprecationWarning) 

        self._NetworkType = NetworkType

    @property
    def TemplateId(self):
        warnings.warn("parameter `TemplateId` is deprecated", DeprecationWarning) 

        """实例所应用的参数模板 ID。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        warnings.warn("parameter `TemplateId` is deprecated", DeprecationWarning) 

        self._TemplateId = TemplateId

    @property
    def Components(self):
        warnings.warn("parameter `Components` is deprecated", DeprecationWarning) 

        """组件具体设置列表。
        :rtype: list of CreateInstancesComponent
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        warnings.warn("parameter `Components` is deprecated", DeprecationWarning) 

        self._Components = Components

    @property
    def Zone(self):
        warnings.warn("parameter `Zone` is deprecated", DeprecationWarning) 

        """实例类型为高可用版，通过该参数指定主可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        warnings.warn("parameter `Zone` is deprecated", DeprecationWarning) 

        self._Zone = Zone

    @property
    def SlaveZones(self):
        warnings.warn("parameter `SlaveZones` is deprecated", DeprecationWarning) 

        """实例类型为高可用版，通过该参数指定备可用区。
        :rtype: list of str
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        warnings.warn("parameter `SlaveZones` is deprecated", DeprecationWarning) 

        self._SlaveZones = SlaveZones

    @property
    def IsNoExpired(self):
        warnings.warn("parameter `IsNoExpired` is deprecated", DeprecationWarning) 

        """是否长期有效
        :rtype: bool
        """
        return self._IsNoExpired

    @IsNoExpired.setter
    def IsNoExpired(self, IsNoExpired):
        warnings.warn("parameter `IsNoExpired` is deprecated", DeprecationWarning) 

        self._IsNoExpired = IsNoExpired

    @property
    def EngineName(self):
        warnings.warn("parameter `EngineName` is deprecated", DeprecationWarning) 

        """引擎名称，业务自定义。
        :rtype: str
        """
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        warnings.warn("parameter `EngineName` is deprecated", DeprecationWarning) 

        self._EngineName = EngineName

    @property
    def EngineVersion(self):
        warnings.warn("parameter `EngineVersion` is deprecated", DeprecationWarning) 

        """引擎版本，业务自定义。
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        warnings.warn("parameter `EngineVersion` is deprecated", DeprecationWarning) 

        self._EngineVersion = EngineVersion

    @property
    def Brief(self):
        warnings.warn("parameter `Brief` is deprecated", DeprecationWarning) 

        """实例描述。
        :rtype: str
        """
        return self._Brief

    @Brief.setter
    def Brief(self, Brief):
        warnings.warn("parameter `Brief` is deprecated", DeprecationWarning) 

        self._Brief = Brief

    @property
    def Chief(self):
        warnings.warn("parameter `Chief` is deprecated", DeprecationWarning) 

        """负责人信息。
        :rtype: str
        """
        return self._Chief

    @Chief.setter
    def Chief(self, Chief):
        warnings.warn("parameter `Chief` is deprecated", DeprecationWarning) 

        self._Chief = Chief

    @property
    def DBA(self):
        warnings.warn("parameter `DBA` is deprecated", DeprecationWarning) 

        """DBA人员信息
        :rtype: str
        """
        return self._DBA

    @DBA.setter
    def DBA(self, DBA):
        warnings.warn("parameter `DBA` is deprecated", DeprecationWarning) 

        self._DBA = DBA

    @property
    def NodeType(self):
        warnings.warn("parameter `NodeType` is deprecated", DeprecationWarning) 

        """指定实例的节点类型。具体信息，请参见[选择节点类型](https://cloud.tencent.com/document/product/1709/113399)。
- compute：计费型。
- normal：标准型。
- store：存储型。
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        warnings.warn("parameter `NodeType` is deprecated", DeprecationWarning) 

        self._NodeType = NodeType

    @property
    def Cpu(self):
        """指定实例所需的 CPU 核数。实例类型不同，支持的 CPU 核数存在差异。
- 计算型： 1、2、4、8、16、24、32。
- 标准型： 1、2、4、8、12、16。
- 存储型： 1、2、4、6、8。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """指定实例所需的内存大小。单位：GB。选择具体规格，请参见[配置规格（选型）](https://cloud.tencent.com/document/product/1709/113399)。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskSize(self):
        """指定实例所需的磁盘大小，单位：GB。选择具体规格，请参见[配置规格（选型）](https://cloud.tencent.com/document/product/1709/113399)。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def WorkerNodeNum(self):
        """指定实例所需配置的节点数量。选择方法，请参见[配置规格（选型）](https://cloud.tencent.com/document/product/1709/113399)。
        :rtype: int
        """
        return self._WorkerNodeNum

    @WorkerNodeNum.setter
    def WorkerNodeNum(self, WorkerNodeNum):
        self._WorkerNodeNum = WorkerNodeNum


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._InstanceName = params.get("InstanceName")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._PayPeriod = params.get("PayPeriod")
        self._AutoRenew = params.get("AutoRenew")
        self._Params = params.get("Params")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Project = params.get("Project")
        self._InstanceType = params.get("InstanceType")
        self._Mode = params.get("Mode")
        self._GoodsNum = params.get("GoodsNum")
        self._NetworkType = params.get("NetworkType")
        self._TemplateId = params.get("TemplateId")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = CreateInstancesComponent()
                obj._deserialize(item)
                self._Components.append(obj)
        self._Zone = params.get("Zone")
        self._SlaveZones = params.get("SlaveZones")
        self._IsNoExpired = params.get("IsNoExpired")
        self._EngineName = params.get("EngineName")
        self._EngineVersion = params.get("EngineVersion")
        self._Brief = params.get("Brief")
        self._Chief = params.get("Chief")
        self._DBA = params.get("DBA")
        self._NodeType = params.get("NodeType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._DiskSize = params.get("DiskSize")
        self._WorkerNodeNum = params.get("WorkerNodeNum")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateInstancesComponent(AbstractModel):
    """组件设置列表

    """

    def __init__(self):
        r"""
        :param _Component: 底层组件名，需要和产品模型中的保持一致
        :type Component: str
        :param _Cpu: 组件cpu大小
        :type Cpu: float
        :param _Memory: 组件内存大小
        :type Memory: float
        :param _ReplicaNum: 业务节点数
        :type ReplicaNum: int
        :param _Name: 自定义组件名
        :type Name: str
        :param _StorageSize: 组件磁盘大小
        :type StorageSize: int
        :param _StorageType: 磁盘类型
        :type StorageType: str
        :param _Params: 组件额外参数，通过JSON提交
        :type Params: str
        """
        self._Component = None
        self._Cpu = None
        self._Memory = None
        self._ReplicaNum = None
        self._Name = None
        self._StorageSize = None
        self._StorageType = None
        self._Params = None

    @property
    def Component(self):
        """底层组件名，需要和产品模型中的保持一致
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Cpu(self):
        """组件cpu大小
        :rtype: float
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """组件内存大小
        :rtype: float
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def ReplicaNum(self):
        """业务节点数
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def Name(self):
        """自定义组件名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StorageSize(self):
        """组件磁盘大小
        :rtype: int
        """
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def StorageType(self):
        """磁盘类型
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Params(self):
        """组件额外参数，通过JSON提交
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._Component = params.get("Component")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._ReplicaNum = params.get("ReplicaNum")
        self._Name = params.get("Name")
        self._StorageSize = params.get("StorageSize")
        self._StorageType = params.get("StorageType")
        self._Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：vdb-c1nl9***。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID，格式如：vdb-c1nl9***。
        :rtype: str
        """
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
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of SecurityGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        """安全组规则。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMaintenanceWindowRequest(AbstractModel):
    """DescribeInstanceMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定查询维护时间窗的具体实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """指定查询维护时间窗的具体实例 ID。
        :rtype: str
        """
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
        


class DescribeInstanceMaintenanceWindowResponse(AbstractModel):
    """DescribeInstanceMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _StartTime: 维护时间窗开始时间。
        :type StartTime: str
        :param _EndTime: 维护时间窗结束时间。
        :type EndTime: str
        :param _TimeSpan: 维护时间窗时长。单位：小时。
        :type TimeSpan: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._TimeSpan = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """维护时间窗开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """维护时间窗结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TimeSpan(self):
        """维护时间窗时长。单位：小时。
        :rtype: float
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TimeSpan = params.get("TimeSpan")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRequest(AbstractModel):
    """DescribeInstanceNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Limit: limit
        :type Limit: int
        :param _Offset: offset
        :type Offset: int
        :param _Component: component
        :type Component: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._Component = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Component(self):
        """component
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Component = params.get("Component")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesResponse(AbstractModel):
    """DescribeInstanceNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 实例pod列表。
        :type Items: list of NodeInfo
        :param _TotalCount: 查询结果总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """实例pod列表。
        :rtype: list of NodeInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """查询结果总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID数组。
        :type InstanceIds: list of str
        :param _InstanceNames: 实例名称，支持模糊搜索。
        :type InstanceNames: list of str
        :param _InstanceKeys: 实例模糊搜索字段。
        :type InstanceKeys: list of str
        :param _Status: 根据状态获取实例， 为空则获取全部非隔离和非下线的实例。
        :type Status: list of str
        :param _EngineNames: 按照引擎筛选实例。
        :type EngineNames: list of str
        :param _EngineVersions: 按照版本筛选实例。
        :type EngineVersions: list of str
        :param _ApiVersions: 按照api版本筛选实例
        :type ApiVersions: list of str
        :param _CreateAt: 按照创建时间筛选实例。
        :type CreateAt: str
        :param _Zones: 按照可用区筛选实例。
        :type Zones: list of str
        :param _OrderBy: 排序字段。
        :type OrderBy: str
        :param _OrderDirection: 排序方式。
        :type OrderDirection: str
        :param _Offset: 查询开始位置。
        :type Offset: int
        :param _Limit: 列表查询数量。
        :type Limit: int
        :param _ResourceTags: 按照标签筛选实例
        :type ResourceTags: list of Tag
        :param _TaskStatus: 任务状态：1-待执行任务；2-密钥更新中；3-网络变更中；4-参数变更中；5-embedding变更中；6-ai套件变更中；7-滚动升级中；8-纵向扩容中；9-纵向缩容中；10-横向扩容中；11-横向缩容中
        :type TaskStatus: list of int
        """
        self._InstanceIds = None
        self._InstanceNames = None
        self._InstanceKeys = None
        self._Status = None
        self._EngineNames = None
        self._EngineVersions = None
        self._ApiVersions = None
        self._CreateAt = None
        self._Zones = None
        self._OrderBy = None
        self._OrderDirection = None
        self._Offset = None
        self._Limit = None
        self._ResourceTags = None
        self._TaskStatus = None

    @property
    def InstanceIds(self):
        """实例ID数组。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        """实例名称，支持模糊搜索。
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def InstanceKeys(self):
        """实例模糊搜索字段。
        :rtype: list of str
        """
        return self._InstanceKeys

    @InstanceKeys.setter
    def InstanceKeys(self, InstanceKeys):
        self._InstanceKeys = InstanceKeys

    @property
    def Status(self):
        """根据状态获取实例， 为空则获取全部非隔离和非下线的实例。
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EngineNames(self):
        warnings.warn("parameter `EngineNames` is deprecated", DeprecationWarning) 

        """按照引擎筛选实例。
        :rtype: list of str
        """
        return self._EngineNames

    @EngineNames.setter
    def EngineNames(self, EngineNames):
        warnings.warn("parameter `EngineNames` is deprecated", DeprecationWarning) 

        self._EngineNames = EngineNames

    @property
    def EngineVersions(self):
        """按照版本筛选实例。
        :rtype: list of str
        """
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def ApiVersions(self):
        """按照api版本筛选实例
        :rtype: list of str
        """
        return self._ApiVersions

    @ApiVersions.setter
    def ApiVersions(self, ApiVersions):
        self._ApiVersions = ApiVersions

    @property
    def CreateAt(self):
        """按照创建时间筛选实例。
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def Zones(self):
        warnings.warn("parameter `Zones` is deprecated", DeprecationWarning) 

        """按照可用区筛选实例。
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        warnings.warn("parameter `Zones` is deprecated", DeprecationWarning) 

        self._Zones = Zones

    @property
    def OrderBy(self):
        """排序字段。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        """排序方式。
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def Offset(self):
        """查询开始位置。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """列表查询数量。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourceTags(self):
        """按照标签筛选实例
        :rtype: list of Tag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def TaskStatus(self):
        """任务状态：1-待执行任务；2-密钥更新中；3-网络变更中；4-参数变更中；5-embedding变更中；6-ai套件变更中；7-滚动升级中；8-纵向扩容中；9-纵向缩容中；10-横向扩容中；11-横向缩容中
        :rtype: list of int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._InstanceKeys = params.get("InstanceKeys")
        self._Status = params.get("Status")
        self._EngineNames = params.get("EngineNames")
        self._EngineVersions = params.get("EngineVersions")
        self._ApiVersions = params.get("ApiVersions")
        self._CreateAt = params.get("CreateAt")
        self._Zones = params.get("Zones")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._TaskStatus = params.get("TaskStatus")
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
        :param _Items: 实例列表。
        :type Items: list of InstanceInfo
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """实例列表。
        :rtype: list of InstanceInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """实例总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DestroyInstancesRequest(AbstractModel):
    """DestroyInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 以数组形式指定待销毁下线的实例 ID。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        """以数组形式指定待销毁下线的实例 ID。
        :rtype: list of str
        """
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
        


class DestroyInstancesResponse(AbstractModel):
    """DestroyInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 要绑定的安全组 ID，类似sg-efil****。
        :type SecurityGroupIds: str
        :param _InstanceIds: 实例 ID，格式如：vdb-c1nl****，支持指定多个实例。
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        """要绑定的安全组 ID，类似sg-efil****。
        :rtype: str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        """实例 ID，格式如：vdb-c1nl****，支持指定多个实例。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Inbound(AbstractModel):
    """安全组入站规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT或者DROP。
        :type Action: str
        :param _AddressModule: 地址组id代表的地址集合。
        :type AddressModule: str
        :param _CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。
        :type CidrIp: str
        :param _Desc: 描述。
        :type Desc: str
        :param _IpProtocol: 网络协议，支持udp、tcp等。
        :type IpProtocol: str
        :param _PortRange: 端口。
        :type PortRange: str
        :param _ServiceModule: 服务组id代表的协议和端口集合。
        :type ServiceModule: str
        :param _Id: 安全组id代表的地址集合。
        :type Id: str
        """
        self._Action = None
        self._AddressModule = None
        self._CidrIp = None
        self._Desc = None
        self._IpProtocol = None
        self._PortRange = None
        self._ServiceModule = None
        self._Id = None

    @property
    def Action(self):
        """策略，ACCEPT或者DROP。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        """地址组id代表的地址集合。
        :rtype: str
        """
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        """来源Ip或Ip段，例如192.168.0.0/16。
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        """描述。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        """网络协议，支持udp、tcp等。
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        """端口。
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        """服务组id代表的协议和端口集合。
        :rtype: str
        """
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
        """安全组id代表的地址集合。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._AddressModule = params.get("AddressModule")
        self._CidrIp = params.get("CidrIp")
        self._Desc = params.get("Desc")
        self._IpProtocol = params.get("IpProtocol")
        self._PortRange = params.get("PortRange")
        self._ServiceModule = params.get("ServiceModule")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例信息，用于实例列表

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Name: 实例自定义名称。
        :type Name: str
        :param _AppId: 用户APPID。
        :type AppId: int
        :param _Region: 地域。
        :type Region: str
        :param _Zone: 可用区。
        :type Zone: str
        :param _Product: 产品。
        :type Product: str
        :param _Networks: 网络信息。
        :type Networks: list of Network
        :param _ShardNum: 分片信息。
        :type ShardNum: int
        :param _ReplicaNum: 副本数。
        :type ReplicaNum: int
        :param _Cpu: CPU.
        :type Cpu: float
        :param _Memory: 内存。
        :type Memory: float
        :param _Disk: 磁盘。
        :type Disk: int
        :param _HealthScore: 健康得分。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthScore: float
        :param _Warning: 异常告警。
注意：此字段可能返回 null，表示取不到有效值。
        :type Warning: int
        :param _Project: 所属项目。
注意：此字段可能返回 null，表示取不到有效值。
        :type Project: str
        :param _ResourceTags: 所属标签。
        :type ResourceTags: list of Tag
        :param _CreatedAt: 创建时间。
        :type CreatedAt: str
        :param _Status: 资源状态。
        :type Status: str
        :param _EngineName: 引擎名称。
        :type EngineName: str
        :param _EngineVersion: 引擎版本。
        :type EngineVersion: str
        :param _ApiVersion: api版本
        :type ApiVersion: str
        :param _PayMode: 计费模式。
        :type PayMode: int
        :param _Extend: 差异化扩展信息, json格式。
        :type Extend: str
        :param _ExpiredAt: 过期时间。
        :type ExpiredAt: str
        :param _IsNoExpired: 是否不过期(永久)。
        :type IsNoExpired: bool
        :param _WanAddress: 外网地址。
        :type WanAddress: str
        :param _IsolateAt: 隔离时间
        :type IsolateAt: str
        :param _AutoRenew: 是否自动续费。0: 不自动续费(可以支持特权不停服)；1:自动续费；2:到期不续费.
        :type AutoRenew: int
        :param _TaskStatus: 任务状态：0-无任务；1-待执行任务；2-密钥更新中；3-网络变更中；4-参数变更中；5-embedding变更中；6-ai套件变更中；7-滚动升级中；8-纵向扩容中；9-纵向缩容中；10-横向扩容中；11-横向缩容中
        :type TaskStatus: int
        """
        self._InstanceId = None
        self._Name = None
        self._AppId = None
        self._Region = None
        self._Zone = None
        self._Product = None
        self._Networks = None
        self._ShardNum = None
        self._ReplicaNum = None
        self._Cpu = None
        self._Memory = None
        self._Disk = None
        self._HealthScore = None
        self._Warning = None
        self._Project = None
        self._ResourceTags = None
        self._CreatedAt = None
        self._Status = None
        self._EngineName = None
        self._EngineVersion = None
        self._ApiVersion = None
        self._PayMode = None
        self._Extend = None
        self._ExpiredAt = None
        self._IsNoExpired = None
        self._WanAddress = None
        self._IsolateAt = None
        self._AutoRenew = None
        self._TaskStatus = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """实例自定义名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppId(self):
        """用户APPID。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        """地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Product(self):
        """产品。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Networks(self):
        """网络信息。
        :rtype: list of Network
        """
        return self._Networks

    @Networks.setter
    def Networks(self, Networks):
        self._Networks = Networks

    @property
    def ShardNum(self):
        """分片信息。
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def ReplicaNum(self):
        """副本数。
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def Cpu(self):
        """CPU.
        :rtype: float
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存。
        :rtype: float
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        """磁盘。
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def HealthScore(self):
        warnings.warn("parameter `HealthScore` is deprecated", DeprecationWarning) 

        """健康得分。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        warnings.warn("parameter `HealthScore` is deprecated", DeprecationWarning) 

        self._HealthScore = HealthScore

    @property
    def Warning(self):
        warnings.warn("parameter `Warning` is deprecated", DeprecationWarning) 

        """异常告警。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Warning

    @Warning.setter
    def Warning(self, Warning):
        warnings.warn("parameter `Warning` is deprecated", DeprecationWarning) 

        self._Warning = Warning

    @property
    def Project(self):
        warnings.warn("parameter `Project` is deprecated", DeprecationWarning) 

        """所属项目。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        warnings.warn("parameter `Project` is deprecated", DeprecationWarning) 

        self._Project = Project

    @property
    def ResourceTags(self):
        """所属标签。
        :rtype: list of Tag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def CreatedAt(self):
        """创建时间。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Status(self):
        """资源状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EngineName(self):
        """引擎名称。
        :rtype: str
        """
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def EngineVersion(self):
        """引擎版本。
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def ApiVersion(self):
        """api版本
        :rtype: str
        """
        return self._ApiVersion

    @ApiVersion.setter
    def ApiVersion(self, ApiVersion):
        self._ApiVersion = ApiVersion

    @property
    def PayMode(self):
        """计费模式。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Extend(self):
        """差异化扩展信息, json格式。
        :rtype: str
        """
        return self._Extend

    @Extend.setter
    def Extend(self, Extend):
        self._Extend = Extend

    @property
    def ExpiredAt(self):
        """过期时间。
        :rtype: str
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def IsNoExpired(self):
        """是否不过期(永久)。
        :rtype: bool
        """
        return self._IsNoExpired

    @IsNoExpired.setter
    def IsNoExpired(self, IsNoExpired):
        self._IsNoExpired = IsNoExpired

    @property
    def WanAddress(self):
        """外网地址。
        :rtype: str
        """
        return self._WanAddress

    @WanAddress.setter
    def WanAddress(self, WanAddress):
        self._WanAddress = WanAddress

    @property
    def IsolateAt(self):
        """隔离时间
        :rtype: str
        """
        return self._IsolateAt

    @IsolateAt.setter
    def IsolateAt(self, IsolateAt):
        self._IsolateAt = IsolateAt

    @property
    def AutoRenew(self):
        """是否自动续费。0: 不自动续费(可以支持特权不停服)；1:自动续费；2:到期不续费.
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def TaskStatus(self):
        """任务状态：0-无任务；1-待执行任务；2-密钥更新中；3-网络变更中；4-参数变更中；5-embedding变更中；6-ai套件变更中；7-滚动升级中；8-纵向扩容中；9-纵向缩容中；10-横向扩容中；11-横向缩容中
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Product = params.get("Product")
        if params.get("Networks") is not None:
            self._Networks = []
            for item in params.get("Networks"):
                obj = Network()
                obj._deserialize(item)
                self._Networks.append(obj)
        self._ShardNum = params.get("ShardNum")
        self._ReplicaNum = params.get("ReplicaNum")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._HealthScore = params.get("HealthScore")
        self._Warning = params.get("Warning")
        self._Project = params.get("Project")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._Status = params.get("Status")
        self._EngineName = params.get("EngineName")
        self._EngineVersion = params.get("EngineVersion")
        self._ApiVersion = params.get("ApiVersion")
        self._PayMode = params.get("PayMode")
        self._Extend = params.get("Extend")
        self._ExpiredAt = params.get("ExpiredAt")
        self._IsNoExpired = params.get("IsNoExpired")
        self._WanAddress = params.get("WanAddress")
        self._IsolateAt = params.get("IsolateAt")
        self._AutoRenew = params.get("AutoRenew")
        self._TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstanceRequest(AbstractModel):
    """IsolateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定需隔离的实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """指定需隔离的实例 ID。
        :rtype: str
        """
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
        


class IsolateInstanceResponse(AbstractModel):
    """IsolateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        :param _InstanceIds: 实例ID，格式如：vdb-c9s3****。
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        """要修改的安全组ID列表，一个或者多个安全组 ID 组成的数组。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        """实例ID，格式如：vdb-c9s3****。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyInstanceMaintenanceWindowRequest(AbstractModel):
    """ModifyInstanceMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定需修改维护时间窗的实例 ID。
        :type InstanceId: str
        :param _StartTime: 维护时间窗开始时间。取值范围为"00:00-23:00"的任意整点，如01:00。
        :type StartTime: str
        :param _TimeSpan: 设置维护时间窗的时长。根据指定的维护时间窗开始时间与时长可确定维护时间窗的范围。
- 单位：小时。
- 取值范围：3、6、8、10、12。
        :type TimeSpan: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._TimeSpan = None

    @property
    def InstanceId(self):
        """指定需修改维护时间窗的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """维护时间窗开始时间。取值范围为"00:00-23:00"的任意整点，如01:00。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TimeSpan(self):
        """设置维护时间窗的时长。根据指定的维护时间窗开始时间与时长可确定维护时间窗的范围。
- 单位：小时。
- 取值范围：3、6、8、10、12。
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceMaintenanceWindowResponse(AbstractModel):
    """ModifyInstanceMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Network(AbstractModel):
    """网络信息

    """

    def __init__(self):
        r"""
        :param _VpcId: VpcId(VPC网络下有效)
        :type VpcId: str
        :param _SubnetId: 子网Id(VPC网络下有效)。
        :type SubnetId: str
        :param _Vip: 内网访问IP。
        :type Vip: str
        :param _Port: 内网访问Port。
        :type Port: int
        :param _PreserveDuration: 旧 ip 保留时长，单位天
        :type PreserveDuration: int
        :param _ExpireTime: 旧 ip 到期时间
        :type ExpireTime: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Port = None
        self._PreserveDuration = None
        self._ExpireTime = None

    @property
    def VpcId(self):
        """VpcId(VPC网络下有效)
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网Id(VPC网络下有效)。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        """内网访问IP。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Port(self):
        """内网访问Port。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def PreserveDuration(self):
        """旧 ip 保留时长，单位天
        :rtype: int
        """
        return self._PreserveDuration

    @PreserveDuration.setter
    def PreserveDuration(self, PreserveDuration):
        self._PreserveDuration = PreserveDuration

    @property
    def ExpireTime(self):
        """旧 ip 到期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Port = params.get("Port")
        self._PreserveDuration = params.get("PreserveDuration")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """实例pod信息， pod 名称

    """

    def __init__(self):
        r"""
        :param _Name: Pod名称。
        :type Name: str
        :param _Status: pod状态
        :type Status: str
        """
        self._Name = None
        self._Status = None

    @property
    def Name(self):
        """Pod名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """pod状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Outbound(AbstractModel):
    """安全组出站规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT或者DROP。
        :type Action: str
        :param _AddressModule: 地址组id代表的地址集合。
        :type AddressModule: str
        :param _CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。
        :type CidrIp: str
        :param _Desc: 描述。
        :type Desc: str
        :param _IpProtocol: 网络协议，支持udp、tcp等。
        :type IpProtocol: str
        :param _PortRange: 端口。
        :type PortRange: str
        :param _ServiceModule: 服务组id代表的协议和端口集合。
        :type ServiceModule: str
        :param _Id: 安全组id代表的地址集合。
        :type Id: str
        """
        self._Action = None
        self._AddressModule = None
        self._CidrIp = None
        self._Desc = None
        self._IpProtocol = None
        self._PortRange = None
        self._ServiceModule = None
        self._Id = None

    @property
    def Action(self):
        """策略，ACCEPT或者DROP。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        """地址组id代表的地址集合。
        :rtype: str
        """
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        """来源Ip或Ip段，例如192.168.0.0/16。
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        """描述。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        """网络协议，支持udp、tcp等。
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        """端口。
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        """服务组id代表的协议和端口集合。
        :rtype: str
        """
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
        """安全组id代表的地址集合。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._AddressModule = params.get("AddressModule")
        self._CidrIp = params.get("CidrIp")
        self._Desc = params.get("Desc")
        self._IpProtocol = params.get("IpProtocol")
        self._PortRange = params.get("PortRange")
        self._ServiceModule = params.get("ServiceModule")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverInstanceRequest(AbstractModel):
    """RecoverInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定待恢复的实例 ID。
        :type InstanceId: str
        :param _PayPeriod: 若实例为包年包月计费，需通过该参数指定续费的时长。
- 单位：月。
- 取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。默认为1。
        :type PayPeriod: int
        """
        self._InstanceId = None
        self._PayPeriod = None

    @property
    def InstanceId(self):
        """指定待恢复的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PayPeriod(self):
        """若实例为包年包月计费，需通过该参数指定续费的时长。
- 单位：月。
- 取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。默认为1。
        :rtype: int
        """
        return self._PayPeriod

    @PayPeriod.setter
    def PayPeriod(self, PayPeriod):
        self._PayPeriod = PayPeriod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PayPeriod = params.get("PayPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverInstanceResponse(AbstractModel):
    """RecoverInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定需扩容节点数量的实例 ID。
        :type InstanceId: str
        :param _ReplicaNum: 指定扩容后的节点数量。选项范围起始于当前实例已有的节点数，上限为30个节点。
        :type ReplicaNum: int
        :param _RunNow: 指定水平扩容增加节点数量的时间。
- false：默认值，指在下一个维护时间段内执行增加节点数的任务。实例列表中“状态”列将显示“待执行配置变更”，等到维护时间窗内启动扩容任务。维护时间的更多信息，请参维护时间窗。
- true：立即执行增加节点数的任务，请确保此时没有重大业务操作。
        :type RunNow: bool
        """
        self._InstanceId = None
        self._ReplicaNum = None
        self._RunNow = None

    @property
    def InstanceId(self):
        """指定需扩容节点数量的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReplicaNum(self):
        """指定扩容后的节点数量。选项范围起始于当前实例已有的节点数，上限为30个节点。
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def RunNow(self):
        """指定水平扩容增加节点数量的时间。
- false：默认值，指在下一个维护时间段内执行增加节点数的任务。实例列表中“状态”列将显示“待执行配置变更”，等到维护时间窗内启动扩容任务。维护时间的更多信息，请参维护时间窗。
- true：立即执行增加节点数的任务，请确保此时没有重大业务操作。
        :rtype: bool
        """
        return self._RunNow

    @RunNow.setter
    def RunNow(self, RunNow):
        self._RunNow = RunNow


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReplicaNum = params.get("ReplicaNum")
        self._RunNow = params.get("RunNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ScaleUpInstanceRequest(AbstractModel):
    """ScaleUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 指定需升级配置的实例 ID。
        :type InstanceId: str
        :param _Cpu: 指定升级配置后的 CPU 核数。
- 节点规格可选项（CPU & 内存）必须 >= 当前配置。
- 可选择的规格信息，请参见[选择节点规格与数量](https://cloud.tencent.com/document/product/1709/113399)。
        :type Cpu: float
        :param _Memory: 指定升级配置后的内存大小，单位为：GB。
- 节点规格可选项（CPU & 内存）必须 >= 当前配置。
- 不同实例类型对 CPU 与内存资源的配置比例有不同的要求。例如，计算型实例，CPU 与内存的分配比例要求为 1:2。CPU 被指定为 4 核，那么内存则应被指定为 8GB。节点规格的详细信息，请参见[选择节点规格与数量](https://cloud.tencent.com/document/product/1709/113399)。

        :type Memory: float
        :param _StorageSize: 指定升级配置后的磁盘容量。
- 单位：GB。
- 取值范围为：[10,1000]。
- 取值必须为10的倍数。
        :type StorageSize: int
        :param _RunNow: 指定垂直扩容升级节点配置的时间。
- false：默认值，指在下一个维护时间段内执行升配节点规格的任务。实例列表中“状态”列将显示“待执行配置变更”，等到维护时间窗内启动任务。维护时间的更多信息，请参见维护时间窗。
- true：立即执行升级配置的任务，请确保此时没有重大业务操作。
        :type RunNow: bool
        """
        self._InstanceId = None
        self._Cpu = None
        self._Memory = None
        self._StorageSize = None
        self._RunNow = None

    @property
    def InstanceId(self):
        """指定需升级配置的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cpu(self):
        """指定升级配置后的 CPU 核数。
- 节点规格可选项（CPU & 内存）必须 >= 当前配置。
- 可选择的规格信息，请参见[选择节点规格与数量](https://cloud.tencent.com/document/product/1709/113399)。
        :rtype: float
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """指定升级配置后的内存大小，单位为：GB。
- 节点规格可选项（CPU & 内存）必须 >= 当前配置。
- 不同实例类型对 CPU 与内存资源的配置比例有不同的要求。例如，计算型实例，CPU 与内存的分配比例要求为 1:2。CPU 被指定为 4 核，那么内存则应被指定为 8GB。节点规格的详细信息，请参见[选择节点规格与数量](https://cloud.tencent.com/document/product/1709/113399)。

        :rtype: float
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def StorageSize(self):
        """指定升级配置后的磁盘容量。
- 单位：GB。
- 取值范围为：[10,1000]。
- 取值必须为10的倍数。
        :rtype: int
        """
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def RunNow(self):
        """指定垂直扩容升级节点配置的时间。
- false：默认值，指在下一个维护时间段内执行升配节点规格的任务。实例列表中“状态”列将显示“待执行配置变更”，等到维护时间窗内启动任务。维护时间的更多信息，请参见维护时间窗。
- true：立即执行升级配置的任务，请确保此时没有重大业务操作。
        :rtype: bool
        """
        return self._RunNow

    @RunNow.setter
    def RunNow(self, RunNow):
        self._RunNow = RunNow


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._StorageSize = params.get("StorageSize")
        self._RunNow = params.get("RunNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpInstanceResponse(AbstractModel):
    """ScaleUpInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss。
        :type CreateTime: str
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称。
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组备注。
        :type SecurityGroupRemark: str
        :param _Outbound: 出站规则。
        :type Outbound: list of Outbound
        :param _Inbound: 入站规则。
        :type Inbound: list of Inbound
        :param _UpdateTime: 修改时间，时间格式：yyyy-mm-dd hh:mm:ss。
        :type UpdateTime: str
        """
        self._CreateTime = None
        self._ProjectId = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Outbound = None
        self._Inbound = None
        self._UpdateTime = None

    @property
    def CreateTime(self):
        """创建时间，时间格式：yyyy-mm-dd hh:mm:ss。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectId(self):
        """项目ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupId(self):
        """安全组ID。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        """安全组名称。
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        """安全组备注。
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Outbound(self):
        """出站规则。
        :rtype: list of Outbound
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def Inbound(self):
        """入站规则。
        :rtype: list of Inbound
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def UpdateTime(self):
        """修改时间，时间格式：yyyy-mm-dd hh:mm:ss。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

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
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
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
        