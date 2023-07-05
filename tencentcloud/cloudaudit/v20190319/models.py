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


class AttributeKeyDetail(AbstractModel):
    """AttributeKey值详情

    """

    def __init__(self):
        r"""
        :param _LabelType: 输入框类型
        :type LabelType: str
        :param _Starter: 初始化展示
        :type Starter: str
        :param _Order: 展示排序
        :type Order: int
        :param _Value: AttributeKey值
        :type Value: str
        :param _Label: 中文标签
        :type Label: str
        """
        self._LabelType = None
        self._Starter = None
        self._Order = None
        self._Value = None
        self._Label = None

    @property
    def LabelType(self):
        return self._LabelType

    @LabelType.setter
    def LabelType(self, LabelType):
        self._LabelType = LabelType

    @property
    def Starter(self):
        return self._Starter

    @Starter.setter
    def Starter(self, Starter):
        self._Starter = Starter

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._LabelType = params.get("LabelType")
        self._Starter = params.get("Starter")
        self._Order = params.get("Order")
        self._Value = params.get("Value")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditSummary(AbstractModel):
    """跟踪集概览

    """

    def __init__(self):
        r"""
        :param _AuditStatus: 跟踪集状态，1：开启，0：关闭
        :type AuditStatus: int
        :param _CosBucketName: COS存储桶名称
        :type CosBucketName: str
        :param _AuditName: 跟踪集名称
        :type AuditName: str
        :param _LogFilePrefix: 日志前缀
        :type LogFilePrefix: str
        """
        self._AuditStatus = None
        self._CosBucketName = None
        self._AuditName = None
        self._LogFilePrefix = None

    @property
    def AuditStatus(self):
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def AuditName(self):
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName

    @property
    def LogFilePrefix(self):
        return self._LogFilePrefix

    @LogFilePrefix.setter
    def LogFilePrefix(self, LogFilePrefix):
        self._LogFilePrefix = LogFilePrefix


    def _deserialize(self, params):
        self._AuditStatus = params.get("AuditStatus")
        self._CosBucketName = params.get("CosBucketName")
        self._AuditName = params.get("AuditName")
        self._LogFilePrefix = params.get("LogFilePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqRegionInfo(AbstractModel):
    """cmq地域信息

    """

    def __init__(self):
        r"""
        :param _CmqRegionName: 地域描述
        :type CmqRegionName: str
        :param _CmqRegion: cmq地域
        :type CmqRegion: str
        """
        self._CmqRegionName = None
        self._CmqRegion = None

    @property
    def CmqRegionName(self):
        return self._CmqRegionName

    @CmqRegionName.setter
    def CmqRegionName(self, CmqRegionName):
        self._CmqRegionName = CmqRegionName

    @property
    def CmqRegion(self):
        return self._CmqRegion

    @CmqRegion.setter
    def CmqRegion(self, CmqRegion):
        self._CmqRegion = CmqRegion


    def _deserialize(self, params):
        self._CmqRegionName = params.get("CmqRegionName")
        self._CmqRegion = params.get("CmqRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosRegionInfo(AbstractModel):
    """cos地域信息

    """

    def __init__(self):
        r"""
        :param _CosRegion: cos地域
        :type CosRegion: str
        :param _CosRegionName: 地域描述
        :type CosRegionName: str
        """
        self._CosRegion = None
        self._CosRegionName = None

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def CosRegionName(self):
        return self._CosRegionName

    @CosRegionName.setter
    def CosRegionName(self, CosRegionName):
        self._CosRegionName = CosRegionName


    def _deserialize(self, params):
        self._CosRegion = params.get("CosRegion")
        self._CosRegionName = params.get("CosRegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRequest(AbstractModel):
    """CreateAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。目前仅支持cmq的队列服务。如果开启cmq消息通知服务，云审计会将您的日志内容实时投递到您指定地域的指定队列中。
        :type IsEnableCmqNotify: int
        :param _ReadWriteAttribute: 管理事件的读写属性。1：只读，2：只写，3：全部。
        :type ReadWriteAttribute: int
        :param _AuditName: 跟踪集名称。3-128字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9，下划线 _。
        :type AuditName: str
        :param _CosRegion: cos地域。目前支持的地域可以使用ListCosEnableRegion来获取。
        :type CosRegion: str
        :param _IsCreateNewBucket: 是否创建新的cos存储桶。1：是，0：否。
        :type IsCreateNewBucket: int
        :param _CosBucketName: cos的存储桶名称。仅支持小写英文字母和数字即[a-z，0-9]、中划线“-”及其组合。用户自定义的字符串支持1 - 40个字符。存储桶命名不能以“-”开头或结尾。如果不是新创建的存储桶，云审计不会去校验该存储桶是否真的存在，请谨慎填写，避免日志投递不成功，导致您的数据丢失。
        :type CosBucketName: str
        :param _KeyId: CMK的全局唯一标识符，如果不是新创建的kms，该值是必填值。可以通过ListKeyAliasByRegion来获取。云审计不会校验KeyId的合法性，请您谨慎填写，避免给您的数据造成损失。
        :type KeyId: str
        :param _CmqQueueName: 队列名称。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。如果IsEnableCmqNotify值是1的话，此值属于必填字段。如果不是新创建的队列，云审计不会去校验该队列是否真的存在，请谨慎填写，避免日志通知不成功，导致您的数据丢失。
        :type CmqQueueName: str
        :param _KmsRegion: kms地域。目前支持的地域可以使用ListKmsEnableRegion来获取。必须要和cos的地域保持一致。
        :type KmsRegion: str
        :param _IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param _CmqRegion: 队列所在的地域。可以通过ListCmqEnableRegion获取支持的cmq地域。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type CmqRegion: str
        :param _LogFilePrefix: 日志文件前缀。3-40个字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9。可以不填，默认以账号ID作为日志前缀。
        :type LogFilePrefix: str
        :param _IsCreateNewQueue: 是否创建新的队列。1：是，0：否。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type IsCreateNewQueue: int
        """
        self._IsEnableCmqNotify = None
        self._ReadWriteAttribute = None
        self._AuditName = None
        self._CosRegion = None
        self._IsCreateNewBucket = None
        self._CosBucketName = None
        self._KeyId = None
        self._CmqQueueName = None
        self._KmsRegion = None
        self._IsEnableKmsEncry = None
        self._CmqRegion = None
        self._LogFilePrefix = None
        self._IsCreateNewQueue = None

    @property
    def IsEnableCmqNotify(self):
        return self._IsEnableCmqNotify

    @IsEnableCmqNotify.setter
    def IsEnableCmqNotify(self, IsEnableCmqNotify):
        self._IsEnableCmqNotify = IsEnableCmqNotify

    @property
    def ReadWriteAttribute(self):
        return self._ReadWriteAttribute

    @ReadWriteAttribute.setter
    def ReadWriteAttribute(self, ReadWriteAttribute):
        self._ReadWriteAttribute = ReadWriteAttribute

    @property
    def AuditName(self):
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def IsCreateNewBucket(self):
        return self._IsCreateNewBucket

    @IsCreateNewBucket.setter
    def IsCreateNewBucket(self, IsCreateNewBucket):
        self._IsCreateNewBucket = IsCreateNewBucket

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def CmqQueueName(self):
        return self._CmqQueueName

    @CmqQueueName.setter
    def CmqQueueName(self, CmqQueueName):
        self._CmqQueueName = CmqQueueName

    @property
    def KmsRegion(self):
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def IsEnableKmsEncry(self):
        return self._IsEnableKmsEncry

    @IsEnableKmsEncry.setter
    def IsEnableKmsEncry(self, IsEnableKmsEncry):
        self._IsEnableKmsEncry = IsEnableKmsEncry

    @property
    def CmqRegion(self):
        return self._CmqRegion

    @CmqRegion.setter
    def CmqRegion(self, CmqRegion):
        self._CmqRegion = CmqRegion

    @property
    def LogFilePrefix(self):
        return self._LogFilePrefix

    @LogFilePrefix.setter
    def LogFilePrefix(self, LogFilePrefix):
        self._LogFilePrefix = LogFilePrefix

    @property
    def IsCreateNewQueue(self):
        return self._IsCreateNewQueue

    @IsCreateNewQueue.setter
    def IsCreateNewQueue(self, IsCreateNewQueue):
        self._IsCreateNewQueue = IsCreateNewQueue


    def _deserialize(self, params):
        self._IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self._ReadWriteAttribute = params.get("ReadWriteAttribute")
        self._AuditName = params.get("AuditName")
        self._CosRegion = params.get("CosRegion")
        self._IsCreateNewBucket = params.get("IsCreateNewBucket")
        self._CosBucketName = params.get("CosBucketName")
        self._KeyId = params.get("KeyId")
        self._CmqQueueName = params.get("CmqQueueName")
        self._KmsRegion = params.get("KmsRegion")
        self._IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self._CmqRegion = params.get("CmqRegion")
        self._LogFilePrefix = params.get("LogFilePrefix")
        self._IsCreateNewQueue = params.get("IsCreateNewQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditResponse(AbstractModel):
    """CreateAudit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSuccess: 是否创建成功。
        :type IsSuccess: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class CreateAuditTrackRequest(AbstractModel):
    """CreateAuditTrack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 跟踪集名称，仅支持大小写字母、数字、-以及_的组合，3-48个字符
        :type Name: str
        :param _ActionType: 跟踪事件类型（读：Read；写：Write；全部：*）
        :type ActionType: str
        :param _ResourceType: 跟踪事件所属产品（支持全部产品或单个产品，如：cos，全部：*）
        :type ResourceType: str
        :param _Status: 跟踪集状态（未开启：0；开启：1）
        :type Status: int
        :param _EventNames: 跟踪事件接口名列表（ResourceType为 * 时，EventNames必须为全部：["*"]；指定ResourceType时，支持全部接口：["*"]；支持部分接口：["cos", "cls"]，接口列表上限10个）
        :type EventNames: list of str
        :param _Storage: 数据投递存储（目前支持 cos、cls）
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param _TrackForAllMembers: 是否开启将集团成员操作日志投递到集团管理账号或者可信服务管理账号(0：未开启，1：开启，只能集团管理账号或者可信服务管理账号开启此项功能)
        :type TrackForAllMembers: int
        """
        self._Name = None
        self._ActionType = None
        self._ResourceType = None
        self._Status = None
        self._EventNames = None
        self._Storage = None
        self._TrackForAllMembers = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventNames(self):
        return self._EventNames

    @EventNames.setter
    def EventNames(self, EventNames):
        self._EventNames = EventNames

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def TrackForAllMembers(self):
        return self._TrackForAllMembers

    @TrackForAllMembers.setter
    def TrackForAllMembers(self, TrackForAllMembers):
        self._TrackForAllMembers = TrackForAllMembers


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self._Storage = Storage()
            self._Storage._deserialize(params.get("Storage"))
        self._TrackForAllMembers = params.get("TrackForAllMembers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditTrackResponse(AbstractModel):
    """CreateAuditTrack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrackId: 跟踪集 ID
        :type TrackId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrackId = None
        self._RequestId = None

    @property
    def TrackId(self):
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TrackId = params.get("TrackId")
        self._RequestId = params.get("RequestId")


class DeleteAuditRequest(AbstractModel):
    """DeleteAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditName: 跟踪集名称
        :type AuditName: str
        """
        self._AuditName = None

    @property
    def AuditName(self):
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditResponse(AbstractModel):
    """DeleteAudit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSuccess: 是否删除成功
        :type IsSuccess: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class DeleteAuditTrackRequest(AbstractModel):
    """DeleteAuditTrack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrackId: 跟踪集 ID
        :type TrackId: int
        """
        self._TrackId = None

    @property
    def TrackId(self):
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId


    def _deserialize(self, params):
        self._TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditTrackResponse(AbstractModel):
    """DeleteAuditTrack返回参数结构体

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


class DescribeAuditRequest(AbstractModel):
    """DescribeAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditName: 跟踪集名称
        :type AuditName: str
        """
        self._AuditName = None

    @property
    def AuditName(self):
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditResponse(AbstractModel):
    """DescribeAudit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。
        :type IsEnableCmqNotify: int
        :param _ReadWriteAttribute: 管理事件读写属性，1：只读，2：只写，3：全部
        :type ReadWriteAttribute: int
        :param _KeyId: CMK的全局唯一标识符。
        :type KeyId: str
        :param _AuditStatus: 跟踪集状态，1：开启，0：停止。
        :type AuditStatus: int
        :param _AuditName: 跟踪集名称。
        :type AuditName: str
        :param _CosRegion: cos存储桶所在地域。
        :type CosRegion: str
        :param _CmqQueueName: 队列名称。
        :type CmqQueueName: str
        :param _KmsAlias: CMK别名。
        :type KmsAlias: str
        :param _KmsRegion: kms地域。
        :type KmsRegion: str
        :param _IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param _CosBucketName: cos存储桶名称。
        :type CosBucketName: str
        :param _CmqRegion: 队列所在地域。
        :type CmqRegion: str
        :param _LogFilePrefix: 日志前缀。
        :type LogFilePrefix: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsEnableCmqNotify = None
        self._ReadWriteAttribute = None
        self._KeyId = None
        self._AuditStatus = None
        self._AuditName = None
        self._CosRegion = None
        self._CmqQueueName = None
        self._KmsAlias = None
        self._KmsRegion = None
        self._IsEnableKmsEncry = None
        self._CosBucketName = None
        self._CmqRegion = None
        self._LogFilePrefix = None
        self._RequestId = None

    @property
    def IsEnableCmqNotify(self):
        return self._IsEnableCmqNotify

    @IsEnableCmqNotify.setter
    def IsEnableCmqNotify(self, IsEnableCmqNotify):
        self._IsEnableCmqNotify = IsEnableCmqNotify

    @property
    def ReadWriteAttribute(self):
        return self._ReadWriteAttribute

    @ReadWriteAttribute.setter
    def ReadWriteAttribute(self, ReadWriteAttribute):
        self._ReadWriteAttribute = ReadWriteAttribute

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def AuditStatus(self):
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def AuditName(self):
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def CmqQueueName(self):
        return self._CmqQueueName

    @CmqQueueName.setter
    def CmqQueueName(self, CmqQueueName):
        self._CmqQueueName = CmqQueueName

    @property
    def KmsAlias(self):
        return self._KmsAlias

    @KmsAlias.setter
    def KmsAlias(self, KmsAlias):
        self._KmsAlias = KmsAlias

    @property
    def KmsRegion(self):
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def IsEnableKmsEncry(self):
        return self._IsEnableKmsEncry

    @IsEnableKmsEncry.setter
    def IsEnableKmsEncry(self, IsEnableKmsEncry):
        self._IsEnableKmsEncry = IsEnableKmsEncry

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CmqRegion(self):
        return self._CmqRegion

    @CmqRegion.setter
    def CmqRegion(self, CmqRegion):
        self._CmqRegion = CmqRegion

    @property
    def LogFilePrefix(self):
        return self._LogFilePrefix

    @LogFilePrefix.setter
    def LogFilePrefix(self, LogFilePrefix):
        self._LogFilePrefix = LogFilePrefix

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self._ReadWriteAttribute = params.get("ReadWriteAttribute")
        self._KeyId = params.get("KeyId")
        self._AuditStatus = params.get("AuditStatus")
        self._AuditName = params.get("AuditName")
        self._CosRegion = params.get("CosRegion")
        self._CmqQueueName = params.get("CmqQueueName")
        self._KmsAlias = params.get("KmsAlias")
        self._KmsRegion = params.get("KmsRegion")
        self._IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self._CosBucketName = params.get("CosBucketName")
        self._CmqRegion = params.get("CmqRegion")
        self._LogFilePrefix = params.get("LogFilePrefix")
        self._RequestId = params.get("RequestId")


class DescribeAuditTrackRequest(AbstractModel):
    """DescribeAuditTrack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrackId: 跟踪集 ID
        :type TrackId: int
        """
        self._TrackId = None

    @property
    def TrackId(self):
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId


    def _deserialize(self, params):
        self._TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditTrackResponse(AbstractModel):
    """DescribeAuditTrack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 跟踪集名称
        :type Name: str
        :param _ActionType: 跟踪事件类型（读：Read；写：Write；全部：*）
        :type ActionType: str
        :param _ResourceType: 跟踪事件所属产品（如：cos，全部：*）
        :type ResourceType: str
        :param _Status: 跟踪集状态（未开启：0；开启：1）
        :type Status: int
        :param _EventNames: 跟踪事件接口名列表（全部：[*]）
        :type EventNames: list of str
        :param _Storage: 数据投递存储（目前支持 cos、cls）
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param _CreateTime: 跟踪集创建时间
        :type CreateTime: str
        :param _TrackForAllMembers: 是否开启将集团成员操作日志投递到集团管理账号或者可信服务管理账号
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackForAllMembers: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._ActionType = None
        self._ResourceType = None
        self._Status = None
        self._EventNames = None
        self._Storage = None
        self._CreateTime = None
        self._TrackForAllMembers = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventNames(self):
        return self._EventNames

    @EventNames.setter
    def EventNames(self, EventNames):
        self._EventNames = EventNames

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TrackForAllMembers(self):
        return self._TrackForAllMembers

    @TrackForAllMembers.setter
    def TrackForAllMembers(self, TrackForAllMembers):
        self._TrackForAllMembers = TrackForAllMembers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self._Storage = Storage()
            self._Storage._deserialize(params.get("Storage"))
        self._CreateTime = params.get("CreateTime")
        self._TrackForAllMembers = params.get("TrackForAllMembers")
        self._RequestId = params.get("RequestId")


class DescribeAuditTracksRequest(AbstractModel):
    """DescribeAuditTracks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数目
        :type PageSize: int
        """
        self._PageNumber = None
        self._PageSize = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditTracksResponse(AbstractModel):
    """DescribeAuditTracks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tracks: 跟踪集列表
        :type Tracks: list of Tracks
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tracks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tracks(self):
        return self._Tracks

    @Tracks.setter
    def Tracks(self, Tracks):
        self._Tracks = Tracks

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
        if params.get("Tracks") is not None:
            self._Tracks = []
            for item in params.get("Tracks"):
                obj = Tracks()
                obj._deserialize(item)
                self._Tracks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEventsRequest(AbstractModel):
    """DescribeEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间戳（单位秒，不超过当前时间 90 天）
        :type StartTime: int
        :param _EndTime: 结束时间戳（单位秒，查询时间跨度小于 30 天）
        :type EndTime: int
        :param _NextToken: 查看更多日志的凭证
        :type NextToken: int
        :param _MaxResults: 返回日志的最大条数（最大 50 条）
        :type MaxResults: int
        :param _LookupAttributes: 检索条件（目前支持 RequestId：请求 ID、EventName：事件名称、ActionType：操作类型（Write：写；Read：读）、PrincipalId：子账号、ResourceType：资源类型、ResourceName：资源名称、AccessKeyId：密钥 ID、SensitiveAction：是否敏感操作、ApiErrorCode：API 错误码、CamErrorCode：CAM 错误码、Tags：标签（AttributeValue格式：[{"key":"*","value":"*"}]）备注:检索的各个条件间是与的关系,EventName传多个值内部是或的关系）
        :type LookupAttributes: list of LookupAttribute
        :param _IsReturnLocation: 是否返回 IP 归属地（1 返回，0 不返回）
        :type IsReturnLocation: int
        """
        self._StartTime = None
        self._EndTime = None
        self._NextToken = None
        self._MaxResults = None
        self._LookupAttributes = None
        self._IsReturnLocation = None

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
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def LookupAttributes(self):
        return self._LookupAttributes

    @LookupAttributes.setter
    def LookupAttributes(self, LookupAttributes):
        self._LookupAttributes = LookupAttributes

    @property
    def IsReturnLocation(self):
        return self._IsReturnLocation

    @IsReturnLocation.setter
    def IsReturnLocation(self, IsReturnLocation):
        self._IsReturnLocation = IsReturnLocation


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        if params.get("LookupAttributes") is not None:
            self._LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self._LookupAttributes.append(obj)
        self._IsReturnLocation = params.get("IsReturnLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventsResponse(AbstractModel):
    """DescribeEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListOver: 日志集合是否结束。true表示结束，无需进行翻页。
        :type ListOver: bool
        :param _NextToken: 查看更多日志的凭证
        :type NextToken: int
        :param _Events: 日志集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of Event
        :param _TotalCount: 此字段已经废弃。翻页请使用ListOver配合NextToken，在ListOver为false进行下一页数据读取。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListOver = None
        self._NextToken = None
        self._Events = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

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
        self._ListOver = params.get("ListOver")
        self._NextToken = params.get("NextToken")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Event(AbstractModel):
    """日志详情

    """

    def __init__(self):
        r"""
        :param _EventId: 日志ID
        :type EventId: str
        :param _Username: 用户名
        :type Username: str
        :param _EventTime: 事件时间
        :type EventTime: str
        :param _CloudAuditEvent: 日志详情
        :type CloudAuditEvent: str
        :param _ResourceTypeCn: 资源类型中文描述（此字段请按需使用，如果您是其他语言使用者，可以忽略该字段描述）
        :type ResourceTypeCn: str
        :param _ErrorCode: 鉴权错误码
        :type ErrorCode: int
        :param _EventName: 事件名称
        :type EventName: str
        :param _SecretId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretId: str
        :param _EventSource: 请求来源
        :type EventSource: str
        :param _RequestID: 请求ID
        :type RequestID: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param _AccountID: 主账号ID
        :type AccountID: int
        :param _SourceIPAddress: 源IP
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceIPAddress: str
        :param _EventNameCn: 事件名称中文描述（此字段请按需使用，如果您是其他语言使用者，可以忽略该字段描述）
        :type EventNameCn: str
        :param _Resources: 资源对
        :type Resources: :class:`tencentcloud.cloudaudit.v20190319.models.Resource`
        :param _EventRegion: 事件地域
        :type EventRegion: str
        :param _Location: IP 归属地
        :type Location: str
        """
        self._EventId = None
        self._Username = None
        self._EventTime = None
        self._CloudAuditEvent = None
        self._ResourceTypeCn = None
        self._ErrorCode = None
        self._EventName = None
        self._SecretId = None
        self._EventSource = None
        self._RequestID = None
        self._ResourceRegion = None
        self._AccountID = None
        self._SourceIPAddress = None
        self._EventNameCn = None
        self._Resources = None
        self._EventRegion = None
        self._Location = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def EventTime(self):
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def CloudAuditEvent(self):
        return self._CloudAuditEvent

    @CloudAuditEvent.setter
    def CloudAuditEvent(self, CloudAuditEvent):
        self._CloudAuditEvent = CloudAuditEvent

    @property
    def ResourceTypeCn(self):
        return self._ResourceTypeCn

    @ResourceTypeCn.setter
    def ResourceTypeCn(self, ResourceTypeCn):
        self._ResourceTypeCn = ResourceTypeCn

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def SecretId(self):
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def EventSource(self):
        return self._EventSource

    @EventSource.setter
    def EventSource(self, EventSource):
        self._EventSource = EventSource

    @property
    def RequestID(self):
        return self._RequestID

    @RequestID.setter
    def RequestID(self, RequestID):
        self._RequestID = RequestID

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def AccountID(self):
        return self._AccountID

    @AccountID.setter
    def AccountID(self, AccountID):
        self._AccountID = AccountID

    @property
    def SourceIPAddress(self):
        return self._SourceIPAddress

    @SourceIPAddress.setter
    def SourceIPAddress(self, SourceIPAddress):
        self._SourceIPAddress = SourceIPAddress

    @property
    def EventNameCn(self):
        return self._EventNameCn

    @EventNameCn.setter
    def EventNameCn(self, EventNameCn):
        self._EventNameCn = EventNameCn

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def EventRegion(self):
        return self._EventRegion

    @EventRegion.setter
    def EventRegion(self, EventRegion):
        self._EventRegion = EventRegion

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._Username = params.get("Username")
        self._EventTime = params.get("EventTime")
        self._CloudAuditEvent = params.get("CloudAuditEvent")
        self._ResourceTypeCn = params.get("ResourceTypeCn")
        self._ErrorCode = params.get("ErrorCode")
        self._EventName = params.get("EventName")
        self._SecretId = params.get("SecretId")
        self._EventSource = params.get("EventSource")
        self._RequestID = params.get("RequestID")
        self._ResourceRegion = params.get("ResourceRegion")
        self._AccountID = params.get("AccountID")
        self._SourceIPAddress = params.get("SourceIPAddress")
        self._EventNameCn = params.get("EventNameCn")
        if params.get("Resources") is not None:
            self._Resources = Resource()
            self._Resources._deserialize(params.get("Resources"))
        self._EventRegion = params.get("EventRegion")
        self._Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttributeKeyRequest(AbstractModel):
    """GetAttributeKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WebsiteType: 网站类型，取值范围是zh和en。如果不传值默认zh
        :type WebsiteType: str
        """
        self._WebsiteType = None

    @property
    def WebsiteType(self):
        return self._WebsiteType

    @WebsiteType.setter
    def WebsiteType(self, WebsiteType):
        self._WebsiteType = WebsiteType


    def _deserialize(self, params):
        self._WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttributeKeyResponse(AbstractModel):
    """GetAttributeKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttributeKeyDetails: AttributeKey的有效取值范围
        :type AttributeKeyDetails: list of AttributeKeyDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttributeKeyDetails = None
        self._RequestId = None

    @property
    def AttributeKeyDetails(self):
        return self._AttributeKeyDetails

    @AttributeKeyDetails.setter
    def AttributeKeyDetails(self, AttributeKeyDetails):
        self._AttributeKeyDetails = AttributeKeyDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AttributeKeyDetails") is not None:
            self._AttributeKeyDetails = []
            for item in params.get("AttributeKeyDetails"):
                obj = AttributeKeyDetail()
                obj._deserialize(item)
                self._AttributeKeyDetails.append(obj)
        self._RequestId = params.get("RequestId")


class InquireAuditCreditRequest(AbstractModel):
    """InquireAuditCredit请求参数结构体

    """


class InquireAuditCreditResponse(AbstractModel):
    """InquireAuditCredit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditAmount: 可创建跟踪集的数量
        :type AuditAmount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuditAmount = None
        self._RequestId = None

    @property
    def AuditAmount(self):
        return self._AuditAmount

    @AuditAmount.setter
    def AuditAmount(self, AuditAmount):
        self._AuditAmount = AuditAmount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AuditAmount = params.get("AuditAmount")
        self._RequestId = params.get("RequestId")


class KeyMetadata(AbstractModel):
    """CMK属性

    """

    def __init__(self):
        r"""
        :param _Alias: 作为密钥更容易辨识，更容易被人看懂的别名
        :type Alias: str
        :param _KeyId: CMK的全局唯一标识
        :type KeyId: str
        """
        self._Alias = None
        self._KeyId = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuditsRequest(AbstractModel):
    """ListAudits请求参数结构体

    """


class ListAuditsResponse(AbstractModel):
    """ListAudits返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditSummarys: 查询跟踪集概要集合
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditSummarys: list of AuditSummary
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuditSummarys = None
        self._RequestId = None

    @property
    def AuditSummarys(self):
        return self._AuditSummarys

    @AuditSummarys.setter
    def AuditSummarys(self, AuditSummarys):
        self._AuditSummarys = AuditSummarys

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AuditSummarys") is not None:
            self._AuditSummarys = []
            for item in params.get("AuditSummarys"):
                obj = AuditSummary()
                obj._deserialize(item)
                self._AuditSummarys.append(obj)
        self._RequestId = params.get("RequestId")


class ListCmqEnableRegionRequest(AbstractModel):
    """ListCmqEnableRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WebsiteType: 站点类型。zh表示中国区，en表示国际区。默认中国区。
        :type WebsiteType: str
        """
        self._WebsiteType = None

    @property
    def WebsiteType(self):
        return self._WebsiteType

    @WebsiteType.setter
    def WebsiteType(self, WebsiteType):
        self._WebsiteType = WebsiteType


    def _deserialize(self, params):
        self._WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCmqEnableRegionResponse(AbstractModel):
    """ListCmqEnableRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnableRegions: 云审计支持的cmq的可用区
        :type EnableRegions: list of CmqRegionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnableRegions = None
        self._RequestId = None

    @property
    def EnableRegions(self):
        return self._EnableRegions

    @EnableRegions.setter
    def EnableRegions(self, EnableRegions):
        self._EnableRegions = EnableRegions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self._EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CmqRegionInfo()
                obj._deserialize(item)
                self._EnableRegions.append(obj)
        self._RequestId = params.get("RequestId")


class ListCosEnableRegionRequest(AbstractModel):
    """ListCosEnableRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WebsiteType: 站点类型。zh表示中国区，en表示国际区。默认中国区。
        :type WebsiteType: str
        """
        self._WebsiteType = None

    @property
    def WebsiteType(self):
        return self._WebsiteType

    @WebsiteType.setter
    def WebsiteType(self, WebsiteType):
        self._WebsiteType = WebsiteType


    def _deserialize(self, params):
        self._WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCosEnableRegionResponse(AbstractModel):
    """ListCosEnableRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnableRegions: 云审计支持的cos可用区
        :type EnableRegions: list of CosRegionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnableRegions = None
        self._RequestId = None

    @property
    def EnableRegions(self):
        return self._EnableRegions

    @EnableRegions.setter
    def EnableRegions(self, EnableRegions):
        self._EnableRegions = EnableRegions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self._EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CosRegionInfo()
                obj._deserialize(item)
                self._EnableRegions.append(obj)
        self._RequestId = params.get("RequestId")


class ListKeyAliasByRegionRequest(AbstractModel):
    """ListKeyAliasByRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KmsRegion: Kms地域
        :type KmsRegion: str
        :param _Limit: 含义跟 SQL 查询的 Limit 一致，表示本次获最多获取 Limit 个元素。缺省值为10，最大值为200
        :type Limit: int
        :param _Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0
        :type Offset: int
        """
        self._KmsRegion = None
        self._Limit = None
        self._Offset = None

    @property
    def KmsRegion(self):
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

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
        self._KmsRegion = params.get("KmsRegion")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeyAliasByRegionResponse(AbstractModel):
    """ListKeyAliasByRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: CMK的总数量
        :type TotalCount: int
        :param _KeyMetadatas: 密钥别名
        :type KeyMetadatas: list of KeyMetadata
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KeyMetadatas = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KeyMetadatas(self):
        return self._KeyMetadatas

    @KeyMetadatas.setter
    def KeyMetadatas(self, KeyMetadatas):
        self._KeyMetadatas = KeyMetadatas

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KeyMetadatas") is not None:
            self._KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self._KeyMetadatas.append(obj)
        self._RequestId = params.get("RequestId")


class LookUpEventsRequest(AbstractModel):
    """LookUpEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _LookupAttributes: 检索条件
        :type LookupAttributes: list of LookupAttribute
        :param _NextToken: 查看更多日志的凭证
        :type NextToken: str
        :param _MaxResults: 返回日志的最大条数
        :type MaxResults: int
        :param _Mode: 云审计模式，有效值：standard | quick，其中standard是标准模式，quick是极速模式。默认为标准模式
        :type Mode: str
        """
        self._StartTime = None
        self._EndTime = None
        self._LookupAttributes = None
        self._NextToken = None
        self._MaxResults = None
        self._Mode = None

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
    def LookupAttributes(self):
        return self._LookupAttributes

    @LookupAttributes.setter
    def LookupAttributes(self, LookupAttributes):
        self._LookupAttributes = LookupAttributes

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("LookupAttributes") is not None:
            self._LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self._LookupAttributes.append(obj)
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LookUpEventsResponse(AbstractModel):
    """LookUpEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 查看更多日志的凭证
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _Events: 日志集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of Event
        :param _ListOver: 日志集合是否结束
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOver: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._Events = None
        self._ListOver = None
        self._RequestId = None

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextToken = params.get("NextToken")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self._Events.append(obj)
        self._ListOver = params.get("ListOver")
        self._RequestId = params.get("RequestId")


class LookupAttribute(AbstractModel):
    """检索条件

    """

    def __init__(self):
        r"""
        :param _AttributeKey: AttributeKey的有效取值范围是:RequestId、EventName、ReadOnly、Username、ResourceType、ResourceName和AccessKeyId，EventId
        :type AttributeKey: str
        :param _AttributeValue: AttributeValue的值
        :type AttributeValue: str
        """
        self._AttributeKey = None
        self._AttributeValue = None

    @property
    def AttributeKey(self):
        return self._AttributeKey

    @AttributeKey.setter
    def AttributeKey(self, AttributeKey):
        self._AttributeKey = AttributeKey

    @property
    def AttributeValue(self):
        return self._AttributeValue

    @AttributeValue.setter
    def AttributeValue(self, AttributeValue):
        self._AttributeValue = AttributeValue


    def _deserialize(self, params):
        self._AttributeKey = params.get("AttributeKey")
        self._AttributeValue = params.get("AttributeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditTrackRequest(AbstractModel):
    """ModifyAuditTrack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrackId: 跟踪集 ID
        :type TrackId: int
        :param _Name: 跟踪集名称，仅支持大小写字母、数字、-以及_的组合，3-48个字符
        :type Name: str
        :param _ActionType: 跟踪事件类型（读：Read；写：Write；全部：*）
        :type ActionType: str
        :param _ResourceType: 跟踪事件所属产品（支持全部产品或单个产品，如：cos，全部：*）
        :type ResourceType: str
        :param _Status: 跟踪集状态（未开启：0；开启：1）
        :type Status: int
        :param _EventNames: 跟踪事件接口名列表（ResourceType为 * 时，EventNames必须为全部：["*"]；指定ResourceType时，支持全部接口：["*"]；支持部分接口：["cos", "cls"]，接口列表上限10个）
        :type EventNames: list of str
        :param _Storage: 数据投递存储（目前支持 cos、cls）
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param _TrackForAllMembers: 是否开启将集团成员操作日志投递到集团管理账号或者可信服务管理账号(0：未开启，1：开启，只能集团管理账号或者可信服务管理账号开启此项功能)
        :type TrackForAllMembers: int
        """
        self._TrackId = None
        self._Name = None
        self._ActionType = None
        self._ResourceType = None
        self._Status = None
        self._EventNames = None
        self._Storage = None
        self._TrackForAllMembers = None

    @property
    def TrackId(self):
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventNames(self):
        return self._EventNames

    @EventNames.setter
    def EventNames(self, EventNames):
        self._EventNames = EventNames

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def TrackForAllMembers(self):
        return self._TrackForAllMembers

    @TrackForAllMembers.setter
    def TrackForAllMembers(self, TrackForAllMembers):
        self._TrackForAllMembers = TrackForAllMembers


    def _deserialize(self, params):
        self._TrackId = params.get("TrackId")
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self._Storage = Storage()
            self._Storage._deserialize(params.get("Storage"))
        self._TrackForAllMembers = params.get("TrackForAllMembers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditTrackResponse(AbstractModel):
    """ModifyAuditTrack返回参数结构体

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


class Resource(AbstractModel):
    """资源类型

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        """
        self._ResourceType = None
        self._ResourceName = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLoggingRequest(AbstractModel):
    """StartLogging请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditName: 跟踪集名称
        :type AuditName: str
        """
        self._AuditName = None

    @property
    def AuditName(self):
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLoggingResponse(AbstractModel):
    """StartLogging返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSuccess: 是否开启成功
        :type IsSuccess: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class StopLoggingRequest(AbstractModel):
    """StopLogging请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditName: 跟踪集名称
        :type AuditName: str
        """
        self._AuditName = None

    @property
    def AuditName(self):
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLoggingResponse(AbstractModel):
    """StopLogging返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSuccess: 是否关闭成功
        :type IsSuccess: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class Storage(AbstractModel):
    """跟踪集存储信息

    """

    def __init__(self):
        r"""
        :param _StorageType: 存储类型（目前支持 cos、cls）
        :type StorageType: str
        :param _StorageRegion: 存储所在地域
        :type StorageRegion: str
        :param _StorageName: 存储名称(cos：存储名称为用户自定义的存储桶名称，不包含"-APPID"，仅支持小写字母、数字以及中划线"-"的组合，不能超过50字符，且不支持中划线"-"开头或结尾； cls：存储名称为日志主题id，字符长度为1-50个字符)
        :type StorageName: str
        :param _StoragePrefix: 存储目录前缀，cos日志文件前缀仅支持字母和数字的组合，3-40个字符
        :type StoragePrefix: str
        """
        self._StorageType = None
        self._StorageRegion = None
        self._StorageName = None
        self._StoragePrefix = None

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageRegion(self):
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def StorageName(self):
        return self._StorageName

    @StorageName.setter
    def StorageName(self, StorageName):
        self._StorageName = StorageName

    @property
    def StoragePrefix(self):
        return self._StoragePrefix

    @StoragePrefix.setter
    def StoragePrefix(self, StoragePrefix):
        self._StoragePrefix = StoragePrefix


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._StorageRegion = params.get("StorageRegion")
        self._StorageName = params.get("StorageName")
        self._StoragePrefix = params.get("StoragePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tracks(AbstractModel):
    """跟踪集列表

    """

    def __init__(self):
        r"""
        :param _Name: 跟踪集名称
        :type Name: str
        :param _ActionType: 跟踪事件类型（读：Read；写：Write；全部：*）
        :type ActionType: str
        :param _ResourceType: 跟踪事件所属产品（如：cos，全部：*）
        :type ResourceType: str
        :param _Status: 跟踪集状态（未开启：0；开启：1）
        :type Status: int
        :param _EventNames: 跟踪事件接口名列表（全部：[*]）
        :type EventNames: list of str
        :param _Storage: 数据投递存储（目前支持 cos、cls）
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param _CreateTime: 跟踪集创建时间
        :type CreateTime: str
        :param _TrackId: 跟踪集 ID
        :type TrackId: int
        """
        self._Name = None
        self._ActionType = None
        self._ResourceType = None
        self._Status = None
        self._EventNames = None
        self._Storage = None
        self._CreateTime = None
        self._TrackId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventNames(self):
        return self._EventNames

    @EventNames.setter
    def EventNames(self, EventNames):
        self._EventNames = EventNames

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TrackId(self):
        return self._TrackId

    @TrackId.setter
    def TrackId(self, TrackId):
        self._TrackId = TrackId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self._Storage = Storage()
            self._Storage._deserialize(params.get("Storage"))
        self._CreateTime = params.get("CreateTime")
        self._TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuditRequest(AbstractModel):
    """UpdateAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditName: 跟踪集名称
        :type AuditName: str
        :param _IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。目前仅支持cmq的队列服务。如果开启cmq消息通知服务，云审计会将您的日志内容实时投递到您指定地域的指定队列中。
        :type IsEnableCmqNotify: int
        :param _ReadWriteAttribute: 管理事件的读写属性。1：只读，2：只写，3：全部。
        :type ReadWriteAttribute: int
        :param _KeyId: CMK的全局唯一标识符，如果不是新创建的kms，该值是必填值。可以通过ListKeyAliasByRegion来获取。云审计不会校验KeyId的合法性，请您谨慎填写，避免给您的数据造成损失。
        :type KeyId: str
        :param _CosRegion: cos地域。目前支持的地域可以使用ListCosEnableRegion来获取。
        :type CosRegion: str
        :param _CmqQueueName: 队列名称。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。如果IsEnableCmqNotify值是1的话，此值属于必填字段。如果不是新创建的队列，云审计不会去校验该队列是否真的存在，请谨慎填写，避免日志通知不成功，导致您的数据丢失。
        :type CmqQueueName: str
        :param _IsCreateNewBucket: 是否创建新的cos存储桶。1：是，0：否。
        :type IsCreateNewBucket: int
        :param _KmsRegion: kms地域。目前支持的地域可以使用ListKmsEnableRegion来获取。必须要和cos的地域保持一致。
        :type KmsRegion: str
        :param _IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param _CosBucketName: cos的存储桶名称。仅支持小写英文字母和数字即[a-z，0-9]、中划线“-”及其组合。用户自定义的字符串支持1 - 40个字符。存储桶命名不能以“-”开头或结尾。如果不是新创建的存储桶，云审计不会去校验该存储桶是否真的存在，请谨慎填写，避免日志投递不成功，导致您的数据丢失。
        :type CosBucketName: str
        :param _CmqRegion: 队列所在的地域。可以通过ListCmqEnableRegion获取支持的cmq地域。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type CmqRegion: str
        :param _LogFilePrefix: 日志文件前缀。3-40个字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9。
        :type LogFilePrefix: str
        :param _IsCreateNewQueue: 是否创建新的队列。1：是，0：否。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type IsCreateNewQueue: int
        """
        self._AuditName = None
        self._IsEnableCmqNotify = None
        self._ReadWriteAttribute = None
        self._KeyId = None
        self._CosRegion = None
        self._CmqQueueName = None
        self._IsCreateNewBucket = None
        self._KmsRegion = None
        self._IsEnableKmsEncry = None
        self._CosBucketName = None
        self._CmqRegion = None
        self._LogFilePrefix = None
        self._IsCreateNewQueue = None

    @property
    def AuditName(self):
        return self._AuditName

    @AuditName.setter
    def AuditName(self, AuditName):
        self._AuditName = AuditName

    @property
    def IsEnableCmqNotify(self):
        return self._IsEnableCmqNotify

    @IsEnableCmqNotify.setter
    def IsEnableCmqNotify(self, IsEnableCmqNotify):
        self._IsEnableCmqNotify = IsEnableCmqNotify

    @property
    def ReadWriteAttribute(self):
        return self._ReadWriteAttribute

    @ReadWriteAttribute.setter
    def ReadWriteAttribute(self, ReadWriteAttribute):
        self._ReadWriteAttribute = ReadWriteAttribute

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def CmqQueueName(self):
        return self._CmqQueueName

    @CmqQueueName.setter
    def CmqQueueName(self, CmqQueueName):
        self._CmqQueueName = CmqQueueName

    @property
    def IsCreateNewBucket(self):
        return self._IsCreateNewBucket

    @IsCreateNewBucket.setter
    def IsCreateNewBucket(self, IsCreateNewBucket):
        self._IsCreateNewBucket = IsCreateNewBucket

    @property
    def KmsRegion(self):
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def IsEnableKmsEncry(self):
        return self._IsEnableKmsEncry

    @IsEnableKmsEncry.setter
    def IsEnableKmsEncry(self, IsEnableKmsEncry):
        self._IsEnableKmsEncry = IsEnableKmsEncry

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CmqRegion(self):
        return self._CmqRegion

    @CmqRegion.setter
    def CmqRegion(self, CmqRegion):
        self._CmqRegion = CmqRegion

    @property
    def LogFilePrefix(self):
        return self._LogFilePrefix

    @LogFilePrefix.setter
    def LogFilePrefix(self, LogFilePrefix):
        self._LogFilePrefix = LogFilePrefix

    @property
    def IsCreateNewQueue(self):
        return self._IsCreateNewQueue

    @IsCreateNewQueue.setter
    def IsCreateNewQueue(self, IsCreateNewQueue):
        self._IsCreateNewQueue = IsCreateNewQueue


    def _deserialize(self, params):
        self._AuditName = params.get("AuditName")
        self._IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self._ReadWriteAttribute = params.get("ReadWriteAttribute")
        self._KeyId = params.get("KeyId")
        self._CosRegion = params.get("CosRegion")
        self._CmqQueueName = params.get("CmqQueueName")
        self._IsCreateNewBucket = params.get("IsCreateNewBucket")
        self._KmsRegion = params.get("KmsRegion")
        self._IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self._CosBucketName = params.get("CosBucketName")
        self._CmqRegion = params.get("CmqRegion")
        self._LogFilePrefix = params.get("LogFilePrefix")
        self._IsCreateNewQueue = params.get("IsCreateNewQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuditResponse(AbstractModel):
    """UpdateAudit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSuccess: 是否更新成功
        :type IsSuccess: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsSuccess = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")