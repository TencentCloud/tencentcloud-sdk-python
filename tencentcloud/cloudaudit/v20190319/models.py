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
        :param LabelType: 输入框类型
        :type LabelType: str
        :param Starter: 初始化展示
        :type Starter: str
        :param Order: 展示排序
        :type Order: int
        :param Value: AttributeKey值
        :type Value: str
        :param Label: 中文标签
        :type Label: str
        """
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
        r"""
        :param AuditStatus: 跟踪集状态，1：开启，0：关闭
        :type AuditStatus: int
        :param CosBucketName: COS存储桶名称
        :type CosBucketName: str
        :param AuditName: 跟踪集名称
        :type AuditName: str
        :param LogFilePrefix: 日志前缀
        :type LogFilePrefix: str
        """
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
        r"""
        :param CmqRegionName: 地域描述
        :type CmqRegionName: str
        :param CmqRegion: cmq地域
        :type CmqRegion: str
        """
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
        r"""
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
        r"""
        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。目前仅支持cmq的队列服务。如果开启cmq消息通知服务，云审计会将您的日志内容实时投递到您指定地域的指定队列中。
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: 管理事件的读写属性。1：只读，2：只写，3：全部。
        :type ReadWriteAttribute: int
        :param AuditName: 跟踪集名称。3-128字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9，下划线 _。
        :type AuditName: str
        :param CosRegion: cos地域。目前支持的地域可以使用ListCosEnableRegion来获取。
        :type CosRegion: str
        :param IsCreateNewBucket: 是否创建新的cos存储桶。1：是，0：否。
        :type IsCreateNewBucket: int
        :param CosBucketName: cos的存储桶名称。仅支持小写英文字母和数字即[a-z，0-9]、中划线“-”及其组合。用户自定义的字符串支持1 - 40个字符。存储桶命名不能以“-”开头或结尾。如果不是新创建的存储桶，云审计不会去校验该存储桶是否真的存在，请谨慎填写，避免日志投递不成功，导致您的数据丢失。
        :type CosBucketName: str
        :param KeyId: CMK的全局唯一标识符，如果不是新创建的kms，该值是必填值。可以通过ListKeyAliasByRegion来获取。云审计不会校验KeyId的合法性，请您谨慎填写，避免给您的数据造成损失。
        :type KeyId: str
        :param CmqQueueName: 队列名称。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。如果IsEnableCmqNotify值是1的话，此值属于必填字段。如果不是新创建的队列，云审计不会去校验该队列是否真的存在，请谨慎填写，避免日志通知不成功，导致您的数据丢失。
        :type CmqQueueName: str
        :param KmsRegion: kms地域。目前支持的地域可以使用ListKmsEnableRegion来获取。必须要和cos的地域保持一致。
        :type KmsRegion: str
        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param CmqRegion: 队列所在的地域。可以通过ListCmqEnableRegion获取支持的cmq地域。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type CmqRegion: str
        :param LogFilePrefix: 日志文件前缀。3-40个字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9。可以不填，默认以账号ID作为日志前缀。
        :type LogFilePrefix: str
        :param IsCreateNewQueue: 是否创建新的队列。1：是，0：否。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type IsCreateNewQueue: int
        """
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
        r"""
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


class CreateAuditTrackRequest(AbstractModel):
    """CreateAuditTrack请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 跟踪集名称，仅支持大小写字母、数字、-以及_的组合，3-48个字符
        :type Name: str
        :param ActionType: 跟踪事件类型（读：Read；写：Write；全部：*）
        :type ActionType: str
        :param ResourceType: 跟踪事件所属产品（支持全部产品或单个产品，如：cos，全部：*）
        :type ResourceType: str
        :param Status: 跟踪集状态（未开启：0；开启：1）
        :type Status: int
        :param EventNames: 跟踪事件接口名列表（ResourceType为 * 时，EventNames必须为全部：["*"]；指定ResourceType时，支持全部接口：["*"]；支持部分接口：["cos", "cls"]，接口列表上限10个）
        :type EventNames: list of str
        :param Storage: 数据投递存储（目前支持 cos、cls）
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param TrackForAllMembers: 是否开启将集团成员操作日志投递到集团管理账号或者可信服务管理账号(0：未开启，1：开启，只能集团管理账号或者可信服务管理账号开启此项功能)
        :type TrackForAllMembers: int
        """
        self.Name = None
        self.ActionType = None
        self.ResourceType = None
        self.Status = None
        self.EventNames = None
        self.Storage = None
        self.TrackForAllMembers = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ActionType = params.get("ActionType")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        self.EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self.Storage = Storage()
            self.Storage._deserialize(params.get("Storage"))
        self.TrackForAllMembers = params.get("TrackForAllMembers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditTrackResponse(AbstractModel):
    """CreateAuditTrack返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrackId: 跟踪集 ID
        :type TrackId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrackId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TrackId = params.get("TrackId")
        self.RequestId = params.get("RequestId")


