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


class AmsDetailInfo(AbstractModel):
    """机器审核详情列表数据项

    """

    def __init__(self):
        """
        :param Label: 标签
        :type Label: list of str
        :param Duration: 时长(秒/s)
        :type Duration: int
        :param Name: 任务名
        :type Name: str
        :param TaskID: 任务ID，创建任务后返回的TaskId字段
        :type TaskID: str
        :param InsertTime: 插入时间
        :type InsertTime: str
        :param DataForm: 数据来源 0机审，其他为自主审核
        :type DataForm: int
        :param Operator: 操作人
        :type Operator: str
        :param OriginalLabel: 原始命中标签
        :type OriginalLabel: list of str
        :param OperateTime: 操作时间
        :type OperateTime: str
        :param Url: 视频原始地址
        :type Url: str
        :param Thumbnail: 封面图地址
        :type Thumbnail: str
        :param Content: 短音频内容
        :type Content: str
        :param DetailCount: 短音频个数
        :type DetailCount: int
        :param RequestId: 音频审核的请求 id
        :type RequestId: str
        :param Status: 音频机审状态
        :type Status: str
        """
        self.Label = None
        self.Duration = None
        self.Name = None
        self.TaskID = None
        self.InsertTime = None
        self.DataForm = None
        self.Operator = None
        self.OriginalLabel = None
        self.OperateTime = None
        self.Url = None
        self.Thumbnail = None
        self.Content = None
        self.DetailCount = None
        self.RequestId = None
        self.Status = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Duration = params.get("Duration")
        self.Name = params.get("Name")
        self.TaskID = params.get("TaskID")
        self.InsertTime = params.get("InsertTime")
        self.DataForm = params.get("DataForm")
        self.Operator = params.get("Operator")
        self.OriginalLabel = params.get("OriginalLabel")
        self.OperateTime = params.get("OperateTime")
        self.Url = params.get("Url")
        self.Thumbnail = params.get("Thumbnail")
        self.Content = params.get("Content")
        self.DetailCount = params.get("DetailCount")
        self.RequestId = params.get("RequestId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResult(AbstractModel):
    """音频输出参数

    """

    def __init__(self):
        """
        :param HitFlag: 是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 得分，0-100
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Text: 音频ASR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Url: 音频片段存储URL，有效期为1天
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Duration: 音频时长
        :type Duration: str
        :param Extra: 拓展字段
        :type Extra: str
        :param TextResults: 文本识别结果
        :type TextResults: list of AudioResultDetailTextResult
        :param MoanResults: 音频呻吟检测结果
        :type MoanResults: list of AudioResultDetailMoanResult
        :param LanguageResults: 音频语言检测结果
        :type LanguageResults: list of AudioResultDetailLanguageResult
        """
        self.HitFlag = None
        self.Label = None
        self.Suggestion = None
        self.Score = None
        self.Text = None
        self.Url = None
        self.Duration = None
        self.Extra = None
        self.TextResults = None
        self.MoanResults = None
        self.LanguageResults = None


    def _deserialize(self, params):
        self.HitFlag = params.get("HitFlag")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        self.Text = params.get("Text")
        self.Url = params.get("Url")
        self.Duration = params.get("Duration")
        self.Extra = params.get("Extra")
        if params.get("TextResults") is not None:
            self.TextResults = []
            for item in params.get("TextResults"):
                obj = AudioResultDetailTextResult()
                obj._deserialize(item)
                self.TextResults.append(obj)
        if params.get("MoanResults") is not None:
            self.MoanResults = []
            for item in params.get("MoanResults"):
                obj = AudioResultDetailMoanResult()
                obj._deserialize(item)
                self.MoanResults.append(obj)
        if params.get("LanguageResults") is not None:
            self.LanguageResults = []
            for item in params.get("LanguageResults"):
                obj = AudioResultDetailLanguageResult()
                obj._deserialize(item)
                self.LanguageResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailLanguageResult(AbstractModel):
    """音频小语种检测结果

    """

    def __init__(self):
        """
        :param Label: 语言信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        :param SubLabelCode: 子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self.Label = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None
        self.SubLabelCode = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailMoanResult(AbstractModel):
    """音频呻吟审核结果

    """

    def __init__(self):
        """
        :param Label: 固定为Moan（呻吟）
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 分数
        :type Score: int
        :param StartTime: 开始时间
        :type StartTime: float
        :param EndTime: 结束时间
        :type EndTime: float
        :param SubLabelCode: 子标签码
        :type SubLabelCode: str
        """
        self.Label = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None
        self.SubLabelCode = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailTextResult(AbstractModel):
    """音频ASR文本审核结果

    """

    def __init__(self):
        """
        :param Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Keywords: 命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param LibId: 命中的LibId
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param LibName: 命中的LibName
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Suggestion: 审核建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param LibType: 词库类型 1 黑白库 2 自定义库
        :type LibType: int
        """
        self.Label = None
        self.Keywords = None
        self.LibId = None
        self.LibName = None
        self.Score = None
        self.Suggestion = None
        self.LibType = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Keywords = params.get("Keywords")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Score = params.get("Score")
        self.Suggestion = params.get("Suggestion")
        self.LibType = params.get("LibType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSegments(AbstractModel):
    """声音段信息

    """

    def __init__(self):
        """
        :param OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetTime: str
        :param Result: 结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ams.v20200608.models.AudioResult`
        """
        self.OffsetTime = None
        self.Result = None


    def _deserialize(self, params):
        self.OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self.Result = AudioResult()
            self.Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BucketInfo(AbstractModel):
    """文件桶信息
    参考腾讯云存储相关说明 https://cloud.tencent.com/document/product/436/44352

    """

    def __init__(self):
        """
        :param Bucket: 腾讯云对象存储，存储桶名称
        :type Bucket: str
        :param Region: 地域
        :type Region: str
        :param Object: 对象Key
        :type Object: str
        """
        self.Bucket = None
        self.Region = None
        self.Object = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAudioModerationTaskRequest(AbstractModel):
    """CreateAudioModerationTask请求参数结构体

    """

    def __init__(self):
        """
        :param BizType: 业务类型, 定义 模版策略，输出存储配置。如果没有BizType，可以先参考 【创建业务配置】接口进行创建
        :type BizType: str
        :param Type: 审核类型，这里可选：AUDIO (点播音频)和 LIVE_AUDIO（直播音频）
        :type Type: str
        :param Seed: 回调签名key，具体可以查看签名文档。
        :type Seed: str
        :param CallbackUrl: 接收审核信息回调地址，如果设置，则审核过程中产生的违规音频片段和画面截帧发送此接口
        :type CallbackUrl: str
        :param Tasks: 输入的任务信息，最多可以同时创建10个任务
        :type Tasks: list of TaskInput
        """
        self.BizType = None
        self.Type = None
        self.Seed = None
        self.CallbackUrl = None
        self.Tasks = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        self.Seed = params.get("Seed")
        self.CallbackUrl = params.get("CallbackUrl")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInput()
                obj._deserialize(item)
                self.Tasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAudioModerationTaskResponse(AbstractModel):
    """CreateAudioModerationTask返回参数结构体

    """

    def __init__(self):
        """
        :param Results: 任务创建结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class CreateBizConfigRequest(AbstractModel):
    """CreateBizConfig请求参数结构体

    """

    def __init__(self):
        """
        :param BizType: 业务类型，仅限英文字母、数字和下划线（_）组成，长度不超过8位
        :type BizType: str
        :param MediaModeration: 配置信息，
        :type MediaModeration: :class:`tencentcloud.ams.v20200608.models.MediaModerationConfig`
        :param BizName: 业务名称，用于标识业务场景，长度不超过32位
        :type BizName: str
        :param ModerationCategories: 审核内容，可选：Polity (政治); Porn (色情); Illegal(违法);Abuse (谩骂); Terror (暴恐); Ad (广告);
        :type ModerationCategories: list of str
        """
        self.BizType = None
        self.MediaModeration = None
        self.BizName = None
        self.ModerationCategories = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        if params.get("MediaModeration") is not None:
            self.MediaModeration = MediaModerationConfig()
            self.MediaModeration._deserialize(params.get("MediaModeration"))
        self.BizName = params.get("BizName")
        self.ModerationCategories = params.get("ModerationCategories")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBizConfigResponse(AbstractModel):
    """CreateBizConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAmsListRequest(AbstractModel):
    """DescribeAmsList请求参数结构体

    """

    def __init__(self):
        """
        :param PageToken: 页码
        :type PageToken: str
        :param Limit: 过滤条件
        :type Limit: int
        :param PageDirection: 查询方向
        :type PageDirection: str
        :param Filters: 过滤条件
        :type Filters: list of Filter
        """
        self.PageToken = None
        self.Limit = None
        self.PageDirection = None
        self.Filters = None


    def _deserialize(self, params):
        self.PageToken = params.get("PageToken")
        self.Limit = params.get("Limit")
        self.PageDirection = params.get("PageDirection")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAmsListResponse(AbstractModel):
    """DescribeAmsList返回参数结构体

    """

    def __init__(self):
        """
        :param AmsDetailSet: 返回列表数据----非必选，该参数暂未对外开放
        :type AmsDetailSet: list of AmsDetailInfo
        :param Total: 总条数
        :type Total: int
        :param PageToken: 分页 token
        :type PageToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AmsDetailSet = None
        self.Total = None
        self.PageToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AmsDetailSet") is not None:
            self.AmsDetailSet = []
            for item in params.get("AmsDetailSet"):
                obj = AmsDetailInfo()
                obj._deserialize(item)
                self.AmsDetailSet.append(obj)
        self.Total = params.get("Total")
        self.PageToken = params.get("PageToken")
        self.RequestId = params.get("RequestId")


class DescribeAudioStatRequest(AbstractModel):
    """DescribeAudioStat请求参数结构体

    """

    def __init__(self):
        """
        :param AuditType: 审核类型 1: 机器审核; 2: 人工审核
        :type AuditType: int
        :param Filters: 查询条件
        :type Filters: list of Filters
        """
        self.AuditType = None
        self.Filters = None


    def _deserialize(self, params):
        self.AuditType = params.get("AuditType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAudioStatResponse(AbstractModel):
    """DescribeAudioStat返回参数结构体

    """

    def __init__(self):
        """
        :param Overview: 识别结果统计
        :type Overview: :class:`tencentcloud.ams.v20200608.models.Overview`
        :param TrendCount: 识别量统计
        :type TrendCount: list of TrendCount
        :param EvilCount: 违规数据分布
        :type EvilCount: list of EvilCount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Overview = None
        self.TrendCount = None
        self.EvilCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Overview") is not None:
            self.Overview = Overview()
            self.Overview._deserialize(params.get("Overview"))
        if params.get("TrendCount") is not None:
            self.TrendCount = []
            for item in params.get("TrendCount"):
                obj = TrendCount()
                obj._deserialize(item)
                self.TrendCount.append(obj)
        if params.get("EvilCount") is not None:
            self.EvilCount = []
            for item in params.get("EvilCount"):
                obj = EvilCount()
                obj._deserialize(item)
                self.EvilCount.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBizConfigRequest(AbstractModel):
    """DescribeBizConfig请求参数结构体

    """

    def __init__(self):
        """
        :param BizType: 审核业务类类型
        :type BizType: str
        """
        self.BizType = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizConfigResponse(AbstractModel):
    """DescribeBizConfig返回参数结构体

    """

    def __init__(self):
        """
        :param BizType: 业务类型
        :type BizType: str
        :param BizName: 业务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BizName: str
        :param ModerationCategories: 审核范围
        :type ModerationCategories: list of str
        :param MediaModeration: 多媒体审核配置
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaModeration: :class:`tencentcloud.ams.v20200608.models.MediaModerationConfig`
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BizType = None
        self.BizName = None
        self.ModerationCategories = None
        self.MediaModeration = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.BizName = params.get("BizName")
        self.ModerationCategories = params.get("ModerationCategories")
        if params.get("MediaModeration") is not None:
            self.MediaModeration = MediaModerationConfig()
            self.MediaModeration._deserialize(params.get("MediaModeration"))
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，创建任务后返回的TaskId字段
        :type TaskId: str
        :param ShowAllSegments: 是否展示所有分片，默认只展示命中规则的分片
        :type ShowAllSegments: bool
        """
        self.TaskId = None
        self.ShowAllSegments = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ShowAllSegments = params.get("ShowAllSegments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param DataId: 审核时传入的数据Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param BizType: 业务类型，用于调用识别策略模板；
（暂未发布功能，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Status: 查询内容审核任务的状态，可选值：
FINISH 已完成
PENDING 等待中
RUNNING 进行中
ERROR 出错
CANCELLED 已取消
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Type: 任务类型：可选AUDIO（点播音频），LIVE_AUDIO（直播音频）
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Suggestion: 智能审核服务对于内容违规类型的等级，可选值：
Pass 建议通过；
Reveiw 建议复审；
Block 建议屏蔽；
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Labels: 智能审核服务对于内容违规类型的判断，详见返回值列表
如：Label：Porn（色情）；
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param MediaInfo: 传入媒体的解码信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.ams.v20200608.models.MediaInfo`
        :param InputInfo: 审核任务的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.ams.v20200608.models.InputInfo`
        :param CreatedAt: 审核任务的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 审核任务的更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param TryInSeconds: 在N秒后重试
注意：此字段可能返回 null，表示取不到有效值。
        :type TryInSeconds: int
        :param AudioSegments: 视频/音频审核中的音频结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioSegments: list of AudioSegments
        :param ImageSegments: 视频审核中的图片结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSegments: list of ImageSegments
        :param AudioText: 音频识别总文本
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioText: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.DataId = None
        self.BizType = None
        self.Name = None
        self.Status = None
        self.Type = None
        self.Suggestion = None
        self.Labels = None
        self.MediaInfo = None
        self.InputInfo = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.TryInSeconds = None
        self.AudioSegments = None
        self.ImageSegments = None
        self.AudioText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DataId = params.get("DataId")
        self.BizType = params.get("BizType")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("MediaInfo") is not None:
            self.MediaInfo = MediaInfo()
            self.MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("InputInfo") is not None:
            self.InputInfo = InputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.TryInSeconds = params.get("TryInSeconds")
        if params.get("AudioSegments") is not None:
            self.AudioSegments = []
            for item in params.get("AudioSegments"):
                obj = AudioSegments()
                obj._deserialize(item)
                self.AudioSegments.append(obj)
        if params.get("ImageSegments") is not None:
            self.ImageSegments = []
            for item in params.get("ImageSegments"):
                obj = ImageSegments()
                obj._deserialize(item)
                self.ImageSegments.append(obj)
        self.AudioText = params.get("AudioText")
        self.RequestId = params.get("RequestId")


class EvilCount(AbstractModel):
    """违规数据分布

    """

    def __init__(self):
        """
        :param EvilType: ----非必选，该参数功能暂未对外开放
        :type EvilType: str
        :param Count: 分布类型总量
        :type Count: int
        """
        self.EvilType = None
        self.Count = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileOutput(AbstractModel):
    """Cos FileOutput

    """

    def __init__(self):
        """
        :param Bucket: 存储的Bucket
        :type Bucket: str
        :param Region: Cos Region
        :type Region: str
        :param ObjectPrefix: 对象前缀
        :type ObjectPrefix: str
        """
        self.Bucket = None
        self.Region = None
        self.ObjectPrefix = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.ObjectPrefix = params.get("ObjectPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """音频过滤条件

    """

    def __init__(self):
        """
        :param Name: 查询字段：
策略BizType
子账号SubUin
日期区间DateRange
        :type Name: str
        :param Values: 查询值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResult(AbstractModel):
    """Result结果详情

    """

    def __init__(self):
        """
        :param HitFlag: 违规标志
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 得分
        :type Score: int
        :param Results: 画面截帧图片结果集
        :type Results: list of ImageResultResult
        :param Url: 图片URL地址
        :type Url: str
        :param Extra: 附加字段
        :type Extra: str
        """
        self.HitFlag = None
        self.Suggestion = None
        self.Label = None
        self.Score = None
        self.Results = None
        self.Url = None
        self.Extra = None


    def _deserialize(self, params):
        self.HitFlag = params.get("HitFlag")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = ImageResultResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.Url = params.get("Url")
        self.Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultResult(AbstractModel):
    """图片输出结果的子结果

    """

    def __init__(self):
        """
        :param Scene: 场景
Porn 色情
Sexy 性感
Abuse 谩骂
Ad 广告
等多个识别场景
注意：此字段可能返回 null，表示取不到有效值。
        :type Scene: str
        :param HitFlag: 是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param SubLabel: 子标签
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param Score: 分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Names: 如果命中场景为涉政，则该数据为人物姓名列表，否则null
        :type Names: list of str
        :param Text: 图片OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Details: 其他详情
        :type Details: list of ImageResultsResultDetail
        """
        self.Scene = None
        self.HitFlag = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Names = None
        self.Text = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.HitFlag = params.get("HitFlag")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        self.Names = params.get("Names")
        self.Text = params.get("Text")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ImageResultsResultDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultsResultDetail(AbstractModel):
    """具体场景下的图片识别结果

    """

    def __init__(self):
        """
        :param Location: 位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: list of ImageResultsResultDetailLocation
        :param Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Text: OCR识别文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Label: 标签
        :type Label: str
        :param LibId: 库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param LibName: 库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param Keywords: 命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param Suggestion: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param SubLabelCode: 子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self.Location = None
        self.Name = None
        self.Text = None
        self.Label = None
        self.LibId = None
        self.LibName = None
        self.Keywords = None
        self.Suggestion = None
        self.Score = None
        self.SubLabelCode = None


    def _deserialize(self, params):
        if params.get("Location") is not None:
            self.Location = []
            for item in params.get("Location"):
                obj = ImageResultsResultDetailLocation()
                obj._deserialize(item)
                self.Location.append(obj)
        self.Name = params.get("Name")
        self.Text = params.get("Text")
        self.Label = params.get("Label")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Keywords = params.get("Keywords")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        self.SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultsResultDetailLocation(AbstractModel):
    """图片详情位置信息

    """

    def __init__(self):
        """
        :param X: x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: float
        :param Y: y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        :param Width: 宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Rotate: 旋转角度
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: float
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.Rotate = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Rotate = params.get("Rotate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSegments(AbstractModel):
    """图片段信息

    """

    def __init__(self):
        """
        :param Result: 画面截帧结果详情
        :type Result: :class:`tencentcloud.ams.v20200608.models.ImageResult`
        :param OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
        :type OffsetTime: str
        """
        self.Result = None
        self.OffsetTime = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ImageResult()
            self.Result._deserialize(params.get("Result"))
        self.OffsetTime = params.get("OffsetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """输入信息详情

    """

    def __init__(self):
        """
        :param Type: 传入的类型可选：URL，COS
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Url: Url地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param BucketInfo: 桶信息。当输入当时COS时，该字段不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketInfo: :class:`tencentcloud.ams.v20200608.models.BucketInfo`
        """
        self.Type = None
        self.Url = None
        self.BucketInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Url = params.get("Url")
        if params.get("BucketInfo") is not None:
            self.BucketInfo = BucketInfo()
            self.BucketInfo._deserialize(params.get("BucketInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    """媒体类型

    """

    def __init__(self):
        """
        :param Codecs: 编码格式
        :type Codecs: str
        :param Duration: 流检测时分片时长
注意：此字段可能返回 0，表示取不到有效值。
        :type Duration: int
        :param Width: 宽，单位为像素
        :type Width: int
        :param Height: 高，单位为像素
        :type Height: int
        :param Thumbnail: 缩略图
        :type Thumbnail: str
        """
        self.Codecs = None
        self.Duration = None
        self.Width = None
        self.Height = None
        self.Thumbnail = None


    def _deserialize(self, params):
        self.Codecs = params.get("Codecs")
        self.Duration = params.get("Duration")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaModerationConfig(AbstractModel):
    """媒体审核配置

    """

    def __init__(self):
        """
        :param AudioFrequency: 音频截帧频率。默认一分钟
        :type AudioFrequency: int
        :param ImageFrequency: 图片取帧频率, 单位（秒/帧），默认 5， 可选 1 ～ 300
        :type ImageFrequency: int
        :param CallbackUrl: 异步回调地址。
        :type CallbackUrl: str
        :param SegmentOutput: 临时文件存储位置
        :type SegmentOutput: :class:`tencentcloud.ams.v20200608.models.FileOutput`
        :param UseOCR: 是否使用OCR，默认为true
        :type UseOCR: bool
        :param UseAudio: 是否使用音频。（音频场景下，该值永远为true）
        :type UseAudio: bool
        """
        self.AudioFrequency = None
        self.ImageFrequency = None
        self.CallbackUrl = None
        self.SegmentOutput = None
        self.UseOCR = None
        self.UseAudio = None


    def _deserialize(self, params):
        self.AudioFrequency = params.get("AudioFrequency")
        self.ImageFrequency = params.get("ImageFrequency")
        self.CallbackUrl = params.get("CallbackUrl")
        if params.get("SegmentOutput") is not None:
            self.SegmentOutput = FileOutput()
            self.SegmentOutput._deserialize(params.get("SegmentOutput"))
        self.UseOCR = params.get("UseOCR")
        self.UseAudio = params.get("UseAudio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Overview(AbstractModel):
    """识别结果统计

    """

    def __init__(self):
        """
        :param TotalCount: 总调用量
        :type TotalCount: int
        :param TotalHour: 总调用时长
        :type TotalHour: int
        :param PassCount: 通过量
        :type PassCount: int
        :param PassHour: 通过时长
        :type PassHour: int
        :param EvilCount: 违规量
        :type EvilCount: int
        :param EvilHour: 违规时长
        :type EvilHour: int
        :param SuspectCount: 疑似违规量
        :type SuspectCount: int
        :param SuspectHour: 疑似违规时长
        :type SuspectHour: int
        """
        self.TotalCount = None
        self.TotalHour = None
        self.PassCount = None
        self.PassHour = None
        self.EvilCount = None
        self.EvilHour = None
        self.SuspectCount = None
        self.SuspectHour = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TotalHour = params.get("TotalHour")
        self.PassCount = params.get("PassCount")
        self.PassHour = params.get("PassHour")
        self.EvilCount = params.get("EvilCount")
        self.EvilHour = params.get("EvilHour")
        self.SuspectCount = params.get("SuspectCount")
        self.SuspectHour = params.get("SuspectHour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """数据存储信息

    """

    def __init__(self):
        """
        :param Type: 类型 可选：
URL 资源链接类型
COS 腾讯云对象存储类型
        :type Type: str
        :param Url: 资源链接
        :type Url: str
        :param BucketInfo: 腾讯云存储桶信息
        :type BucketInfo: :class:`tencentcloud.ams.v20200608.models.BucketInfo`
        """
        self.Type = None
        self.Url = None
        self.BucketInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Url = params.get("Url")
        if params.get("BucketInfo") is not None:
            self.BucketInfo = BucketInfo()
            self.BucketInfo._deserialize(params.get("BucketInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """音视频任务结构

    """

    def __init__(self):
        """
        :param DataId: 数据ID
        :type DataId: str
        :param Name: 任务名
        :type Name: str
        :param Input: 任务输入
        :type Input: :class:`tencentcloud.ams.v20200608.models.StorageInfo`
        """
        self.DataId = None
        self.Name = None
        self.Input = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Name = params.get("Name")
        if params.get("Input") is not None:
            self.Input = StorageInfo()
            self.Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLabel(AbstractModel):
    """任务输出标签

    """

    def __init__(self):
        """
        :param Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 得分，分数是 0 ～ 100
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        """
        self.Label = None
        self.Suggestion = None
        self.Score = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """创建任务时的返回结果

    """

    def __init__(self):
        """
        :param DataId: 请求时传入的DataId
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param TaskId: TaskId，任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param Code: 错误码。如果code为OK，则表示创建成功，其他则参考公共错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Message: 如果错误，该字段表示错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.DataId = None
        self.TaskId = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrendCount(AbstractModel):
    """识别量统计

    """

    def __init__(self):
        """
        :param TotalCount: 总调用量
        :type TotalCount: int
        :param TotalHour: 总调用时长
        :type TotalHour: int
        :param PassCount: 通过量
        :type PassCount: int
        :param PassHour: 通过时长
        :type PassHour: int
        :param EvilCount: 违规量
        :type EvilCount: int
        :param EvilHour: 违规时长
        :type EvilHour: int
        :param SuspectCount: 疑似违规量
        :type SuspectCount: int
        :param SuspectHour: 疑似违规时长
        :type SuspectHour: int
        :param Date: 日期
        :type Date: str
        """
        self.TotalCount = None
        self.TotalHour = None
        self.PassCount = None
        self.PassHour = None
        self.EvilCount = None
        self.EvilHour = None
        self.SuspectCount = None
        self.SuspectHour = None
        self.Date = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TotalHour = params.get("TotalHour")
        self.PassCount = params.get("PassCount")
        self.PassHour = params.get("PassHour")
        self.EvilCount = params.get("EvilCount")
        self.EvilHour = params.get("EvilHour")
        self.SuspectCount = params.get("SuspectCount")
        self.SuspectHour = params.get("SuspectHour")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        