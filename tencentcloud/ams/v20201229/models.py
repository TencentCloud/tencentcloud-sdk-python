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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


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
以及其他令人反感、不安全或不适宜的内容类型。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AudioSegments(AbstractModel):
    """声音段信息

    """

    def __init__(self):
        """
        :param OffsetTime: 截帧时间, 单位：秒
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetTime: str
        :param Result: 结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ams.v20201229.models.AudioResult`
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAudioModerationSyncTaskRequest(AbstractModel):
    """CreateAudioModerationSyncTask请求参数结构体

    """

    def __init__(self):
        """
        :param BizType: Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；调用时不传入Biztype代表采用默认的识别策略。
        :type BizType: str
        :param DataId: 数据标识，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :type DataId: str
        :param FileFormat: 音频文件资源格式，当前为mp3，wav，请按照实际文件格式填入
        :type FileFormat: str
        :param Name: 文件名称，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :type Name: str
        :param FileContent: 数据Base64编码，短音频同步接口仅传入可音频内容；
支持范围：文件大小不能超过5M，时长不可超过60s，码率范围为8-16Kbps；
支持格式：wav、mp3
        :type FileContent: str
        :param FileUrl: 音频资源访问链接，与FileContent参数必须二选一输入；
支持范围：同FileContent；
        :type FileUrl: str
        """
        self.BizType = None
        self.DataId = None
        self.FileFormat = None
        self.Name = None
        self.FileContent = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.DataId = params.get("DataId")
        self.FileFormat = params.get("FileFormat")
        self.Name = params.get("Name")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAudioModerationSyncTaskResponse(AbstractModel):
    """CreateAudioModerationSyncTask返回参数结构体

    """

    def __init__(self):
        """
        :param DataId: 请求接口时传入的数据标识
        :type DataId: str
        :param Name: 文件名称，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param BizType: Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；调用时不传入Biztype代表采用默认的识别策略。
        :type BizType: str
        :param Suggestion: 智能审核服务对于内容违规类型的等级，可选值：
Pass 建议通过；
Reveiw 建议复审；
Block 建议屏蔽；
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 智能审核服务对于内容违规类型的判断，详见返回值列表
如：Label：Porn（色情）；
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param AsrText: 音频文本，备注：这里的文本最大只返回前1000个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrText: str
        :param TextResults: 音频中对话内容审核结果；
注意：此字段可能返回 null，表示取不到有效值。
        :type TextResults: list of TextResult
        :param MoanResults: 音频中低俗内容审核结果；