class DeleteAuditRequest(AbstractModel):
    """DeleteAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param AuditName: 跟踪集名称
        :type AuditName: str
        """
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
        r"""
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


class DeleteAuditTrackRequest(AbstractModel):
    """DeleteAuditTrack请求参数结构体

    """

    def __init__(self):
        r"""
        :param TrackId: 跟踪集 ID
        :type TrackId: int
        """
        self.TrackId = None


    def _deserialize(self, params):
        self.TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditTrackResponse(AbstractModel):
    """DeleteAuditTrack返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAuditRequest(AbstractModel):
    """DescribeAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param AuditName: 跟踪集名称
        :type AuditName: str
        """
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
        r"""
        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: 管理事件读写属性，1：只读，2：只写，3：全部
        :type ReadWriteAttribute: int
        :param KeyId: CMK的全局唯一标识符。
        :type KeyId: str
        :param AuditStatus: 跟踪集状态，1：开启，0：停止。
        :type AuditStatus: int
        :param AuditName: 跟踪集名称。
        :type AuditName: str
        :param CosRegion: cos存储桶所在地域。
        :type CosRegion: str
        :param CmqQueueName: 队列名称。
        :type CmqQueueName: str
        :param KmsAlias: CMK别名。
        :type KmsAlias: str
        :param KmsRegion: kms地域。
        :type KmsRegion: str
        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param CosBucketName: cos存储桶名称。
        :type CosBucketName: str
        :param CmqRegion: 队列所在地域。
        :type CmqRegion: str
        :param LogFilePrefix: 日志前缀。
        :type LogFilePrefix: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeAuditTrackRequest(AbstractModel):
    """DescribeAuditTrack请求参数结构体

    """

    def __init__(self):
        r"""
        :param TrackId: 跟踪集 ID
        :type TrackId: int
        """
        self.TrackId = None


    def _deserialize(self, params):
        self.TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditTrackResponse(AbstractModel):
    """DescribeAuditTrack返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 跟踪集名称
        :type Name: str
        :param ActionType: 跟踪事件类型（读：Read；写：Write；全部：*）
        :type ActionType: str
        :param ResourceType: 跟踪事件所属产品（如：cos，全部：*）
        :type ResourceType: str
        :param Status: 跟踪集状态（未开启：0；开启：1）
        :type Status: int
        :param EventNames: 跟踪事件接口名列表（全部：[*]）
        :type EventNames: list of str
        :param Storage: 数据投递存储（目前支持 cos、cls）
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param CreateTime: 跟踪集创建时间
        :type CreateTime: str
        :param TrackForAllMembers: 是否开启将集团成员操作日志投递到集团管理账号或者可信服务管理账号
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackForAllMembers: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.ActionType = None
        self.ResourceType = None
        self.Status = None
        self.EventNames = None
        self.Storage = None
        self.CreateTime = None
        self.TrackForAllMembers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ActionType = params.get("ActionType")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        self.EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self.Storage = Storage()
            self.Storage._deserialize(params.get("Storage"))
        self.CreateTime = params.get("CreateTime")
        self.TrackForAllMembers = params.get("TrackForAllMembers")
        self.RequestId = params.get("RequestId")


