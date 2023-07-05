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
        r"""
        :param _Label: 标签
        :type Label: list of str
        :param _Duration: 时长(秒/s)
        :type Duration: int
        :param _Name: 任务名
        :type Name: str
        :param _TaskID: 任务ID，创建任务后返回的TaskId字段
        :type TaskID: str
        :param _InsertTime: 插入时间
        :type InsertTime: str
        :param _DataForm: 数据来源 0机审，其他为自主审核
        :type DataForm: int
        :param _Operator: 操作人
        :type Operator: str
        :param _OriginalLabel: 原始命中标签
        :type OriginalLabel: list of str
        :param _OperateTime: 操作时间
        :type OperateTime: str
        :param _Url: 视频原始地址
        :type Url: str
        :param _Thumbnail: 封面图地址
        :type Thumbnail: str
        :param _Content: 短音频内容
        :type Content: str
        :param _DetailCount: 短音频个数
        :type DetailCount: int
        :param _RequestId: 音频审核的请求 id
        :type RequestId: str
        :param _Status: 音频机审状态
        :type Status: str
        """
        self._Label = None
        self._Duration = None
        self._Name = None
        self._TaskID = None
        self._InsertTime = None
        self._DataForm = None
        self._Operator = None
        self._OriginalLabel = None
        self._OperateTime = None
        self._Url = None
        self._Thumbnail = None
        self._Content = None
        self._DetailCount = None
        self._RequestId = None
        self._Status = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def DataForm(self):
        return self._DataForm

    @DataForm.setter
    def DataForm(self, DataForm):
        self._DataForm = DataForm

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def OriginalLabel(self):
        return self._OriginalLabel

    @OriginalLabel.setter
    def OriginalLabel(self, OriginalLabel):
        self._OriginalLabel = OriginalLabel

    @property
    def OperateTime(self):
        return self._OperateTime

    @OperateTime.setter
    def OperateTime(self, OperateTime):
        self._OperateTime = OperateTime

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Thumbnail(self):
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def DetailCount(self):
        return self._DetailCount

    @DetailCount.setter
    def DetailCount(self, DetailCount):
        self._DetailCount = DetailCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Duration = params.get("Duration")
        self._Name = params.get("Name")
        self._TaskID = params.get("TaskID")
        self._InsertTime = params.get("InsertTime")
        self._DataForm = params.get("DataForm")
        self._Operator = params.get("Operator")
        self._OriginalLabel = params.get("OriginalLabel")
        self._OperateTime = params.get("OperateTime")
        self._Url = params.get("Url")
        self._Thumbnail = params.get("Thumbnail")
        self._Content = params.get("Content")
        self._DetailCount = params.get("DetailCount")
        self._RequestId = params.get("RequestId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResult(AbstractModel):
    """音频输出参数

    """

    def __init__(self):
        r"""
        :param _HitFlag: 是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Score: 得分，0-100
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Text: 音频ASR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Url: 音频片段存储URL，有效期为1天
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Duration: 音频时长
        :type Duration: str
        :param _Extra: 拓展字段
        :type Extra: str
        :param _TextResults: 文本识别结果
        :type TextResults: list of AudioResultDetailTextResult
        :param _MoanResults: 音频呻吟检测结果
        :type MoanResults: list of AudioResultDetailMoanResult
        :param _LanguageResults: 音频语言检测结果
        :type LanguageResults: list of AudioResultDetailLanguageResult
        """
        self._HitFlag = None
        self._Label = None
        self._Suggestion = None
        self._Score = None
        self._Text = None
        self._Url = None
        self._Duration = None
        self._Extra = None
        self._TextResults = None
        self._MoanResults = None
        self._LanguageResults = None

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def TextResults(self):
        return self._TextResults

    @TextResults.setter
    def TextResults(self, TextResults):
        self._TextResults = TextResults

    @property
    def MoanResults(self):
        return self._MoanResults

    @MoanResults.setter
    def MoanResults(self, MoanResults):
        self._MoanResults = MoanResults

    @property
    def LanguageResults(self):
        return self._LanguageResults

    @LanguageResults.setter
    def LanguageResults(self, LanguageResults):
        self._LanguageResults = LanguageResults


    def _deserialize(self, params):
        self._HitFlag = params.get("HitFlag")
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Score = params.get("Score")
        self._Text = params.get("Text")
        self._Url = params.get("Url")
        self._Duration = params.get("Duration")
        self._Extra = params.get("Extra")
        if params.get("TextResults") is not None:
            self._TextResults = []
            for item in params.get("TextResults"):
                obj = AudioResultDetailTextResult()
                obj._deserialize(item)
                self._TextResults.append(obj)
        if params.get("MoanResults") is not None:
            self._MoanResults = []
            for item in params.get("MoanResults"):
                obj = AudioResultDetailMoanResult()
                obj._deserialize(item)
                self._MoanResults.append(obj)
        if params.get("LanguageResults") is not None:
            self._LanguageResults = []
            for item in params.get("LanguageResults"):
                obj = AudioResultDetailLanguageResult()
                obj._deserialize(item)
                self._LanguageResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailLanguageResult(AbstractModel):
    """音频小语种检测结果

    """

    def __init__(self):
        r"""
        :param _Label: 语言信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        :param _SubLabelCode: 子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self._Label = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None
        self._SubLabelCode = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

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
    def SubLabelCode(self):
        return self._SubLabelCode

    @SubLabelCode.setter
    def SubLabelCode(self, SubLabelCode):
        self._SubLabelCode = SubLabelCode


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Score = params.get("Score")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailMoanResult(AbstractModel):
    """音频呻吟审核结果

    """

    def __init__(self):
        r"""
        :param _Label: 固定为Moan（呻吟）
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Score: 分数
        :type Score: int
        :param _StartTime: 开始时间
        :type StartTime: float
        :param _EndTime: 结束时间
        :type EndTime: float
        :param _SubLabelCode: 子标签码
        :type SubLabelCode: str
        """
        self._Label = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None
        self._SubLabelCode = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

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
    def SubLabelCode(self):
        return self._SubLabelCode

    @SubLabelCode.setter
    def SubLabelCode(self, SubLabelCode):
        self._SubLabelCode = SubLabelCode


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Score = params.get("Score")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailTextResult(AbstractModel):
    """音频ASR文本审核结果

    """

    def __init__(self):
        r"""
        :param _Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Keywords: 命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _LibId: 命中的LibId
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param _LibName: 命中的LibName
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param _Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Suggestion: 审核建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _LibType: 词库类型 1 黑白库 2 自定义库
        :type LibType: int
        """
        self._Label = None
        self._Keywords = None
        self._LibId = None
        self._LibName = None
        self._Score = None
        self._Suggestion = None
        self._LibType = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def LibType(self):
        return self._LibType

    @LibType.setter
    def LibType(self, LibType):
        self._LibType = LibType


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Keywords = params.get("Keywords")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Score = params.get("Score")
        self._Suggestion = params.get("Suggestion")
        self._LibType = params.get("LibType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSegments(AbstractModel):
    """声音段信息

    """

    def __init__(self):
        r"""
        :param _OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetTime: str
        :param _Result: 结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ams.v20200608.models.AudioResult`
        """
        self._OffsetTime = None
        self._Result = None

    @property
    def OffsetTime(self):
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self._Result = AudioResult()
            self._Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BucketInfo(AbstractModel):
    """文件桶信息
    参考腾讯云存储相关说明 https://cloud.tencent.com/document/product/436/44352

    """

    def __init__(self):
        r"""
        :param _Bucket: 腾讯云对象存储，存储桶名称
        :type Bucket: str
        :param _Region: 地域
        :type Region: str
        :param _Object: 对象Key
        :type Object: str
        """
        self._Bucket = None
        self._Region = None
        self._Object = None

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

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


class CreateAudioModerationTaskRequest(AbstractModel):
    """CreateAudioModerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 业务类型, 定义 模版策略，输出存储配置。如果没有BizType，可以先参考 【创建业务配置】接口进行创建
        :type BizType: str
        :param _Type: 审核类型，这里可选：AUDIO (点播音频)和 LIVE_AUDIO（直播音频）
        :type Type: str
        :param _Seed: 回调签名key，具体可以查看签名文档。
        :type Seed: str
        :param _CallbackUrl: 接收审核信息回调地址，如果设置，则审核过程中产生的违规音频片段和画面截帧发送此接口
        :type CallbackUrl: str
        :param _Tasks: 输入的任务信息，最多可以同时创建10个任务
        :type Tasks: list of TaskInput
        """
        self._BizType = None
        self._Type = None
        self._Seed = None
        self._CallbackUrl = None
        self._Tasks = None

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Seed(self):
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._Type = params.get("Type")
        self._Seed = params.get("Seed")
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInput()
                obj._deserialize(item)
                self._Tasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAudioModerationTaskResponse(AbstractModel):
    """CreateAudioModerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 任务创建结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class CreateBizConfigRequest(AbstractModel):
    """CreateBizConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 业务类型，仅限英文字母、数字和下划线（_）组成，长度不超过8位
        :type BizType: str
        :param _MediaModeration: 配置信息，
        :type MediaModeration: :class:`tencentcloud.ams.v20200608.models.MediaModerationConfig`
        :param _BizName: 业务名称，用于标识业务场景，长度不超过32位
        :type BizName: str
        :param _ModerationCategories: 审核内容，可选：Polity (政治); Porn (色情); Illegal(违法);Abuse (谩骂); Terror (暴恐); Ad (广告);
        :type ModerationCategories: list of str
        """
        self._BizType = None
        self._MediaModeration = None
        self._BizName = None
        self._ModerationCategories = None

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def MediaModeration(self):
        return self._MediaModeration

    @MediaModeration.setter
    def MediaModeration(self, MediaModeration):
        self._MediaModeration = MediaModeration

    @property
    def BizName(self):
        return self._BizName

    @BizName.setter
    def BizName(self, BizName):
        self._BizName = BizName

    @property
    def ModerationCategories(self):
        return self._ModerationCategories

    @ModerationCategories.setter
    def ModerationCategories(self, ModerationCategories):
        self._ModerationCategories = ModerationCategories


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        if params.get("MediaModeration") is not None:
            self._MediaModeration = MediaModerationConfig()
            self._MediaModeration._deserialize(params.get("MediaModeration"))
        self._BizName = params.get("BizName")
        self._ModerationCategories = params.get("ModerationCategories")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBizConfigResponse(AbstractModel):
    """CreateBizConfig返回参数结构体

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


class DescribeAmsListRequest(AbstractModel):
    """DescribeAmsList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageToken: 页码
        :type PageToken: str
        :param _Limit: 过滤条件
        :type Limit: int
        :param _PageDirection: 查询方向
        :type PageDirection: str
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._PageToken = None
        self._Limit = None
        self._PageDirection = None
        self._Filters = None

    @property
    def PageToken(self):
        return self._PageToken

    @PageToken.setter
    def PageToken(self, PageToken):
        self._PageToken = PageToken

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PageDirection(self):
        return self._PageDirection

    @PageDirection.setter
    def PageDirection(self, PageDirection):
        self._PageDirection = PageDirection

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._PageToken = params.get("PageToken")
        self._Limit = params.get("Limit")
        self._PageDirection = params.get("PageDirection")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAmsListResponse(AbstractModel):
    """DescribeAmsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AmsDetailSet: 返回列表数据----非必选，该参数暂未对外开放
        :type AmsDetailSet: list of AmsDetailInfo
        :param _Total: 总条数
        :type Total: int
        :param _PageToken: 分页 token
        :type PageToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AmsDetailSet = None
        self._Total = None
        self._PageToken = None
        self._RequestId = None

    @property
    def AmsDetailSet(self):
        return self._AmsDetailSet

    @AmsDetailSet.setter
    def AmsDetailSet(self, AmsDetailSet):
        self._AmsDetailSet = AmsDetailSet

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def PageToken(self):
        return self._PageToken

    @PageToken.setter
    def PageToken(self, PageToken):
        self._PageToken = PageToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AmsDetailSet") is not None:
            self._AmsDetailSet = []
            for item in params.get("AmsDetailSet"):
                obj = AmsDetailInfo()
                obj._deserialize(item)
                self._AmsDetailSet.append(obj)
        self._Total = params.get("Total")
        self._PageToken = params.get("PageToken")
        self._RequestId = params.get("RequestId")


class DescribeAudioStatRequest(AbstractModel):
    """DescribeAudioStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditType: 审核类型 1: 机器审核; 2: 人工审核
        :type AuditType: int
        :param _Filters: 查询条件
        :type Filters: list of Filters
        """
        self._AuditType = None
        self._Filters = None

    @property
    def AuditType(self):
        return self._AuditType

    @AuditType.setter
    def AuditType(self, AuditType):
        self._AuditType = AuditType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AuditType = params.get("AuditType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAudioStatResponse(AbstractModel):
    """DescribeAudioStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Overview: 识别结果统计
        :type Overview: :class:`tencentcloud.ams.v20200608.models.Overview`
        :param _TrendCount: 识别量统计
        :type TrendCount: list of TrendCount
        :param _EvilCount: 违规数据分布
        :type EvilCount: list of EvilCount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Overview = None
        self._TrendCount = None
        self._EvilCount = None
        self._RequestId = None

    @property
    def Overview(self):
        return self._Overview

    @Overview.setter
    def Overview(self, Overview):
        self._Overview = Overview

    @property
    def TrendCount(self):
        return self._TrendCount

    @TrendCount.setter
    def TrendCount(self, TrendCount):
        self._TrendCount = TrendCount

    @property
    def EvilCount(self):
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Overview") is not None:
            self._Overview = Overview()
            self._Overview._deserialize(params.get("Overview"))
        if params.get("TrendCount") is not None:
            self._TrendCount = []
            for item in params.get("TrendCount"):
                obj = TrendCount()
                obj._deserialize(item)
                self._TrendCount.append(obj)
        if params.get("EvilCount") is not None:
            self._EvilCount = []
            for item in params.get("EvilCount"):
                obj = EvilCount()
                obj._deserialize(item)
                self._EvilCount.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBizConfigRequest(AbstractModel):
    """DescribeBizConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 审核业务类类型
        :type BizType: str
        """
        self._BizType = None

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizConfigResponse(AbstractModel):
    """DescribeBizConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 业务类型
        :type BizType: str
        :param _BizName: 业务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BizName: str
        :param _ModerationCategories: 审核范围
        :type ModerationCategories: list of str
        :param _MediaModeration: 多媒体审核配置
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaModeration: :class:`tencentcloud.ams.v20200608.models.MediaModerationConfig`
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BizType = None
        self._BizName = None
        self._ModerationCategories = None
        self._MediaModeration = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._RequestId = None

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def BizName(self):
        return self._BizName

    @BizName.setter
    def BizName(self, BizName):
        self._BizName = BizName

    @property
    def ModerationCategories(self):
        return self._ModerationCategories

    @ModerationCategories.setter
    def ModerationCategories(self, ModerationCategories):
        self._ModerationCategories = ModerationCategories

    @property
    def MediaModeration(self):
        return self._MediaModeration

    @MediaModeration.setter
    def MediaModeration(self, MediaModeration):
        self._MediaModeration = MediaModeration

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._BizName = params.get("BizName")
        self._ModerationCategories = params.get("ModerationCategories")
        if params.get("MediaModeration") is not None:
            self._MediaModeration = MediaModerationConfig()
            self._MediaModeration._deserialize(params.get("MediaModeration"))
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，创建任务后返回的TaskId字段
        :type TaskId: str
        :param _ShowAllSegments: 是否展示所有分片，默认只展示命中规则的分片
        :type ShowAllSegments: bool
        """
        self._TaskId = None
        self._ShowAllSegments = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ShowAllSegments(self):
        return self._ShowAllSegments

    @ShowAllSegments.setter
    def ShowAllSegments(self, ShowAllSegments):
        self._ShowAllSegments = ShowAllSegments


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ShowAllSegments = params.get("ShowAllSegments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _DataId: 审核时传入的数据Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param _BizType: 业务类型，用于调用识别策略模板；
（暂未发布功能，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param _Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: 查询内容审核任务的状态，可选值：
FINISH 已完成
PENDING 等待中
RUNNING 进行中
ERROR 出错
CANCELLED 已取消
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Type: 任务类型：可选AUDIO（点播音频），LIVE_AUDIO（直播音频）
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Suggestion: 智能审核服务对于内容违规类型的等级，可选值：
Pass 建议通过；
Reveiw 建议复审；
Block 建议屏蔽；
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Labels: 智能审核服务对于内容违规类型的判断，详见返回值列表
如：Label：Porn（色情）；
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param _MediaInfo: 传入媒体的解码信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.ams.v20200608.models.MediaInfo`
        :param _InputInfo: 审核任务的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.ams.v20200608.models.InputInfo`
        :param _CreatedAt: 审核任务的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 审核任务的更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _TryInSeconds: 在N秒后重试
注意：此字段可能返回 null，表示取不到有效值。
        :type TryInSeconds: int
        :param _AudioSegments: 视频/音频审核中的音频结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioSegments: list of AudioSegments
        :param _ImageSegments: 视频审核中的图片结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSegments: list of ImageSegments
        :param _AudioText: 音频识别总文本
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioText: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._DataId = None
        self._BizType = None
        self._Name = None
        self._Status = None
        self._Type = None
        self._Suggestion = None
        self._Labels = None
        self._MediaInfo = None
        self._InputInfo = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._TryInSeconds = None
        self._AudioSegments = None
        self._ImageSegments = None
        self._AudioText = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def MediaInfo(self):
        return self._MediaInfo

    @MediaInfo.setter
    def MediaInfo(self, MediaInfo):
        self._MediaInfo = MediaInfo

    @property
    def InputInfo(self):
        return self._InputInfo

    @InputInfo.setter
    def InputInfo(self, InputInfo):
        self._InputInfo = InputInfo

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def TryInSeconds(self):
        return self._TryInSeconds

    @TryInSeconds.setter
    def TryInSeconds(self, TryInSeconds):
        self._TryInSeconds = TryInSeconds

    @property
    def AudioSegments(self):
        return self._AudioSegments

    @AudioSegments.setter
    def AudioSegments(self, AudioSegments):
        self._AudioSegments = AudioSegments

    @property
    def ImageSegments(self):
        return self._ImageSegments

    @ImageSegments.setter
    def ImageSegments(self, ImageSegments):
        self._ImageSegments = ImageSegments

    @property
    def AudioText(self):
        return self._AudioText

    @AudioText.setter
    def AudioText(self, AudioText):
        self._AudioText = AudioText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DataId = params.get("DataId")
        self._BizType = params.get("BizType")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Suggestion = params.get("Suggestion")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("MediaInfo") is not None:
            self._MediaInfo = MediaInfo()
            self._MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("InputInfo") is not None:
            self._InputInfo = InputInfo()
            self._InputInfo._deserialize(params.get("InputInfo"))
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._TryInSeconds = params.get("TryInSeconds")
        if params.get("AudioSegments") is not None:
            self._AudioSegments = []
            for item in params.get("AudioSegments"):
                obj = AudioSegments()
                obj._deserialize(item)
                self._AudioSegments.append(obj)
        if params.get("ImageSegments") is not None:
            self._ImageSegments = []
            for item in params.get("ImageSegments"):
                obj = ImageSegments()
                obj._deserialize(item)
                self._ImageSegments.append(obj)
        self._AudioText = params.get("AudioText")
        self._RequestId = params.get("RequestId")


class EvilCount(AbstractModel):
    """违规数据分布

    """

    def __init__(self):
        r"""
        :param _EvilType: ----非必选，该参数功能暂未对外开放
        :type EvilType: str
        :param _Count: 分布类型总量
        :type Count: int
        """
        self._EvilType = None
        self._Count = None

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileOutput(AbstractModel):
    """Cos FileOutput

    """

    def __init__(self):
        r"""
        :param _Bucket: 存储的Bucket
        :type Bucket: str
        :param _Region: Cos Region
        :type Region: str
        :param _ObjectPrefix: 对象前缀
        :type ObjectPrefix: str
        """
        self._Bucket = None
        self._Region = None
        self._ObjectPrefix = None

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ObjectPrefix(self):
        return self._ObjectPrefix

    @ObjectPrefix.setter
    def ObjectPrefix(self, ObjectPrefix):
        self._ObjectPrefix = ObjectPrefix


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._ObjectPrefix = params.get("ObjectPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    """

    def __init__(self):
        r"""
        :param _Name: 过滤键的名称。
        :type Name: str
        :param _Values: 一个或者多个过滤值。
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
        


class Filters(AbstractModel):
    """音频过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 查询字段：
策略BizType
子账号SubUin
日期区间DateRange
        :type Name: str
        :param _Values: 查询值
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
        


class ImageResult(AbstractModel):
    """Result结果详情

    """

    def __init__(self):
        r"""
        :param _HitFlag: 违规标志
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Score: 得分
        :type Score: int
        :param _Results: 画面截帧图片结果集
        :type Results: list of ImageResultResult
        :param _Url: 图片URL地址
        :type Url: str
        :param _Extra: 附加字段
        :type Extra: str
        """
        self._HitFlag = None
        self._Suggestion = None
        self._Label = None
        self._Score = None
        self._Results = None
        self._Url = None
        self._Extra = None

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._HitFlag = params.get("HitFlag")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._Score = params.get("Score")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ImageResultResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._Url = params.get("Url")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultResult(AbstractModel):
    """图片输出结果的子结果

    """

    def __init__(self):
        r"""
        :param _Scene: 场景
Porn 色情
Sexy 性感
Abuse 谩骂
Ad 广告
等多个识别场景
注意：此字段可能返回 null，表示取不到有效值。
        :type Scene: str
        :param _HitFlag: 是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _SubLabel: 子标签
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _Score: 分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Names: 如果命中场景为涉政，则该数据为人物姓名列表，否则null
        :type Names: list of str
        :param _Text: 图片OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Details: 其他详情
        :type Details: list of ImageResultsResultDetail
        """
        self._Scene = None
        self._HitFlag = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Names = None
        self._Text = None
        self._Details = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._HitFlag = params.get("HitFlag")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        self._Names = params.get("Names")
        self._Text = params.get("Text")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ImageResultsResultDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultsResultDetail(AbstractModel):
    """具体场景下的图片识别结果

    """

    def __init__(self):
        r"""
        :param _Location: 位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: list of ImageResultsResultDetailLocation
        :param _Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Text: OCR识别文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Label: 标签
        :type Label: str
        :param _LibId: 库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param _LibName: 库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param _Keywords: 命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _Suggestion: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _SubLabelCode: 子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self._Location = None
        self._Name = None
        self._Text = None
        self._Label = None
        self._LibId = None
        self._LibName = None
        self._Keywords = None
        self._Suggestion = None
        self._Score = None
        self._SubLabelCode = None

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def SubLabelCode(self):
        return self._SubLabelCode

    @SubLabelCode.setter
    def SubLabelCode(self, SubLabelCode):
        self._SubLabelCode = SubLabelCode


    def _deserialize(self, params):
        if params.get("Location") is not None:
            self._Location = []
            for item in params.get("Location"):
                obj = ImageResultsResultDetailLocation()
                obj._deserialize(item)
                self._Location.append(obj)
        self._Name = params.get("Name")
        self._Text = params.get("Text")
        self._Label = params.get("Label")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Keywords = params.get("Keywords")
        self._Suggestion = params.get("Suggestion")
        self._Score = params.get("Score")
        self._SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultsResultDetailLocation(AbstractModel):
    """图片详情位置信息

    """

    def __init__(self):
        r"""
        :param _X: x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: float
        :param _Y: y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        :param _Width: 宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Rotate: 旋转角度
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: float
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._Rotate = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Rotate = params.get("Rotate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSegments(AbstractModel):
    """图片段信息

    """

    def __init__(self):
        r"""
        :param _Result: 画面截帧结果详情
        :type Result: :class:`tencentcloud.ams.v20200608.models.ImageResult`
        :param _OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
        :type OffsetTime: str
        """
        self._Result = None
        self._OffsetTime = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def OffsetTime(self):
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ImageResult()
            self._Result._deserialize(params.get("Result"))
        self._OffsetTime = params.get("OffsetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """输入信息详情

    """

    def __init__(self):
        r"""
        :param _Type: 传入的类型可选：URL，COS
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Url: Url地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _BucketInfo: 桶信息。当输入当时COS时，该字段不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketInfo: :class:`tencentcloud.ams.v20200608.models.BucketInfo`
        """
        self._Type = None
        self._Url = None
        self._BucketInfo = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BucketInfo(self):
        return self._BucketInfo

    @BucketInfo.setter
    def BucketInfo(self, BucketInfo):
        self._BucketInfo = BucketInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        if params.get("BucketInfo") is not None:
            self._BucketInfo = BucketInfo()
            self._BucketInfo._deserialize(params.get("BucketInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    """媒体类型

    """

    def __init__(self):
        r"""
        :param _Codecs: 编码格式
        :type Codecs: str
        :param _Duration: 流检测时分片时长
注意：此字段可能返回 0，表示取不到有效值。
        :type Duration: int
        :param _Width: 宽，单位为像素
        :type Width: int
        :param _Height: 高，单位为像素
        :type Height: int
        :param _Thumbnail: 缩略图
        :type Thumbnail: str
        """
        self._Codecs = None
        self._Duration = None
        self._Width = None
        self._Height = None
        self._Thumbnail = None

    @property
    def Codecs(self):
        return self._Codecs

    @Codecs.setter
    def Codecs(self, Codecs):
        self._Codecs = Codecs

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Thumbnail(self):
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail


    def _deserialize(self, params):
        self._Codecs = params.get("Codecs")
        self._Duration = params.get("Duration")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaModerationConfig(AbstractModel):
    """媒体审核配置

    """

    def __init__(self):
        r"""
        :param _AudioFrequency: 音频截帧频率。默认一分钟
        :type AudioFrequency: int
        :param _ImageFrequency: 图片取帧频率, 单位（秒/帧），默认 5， 可选 1 ～ 300
        :type ImageFrequency: int
        :param _CallbackUrl: 异步回调地址。
        :type CallbackUrl: str
        :param _SegmentOutput: 临时文件存储位置
        :type SegmentOutput: :class:`tencentcloud.ams.v20200608.models.FileOutput`
        :param _UseOCR: 是否使用OCR，默认为true
        :type UseOCR: bool
        :param _UseAudio: 是否使用音频。（音频场景下，该值永远为true）
        :type UseAudio: bool
        """
        self._AudioFrequency = None
        self._ImageFrequency = None
        self._CallbackUrl = None
        self._SegmentOutput = None
        self._UseOCR = None
        self._UseAudio = None

    @property
    def AudioFrequency(self):
        return self._AudioFrequency

    @AudioFrequency.setter
    def AudioFrequency(self, AudioFrequency):
        self._AudioFrequency = AudioFrequency

    @property
    def ImageFrequency(self):
        return self._ImageFrequency

    @ImageFrequency.setter
    def ImageFrequency(self, ImageFrequency):
        self._ImageFrequency = ImageFrequency

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def SegmentOutput(self):
        return self._SegmentOutput

    @SegmentOutput.setter
    def SegmentOutput(self, SegmentOutput):
        self._SegmentOutput = SegmentOutput

    @property
    def UseOCR(self):
        return self._UseOCR

    @UseOCR.setter
    def UseOCR(self, UseOCR):
        self._UseOCR = UseOCR

    @property
    def UseAudio(self):
        return self._UseAudio

    @UseAudio.setter
    def UseAudio(self, UseAudio):
        self._UseAudio = UseAudio


    def _deserialize(self, params):
        self._AudioFrequency = params.get("AudioFrequency")
        self._ImageFrequency = params.get("ImageFrequency")
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("SegmentOutput") is not None:
            self._SegmentOutput = FileOutput()
            self._SegmentOutput._deserialize(params.get("SegmentOutput"))
        self._UseOCR = params.get("UseOCR")
        self._UseAudio = params.get("UseAudio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Overview(AbstractModel):
    """识别结果统计

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总调用量
        :type TotalCount: int
        :param _TotalHour: 总调用时长
        :type TotalHour: int
        :param _PassCount: 通过量
        :type PassCount: int
        :param _PassHour: 通过时长
        :type PassHour: int
        :param _EvilCount: 违规量
        :type EvilCount: int
        :param _EvilHour: 违规时长
        :type EvilHour: int
        :param _SuspectCount: 疑似违规量
        :type SuspectCount: int
        :param _SuspectHour: 疑似违规时长
        :type SuspectHour: int
        """
        self._TotalCount = None
        self._TotalHour = None
        self._PassCount = None
        self._PassHour = None
        self._EvilCount = None
        self._EvilHour = None
        self._SuspectCount = None
        self._SuspectHour = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalHour(self):
        return self._TotalHour

    @TotalHour.setter
    def TotalHour(self, TotalHour):
        self._TotalHour = TotalHour

    @property
    def PassCount(self):
        return self._PassCount

    @PassCount.setter
    def PassCount(self, PassCount):
        self._PassCount = PassCount

    @property
    def PassHour(self):
        return self._PassHour

    @PassHour.setter
    def PassHour(self, PassHour):
        self._PassHour = PassHour

    @property
    def EvilCount(self):
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

    @property
    def EvilHour(self):
        return self._EvilHour

    @EvilHour.setter
    def EvilHour(self, EvilHour):
        self._EvilHour = EvilHour

    @property
    def SuspectCount(self):
        return self._SuspectCount

    @SuspectCount.setter
    def SuspectCount(self, SuspectCount):
        self._SuspectCount = SuspectCount

    @property
    def SuspectHour(self):
        return self._SuspectHour

    @SuspectHour.setter
    def SuspectHour(self, SuspectHour):
        self._SuspectHour = SuspectHour


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalHour = params.get("TotalHour")
        self._PassCount = params.get("PassCount")
        self._PassHour = params.get("PassHour")
        self._EvilCount = params.get("EvilCount")
        self._EvilHour = params.get("EvilHour")
        self._SuspectCount = params.get("SuspectCount")
        self._SuspectHour = params.get("SuspectHour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """数据存储信息

    """

    def __init__(self):
        r"""
        :param _Type: 类型 可选：
URL 资源链接类型
COS 腾讯云对象存储类型
        :type Type: str
        :param _Url: 资源链接
        :type Url: str
        :param _BucketInfo: 腾讯云存储桶信息
        :type BucketInfo: :class:`tencentcloud.ams.v20200608.models.BucketInfo`
        """
        self._Type = None
        self._Url = None
        self._BucketInfo = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BucketInfo(self):
        return self._BucketInfo

    @BucketInfo.setter
    def BucketInfo(self, BucketInfo):
        self._BucketInfo = BucketInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        if params.get("BucketInfo") is not None:
            self._BucketInfo = BucketInfo()
            self._BucketInfo._deserialize(params.get("BucketInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """音视频任务结构

    """

    def __init__(self):
        r"""
        :param _DataId: 数据ID
        :type DataId: str
        :param _Name: 任务名
        :type Name: str
        :param _Input: 任务输入
        :type Input: :class:`tencentcloud.ams.v20200608.models.StorageInfo`
        """
        self._DataId = None
        self._Name = None
        self._Input = None

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._Name = params.get("Name")
        if params.get("Input") is not None:
            self._Input = StorageInfo()
            self._Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLabel(AbstractModel):
    """任务输出标签

    """

    def __init__(self):
        r"""
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Score: 得分，分数是 0 ～ 100
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        """
        self._Label = None
        self._Suggestion = None
        self._Score = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """创建任务时的返回结果

    """

    def __init__(self):
        r"""
        :param _DataId: 请求时传入的DataId
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param _TaskId: TaskId，任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _Code: 错误码。如果code为OK，则表示创建成功，其他则参考公共错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Message: 如果错误，该字段表示错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._DataId = None
        self._TaskId = None
        self._Code = None
        self._Message = None

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._TaskId = params.get("TaskId")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrendCount(AbstractModel):
    """识别量统计

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总调用量
        :type TotalCount: int
        :param _TotalHour: 总调用时长
        :type TotalHour: int
        :param _PassCount: 通过量
        :type PassCount: int
        :param _PassHour: 通过时长
        :type PassHour: int
        :param _EvilCount: 违规量
        :type EvilCount: int
        :param _EvilHour: 违规时长
        :type EvilHour: int
        :param _SuspectCount: 疑似违规量
        :type SuspectCount: int
        :param _SuspectHour: 疑似违规时长
        :type SuspectHour: int
        :param _Date: 日期
        :type Date: str
        """
        self._TotalCount = None
        self._TotalHour = None
        self._PassCount = None
        self._PassHour = None
        self._EvilCount = None
        self._EvilHour = None
        self._SuspectCount = None
        self._SuspectHour = None
        self._Date = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalHour(self):
        return self._TotalHour

    @TotalHour.setter
    def TotalHour(self, TotalHour):
        self._TotalHour = TotalHour

    @property
    def PassCount(self):
        return self._PassCount

    @PassCount.setter
    def PassCount(self, PassCount):
        self._PassCount = PassCount

    @property
    def PassHour(self):
        return self._PassHour

    @PassHour.setter
    def PassHour(self, PassHour):
        self._PassHour = PassHour

    @property
    def EvilCount(self):
        return self._EvilCount

    @EvilCount.setter
    def EvilCount(self, EvilCount):
        self._EvilCount = EvilCount

    @property
    def EvilHour(self):
        return self._EvilHour

    @EvilHour.setter
    def EvilHour(self, EvilHour):
        self._EvilHour = EvilHour

    @property
    def SuspectCount(self):
        return self._SuspectCount

    @SuspectCount.setter
    def SuspectCount(self, SuspectCount):
        self._SuspectCount = SuspectCount

    @property
    def SuspectHour(self):
        return self._SuspectHour

    @SuspectHour.setter
    def SuspectHour(self, SuspectHour):
        self._SuspectHour = SuspectHour

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalHour = params.get("TotalHour")
        self._PassCount = params.get("PassCount")
        self._PassHour = params.get("PassHour")
        self._EvilCount = params.get("EvilCount")
        self._EvilHour = params.get("EvilHour")
        self._SuspectCount = params.get("SuspectCount")
        self._SuspectHour = params.get("SuspectHour")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        