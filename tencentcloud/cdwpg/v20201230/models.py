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


class CBSSpec(AbstractModel):
    """磁盘规格

    """

    def __init__(self):
        r"""
        :param _DiskType: 盘类型
        :type DiskType: str
        :param _DiskSize: 大小
        :type DiskSize: int
        :param _DiskCount: 个数
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
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
        


class ChargeProperties(AbstractModel):
    """计费时间参数

    """

    def __init__(self):
        r"""
        :param _RenewFlag: 1-需要自动续期
        :type RenewFlag: int
        :param _TimeSpan: 订单时间范围
        :type TimeSpan: int
        :param _TimeUnit: 时间单位，一般为h和m
        :type TimeUnit: str
        :param _PayMode: 计费类型0-按量计费，1-包年包月
        :type PayMode: int
        :param _ChargeType: PREPAID、POSTPAID_BY_HOUR
        :type ChargeType: str
        """
        self._RenewFlag = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._PayMode = None
        self._ChargeType = None

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ChargeType(self):
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
        """
        self._InstanceName = None
        self._Zone = None
        self._UserVPCId = None
        self._UserSubnetId = None
        self._ChargeProperties = None
        self._AdminPassword = None
        self._Resources = None
        self._Tags = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UserVPCId(self):
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ChargeProperties(self):
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def AdminPassword(self):
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


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
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def Type(self):
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
        