class DescribeAuditTracksRequest(AbstractModel):
    """DescribeAuditTracks请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 页码
        :type PageNumber: int
        :param PageSize: 每页数目
        :type PageSize: int
        """
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditTracksResponse(AbstractModel):
    """DescribeAuditTracks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tracks: 跟踪集列表
        :type Tracks: list of Tracks
        :param TotalCount: 总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tracks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self.Tracks = []
            for item in params.get("Tracks"):
                obj = Tracks()
                obj._deserialize(item)
                self.Tracks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEventsRequest(AbstractModel):
    """DescribeEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间戳（单位秒，不超过当前时间 90 天）
        :type StartTime: int
        :param EndTime: 结束时间戳（单位秒，查询时间跨度小于 30 天）
        :type EndTime: int
        :param NextToken: 查看更多日志的凭证
        :type NextToken: int
        :param MaxResults: 返回日志的最大条数（最大 50 条）
        :type MaxResults: int
        :param LookupAttributes: 检索条件（目前支持 RequestId：请求 ID、EventName：事件名称、ActionType：操作类型（Write：写；Read：读）、PrincipalId：子账号、ResourceType：资源类型、ResourceName：资源名称、AccessKeyId：密钥 ID、SensitiveAction：是否敏感操作、ApiErrorCode：API 错误码、CamErrorCode：CAM 错误码、Tags：标签（AttributeValue格式：[{"key":"*","value":"*"}]）备注:检索的各个条件间是与的关系,EventName传多个值内部是或的关系）
        :type LookupAttributes: list of LookupAttribute
        :param IsReturnLocation: 是否返回 IP 归属地（1 返回，0 不返回）
        :type IsReturnLocation: int
        """
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
        r"""
        :param ListOver: 日志集合是否结束。true表示结束，无需进行翻页。
        :type ListOver: bool
        :param NextToken: 查看更多日志的凭证
        :type NextToken: int
        :param Events: 日志集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of Event
        :param TotalCount: 此字段已经废弃。翻页请使用ListOver配合NextToken，在ListOver为false进行下一页数据读取。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListOver = None
        self.NextToken = None
        self.Events = None
        self.TotalCount = None
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
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Event(AbstractModel):
    """日志详情

    """

    def __init__(self):
        r"""
        :param EventId: 日志ID
        :type EventId: str
        :param Username: 用户名
        :type Username: str
        :param EventTime: 事件时间
        :type EventTime: str
        :param CloudAuditEvent: 日志详情
        :type CloudAuditEvent: str
        :param ResourceTypeCn: 资源类型中文描述（此字段请按需使用，如果您是其他语言使用者，可以忽略该字段描述）
        :type ResourceTypeCn: str
        :param ErrorCode: 鉴权错误码
        :type ErrorCode: int
        :param EventName: 事件名称
        :type EventName: str
        :param SecretId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretId: str
        :param EventSource: 请求来源
        :type EventSource: str
        :param RequestID: 请求ID
        :type RequestID: str
        :param ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param AccountID: 主账号ID
        :type AccountID: int
        :param SourceIPAddress: 源IP
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceIPAddress: str
        :param EventNameCn: 事件名称中文描述（此字段请按需使用，如果您是其他语言使用者，可以忽略该字段描述）
        :type EventNameCn: str
        :param Resources: 资源对
        :type Resources: :class:`tencentcloud.cloudaudit.v20190319.models.Resource`
        :param EventRegion: 事件地域
        :type EventRegion: str
        :param Location: IP 归属地
        :type Location: str
        """
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
        r"""
        :param WebsiteType: 网站类型，取值范围是zh和en。如果不传值默认zh
        :type WebsiteType: str
        """
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
        r"""
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
        r"""
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


