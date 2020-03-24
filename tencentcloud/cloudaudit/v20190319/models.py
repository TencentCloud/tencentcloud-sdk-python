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


class AttributeKeyDetail(AbstractModel):
    """AttributeKey值详情

    """

    def __init__(self):
        """
        :param Label: 中文标签
        :type Label: str
        :param LabelType: 输入框类型
        :type LabelType: str
        :param Order: 展示排序
        :type Order: int
        :param Starter: 初始化展示
        :type Starter: str
        :param Value: AttributeKey值
        :type Value: str
        """
        self.Label = None
        self.LabelType = None
        self.Order = None
        self.Starter = None
        self.Value = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.LabelType = params.get("LabelType")
        self.Order = params.get("Order")
        self.Starter = params.get("Starter")
        self.Value = params.get("Value")


class AuditSummary(AbstractModel):
    """跟踪集概览

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称
        :type AuditName: str
        :param AuditStatus: 跟踪集状态，1：开启，0：关闭
        :type AuditStatus: int
        :param CosBucketName: COS存储桶名称
        :type CosBucketName: str
        :param LogFilePrefix: 日志前缀
        :type LogFilePrefix: str
        """
        self.AuditName = None
        self.AuditStatus = None
        self.CosBucketName = None
        self.LogFilePrefix = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.AuditStatus = params.get("AuditStatus")
        self.CosBucketName = params.get("CosBucketName")
        self.LogFilePrefix = params.get("LogFilePrefix")


class CmqRegionInfo(AbstractModel):
    """cmq地域信息

    """

    def __init__(self):
        """
        :param CmqRegion: cmq地域
        :type CmqRegion: str
        :param CmqRegionName: 地域描述
        :type CmqRegionName: str
        """
        self.CmqRegion = None
        self.CmqRegionName = None


    def _deserialize(self, params):
        self.CmqRegion = params.get("CmqRegion")
        self.CmqRegionName = params.get("CmqRegionName")


class CosRegionInfo(AbstractModel):
    """cmq地域信息

    """

    def __init__(self):
        """
        :param CosRegion: cos地域
        :type CosRegion: str
        :param CosRegionName: 地域描述
        :type CosRegionName: str
        """
        self.CosRegion = None
        self.CosRegionName = None


    def _deserialize(self, params):
        self.CosRegion = params.get("CosRegion")
        self.CosRegionName = params.get("CosRegionName")


class CreateAuditRequest(AbstractModel):
    """CreateAudit请求参数结构体

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称。3-128字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9，下划线 _。
        :type AuditName: str
        :param CosBucketName: cos的存储桶名称。仅支持小写英文字母和数字即[a-z，0-9]、中划线“-”及其组合。用户自定义的字符串支持1 - 40个字符。存储桶命名不能以“-”开头或结尾。如果不是新创建的存储桶，云审计不会去校验该存储桶是否真的存在，请谨慎填写，避免日志投递不成功，导致您的数据丢失。
        :type CosBucketName: str
        :param CosRegion: cos地域。目前支持的地域可以使用ListCosEnableRegion来获取。
        :type CosRegion: str
        :param IsCreateNewBucket: 是否创建新的cos存储桶。1：是，0：否。
        :type IsCreateNewBucket: int
        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。目前仅支持cmq的队列服务。如果开启cmq消息通知服务，云审计会将您的日志内容实时投递到您指定地域的指定队列中。
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: 管理事件的读写属性。1：只读，2：只写，3：全部。
        :type ReadWriteAttribute: int
        :param CmqQueueName: 队列名称。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。如果IsEnableCmqNotify值是1的话，此值属于必填字段。如果不是新创建的队列，云审计不会去校验该队列是否真的存在，请谨慎填写，避免日志通知不成功，导致您的数据丢失。
        :type CmqQueueName: str
        :param CmqRegion: 队列所在的地域。可以通过ListCmqEnableRegion获取支持的cmq地域。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type CmqRegion: str
        :param IsCreateNewQueue: 是否创建新的队列。1：是，0：否。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type IsCreateNewQueue: int
        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param KeyId: CMK的全局唯一标识符，如果不是新创建的kms，该值是必填值。可以通过ListKeyAliasByRegion来获取。云审计不会校验KeyId的合法性，请您谨慎填写，避免给您的数据造成损失。
        :type KeyId: str
        :param KmsRegion: kms地域。目前支持的地域可以使用ListKmsEnableRegion来获取。必须要和cos的地域保持一致。
        :type KmsRegion: str
        :param LogFilePrefix: 日志文件前缀。3-40个字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9。可以不填，默认以账号ID作为日志前缀。
        :type LogFilePrefix: str
        """
        self.AuditName = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsCreateNewBucket = None
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.IsCreateNewQueue = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsRegion = None
        self.LogFilePrefix = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")


