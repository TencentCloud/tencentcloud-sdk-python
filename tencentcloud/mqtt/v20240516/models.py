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


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件列表
        :type Filters: list of Filter
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        :param _TagFilters: 标签过滤器
        :type TagFilters: list of TagFilter
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._TagFilters = None

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

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceListResponse(AbstractModel):
    """DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 实例列表
        :type Data: list of MQTTInstanceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTInstanceItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
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
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，
EXPERIMENT 体验版
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :type InstanceType: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _TopicNumLimit: 实例最大主题数量
        :type TopicNumLimit: int
        :param _TpsLimit: TPS限流值
        :type TpsLimit: int
        :param _CreatedTime: 创建时间，秒为单位
        :type CreatedTime: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _InstanceStatus: 实例状态
        :type InstanceStatus: str
        :param _SkuCode: 实例规格
        :type SkuCode: str
        :param _MaxSubscriptionPerClient: 单客户端最大订阅数
        :type MaxSubscriptionPerClient: int
        :param _AuthorizationPolicyLimit: 授权规则条数
        :type AuthorizationPolicyLimit: int
        :param _ClientNumLimit: 客户端数量上限
        :type ClientNumLimit: int
        :param _DeviceCertificateProvisionType: 客户端证书注册方式：JITP，API
        :type DeviceCertificateProvisionType: str
        :param _AutomaticActivation: 自动注册设备证书时是否自动激活
        :type AutomaticActivation: bool
        :param _RenewFlag: 是否自动续费
        :type RenewFlag: int
        :param _PayMode: 计费模式， POSTPAID，按量计费 PREPAID，包年包月
        :type PayMode: str
        :param _ExpiryTime: 到期时间，秒为单位
        :type ExpiryTime: int
        :param _DestroyTime: 预销毁时间
        :type DestroyTime: int
        :param _X509Mode:     TLS,单向认证
    mTLS,双向认证
    BYOC;一机一证
        :type X509Mode: str
        :param _MaxCaNum: 最大Ca配额
        :type MaxCaNum: int
        :param _RegistrationCode: 证书注册码
        :type RegistrationCode: str
        :param _MaxSubscription: 集群最大订阅数
        :type MaxSubscription: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceType = None
        self._InstanceId = None
        self._InstanceName = None
        self._TopicNum = None
        self._TopicNumLimit = None
        self._TpsLimit = None
        self._CreatedTime = None
        self._Remark = None
        self._InstanceStatus = None
        self._SkuCode = None
        self._MaxSubscriptionPerClient = None
        self._AuthorizationPolicyLimit = None
        self._ClientNumLimit = None
        self._DeviceCertificateProvisionType = None
        self._AutomaticActivation = None
        self._RenewFlag = None
        self._PayMode = None
        self._ExpiryTime = None
        self._DestroyTime = None
        self._X509Mode = None
        self._MaxCaNum = None
        self._RegistrationCode = None
        self._MaxSubscription = None
        self._RequestId = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

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
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def TopicNumLimit(self):
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def TpsLimit(self):
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SkuCode(self):
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def MaxSubscriptionPerClient(self):
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def AuthorizationPolicyLimit(self):
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def ClientNumLimit(self):
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def DeviceCertificateProvisionType(self):
        return self._DeviceCertificateProvisionType

    @DeviceCertificateProvisionType.setter
    def DeviceCertificateProvisionType(self, DeviceCertificateProvisionType):
        self._DeviceCertificateProvisionType = DeviceCertificateProvisionType

    @property
    def AutomaticActivation(self):
        return self._AutomaticActivation

    @AutomaticActivation.setter
    def AutomaticActivation(self, AutomaticActivation):
        self._AutomaticActivation = AutomaticActivation

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def DestroyTime(self):
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def X509Mode(self):
        return self._X509Mode

    @X509Mode.setter
    def X509Mode(self, X509Mode):
        self._X509Mode = X509Mode

    @property
    def MaxCaNum(self):
        return self._MaxCaNum

    @MaxCaNum.setter
    def MaxCaNum(self, MaxCaNum):
        self._MaxCaNum = MaxCaNum

    @property
    def RegistrationCode(self):
        return self._RegistrationCode

    @RegistrationCode.setter
    def RegistrationCode(self, RegistrationCode):
        self._RegistrationCode = RegistrationCode

    @property
    def MaxSubscription(self):
        return self._MaxSubscription

    @MaxSubscription.setter
    def MaxSubscription(self, MaxSubscription):
        self._MaxSubscription = MaxSubscription

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._TopicNum = params.get("TopicNum")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._TpsLimit = params.get("TpsLimit")
        self._CreatedTime = params.get("CreatedTime")
        self._Remark = params.get("Remark")
        self._InstanceStatus = params.get("InstanceStatus")
        self._SkuCode = params.get("SkuCode")
        self._MaxSubscriptionPerClient = params.get("MaxSubscriptionPerClient")
        self._AuthorizationPolicyLimit = params.get("AuthorizationPolicyLimit")
        self._ClientNumLimit = params.get("ClientNumLimit")
        self._DeviceCertificateProvisionType = params.get("DeviceCertificateProvisionType")
        self._AutomaticActivation = params.get("AutomaticActivation")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._ExpiryTime = params.get("ExpiryTime")
        self._DestroyTime = params.get("DestroyTime")
        self._X509Mode = params.get("X509Mode")
        self._MaxCaNum = params.get("MaxCaNum")
        self._RegistrationCode = params.get("RegistrationCode")
        self._MaxSubscription = params.get("MaxSubscription")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 过滤条件名
        :type Name: str
        :param _Values: 过滤条件的值
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
        


class MQTTInstanceItem(AbstractModel):
    """MQTT 实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Version: 实例版本
        :type Version: str
        :param _InstanceType: 实例类型，