class KeyMetadata(AbstractModel):
    """CMK属性

    """

    def __init__(self):
        r"""
        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名
        :type Alias: str
        :param KeyId: CMK的全局唯一标识
        :type KeyId: str
        """
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
        r"""
        :param AuditSummarys: 查询跟踪集概要集合
注意：此字段可能返回 null，表示取不到有效值。
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
        r"""
        :param WebsiteType: 站点类型。zh表示中国区，en表示国际区。默认中国区。
        :type WebsiteType: str
        """
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
        r"""
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
        r"""
        :param WebsiteType: 站点类型。zh表示中国区，en表示国际区。默认中国区。
        :type WebsiteType: str
        """
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
        r"""
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


class ListKeyAliasByRegionRequest(AbstractModel):
    """ListKeyAliasByRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param KmsRegion: Kms地域
        :type KmsRegion: str
        :param Limit: 含义跟 SQL 查询的 Limit 一致，表示本次获最多获取 Limit 个元素。缺省值为10，最大值为200
        :type Limit: int
        :param Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0
        :type Offset: int
        """
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
        r"""
        :param TotalCount: CMK的总数量
        :type TotalCount: int
        :param KeyMetadatas: 密钥别名
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param EndTime: 结束时间
        :type EndTime: int
        :param LookupAttributes: 检索条件
        :type LookupAttributes: list of LookupAttribute
        :param NextToken: 查看更多日志的凭证
        :type NextToken: str
        :param MaxResults: 返回日志的最大条数
        :type MaxResults: int
        :param Mode: 云审计模式，有效值：standard | quick，其中standard是标准模式，quick是极速模式。默认为标准模式
        :type Mode: str
        """
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
        r"""
        :param NextToken: 查看更多日志的凭证
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param Events: 日志集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of Event
        :param ListOver: 日志集合是否结束
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOver: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param AttributeKey: AttributeKey的有效取值范围是:RequestId、EventName、ReadOnly、Username、ResourceType、ResourceName和AccessKeyId，EventId
        :type AttributeKey: str
        :param AttributeValue: AttributeValue的值
        :type AttributeValue: str
        """
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
        


class ModifyAuditTrackRequest(AbstractModel):
    """ModifyAuditTrack请求参数结构体

    """

    def __init__(self):
        r"""
        :param TrackId: 跟踪集 ID
        :type TrackId: int
        :param Name: 跟踪集名称，仅支持大小写字母、数字、-以及_的组合，3-48个字符
        :type Name: str
        :param ActionType: 跟踪事件类型（读：Read；写：Write；全部：*）
        :type ActionType: str
        :param ResourceType: 跟踪事件所属产品（支持全部产品或单个产品，如：cos，全部：*）
        :type ResourceType: str
        :param Status: 跟踪集状态（未开启：0；开启：1）
        :type Status: int
        :param EventNames: 跟踪事件接口名列表（ResourceType为 * 时，EventNames必须为全部：["*"]；指定ResourceType时，支持全部接口：["*"]；支持部分接口：["cos", "cls"]，接口列表上限10个）
        :type EventNames: list of str
        :param Storage: 数据投递存储（目前支持 cos、cls）
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param TrackForAllMembers: 是否开启将集团成员操作日志投递到集团管理账号或者可信服务管理账号(0：未开启，1：开启，只能集团管理账号或者可信服务管理账号开启此项功能)
        :type TrackForAllMembers: int
        """
        self.TrackId = None
        self.Name = None
        self.ActionType = None
        self.ResourceType = None
        self.Status = None
        self.EventNames = None
        self.Storage = None
        self.TrackForAllMembers = None


    def _deserialize(self, params):
        self.TrackId = params.get("TrackId")
        self.Name = params.get("Name")
        self.ActionType = params.get("ActionType")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        self.EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self.Storage = Storage()
            self.Storage._deserialize(params.get("Storage"))
        self.TrackForAllMembers = params.get("TrackForAllMembers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditTrackResponse(AbstractModel):
    """ModifyAuditTrack返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """资源类型

    """

    def __init__(self):
        r"""
        :param ResourceType: 资源类型
        :type ResourceType: str
        :param ResourceName: 资源名称
        :type ResourceName: str
        """
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
        r"""
        :param AuditName: 跟踪集名称
        :type AuditName: str
        """
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
        r"""
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
        r"""
        :param AuditName: 跟踪集名称
        :type AuditName: str
        """
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
        r"""
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