class CreateAuditResponse(AbstractModel):
    """CreateAudit返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否创建成功。
        :type IsSuccess: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DeleteAuditRequest(AbstractModel):
    """DeleteAudit请求参数结构体

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class DeleteAuditResponse(AbstractModel):
    """DeleteAudit返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否删除成功
        :type IsSuccess: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DescribeAuditRequest(AbstractModel):
    """DescribeAudit请求参数结构体

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class DescribeAuditResponse(AbstractModel):
    """DescribeAudit返回参数结构体

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称。
        :type AuditName: str
        :param AuditStatus: 跟踪集状态，1：开启，0：停止。
        :type AuditStatus: int
        :param CmqQueueName: 队列名称。
        :type CmqQueueName: str
        :param CmqRegion: 队列所在地域。
        :type CmqRegion: str
        :param CosBucketName: cos存储桶名称。
        :type CosBucketName: str
        :param CosRegion: cos存储桶所在地域。
        :type CosRegion: str
        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。
        :type IsEnableCmqNotify: int
        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param KeyId: CMK的全局唯一标识符。
        :type KeyId: str
        :param KmsAlias: CMK别名。
        :type KmsAlias: str
        :param KmsRegion: kms地域。
        :type KmsRegion: str
        :param LogFilePrefix: 日志前缀。
        :type LogFilePrefix: str
        :param ReadWriteAttribute: 管理事件读写属性，1：只读，2：只写，3：全部
        :type ReadWriteAttribute: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuditName = None
        self.AuditStatus = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsEnableCmqNotify = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsAlias = None
        self.KmsRegion = None
        self.LogFilePrefix = None
        self.ReadWriteAttribute = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.AuditStatus = params.get("AuditStatus")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsAlias = params.get("KmsAlias")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.RequestId = params.get("RequestId")


class Event(AbstractModel):
    """日志详情

    """

    def __init__(self):
        """
        :param Resources: 资源对
        :type Resources: :class:`tencentcloud.cloudaudit.v20190319.models.Resource`
        :param AccountID: 主账号ID
        :type AccountID: int
        :param CloudAuditEvent: 日志详情
        :type CloudAuditEvent: str
        :param ErrorCode: 鉴权错误码
        :type ErrorCode: int
        :param EventId: 日志ID
        :type EventId: str
        :param EventName: 事件名称
        :type EventName: str
        :param EventNameCn: 事件名称中文描述（此字段请按需使用，如果您是其他语言使用者，可以忽略该字段描述）
        :type EventNameCn: str
        :param EventRegion: 事件地域
        :type EventRegion: str
        :param EventSource: 请求来源
        :type EventSource: str
        :param EventTime: 事件时间
        :type EventTime: str
        :param RequestID: 请求ID
        :type RequestID: str
        :param ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param ResourceTypeCn: 资源类型中文描述（此字段请按需使用，如果您是其他语言使用者，可以忽略该字段描述）
        :type ResourceTypeCn: str
        :param SecretId: 证书ID
        :type SecretId: str
        :param SourceIPAddress: 源IP
        :type SourceIPAddress: str
        :param Username: 用户名
        :type Username: str
        """
        self.Resources = None
        self.AccountID = None
        self.CloudAuditEvent = None
        self.ErrorCode = None
        self.EventId = None
        self.EventName = None
        self.EventNameCn = None
        self.EventRegion = None
        self.EventSource = None
        self.EventTime = None
        self.RequestID = None
        self.ResourceRegion = None
        self.ResourceTypeCn = None
        self.SecretId = None
        self.SourceIPAddress = None
        self.Username = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = Resource()
            self.Resources._deserialize(params.get("Resources"))
        self.AccountID = params.get("AccountID")
        self.CloudAuditEvent = params.get("CloudAuditEvent")
        self.ErrorCode = params.get("ErrorCode")
        self.EventId = params.get("EventId")
        self.EventName = params.get("EventName")
        self.EventNameCn = params.get("EventNameCn")
        self.EventRegion = params.get("EventRegion")
        self.EventSource = params.get("EventSource")
        self.EventTime = params.get("EventTime")
        self.RequestID = params.get("RequestID")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourceTypeCn = params.get("ResourceTypeCn")
        self.SecretId = params.get("SecretId")
        self.SourceIPAddress = params.get("SourceIPAddress")
        self.Username = params.get("Username")


class GetAttributeKeyRequest(AbstractModel):
    """GetAttributeKey请求参数结构体

    """

    def __init__(self):
        """
        :param WebsiteType: 网站类型，取值范围是zh和en。如果不传值默认zh
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class GetAttributeKeyResponse(AbstractModel):
    """GetAttributeKey返回参数结构体

    """

    def __init__(self):
        """
        :param AttributeKeyDetails: AttributeKey的有效取值范围
        :type AttributeKeyDetails: list of AttributeKeyDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AttributeKeyDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttributeKeyDetails") is not None:
            self.AttributeKeyDetails = []
            for item in params.get("AttributeKeyDetails"):
                obj = AttributeKeyDetail()
                obj._deserialize(item)
                self.AttributeKeyDetails.append(obj)
        self.RequestId = params.get("RequestId")


class InquireAuditCreditRequest(AbstractModel):
    """InquireAuditCredit请求参数结构体

    """


class InquireAuditCreditResponse(AbstractModel):
    """InquireAuditCredit返回参数结构体

    """

    def __init__(self):
        """
        :param AuditAmount: 可创建跟踪集的数量
        :type AuditAmount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuditAmount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditAmount = params.get("AuditAmount")
        self.RequestId = params.get("RequestId")