EXPERIMENT，体验版
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :type InstanceType: str
        :param _InstanceStatus: 实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :type InstanceStatus: str
        :param _TopicNumLimit: 实例主题数上限
        :type TopicNumLimit: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _SkuCode: 商品规格
        :type SkuCode: str
        :param _TpsLimit: 弹性TPS限流值
注意：此字段可能返回 null，表示取不到有效值。
        :type TpsLimit: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _MaxSubscriptionPerClient: 单客户端最大订阅数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSubscriptionPerClient: int
        :param _ClientNumLimit: 客户端连接数上线
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientNumLimit: int
        :param _RenewFlag: 是否自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _PayMode: 计费模式， POSTPAID，按量计费 PREPAID，包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _ExpiryTime: 到期时间，秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiryTime: int
        :param _DestroyTime: 预销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DestroyTime: int
        :param _AuthorizationPolicyLimit: 授权规则条数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationPolicyLimit: int
        :param _MaxCaNum: 最大ca配额
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCaNum: int
        :param _MaxSubscription: 最大订阅数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSubscription: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._TopicNumLimit = None
        self._Remark = None
        self._TopicNum = None
        self._SkuCode = None
        self._TpsLimit = None
        self._CreateTime = None
        self._MaxSubscriptionPerClient = None
        self._ClientNumLimit = None
        self._RenewFlag = None
        self._PayMode = None
        self._ExpiryTime = None
        self._DestroyTime = None
        self._AuthorizationPolicyLimit = None
        self._MaxCaNum = None
        self._MaxSubscription = None

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
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TopicNumLimit(self):
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def SkuCode(self):
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def TpsLimit(self):
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MaxSubscriptionPerClient(self):
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def ClientNumLimit(self):
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def DestroyTime(self):
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def AuthorizationPolicyLimit(self):
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def MaxCaNum(self):
        return self._MaxCaNum

    @MaxCaNum.setter
    def MaxCaNum(self, MaxCaNum):
        self._MaxCaNum = MaxCaNum

    @property
    def MaxSubscription(self):
        return self._MaxSubscription

    @MaxSubscription.setter
    def MaxSubscription(self, MaxSubscription):
        self._MaxSubscription = MaxSubscription


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._Remark = params.get("Remark")
        self._TopicNum = params.get("TopicNum")
        self._SkuCode = params.get("SkuCode")
        self._TpsLimit = params.get("TpsLimit")
        self._CreateTime = params.get("CreateTime")
        self._MaxSubscriptionPerClient = params.get("MaxSubscriptionPerClient")
        self._ClientNumLimit = params.get("ClientNumLimit")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._ExpiryTime = params.get("ExpiryTime")
        self._DestroyTime = params.get("DestroyTime")
        self._AuthorizationPolicyLimit = params.get("AuthorizationPolicyLimit")
        self._MaxCaNum = params.get("MaxCaNum")
        self._MaxSubscription = params.get("MaxSubscription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """标签过滤器

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键名称
        :type TagKey: str
        :param _TagValues: 标签键名称
        :type TagValues: list of str
        """
        self._TagKey = None
        self._TagValues = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValues(self):
        return self._TagValues

    @TagValues.setter
    def TagValues(self, TagValues):
        self._TagValues = TagValues


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValues = params.get("TagValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        