class Storage(AbstractModel):
    """跟踪集存储信息

    """

    def __init__(self):
        r"""
        :param StorageType: 存储类型（目前支持 cos、cls）
        :type StorageType: str
        :param StorageRegion: 存储所在地域
        :type StorageRegion: str
        :param StorageName: 存储名称(cos：存储名称为用户自定义的存储桶名称，不包含"-APPID"，仅支持小写字母、数字以及中划线"-"的组合，不能超过50字符，且不支持中划线"-"开头或结尾； cls：存储名称为日志主题id，字符长度为1-50个字符)
        :type StorageName: str
        :param StoragePrefix: 存储目录前缀，cos日志文件前缀仅支持字母和数字的组合，3-40个字符
        :type StoragePrefix: str
        """
        self.StorageType = None
        self.StorageRegion = None
        self.StorageName = None
        self.StoragePrefix = None


    def _deserialize(self, params):
        self.StorageType = params.get("StorageType")
        self.StorageRegion = params.get("StorageRegion")
        self.StorageName = params.get("StorageName")
        self.StoragePrefix = params.get("StoragePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tracks(AbstractModel):
    """跟踪集列表

    """

    def __init__(self):
        r"""
        :param Name: 跟踪集名称
        :type Name: str
        :param ActionType: 跟踪事件类型（读：Read；写：Write；全部：*）
        :type ActionType: str
        :param ResourceType: 跟踪事件所属产品（如：cos，全部：*）
        :type ResourceType: str
        :param Status: 跟踪集状态（未开启：0；开启：1）
        :type Status: int
        :param EventNames: 跟踪事件接口名列表（全部：[*]）
        :type EventNames: list of str
        :param Storage: 数据投递存储（目前支持 cos、cls）
        :type Storage: :class:`tencentcloud.cloudaudit.v20190319.models.Storage`
        :param CreateTime: 跟踪集创建时间
        :type CreateTime: str
        :param TrackId: 跟踪集 ID
        :type TrackId: int
        """
        self.Name = None
        self.ActionType = None
        self.ResourceType = None
        self.Status = None
        self.EventNames = None
        self.Storage = None
        self.CreateTime = None
        self.TrackId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ActionType = params.get("ActionType")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        self.EventNames = params.get("EventNames")
        if params.get("Storage") is not None:
            self.Storage = Storage()
            self.Storage._deserialize(params.get("Storage"))
        self.CreateTime = params.get("CreateTime")
        self.TrackId = params.get("TrackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuditRequest(AbstractModel):
    """UpdateAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param AuditName: 跟踪集名称
        :type AuditName: str
        :param IsEnableCmqNotify: 是否开启cmq消息通知。1：是，0：否。目前仅支持cmq的队列服务。如果开启cmq消息通知服务，云审计会将您的日志内容实时投递到您指定地域的指定队列中。
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: 管理事件的读写属性。1：只读，2：只写，3：全部。
        :type ReadWriteAttribute: int
        :param KeyId: CMK的全局唯一标识符，如果不是新创建的kms，该值是必填值。可以通过ListKeyAliasByRegion来获取。云审计不会校验KeyId的合法性，请您谨慎填写，避免给您的数据造成损失。
        :type KeyId: str
        :param CosRegion: cos地域。目前支持的地域可以使用ListCosEnableRegion来获取。
        :type CosRegion: str
        :param CmqQueueName: 队列名称。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。如果IsEnableCmqNotify值是1的话，此值属于必填字段。如果不是新创建的队列，云审计不会去校验该队列是否真的存在，请谨慎填写，避免日志通知不成功，导致您的数据丢失。
        :type CmqQueueName: str
        :param IsCreateNewBucket: 是否创建新的cos存储桶。1：是，0：否。
        :type IsCreateNewBucket: int
        :param KmsRegion: kms地域。目前支持的地域可以使用ListKmsEnableRegion来获取。必须要和cos的地域保持一致。
        :type KmsRegion: str
        :param IsEnableKmsEncry: 是否开启kms加密。1：是，0：否。如果开启KMS加密，数据在投递到cos时，会将数据加密。
        :type IsEnableKmsEncry: int
        :param CosBucketName: cos的存储桶名称。仅支持小写英文字母和数字即[a-z，0-9]、中划线“-”及其组合。用户自定义的字符串支持1 - 40个字符。存储桶命名不能以“-”开头或结尾。如果不是新创建的存储桶，云审计不会去校验该存储桶是否真的存在，请谨慎填写，避免日志投递不成功，导致您的数据丢失。
        :type CosBucketName: str
        :param CmqRegion: 队列所在的地域。可以通过ListCmqEnableRegion获取支持的cmq地域。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type CmqRegion: str
        :param LogFilePrefix: 日志文件前缀。3-40个字符，只能包含 ASCII 编码字母 a-z，A-Z，数字 0-9。
        :type LogFilePrefix: str
        :param IsCreateNewQueue: 是否创建新的队列。1：是，0：否。如果IsEnableCmqNotify值是1的话，此值属于必填字段。
        :type IsCreateNewQueue: int
        """
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
        r"""
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