class ListAuditsRequest(AbstractModel):
    """ListAudits请求参数结构体

    """


class ListAuditsResponse(AbstractModel):
    """ListAudits返回参数结构体

    """

    def __init__(self):
        """
        :param AuditSummarys: 查询跟踪集概要集合
        :type AuditSummarys: list of AuditSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuditSummarys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuditSummarys") is not None:
            self.AuditSummarys = []
            for item in params.get("AuditSummarys"):
                obj = AuditSummary()
                obj._deserialize(item)
                self.AuditSummarys.append(obj)
        self.RequestId = params.get("RequestId")


class ListCmqEnableRegionRequest(AbstractModel):
    """ListCmqEnableRegion请求参数结构体

    """

    def __init__(self):
        """
        :param WebsiteType: 站点类型。zh表示中国区，en表示国际区。默认中国区。
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class ListCmqEnableRegionResponse(AbstractModel):
    """ListCmqEnableRegion返回参数结构体

    """

    def __init__(self):
        """
        :param EnableRegions: 云审计支持的cmq的可用区
        :type EnableRegions: list of CmqRegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnableRegions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self.EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CmqRegionInfo()
                obj._deserialize(item)
                self.EnableRegions.append(obj)
        self.RequestId = params.get("RequestId")


class ListCosEnableRegionRequest(AbstractModel):
    """ListCosEnableRegion请求参数结构体

    """

    def __init__(self):
        """
        :param WebsiteType: 站点类型。zh表示中国区，en表示国际区。默认中国区。
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class ListCosEnableRegionResponse(AbstractModel):
    """ListCosEnableRegion返回参数结构体

    """

    def __init__(self):
        """
        :param EnableRegions: 云审计支持的cos可用区
        :type EnableRegions: list of CosRegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnableRegions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self.EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CosRegionInfo()
                obj._deserialize(item)
                self.EnableRegions.append(obj)
        self.RequestId = params.get("RequestId")


class LookUpEventsRequest(AbstractModel):
    """LookUpEvents请求参数结构体

    """

    def __init__(self):
        """
        :param EndTime: 结束时间
        :type EndTime: int
        :param StartTime: 开始时间
        :type StartTime: int
        :param LookupAttributes: 检索条件
        :type LookupAttributes: list of LookupAttribute
        :param MaxResults: 返回日志的最大条数
        :type MaxResults: int
        :param Mode: 云审计模式，有效值：standard | quick，其中standard是标准模式，quick是极速模式。默认为标准模式
        :type Mode: str
        :param NextToken: 查看更多日志的凭证
        :type NextToken: str
        """
        self.EndTime = None
        self.StartTime = None
        self.LookupAttributes = None
        self.MaxResults = None
        self.Mode = None
        self.NextToken = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        if params.get("LookupAttributes") is not None:
            self.LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self.LookupAttributes.append(obj)
        self.MaxResults = params.get("MaxResults")
        self.Mode = params.get("Mode")
        self.NextToken = params.get("NextToken")


class LookUpEventsResponse(AbstractModel):
    """LookUpEvents返回参数结构体

    """

    def __init__(self):
        """
        :param Events: 日志集合
        :type Events: list of Event
        :param ListOver: 日志集合是否结束
        :type ListOver: bool
        :param NextToken: 查看更多日志的凭证
        :type NextToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.ListOver = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.ListOver = params.get("ListOver")
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class LookupAttribute(AbstractModel):
    """检索条件

    """

    def __init__(self):
        """
        :param AttributeKey: AttributeKey的有效取值范围是:RequestId、EventName、ReadOnly、Username、ResourceType、ResourceName和AccessKeyId，EventId
        :type AttributeKey: str
        :param AttributeValue: AttributeValue
        :type AttributeValue: str
        """
        self.AttributeKey = None
        self.AttributeValue = None


    def _deserialize(self, params):
        self.AttributeKey = params.get("AttributeKey")
        self.AttributeValue = params.get("AttributeValue")


