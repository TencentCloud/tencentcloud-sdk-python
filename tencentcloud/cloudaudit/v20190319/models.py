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
        """
        :param LabelType: 输入框类型\n        :type LabelType: str\n        :param Starter: 初始化展示\n        :type Starter: str\n        :param Order: 展示排序\n        :type Order: int\n        :param Value: AttributeKey值\n        :type Value: str\n        :param Label: 中文标签\n        :type Label: str\n        """
        self.LabelType = None
        self.Starter = None
        self.Order = None
        self.Value = None
        self.Label = None


    def _deserialize(self, params):
        self.LabelType = params.get("LabelType")
        self.Starter = params.get("Starter")
        self.Order = params.get("Order")
        self.Value = params.get("Value")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditSummary(AbstractModel):
    """跟踪集概览

    """

    def __init__(self):
        """
        :param AuditStatus: 跟踪集状态，1：开启，0：关闭\n        :type AuditStatus: int\n        :param CosBucketName: COS存储桶名称\n        :type CosBucketName: str\n        :param AuditName: 跟踪集名称\n        :type AuditName: str\n        :param LogFilePrefix: 日志前缀\n        :type LogFilePrefix: str\n        """
        self.AuditStatus = None
        self.CosBucketName = None
        self.AuditName = None
        self.LogFilePrefix = None


    def _deserialize(self, params):
        self.AuditStatus = params.get("AuditStatus")
        self.CosBucketName = params.get("CosBucketName")
        self.AuditName = params.get("AuditName")
        self.LogFilePrefix = params.get("LogFilePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqRegionInfo(AbstractModel):
    """cmq地域信息

    """

    def __init__(self):
        """
        :param CmqRegionName: 地域描述\n        :type CmqRegionName: str\n        :param CmqRegion: cmq地域\n        :type CmqRegion: str\n        """
        self.CmqRegionName = None
        self.CmqRegion = None


    def _deserialize(self, params):
        self.CmqRegionName = params.get("CmqRegionName")
        self.CmqRegion = params.get("CmqRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosRegionInfo(AbstractModel):
    """cos地域信息

    """

    def __init__(self):
        """
        :param CosRegion: cos地域\n        :type CosRegion: str\n        :param CosRegionName: 地域描述\n        :type CosRegionName: str\n        """
        self.CosRegion = None
        self.CosRegionName = None


    def _deserialize(self, params):
        self.CosRegion = params.get("CosRegion")
        self.CosRegionName = params.get("CosRegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRequest(AbstractModel):
    """CreateAudit请求参数结构体

    """

    def __init__(self):
        """
        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。目前仅支持cmq的队列服务。如果开启cmq消息通知服务，云审计会将您的日志内容实时投递到您指定地域的指定队列中。\n        :type IsEnableCmqNotify: int\n        :param ReadWriteAttribute: 管理事件的读写属性。1：只读，2：只写，3：全部。\n        :type ReadWriteAttribute: int\n        :param AuditName: 跟踪集名称。3-128字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9，下划线 _。\n        :type AuditName: str\n        :param CosRegion: cos地域。目前支持的地域可以使用ListCosEnableRegion来获取。\n        :type CosRegion: str\n        :param IsCreateNewBucket: 是否创建新的cos存储桶。1：是，0：否。\n        :type IsCreateNewBucket: int\n        :param CosBucketName: cos的存储桶名称。仅支持小写英文字母和数字即[a-z，0-9]、中划线“-”及其组合。用户自定义的字符串支持1 - 40个字符。存储桶命名不能以“-”开头或结尾。如果不是新创建的存储桶，云审计不会去校验该存储桶是否真的存在，请谨慎填写，避免日志投递不成功，导致您的数据丢失。\n        :type CosBucketName: str\n        :param KeyId: CMK的全局唯一标识符，如果不是新创建的kms，该值是必填值。可以通过ListKeyAliasByRegion来获取。云审计不会校验KeyId的合法性，请您谨慎填写，避免给您的数据造成损失。\n        :type KeyId: str\n        :param CmqQueueName: 队列名称。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。如果IsEnableCmqNotify值是1的话，此值属于必填字段。如果不是新创建的队列，云审计不会去校验该队列是否真的存在，请谨慎填写，避免日志通知不成功，导致您的数据丢失。\n        :type CmqQueueName: str\n        :param KmsRegion: kms地域。目前支持的地域可以使用ListKmsEnableRegion来获取。必须要和cos的地域保持一致。\n        :type KmsRegion: str\n        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。\n        :type IsEnableKmsEncry: int\n        :param CmqRegion: 队列所在的地域。可以通过ListCmqEnableRegion获取支持的cmq地域。如果IsEnableCmqNotify值是1的话，此值属于必填字段。\n        :type CmqRegion: str\n        :param LogFilePrefix: 日志文件前缀。3-40个字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9。可以不填，默认以账号ID作为日志前缀。\n        :type LogFilePrefix: str\n        :param IsCreateNewQueue: 是否创建新的队列。1：是，0：否。如果IsEnableCmqNotify值是1的话，此值属于必填字段。\n        :type IsCreateNewQueue: int\n        """
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.AuditName = None
        self.CosRegion = None
        self.IsCreateNewBucket = None
        self.CosBucketName = None
        self.KeyId = None
        self.CmqQueueName = None
        self.KmsRegion = None
        self.IsEnableKmsEncry = None
        self.CmqRegion = None
        self.LogFilePrefix = None
        self.IsCreateNewQueue = None


    def _deserialize(self, params):
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.AuditName = params.get("AuditName")
        self.CosRegion = params.get("CosRegion")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.CosBucketName = params.get("CosBucketName")
        self.KeyId = params.get("KeyId")
        self.CmqQueueName = params.get("CmqQueueName")
        self.KmsRegion = params.get("KmsRegion")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.CmqRegion = params.get("CmqRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditResponse(AbstractModel):
    """CreateAudit返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否创建成功。\n        :type IsSuccess: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AuditName: 跟踪集名称\n        :type AuditName: str\n        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditResponse(AbstractModel):
    """DeleteAudit返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否删除成功\n        :type IsSuccess: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AuditName: 跟踪集名称\n        :type AuditName: str\n        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditResponse(AbstractModel):
    """DescribeAudit返回参数结构体

    """

    def __init__(self):
        """
        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。\n        :type IsEnableCmqNotify: int\n        :param ReadWriteAttribute: 管理事件读写属性，1：只读，2：只写，3：全部\n        :type ReadWriteAttribute: int\n        :param KeyId: CMK的全局唯一标识符。\n        :type KeyId: str\n        :param AuditStatus: 跟踪集状态，1：开启，0：停止。\n        :type AuditStatus: int\n        :param AuditName: 跟踪集名称。\n        :type AuditName: str\n        :param CosRegion: cos存储桶所在地域。\n        :type CosRegion: str\n        :param CmqQueueName: 队列名称。\n        :type CmqQueueName: str\n        :param KmsAlias: CMK别名。\n        :type KmsAlias: str\n        :param KmsRegion: kms地域。\n        :type KmsRegion: str\n        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。\n        :type IsEnableKmsEncry: int\n        :param CosBucketName: cos存储桶名称。\n        :type CosBucketName: str\n        :param CmqRegion: 队列所在地域。\n        :type CmqRegion: str\n        :param LogFilePrefix: 日志前缀。\n        :type LogFilePrefix: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.KeyId = None
        self.AuditStatus = None
        self.AuditName = None
        self.CosRegion = None
        self.CmqQueueName = None
        self.KmsAlias = None
        self.KmsRegion = None
        self.IsEnableKmsEncry = None
        self.CosBucketName = None
        self.CmqRegion = None
        self.LogFilePrefix = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.KeyId = params.get("KeyId")
        self.AuditStatus = params.get("AuditStatus")
        self.AuditName = params.get("AuditName")
        self.CosRegion = params.get("CosRegion")
        self.CmqQueueName = params.get("CmqQueueName")
        self.KmsAlias = params.get("KmsAlias")
        self.KmsRegion = params.get("KmsRegion")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.CosBucketName = params.get("CosBucketName")
        self.CmqRegion = params.get("CmqRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.RequestId = params.get("RequestId")


class DescribeEventsRequest(AbstractModel):
    """DescribeEvents请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间戳（单位秒，不超过当前时间 90 天）\n        :type StartTime: int\n        :param EndTime: 结束时间戳（单位秒，查询时间跨度小于 30 天）\n        :type EndTime: int\n        :param NextToken: 查看更多日志的凭证\n        :type NextToken: int\n        :param MaxResults: 返回日志的最大条数（最大 50 条）\n        :type MaxResults: int\n        :param LookupAttributes: 检索条件（目前支持 RequestId：请求 ID、EventName：事件名称、ActionType：操作类型（Write：写；Read：读）、PrincipalId：子账号、ResourceType：资源类型、ResourceName：资源名称、AccessKeyId：密钥 ID、SensitiveAction：是否敏感操作、ApiErrorCode：API 错误码、CamErrorCode：CAM 错误码）\n        :type LookupAttributes: list of LookupAttribute\n        :param IsReturnLocation: 是否返回 IP 归属地（1 返回，0 不返回）\n        :type IsReturnLocation: int\n        """
        self.StartTime = None
        self.EndTime = None
        self.NextToken = None
        self.MaxResults = None
        self.LookupAttributes = None
        self.IsReturnLocation = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NextToken = params.get("NextToken")
        self.MaxResults = params.get("MaxResults")
        if params.get("LookupAttributes") is not None:
            self.LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self.LookupAttributes.append(obj)
        self.IsReturnLocation = params.get("IsReturnLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventsResponse(AbstractModel):
    """DescribeEvents返回参数结构体

    """

    def __init__(self):
        """
        :param ListOver: 日志集合是否结束\n        :type ListOver: bool\n        :param NextToken: 查看更多日志的凭证\n        :type NextToken: int\n        :param Events: 日志集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type Events: list of Event\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListOver = None
        self.NextToken = None
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListOver = params.get("ListOver")
        self.NextToken = params.get("NextToken")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")


class Event(AbstractModel):
    """日志详情

    """

    def __init__(self):
        """
        :param EventId: 日志ID\n        :type EventId: str\n        :param Username: 用户名\n        :type Username: str\n        :param EventTime: 事件时间\n        :type EventTime: str\n        :param CloudAuditEvent: 日志详情\n        :type CloudAuditEvent: str\n        :param ResourceTypeCn: 资源类型中文描述（此字段请按需使用，如果您是其他语言使用者，可以忽略该字段描述）\n        :type ResourceTypeCn: str\n        :param ErrorCode: 鉴权错误码\n        :type ErrorCode: int\n        :param EventName: 事件名称\n        :type EventName: str\n        :param SecretId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretId: str\n        :param EventSource: 请求来源\n        :type EventSource: str\n        :param RequestID: 请求ID\n        :type RequestID: str\n        :param ResourceRegion: 资源地域\n        :type ResourceRegion: str\n        :param AccountID: 主账号ID\n        :type AccountID: int\n        :param SourceIPAddress: 源IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type SourceIPAddress: str\n        :param EventNameCn: 事件名称中文描述（此字段请按需使用，如果您是其他语言使用者，可以忽略该字段描述）\n        :type EventNameCn: str\n        :param Resources: 资源对\n        :type Resources: :class:`tencentcloud.cloudaudit.v20190319.models.Resource`\n        :param EventRegion: 事件地域\n        :type EventRegion: str\n        :param Location: IP 归属地\n        :type Location: str\n        """
        self.EventId = None
        self.Username = None
        self.EventTime = None
        self.CloudAuditEvent = None
        self.ResourceTypeCn = None
        self.ErrorCode = None
        self.EventName = None
        self.SecretId = None
        self.EventSource = None
        self.RequestID = None
        self.ResourceRegion = None
        self.AccountID = None
        self.SourceIPAddress = None
        self.EventNameCn = None
        self.Resources = None
        self.EventRegion = None
        self.Location = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.Username = params.get("Username")
        self.EventTime = params.get("EventTime")
        self.CloudAuditEvent = params.get("CloudAuditEvent")
        self.ResourceTypeCn = params.get("ResourceTypeCn")
        self.ErrorCode = params.get("ErrorCode")
        self.EventName = params.get("EventName")
        self.SecretId = params.get("SecretId")
        self.EventSource = params.get("EventSource")
        self.RequestID = params.get("RequestID")
        self.ResourceRegion = params.get("ResourceRegion")
        self.AccountID = params.get("AccountID")
        self.SourceIPAddress = params.get("SourceIPAddress")
        self.EventNameCn = params.get("EventNameCn")
        if params.get("Resources") is not None:
            self.Resources = Resource()
            self.Resources._deserialize(params.get("Resources"))
        self.EventRegion = params.get("EventRegion")
        self.Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttributeKeyRequest(AbstractModel):
    """GetAttributeKey请求参数结构体

    """

    def __init__(self):
        """
        :param WebsiteType: 网站类型，取值范围是zh和en。如果不传值默认zh\n        :type WebsiteType: str\n        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttributeKeyResponse(AbstractModel):
    """GetAttributeKey返回参数结构体

    """

    def __init__(self):
        """
        :param AttributeKeyDetails: AttributeKey的有效取值范围\n        :type AttributeKeyDetails: list of AttributeKeyDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AuditAmount: 可创建跟踪集的数量\n        :type AuditAmount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AuditAmount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditAmount = params.get("AuditAmount")
        self.RequestId = params.get("RequestId")


class KeyMetadata(AbstractModel):
    """CMK属性

    """

    def __init__(self):
        """
        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名\n        :type Alias: str\n        :param KeyId: CMK的全局唯一标识\n        :type KeyId: str\n        """
        self.Alias = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuditsRequest(AbstractModel):
    """ListAudits请求参数结构体

    """


class ListAuditsResponse(AbstractModel):
    """ListAudits返回参数结构体

    """

    def __init__(self):
        """
        :param AuditSummarys: 查询跟踪集概要集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuditSummarys: list of AuditSummary\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param WebsiteType: 站点类型。zh表示中国区，en表示国际区。默认中国区。\n        :type WebsiteType: str\n        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCmqEnableRegionResponse(AbstractModel):
    """ListCmqEnableRegion返回参数结构体

    """

    def __init__(self):
        """
        :param EnableRegions: 云审计支持的cmq的可用区\n        :type EnableRegions: list of CmqRegionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param WebsiteType: 站点类型。zh表示中国区，en表示国际区。默认中国区。\n        :type WebsiteType: str\n        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCosEnableRegionResponse(AbstractModel):
    """ListCosEnableRegion返回参数结构体

    """

    def __init__(self):
        """
        :param EnableRegions: 云审计支持的cos可用区\n        :type EnableRegions: list of CosRegionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class ListKeyAliasByRegionRequest(AbstractModel):
    """ListKeyAliasByRegion请求参数结构体

    """

    def __init__(self):
        """
        :param KmsRegion: Kms地域\n        :type KmsRegion: str\n        :param Limit: 含义跟 SQL 查询的 Limit 一致，表示本次获最多获取 Limit 个元素。缺省值为10，最大值为200\n        :type Limit: int\n        :param Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0\n        :type Offset: int\n        """
        self.KmsRegion = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.KmsRegion = params.get("KmsRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeyAliasByRegionResponse(AbstractModel):
    """ListKeyAliasByRegion返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: CMK的总数量\n        :type TotalCount: int\n        :param KeyMetadatas: 密钥别名\n        :type KeyMetadatas: list of KeyMetadata\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class LookUpEventsRequest(AbstractModel):
    """LookUpEvents请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间\n        :type StartTime: int\n        :param EndTime: 结束时间\n        :type EndTime: int\n        :param LookupAttributes: 检索条件\n        :type LookupAttributes: list of LookupAttribute\n        :param NextToken: 查看更多日志的凭证\n        :type NextToken: str\n        :param MaxResults: 返回日志的最大条数\n        :type MaxResults: int\n        :param Mode: 云审计模式，有效值：standard | quick，其中standard是标准模式，quick是极速模式。默认为标准模式\n        :type Mode: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.LookupAttributes = None
        self.NextToken = None
        self.MaxResults = None
        self.Mode = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("LookupAttributes") is not None:
            self.LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self.LookupAttributes.append(obj)
        self.NextToken = params.get("NextToken")
        self.MaxResults = params.get("MaxResults")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LookUpEventsResponse(AbstractModel):
    """LookUpEvents返回参数结构体

    """

    def __init__(self):
        """
        :param NextToken: 查看更多日志的凭证
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextToken: str\n        :param Events: 日志集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type Events: list of Event\n        :param ListOver: 日志集合是否结束
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListOver: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NextToken = None
        self.Events = None
        self.ListOver = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextToken = params.get("NextToken")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.ListOver = params.get("ListOver")
        self.RequestId = params.get("RequestId")


class LookupAttribute(AbstractModel):
    """检索条件

    """

    def __init__(self):
        """
        :param AttributeKey: AttributeKey的有效取值范围是:RequestId、EventName、ReadOnly、Username、ResourceType、ResourceName和AccessKeyId，EventId
注意：此字段可能返回 null，表示取不到有效值。\n        :type AttributeKey: str\n        :param AttributeValue: AttributeValue的值
注意：此字段可能返回 null，表示取不到有效值。\n        :type AttributeValue: str\n        """
        self.AttributeKey = None
        self.AttributeValue = None


    def _deserialize(self, params):
        self.AttributeKey = params.get("AttributeKey")
        self.AttributeValue = params.get("AttributeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """资源类型

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型\n        :type ResourceType: str\n        :param ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceName: str\n        """
        self.ResourceType = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLoggingRequest(AbstractModel):
    """StartLogging请求参数结构体

    """

    def __init__(self):
        """
        :param AuditName: 跟踪集名称\n        :type AuditName: str\n        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLoggingResponse(AbstractModel):
    """StartLogging返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否开启成功\n        :type IsSuccess: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AuditName: 跟踪集名称\n        :type AuditName: str\n        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLoggingResponse(AbstractModel):
    """StopLogging返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否关闭成功\n        :type IsSuccess: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AuditName: 跟踪集名称\n        :type AuditName: str\n        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。目前仅支持cmq的队列服务。如果开启cmq消息通知服务，云审计会将您的日志内容实时投递到您指定地域的指定队列中。\n        :type IsEnableCmqNotify: int\n        :param ReadWriteAttribute: 管理事件的读写属性。1：只读，2：只写，3：全部。\n        :type ReadWriteAttribute: int\n        :param KeyId: CMK的全局唯一标识符，如果不是新创建的kms，该值是必填值。可以通过ListKeyAliasByRegion来获取。云审计不会校验KeyId的合法性，请您谨慎填写，避免给您的数据造成损失。\n        :type KeyId: str\n        :param CosRegion: cos地域。目前支持的地域可以使用ListCosEnableRegion来获取。\n        :type CosRegion: str\n        :param CmqQueueName: 队列名称。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。如果IsEnableCmqNotify值是1的话，此值属于必填字段。如果不是新创建的队列，云审计不会去校验该队列是否真的存在，请谨慎填写，避免日志通知不成功，导致您的数据丢失。\n        :type CmqQueueName: str\n        :param IsCreateNewBucket: 是否创建新的cos存储桶。1：是，0：否。\n        :type IsCreateNewBucket: int\n        :param KmsRegion: kms地域。目前支持的地域可以使用ListKmsEnableRegion来获取。必须要和cos的地域保持一致。\n        :type KmsRegion: str\n        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。\n        :type IsEnableKmsEncry: int\n        :param CosBucketName: cos的存储桶名称。仅支持小写英文字母和数字即[a-z，0-9]、中划线“-”及其组合。用户自定义的字符串支持1 - 40个字符。存储桶命名不能以“-”开头或结尾。如果不是新创建的存储桶，云审计不会去校验该存储桶是否真的存在，请谨慎填写，避免日志投递不成功，导致您的数据丢失。\n        :type CosBucketName: str\n        :param CmqRegion: 队列所在的地域。可以通过ListCmqEnableRegion获取支持的cmq地域。如果IsEnableCmqNotify值是1的话，此值属于必填字段。\n        :type CmqRegion: str\n        :param LogFilePrefix: 日志文件前缀。3-40个字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9。\n        :type LogFilePrefix: str\n        :param IsCreateNewQueue: 是否创建新的队列。1：是，0：否。如果IsEnableCmqNotify值是1的话，此值属于必填字段。\n        :type IsCreateNewQueue: int\n        """
        self.AuditName = None
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.KeyId = None
        self.CosRegion = None
        self.CmqQueueName = None
        self.IsCreateNewBucket = None
        self.KmsRegion = None
        self.IsEnableKmsEncry = None
        self.CosBucketName = None
        self.CmqRegion = None
        self.LogFilePrefix = None
        self.IsCreateNewQueue = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.KeyId = params.get("KeyId")
        self.CosRegion = params.get("CosRegion")
        self.CmqQueueName = params.get("CmqQueueName")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.KmsRegion = params.get("KmsRegion")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.CosBucketName = params.get("CosBucketName")
        self.CmqRegion = params.get("CmqRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuditResponse(AbstractModel):
    """UpdateAudit返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 是否更新成功\n        :type IsSuccess: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")