注意：此字段可能返回 null，表示取不到有效值。
        :type MoanResults: list of MoanResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataId = None
        self.Name = None
        self.BizType = None
        self.Suggestion = None
        self.Label = None
        self.AsrText = None
        self.TextResults = None
        self.MoanResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Name = params.get("Name")
        self.BizType = params.get("BizType")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.AsrText = params.get("AsrText")
        if params.get("TextResults") is not None:
            self.TextResults = []
            for item in params.get("TextResults"):
                obj = TextResult()
                obj._deserialize(item)
                self.TextResults.append(obj)
        if params.get("MoanResults") is not None:
            self.MoanResults = []
            for item in params.get("MoanResults"):
                obj = MoanResult()
                obj._deserialize(item)
                self.MoanResults.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAudioModerationTaskRequest(AbstractModel):
    """CreateAudioModerationTask请求参数结构体

    """

    def __init__(self):
        """
        :param Tasks: 输入的任务信息，最多可以同时创建10个任务
        :type Tasks: list of TaskInput
        :param BizType: 默认为：default，客户可以在音频审核控制台配置自己的BizType
        :type BizType: str
        :param Type: 审核类型，这里可选：AUDIO (点播音频)和 LIVE_AUDIO（直播音频），默认为 AUDIIO
        :type Type: str
        :param Seed: （可选）回调签名key，具体可以查看 回调签名示例
        :type Seed: str
        :param CallbackUrl: 接收审核信息回调地址，如果设置，则审核过程中产生的违规音频片段和画面截帧发送此接口
        :type CallbackUrl: str
        """
        self.Tasks = None
        self.BizType = None
        self.Type = None
        self.Seed = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInput()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        self.Seed = params.get("Seed")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param BizType: 业务类型，用户可以在控制台查看自己配置的BizType
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
        :param InputInfo: 输入的媒体信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.ams.v20201229.models.InputInfo`
        :param AudioText: 音频文本，备注：这里的文本最大只返回前1000个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioText: str
        :param AudioSegments: 音频片段审核信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioSegments: list of AudioSegments
        :param ErrorType: 错误类型，如果任务状态为Error，则该字段不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorType: str
        :param ErrorDescription: 错误描述，如果任务状态为Error，则该字段不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDescription: str
        :param CreatedAt: 任务创建时间，格式为 ISO 8601
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 任务最后更新时间，格式为 ISO 8601
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
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
        self.InputInfo = None
        self.AudioText = None
        self.AudioSegments = None
        self.ErrorType = None
        self.ErrorDescription = None
        self.CreatedAt = None
        self.UpdatedAt = None
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
        if params.get("InputInfo") is not None:
            self.InputInfo = InputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.AudioText = params.get("AudioText")
        if params.get("AudioSegments") is not None:
            self.AudioSegments = []
            for item in params.get("AudioSegments"):
                obj = AudioSegments()
                obj._deserialize(item)
                self.AudioSegments.append(obj)
        self.ErrorType = params.get("ErrorType")
        self.ErrorDescription = params.get("ErrorDescription")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 每页展示多少条。（默认展示10条）
        :type Limit: int
        :param Filter: 过滤参数
        :type Filter: :class:`tencentcloud.ams.v20201229.models.TaskFilter`
        :param PageToken: 翻页token，在向前或向后翻页时需要
        :type PageToken: str
        :param StartTime: 开始时间。默认是最近3天。
        :type StartTime: str
        :param EndTime: 结束时间。默认为空
        :type EndTime: str
        """
        self.Limit = None
        self.Filter = None
        self.PageToken = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self.Filter = TaskFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.PageToken = params.get("PageToken")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 任务总量，为 int 字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: str
        :param Data: 当前页数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TaskData
        :param PageToken: 翻页Token，当已经到最后一页时，该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :type PageToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.PageToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TaskData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.PageToken = params.get("PageToken")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :type BucketInfo: :class:`tencentcloud.ams.v20201229.models.BucketInfo`
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MoanResult(AbstractModel):
    """呻吟低俗检测结果

    """

    def __init__(self):
        """
        :param Label: 固定取值为Moan（呻吟/娇喘），如音频中无复杂类型「MoanResult」的返回则代表改音频中无呻吟/娇喘相关违规内容；
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 机器判断当前分类的置信度，取值范围：0~100。分数越高，表示越有可能属于当前分类。
（如：Moan 99，则该样本属于呻吟/娇喘的置信度非常高。）
        :type Score: int
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param StartTime: 违规事件开始时间，单位为毫秒（ms）；
        :type StartTime: float
        :param EndTime: 违规事件结束时间，单位为毫秒（ms）；
        :type EndTime: float
        """
        self.Label = None
        self.Score = None
        self.Suggestion = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.Suggestion = params.get("Suggestion")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :type BucketInfo: :class:`tencentcloud.ams.v20201229.models.BucketInfo`
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TaskData(AbstractModel):
    """任务数据

    """

    def __init__(self):
        """
        :param DataId: 输入的数据ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param Status: 状态，可选：PENDING，RUNNING，ERROR，FINISH，CANCELLED
        :type Status: str
        :param Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param BizType: 业务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Suggestion: 建议。可选：Pass，Block，Review
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param MediaInfo: 输入信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.ams.v20201229.models.MediaInfo`
        :param Labels: 任务违规标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param CreatedAt: 创建时间（ iso 8601 格式）
        :type CreatedAt: str
        :param UpdatedAt: 更新时间（ iso 8601 格式）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self.DataId = None
        self.TaskId = None
        self.Status = None
        self.Name = None
        self.BizType = None
        self.Type = None
        self.Suggestion = None
        self.MediaInfo = None
        self.Labels = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.Name = params.get("Name")
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        if params.get("MediaInfo") is not None:
            self.MediaInfo = MediaInfo()
            self.MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TaskFilter(AbstractModel):
    """任务筛选器

    """

    def __init__(self):
        """
        :param BizType: 任务业务类型
        :type BizType: str
        :param Type: 任务类型，可选：VIDEO，AUDIO， LIVE_VIDEO, LIVE_AUDIO
        :type Type: str
        :param Suggestion: 建议，可选：Pass, Review,Block
        :type Suggestion: str
        :param TaskStatus: 状态，可选：PENDING，RUNNING，ERROR，FINISH，CANCELLED
        :type TaskStatus: str
        """
        self.BizType = None
        self.Type = None
        self.Suggestion = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :type Input: :class:`tencentcloud.ams.v20201229.models.StorageInfo`
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TaskLabel(AbstractModel):
    """任务输出标签

    """

    def __init__(self):
        """
        :param Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及其他令人反感、不安全或不适宜的内容类型。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TextResult(AbstractModel):
    """音频文本内容审核结果

    """

    def __init__(self):
        """
        :param Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及其他令人反感、不安全或不适宜的内容类型。

如音频中无复杂类型「TextResults」的返回则代表改音频中无相关违规内容；
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Keywords: 命中的关键词，为空则代表该违规内容出自于模型的判断；
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param LibId: 命中关键词库的库标识；
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param LibName: 命中关键词库的名字；
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param Score: 机器判断当前分类的置信度，取值范围：0~100。分数越高，表示越有可能属于当前分类。
（如：Porn 99，则该样本属于色情的置信度非常高。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param LibType: 自定义词库的类型，自定义词库相关的信息可登录控制台中查看；

1：自定义黑白库；

2：自定义库；
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        