class Resource(AbstractModel):
    """资源类型

    """

    def __init__(self):
        """
        :param ResourceName: 资源名称
        :type ResourceName: str
        :param ResourceType: 资源类型
        :type ResourceType: str
        """
        self.ResourceName = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.ResourceName = params.get("ResourceName")
        self.ResourceType = params.get("ResourceType")


class StartLoggingRequest(AbstractModel):
    """StartLogging请求参数结构体

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class StartLoggingResponse(AbstractModel):
    """StartLogging返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否开启成功
        :type IsSuccess: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class StopLoggingRequest(AbstractModel):
    """StopLogging请求参数结构体

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class StopLoggingResponse(AbstractModel):
    """StopLogging返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否关闭成功
        :type IsSuccess: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class UpdateAuditRequest(AbstractModel):
    """UpdateAudit请求参数结构体

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称
        :type AuditName: str
        :param CmqQueueName: 队列名称。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。如果IsEnableCmqNotify值是1的话，此值属于必填字段。如果不是新创建的队列，云审计不会去校验该队列是否真的存在，请谨慎填写，避免日志通知不成功，导致您的数据丢失。
        :type CmqQueueName: str
        :param CmqRegion: 队列所在的地域。可以通过ListCmqEnableRegion获取支持的cmq地域。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type CmqRegion: str
        :param CosBucketName: cos的存储桶名称。仅支持小写英文字母和数字即[a-z，0-9]、中划线“-”及其组合。用户自定义的字符串支持1 - 40个字符。存储桶命名不能以“-”开头或结尾。如果不是新创建的存储桶，云审计不会去校验该存储桶是否真的存在，请谨慎填写，避免日志投递不成功，导致您的数据丢失。
        :type CosBucketName: str
        :param CosRegion: cos地域。目前支持的地域可以使用ListCosEnableRegion来获取。
        :type CosRegion: str
        :param IsCreateNewBucket: 是否创建新的cos存储桶。1：是，0：否。
        :type IsCreateNewBucket: int
        :param IsCreateNewQueue: 是否创建新的队列。1：是，0：否。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type IsCreateNewQueue: int
        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。目前仅支持cmq的队列服务。如果开启cmq消息通知服务，云审计会将您的日志内容实时投递到您指定地域的指定队列中。
        :type IsEnableCmqNotify: int
        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param KeyId: CMK的全局唯一标识符，如果不是新创建的kms，该值是必填值。可以通过ListKeyAliasByRegion来获取。云审计不会校验KeyId的合法性，请您谨慎填写，避免给您的数据造成损失。
        :type KeyId: str
        :param KmsRegion: kms地域。目前支持的地域可以使用ListKmsEnableRegion来获取。必须要和cos的地域保持一致。
        :type KmsRegion: str
        :param LogFilePrefix: 日志文件前缀。3-40个字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9。
        :type LogFilePrefix: str
        :param ReadWriteAttribute: 管理事件的读写属性。1：只读，2：只写，3：全部。
        :type ReadWriteAttribute: int
        """
        self.AuditName = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsCreateNewBucket = None
        self.IsCreateNewQueue = None
        self.IsEnableCmqNotify = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsRegion = None
        self.LogFilePrefix = None
        self.ReadWriteAttribute = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")


class UpdateAuditResponse(AbstractModel):
    """UpdateAudit返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否更新成功
        :type IsSuccess: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")