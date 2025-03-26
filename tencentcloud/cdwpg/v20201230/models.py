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


class AccessInfo(AbstractModel):
    """访问信息

    """

    def __init__(self):
        r"""
        :param _Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        """
        self._Address = None
        self._Protocol = None

    @property
    def Address(self):
        """地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Protocol(self):
        """协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountInfo(AbstractModel):
    """用于描述账号的实例ID、账号名

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _UserName: 账号名
        :type UserName: str
        :param _Perms: 账户属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Perms: list of str
        """
        self._InstanceId = None
        self._UserName = None
        self._Perms = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """账号名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Perms(self):
        """账户属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Perms

    @Perms.setter
    def Perms(self, Perms):
        self._Perms = Perms


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Perms = params.get("Perms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CBSSpec(AbstractModel):
    """磁盘规格

    """

    def __init__(self):
        r"""
        :param _DiskType: 盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _DiskCount: 个数
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        """盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        """个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CBSSpecInfo(AbstractModel):
    """磁盘信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _DiskCount: 个数
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        """盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        """个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNResourceSpec(AbstractModel):
    """云原生资源规格描述信息

    """

    def __init__(self):
        r"""
        :param _Type: 节点类型
        :type Type: str
        :param _SpecName: 机型
        :type SpecName: str
        :param _Count: 节点个数
        :type Count: int
        :param _DiskSpec: 磁盘信息
        :type DiskSpec: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        """
        self._Type = None
        self._SpecName = None
        self._Count = None
        self._DiskSpec = None

    @property
    def Type(self):
        """节点类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SpecName(self):
        """机型
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        """节点个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        """磁盘信息
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        if params.get("DiskSpec") is not None:
            self._DiskSpec = CBSSpec()
            self._DiskSpec._deserialize(params.get("DiskSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargeProperties(AbstractModel):
    """计费时间参数

    """

    def __init__(self):
        r"""
        :param _RenewFlag: 1-需要自动续期
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _TimeSpan: 订单时间范围
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _TimeUnit: 时间单位，一般为h和m
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _PayMode: 计费类型0-按量计费，1-包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _ChargeType: PREPAID、POSTPAID_BY_HOUR
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        """
        self._RenewFlag = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._PayMode = None
        self._ChargeType = None

    @property
    def RenewFlag(self):
        """1-需要自动续期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        """订单时间范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """时间单位，一般为h和m
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def PayMode(self):
        """计费类型0-按量计费，1-包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ChargeType(self):
        """PREPAID、POSTPAID_BY_HOUR
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType


    def _deserialize(self, params):
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._PayMode = params.get("PayMode")
        self._ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigHistory(AbstractModel):
    """ConfigHistory1

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: int
        :param _InstanceId: 实例名
        :type InstanceId: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _NodeType: dn/cn
        :type NodeType: str
        :param _ParamName: 参数名
        :type ParamName: str
        :param _ParamNewValue: 新参数值
        :type ParamNewValue: str
        :param _ParamOldValue: 旧参数值
        :type ParamOldValue: str
        :param _Status: 状态 doing/success
        :type Status: str
        """
        self._Id = None
        self._InstanceId = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._NodeType = None
        self._ParamName = None
        self._ParamNewValue = None
        self._ParamOldValue = None
        self._Status = None

    @property
    def Id(self):
        """id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        """实例名
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreatedAt(self):
        """创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        """更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def NodeType(self):
        """dn/cn
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ParamName(self):
        """参数名
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamNewValue(self):
        """新参数值
        :rtype: str
        """
        return self._ParamNewValue

    @ParamNewValue.setter
    def ParamNewValue(self, ParamNewValue):
        self._ParamNewValue = ParamNewValue

    @property
    def ParamOldValue(self):
        """旧参数值
        :rtype: str
        """
        return self._ParamOldValue

    @ParamOldValue.setter
    def ParamOldValue(self, ParamOldValue):
        self._ParamOldValue = ParamOldValue

    @property
    def Status(self):
        """状态 doing/success
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._NodeType = params.get("NodeType")
        self._ParamName = params.get("ParamName")
        self._ParamNewValue = params.get("ParamNewValue")
        self._ParamOldValue = params.get("ParamOldValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigParams(AbstractModel):
    """参数

    """

    def __init__(self):
        r"""
        :param _ParameterName: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ParameterName: str
        :param _ParameterValue: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type ParameterValue: str
        :param _ParameterOldValue: 修改前的值
注意：此字段可能返回 null，表示取不到有效值。
        :type ParameterOldValue: str
        """
        self._ParameterName = None
        self._ParameterValue = None
        self._ParameterOldValue = None

    @property
    def ParameterName(self):
        """名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName

    @property
    def ParameterValue(self):
        """值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParameterValue

    @ParameterValue.setter
    def ParameterValue(self, ParameterValue):
        self._ParameterValue = ParameterValue

    @property
    def ParameterOldValue(self):
        """修改前的值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParameterOldValue

    @ParameterOldValue.setter
    def ParameterOldValue(self, ParameterOldValue):
        self._ParameterOldValue = ParameterOldValue


    def _deserialize(self, params):
        self._ParameterName = params.get("ParameterName")
        self._ParameterValue = params.get("ParameterValue")
        self._ParameterOldValue = params.get("ParameterOldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceByApiRequest(AbstractModel):
    """CreateInstanceByApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Zone: 可用区
        :type Zone: str
        :param _UserVPCId: 私有网络
        :type UserVPCId: str
        :param _UserSubnetId: 子网
        :type UserSubnetId: str
        :param _ChargeProperties: 计费方式
        :type ChargeProperties: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        :param _AdminPassword: 集群密码
        :type AdminPassword: str
        :param _Resources: 资源信息
        :type Resources: list of ResourceSpecNew
        :param _Tags: 标签列表
        :type Tags: :class:`tencentcloud.cdwpg.v20201230.models.Tag`
        :param _ProductVersion: 版本
        :type ProductVersion: str
        """
        self._InstanceName = None
        self._Zone = None
        self._UserVPCId = None
        self._UserSubnetId = None
        self._ChargeProperties = None
        self._AdminPassword = None
        self._Resources = None
        self._Tags = None
        self._ProductVersion = None

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UserVPCId(self):
        """私有网络
        :rtype: str
        """
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        """子网
        :rtype: str
        """
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ChargeProperties(self):
        """计费方式
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def AdminPassword(self):
        """集群密码
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Resources(self):
        """资源信息
        :rtype: list of ResourceSpecNew
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Tags(self):
        """标签列表
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.Tag`
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProductVersion(self):
        """版本
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._Zone = params.get("Zone")
        self._UserVPCId = params.get("UserVPCId")
        self._UserSubnetId = params.get("UserSubnetId")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = ChargeProperties()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        self._AdminPassword = params.get("AdminPassword")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceSpecNew()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("Tags") is not None:
            self._Tags = Tag()
            self._Tags._deserialize(params.get("Tags"))
        self._ProductVersion = params.get("ProductVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceByApiResponse(AbstractModel):
    """CreateInstanceByApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Accounts: 账号数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Accounts: list of AccountInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Accounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Accounts(self):
        """账号数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AccountInfo
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountInfo()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBConfigHistoryRequest(AbstractModel):
    """DescribeDBConfigHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Limit: 数据库分页
        :type Limit: int
        :param _Offset: 数据库分页
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """数据库分页
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """数据库分页
        :rtype: int
        """
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
        


class DescribeDBConfigHistoryResponse(AbstractModel):
    """DescribeDBConfigHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _ConfigHistory: 历史参数
        :type ConfigHistory: list of ConfigHistory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConfigHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConfigHistory(self):
        """历史参数
        :rtype: list of ConfigHistory
        """
        return self._ConfigHistory

    @ConfigHistory.setter
    def ConfigHistory(self, ConfigHistory):
        self._ConfigHistory = ConfigHistory

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
        self._TotalCount = params.get("TotalCount")
        if params.get("ConfigHistory") is not None:
            self._ConfigHistory = []
            for item in params.get("ConfigHistory"):
                obj = ConfigHistory()
                obj._deserialize(item)
                self._ConfigHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBParamsRequest(AbstractModel):
    """DescribeDBParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeTypes: cn/dn
        :type NodeTypes: list of str
        :param _Limit: 分页参数，分页步长，默认为10 示例值：10
        :type Limit: int
        :param _Offset: 分页参数，第一页为0，第二页为10
        :type Offset: int
        :param _InstanceId: InstanceId名称
        :type InstanceId: str
        """
        self._NodeTypes = None
        self._Limit = None
        self._Offset = None
        self._InstanceId = None

    @property
    def NodeTypes(self):
        """cn/dn
        :rtype: list of str
        """
        return self._NodeTypes

    @NodeTypes.setter
    def NodeTypes(self, NodeTypes):
        self._NodeTypes = NodeTypes

    @property
    def Limit(self):
        """分页参数，分页步长，默认为10 示例值：10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页参数，第一页为0，第二页为10
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceId(self):
        """InstanceId名称
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._NodeTypes = params.get("NodeTypes")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBParamsResponse(AbstractModel):
    """DescribeDBParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Items: 参数信息
        :type Items: list of ParamItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """参数信息
        :rtype: list of ParamItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeErrorLogRequest(AbstractModel):
    """DescribeErrorLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Limit: 返回数量，默认为20，最大值为2000
        :type Limit: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为2000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorLogResponse(AbstractModel):
    """DescribeErrorLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回信息总数
        :type TotalCount: int
        :param _ErrorLogDetails: 错误日志详细信息
        :type ErrorLogDetails: list of ErrorLogDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ErrorLogDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回信息总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ErrorLogDetails(self):
        """错误日志详细信息
        :rtype: list of ErrorLogDetail
        """
        return self._ErrorLogDetails

    @ErrorLogDetails.setter
    def ErrorLogDetails(self, ErrorLogDetails):
        self._ErrorLogDetails = ErrorLogDetails

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
        self._TotalCount = params.get("TotalCount")
        if params.get("ErrorLogDetails") is not None:
            self._ErrorLogDetails = []
            for item in params.get("ErrorLogDetails"):
                obj = ErrorLogDetail()
                obj._deserialize(item)
                self._ErrorLogDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceInfoRequest(AbstractModel):
    """DescribeInstanceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群实例ID
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
        


class DescribeInstanceInfoResponse(AbstractModel):
    """DescribeInstanceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SimpleInstanceInfo: 集群描述信息
        :type SimpleInstanceInfo: :class:`tencentcloud.cdwpg.v20201230.models.SimpleInstanceInfo`
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SimpleInstanceInfo = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def SimpleInstanceInfo(self):
        """集群描述信息
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.SimpleInstanceInfo`
        """
        return self._SimpleInstanceInfo

    @SimpleInstanceInfo.setter
    def SimpleInstanceInfo(self, SimpleInstanceInfo):
        self._SimpleInstanceInfo = SimpleInstanceInfo

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("SimpleInstanceInfo") is not None:
            self._SimpleInstanceInfo = SimpleInstanceInfo()
            self._SimpleInstanceInfo._deserialize(params.get("SimpleInstanceInfo"))
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRequest(AbstractModel):
    """DescribeInstanceNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群ID
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
        


class DescribeInstanceNodesResponse(AbstractModel):
    """DescribeInstanceNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: error msg
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _InstanceNodes: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceNodes: list of InstanceNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._InstanceNodes = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """error msg
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def InstanceNodes(self):
        """节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceNode
        """
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

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
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("InstanceNodes") is not None:
            self._InstanceNodes = []
            for item in params.get("InstanceNodes"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._InstanceNodes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    """DescribeInstanceOperations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Offset: 分页参数，偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页参数，每页数目，默认为10
        :type Limit: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        """集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """分页参数，偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数，每页数目，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 操作记录总数
        :type TotalCount: int
        :param _Operations: 操作记录具体数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Operations: list of InstanceOperation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Operations = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """操作记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Operations(self):
        """操作记录具体数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceOperation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = InstanceOperation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群实例ID
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
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceInfo: 实例描述信息
        :type InstanceInfo: :class:`tencentcloud.cdwpg.v20201230.models.InstanceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceInfo = None
        self._RequestId = None

    @property
    def InstanceInfo(self):
        """实例描述信息
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.InstanceInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

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
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    """DescribeInstanceState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例名称
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群实例名称
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
        


class DescribeInstanceStateResponse(AbstractModel):
    """DescribeInstanceState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceState: 集群状态，例如：Serving
        :type InstanceState: str
        :param _FlowCreateTime: 集群操作创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowCreateTime: str
        :param _FlowName: 集群操作名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowName: str
        :param _FlowProgress: 集群操作进度
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowProgress: float
        :param _InstanceStateDesc: 集群状态描述，例如：运行中
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateDesc: str
        :param _FlowMsg: 集群流程错误信息，例如：“创建失败，资源不足”
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMsg: str
        :param _ProcessName: 当前步骤的名称，例如：”购买资源中“
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessName: str
        :param _BackupStatus: 集群备份任务开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatus: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessName = None
        self._BackupStatus = None
        self._RequestId = None

    @property
    def InstanceState(self):
        """集群状态，例如：Serving
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        """集群操作创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        """集群操作名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        """集群操作进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        """集群状态描述，例如：运行中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        """集群流程错误信息，例如：“创建失败，资源不足”
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        """当前步骤的名称，例如：”购买资源中“
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def BackupStatus(self):
        """集群备份任务开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

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
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._ProcessName = params.get("ProcessName")
        self._BackupStatus = params.get("BackupStatus")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: 用集群id搜索
        :type SearchInstanceId: str
        :param _SearchInstanceName: 用集群名字搜索
        :type SearchInstanceName: str
        :param _Offset: 分页参数，第一页为0，第二页为10
        :type Offset: int
        :param _Limit: 分页参数，分页步长，默认为10
        :type Limit: int
        :param _SearchTags: 搜索标签列表
        :type SearchTags: list of SearchTags
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None

    @property
    def SearchInstanceId(self):
        """用集群id搜索
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        """用集群名字搜索
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        """分页参数，第一页为0，第二页为10
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数，分页步长，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        """搜索标签列表
        :rtype: list of SearchTags
        """
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags


    def _deserialize(self, params):
        self._SearchInstanceId = params.get("SearchInstanceId")
        self._SearchInstanceName = params.get("SearchInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("SearchTags") is not None:
            self._SearchTags = []
            for item in params.get("SearchTags"):
                obj = SearchTags()
                obj._deserialize(item)
                self._SearchTags.append(obj)
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
        :param _TotalCount: 实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _InstancesList: 实例数组
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancesList: list of InstanceInfo
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstancesList = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        """实例数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceInfo
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def ErrorMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._TotalCount = params.get("TotalCount")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeSimpleInstancesRequest(AbstractModel):
    """DescribeSimpleInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: 用集群id搜索
        :type SearchInstanceId: str
        :param _SearchInstanceName: 用集群名字搜索
        :type SearchInstanceName: str
        :param _Offset: 分页参数，第一页为0，第二页为10
        :type Offset: int
        :param _Limit: 分页参数，分页步长，默认为10
        :type Limit: int
        :param _SearchTags: 用标签列表搜索
        :type SearchTags: list of str
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None

    @property
    def SearchInstanceId(self):
        """用集群id搜索
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        """用集群名字搜索
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        """分页参数，第一页为0，第二页为10
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数，分页步长，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        """用标签列表搜索
        :rtype: list of str
        """
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags


    def _deserialize(self, params):
        self._SearchInstanceId = params.get("SearchInstanceId")
        self._SearchInstanceName = params.get("SearchInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchTags = params.get("SearchTags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSimpleInstancesResponse(AbstractModel):
    """DescribeSimpleInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集群列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _InstancesList: 集群列表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancesList: list of InstanceSimpleInfoNew
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstancesList = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """集群列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        """集群列表详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceSimpleInfoNew
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def ErrorMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._TotalCount = params.get("TotalCount")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceSimpleInfoNew()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    """DescribeSlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Limit: 返回数量，默认为20，最大值为2000
        :type Limit: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Database: 数据库
        :type Database: str
        :param _OrderBy: 排序根据
        :type OrderBy: str
        :param _OrderByType: 升降序
        :type OrderByType: str
        :param _Duration: 过滤时间
        :type Duration: float
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Database = None
        self._OrderBy = None
        self._OrderByType = None
        self._Duration = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为2000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Database(self):
        """数据库
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def OrderBy(self):
        """排序根据
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """升降序
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Duration(self):
        """过滤时间
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Database = params.get("Database")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogResponse(AbstractModel):
    """DescribeSlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回信息总数
        :type TotalCount: int
        :param _SlowLogDetails: 慢SQL日志详细信息
        :type SlowLogDetails: :class:`tencentcloud.cdwpg.v20201230.models.SlowLogDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowLogDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回信息总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowLogDetails(self):
        """慢SQL日志详细信息
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.SlowLogDetail`
        """
        return self._SlowLogDetails

    @SlowLogDetails.setter
    def SlowLogDetails(self, SlowLogDetails):
        self._SlowLogDetails = SlowLogDetails

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SlowLogDetails") is not None:
            self._SlowLogDetails = SlowLogDetail()
            self._SlowLogDetails._deserialize(params.get("SlowLogDetails"))
        self._RequestId = params.get("RequestId")


class DescribeUpgradeListRequest(AbstractModel):
    """DescribeUpgradeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Offset: 分页参数，偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页参数，每页数目，默认为10
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """分页参数，偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数，每页数目，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpgradeListResponse(AbstractModel):
    """DescribeUpgradeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UpgradeItems: 升级记录具体数据
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeItems: list of UpgradeItem
        :param _TotalCount: 升级记录总数
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UpgradeItems = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UpgradeItems(self):
        """升级记录具体数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UpgradeItem
        """
        return self._UpgradeItems

    @UpgradeItems.setter
    def UpgradeItems(self, UpgradeItems):
        self._UpgradeItems = UpgradeItems

    @property
    def TotalCount(self):
        """升级记录总数
        :rtype: str
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
        if params.get("UpgradeItems") is not None:
            self._UpgradeItems = []
            for item in params.get("UpgradeItems"):
                obj = UpgradeItem()
                obj._deserialize(item)
                self._UpgradeItems.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserHbaConfigRequest(AbstractModel):
    """DescribeUserHbaConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
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
        


class DescribeUserHbaConfigResponse(AbstractModel):
    """DescribeUserHbaConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _HbaConfigs: hba数组
注意：此字段可能返回 null，表示取不到有效值。
        :type HbaConfigs: list of HbaConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._HbaConfigs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HbaConfigs(self):
        """hba数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of HbaConfig
        """
        return self._HbaConfigs

    @HbaConfigs.setter
    def HbaConfigs(self, HbaConfigs):
        self._HbaConfigs = HbaConfigs

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
        self._TotalCount = params.get("TotalCount")
        if params.get("HbaConfigs") is not None:
            self._HbaConfigs = []
            for item in params.get("HbaConfigs"):
                obj = HbaConfig()
                obj._deserialize(item)
                self._HbaConfigs.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyInstanceByApiRequest(AbstractModel):
    """DestroyInstanceByApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称，例如"cdwpg-xxxx"
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例名称，例如"cdwpg-xxxx"
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
        


class DestroyInstanceByApiResponse(AbstractModel):
    """DestroyInstanceByApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 销毁流程Id
        :type FlowId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """销毁流程Id
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DiskSpecPlus(AbstractModel):
    """磁盘规格

    """

    def __init__(self):
        r"""
        :param _DiskCount: 磁盘个数
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskCount: int
        :param _MaxDiskSize: 磁盘最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDiskSize: int
        :param _MinDiskSize: 磁盘最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type MinDiskSize: int
        :param _DiskType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskDesc: 磁盘类型详情
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskDesc: str
        :param _CvmClass: 机型类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmClass: str
        """
        self._DiskCount = None
        self._MaxDiskSize = None
        self._MinDiskSize = None
        self._DiskType = None
        self._DiskDesc = None
        self._CvmClass = None

    @property
    def DiskCount(self):
        """磁盘个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def MaxDiskSize(self):
        """磁盘最大值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MinDiskSize(self):
        """磁盘最小值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def DiskType(self):
        """磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        """磁盘类型详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def CvmClass(self):
        """机型类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CvmClass

    @CvmClass.setter
    def CvmClass(self, CvmClass):
        self._CvmClass = CvmClass


    def _deserialize(self, params):
        self._DiskCount = params.get("DiskCount")
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._MinDiskSize = params.get("MinDiskSize")
        self._DiskType = params.get("DiskType")
        self._DiskDesc = params.get("DiskDesc")
        self._CvmClass = params.get("CvmClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorLogDetail(AbstractModel):
    """错误日志详细信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Database: 数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _ErrorTime: 报错时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorTime: str
        :param _ErrorMessage: 报错信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        """
        self._UserName = None
        self._Database = None
        self._ErrorTime = None
        self._ErrorMessage = None

    @property
    def UserName(self):
        """用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        """数据库
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def ErrorTime(self):
        """报错时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorTime

    @ErrorTime.setter
    def ErrorTime(self, ErrorTime):
        self._ErrorTime = ErrorTime

    @property
    def ErrorMessage(self):
        """报错信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._ErrorTime = params.get("ErrorTime")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HbaConfig(AbstractModel):
    """user_config

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: str
        :param _Database: 数据库
        :type Database: str
        :param _User: 用户
        :type User: str
        :param _Address: ip地址
        :type Address: str
        :param _Method: 方法
        :type Method: str
        :param _Mask: 是否遮盖
注意：此字段可能返回 null，表示取不到有效值。
        :type Mask: str
        """
        self._Type = None
        self._Database = None
        self._User = None
        self._Address = None
        self._Method = None
        self._Mask = None

    @property
    def Type(self):
        """类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Database(self):
        """数据库
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def User(self):
        """用户
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Address(self):
        """ip地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Method(self):
        """方法
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Mask(self):
        """是否遮盖
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Database = params.get("Database")
        self._User = params.get("User")
        self._Address = params.get("Address")
        self._Method = params.get("Method")
        self._Mask = params.get("Mask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """云原生实例详情

    """

    def __init__(self):
        r"""
        :param _ID: ID值
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _InstanceType: 内核版本类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _InstanceName: 集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Status: 集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StatusDesc: 集群状态详情
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _InstanceStateInfo: 集群状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateInfo: :class:`tencentcloud.cdwpg.v20201230.models.InstanceStateInfo`
        :param _InstanceID: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zone: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _RegionDesc: 地域详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionDesc: str
        :param _ZoneDesc: 地区详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneDesc: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Version: 内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Charset: 字符集
注意：此字段可能返回 null，表示取不到有效值。
        :type Charset: str
        :param _CNNodes: CN节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CNNodes: list of InstanceNodeGroup
        :param _DNNodes: DN节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DNNodes: list of InstanceNodeGroup
        :param _RegionId: 地域id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _ZoneId: 地区id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _VpcId: 私有网络
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _PayMode: 计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _RenewFlag: 自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: bool
        :param _InstanceId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _AccessDetails: 访问信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessDetails: list of AccessInfo
        """
        self._ID = None
        self._InstanceType = None
        self._InstanceName = None
        self._Status = None
        self._StatusDesc = None
        self._InstanceStateInfo = None
        self._InstanceID = None
        self._CreateTime = None
        self._Region = None
        self._Zone = None
        self._RegionDesc = None
        self._ZoneDesc = None
        self._Tags = None
        self._Version = None
        self._Charset = None
        self._CNNodes = None
        self._DNNodes = None
        self._RegionId = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._ExpireTime = None
        self._PayMode = None
        self._RenewFlag = None
        self._InstanceId = None
        self._AccessDetails = None

    @property
    def ID(self):
        """ID值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceType(self):
        """内核版本类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        """集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        """集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """集群状态详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def InstanceStateInfo(self):
        """集群状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.InstanceStateInfo`
        """
        return self._InstanceStateInfo

    @InstanceStateInfo.setter
    def InstanceStateInfo(self, InstanceStateInfo):
        self._InstanceStateInfo = InstanceStateInfo

    @property
    def InstanceID(self):
        """集群id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Region(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """地区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RegionDesc(self):
        """地域详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def ZoneDesc(self):
        """地区详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Version(self):
        """内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Charset(self):
        """字符集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CNNodes(self):
        """CN节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceNodeGroup
        """
        return self._CNNodes

    @CNNodes.setter
    def CNNodes(self, CNNodes):
        self._CNNodes = CNNodes

    @property
    def DNNodes(self):
        """DN节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceNodeGroup
        """
        return self._DNNodes

    @DNNodes.setter
    def DNNodes(self, DNNodes):
        self._DNNodes = DNNodes

    @property
    def RegionId(self):
        """地域id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        """地区id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        """私有网络
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ExpireTime(self):
        """过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PayMode(self):
        """计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        """自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def InstanceId(self):
        """集群id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccessDetails(self):
        """访问信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AccessInfo
        """
        return self._AccessDetails

    @AccessDetails.setter
    def AccessDetails(self, AccessDetails):
        self._AccessDetails = AccessDetails


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceType = params.get("InstanceType")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        if params.get("InstanceStateInfo") is not None:
            self._InstanceStateInfo = InstanceStateInfo()
            self._InstanceStateInfo._deserialize(params.get("InstanceStateInfo"))
        self._InstanceID = params.get("InstanceID")
        self._CreateTime = params.get("CreateTime")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._RegionDesc = params.get("RegionDesc")
        self._ZoneDesc = params.get("ZoneDesc")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Version = params.get("Version")
        self._Charset = params.get("Charset")
        if params.get("CNNodes") is not None:
            self._CNNodes = []
            for item in params.get("CNNodes"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._CNNodes.append(obj)
        if params.get("DNNodes") is not None:
            self._DNNodes = []
            for item in params.get("DNNodes"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._DNNodes.append(obj)
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ExpireTime = params.get("ExpireTime")
        self._PayMode = params.get("PayMode")
        self._RenewFlag = params.get("RenewFlag")
        self._InstanceId = params.get("InstanceId")
        if params.get("AccessDetails") is not None:
            self._AccessDetails = []
            for item in params.get("AccessDetails"):
                obj = AccessInfo()
                obj._deserialize(item)
                self._AccessDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    """Instance node

    """

    def __init__(self):
        r"""
        :param _NodeId: id
        :type NodeId: int
        :param _NodeType: cn
        :type NodeType: str
        :param _NodeIp: ip
        :type NodeIp: str
        """
        self._NodeId = None
        self._NodeType = None
        self._NodeIp = None

    @property
    def NodeId(self):
        """id
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeType(self):
        """cn
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeIp(self):
        """ip
        :rtype: str
        """
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeType = params.get("NodeType")
        self._NodeIp = params.get("NodeIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNodeGroup(AbstractModel):
    """集群节点信息

    """

    def __init__(self):
        r"""
        :param _SpecName: 机型
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _DataDisk: 磁盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisk: :class:`tencentcloud.cdwpg.v20201230.models.DiskSpecPlus`
        :param _CvmCount: 机器个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmCount: int
        """
        self._SpecName = None
        self._DataDisk = None
        self._CvmCount = None

    @property
    def SpecName(self):
        """机型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def DataDisk(self):
        """磁盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DiskSpecPlus`
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def CvmCount(self):
        """机器个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CvmCount

    @CvmCount.setter
    def CvmCount(self, CvmCount):
        self._CvmCount = CvmCount


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        if params.get("DataDisk") is not None:
            self._DataDisk = DiskSpecPlus()
            self._DataDisk._deserialize(params.get("DataDisk"))
        self._CvmCount = params.get("CvmCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceOperation(AbstractModel):
    """集群操作描述

    """

    def __init__(self):
        r"""
        :param _Id: 操作名称，例如“create_instance"、“scaleout_instance”等
        :type Id: int
        :param _InstanceId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Action: 操作名称描述，例如“创建”，“修改集群名称”等
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StartTime: 操作开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 操作结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Context: 操作上下文
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _UpdateTime: 操作更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Uin: 操作UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        """
        self._Id = None
        self._InstanceId = None
        self._Action = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._Context = None
        self._UpdateTime = None
        self._Uin = None

    @property
    def Id(self):
        """操作名称，例如“create_instance"、“scaleout_instance”等
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        """集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Action(self):
        """操作名称描述，例如“创建”，“修改集群名称”等
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Status(self):
        """状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        """操作开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """操作结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Context(self):
        """操作上下文
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def UpdateTime(self):
        """操作更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Uin(self):
        """操作UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Action = params.get("Action")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Context = params.get("Context")
        self._UpdateTime = params.get("UpdateTime")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSimpleInfoNew(AbstractModel):
    """精简集群信息

    """

    def __init__(self):
        r"""
        :param _ID: ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _InstanceId: 集群Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Version: 内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _RegionId: 地域Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _RegionDesc: 地域详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionDesc: str
        :param _Zone: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _ZoneId: 地区id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _ZoneDesc: 地区详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneDesc: str
        :param _VpcId: 私有网络
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _CreateTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _AccessInfo: 访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessInfo: str
        :param _PayMode: 计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _RenewFlag: 自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: bool
        """
        self._ID = None
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._Region = None
        self._RegionId = None
        self._RegionDesc = None
        self._Zone = None
        self._ZoneId = None
        self._ZoneDesc = None
        self._VpcId = None
        self._SubnetId = None
        self._CreateTime = None
        self._ExpireTime = None
        self._AccessInfo = None
        self._PayMode = None
        self._RenewFlag = None

    @property
    def ID(self):
        """ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        """集群Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        """内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        """地域Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionDesc(self):
        """地域详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def Zone(self):
        """地区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        """地区id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneDesc(self):
        """地区详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def VpcId(self):
        """私有网络
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreateTime(self):
        """开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AccessInfo(self):
        """访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def PayMode(self):
        """计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        """自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._RegionDesc = params.get("RegionDesc")
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneDesc = params.get("ZoneDesc")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AccessInfo = params.get("AccessInfo")
        self._PayMode = params.get("PayMode")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStateInfo(AbstractModel):
    """集群状态抽象后的结构体

    """

    def __init__(self):
        r"""
        :param _InstanceState: 集群状态，例如：Serving
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceState: str
        :param _FlowCreateTime: 集群操作创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowCreateTime: str
        :param _FlowName: 集群操作名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowName: str
        :param _FlowProgress: 集群操作进度
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowProgress: int
        :param _InstanceStateDesc: 集群状态描述，例如：运行中
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateDesc: str
        :param _FlowMsg: 集群流程错误信息，例如：“创建失败，资源不足”
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMsg: str
        :param _ProcessName: 当前步骤的名称，例如：”购买资源中“
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessName: str
        :param _BackupStatus: 集群是否有备份中任务，有为1,无为0
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatus: int
        :param _RequestId: 请求id
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        :param _BackupOpenStatus: 集群是否有备份中任务，有为1,无为0
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOpenStatus: int
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessName = None
        self._BackupStatus = None
        self._RequestId = None
        self._BackupOpenStatus = None

    @property
    def InstanceState(self):
        """集群状态，例如：Serving
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        """集群操作创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        """集群操作名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        """集群操作进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        """集群状态描述，例如：运行中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        """集群流程错误信息，例如：“创建失败，资源不足”
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        """当前步骤的名称，例如：”购买资源中“
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def BackupStatus(self):
        """集群是否有备份中任务，有为1,无为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def RequestId(self):
        """请求id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def BackupOpenStatus(self):
        """集群是否有备份中任务，有为1,无为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BackupOpenStatus

    @BackupOpenStatus.setter
    def BackupOpenStatus(self, BackupOpenStatus):
        self._BackupOpenStatus = BackupOpenStatus


    def _deserialize(self, params):
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._ProcessName = params.get("ProcessName")
        self._BackupStatus = params.get("BackupStatus")
        self._RequestId = params.get("RequestId")
        self._BackupOpenStatus = params.get("BackupOpenStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance 名字
        :type InstanceId: str
        :param _NodeConfigParams: node参数
        :type NodeConfigParams: list of NodeConfigParams
        """
        self._InstanceId = None
        self._NodeConfigParams = None

    @property
    def InstanceId(self):
        """Instance 名字
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeConfigParams(self):
        """node参数
        :rtype: list of NodeConfigParams
        """
        return self._NodeConfigParams

    @NodeConfigParams.setter
    def NodeConfigParams(self, NodeConfigParams):
        self._NodeConfigParams = NodeConfigParams


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("NodeConfigParams") is not None:
            self._NodeConfigParams = []
            for item in params.get("NodeConfigParams"):
                obj = NodeConfigParams()
                obj._deserialize(item)
                self._NodeConfigParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程Id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步流程Id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _InstanceName: 新修改的实例名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """新修改的实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
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
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyUserHbaRequest(AbstractModel):
    """ModifyUserHba请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _HbaConfigs: hba数组
        :type HbaConfigs: list of HbaConfig
        """
        self._InstanceId = None
        self._HbaConfigs = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def HbaConfigs(self):
        """hba数组
        :rtype: list of HbaConfig
        """
        return self._HbaConfigs

    @HbaConfigs.setter
    def HbaConfigs(self, HbaConfigs):
        self._HbaConfigs = HbaConfigs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("HbaConfigs") is not None:
            self._HbaConfigs = []
            for item in params.get("HbaConfigs"):
                obj = HbaConfig()
                obj._deserialize(item)
                self._HbaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserHbaResponse(AbstractModel):
    """ModifyUserHba返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ErrorMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._TaskId = params.get("TaskId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class NodeConfigParams(AbstractModel):
    """node参数

    """

    def __init__(self):
        r"""
        :param _NodeType: node类型
        :type NodeType: str
        :param _ConfigParams: 参数
        :type ConfigParams: list of ConfigParams
        """
        self._NodeType = None
        self._ConfigParams = None

    @property
    def NodeType(self):
        """node类型
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ConfigParams(self):
        """参数
        :rtype: list of ConfigParams
        """
        return self._ConfigParams

    @ConfigParams.setter
    def ConfigParams(self, ConfigParams):
        self._ConfigParams = ConfigParams


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        if params.get("ConfigParams") is not None:
            self._ConfigParams = []
            for item in params.get("ConfigParams"):
                obj = ConfigParams()
                obj._deserialize(item)
                self._ConfigParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormQueryItem(AbstractModel):
    """慢查询项目信息

    """

    def __init__(self):
        r"""
        :param _CallTimes: 调用次数
注意：此字段可能返回 null，表示取不到有效值。
        :type CallTimes: int
        :param _SharedReadBlocks: 读共享内存块数
注意：此字段可能返回 null，表示取不到有效值。
        :type SharedReadBlocks: int
        :param _SharedWriteBlocks: 写共享内存块数
注意：此字段可能返回 null，表示取不到有效值。
        :type SharedWriteBlocks: int
        :param _DatabaseName: 数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param _NormalQuery: 脱敏后语句
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalQuery: str
        :param _MaxElapsedQuery: 执行时间最长的语句
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxElapsedQuery: str
        :param _CostTime: 花费总时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: float
        :param _ClientIp: 客户端ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIp: str
        :param _UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _TotalCallTimesPercent: 总次数占比
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCallTimesPercent: float
        :param _TotalCostTimePercent: 总耗时占比
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCostTimePercent: float
        :param _MinCostTime: 花费最小时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MinCostTime: float
        :param _MaxCostTime: 花费最大时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCostTime: float
        :param _FirstTime: 最早一条时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstTime: str
        :param _LastTime: 最晚一条时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTime: str
        :param _ReadCostTime: 读io总耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadCostTime: float
        :param _WriteCostTime: 写io总耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type WriteCostTime: float
        """
        self._CallTimes = None
        self._SharedReadBlocks = None
        self._SharedWriteBlocks = None
        self._DatabaseName = None
        self._NormalQuery = None
        self._MaxElapsedQuery = None
        self._CostTime = None
        self._ClientIp = None
        self._UserName = None
        self._TotalCallTimesPercent = None
        self._TotalCostTimePercent = None
        self._MinCostTime = None
        self._MaxCostTime = None
        self._FirstTime = None
        self._LastTime = None
        self._ReadCostTime = None
        self._WriteCostTime = None

    @property
    def CallTimes(self):
        """调用次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CallTimes

    @CallTimes.setter
    def CallTimes(self, CallTimes):
        self._CallTimes = CallTimes

    @property
    def SharedReadBlocks(self):
        """读共享内存块数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SharedReadBlocks

    @SharedReadBlocks.setter
    def SharedReadBlocks(self, SharedReadBlocks):
        self._SharedReadBlocks = SharedReadBlocks

    @property
    def SharedWriteBlocks(self):
        """写共享内存块数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SharedWriteBlocks

    @SharedWriteBlocks.setter
    def SharedWriteBlocks(self, SharedWriteBlocks):
        self._SharedWriteBlocks = SharedWriteBlocks

    @property
    def DatabaseName(self):
        """数据库
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def NormalQuery(self):
        """脱敏后语句
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NormalQuery

    @NormalQuery.setter
    def NormalQuery(self, NormalQuery):
        self._NormalQuery = NormalQuery

    @property
    def MaxElapsedQuery(self):
        """执行时间最长的语句
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MaxElapsedQuery

    @MaxElapsedQuery.setter
    def MaxElapsedQuery(self, MaxElapsedQuery):
        self._MaxElapsedQuery = MaxElapsedQuery

    @property
    def CostTime(self):
        """花费总时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def ClientIp(self):
        """客户端ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def UserName(self):
        """用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def TotalCallTimesPercent(self):
        """总次数占比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TotalCallTimesPercent

    @TotalCallTimesPercent.setter
    def TotalCallTimesPercent(self, TotalCallTimesPercent):
        self._TotalCallTimesPercent = TotalCallTimesPercent

    @property
    def TotalCostTimePercent(self):
        """总耗时占比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TotalCostTimePercent

    @TotalCostTimePercent.setter
    def TotalCostTimePercent(self, TotalCostTimePercent):
        self._TotalCostTimePercent = TotalCostTimePercent

    @property
    def MinCostTime(self):
        """花费最小时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MinCostTime

    @MinCostTime.setter
    def MinCostTime(self, MinCostTime):
        self._MinCostTime = MinCostTime

    @property
    def MaxCostTime(self):
        """花费最大时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MaxCostTime

    @MaxCostTime.setter
    def MaxCostTime(self, MaxCostTime):
        self._MaxCostTime = MaxCostTime

    @property
    def FirstTime(self):
        """最早一条时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def LastTime(self):
        """最晚一条时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def ReadCostTime(self):
        """读io总耗时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._ReadCostTime

    @ReadCostTime.setter
    def ReadCostTime(self, ReadCostTime):
        self._ReadCostTime = ReadCostTime

    @property
    def WriteCostTime(self):
        """写io总耗时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._WriteCostTime

    @WriteCostTime.setter
    def WriteCostTime(self, WriteCostTime):
        self._WriteCostTime = WriteCostTime


    def _deserialize(self, params):
        self._CallTimes = params.get("CallTimes")
        self._SharedReadBlocks = params.get("SharedReadBlocks")
        self._SharedWriteBlocks = params.get("SharedWriteBlocks")
        self._DatabaseName = params.get("DatabaseName")
        self._NormalQuery = params.get("NormalQuery")
        self._MaxElapsedQuery = params.get("MaxElapsedQuery")
        self._CostTime = params.get("CostTime")
        self._ClientIp = params.get("ClientIp")
        self._UserName = params.get("UserName")
        self._TotalCallTimesPercent = params.get("TotalCallTimesPercent")
        self._TotalCostTimePercent = params.get("TotalCostTimePercent")
        self._MinCostTime = params.get("MinCostTime")
        self._MaxCostTime = params.get("MaxCostTime")
        self._FirstTime = params.get("FirstTime")
        self._LastTime = params.get("LastTime")
        self._ReadCostTime = params.get("ReadCostTime")
        self._WriteCostTime = params.get("WriteCostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDetail(AbstractModel):
    """ParamDetail 详细

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamName: str
        :param _DefaultValue: 默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        :param _NeedRestart: 是否需要重启
注意：此字段可能返回 null，表示取不到有效值。
        :type NeedRestart: bool
        :param _RunningValue: 当前运行值
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningValue: str
        :param _ValueRange: 取值范围
        :type ValueRange: :class:`tencentcloud.cdwpg.v20201230.models.ValueRange`
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _ShortDesc: 英文简介
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortDesc: str
        :param _ParameterName: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParameterName: str
        """
        self._ParamName = None
        self._DefaultValue = None
        self._NeedRestart = None
        self._RunningValue = None
        self._ValueRange = None
        self._Unit = None
        self._ShortDesc = None
        self._ParameterName = None

    @property
    def ParamName(self):
        """参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def DefaultValue(self):
        """默认值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def NeedRestart(self):
        """是否需要重启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def RunningValue(self):
        """当前运行值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunningValue

    @RunningValue.setter
    def RunningValue(self, RunningValue):
        self._RunningValue = RunningValue

    @property
    def ValueRange(self):
        """取值范围
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ValueRange`
        """
        return self._ValueRange

    @ValueRange.setter
    def ValueRange(self, ValueRange):
        self._ValueRange = ValueRange

    @property
    def Unit(self):
        """单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def ShortDesc(self):
        """英文简介
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ShortDesc

    @ShortDesc.setter
    def ShortDesc(self, ShortDesc):
        self._ShortDesc = ShortDesc

    @property
    def ParameterName(self):
        """参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._DefaultValue = params.get("DefaultValue")
        self._NeedRestart = params.get("NeedRestart")
        self._RunningValue = params.get("RunningValue")
        if params.get("ValueRange") is not None:
            self._ValueRange = ValueRange()
            self._ValueRange._deserialize(params.get("ValueRange"))
        self._Unit = params.get("Unit")
        self._ShortDesc = params.get("ShortDesc")
        self._ParameterName = params.get("ParameterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItem(AbstractModel):
    """ParamItem 信息

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型, cn/dn
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param _NodeName: 节点名
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _TotalCount: 参数个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Details: 参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of ParamDetail
        """
        self._NodeType = None
        self._NodeName = None
        self._TotalCount = None
        self._Details = None

    @property
    def NodeType(self):
        """节点类型, cn/dn
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeName(self):
        """节点名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def TotalCount(self):
        """参数个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        """参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeName = params.get("NodeName")
        self._TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ParamDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Range(AbstractModel):
    """Range范围

    """

    def __init__(self):
        r"""
        :param _Min: 最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: str
        :param _Max: 最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: str
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        """最小值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        """最大值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _UserName: 需要修改的用户名
        :type UserName: str
        :param _NewPassword: 新密码
        :type NewPassword: str
        """
        self._InstanceId = None
        self._UserName = None
        self._NewPassword = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """需要修改的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def NewPassword(self):
        """新密码
        :rtype: str
        """
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._NewPassword = params.get("NewPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ResourceInfo(AbstractModel):
    """资源信息

    """

    def __init__(self):
        r"""
        :param _SpecName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _Count: 资源数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _DiskSpec: 磁盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSpec: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpecInfo`
        :param _Type: 节点类型，cn 或dn
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self._SpecName = None
        self._Count = None
        self._DiskSpec = None
        self._Type = None

    @property
    def SpecName(self):
        """资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        """资源数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        """磁盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpecInfo`
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def Type(self):
        """节点类型，cn 或dn
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        if params.get("DiskSpec") is not None:
            self._DiskSpec = CBSSpecInfo()
            self._DiskSpec._deserialize(params.get("DiskSpec"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceSpecNew(AbstractModel):
    """资源规格

    """

    def __init__(self):
        r"""
        :param _SpecName: 资源名称
        :type SpecName: str
        :param _Count: 资源数
        :type Count: int
        :param _DiskSpec: 磁盘信息
        :type DiskSpec: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        :param _Type: 资源类型，DATA
        :type Type: str
        """
        self._SpecName = None
        self._Count = None
        self._DiskSpec = None
        self._Type = None

    @property
    def SpecName(self):
        """资源名称
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        """资源数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        """磁盘信息
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def Type(self):
        """资源类型，DATA
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        if params.get("DiskSpec") is not None:
            self._DiskSpec = CBSSpec()
            self._DiskSpec._deserialize(params.get("DiskSpec"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称，例如“cdwpg-xxxx"
        :type InstanceId: str
        :param _NodeTypes: 需要重启的节点类型么，gtm/cn/dn/fn
        :type NodeTypes: list of str
        :param _NodeIds: 需要重启的节点编号，指定重启节点
        :type NodeIds: list of str
        """
        self._InstanceId = None
        self._NodeTypes = None
        self._NodeIds = None

    @property
    def InstanceId(self):
        """实例名称，例如“cdwpg-xxxx"
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeTypes(self):
        """需要重启的节点类型么，gtm/cn/dn/fn
        :rtype: list of str
        """
        return self._NodeTypes

    @NodeTypes.setter
    def NodeTypes(self, NodeTypes):
        self._NodeTypes = NodeTypes

    @property
    def NodeIds(self):
        """需要重启的节点编号，指定重启节点
        :rtype: list of str
        """
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeTypes = params.get("NodeTypes")
        self._NodeIds = params.get("NodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 重启实例id
        :type FlowId: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """重启实例id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群名
        :type InstanceId: str
        :param _NodeType: 节点类型
        :type NodeType: str
        :param _ScaleOutCount: 扩容节点数量
        :type ScaleOutCount: int
        """
        self._InstanceId = None
        self._NodeType = None
        self._ScaleOutCount = None

    @property
    def InstanceId(self):
        """集群名
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeType(self):
        """节点类型
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ScaleOutCount(self):
        """扩容节点数量
        :rtype: int
        """
        return self._ScaleOutCount

    @ScaleOutCount.setter
    def ScaleOutCount(self, ScaleOutCount):
        self._ScaleOutCount = ScaleOutCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeType = params.get("NodeType")
        self._ScaleOutCount = params.get("ScaleOutCount")
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
        :param _FlowId: 流程id
        :type FlowId: str
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """流程id
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScaleUpInstanceRequest(AbstractModel):
    """ScaleUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群唯一ID
        :type InstanceId: str
        :param _Case: 变更资源类型
        :type Case: str
        :param _ModifySpec: 修改的参数
        :type ModifySpec: :class:`tencentcloud.cdwpg.v20201230.models.CNResourceSpec`
        :param _InstanceName: 集群名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._Case = None
        self._ModifySpec = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """集群唯一ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Case(self):
        """变更资源类型
        :rtype: str
        """
        return self._Case

    @Case.setter
    def Case(self, Case):
        self._Case = Case

    @property
    def ModifySpec(self):
        """修改的参数
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CNResourceSpec`
        """
        return self._ModifySpec

    @ModifySpec.setter
    def ModifySpec(self, ModifySpec):
        self._ModifySpec = ModifySpec

    @property
    def InstanceName(self):
        """集群名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Case = params.get("Case")
        if params.get("ModifySpec") is not None:
            self._ModifySpec = CNResourceSpec()
            self._ModifySpec._deserialize(params.get("ModifySpec"))
        self._InstanceName = params.get("InstanceName")
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
        :param _FlowId: 返回的id
        :type FlowId: int
        :param _ErrorMsg: 具体错误
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """返回的id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """具体错误
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class SearchTags(AbstractModel):
    """列表页搜索的标记列表

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        :param _AllValue: 1表示只输入标签的键，没有输入值；0表示输入键时且输入值
        :type AllValue: int
        """
        self._TagKey = None
        self._TagValue = None
        self._AllValue = None

    @property
    def TagKey(self):
        """标签的键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签的值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def AllValue(self):
        """1表示只输入标签的键，没有输入值；0表示输入键时且输入值
        :rtype: int
        """
        return self._AllValue

    @AllValue.setter
    def AllValue(self, AllValue):
        self._AllValue = AllValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._AllValue = params.get("AllValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleInstanceInfo(AbstractModel):
    """集群信息

    """

    def __init__(self):
        r"""
        :param _ID: ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _InstanceId: 集群Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Version: 内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zone: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _UserVPCID: 私有网络
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVPCID: str
        :param _UserSubnetID: 子网
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSubnetID: str
        :param _CreateTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ExpireTime: 到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _AccessInfo: 访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessInfo: str
        :param _RenewFlag: 自动续费开关，0为不自动续费，1为自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _ChargeProperties: 计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeProperties: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        :param _Resources: 资源集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of ResourceInfo
        :param _Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Status: 集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._ID = None
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._Region = None
        self._Zone = None
        self._UserVPCID = None
        self._UserSubnetID = None
        self._CreateTime = None
        self._ExpireTime = None
        self._AccessInfo = None
        self._RenewFlag = None
        self._ChargeProperties = None
        self._Resources = None
        self._Tags = None
        self._Status = None

    @property
    def ID(self):
        """ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        """集群Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        """内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """地区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UserVPCID(self):
        """私有网络
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserVPCID

    @UserVPCID.setter
    def UserVPCID(self, UserVPCID):
        self._UserVPCID = UserVPCID

    @property
    def UserSubnetID(self):
        """子网
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserSubnetID

    @UserSubnetID.setter
    def UserSubnetID(self, UserSubnetID):
        self._UserSubnetID = UserSubnetID

    @property
    def CreateTime(self):
        """开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AccessInfo(self):
        """访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def RenewFlag(self):
        """自动续费开关，0为不自动续费，1为自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ChargeProperties(self):
        """计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def Resources(self):
        """资源集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceInfo
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Tags(self):
        """标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        """集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._UserVPCID = params.get("UserVPCID")
        self._UserSubnetID = params.get("UserSubnetID")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AccessInfo = params.get("AccessInfo")
        self._RenewFlag = params.get("RenewFlag")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = ChargeProperties()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogDetail(AbstractModel):
    """慢SQL日志

    """

    def __init__(self):
        r"""
        :param _TotalTime: 花费总时间
        :type TotalTime: float
        :param _TotalCallTimes: 调用总次数
        :type TotalCallTimes: int
        :param _NormalQuerys: 慢SQL
        :type NormalQuerys: list of NormQueryItem
        """
        self._TotalTime = None
        self._TotalCallTimes = None
        self._NormalQuerys = None

    @property
    def TotalTime(self):
        """花费总时间
        :rtype: float
        """
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def TotalCallTimes(self):
        """调用总次数
        :rtype: int
        """
        return self._TotalCallTimes

    @TotalCallTimes.setter
    def TotalCallTimes(self, TotalCallTimes):
        self._TotalCallTimes = TotalCallTimes

    @property
    def NormalQuerys(self):
        """慢SQL
        :rtype: list of NormQueryItem
        """
        return self._NormalQuerys

    @NormalQuerys.setter
    def NormalQuerys(self, NormalQuerys):
        self._NormalQuerys = NormalQuerys


    def _deserialize(self, params):
        self._TotalTime = params.get("TotalTime")
        self._TotalCallTimes = params.get("TotalCallTimes")
        if params.get("NormalQuerys") is not None:
            self._NormalQuerys = []
            for item in params.get("NormalQuerys"):
                obj = NormQueryItem()
                obj._deserialize(item)
                self._NormalQuerys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签描述

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
        """标签的键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签的值
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
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _PackageVersion: 安装包版本
        :type PackageVersion: str
        """
        self._InstanceId = None
        self._PackageVersion = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PackageVersion(self):
        """安装包版本
        :rtype: str
        """
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务id
        :type FlowId: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """任务id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class UpgradeItem(AbstractModel):
    """升级信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _SourceVersion: 原有内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceVersion: str
        :param _TargetVersion: 目标内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetVersion: str
        :param _CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Status: 任务完成状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _OperateUin: 操作者
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUin: str
        """
        self._TaskName = None
        self._SourceVersion = None
        self._TargetVersion = None
        self._CreateTime = None
        self._EndTime = None
        self._Status = None
        self._OperateUin = None

    @property
    def TaskName(self):
        """任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def SourceVersion(self):
        """原有内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceVersion

    @SourceVersion.setter
    def SourceVersion(self, SourceVersion):
        self._SourceVersion = SourceVersion

    @property
    def TargetVersion(self):
        """目标内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetVersion

    @TargetVersion.setter
    def TargetVersion(self, TargetVersion):
        self._TargetVersion = TargetVersion

    @property
    def CreateTime(self):
        """任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        """任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """任务完成状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OperateUin(self):
        """操作者
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._SourceVersion = params.get("SourceVersion")
        self._TargetVersion = params.get("TargetVersion")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._OperateUin = params.get("OperateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValueRange(AbstractModel):
    """ValueRange值

    """

    def __init__(self):
        r"""
        :param _Type: 参数类型，可以为 enum，string，section; 其中enum表示枚举，类似： utf8,latin1,gbk; string表示返回的参数值是字符串; section表示返回的参数值是一个取值范围，类似：[4-8]
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Range: type 取section的时候，返回的参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: :class:`tencentcloud.cdwpg.v20201230.models.Range`
        :param _Enum: type 取enum的时候，返回参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Enum: list of str
        :param _String: type 取string的时候，返回的参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type String: str
        """
        self._Type = None
        self._Range = None
        self._Enum = None
        self._String = None

    @property
    def Type(self):
        """参数类型，可以为 enum，string，section; 其中enum表示枚举，类似： utf8,latin1,gbk; string表示返回的参数值是字符串; section表示返回的参数值是一个取值范围，类似：[4-8]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Range(self):
        """type 取section的时候，返回的参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.Range`
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def Enum(self):
        """type 取enum的时候，返回参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Enum

    @Enum.setter
    def Enum(self, Enum):
        self._Enum = Enum

    @property
    def String(self):
        """type 取string的时候，返回的参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._String

    @String.setter
    def String(self, String):
        self._String = String


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Range") is not None:
            self._Range = Range()
            self._Range._deserialize(params.get("Range"))
        self._Enum = params.get("Enum")
        self._String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        